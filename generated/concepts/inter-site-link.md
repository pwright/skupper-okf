---
type: Concept
title: Inter-Site Link
id: skupper-concept-inter-site-link
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper
source_paths:
  - human/skupper-docs/input/refdog/concepts/link.md
  - human/skupper-docs/input/kube-cli/site-linking.md
  - human/skupper-docs/input/kube-yaml/site-linking.md
  - human/skupper/config/crd/bases/skupper_link_crd.yaml
  - human/skupper/pkg/nonkube/api/token.go
tags:
  - skupper
  - link
  - site-linking
  - inter-site
  - access-token
  - access-grant
  - mtls
related:
  - skupper-concept-routing-key
  - skupper-crd-links-skupper-io
  - skupper-crd-accessgrants-skupper-io
  - skupper-crd-accesstokens-skupper-io
  - skupper-crd-routeraccesses-skupper-io
decision:
  setupStep:
    - decide-link-access
    - join-sites
  platform:
    - kubernetes
    - openshift
    - podman
    - docker
    - linux
  joinMethod:
    - cli-token
    - access-grant-token
timestamp: 2026-08-11T17:21:39Z
---

# Inter-Site Link

An **inter-site link** is a mutual TLS channel between two Skupper sites that
carries all application connections and requests across the network. A set of
linked sites forms an **application network**. Services exposed on any site
are reachable from every other site in the network, regardless of whether the
sites are linked directly.

## Relationship to routing keys

A link is a transport-layer channel; it is distinct from the
[routing key](./routing-key.md) used to route application traffic. Routing keys
identify which listeners and connectors belong together. Links provide the
underlay over which that matched traffic flows. Without at least one active
link between sites, routing-key reachability information cannot propagate and
no cross-site traffic can flow.

## Link model

```text
Site A                         Site B
──────────────────             ──────────────────
 RouterAccess (listening)  ←── Link (connecting)
   port: 55671 (inter-router)
   port: 45671 (edge)
```

The **listening site** exposes a `RouterAccess` endpoint. The **connecting
site** holds a `Link` resource pointing at that endpoint. Link direction is
not significant for traffic — application connections flow both ways.
Direction is typically chosen by network topology (e.g. the site behind a
firewall initiates outward).

## Resources involved

| Resource | Role |
|---|---|
| `RouterAccess` | Exposes an external TLS endpoint that accepts incoming links |
| `AccessGrant` | Permission on the listening site allowing tokens to be issued |
| `AccessToken` | Short-lived credential exchanged for a `Link` on the connecting site |
| `Link` | The active inter-site channel; holds endpoints and TLS credentials |

## Linking with a token (CLI)

Token-based linking is the standard introductory path.

**On the listening site** — enable link access and issue a token:

```bash
skupper site update --enable-link-access
skupper token issue west.yaml
```

> ⚠️ The token file grants access to the application network. Transfer it
> securely. By default it expires after 15 minutes and can only be redeemed
> once.

**On the connecting site** — redeem the token:

```bash
skupper token redeem west.yaml
skupper link status
```

## Linking with YAML (Kubernetes)

**On the listening site** (`west` namespace):

```yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: west
  namespace: west
spec:
  linkAccess: default
---
apiVersion: skupper.io/v2alpha1
kind: AccessGrant
metadata:
  name: grant-west
spec:
  redemptionsAllowed: 1
  expirationWindow: 15m
```

Populate the token from grant status:

```bash
URL="$(kubectl get accessgrant grant-west -o template --template '{{ .status.url }}')"
CODE="$(kubectl get accessgrant grant-west -o template --template '{{ .status.code }}')"
CA_RAW="$(kubectl get accessgrant grant-west -o template --template '{{ .status.ca }}')"
```

Create and transfer the `AccessToken` YAML, then **on the connecting site**:

```bash
kubectl apply -f token.yaml
kubectl get accesstokens   # status should show Redeemed: true
kubectl get links          # status should show Ready
```

## Link resource structure

A redeemed token produces a `Link` resource like:

```yaml
apiVersion: skupper.io/v2alpha1
kind: Link
metadata:
  name: link-west
spec:
  endpoints:
    - name: inter-router
      host: remote-site.example.com
      port: "55671"
    - name: edge
      host: remote-site.example.com
      port: "45671"
  tlsCredentials: link-west   # name of the mTLS Secret
  cost: 1
```

All traffic over a link is protected by mutual TLS using a private, dedicated
certificate authority managed by Skupper. The `tlsCredentials` field names the
Kubernetes `Secret` (or `input/certs/` directory on non-Kubernetes systems)
that contains the client certificate, key, and trusted CA.

## Link cost

`spec.cost` is a positive integer (default `1`) that influences routing
decisions when multiple paths exist. Lower cost paths are preferred. A common
pattern is a local-primary / remote-backup pair:

```yaml
spec:
  cost: 99999   # backup site link — only used when primary is unreachable
```

Cost is per-link and applies to **all** services traversing it. For
per-service traffic shaping use a `MultiKeyListener` instead.

## Status conditions

| Condition | Meaning |
|---|---|
| `Configured` | Link configuration applied to the router |
| `Operational` | Active mTLS connection to the remote site established |
| `Ready` | All conditions true; link is ready for traffic |

```bash
kubectl get links
# NAME          STATUS   REMOTE SITE   MESSAGE
# link-west     Ready    west          OK
```

## References

- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Site linking with CLI (Kubernetes)](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Site linking with YAML (Kubernetes)](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [Link CRD](../skupper/skupper-crd-links-skupper-io.md)
- [AccessToken CRD](../skupper/skupper-crd-accesstokens-skupper-io.md)
- [AccessGrant CRD](../skupper/skupper-crd-accessgrants-skupper-io.md)

## Inter-site link — consolidated summary

**What a link is**

A link is the secure, TLS-authenticated channel connecting two Skupper sites. Links carry application connections and requests, and a set of linked sites forms the network [1](#4-0) . It's represented by a `Link` custom resource, which specifies remote connection `endpoints` (host/port pairs) and `tlsCredentials` for mutual TLS [2](#4-1) . Links usually aren't created directly — a site issues an `AccessToken`, which the other site redeems, and the controller creates the `Link` resource [3](#4-2) .

**Two layers to keep separate**

1. **Site mode (`interior` vs `edge`)** — a site-wide property, set via `Site.Spec.Edge`:
   ```yaml
   edge:
     type: boolean
     description: |-
       Advanced. Configure the site to operate in edge mode. Edge
       sites cannot accept links from remote sites.
   ``` [4](#4-3) 

   This translates to the router's actual `mode`: `interior` or `edge` [5](#4-4) , exposed via `Site.isEdge()`/`routerMode()` [6](#4-5) .
   - **Interior**: full mesh participant, knows the whole topology, can relay traffic, can accept incoming links.
   - **Edge**: a leaf site with a single outbound uplink; cannot accept links from other sites. Meant to help scale beyond ~16 sites, with little benefit below that.

2. **Port role (`inter-router` vs `edge`)** — the two listener ports a link-accepting site opens, unrelated to that site's own mode. Any site with link access enabled opens *both*:
   ```go
   Roles: []skupperv2alpha1.RouterAccessRole{
       {Name: "inter-router", Port: 55671},
       {Name: "edge",         Port: 45671},
   },
   ``` [7](#4-6) 
   These become actual router listeners via `desiredListeners()` [8](#4-7) , and correspond to the underlying `qdr.RoleInterRouter`/`qdr.RoleEdge` connector roles [9](#4-8) .

**How the two layers interact when a link forms**

The *connecting* side picks exactly one port based on its own mode:
```go
role := qdr.RoleInterRouter
if current.IsEdge() {
    role = qdr.RoleEdge
}
endpoint, ok := l.definition.Spec.GetEndpointForRole(string(role))
``` [10](#4-9) 

So:
- Interior site dialing out → always uses the remote's `inter-router` port.
- Edge site dialing out → always uses the remote's `edge` port (and per the CRD note, edge sites don't accept inbound links themselves).
- A link-accepting interior site keeps both ports open simultaneously, since it can't know in advance whether an inbound peer is interior or edge.

**CLI/controller touchpoints**

- `skupper link` command group (generate/update/status/delete) manages links from the CLI [11](#4-10) .
- The site controller (`internal/kube/site/site.go`) maintains a map of `Link` objects and applies them to router config via `s.link()`/`CheckLink()`, deferring configuration if TLS credentials aren't ready yet [12](#4-11) .
- `Link` status conditions (`Configured`, `Operational`, `Ready`) and `remoteSiteId`/`remoteSiteName` report whether the link is actually up [13](#4-12) .

**One-paragraph takeaway**

An inter-site link is a mTLS connection between two sites' routers. Whether a site can act as a full mesh member or only a leaf is determined by its `interior`/`edge` *mode*; separately, any site accepting links opens two ports (`inter-router` 55671, `edge` 45671) so that both interior peers and edge leaves have a matching door to connect through — the connecting site's own mode decides which of those two ports it dials.

### Citations

**File:** config/crd/bases/skupper_link_crd.yaml (L13-59)
```yaml
          description: |-
            A link is a channel for communication between sites.
            Links carry application connections and requests.  A set of linked
            sites constitutes a network.

            A Link resource specifies remote connection endpoints and TLS
            credentials for establishing a mutual TLS connection to a remote
            site.  To create an active link, the remote site must first enable
            _link access_.  Link access provides an external access point for
            accepting links.

            **Note:** Links are not usually created directly.  Instead, you can
            use an AccessToken to obtain a link.
          type: object
          properties:
            spec:
              type: object
              properties:
                endpoints:
                  description : |-
                    An array of connection endpoints. Each item has a name, host,
                    port, and group.
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                      host:
                        type: string
                      port:
                        type: string
                      group:
                        type: string
                tlsCredentials:
                  description: |-
                    The name of a bundle of certificates used for mutual TLS
                    router-to-router communication.  The bundle contains the
                    client certificate and key and the trusted server certificate
                    (usually a CA).

                    On Kubernetes, the value is the name of a Secret in the
                    current namespace.

                    On Docker, Podman, and Linux, the value is the name of a
                    directory under `input/certs/` in the current namespace.
                  type: string
```

**File:** config/crd/bases/skupper_link_crd.yaml (L76-105)
```yaml
            status:
              type: object
              properties:
                status:
                  description: |-
                    The current state of the resource.
                    - `Pending`: The resource is being processed.
                    - `Error`: There was an error processing the resource. See `message` for more information.
                    - `Ready`: The resource is ready to use.
                  type: string
                message:
                  description: |-
                    A human-readable status message. Error messages are reported here.
                  type: string
                remoteSiteId:
                  description: |-
                    The unique ID of the site linked to.
                  type: string
                remoteSiteName:
                  description: |-
                    The name of the site linked to.
                  type: string
                conditions:
                  type: array
                  description: |-
                    A set of named conditions describing the current state of the resource.

                    - `Configured`: The link configuration has been applied to the router.
                    - `Operational`: The link to the remote site is active.
                    - `Ready`: The link is ready for use. All other conditions are true.
```

**File:** config/crd/bases/skupper_site_crd.yaml (L69-79)
```yaml
                edge:
                  type: boolean
                  description: |-
                    Advanced. Configure the site to operate in edge mode. Edge
                    sites cannot accept links from remote sites.

                    Edge mode can help you scale your network to large numbers
                    of sites. However, for networks with 16 or fewer sites,
                    there is little benefit.

                    Currently, edge sites cannot also have HA enabled.
```

**File:** internal/qdr/qdr.go (L430-437)
```go
type Role string

const (
	RoleInterRouter Role = "inter-router"
	RoleEdge             = "edge"
	RoleNormal           = "normal"
	RoleDefault          = ""
)
```

**File:** internal/qdr/qdr.go (L461-466)
```go
type Mode string

const (
	ModeInterior Mode = "interior"
	ModeEdge          = "edge"
)
```

**File:** internal/kube/site/site.go (L181-191)
```go
func (s *Site) isEdge() bool {
	return s.routerMode() == qdr.ModeEdge
}

func (s *Site) routerMode() qdr.Mode {
	if s.site != nil && s.site.Spec.Edge {
		return qdr.ModeEdge
	} else {
		return qdr.ModeInterior
	}
}
```

**File:** internal/kube/site/site.go (L381-420)
```go
func (s *Site) checkDefaultRouterAccess(ctxt context.Context, site *skupperv2alpha1.Site) error {
	if site.Spec.LinkAccess == "" || site.Spec.LinkAccess == "none" {
		return nil
	}
	name := "skupper-router"
	accessType := site.Spec.LinkAccess
	if site.Spec.LinkAccess == "default" {
		accessType = ""
	}
	current, ok := s.linkAccess[name]
	desired := &skupperv2alpha1.RouterAccess{
		TypeMeta: metav1.TypeMeta{
			APIVersion: "skupper.io/v2alpha1",
			Kind:       "RouterAccess",
		},
		ObjectMeta: metav1.ObjectMeta{
			Name:            name,
			OwnerReferences: s.ownerReferences(),
			Annotations: map[string]string{
				"internal.skupper.io/controlled": "true",
			},
		},
		Spec: skupperv2alpha1.RouterAccessSpec{
			AccessType:             accessType,
			TlsCredentials:         "skupper-site-server",
			Issuer:                 "skupper-site-ca", //TODO: can rely ondefault here
			GenerateTlsCredentials: true,
			Roles: []skupperv2alpha1.RouterAccessRole{
				{
					Name: "inter-router",
					Port: 55671,
				},
				{
					Name: "edge",
					Port: 45671,
				},
			},
			Settings: routerAccessSettingsMerge(site, current),
		},
	}
```

**File:** internal/kube/site/site.go (L1299-1345)
```go
func (s *Site) CheckLink(name string, linkconfig *skupperv2alpha1.Link) error {
	s.logger.Debug("checkLink",
		slog.String("name", name))
	if linkconfig == nil {
		return s.unlink(name)
	}
	return s.link(linkconfig)
}

func (s *Site) link(linkconfig *skupperv2alpha1.Link) error {
	var config *site.Link
	prevProxyProfileName := ""
	currentProxyProfileName := linkconfig.Spec.GetProxyConfiguration()
	if existing, ok := s.links[linkconfig.ObjectMeta.Name]; ok {
		prevProxyProfileName = existing.Definition().Spec.GetProxyConfiguration()
		if existing.Update(linkconfig) || !existing.Definition().IsConfigured() {
			config = existing
		}
	} else {
		config, err := s.newLink(linkconfig)
		if err == nil {
			s.links[linkconfig.ObjectMeta.Name] = config
		} else {
			return s.updateLinkConfiguredCondition(linkconfig, err)
		}
	}
	if s.initialised {
		if config != nil {
			s.logger.Info("Connecting site using token",
				slog.String("namespace", s.namespace),
				slog.String("token", linkconfig.ObjectMeta.Name))
			if currentProxyProfileName != "" && prevProxyProfileName != "" && currentProxyProfileName != prevProxyProfileName {
				currentProxyConfig, err := s.getProxyConfig(currentProxyProfileName)
				if err == nil {
					config.UpdateProxyConfig(currentProxyConfig)
				}
			}
			if tlsErr := s.missingTlsCredentialsErr(linkconfig.Spec.TlsCredentials); tlsErr != nil {
				s.logger.Info("Deferring link router configuration until TLS credentials secret exists",
					slog.String("namespace", s.namespace),
					slog.String("link", linkconfig.Name),
					slog.String("secret", linkconfig.Spec.TlsCredentials),
				)
				return s.updateLinkConfiguredCondition(linkconfig, tlsErr)
			}
			err := s.updateRouterConfig(config)
			return s.updateLinkConfiguredCondition(linkconfig, err)
```

**File:** internal/site/routeraccess.go (L12-29)
```go
func (m RouterAccessMap) desiredListeners() map[string]qdr.Listener {
	desired := map[string]qdr.Listener{}
	for _, ra := range m {
		for _, role := range ra.Spec.Roles {
			name := ra.Name + "-" + role.Name
			desired[name] = qdr.Listener{
				Name:             name,
				Role:             qdr.GetRole(role.Name),
				Host:             ra.Spec.BindHost,
				Port:             role.GetPort(),
				SslProfile:       ra.Spec.TlsCredentials,
				SaslMechanisms:   "EXTERNAL",
				AuthenticatePeer: true,
			}
		}
	}
	return desired
}
```

**File:** internal/site/link.go (L41-52)
```go
func (l *Link) Apply(current *qdr.RouterConfig) bool {
	if l.definition == nil {
		return false
	}
	role := qdr.RoleInterRouter
	if current.IsEdge() {
		role = qdr.RoleEdge
	}
	endpoint, ok := l.definition.Spec.GetEndpointForRole(string(role))
	if !ok {
		return false
	}
```

**File:** internal/cmd/skupper/link/link.go (L13-21)
```go
func NewCmdLink() *cobra.Command {

	cmd := &cobra.Command{
		Use:   "link",
		Short: "A site-to-site communication channel",
		Long:  `A site-to-site communication channel. Links serve as a transport for application connections and requests. A set of linked sites constitute a network.`,
		Example: `skupper link generate
skupper link status`,
	}
```
