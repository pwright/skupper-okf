# Resilient Parallel Service Instances Pattern

## Pattern Overview

The resilient parallel service instances pattern deploys multiple instances of a service across independent failure domains (locations, availability zones, clusters) to provide resilience through redundancy and automatic failover. When one instance becomes unavailable, traffic automatically routes to remaining instances without manual intervention.

**Reference**: [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)

## TOGAF Context

### Architecture Building Block

**Cross-location service resilience**: Services must maintain availability despite failure of individual instances, locations, or infrastructure components through redundant deployment and automatic failover.

### Solution Building Block

**Skupper multi-location routing**: Multiple service instances across locations share a routing key, with automatic connection distribution and failover when instances become unavailable.

## Problem Statement

Single points of failure create availability risk:

### Failure Domains

| Failure Type | Impact Without Resilience | Frequency |
|--------------|--------------------------|-----------|
| **Instance crash** | Service unavailable until restart | Common (bugs, OOM, etc.) |
| **Node failure** | All instances on node unavailable | Occasional (hardware, OS issues) |
| **Cluster failure** | Entire cluster unavailable | Rare (control plane issues) |
| **Availability zone failure** | Entire AZ unavailable | Very rare (infrastructure outage) |
| **Region failure** | Entire region unavailable | Extremely rare (disaster) |
| **Cloud provider outage** | All resources in provider unavailable | Rare (major incidents) |

### Traditional Resilience Solutions

| Approach | Limitation |
|----------|-----------|
| **Kubernetes replicas** | Only within a cluster; doesn't protect against cluster failure |
| **Multi-AZ deployment** | Within one cloud region; doesn't protect against region failure |
| **Load balancer with health checks** | Requires load balancer configuration; typically within one location |
| **DNS failover** | Slow (DNS TTL propagation); client-side caching issues |
| **Manual failover** | Requires human intervention; slow; risk of errors |

## Solution with Skupper

Skupper enables resilient service instances by:

1. **Multi-location deployment**: Instances across independent failure domains
2. **Shared routing key**: All instances appear as single logical service
3. **Automatic distribution**: New connections distributed across available instances
4. **Automatic failover**: Unavailable instances automatically bypassed
5. **Transparent recovery**: Recovered instances automatically receive traffic again

### Architecture Diagram

```
Client Application
        ↓
    Listener: payment:8080
        ↓
  Skupper Network
        ↓
   ┌────┼────┬─────┐
   ↓    ↓    ↓     ↓
Conn Conn Conn  Conn
 ↓    ↓    ↓     ↓
AWS  Azure GCP   DC
 ✓    ✗    ✓     ✓

(Azure instance failed, traffic automatically routes to AWS, GCP, DC)
```

## Resilience Patterns

### Pattern A: Active-Active Multi-Location

All instances actively serve traffic.

```
Primary Datacenter:
  - Payment Service (active)
  - Connector: payment

Secondary Datacenter:
  - Payment Service (active)
  - Connector: payment

Cloud DR Site:
  - Payment Service (active)
  - Connector: payment

Traffic distributed across all three locations
Any two locations can fail; service still available
```

**Characteristics**:
- Maximum resilience (survives multiple location failures)
- Highest cost (running instances in all locations)
- Even load distribution
- Fast recovery (instances already warm)

**Use when**:
- Availability is critical (99.99%+ SLA)
- Cost is not primary concern
- Geographic distribution beneficial for latency

### Pattern B: Active-Standby Multi-Location

Primary location serves traffic; secondary locations standby.

```
Primary Datacenter (cost: 1):
  - Payment Service (active)
  - Connector: payment

Secondary Cloud (cost: 100):
  - Payment Service (standby, minimal traffic)
  - Connector: payment

On primary failure:
  - Skupper detects primary unavailable
  - Routes all traffic to secondary
  - Secondary scales up to handle load
```

**Characteristics**:
- Good resilience (survives primary location failure)
- Lower cost (minimal instances in standby)
- Primary handles most traffic
- Slower recovery (standby must scale up)

**Use when**:
- Cost optimization important
- Some failover delay acceptable
- Geographic distribution not required for latency

### Pattern C: Active-Active Within Location, Active-Standby Across Locations

Multiple instances in primary location; standby in secondary location.

```
Primary Location:
  - Payment instances (replicas=5, active)
  - Connector: payment (cost: 1)

Secondary Location:
  - Payment instances (replicas=1, standby)
  - Connector: payment (cost: 100)

Failure scenarios:
- Instance fails: Other instances in primary location handle load
- Primary location fails: Secondary location takes over
```

**Characteristics**:
- Resilience at two levels (instance, location)
- Optimized cost (full scale primary, minimal standby)
- Appropriate for most applications

**Use when**:
- Balancing cost and resilience
- Primary location has capacity for normal operations
- DR capability required but full multi-location active-active not needed

### Pattern D: Multi-Region Active-Active with Affinity

Instances in multiple regions; traffic prefers closest region.

```
US-East:
  - Connector: api (cost: 1 for US clients)

EU-West:
  - Connector: api (cost: 1 for EU clients)

Asia-Pacific:
  - Connector: api (cost: 1 for APAC clients)

US clients preferentially route to US-East
If US-East fails, automatically route to EU-West or APAC
Same for other regions
```

**Characteristics**:
- Low latency (regional affinity)
- High availability (survives region failures)
- Geographic distribution

**Use when**:
- Global user base
- Latency requirements
- High availability SLA

## Failover Behavior

### Detection

Skupper detects instance unavailability through:

- **TCP health checks**: Connector cannot establish connections to backend
- **Connection failures**: Existing connections drop
- **Router communication**: Routers detect connector health status

### Failover Timing

```
Instance becomes unavailable
    ↓
Detection (typically seconds)
    ↓
Router marks connector unavailable
    ↓
New connections route to remaining connectors
    ↓
Existing connections: Depend on application retry behavior
```

**New connections**: Immediate failover (next connection attempt uses available instance)

**Existing connections**: May fail; application should retry (standard resilience pattern)

### Recovery

When failed instance recovers:

```
Instance becomes available
    ↓
Connector detects backend available
    ↓
Router marks connector available
    ↓
New connections begin distributing to recovered instance
    ↓
Gradual rebalancing (as existing connections close, new connections distribute evenly)
```

**Note**: No immediate rebalancing of existing connections. Recovery is gradual through natural connection churn.

## Implementation Example

### Setup

Deploy payment service across three locations:

```yaml
# AWS deployment
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: payment-aws
  namespace: aws-namespace
spec:
  routingKey: payment
  selector: app=payment
  port: 8080
---
# Azure deployment
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: payment-azure
  namespace: azure-namespace
spec:
  routingKey: payment
  selector: app=payment
  port: 8080
---
# Datacenter deployment
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: payment-dc
  namespace: dc-namespace
spec:
  routingKey: payment
  selector: app=payment
  port: 8080
---
# Client-side listener
apiVersion: skupper.io/v2alpha1
kind: Listener
metadata:
  name: payment
  namespace: client-namespace
spec:
  routingKey: payment
  host: payment.svc.cluster.local
  port: 8080
```

### Normal Operation

```
100 new connections:
├── 33 → AWS
├── 33 → Azure
└── 34 → Datacenter

All instances healthy and serving traffic
```

### Azure Failure

```
Azure connector becomes unavailable
    ↓
100 new connections:
├── 50 → AWS
└── 50 → Datacenter

Azure instances not receiving traffic
```

### Azure Recovery

```
Azure connector becomes available
    ↓
100 new connections:
├── 33 → AWS
├── 33 → Azure (resuming traffic)
└── 34 → Datacenter

Gradual rebalancing to equal distribution
```

## Testing Resilience

### Chaos Engineering Practices

Regularly test failover to verify behavior:

#### Test 1: Single Instance Failure

```bash
# Kill one pod/container instance
kubectl delete pod payment-abc123

# Verify:
# - Other instances in same location continue serving
# - No user-visible impact
# - New pod starts and joins rotation
```

#### Test 2: Connector Failure

```bash
# Delete connector to simulate connector failure
kubectl delete connector payment-aws

# Verify:
# - Traffic fails over to remaining locations
# - Application continues functioning
# - Monitoring detects the failure

# Restore connector
kubectl apply -f payment-aws-connector.yaml

# Verify:
# - Connector rejoins rotation
# - Traffic distributes to restored connector
```

#### Test 3: Location Failure

```bash
# Simulate entire location failure
# (In test environment, stop all instances and connector)

# Verify:
# - Traffic fails over to remaining locations
# - Application remains available
# - Alerts fire for location failure
# - Capacity in remaining locations sufficient
```

#### Test 4: Network Partition

```bash
# Simulate network partition between locations
# (Block Skupper link traffic)

# Verify:
# - Isolated location instances not reachable
# - Traffic routes to reachable locations
# - Recovery when network restored
```

### Metrics to Monitor

- **Connection distribution**: Verify even distribution across available instances
- **Failover events**: Count and timing of connector state changes
- **Recovery time**: Time from failure detection to traffic restoration
- **Error rates**: Application errors during failover
- **Capacity headroom**: Remaining locations can handle full load during failure

## Capacity Planning

### N+1 Capacity Model

Each location should be able to handle failure of one other location:

```
Normal load: 100 req/s distributed across 3 locations
├── AWS: 33 req/s
├── Azure: 33 req/s
└── DC: 34 req/s

One location fails: 100 req/s distributed across 2 locations
├── AWS: 50 req/s (capacity must support)
└── DC: 50 req/s (capacity must support)

Each location provisioned for:
  (Total load / (N - 1)) where N = number of locations
```

### N+2 for Critical Services

For highest availability, provision for two simultaneous location failures:

```
Normal load: 100 req/s across 3 locations

Two locations fail: 100 req/s on 1 location
└── DC: 100 req/s (must have capacity)

Each location provisioned for:
  (Total load / 1)  = full load
```

**Cost-benefit**: Expensive (3× capacity for normal load), but provides maximum resilience.

## Operational Considerations

### Monitoring

Monitor resilience health:

- **Instance health**: Are all instances healthy?
- **Connector status**: Are all connectors Ready?
- **Connection distribution**: Is traffic distributing as expected?
- **Failure detection time**: How quickly are failures detected?
- **Recovery time**: How quickly do recovered instances resume serving traffic?

### Alerting

Configure alerts for:

- **Connector unavailable**: Immediate alert when connector becomes unavailable
- **Location down**: All connectors in a location unavailable
- **Degraded capacity**: Fewer instances available than expected
- **Uneven distribution**: Traffic not distributing as expected (may indicate problem)

### Runbooks

Document procedures:

- **Instance failure**: Expected (automatic recovery); verify new instance joins
- **Connector failure**: Investigate connector; verify failover; restore connector
- **Location failure**: Major incident; verify remaining capacity; communicate SLA impact; plan restoration
- **Network partition**: Complex; may require manual intervention; coordinate with network team

### Cost Optimization

Balance resilience and cost:

- **Development/staging**: May not need multi-location resilience
- **Production non-critical**: Active-standby may be sufficient
- **Production critical**: Active-active justified by SLA
- **Production tier-1**: May justify N+2 capacity

## Security Considerations

### Data Consistency

Multiple instances serving same service:

- **Stateless services**: No consistency issues
- **Services with shared state**: Use distributed data store or database
- **Services with local cache**: Cache may be inconsistent across instances; design accordingly

### Session Management

User sessions across multiple instances:

- **Sticky sessions**: Not available with Skupper (connection-level distribution)
- **Shared session store**: Use Redis, Memcached, or database for session storage
- **Stateless authentication**: Use JWT or similar token-based auth

### Data Synchronization

If instances have local data:

- **Read replicas**: Acceptable if eventual consistency ok
- **Multi-master**: Complex; requires conflict resolution
- **Centralized data**: Prefer shared database over instance-local data

## Anti-Patterns

### ❌ Testing Failover Only in Production

Test failover regularly in non-production environments. Don't discover failover doesn't work during actual outage.

### ❌ Insufficient Capacity

Don't provision locations such that N-1 locations can't handle the load. Failover succeeds but service collapses under load.

### ❌ Shared Failure Domains

Don't deploy "multiple" instances that share infrastructure. Example: Multiple cloud regions but all in same cloud provider (provider-level outage still takes down all instances).

### ❌ Neglecting Data Consistency

Don't assume multiple instances will automatically have consistent data. Design for distributed data consistency.

## Implementation Checklist

- [ ] Identify critical services requiring resilience
- [ ] Determine failure domains (instances, locations, regions)
- [ ] Choose resilience pattern (active-active, active-standby, etc.)
- [ ] Calculate capacity requirements for N-1 or N-2 scenarios
- [ ] Deploy service instances across failure domains
- [ ] Create connectors in each location with shared routing key
- [ ] Create listeners at client locations
- [ ] Test normal operation (verify distribution)
- [ ] Test instance failure (kill pod, verify failover)
- [ ] Test location failure (stop entire location, verify failover)
- [ ] Test recovery (restore location, verify traffic resumes)
- [ ] Verify capacity during failure scenarios
- [ ] Configure monitoring and alerting
- [ ] Document runbooks for failure scenarios
- [ ] Schedule regular resilience testing (chaos engineering)

## Relationship to Other Patterns

- [Hybrid-cloud Elasticity](hybrid-cloud-elasticity.md): Provides elasticity; this pattern provides resilience
- [Service Virtualization](service-virtualization.md): Abstracts instances behind logical service identity
- [Independent Service Placement](independent-service-placement.md): Instances can be independently placed for resilience

## References

- [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)
- [Skupper Load Balancing](https://skupper.io/docs/overview/load-balancing.html)
- [Service Failover Capability](togaf-overview.md#service-failover)
