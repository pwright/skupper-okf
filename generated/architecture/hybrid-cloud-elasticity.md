# Hybrid-Cloud Elasticity Pattern

## Pattern Overview

Hybrid-cloud elasticity is the architectural capability to dynamically distribute workloads between on-premises infrastructure and cloud environments based on demand, cost, or other operational factors. Services can preferentially run in one location (typically on-premises) with the ability to burst or fail over to another location (typically cloud) when needed.

This pattern addresses a core enterprise requirement: **Compute placement shall vary independently of service consumption.**

**Reference**: [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)

## TOGAF Context

### Architecture Building Block

**Elastic hybrid-cloud placement**: Services must be able to scale across on-premises and cloud environments with automatic load distribution and location preference.

### Solution Building Block

**Skupper multi-location routing**: Multiple service instances in different locations share a routing key, with connection distribution and optional location preference via routing cost.

## Problem Statement

Organizations want to:

- Run workloads on-premises for cost, compliance, or latency reasons
- Burst to cloud during peak demand periods
- Maintain capacity for failover without running duplicate infrastructure constantly
- Avoid lock-in to a single cloud provider
- Balance cost (on-premises cheaper for baseline) with agility (cloud for spikes)

Traditional solutions require:

- **Cloud load balancers**: Expensive for cross-region/cross-cloud; don't support hybrid deployments
- **Global server load balancing (GSLB)**: DNS-based; long TTLs cause slow failover; client-side caching issues
- **Application-level retry**: Complexity in every application; inconsistent behavior
- **Infrastructure reconfiguration**: Manual or slow automation to shift traffic

## Solution with Skupper

Skupper enables hybrid-cloud elasticity through:

1. **Multi-location service**: Multiple connectors share the same routing key across locations
2. **Connection distribution**: Skupper router distributes new connections across available instances
3. **Automatic failover**: Unavailable instances are automatically bypassed
4. **Location preference**: Routing cost allows preferential use of specific locations

### Architecture Diagram

```
Client Application
        ↓
    Listener: orders:8080
        ↓
  Skupper Network
        ↓
   ┌────┴────────┐
   ↓             ↓
Connector      Connector
(cost: 1)     (cost: 10)
   ↓             ↓
Orders        Orders
Datacenter    Cloud
[Preferred]   [Overflow]
```

In normal operation, new connections prefer the datacenter instance (lower cost). When datacenter capacity is exhausted or unavailable, connections route to cloud.

## Key Components

### 1. Shared Routing Key

All service instances (datacenter and cloud) use the same routing key:

```yaml
# Both connectors use the same routing key
routingKey: orders
```

This creates a **logical service** that spans locations.

### 2. Multiple Connectors

Each location deploys a connector pointing to its local service instance:

```yaml
# Datacenter connector
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: orders-datacenter
  namespace: datacenter
spec:
  routingKey: orders
  selector: app=orders
  port: 8080
```

```yaml
# Cloud connector
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: orders-cloud
  namespace: cloud
spec:
  routingKey: orders
  selector: app=orders
  port: 8080
```

### 3. Location Preference via Routing Cost

Site links can be assigned routing costs to influence routing decisions:

```yaml
# Link from client site to datacenter
apiVersion: skupper.io/v2alpha1
kind: Link
metadata:
  name: to-datacenter
spec:
  cost: 1  # Lower cost = preferred
```

```yaml
# Link from client site to cloud
apiVersion: skupper.io/v2alpha1
kind: Link
metadata:
  name: to-cloud
spec:
  cost: 10  # Higher cost = used when preferred unavailable
```

### 4. Single Listener

Client applications use a single listener endpoint regardless of which location serves the request:

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

## Traffic Distribution Behavior

### Normal Operation (Datacenter Available)

```
100 new connections arrive
├─ 100 → Datacenter (cost: 1)
└─   0 → Cloud (cost: 10)
```

### Datacenter at Capacity

When datacenter connector reaches maximum connections, overflow routes to cloud:

```
100 new connections arrive
├─ 60 → Datacenter (at capacity)
└─ 40 → Cloud (overflow)
```

### Datacenter Unavailable

When datacenter connector is completely unavailable:

```
100 new connections arrive
├─   0 → Datacenter (unavailable)
└─ 100 → Cloud (active failover)
```

### Gradual Recovery

As datacenter recovers, **new** connections prefer datacenter again. Existing cloud connections remain until they close naturally.

## Use Cases

### Use Case 1: Cost Optimization with Burst Capacity

**Scenario**: E-commerce site with predictable baseline load but occasional spikes (product launches, sales events).

**Implementation**:
- Run baseline capacity in datacenter (cheaper for constant load)
- Cloud capacity available but scaled to zero normally
- During spikes, scale cloud instances to handle overflow
- After spike, scale cloud back to zero

**Benefit**: Pay datacenter baseline cost + cloud burst cost only when needed, rather than constant cloud cost for peak capacity.

### Use Case 2: Gradual Cloud Migration

**Scenario**: Organization migrating from datacenter to cloud but wants to derisk the transition.

**Implementation**:
- Phase 1: 100% datacenter, cloud available as failover
- Phase 2: 50/50 split to test cloud under load
- Phase 3: Prefer cloud, datacenter as failover
- Phase 4: 100% cloud, retire datacenter

**Benefit**: Gradual migration with instant rollback capability at any phase.

### Use Case 3: Multi-Cloud Resilience

**Scenario**: Run services across AWS and Azure to avoid single-cloud dependency.

**Implementation**:
- Primary instances in AWS (cost: 1)
- Secondary instances in Azure (cost: 10)
- Automatic failover if AWS region issue
- Can manually adjust costs to shift preference

**Benefit**: Cloud provider resilience without application-level multi-cloud awareness.

### Use Case 4: Compliance and Performance Balance

**Scenario**: Financial services app must keep some data on-premises (compliance) but wants cloud bursting for compute.

**Implementation**:
- Database remains in datacenter (compliance requirement)
- Application tier runs in datacenter (preferred, close to data)
- Cloud application tier available for compute bursting
- All app tiers connect to datacenter database through Skupper

**Benefit**: Meet compliance requirements while gaining cloud burst capacity.

## Configuration Patterns

### Pattern A: Equal Distribution

No routing costs configured. Connections distribute roughly evenly across locations.

**Use when**: Both locations have equal cost and performance characteristics.

```
Datacenter (cost: default)
Cloud (cost: default)
→ ~50/50 distribution
```

### Pattern B: Strong Preference

Large cost difference creates strong preference with failover.

**Use when**: Want to use one location almost exclusively unless unavailable.

```
Datacenter (cost: 1)
Cloud (cost: 100)
→ 100% datacenter unless unavailable
```

### Pattern C: Gradual Spillover

Moderate cost difference allows controlled spillover under load.

**Use when**: Want preference but expect regular overflow.

```
Datacenter (cost: 1)
Cloud (cost: 5)
→ Prefer datacenter, overflow to cloud sooner
```

### Pattern D: Multi-Region Active-Active

Multiple regions with similar costs for geographic distribution.

**Use when**: Global application with regional presence.

```
US-East (cost: 1)
EU-West (cost: 1)
Asia-Pacific (cost: 1)
→ Distribute based on router proximity
```

## Operational Considerations

### Monitoring

Monitor connection distribution to verify behavior:

- Current connections per location
- Connection rate per location
- Failover events (transitions from preferred to fallback)
- Cost values in effect
- Connector availability status

### Capacity Planning

- Set datacenter capacity to expected baseline + buffer
- Set cloud capacity to handle expected peak - baseline
- Test failover regularly to verify cloud capacity sufficient
- Monitor actual vs. expected distribution

### Cost Management

Track costs by location:

- Datacenter: Fixed cost (mostly)
- Cloud: Variable cost based on actual usage
- Network transfer costs (watch cross-region/cross-cloud traffic)

### Scaling Automation

Automate cloud scaling based on load:

```
IF datacenter_utilization > 80%:
    scale_cloud_to(expected_overflow_capacity)
ELSE:
    scale_cloud_to(minimal_capacity)
```

## Performance Characteristics

### Latency

- **Intra-site latency**: Minimal (local connection through Skupper router)
- **Cross-site latency**: Depends on network path between sites
- **Consideration**: If latency-sensitive, prefer location closer to clients

### Throughput

- Skupper router throughput typically not the bottleneck
- Actual service capacity determines throughput
- Monitor router resource usage if handling extremely high connection rates

### Connection Distribution Timing

- Distribution decisions made when **new** connections are established
- Existing connections remain on current instance
- Gradual rebalancing as connections naturally close and new ones open

## Security Considerations

### Data Residency

If data residency requirements exist:

- Ensure cloud instances in compliant regions
- Or, keep data tier in datacenter and only burst compute tier to cloud
- Audit data flows to verify compliance

### Access Controls

- Both locations should have equivalent authentication/authorization
- Credentials/secrets management for multi-location deployment
- Consider different network security postures (datacenter vs. cloud)

### Encryption

- Skupper encrypts cross-site traffic (mutual TLS)
- May still want application-level encryption for sensitive data
- Monitor certificate expiration and rotation

## Integration with Auto-Scaling

Skupper complements platform auto-scaling:

```
Kubernetes HPA/VPA
    ↓
Scales pods in each location
    ↓
Skupper connectors detect new pods
    ↓
Router includes new instances in distribution
```

Skupper distributes traffic across locations; platform auto-scaler scales instances within each location.

## Troubleshooting

### Issue: Cloud not receiving overflow traffic

**Check**:
- Routing cost configured correctly (higher cost for overflow)
- Cloud connector status is Ready
- Cloud service instances are actually running and healthy
- Site link to cloud is active

### Issue: Uneven distribution despite equal costs

**Check**:
- Router connection distribution algorithm (may not be purely round-robin)
- Connection lifetime (long-lived connections create imbalance)
- Client-side connection pooling (may concentrate connections)

### Issue: Slow failover during datacenter outage

**Check**:
- Connector health check interval (how quickly router detects unavailability)
- Existing connections may remain on datacenter temporarily before timing out
- New connections should route to cloud immediately once datacenter detected unavailable

## Implementation Checklist

- [ ] Define routing key for the logical service
- [ ] Deploy service instances in datacenter
- [ ] Deploy service instances in cloud
- [ ] Create connectors in both locations with shared routing key
- [ ] Configure site links with appropriate routing costs
- [ ] Create listener at client location
- [ ] Test connection distribution under normal load
- [ ] Test failover (stop datacenter instances, verify cloud takeover)
- [ ] Test recovery (restart datacenter, verify preference returns)
- [ ] Document cost structure (datacenter baseline + cloud burst)
- [ ] Set up monitoring for location distribution
- [ ] Configure auto-scaling policies for cloud instances
- [ ] Create runbooks for manual traffic shifting (cost adjustments)

## Related Patterns

- [Service Virtualization](service-virtualization.md): Abstracts location from clients
- [Resilient Service Instances](resilient-service-instances.md): Related resilience pattern
- [Independent Microservice Placement](independent-service-placement.md): Enables placement flexibility

## References

- [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)
- [Skupper Routing](https://skupper.io/docs/overview/routing.html)
- [Skupper Load Balancing](https://skupper.io/docs/overview/load-balancing.html)
