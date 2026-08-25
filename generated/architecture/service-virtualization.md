# Service Virtualization / Location Transparency

## Pattern Overview

Service virtualization is an architectural pattern where service consumers interact with a logical service representation without needing to know the physical location, network address, or deployment details of the service provider. This allows endpoint and location changes to occur **without affecting the service consumer or provider**.

This is identified by The Open Group SOA Reference Architecture as a core pattern for the Integration Layer, enabling location-independent service interactions.

**Reference**: [The Open Group SOA Reference Architecture - Service Virtualization](https://www.opengroup.org/soa/source-book/soa_refarch/p13.htm)

## TOGAF Context

### Architecture Building Block

**Location-transparent service connectivity**: Consumer applications must be able to invoke services without knowing where those services are deployed or how to reach them at the network level.

### Solution Building Block

**Skupper application network**: Provides routing keys as logical service identifiers, with listeners and connectors abstracting the physical service endpoints.

## Problem Statement

In distributed systems, services are often deployed across multiple locations (cloud, datacenter, edge), and their placement may change due to:

- Capacity planning and load management
- Cost optimization (moving workloads between cloud and on-premises)
- Disaster recovery and business continuity
- Development/staging/production environment variations
- Technology platform migrations

When service consumers are tightly coupled to service locations through IP addresses or DNS names, every location change requires:

- Updating consumer configuration
- Coordinating deployments across teams
- Managing DNS or load balancer changes
- Risk of service disruption during transition

## Solution with Skupper

Skupper implements service virtualization through three core components:

### 1. Routing Key (Logical Service Identity)

The routing key represents the stable, location-independent service identity. Consumers and providers reference the same routing key (e.g., `orders`, `payment-api`) regardless of where the service runs.

```yaml
# Example routing key
routingKey: orders
```

### 2. Listener (Consumer-side Abstraction)

The listener creates a stable local endpoint where consumers can connect. The listener is bound to the routing key and forwards connections through the Skupper network.

```yaml
apiVersion: skupper.io/v2alpha1
kind: Listener
metadata:
  name: orders
spec:
  routingKey: orders
  host: orders.svc.cluster.local
  port: 8080
```

Consumer applications connect to `orders.svc.cluster.local:8080` — a stable address that never changes, even when the Orders service is relocated.

### 3. Connector (Provider-side Abstraction)

The connector exposes the actual service workload to the Skupper network using the same routing key. Multiple connectors can share a routing key, and connectors can be moved between locations without affecting consumers.

```yaml
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: orders
spec:
  routingKey: orders
  selector: app=orders
  port: 8080
```

The connector identifies the actual Orders pods using Kubernetes selectors, but this detail is hidden from consumers.

## Architecture Diagram

```
Client Application
        ↓
  orders:8080 (stable address)
        ↓
    Listener
        ↓
  routing-key: orders
        ↓
  Skupper Network
        ↓
   ┌────┴────┐
   ↓         ↓
Connector  Connector
   ↓         ↓
Orders    Orders
  K8s     Podman
 (AWS)   (datacenter)
```

## Key Benefits

### Location Independence

The Orders service can move from AWS to datacenter, or be added in a third location, without any change to client applications or their configuration.

### Transparent Failover

If the Orders service in AWS becomes unavailable, the Skupper router automatically redirects new connections to the datacenter instance through the same listener endpoint.

### Zero Application Changes

Both consumer and provider applications use their native connectivity (HTTP, TCP, etc.) with no Skupper-specific libraries or protocols required.

### Platform Independence

The consumer might run on Kubernetes while providers run on Podman, VMs, or other platforms. The application network abstracts these differences.

## Comparison to Alternative Approaches

| Approach | Location Changes Require | Skupper Service Virtualization |
|----------|-------------------------|-------------------------------|
| **Direct IP addresses** | Update all consumers | No consumer changes |
| **DNS names** | DNS updates, cache wait time | No DNS changes needed |
| **Load balancer** | Load balancer reconfiguration | No load balancer reconfiguration |
| **Service mesh** | Works only within a cluster | Works across locations |
| **VPN + DNS** | VPN topology changes, DNS updates | Uses existing network, no DNS changes |

## When to Use This Pattern

- Services are deployed across multiple locations (cloud, datacenter, edge)
- Service placement may change over time
- Different environments use different deployment locations
- You need to avoid tight coupling between consumers and provider locations
- Platform heterogeneity (Kubernetes, VMs, Podman) needs to be abstracted

## When Skupper Complements Other Solutions

Service virtualization is about **location** abstraction. Skupper can be combined with:

- **API gateways**: Handle API versioning, authentication, rate limiting; Skupper connects gateway to backends
- **Service mesh**: Manages traffic within a cluster; Skupper connects across clusters
- **DNS**: Provides name resolution; Skupper provides location-transparent routing behind the name

## Example Scenarios

### Scenario 1: Hybrid Cloud Deployment

**Situation**: Orders service normally runs in the datacenter but needs to burst to cloud during peak load.

**Without Skupper**: Clients need to be configured with both datacenter and cloud endpoints, or a cross-location load balancer must be provisioned.

**With Skupper**: Listener provides single endpoint. Connector in datacenter and connector in cloud share the routing key. Skupper distributes new connections across both locations.

### Scenario 2: Incremental Migration

**Situation**: Migrating Orders service from VM-based deployment to Kubernetes.

**Without Skupper**: Big-bang cutover or complex DNS-based gradual rollout.

**With Skupper**: Deploy new Orders in Kubernetes with a connector. Both VM and Kubernetes connectors share the routing key. Remove VM connector when ready. Clients never see a change.

### Scenario 3: Development/Production Parity

**Situation**: Development environment needs to access production database API without modifying local config.

**Without Skupper**: Developers need VPN and production DNS configuration, or maintain separate config files.

**With Skupper**: Listener in development uses the same address as production. Connector in production exposes database API. Developer applications use the same configuration in both environments.

## Implementation Checklist

- [ ] Define stable routing key for the logical service
- [ ] Create listener in consumer location(s) with stable host/port
- [ ] Create connector(s) pointing to actual service workload
- [ ] Verify listener status shows as Ready (matching connector found)
- [ ] Test connection from consumer to listener endpoint
- [ ] Verify traffic reaches service provider
- [ ] Test relocation by adding connector in new location and removing old connector

## Related Patterns

- [Integration Layer](integration-layer.md): Service virtualization is a key component
- [Independent Microservice Placement](independent-service-placement.md): Enabled by location transparency
- [Boundaryless Information Flow](boundaryless-information-flow.md): Service virtualization supports flow across boundaries

## References

- [The Open Group SOA Reference Architecture](https://www.opengroup.org/soa/source-book/soa_refarch/p13.htm)
- [Skupper Listener Concept](../concepts/listener.md)
- [Skupper Connector Concept](../concepts/connector.md)
- [Skupper Routing Key Concept](../concepts/routing-key.md)
