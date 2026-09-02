---
type: Concept
title: Default Site (No Link Access, No HA)
id: skupper-concept-default-site
status: generated
owner: agent
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper
source_paths:
  - internal/kube/site/site.go
  - internal/site/routeraccess.go
  - internal/cmd/skupper/site/nonkube/site_create.go
  - pkg/apis/skupper/v2alpha1/types.go
  - config/crd/bases/skupper_site_crd.yaml
tags:
  - skupper
  - site
  - link-access
  - router-access
  - ingress
  - default
related:
  - skupper-concept-inter-site-link
  - skupper-crd-routeraccesses-skupper-io
timestamp: 2026-08-11T00:00:00Z
---

# Default Site (No Link Access, No HA)

A Skupper **site** created with no extra flags starts in a minimal, passive
state: no HA replicas, no ingress, and — critically — no open router ports for
inbound inter-site connections.  Understanding this baseline is important
because the two ports most commonly associated with Skupper
(`inter-router` 55671 and `edge` 45671) do **not** exist until you explicitly
opt in.

## What "no link access" means at the resource level

The site controller creates a `RouterAccess` resource only when
`Site.Spec.LinkAccess` is set to something other than the empty string or
`"none"`:

```go
// internal/kube/site/site.go
func (s *Site) checkDefaultRouterAccess(ctxt context.Context, site *skupperv2alpha1.Site) error {
    if site.Spec.LinkAccess == "" || site.Spec.LinkAccess == "none" {
        return nil
    }
    // ... creates RouterAccess only when link access is requested
}
```

`LinkAccess` defaults to the empty string in `SiteSpec`:

```go
// pkg/apis/skupper/v2alpha1/types.go
type SiteSpec struct {
    ServiceAccount string            `json:"serviceAccount,omitempty"`
    LinkAccess     string            `json:"linkAccess,omitempty"`
    DefaultIssuer  string            `json:"defaultIssuer,omitempty"`
    Edge           bool              `json:"edge,omitempty"`
    HA             bool              `json:"ha,omitempty"`
    Settings       map[string]string `json:"settings,omitempty"`
}
```

The CLI only sets it to `"default"` when `--enable-link-access` is passed:

```go
// internal/cmd/skupper/site/nonkube/site_create.go
if cmd.linkAccessEnabled {
    siteResource.Spec.LinkAccess = "default"
}
```

So out of the box, `checkDefaultRouterAccess` returns immediately and no
`RouterAccess` object is ever created.

## The two router ports never open by default

The `inter-router` (55671) and `edge` (45671) listener ports are **not** part
of the router's baseline configuration.  The initial router config only
includes internal listeners used for controller-to-router communication:

```go
// internal/kube/site/site.go — initialRouterConfig()
rc.AddListener(qdr.Listener{
    Name: "amqp",
    Host: "localhost",
    Port: 5672,
})
rc.AddListener(qdr.Listener{
    Name:             "amqps",
    Port:             5671,
    SslProfile:       "skupper-local-server",
    SaslMechanisms:   "EXTERNAL",
    AuthenticatePeer: true,
})
```

The `inter-router` and `edge` ports are only added as `qdr.Listener` entries
when a `RouterAccess` object (auto-generated or manually authored) carries
those roles:

```go
// internal/kube/site/site.go — auto-generated RouterAccess roles
Roles: []skupperv2alpha1.RouterAccessRole{
    {Name: "inter-router", Port: 55671},
    {Name: "edge",         Port: 45671},
},
```

The `RouterAccessMap.desiredListeners()` function converts those roles into
actual listeners:

```go
// internal/site/routeraccess.go
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

With no `RouterAccess` objects, `desiredListeners()` returns an empty map and
the router never opens either port — **not just "not exposed externally," but
not listening in any form**.

## What the default site can and cannot do

| Capability | Default site (no link access) |
|---|---|
| Accept inbound links from other sites | ✗ — router ports never opened |
| Originate outbound links to sites that *do* have link access | ✓ — outbound connections don't require a local `RouterAccess` |
| Expose services via Listeners / Connectors | ✓ — once linked via an outbound link |
| Be linked to by an interior router | ✗ |
| Be linked to by an edge router | ✗ |

## Enabling link access

Set `linkAccess` on the `Site` spec to one of the supported values.  The CRD
describes all choices:

| Value | Effect |
|---|---|
| `none` (default) | No inbound linking enabled; no ports opened |
| `default` | Platform default — `route` on OpenShift, `loadbalancer` elsewhere |
| `route` | OpenShift Route |
| `loadbalancer` | Kubernetes LoadBalancer Service |
| `ingress` | Generic Kubernetes Ingress (must be enabled on the controller) |
| `ingress-nginx` | Kubernetes Ingress with NGINX-specific TLS annotations |

Via the CLI:

```sh
skupper site create --enable-link-access
```

Via YAML:

```yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: west
spec:
  linkAccess: default   # opens inter-router and edge ports + creates ingress/LB
```

Setting any value other than `""` or `"none"` causes the site controller to
create a `RouterAccess` with the `inter-router` and `edge` roles, which in
turn causes the router to bind those ports and the platform to expose them
through the chosen ingress mechanism.

## No HA by default

`Site.Spec.HA` also defaults to `false`.  High-availability mode runs two
router replicas; the default single-replica mode is sufficient for
development, testing, and networks where the site is the link initiator
rather than the link target.

## Minimum viable two-site network

In a two-site network **at least one site must have link access enabled**.
The passive (default) site originates the outbound link; the active site
accepts it:

```
Site A (linkAccess: none)    →    Site B (linkAccess: default)
  outbound Link CR                  RouterAccess CR
                                    inter-router port 55671 open
                                    edge port 45671 open
```

Site A sends traffic over the link it initiated; neither site requires both
ends to have link access enabled simultaneously.

## References

- [`RouterAccess` CRD](../human/skupper/config/crd/bases/skupper_routeraccess_crd.yaml)
- [`Site` CRD](../human/skupper/config/crd/bases/skupper_site_crd.yaml)
- [Inter-Site Link concept](./inter-site-link.md)
- `internal/kube/site/site.go` — `checkDefaultRouterAccess`, `initialRouterConfig`
- `internal/site/routeraccess.go` — `desiredListeners`
