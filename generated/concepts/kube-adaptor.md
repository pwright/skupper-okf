---
type: Concept
title: Kube Adaptor
id: skupper-concept-kube-adaptor
status: generated
owner: agent
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper
source_paths:
  - cmd/kube-adaptor/main.go
  - internal/kube/adaptor/config_init.go
  - internal/kube/adaptor/config_sync.go
  - internal/kube/adaptor/collector.go
  - internal/kube/site/resources/skupper-router-deployment.yaml
  - internal/qdr/sync_router_ops.go
  - internal/kube/secrets/sync.go
  - api/types/types.go
tags:
  - skupper
  - kube-adaptor
  - router
  - config-sync
  - tls
  - flow-collector
  - sidecar
related:
  - skupper-concept-default-site
  - skupper-concept-inter-site-link
  - skupper-crd-routeraccesses-skupper-io
timestamp: 2026-08-11T00:00:00Z
---

# Kube Adaptor

The **kube-adaptor** is a Kubernetes-aware sidecar that runs alongside the
Skupper router in the `skupper-router` Deployment. Its job is to bridge the
gap between the Kubernetes control plane (ConfigMaps, Secrets) and the router's
live management API — translating Kubernetes-native configuration into live
router state without requiring a router restart.

## Why it exists

The Skupper router (`skrouterd`) reads its initial configuration from a JSON
file on disk (`skrouterd.json`), but it also exposes a management API over AMQP
that allows live updates to listeners, connectors, SSL profiles, and bridge
entities. The Skupper site controller (which is a separate process) writes
desired configuration into a ConfigMap; the kube-adaptor watches that ConfigMap
and keeps the running router in sync with it. This separation means:

- The router never needs to restart when configuration changes.
- TLS certificates can be rotated live by updating Kubernetes Secrets.
- Bridge config (TCP listeners/connectors for service exposure) is updated
  without disrupting existing connections.

## Deployment position

The kube-adaptor image is defined as two things inside the
`skupper-router` Deployment that the site controller creates:

```
skupper-router Deployment
├── initContainer: config-init   (same image, run once at pod start)
│     └─ writes skrouterd.json to a shared emptyDir volume
└── container:    kube-adaptor   (long-running sidecar)
      └─ watches ConfigMap + Secrets, live-syncs router
```

Both the init container and the sidecar mount the same `skupper-router-certs`
and `skupper-router-proxies` `emptyDir` volumes that the router container also
mounts under `/etc/skupper-router-certs`.

The router container reads its start-up config from that volume:

```yaml
# internal/kube/site/resources/skupper-router-deployment.yaml
- name: QDROUTERD_CONF
  value: /etc/skupper-router-certs/skrouterd.json
- name: QDROUTERD_CONF_TYPE
  value: json
```

## Init phase: `config-init`

Before the router starts, the `config-init` init container runs
`kube-adaptor -init`, which calls [`InitialiseConfig`](../human/skupper/internal/kube/adaptor/config_init.go):

1. Reads the `skupper-router` ConfigMap to get the desired `RouterConfig`.
2. Starts a Secrets informer and waits for all required `SslProfile` and
   `ProxyProfile` secrets to appear (retries with exponential back-off for up
   to 60 seconds).
3. Writes the final `RouterConfig` as JSON to
   `/etc/skupper-router-certs/skrouterd.json`.

```go
// internal/kube/adaptor/config_init.go
value, err := qdr.MarshalRouterConfig(*routerConfiguration)
...
configFile := paths.Join(path, "skrouterd.json")
os.WriteFile(configFile, []byte(value), 0777)
```

Only after this file is written does Kubernetes allow the main containers to
start. This guarantees the router always has a valid, fully-materialised
config file at startup — including certificate paths that reference files
already present on disk.

## Run phase: `ConfigSync`

Once the pod is running, the `kube-adaptor` sidecar creates a
[`ConfigSync`](../human/skupper/internal/kube/adaptor/config_sync.go)
and starts its control loop. `ConfigSync` watches the `skupper-router`
ConfigMap for changes and, on each change event, executes
`configEvent` in order:

```go
// internal/kube/adaptor/config_sync.go
func (c *ConfigSync) configEvent(key string, configmap *corev1.ConfigMap) error {
    desired, _ := qdr.GetRouterConfigFromConfigMap(configmap)
    c.syncSslProfileCredentialsToDisk(desired.SslProfiles)
    qdr.SyncSslProfilesToRouter(c.agentPool, desired.SslProfiles)
    c.syncProxyProfileCredentialsToDisk(key, desired.ProxyProfiles)
    qdr.SyncProxyProfilesToRouter(c.agentPool, desired.ProxyProfiles)
    qdr.SyncBridgeConfig(c.agentPool, &desired.Bridges)
    qdr.SyncRouterConfig(c.agentPool, desired, true)
    ...
}
```

Each step is a reconcile against the router's live state:

| Step | What it does |
|---|---|
| `syncSslProfileCredentialsToDisk` | Fetches the Kubernetes Secret backing each SSL profile, writes PEM files to `/etc/skupper-router-certs` |
| `SyncSslProfilesToRouter` | Diffs desired vs. actual SSL profiles in the router; creates, updates, or deletes via AMQP management API |
| `syncProxyProfileCredentialsToDisk` | Same as SSL, but for proxy profiles |
| `SyncProxyProfilesToRouter` | Diffs and reconciles proxy profiles in the router |
| `SyncBridgeConfig` | Reconciles TCP bridge entities (tcpListeners / tcpConnectors used for service exposure) |
| `SyncRouterConfig` | Reconciles router-level listeners and connectors (inter-router / edge / outbound links) |

### How the AMQP management sync works

All live sync operations go through an `AgentPool` that maintains a pool of
connections to the router's local AMQP management port (`amqp://localhost:5672`):

```go
// internal/kube/adaptor/config_sync.go
agentPool: qdr.NewAgentPool("amqp://localhost:5672", nil),
```

Each sync function follows the same pattern — diff actual vs. desired, create
missing entities, update changed ones, delete stale ones:

```go
// internal/qdr/sync_router_ops.go — SyncSslProfilesToRouter (illustrative)
actual, _ := agent.GetSslProfiles()
for _, profile := range desired {
    if _, ok := actual[profile.Name]; !ok {
        agent.CreateSslProfile(profile)
    } else if actual[profile.Name] != profile {
        agent.UpdateSslProfile(profile)
    }
}
for _, profile := range actual {
    if _, ok := desired[profile.Name]; !ok {
        agent.Delete("io.skupper.router.sslProfile", profile.Name)
    }
}
```

`SyncRouterConfig` delegates to two sub-functions:

- **`syncListeners`** — reconciles all listeners that are *not* protected
  (i.e., not the internal `amqp`/`amqps` listeners), including the
  `inter-router` and `edge` listeners that appear when `RouterAccess` is set.
- **`syncConnectors`** — reconciles outbound connectors (links to other sites),
  skipping the `auto-mesh` prefix used for internal router mesh connections.

### Secret rotation

The `ConfigSync` also holds a `secrets.Sync` (`profileSyncer`) that watches
*all* Secrets in the namespace. When a Secret changes, `recheckProfile` fires:

```go
// internal/kube/adaptor/config_sync.go
func (c *ConfigSync) recheckProfile(_ string) {
    configmap, _ := c.config.Get(key)
    c.configEvent(key, configmap)
}
```

This re-runs the full `configEvent` pipeline, which rewrites any rotated cert
files to disk and pushes updated SSL profiles to the router — all without a pod
restart.

## Collector: flow data and site status

In parallel with `ConfigSync`, `StartCollector` runs a leader-election loop
using a Kubernetes `LeaseLock` named `skupper-site-leader`. Only the elected
leader runs the two collector sub-components:

```go
// internal/kube/adaptor/collector.go
OnStartedLeading: func(ctx context.Context) {
    siteCollector(leaderCtx, cli)
    ensureStartFlowController(leaderCtx, cli)
},
```

### `siteCollector`

Creates (or adopts) the `skupper-network-status` ConfigMap owned by the
`skupper-router` Deployment, then starts a `StatusSync` that reads flow data
from the router over AMQP (`kube-flow-collector` container ID) and writes
aggregated network topology into that ConfigMap.

### `startFlowController`

Reads the router Deployment's owner reference to derive the site ID and site
name (the UID and name of the owning `Site` CR), then starts a
`kubeflow.Controller`. The flow controller watches Pods via an informer and
emits `vanflow` site/process records over AMQP (`kube-flow-controller`
container ID), which the Network Observer picks up for topology and metrics.

Leader election ensures exactly one pod per site is emitting these events even
when HA mode runs two router replicas.

## Startup sequence

```
1. config-init runs kube-adaptor -init
   ├─ reads skupper-router ConfigMap
   ├─ waits for all TLS Secrets to exist
   └─ writes /etc/skupper-router-certs/skrouterd.json

2. router container starts, loads skrouterd.json

3. kube-adaptor sidecar starts
   ├─ waits for AMQP connection on localhost:5672 (180s timeout)
   ├─ starts ConfigSync watch loop (ConfigMap + Secrets → live router)
   └─ starts Collector (leader election → StatusSync + FlowController)

4. On any ConfigMap or Secret change:
   └─ configEvent runs full reconcile: disk certs → SSL profiles →
      proxy profiles → bridge config → listeners/connectors
```

## Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `NAMESPACE` / `--namespace` | (required) | Kubernetes namespace to watch |
| `SKUPPER_CONFIG_DIR` / `--config-dir` | `/etc/skupper-router-certs` | Directory for cert files and `skrouterd.json` |
| `SKUPPER_ROUTER_CONFIG` / `--router-config` | `skupper-router` | Name of the ConfigMap holding router config |
| `SKUPPER_ROUTER_DEPLOYMENT` | `skupper-router` | Name of the router Deployment (used to resolve site ID) |

## Relationship to the site controller

The kube-adaptor does **not** make decisions about what the desired
configuration should be. It only applies what the site controller has already
written into the `skupper-router` ConfigMap. The separation of concerns is:

| Component | Responsibility |
|---|---|
| Site controller (`cmd/controller`) | Watches Skupper CRs (Site, RouterAccess, Link, Connector, …) and writes the desired router config into a ConfigMap |
| Kube adaptor (`cmd/kube-adaptor`) | Watches that ConfigMap and Kubernetes Secrets; applies changes to the live running router over AMQP |

This means the kube-adaptor has no knowledge of Skupper CRDs at all — it only
speaks to the Kubernetes core API (ConfigMaps, Secrets) and the router's AMQP
management interface.

## References

- [`cmd/kube-adaptor/main.go`](../human/skupper/cmd/kube-adaptor/main.go)
- [`internal/kube/adaptor/config_sync.go`](../human/skupper/internal/kube/adaptor/config_sync.go)
- [`internal/kube/adaptor/config_init.go`](../human/skupper/internal/kube/adaptor/config_init.go)
- [`internal/kube/adaptor/collector.go`](../human/skupper/internal/kube/adaptor/collector.go)
- [`internal/qdr/sync_router_ops.go`](../human/skupper/internal/qdr/sync_router_ops.go)
- [`internal/kube/site/resources/skupper-router-deployment.yaml`](../human/skupper/internal/kube/site/resources/skupper-router-deployment.yaml)
