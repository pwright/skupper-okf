---
type: Concept
title: System Controller (Non-Kubernetes)
id: skupper-concept-system-controller
status: generated
owner: agent
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper
source_paths:
  - cmd/system-controller/main.go
  - internal/nonkube/controller/system_adaptor.go
  - internal/nonkube/controller/system_adaptor_handler.go
  - internal/nonkube/controller/router_state_handler.go
  - internal/nonkube/controller/router_config_handler.go
  - internal/nonkube/controller/network_status_handler.go
  - internal/nonkube/controller/namespaces.go
tags:
  - skupper
  - system-controller
  - nonkube
  - podman
  - docker
  - linux
  - site-controller
related:
  - skupper-concept-site-controller
  - skupper-concept-kube-adaptor
  - skupper-concept-router-bindings
timestamp: 2026-08-11T00:00:00Z
---

# System Controller (Non-Kubernetes)

The **system controller** (`cmd/system-controller`) is the non-Kubernetes equivalent of the [site controller](./site-controller.md). It runs on bare Linux, Podman, or Docker hosts and performs the same role — watching for configuration changes and keeping the Skupper router in sync — but without any Kubernetes API or CRD machinery. Instead it watches a local filesystem hierarchy of namespaces and JSON config files.

## Contrast with the Kubernetes path

| Concern | Kubernetes (site controller + kube-adaptor) | Non-Kubernetes (system controller) |
|---|---|---|
| Config source | `skupper-router` ConfigMap | JSON files under `~/.local/share/skupper/namespaces/<ns>/runtime/` |
| Config apply | kube-adaptor watches ConfigMap → AMQP | `SystemAdaptorHandler` polls config file → AMQP |
| TLS certs | `Certificate` CRs → Kubernetes Secrets | PEM files on disk at runtime path |
| Router liveness | Kubernetes liveness probe | AMQP heartbeat (`RouterStateHandler`) |
| Network status | `skupper-network-status` ConfigMap | Runtime-state YAML file |
| Namespace discovery | Kubernetes namespace informer | Filesystem watcher on the namespaces directory |

## Entry point

`cmd/system-controller/main.go` is minimal. It:
1. Reads the `SKUPPER_SYSTEM_AUTO_RELOAD` env var (defaults to `manual`).
2. Calls `controller.NewController()` and `c.Start()`.
3. Blocks on SIGINT/SIGTERM; shuts down with a 10-second grace period.

The `namespacesPath` watched is `api.GetDefaultOutputNamespacesPath()` — typically `~/.local/share/skupper/namespaces` (or the container-equivalent host path).

## Namespace discovery (`NamespacesHandler`)

`NamespacesHandler` watches the namespaces directory using an `inotify`-style watcher:

- **`OnCreate`** — a new subdirectory appears → starts a per-namespace controller.
- **`OnRemove`** — a subdirectory is deleted → stops the per-namespace controller.
- **`loadExistingNamespaces`** — at startup, starts controllers for all existing subdirectories.

Each namespace gets its own independent set of handlers that run concurrently.

## Per-namespace handler chain

For each namespace, the system controller creates a chain of handlers connected via `ActivationCallback` interfaces. Each handler activates or deactivates the next one based on readiness:

```
RouterConfigHandler
    (watches for skrouterd.json to appear on disk)
        ↓ activates when config file exists
RouterStateHandler
    (sends AMQP heartbeats; detects router up/down)
        ↓ activates when router is reachable
SystemAdaptorHandler   (optional — only when AUTO_RELOAD is enabled)
    (polls config file every 1s → syncs to live router)
NetworkStatusHandler
    (watches skupper-network-status file for topology changes)
```

### `RouterConfigHandler`

Watches the namespace's runtime directory for the `skrouterd.json` file. When the file appears (`OnCreate`), it triggers the next stage. When removed (`OnRemove`), it tears everything back down. This ensures downstream handlers only start when the router has a valid config to boot from.

### `RouterStateHandler`

Maintains an AMQP heartbeat connection to the local router. Uses an exponential back-off loop to detect when the router comes up and sends periodic heartbeats to confirm it remains reachable:

```go
// internal/nonkube/controller/router_state_handler.go (simplified)
func (h *heartBeatsClient) routerUp(stopCh <-chan struct{}) {
    // activates all registered callbacks
    h.run(stopCh)  // sends heartbeats; on failure → routerDown()
}
func (h *heartBeatsClient) routerDown(reason string) {
    // deactivates all registered callbacks
}
```

When the router is confirmed up, it calls `OnStartedLeading`-equivalent callbacks on all registered `ActivationCallback` implementations.

### `SystemAdaptorHandler` (auto-reload mode only)

Only created when `SKUPPER_SYSTEM_AUTO_RELOAD` is not `manual`. Polls the router config file every second and syncs it to the live router over AMQP:

```go
// internal/nonkube/controller/system_adaptor_handler.go
func (s *SystemAdaptorHandler) processRouterConfig(stopCh <-chan struct{}) {
    ticker := time.NewTicker(time.Second)
    for {
        select {
        case <-ticker.C:
            desired, _ := common.LoadRouterConfig(s.namespace)
            s.systemAdaptor.syncWithRouter(desired)
        }
    }
}
```

`SystemAdaptor.syncWithRouter` runs the same reconcile pipeline as the kube-adaptor:

```go
// internal/nonkube/controller/system_adaptor.go
func (s *SystemAdaptor) syncWithRouter(desired *qdr.RouterConfig) error {
    s.syncSslProfileCredentialsToDisk(desired.SslProfiles)  // verify certs exist
    qdr.SyncSslProfilesToRouter(s.agentPool, s.addSslPathToProfileCredentials(desired.SslProfiles))
    qdr.SyncBridgeConfig(s.agentPool, &desired.Bridges)
    qdr.SyncRouterConfig(s.agentPool, desired, false)  // false = don't recheck cert files
    return nil
}
```

The key difference from the kube-adaptor is that SSL profile credentials are **verified to exist on disk** (not fetched from Kubernetes Secrets), and the cert file paths are resolved relative to `/etc/skupper-router/runtime/certs/<name>/`.

### `NetworkStatusHandler`

Watches the `skupper-network-status` file in the namespace runtime directory. When it changes, it reads the JSON network topology and updates the site's runtime state YAML — the non-Kubernetes equivalent of the kube-adaptor writing to a ConfigMap.

## Config file location

The system controller's config is located entirely on disk:

```
~/.local/share/skupper/namespaces/
└── <namespace>/
    └── runtime/
        ├── skrouterd.json          ← router config (watched by RouterConfigHandler)
        ├── skupper-network-status  ← topology JSON (watched by NetworkStatusHandler)
        └── certs/
            └── <cert-name>/
                ├── ca.crt
                ├── tls.crt
                └── tls.key
```

## Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `SKUPPER_SYSTEM_AUTO_RELOAD` | `manual` | Set to `auto` to enable `SystemAdaptorHandler` polling |

In `manual` mode, the system controller monitors the router's liveness and network status, but does **not** automatically push config changes to the live router. Config changes require a router restart.

## References

- [`cmd/system-controller/main.go`](../human/skupper/cmd/system-controller/main.go)
- [`internal/nonkube/controller/system_adaptor.go`](../human/skupper/internal/nonkube/controller/system_adaptor.go)
- [`internal/nonkube/controller/system_adaptor_handler.go`](../human/skupper/internal/nonkube/controller/system_adaptor_handler.go)
- [`internal/nonkube/controller/router_state_handler.go`](../human/skupper/internal/nonkube/controller/router_state_handler.go)
- [Site Controller concept](./site-controller.md)
- [Kube Adaptor concept](./kube-adaptor.md)
