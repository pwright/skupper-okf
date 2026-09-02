---
type: Concept
title: Site Controller
id: skupper-concept-site-controller
status: generated
owner: agent
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper
source_paths:
  - cmd/controller/
  - internal/kube/controller/controller.go
  - internal/kube/controller/config.go
  - internal/kube/site/site.go
tags:
  - skupper
  - controller
  - site
  - reconciliation
  - kubernetes
related:
  - skupper-concept-kube-adaptor
  - skupper-concept-default-site
  - skupper-concept-secured-access
  - skupper-concept-certificate-manager
  - skupper-concept-access-grants-and-tokens
  - skupper-concept-router-bindings
timestamp: 2026-08-11T00:00:00Z
---

# Site Controller

The **site controller** (`cmd/controller`) is the central Kubernetes operator for Skupper. It watches every Skupper custom resource in one or more namespaces and reconciles them into the desired network state — creating router deployments, ConfigMaps, Certificates, SecuredAccess objects, and Links as needed.

## Role in the architecture

```
Skupper CRs (Site, Link, Connector, Listener, RouterAccess, …)
        ↓  watched by EventProcessor
   Site Controller
        ↓  writes desired state to
   skupper-router ConfigMap
        ↓  read by
   kube-adaptor (sidecar) → live router AMQP API
```

The site controller never touches the router process directly. It only writes to Kubernetes resources; the [kube-adaptor](./kube-adaptor.md) is responsible for applying those changes to the running router.

## Controller struct and sub-managers

The [`Controller`](../human/skupper/internal/kube/controller/controller.go) struct owns three pluggable sub-managers:

| Sub-manager | Package | Responsibility |
|---|---|---|
| `CertificateManagerImpl` | `internal/kube/certificates` | Reconciles `Certificate` CRs → Kubernetes Secrets (mTLS material) |
| `SecuredAccessManager` | `internal/kube/securedaccess` | Reconciles `SecuredAccess` CRs → Services, Routes, Ingresses, LoadBalancers |
| `Grants` | `internal/kube/grants` | Serves the HTTPS grant-redemption endpoint; reconciles `AccessGrant`/`AccessToken` CRs |

Each sub-manager is initialised in `NewController` and handed a `ControllerContext` interface so they can call back into the controller for namespace-filtering and label/annotation propagation.

## Namespace scope

The controller can run in two modes, controlled by `WATCH_NAMESPACE`:

- **Single namespace** (`WATCH_NAMESPACE=my-ns`): only processes resources in that namespace; always requires an explicit control ConfigMap.
- **All namespaces** (`WATCH_NAMESPACE=""`, the default): monitors every namespace. When `REQUIRE_EXPLICIT_CONTROL=true` (or when watching all namespaces from a single-namespace deployment), a namespace is only processed if it contains a ConfigMap named `skupper` with a `controller` entry matching the controller's qualified name.

The `filter` helper wraps every event handler with this check:

```go
// internal/kube/controller/controller.go
func filter[V any](controller *Controller, handler func(string, V) error) func(string, V) error {
    return watchers.FilterByNamespace(controller.IsControlled, handler)
}
```

## Informers registered at startup

`NewController` registers one informer per resource type. All informers are scoped to `WatchNamespace`:

| Informer | Resource | Handler |
|---|---|---|
| `siteWatcher` | `Site` | `checkSite` |
| `listenerWatcher` | `Listener` | `checkListener` |
| `connectorWatcher` | `Connector` | `checkConnector` |
| `multiKeyListenerWatcher` | `MultiKeyListener` | `checkMultiKeyListener` |
| `linkAccessWatcher` | `RouterAccess` | `checkRouterAccess` |
| `attachedConnectorWatcher` | `AttachedConnector` | `checkAttachedConnector` |
| `attachedConnectorBindingWatcher` | `AttachedConnectorBinding` | `checkAttachedConnectorBinding` |
| Links | `Link` | `checkLink` |
| AccessTokens | `AccessToken` | `checkAccessToken` |
| Router pods | Pods with `skupper.io/component=router` | `routerPodEvent` |
| Router ConfigMaps | ConfigMaps labelled `internal.skupper.io/router-config` | `routerConfigUpdate` |
| Network status | `skupper-network-status` ConfigMap | `networkStatusUpdate` |
| Listener services | Services labelled `internal.skupper.io/listener` | `checkListenerService` |
| Other services | Services without that label | `checkObservedService` |
| Site sizing | ConfigMaps labelled with the sizing label | `siteSizing.Update` |
| Label templates | ConfigMaps labelled `skupper.io/label-template` | `labelling.Update` |

## Initialisation sequence

The `init` phase runs before the event loop and performs a full recovery from existing cluster state:

```
1. Start all informers, wait for cache sync
2. Recover namespace control config
3. Recover site-sizing and labelling ConfigMaps
4. Recover CertificateManager (existing Certificates + Secrets)
5. Recover SecuredAccessManager (existing SecuredAccess, Routes, Ingresses, Services)
6. Seed observed services cache
7. Seed RouterAccess objects into each Site (before site recovery)
8. Recover each Site: call site.StartRecovery()
9. Recover Connectors, Listeners, MultiKeyListeners
10. Recover AttachedConnectorBindings and AttachedConnectors
11. Recover network status ConfigMaps
12. Wait for pod-watcher caches to sync (pod selectors from connectors)
13. Call site.Reconcile() for each recovered site → writes router ConfigMap
14. Start grant HTTP server
```

## Per-namespace Site objects

The controller holds a `sites map[string]*site.Site`. Each namespace gets exactly one `Site` instance, created lazily by `getSite`:

```go
// internal/kube/controller/controller.go
func (c *Controller) getSite(namespace string) *site.Site {
    if existing, ok := c.sites[namespace]; ok {
        return existing
    }
    site := site.NewSite(namespace, c.eventProcessor, c.certMgr, c.accessMgr, c.siteSizing, c, c.disableSecContext)
    c.sites[namespace] = site
    return site
}
```

Almost every event handler just extracts the namespace from the key and delegates to the appropriate `Site` method:

```go
func (c *Controller) checkConnector(key string, connector *skupperv2alpha1.Connector) error {
    namespace, name, _ := cache.SplitMetaNamespaceKey(key)
    return c.getSite(namespace).CheckConnector(name, connector)
}
```

## What `site.Reconcile` does

`Site.Reconcile` in [`internal/kube/site/site.go`](../human/skupper/internal/kube/site/site.go) is the core reconcile function. On every `Site` CR change it:

1. Validates the site spec (e.g. rejects invalid `linkAccess` types).
2. Ensures the router `ServiceAccount`, `Role`, and `RoleBinding` exist.
3. Ensures the local CA Certificate and the `skupper-local` mTLS credentials exist (via `certMgr.EnsureCA` / `certMgr.Ensure`).
4. Calls `checkDefaultRouterAccess` — creates a `RouterAccess` CR if `linkAccess` is set (see [Default Site](./default-site.md)).
5. Builds the desired `RouterConfig` (listeners, connectors, SSL profiles) and writes it as a ConfigMap labelled `internal.skupper.io/router-config`.
6. Creates or updates the `skupper-router` Deployment (via the embedded YAML template in `resources/`).
7. Ensures any `SecuredAccess` objects for active `RouterAccess` entries.
8. Updates `Site.Status` conditions (`Configured`, `Resolved`, `Running`).

## AccessToken handling

When an `AccessToken` CR appears (not yet redeemed), the controller calls `grants.RedeemAccessToken` directly from `checkAccessToken`:

```go
func (c *Controller) checkAccessToken(key string, token *skupperv2alpha1.AccessToken) error {
    if token == nil || token.IsRedeemed() {
        return nil
    }
    site := c.getSite(token.Namespace).GetSite()
    return grants.RedeemAccessToken(token, site, c.eventProcessor)
}
```

This makes an HTTPS POST to the grant server on the remote site and, on success, creates the `Secret` and `Link` CRs that establish the inter-site connection. See [Access Grants and Tokens](./access-grants-and-tokens.md).

## Network status propagation

When the `skupper-network-status` ConfigMap changes (written by the kube-adaptor's flow collector), the controller decodes the `NetworkStatus` JSON and forwards it to `site.NetworkStatusUpdated`. The site uses this to update `Link` operational status and — when `exposePodsByName` is used on listeners — to populate per-pod routing entries.

## Configuration reference

| Flag / Env var | Default | Purpose |
|---|---|---|
| `NAMESPACE` | required | Namespace the controller itself runs in |
| `WATCH_NAMESPACE` | `""` (all) | Namespace(s) to monitor for Skupper CRs |
| `REQUIRE_EXPLICIT_CONTROL` | `false` | Require a `skupper` ConfigMap in each namespace |
| `DISABLE_SECURITY_CONTEXT` | `false` | Omit security contexts from managed pods |
| `SKUPPER_ENABLED_ACCESS_TYPES` | `local,loadbalancer,route` | Allowed `SecuredAccess` types |
| `SKUPPER_DEFAULT_ACCESS_TYPE` | auto-detected | Fallback access type when none specified |

## References

- [`internal/kube/controller/controller.go`](../human/skupper/internal/kube/controller/controller.go)
- [`internal/kube/controller/config.go`](../human/skupper/internal/kube/controller/config.go)
- [`internal/kube/site/site.go`](../human/skupper/internal/kube/site/site.go)
- [Kube Adaptor concept](./kube-adaptor.md)
- [Default Site concept](./default-site.md)
- [SecuredAccess concept](./secured-access.md)
- [Certificate Manager concept](./certificate-manager.md)
- [Access Grants and Tokens concept](./access-grants-and-tokens.md)
