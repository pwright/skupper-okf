---
type: Concept
title: Certificate Manager
id: skupper-concept-certificate-manager
status: generated
owner: agent
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper
source_paths:
  - internal/kube/certificates/mgr.go
  - internal/kube/certificates/ownermappings.go
tags:
  - skupper
  - certificate
  - tls
  - mtls
  - pki
  - secret
related:
  - skupper-concept-site-controller
  - skupper-concept-secured-access
  - skupper-concept-kube-adaptor
  - skupper-crd-certificates-skupper-io
timestamp: 2026-08-11T00:00:00Z
---

# Certificate Manager

The **Certificate Manager** (`internal/kube/certificates`) is the PKI subsystem embedded in the site controller. It reconciles `Certificate` custom resources into Kubernetes `Secret` objects containing the actual TLS key material, and keeps those secrets up to date as certificate specs change.

> **Not cert-manager.** This is _not_ [cert-manager.io](https://cert-manager.io/) and has no dependency on it. Skupper's Certificate Manager is a small, self-contained Go package that generates key material directly using the `internal/certs` library. It does not require any cluster-level operator, `Issuer`, `ClusterIssuer`, or `CertificateRequest` CR from the cert-manager project. If you are already running cert-manager in your cluster you can still use Skupper — the two systems are completely independent.

## Role in the system

Every mTLS connection in Skupper is backed by a Kubernetes Secret. The Certificate Manager is the single component responsible for creating and rotating those secrets. Other components — the site reconciler, the `SecuredAccess` manager, the grant server — declare what certificates they need by calling `EnsureCA` or `Ensure`; the Certificate Manager handles the rest.

```
CertificateManager.EnsureCA("skupper-site-ca", …)
        ↓ creates
Certificate CR  (Spec.Signing=true)
        ↓ reconcileSecret
Kubernetes Secret  (CA cert + key)

CertificateManager.Ensure("skupper-local", ca="skupper-site-ca", hosts=[…], …)
        ↓ creates
Certificate CR  (Spec.Ca="skupper-site-ca", Spec.Hosts=[…])
        ↓ reconcileSecret (signs with CA secret)
Kubernetes Secret  (leaf cert + key)
```

## `CertificateManager` interface

The public API is narrow and intentional:

```go
// internal/kube/certificates/mgr.go
type CertificateManager interface {
    EnsureCA(namespace, name, subject string, refs []metav1.OwnerReference) error
    Ensure(namespace, name, ca, subject string, hosts []string, client, server bool, refs []metav1.OwnerReference) error
}
```

- **`EnsureCA`** creates a self-signed CA certificate (`Spec.Signing = true`). Used to bootstrap the site CA (`skupper-site-ca`) and the local CA (`skupper-local-ca`).
- **`Ensure`** creates a leaf certificate signed by the named CA. Used for router ports (inter-router, edge), client credentials (links), and service certs.

Both methods are idempotent: if the `Certificate` CR already exists, they diff the spec and only update if something changed.

## Internal reconcile flow

```
Certificate CR change
        ↓ checkCertificate()
    [controlled?]
    ├─ YES: merge owner-reference metadata, check for stale per-owner hosts
    └─ reconcileSecret()
           ├─ secret exists?
           │   ├─ NO  → createSecret() → generateSecret() → Kubernetes Create
           │   └─ YES → isSecretCorrect()?
           │           ├─ YES → check labels/annotations only
           │           └─ NO  → generateSecret() → Kubernetes Update
           └─ updateStatus(certificate, err)
```

### `generateSecret`

For CA certificates (`Spec.Signing = true`), a self-signed CA is generated with no expiry:

```go
// internal/kube/certificates/mgr.go
if certificate.Spec.Signing {
    secret, err = certs.GenerateSecret(certificate.Name, certificate.Spec.Subject, nil, 0, nil)
```

For leaf certificates, it looks up the CA secret by key `namespace/caName` and signs with it:

```go
} else {
    expiration := time.Hour * 24 * 365 * 5   // 5-year leaf cert lifetime
    ca, ok := m.secrets[caKey]
    secret, err = certs.GenerateSecret(certificate.Name, certificate.Spec.Subject, certificate.Spec.Hosts, expiration, ca)
}
```

### Detecting stale secrets

`isSecretCorrect` checks that the hosts encoded in the secret's annotation `internal.skupper.io/hosts` match the Certificate spec. If the hosts change (e.g. a new `Route` hostname resolves), the cert is regenerated and the Secret updated.

## Multi-owner host merging

A single `Certificate` can be co-owned by multiple Skupper resources (e.g. two `Route` objects with different hostnames both needing the same cert). The Certificate Manager tracks per-owner host sets in annotation metadata:

```
internal.skupper.io/owner-hosts = {"uid1": ["host-a"], "uid2": ["host-b"]}
```

`Ensure` is called once per owner. The combined host list (`host-a`, `host-b`) is written to `Spec.Hosts`. When an owner's UID disappears from `OwnerReferences`, its host entries are pruned and the cert is re-issued with the reduced list.

## Recovery at startup

`Recover()` is called during the controller's `init` phase. It iterates all existing `Certificate` and `Secret` resources in the watched namespace and populates the in-memory `definitions` and `secrets` maps. Any `Certificate` that is missing its corresponding `Secret` triggers `reconcileSecret` immediately.

```go
// internal/kube/certificates/mgr.go
func (m *CertificateManagerImpl) Recover() {
    for _, secret := range m.secretWatcher.List() { ... m.secrets[...] = secret }
    for _, cert := range m.certificateWatcher.List() {
        m.checkCertificate(cert.Key(), cert)
    }
}
```

## Certificates created for a default site

Even a site with `linkAccess: none` (the default) gets certificates created by the Certificate Manager:

| Certificate name | Type | Purpose |
|---|---|---|
| `skupper-site-ca` | CA | Root CA for the site; used to issue all other certs |
| `skupper-local-ca` | CA | Issuer for the internal `amqps` listener |
| `skupper-local` | leaf | Server cert for `amqps` (controller ↔ router) |
| `skupper-local-client` | leaf | Client cert for the kube-adaptor's AMQP connection |

When link access is enabled, additional certs are issued per `RouterAccess` for the `inter-router` and `edge` ports.

## Integration with kube-adaptor

The kube-adaptor's `secrets.Sync` watches all Secrets in the namespace and detects when a certificate-backed Secret changes (identified by the `internal.skupper.io/certificate` annotation). On change it re-runs the `configEvent` pipeline, writing updated PEM files to disk and pushing the new SSL profile to the live router. See [Kube Adaptor](./kube-adaptor.md).

## References

- [`internal/kube/certificates/mgr.go`](../human/skupper/internal/kube/certificates/mgr.go)
- [`internal/kube/certificates/ownermappings.go`](../human/skupper/internal/kube/certificates/ownermappings.go)
- [Site Controller concept](./site-controller.md)
- [Kube Adaptor concept](./kube-adaptor.md)
- [SecuredAccess concept](./secured-access.md)
