---
type: Concept
title: SecuredAccess
id: skupper-concept-secured-access
status: generated
owner: agent
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper
source_paths:
  - internal/kube/securedaccess/access.go
  - internal/kube/securedaccess/config.go
  - internal/kube/securedaccess/loadbalancer.go
  - internal/kube/securedaccess/route.go
  - internal/kube/securedaccess/ingress.go
  - internal/kube/securedaccess/nodeport.go
  - internal/kube/securedaccess/gateway.go
  - internal/kube/securedaccess/local.go
tags:
  - skupper
  - secured-access
  - ingress
  - loadbalancer
  - route
  - tls
  - link-access
related:
  - skupper-concept-default-site
  - skupper-concept-site-controller
  - skupper-concept-certificate-manager
  - skupper-crd-routeraccesses-skupper-io
  - skupper-crd-securedaccesses-skupper-io
timestamp: 2026-08-11T00:00:00Z
---

# SecuredAccess

**SecuredAccess** is Skupper's platform-abstraction layer for exposing the router's `inter-router` and `edge` ports to the outside world. It translates a single `SecuredAccess` CR into the platform-specific resources — Service, Route, Ingress, LoadBalancer, or Gateway — that make the router reachable from remote sites.

## The chain: `linkAccess` → `RouterAccess` → `SecuredAccess`

Enabling link access on a site triggers a three-step resource chain:

```
Site.Spec.LinkAccess = "default"
        ↓ site controller: checkDefaultRouterAccess()
RouterAccess CR
  (roles: inter-router:55671, edge:45671)
        ↓ site controller: CheckRouterAccess() → asSecuredAccessSpec()
SecuredAccess CR
  (ports: inter-router, edge; accessType from linkAccess value)
        ↓ SecuredAccessManager.reconcile()
Kubernetes Service  +  Route / Ingress / LB / Gateway
        ↓ endpoints resolved into
Site.Status.Endpoints[]
```

The site controller calls `SecuredAccessManager.Ensure(...)` when it processes a `RouterAccess`, which creates or updates the `SecuredAccess` CR. The `SecuredAccessManager` then reconciles that CR into the appropriate platform resources.

## Access types

The `SecuredAccessManager` is configured with a set of **enabled access types** at startup. The default set (absent explicit configuration) is:

```go
// internal/kube/securedaccess/config.go
func defaultEnabledAccessTypes() []string {
    return []string{"local", "loadbalancer", "route"}
}
```

The full set of supported types and their implementations:

| Access type constant | Kubernetes resource created | Notes |
|---|---|---|
| `route` | OpenShift `Route` (TLS passthrough) | Auto-selected as default when OpenShift route client is available |
| `loadbalancer` | `Service` of type `LoadBalancer` | Default on non-OpenShift if route is unavailable |
| `ingress` | `Ingress` (generic controller) | Requires `SKUPPER_INGRESS_DOMAIN` to be set |
| `ingress-nginx` | `Ingress` with NGINX TLS annotations | Requires `SKUPPER_INGRESS_DOMAIN`; defaults `ingressClassName` to `"nginx"` |
| `contour-http-proxy` | Contour `HTTPProxy` | Requires `SKUPPER_HTTP_PROXY_DOMAIN` |
| `gateway` | Gateway API `TLSRoute` | Requires `SKUPPER_GATEWAY_CLASS` and `SKUPPER_GATEWAY_PORT` |
| `nodeport` | `Service` of type `NodePort` | Requires `SKUPPER_CLUSTER_HOST` |
| `local` | `Service` of type `ClusterIP` | In-cluster only; used for local access patterns |

The default access type is resolved at startup:

```go
// internal/kube/securedaccess/config.go
func (c *Config) getDefaultAccessType(clients internalclient.Clients) string {
    if c.DefaultAccessType == "" {
        if clients.GetRouteClient() != nil && c.isEnabled(ACCESS_TYPE_ROUTE) {
            return ACCESS_TYPE_ROUTE   // OpenShift: prefer route
        }
        if c.isEnabled(ACCESS_TYPE_LOADBALANCER) {
            return ACCESS_TYPE_LOADBALANCER
        }
        if len(c.EnabledAccessTypes) > 0 {
            return c.EnabledAccessTypes[0]
        }
    }
    return c.DefaultAccessType
}
```

## SecuredAccessManager internals

`SecuredAccessManager` maintains in-memory maps of all owned resources, populated during recovery at startup:

```go
type SecuredAccessManager struct {
    definitions map[string]*skupperv2alpha1.SecuredAccess
    services    map[string]*corev1.Service
    routes      map[string]*routev1.Route
    ingresses   map[string]*networkingv1.Ingress
    httpProxies map[string]*unstructured.Unstructured
    tlsRoutes   map[string]*unstructured.Unstructured
    ...
}
```

### Reconcile flow

On each `SecuredAccess` change, `reconcile` runs a two-step process:

```go
// internal/kube/securedaccess/access.go
func (m *SecuredAccessManager) reconcile(sa *skupperv2alpha1.SecuredAccess) error {
    svc, err := m.checkService(sa)        // 1. ensure Service exists and is correct
    endpoints, resourceErr := m.accessType(sa).RealiseAndResolve(sa, svc)  // 2. platform resource
    certErr := m.checkCertificate(sa)     // 3. ensure TLS certificate
    sa.SetResolved(endpoints)             // 4. write resolved endpoints to status
    sa.SetConfigured(errors.Join(resourceErr, certErr))
    return m.updateStatus(sa)
}
```

**Step 1 — Service**: every access type gets a Kubernetes Service as a backing resource. `checkService` creates or updates it with the correct `type` (ClusterIP, LoadBalancer, NodePort), selector, and ports.

**Step 2 — Platform resource**: each `AccessType` implements `RealiseAndResolve(access, service) ([]Endpoint, error)`. It creates or reconciles the platform-specific object (Route, Ingress, etc.) and returns the resolved external endpoints (hostname/IP + port).

**Step 3 — Certificate**: if `sa.Spec.Issuer` is set, `checkCertificate` calls `certMgr.Ensure(...)` to issue a TLS certificate for the resolved hosts. This is the server certificate used for mTLS on the router ports.

**Step 4 — Status**: resolved endpoints are written to `SecuredAccess.Status.Endpoints` and propagated up to `Site.Status.Endpoints` by the site controller.

### The `AccessType` interface

Each platform implementation satisfies one method:

```go
type AccessType interface {
    RealiseAndResolve(access *skupperv2alpha1.SecuredAccess, service *corev1.Service) ([]skupperv2alpha1.Endpoint, error)
}
```

The implementation is responsible for creating or updating the platform object and returning the resolved external hostname/IP and port that remote sites can connect to.

## Relationship to `RouterAccess`

The `RouterAccess` CR specifies *which* ports to expose and *which* TLS credentials to use. The `SecuredAccess` CR specifies *how* to expose them on the platform. The site controller converts a `RouterAccess` to a `SecuredAccess` spec via `asSecuredAccessSpec`:

```go
// internal/kube/site/site.go (simplified)
func asSecuredAccessSpec(routerAccess *skupperv2alpha1.RouterAccess, group string, defaultIssuer string) skupperv2alpha1.SecuredAccessSpec {
    // maps RouterAccess roles (inter-router, edge) to SecuredAccess ports
    // sets Issuer from routerAccess.Spec.Issuer or site default
    // sets AccessType from routerAccess.Spec.AccessType
    ...
}
```

The name of the `SecuredAccess` CR matches the `RouterAccess` name within the same namespace.

## Recovery

At controller startup, `SecuredAccessResourceWatcher` calls `Recover*` methods to repopulate the in-memory caches from existing Kubernetes resources, before the event loop starts reacting to changes:

```go
// controller init
c.accessRecovery.Recover()
// internally calls:
//   accessMgr.RecoverRoute(route)
//   accessMgr.RecoverIngress(ingress)
//   accessMgr.RecoverService(svc)
//   ...
```

This prevents the manager from re-creating resources that already exist.

## Environment variables / flags

| Flag / Env var | Purpose |
|---|---|
| `SKUPPER_ENABLED_ACCESS_TYPES` | Comma-separated list of allowed access types |
| `SKUPPER_DEFAULT_ACCESS_TYPE` | Override the auto-detected default |
| `SKUPPER_INGRESS_DOMAIN` | Domain suffix for Ingress hostnames |
| `SKUPPER_INGRESS_CLASS_NAME` | Optional `ingressClassName` for Ingress objects |
| `SKUPPER_HTTP_PROXY_DOMAIN` | Domain suffix for Contour HTTPProxy hostnames |
| `SKUPPER_GATEWAY_CLASS` | Gateway API `gatewayClassName` |
| `SKUPPER_GATEWAY_PORT` | Port for Gateway listeners (default 8443) |
| `SKUPPER_GATEWAY_DOMAIN` | Domain suffix for Gateway TLSRoute hostnames |
| `SKUPPER_CLUSTER_HOST` | Cluster hostname for NodePort access type |

## References

- [`internal/kube/securedaccess/access.go`](../human/skupper/internal/kube/securedaccess/access.go)
- [`internal/kube/securedaccess/config.go`](../human/skupper/internal/kube/securedaccess/config.go)
- [Site Controller concept](./site-controller.md)
- [Default Site concept](./default-site.md)
- [Certificate Manager concept](./certificate-manager.md)
