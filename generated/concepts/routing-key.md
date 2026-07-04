---
type: Concept
title: Routing Key
id: skupper-concept-routing-key
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source_url: "https://deepwiki.com/search/describe-routing-keys_2253deab-7e55-44b3-a894-d02a8eeba282?mode=deep"
source_paths:
  - human/skupper-openapi-spec/openapi.yaml
  - human/skupper-docs/input/refdog/concepts/connector.md
  - human/skupper-docs/input/refdog/concepts/listener.md
  - human/skupper-example-hello-world/README.md
human_sources:
  - Skupper Network Observer OpenAPI Specification
  - Skupper documentation repository
  - Skupper Hello World example
tags:
  - skupper
  - routing-key
  - service-exposure
  - amqp
  - connector
  - listener
related:
  - skupper-concept-connector
  - skupper-concept-listener
  - skupper-concept-multikeylistener
  - skupper-concept-network-observer-api
timestamp: 2026-07-04T09:15:00Z
---

# Routing Key

A **routing key** is a string identifier that links listeners and connectors across Skupper sites. When a Listener in one site and a Connector in another share the same routing key, the Skupper router network automatically routes traffic between them—no IP addresses or DNS configuration required.

## Outcome

A routing key enables cross-site service discovery and traffic routing:

```text
remote client → Listener (routingKey: "backend")
                    ↓ (Skupper network)
                Connector (routingKey: "backend") → local workload
```

## How Routing Keys Work

### API Level

At the Kubernetes API level, `routingKey` is a required field on both Listeners and Connectors:

**Listener** — maps local endpoint → routing key:
```yaml
apiVersion: skupper.io/v2alpha1
kind: Listener
metadata:
  name: backend-listener
spec:
  routingKey: backend    # Required string identifier
  host: backend-svc
  port: 8080
```

**Connector** — maps routing key → local workload:
```yaml
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: backend-connector
spec:
  routingKey: backend    # Must match listener's key
  selector: app=backend
  port: 8080
```

### Router Network Level

The routing key is translated directly into the AMQP `address` field of the underlying router bridge entities (`tcpListener` and `tcpConnector`). The routers in different sites exchange reachability information over their inter-site AMQP connections and match endpoints by this address.

From the bridge configuration code:
```go
config.AddTcpListener(qdr.TcpEndpoint{
    Name:       name,
    SiteId:     siteId,
    Host:       host,
    Port:       strconv.Itoa(port),
    Address:    listener.Spec.RoutingKey,  // Becomes AMQP address
    SslProfile: listener.Spec.TlsCredentials,
    Observer:   listener.Spec.Observer,
})
```

## Status Feedback

The controller uses the routing key to report cross-site matching status:

**On Listener:**
```yaml
status:
  hasMatchingConnector: true  # True if any connector with matching key exists
```

**On Connector:**
```yaml
status:
  hasMatchingListener: true   # True if any listener with matching key exists
```

These fields help operators verify that cross-site routing is established.

## Per-Pod Qualified Addresses

When `exposePodsByName: true` is enabled on a Connector, a second address is registered as `<routingKey>.<podName>` in addition to the base routing key, enabling individual pod targeting:

```go
if addQualifiedAddress {
    if updateBridgeConfigForConnector(
        qdr.TcpConnectorNamePrefix+connector.Name+"@"+pod.Name,
        siteId, connector, pod.IP, pod.UID,
        connector.Spec.RoutingKey+"."+pod.Name,  // Qualified address
        config,
    ) {
        updated = true
    }
}
```

This allows clients to route to specific backend pods:
- Base routing key: `backend` → round-robin to all pods
- Qualified key: `backend.pod-abc123` → direct to specific pod

## MultiKeyListener — Multiple Routing Keys on One Endpoint

The `MultiKeyListener` CRD extends the concept by letting a single local endpoint distribute traffic across **multiple** routing keys using one of two strategies:

### Priority Strategy

100% of traffic goes to the first routing key in the list that has a reachable connector. Each key gets a descending numeric `value` so the router knows the order.

```yaml
apiVersion: skupper.io/v2alpha1
kind: MultiKeyListener
metadata:
  name: backend-priority
spec:
  host: backend-priority
  port: 8080
  strategy:
    priority:
      routingKeys:
        - backend-primary      # First choice
        - backend-secondary    # Fallback
```

From the controller implementation:
```go
if mkl.Spec.Strategy.Priority != nil {
    tcpListenerConfig.MultiAddressStrategy = "priority"
    numKeys := len(mkl.Spec.Strategy.Priority.RoutingKeys)
    for i, routingKey := range mkl.Spec.Strategy.Priority.RoutingKeys {
        laName := listenerAddressName(name, routingKey)
        config.AddListenerAddress(qdr.ListenerAddress{
            Name:     laName,
            Address:  routingKey,
            Value:    numKeys - 1 - i,  // Higher value = higher priority
            Listener: tcpListenerName,
        })
    }
}
```

### Weighted Strategy

Traffic is split among reachable routing keys proportionally to their integer weights.

```yaml
apiVersion: skupper.io/v2alpha1
kind: MultiKeyListener
metadata:
  name: backend-weighted
spec:
  host: backend-weighted
  port: 8081
  strategy:
    weighted:
      routingKeys:
        backend-single: 1     # 33% of traffic
        backend-double: 2     # 67% of traffic
```

From the controller implementation:
```go
} else if mkl.Spec.Strategy.Weighted != nil {
    tcpListenerConfig.MultiAddressStrategy = "weighted"
    for routingKey, weight := range mkl.Spec.Strategy.Weighted.RoutingKeys {
        laName := listenerAddressName(name, routingKey)
        config.AddListenerAddress(qdr.ListenerAddress{
            Name:     laName,
            Address:  routingKey,
            Value:    int(weight),
            Listener: tcpListenerName,
        })
    }
}
```

Each routing key in a MultiKeyListener becomes a router entity (type `listenerAddress`) linked to the parent listener.

## Network Observer API

The [Network Observer API](./network-observer-api.md) exposes routing keys in several resources. The `routingKey` field appears as a required property in listeners, connectors, connections, and flow records.

For detailed API schema information, see the [Network Observer API Reference](../sources/skupper-openapi-spec-api-reference.md).

### Service Resource

The `/api/v2alpha1/services` endpoint groups listeners and connectors by routing key and exposes binding status:

```json
{
  "identity": "service-backend@tcp",
  "name": "backend",
  "protocol": "tcp",
  "isBound": true,
  "hasListener": true,
  "listenerCount": 1,
  "connectorCount": 2
}
```

The `isBound` field indicates when a routing key has both listeners and connectors configured—the minimal requirement for cross-site traffic routing.

### Connection Resource

Active connections include the routing key that was used to establish them:

```json
{
  "routingKey": "backend",
  "protocol": "tcp",
  "sourceSiteId": "site-west",
  "destSiteId": "site-east",
  "sourceProcessId": "process-client-123",
  "destProcessId": "process-workload-789"
}
```

This shows which routing keys are in active use and which processes they connect.

### Flow Aggregate Resource

Flow aggregates (sitepairs, processpairs, componentpairs) track traffic volume and can be filtered by routing key. This enables time-series analysis of traffic patterns per service.

## Summary Flow

```text
1. Operator creates Listener with routingKey: "backend" in Site A
   ↓
2. Site A router registers AMQP address "backend"
   ↓
3. Operator creates Connector with routingKey: "backend" in Site B
   ↓
4. Site B router registers AMQP address "backend"
   ↓
5. Routers exchange reachability over inter-site link
   ↓
6. Status updated:
   - Listener.status.hasMatchingConnector = true
   - Connector.status.hasMatchingListener = true
   ↓
7. Client connects to listener → traffic routed to connector
```

The routing key is the **sole mechanism** for cross-site service discovery—no external DNS, IP configuration, or service mesh is required. The AMQP overlay handles all routing and topology changes transparently.

## Key Properties

- **String identifier**: Simple string, no special format required
- **Case-sensitive**: `backend` ≠ `Backend`
- **Scoped to network**: Routing keys are network-wide, not namespace-scoped
- **Many-to-many**: Multiple listeners and connectors can share the same routing key
- **Protocol-agnostic**: Works with TCP, HTTP, gRPC (all tunneled over AMQP)
- **Dynamic**: Adding/removing listeners or connectors updates routing automatically

## References

- [Skupper Network Observer OpenAPI Specification](../human/skupper-openapi-spec/openapi.yaml)
- [DeepWiki: Routing Keys](https://deepwiki.com/search/describe-routing-keys_2253deab-7e55-44b3-a894-d02a8eeba282?mode=deep)
- [Skupper Connector Concept](./connector.md)
- [Skupper Listener Concept](./listener.md)
