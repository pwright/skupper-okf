---
type: Concept
title: Access Grants and Tokens
id: skupper-concept-access-grants-and-tokens
status: generated
owner: agent
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper
source_paths:
  - internal/kube/grants/grants.go
  - internal/kube/grants/redeem.go
  - internal/kube/grants/tokens.go
  - internal/kube/grants/init.go
  - internal/kube/grants/enabled.go
  - internal/kube/grants/server.go
tags:
  - skupper
  - access-grant
  - access-token
  - link
  - tls
  - token-exchange
related:
  - skupper-concept-inter-site-link
  - skupper-concept-default-site
  - skupper-concept-site-controller
  - skupper-concept-certificate-manager
  - skupper-crd-accessgrants-skupper-io
  - skupper-crd-accesstokens-skupper-io
timestamp: 2026-08-11T00:00:00Z
---

# Access Grants and Tokens

Skupper uses a **claim-based token exchange** to connect two sites without requiring network connectivity in both directions simultaneously. One site creates an `AccessGrant` (the offer), and the other creates an `AccessToken` (the claim). When the token is redeemed, the controller automatically creates the `Secret` and `Link` CRs that establish the mTLS inter-site connection.

## Prerequisites

Token exchange only works when **at least one site has link access enabled**. The grant server runs on the site with link access, and the token-redeeming site makes an HTTPS POST to that server. A default site with `linkAccess: none` cannot be the grant-issuing side. See [Default Site](./default-site.md).

## The two-sided ceremony

```
Site A (link access enabled)          Site B (no link access required)
─────────────────────────────         ────────────────────────────────
1. Create AccessGrant CR              
   └─ controller sets:
      status.Url   = https://<host>/<uid>
      status.Ca    = <PEM of site CA>
      status.Code  = <random 24-char token>
      
2. Share Url, Ca, Code out-of-band ──→

                                      3. Create AccessToken CR with:
                                         spec.Url  = status.Url from A
                                         spec.Ca   = status.Ca  from A
                                         spec.Code = status.Code from A

                                      4. controller calls RedeemAccessToken():
                                         - HTTPS POST to spec.Url
                                           body: spec.Code
                                           header name: token name
                                           header subject: site UID

5. Grant server (Site A) validates:
   - code matches
   - not expired
   - redemptions not exceeded
   - generates cert token (Secret + Link YAML)
   - responds with YAML body

                                      6. controller decodes response:
                                         - creates Secret (TLS creds)
                                         - creates Link CR → inter-site link established
```

## Grant server (`internal/kube/grants`)

The grant server is an HTTP handler (`Grants.ServeHTTP`) embedded in the site controller. It is only started when the grants feature is enabled (`config.Enabled`) and runs on a `SecuredAccess`-managed HTTPS endpoint.

### `AccessGrant` reconciliation

When an `AccessGrant` CR is created or updated, `checkGrant` runs:

```go
// internal/kube/grants/grants.go
func (g *Grants) checkGrant(key string, grant *skupperv2alpha1.AccessGrant) error {
    // 1. Default RedemptionsAllowed to 1 if not set
    // 2. Set status.Url = https://<server-url>/<grant.UID>
    // 3. Set status.Ca  = PEM of site CA cert
    // 4. Set status.Code = grant.Spec.Code (or a random 24-char ID)
    // 5. Set status.ExpirationTime = now + Spec.ExpirationWindow (default 10 min)
    // 6. Update status
}
```

The `Url` field uses the grant's Kubernetes UID as the path segment, which means each grant has a unique, unguessable endpoint. The CA PEM is sourced from the site's default issuer secret and included in the grant status so the token holder can pin the server certificate.

### HTTP redemption endpoint

```go
// internal/kube/grants/grants.go
func (g *Grants) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    // POST only
    // key = grant UID from URL path (or namespace/name if keyRedeem is true)
    // body = the secret code
    // validates: grant exists, not expired, redemptions remaining, code matches
    // increments Redemptions counter
    // calls generator(namespace, name, subject, w) → writes YAML to response
}
```

`checkAndUpdateAccessToken` validates the code, expiry, and remaining redemption count atomically before incrementing the counter:

```go
if grant.Spec.RedemptionsAllowed <= grant.Status.Redemptions {
    return nil, httpError("No such access granted", http.StatusNotFound)
}
if grant.Status.Code != string(data) {
    return nil, httpError("Redemption of access token refused", http.StatusForbidden)
}
grant.Status.Redemptions += 1
```

## Token generation (`internal/kube/grants/tokens.go`)

When a redemption request is accepted, the server calls the `generator` callback (provided by the site controller's `generateLinkConfig`), which uses `TokenGenerator`:

```go
// internal/kube/grants/tokens.go
func (g *TokenGenerator) NewCertToken(name string, subject string) (Token, error) {
    cert, _ := certs.GenerateSecret(name, subject, g.hosts, 0, g.ca)
    // For each group of endpoints (HA creates two groups):
    link := &skupperv2alpha1.Link{
        Spec: skupperv2alpha1.LinkSpec{
            Endpoints:      endpoints,   // inter-router + edge for that group
            TlsCredentials: name,        // name of the Secret above
        },
    }
    return &CertToken{tlsCredentials: cert, links: links}, nil
}
```

`TokenGenerator` reads `site.Status.Endpoints` to find all `inter-router` and `edge` endpoints, grouped by HA group. An HA site (two router replicas) produces two `Link` CRs in the token response — one per group — so the connecting site can establish links to both routers.

`CertToken.Write` serialises the `Secret` and each `Link` as YAML separated by `---\n` and writes them to the HTTP response body.

## Token redemption (`internal/kube/grants/redeem.go`)

On the connecting side, when an `AccessToken` CR appears, the site controller calls `RedeemAccessToken`:

```go
// internal/kube/grants/redeem.go
func RedeemAccessToken(token *skupperv2alpha1.AccessToken, site *skupperv2alpha1.Site, clients internalclient.Clients) error {
    transport := &http.Transport{
        TLSClientConfig: tlsConfig(token),   // pins CA from token.Spec.Ca; requires TLS 1.3
    }
    body, err := postTokenRequest(token, site, transport)
    return handleTokenResponse(body, token, site, clients)
}
```

The TLS configuration pins the CA from `token.Spec.Ca` and enforces TLS 1.3 minimum:

```go
func tlsConfig(token *skupperv2alpha1.AccessToken) *tls.Config {
    caPool := x509.NewCertPool()
    caPool.AppendCertsFromPEM([]byte(token.Spec.Ca))
    return &tls.Config{
        RootCAs:    caPool,
        MinVersion: tls.VersionTLS13,
    }
}
```

The POST request carries:
- **Body**: the secret code (`token.Spec.Code`)
- **Header `name`**: the token's Kubernetes name (used to name the created `Secret` and `Link`)
- **Header `subject`**: the connecting site's UID (embedded in the generated certificate's CN)

`handleTokenResponse` decodes the YAML response into a `Secret` and one or more `Link` CRs, then creates them in the connecting site's namespace — both owned by the `Site` CR so they are garbage-collected if the site is deleted:

```go
refs := []metav1.OwnerReference{{
    Kind: "Site", APIVersion: "skupper.io/v2alpha1",
    Name: site.Name, UID: site.ObjectMeta.UID,
}}
clients.GetKubeClient().CoreV1().Secrets(...).Create(ctx, &decoder.secret, ...)
clients.GetSkupperClient().SkupperV2alpha1().Links(...).Create(ctx, &link, ...)
```

Once the `Link` CR exists, the site controller's `CheckLink` handler connects it to the router as an outbound AMQP connector.

## Security properties

| Property | How it is achieved |
|---|---|
| Server authentication | Token holder pins the CA PEM from `status.Ca`; no TOFU |
| Client code verification | Server checks secret code in POST body; 403 on mismatch |
| Expiry | `status.ExpirationTime` checked server-side; default 10 minutes |
| Limited redemptions | `Spec.RedemptionsAllowed` (default 1); counter incremented atomically |
| Transport security | TLS 1.3 minimum enforced in `tlsConfig` |
| URL entropy | Grant UID (Kubernetes UUID) used as path segment — unguessable |

## AccessGrant vs AccessToken

| Resource | Created by | Lives in | Purpose |
|---|---|---|---|
| `AccessGrant` | Operator on site A | Site A namespace | Advertises a claimable URL + CA + code |
| `AccessToken` | Operator on site B | Site B namespace | Triggers redemption; deleted or marked redeemed after use |

A single `AccessGrant` can be redeemed multiple times (up to `RedemptionsAllowed`), enabling a single grant to onboard multiple connecting sites.

## References

- [`internal/kube/grants/grants.go`](../human/skupper/internal/kube/grants/grants.go)
- [`internal/kube/grants/redeem.go`](../human/skupper/internal/kube/grants/redeem.go)
- [`internal/kube/grants/tokens.go`](../human/skupper/internal/kube/grants/tokens.go)
- [Inter-Site Link concept](./inter-site-link.md)
- [Site Controller concept](./site-controller.md)
- [Default Site concept](./default-site.md)
