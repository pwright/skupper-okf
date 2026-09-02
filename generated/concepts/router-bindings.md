---
type: Concept
title: Router Bindings
id: skupper-concept-router-bindings
status: generated
owner: agent
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper
source_paths:
  - internal/site/bindings.go
  - internal/site/connector.go
  - internal/site/listener.go
  - internal/site/multikeylistener.go
  - internal/kube/site/bindings.go
  - internal/kube/site/extended_bindings.go
  - internal/kube/site/pods.go
tags:
  - skupper
  - bindings
  - connector
  - listener
  - bridge-config
  - pod-selector
  - tcp
related:
  - skupper-concept-routing-key
  - skupper-concept-site-controller
  - skupper-concept-kube-adaptor
  - skupper-crd-connectors-skupper-io
  - skupper-crd-listeners-skupper-io
timestamp: 2026-08-11T00:00:00Z
---

# Router Bindings

**Router bindings** are the mechanism that translates Skupper `Connector` and `Listener` CRs into the router's TCP bridge configuration. A binding maps an application-layer endpoint — a host/port pair or a pod selector — to an AMQP address (the routing key) inside the router. The site controller manages bindings; the kube-adaptor pushes the resulting bridge config to the live router.

## Where bindings sit in the architecture

```
Connector CR  ──┐
                ├─→  Bindings.Apply(config)  ──→  qdr.BridgeConfig
Listener  CR  ──┘         (site controller)       (in ConfigMap)
                                                       ↓
                                               kube-adaptor: SyncBridgeConfig()
                                                       ↓
                                               live router: tcpListener / tcpConnector
```

Bindings are platform-agnostic: `internal/site/bindings.go` holds the shared logic; `internal/kube/site/bindings.go` adds the Kubernetes-specific pod-selector watcher.

## `Bindings` struct (`internal/site`)

`Bindings` is the in-memory representation of all service bindings for one site:

```go
// internal/site/bindings.go
type Bindings struct {
    SiteId            string
    connectors        map[string]*skupperv2alpha1.Connector
    listeners         map[string]*skupperv2alpha1.Listener
    multiKeyListeners map[string]*skupperv2alpha1.MultiKeyListener
    configure struct {
        listener         ListenerConfiguration
        connector        ConnectorConfiguration
        multiKeyListener MultiKeyListenerConfiguration
    }
    ...
}
```

`Bindings.Apply(config *qdr.RouterConfig)` iterates all stored connectors, listeners, and multi-key listeners and calls the appropriate configure function for each, building up the desired `BridgeConfig`.

## Listener → `tcpListener`

A `Listener` CR maps a local host/port to an AMQP address (the routing key). The bridge function is straightforward:

```go
// internal/site/listener.go
func UpdateBridgeConfigForListener(siteId string, listener *skupperv2alpha1.Listener, config *qdr.BridgeConfig) {
    config.AddTcpListener(qdr.TcpEndpoint{
        Name:       qdr.TcpListenerNamePrefix + listener.Name,
        SiteId:     siteId,
        Host:       listener.Spec.Host,
        Port:       strconv.Itoa(listener.Spec.Port),
        Address:    listener.Spec.RoutingKey,   // AMQP address
        SslProfile: listener.Spec.TlsCredentials,
        Observer:   listener.Spec.Observer,
    })
}
```

The router binds a TCP port on `Host:Port` and routes incoming connections to the AMQP address `RoutingKey`. Remote connectors with the same routing key receive the traffic.

## Connector → `tcpConnector`

A `Connector` CR maps an AMQP address back to a local workload. There are two variants:

### Host-based connector

Used when `connector.Spec.Host` is set (typically for non-Kubernetes targets or static services):

```go
// internal/site/connector.go
func UpdateBridgeConfigForConnector(siteId string, connector *skupperv2alpha1.Connector, config *qdr.BridgeConfig) {
    if connector.Spec.Host != "" {
        updateBridgeConfigForConnector(
            qdr.TcpConnectorNamePrefix+connector.Name+"@"+connector.Spec.Host,
            siteId, connector, connector.Spec.Host, "", connector.Spec.RoutingKey, config,
        )
    }
}
```

### Pod-selector connector (Kubernetes)

When `connector.Spec.Selector` is set, the site controller starts a `PodWatcher` that tracks matching pods. For each running, ready pod a separate `tcpConnector` entry is created using the pod's IP:

```go
// internal/site/connector.go
func UpdateBridgeConfigForConnectorToPod(siteId string, connector *skupperv2alpha1.Connector, pod skupperv2alpha1.PodDetails, addQualifiedAddress bool, config *qdr.BridgeConfig) bool {
    // Primary entry: routing key → pod IP
    updateBridgeConfigForConnector(
        qdr.TcpConnectorNamePrefix+connector.Name+"@"+pod.IP,
        siteId, connector, pod.IP, pod.UID, connector.Spec.RoutingKey, config,
    )
    // Optional qualified address: "routingKey.podName" → specific pod
    if addQualifiedAddress {
        updateBridgeConfigForConnector(
            qdr.TcpConnectorNamePrefix+connector.Name+"@"+pod.Name,
            siteId, connector, pod.IP, pod.UID, connector.Spec.RoutingKey+"."+pod.Name, config,
        )
    }
}
```

The qualified address (`routingKey.podName`) enables per-pod targeting for callers that need to route to a specific replica. See [Routing Key](./routing-key.md).

### Bridge entry structure

All connector entries ultimately call `config.AddTcpConnector`:

```go
config.AddTcpConnector(qdr.TcpEndpoint{
    Name:           name,           // unique: connector.Name@host or @podIP
    SiteId:         siteId,
    Host:           host,           // pod IP or static host
    Port:           strconv.Itoa(connector.Spec.Port),
    Address:        address,        // AMQP routing key
    SslProfile:     GetSslProfileName(connector.Spec.TlsCredentials, connector.Spec.UseClientCert),
    ProcessID:      processID,      // pod UID for flow tracking
    VerifyHostname: getVerifyHostname(connector),
})
```

## Pod watcher (`internal/kube/site`)

The Kubernetes-specific `PodWatcher` wraps a `watchers.PodWatcher` informer. It filters pods by readiness and running state:

```go
// internal/kube/site/bindings.go
func (w *PodWatcher) pods() []skupperv2alpha1.PodDetails {
    for _, pod := range w.watcher.List() {
        if isPodReady(pod) || w.context.IncludeNotReadyPods() {
            if isPodRunning(pod) && pod.DeletionTimestamp == nil {
                targets = append(targets, skupperv2alpha1.PodDetails{
                    UID: string(pod.UID), Name: pod.Name, IP: pod.Status.PodIP,
                })
            }
        }
    }
}
```

When the pod list changes, `TargetSelectionImpl.Updated` is called, which triggers `site.updateRouterConfig` — re-computing the full bridge config and writing it to the router ConfigMap. The kube-adaptor picks up the ConfigMap change and syncs the live router within seconds.

## Multi-key listeners

A `MultiKeyListener` CR lets a single local endpoint distribute traffic across multiple routing keys using one of two strategies:

- **Priority**: traffic goes to the first key in the list that has a reachable connector.
- **Weighted**: traffic is split proportionally across keys.

The bridge function adds a `tcpListener` plus one `listenerAddress` entry per routing key:

```go
// internal/site/multikeylistener.go (simplified)
tcpListenerConfig.MultiAddressStrategy = "priority"   // or "weighted"
config.AddListenerAddress(qdr.ListenerAddress{
    Name:     listenerAddressName(name, routingKey),
    Address:  routingKey,
    Value:    priorityValue,   // descending integers for priority; weights for weighted
    Listener: tcpListenerName,
})
```

See [Routing Key](./routing-key.md) for full details on multi-key routing.

## Listener services (Kubernetes)

For each `Listener` CR in a Kubernetes site, the site controller also creates a `ClusterIP` Service. This lets in-cluster workloads reach the Skupper listener via Kubernetes DNS (`<listener.Spec.Host>.<namespace>.svc.cluster.local`) rather than knowing the router pod IP directly.

The service is labelled `internal.skupper.io/listener=true` and owned by the `Site` CR. When the Listener is deleted, the service is garbage-collected.

## Binding status conditions

The site controller updates `Connector.Status` and `Listener.Status` after each binding reconcile:

| Condition | Set when |
|---|---|
| `Configured` | Bridge config was successfully written to the ConfigMap |
| `hasMatchingListener` (Connector) | A Listener with the same routing key exists in the network |
| `hasMatchingConnector` (Listener) | A Connector with the same routing key exists in the network |

The matching-peer status is updated by `site.NetworkStatusUpdated` when the network topology changes — i.e., when the kube-adaptor's flow collector detects that a connector or listener has come online on another site.

## References

- [`internal/site/bindings.go`](../human/skupper/internal/site/bindings.go)
- [`internal/site/connector.go`](../human/skupper/internal/site/connector.go)
- [`internal/site/listener.go`](../human/skupper/internal/site/listener.go)
- [`internal/kube/site/bindings.go`](../human/skupper/internal/kube/site/bindings.go)
- [Routing Key concept](./routing-key.md)
- [Site Controller concept](./site-controller.md)
- [Kube Adaptor concept](./kube-adaptor.md)
