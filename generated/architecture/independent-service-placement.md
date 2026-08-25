# Independent Microservice Placement Pattern

## Pattern Overview

Independent microservice placement is an architectural principle from microservices architecture where each service can be deployed in the most appropriate location without constraint from application connectivity requirements. Services remain independently deployable and loosely coupled despite being distributed across multiple platforms and locations.

The core principle: **Deployment topology must not dictate application topology.**

**Reference**: [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)

## TOGAF Context

### Architecture Building Block

**Independent service deployment**: Microservices must be deployable independently in locations optimized for their requirements (cost, latency, compliance, resources) without breaking application connectivity.

### Solution Building Block

**Skupper application network**: Provides location-transparent connectivity so services can communicate regardless of where they are deployed.

## Problem Statement

Microservices architecture promises independent deployment, but network connectivity often creates hidden coupling:

### Placement Constraints

Services may have different optimal placement:

| Service | Optimal Placement | Reason |
|---------|------------------|---------|
| **Frontend** | Cloud (global CDN) | Low latency to users worldwide |
| **API Gateway** | Cloud (edge locations) | Close to users |
| **Business Logic** | Datacenter | Cost optimization |
| **Database** | Datacenter | Compliance, data residency |
| **ML Inference** | Cloud (GPU instances) | Specialized hardware |
| **Batch Processing** | Cloud (spot instances) | Cost for variable load |
| **Legacy Integration** | Datacenter | Must stay with legacy systems |

### Traditional Connectivity Creates Coupling

If services must be in the same network/cluster to communicate:

```
❌ All services must be in the same location
   ↓
Choice A: Everything in cloud (expensive for some services)
Choice B: Everything on-prem (no cloud capabilities)
Choice C: Complex VPN mesh between locations
Choice D: Services can't be independently placed
```

This violates the microservices principle of independent deployment.

## Solution with Skupper

Skupper provides location-transparent connectivity, allowing each service to be placed optimally while maintaining communication.

### Architecture Diagram

```
Frontend
(Cloud CDN)
    ↓
API Gateway
(Cloud Edge)
    ↓
┌───┴────┬──────────┬───────────┐
↓        ↓          ↓           ↓
Orders   Inventory  Payment  Analytics
(DC)     (Cloud)    (DC)     (Cloud/GPU)
↓        ↓          ↓           ↓
    Skupper Network
(location-transparent connectivity)
```

Each service is placed based on its requirements, not connectivity constraints.

## Key Principles

### 1. Logical Service Identity

Services are addressed by stable routing keys, not location-specific addresses.

```
Service calls: payment-service

This works whether payment-service runs:
- In the same Kubernetes cluster
- In a different cloud
- On a VM in the datacenter
- In a Podman container at the edge
```

### 2. Platform Independence

Services communicate using standard protocols (HTTP, gRPC, TCP) without platform-specific dependencies.

```
Frontend (Kubernetes) → Skupper → Orders (VM)

Orders sees standard HTTP requests, doesn't know Frontend is in Kubernetes
Frontend makes standard HTTP calls, doesn't know Orders is a VM
```

### 3. Independent Scaling

Each service scales independently in its optimal location.

```
Frontend:
  - Scales horizontally in cloud (autoscaling)

Orders:
  - Fixed capacity in datacenter (predictable load)

Analytics:
  - Scales up/down based on batch jobs (spot instances)
```

Skupper routing adapts as services scale; no reconfiguration needed.

### 4. Independent Deployment

Services can be deployed, updated, or relocated without affecting other services.

```
Deploy new Orders version in datacenter
  ↓
Skupper connector updated automatically (selectors pick up new pods/containers)
  ↓
Frontend continues calling through same listener
  ↓
Zero frontend changes needed
```

## Placement Decision Framework

### Factors to Consider

When deciding where to place each service:

#### Cost

- **Cloud**: Pay-per-use, expensive for constant load, cost-effective for variable load
- **Datacenter**: Fixed cost, efficient for constant load

#### Latency

- **User-facing services**: Close to users (cloud edge locations, CDN)
- **Internal services**: Close to dependencies (colocated with database)

#### Compliance

- **Data residency**: May require specific geographic locations
- **Regulatory requirements**: May mandate on-premises deployment

#### Resource Requirements

- **Specialized hardware**: GPU, TPU → Cloud (on-demand access)
- **High memory/CPU**: May be cheaper on-premises for constant use

#### Integration Requirements

- **Legacy systems**: Must be close to or able to reach legacy infrastructure
- **Partner APIs**: May need specific network access

#### Operational Concerns

- **Team expertise**: Some teams better with cloud, others with on-prem
- **Tooling**: CI/CD, monitoring may be platform-specific
- **Change velocity**: Services that change frequently may benefit from cloud agility

### Example Placement Matrix

```
Service         | Primary Factor    | Placement    | Backup
----------------|-------------------|--------------|------------------
Frontend        | User latency      | Cloud (CDN)  | Cloud (region)
API Gateway     | User latency      | Cloud (edge) | Cloud (region)
Orders API      | Cost + compliance | Datacenter   | Cloud (DR)
Inventory API   | Integration       | Datacenter   | (legacy system location)
Payment API     | Compliance (PCI)  | Datacenter   | Cloud (compliant region)
Analytics       | Resource (GPU)    | Cloud        | N/A (batch jobs)
Notification    | Cost (variable)   | Cloud        | N/A (send-only)
```

## Implementation Patterns

### Pattern A: Cloud Frontend, Datacenter Backend

**Common for**: Cost optimization, compliance

```
Cloud:
  - Frontend (user-facing, autoscaling)
  - API Gateway (rate limiting, auth)
  - Listener: backend-apis

Datacenter:
  - Business services (stable, predictable)
  - Databases (compliance, data residency)
  - Connector: backend-apis

Cost savings: Datacenter cheaper for constant backend load
User experience: Cloud provides low latency frontend
```

### Pattern B: Multi-Cloud Service Distribution

**Common for**: Avoiding cloud lock-in, geographic distribution

```
AWS:
  - Services A, B
  - Connectors: service-a, service-b

Azure:
  - Services C, D
  - Connectors: service-c, service-d

GCP:
  - Services E, F
  - Connectors: service-e, service-f

Each cloud:
  - Listeners for all other services

Services communicate regardless of cloud
Each service placed in most cost-effective cloud
```

### Pattern C: Specialized Resource Placement

**Common for**: ML, batch processing, specialized workloads

```
Standard compute (Datacenter):
  - Most services
  - Listener: ml-inference

Specialized compute (Cloud GPU):
  - ML Inference Service
  - Connector: ml-inference

ML service has GPU access
Other services call ML service through Skupper
No need to deploy everything in expensive GPU environment
```

### Pattern D: Gradual Cloud Migration

**Common for**: Risk reduction during migration

```
Phase 1: All services in datacenter
  - Services A, B, C, D, E

Phase 2: Move user-facing services to cloud
  - Cloud: A, B (with listeners for C, D, E)
  - Datacenter: C, D, E (with connectors)

Phase 3: Move business logic to cloud
  - Cloud: A, B, C, D (with listener for E)
  - Datacenter: E (with connector)

Phase 4: All services in cloud
  - Cloud: A, B, C, D, E

Each phase preserves connectivity
Services remain independently deployable
Can pause or reverse migration at any phase
```

## Example Scenarios

### Scenario 1: E-Commerce Application

**Requirements**:
- Frontend: Low latency globally
- Checkout: PCI compliance (on-prem)
- Inventory: Integrate with warehouse system (on-prem)
- Recommendations: ML inference (GPU)

**Placement**:
```
Cloud (Global CDN):
  - Frontend SPA
  - Listener: checkout
  - Listener: inventory
  - Listener: recommendations

Cloud (GPU instances):
  - Recommendations Service
  - Connector: recommendations

Datacenter:
  - Checkout Service (PCI environment)
  - Connector: checkout
  - Inventory Service
  - Connector: inventory
  - Warehouse Integration

Skupper Network connects all locations
```

**Outcome**: Each service in optimal location; connectivity preserved.

### Scenario 2: SaaS Application with Regional Data

**Requirements**:
- User data must stay in specific regions (GDPR, etc.)
- Application logic can run anywhere
- Analytics runs in cloud (big data processing)

**Placement**:
```
EU Region (Datacenter):
  - EU Customer Database
  - Connector: eu-customer-data

US Region (Datacenter):
  - US Customer Database
  - Connector: us-customer-data

Application Services (Cloud):
  - API Gateway
  - Business Logic
  - Listener: eu-customer-data
  - Listener: us-customer-data

Analytics (Cloud):
  - Analytics Service
  - Listener: eu-customer-data
  - Listener: us-customer-data

Data stays in compliant regions
Application logic in cost-effective cloud
Analytics has access to data through Skupper
```

### Scenario 3: Microservices with Mixed Maturity

**Requirements**:
- New services: Cloud-native, Kubernetes
- Existing services: VMs, not yet containerized
- Legacy services: Bare metal, not moving soon

**Placement**:
```
Kubernetes (Cloud):
  - New microservices (A, B, C)
  - Connectors: service-a, service-b, service-c

VMs (Datacenter):
  - Existing services (D, E)
  - Connectors: service-d, service-e

Bare Metal (Datacenter):
  - Legacy service (F)
  - Connector: service-f

All locations:
  - Listeners for services they depend on

Mixed platform architecture
Each service uses appropriate platform
Connectivity independent of platform choice
```

## Operational Considerations

### Service Discovery

With services in many locations, discovery is important:

- **Static configuration**: Services configured with known routing keys
- **Service catalog**: Maintain catalog of available services and their routing keys
- **Network Observer API**: Query Skupper for available services

### Deployment Coordination

Independent deployment doesn't mean uncoordinated deployment:

- **API contracts**: Services must maintain compatible APIs
- **Versioning**: Use API versioning for breaking changes
- **Gradual rollout**: Deploy to one location, verify, deploy to others
- **Feature flags**: Control feature availability independently of deployment

### Monitoring and Observability

Track services across locations:

- **Distributed tracing**: Correlate requests across services in different locations
- **Centralized logging**: Aggregate logs from all locations
- **Metrics aggregation**: Combine metrics from all service instances
- **Service health**: Monitor health of services and Skupper connectivity

### Cost Tracking

Understand placement cost implications:

- **Cloud costs**: Track by service (compute, storage, network egress)
- **Datacenter costs**: Allocate fixed costs to services
- **Network transfer**: Monitor Skupper cross-location traffic costs
- **Total cost of ownership**: Include operational complexity in cost calculations

## Benefits

### Optimal Cost

Each service runs where it's most cost-effective:
- Constant load → Datacenter (fixed cost)
- Variable load → Cloud (pay-per-use)
- Specialized resources → Cloud (avoid CapEx for specialized hardware)

### Regulatory Compliance

Services with compliance requirements can be placed appropriately without constraining other services.

### Performance Optimization

- User-facing services close to users
- Data-heavy processing close to data
- Specialized compute available where needed

### Technology Flexibility

- New services can use new platforms (Kubernetes, serverless)
- Existing services can stay on proven platforms
- No forced migration for connectivity reasons

### Risk Reduction

- Gradual migrations rather than big-bang
- Mix of cloud and on-prem for resilience
- Ability to move services if requirements change

## Limitations and Considerations

### Network Latency

Services in different locations have higher latency than colocated services:

- Measure actual latency for critical paths
- Consider caching or data replication for read-heavy patterns
- Minimize chatty protocols across locations

### Data Gravity

Services that process large amounts of data should be close to the data:

- Analytics service should be near database
- Batch processing should be near data source
- Consider data transfer costs

### Complexity

Independent placement adds operational complexity:

- More deployment targets
- More monitoring endpoints
- More potential failure modes
- Document service locations and dependencies

## Implementation Checklist

- [ ] Identify placement factors for each service (cost, latency, compliance, resources)
- [ ] Document optimal placement for each service
- [ ] Design Skupper network topology to connect placements
- [ ] Deploy services to their optimal locations
- [ ] Create connectors for each service at its location
- [ ] Create listeners at consumer locations
- [ ] Test cross-location communication
- [ ] Measure latency for critical paths
- [ ] Verify compliance requirements met
- [ ] Monitor cost by service and location
- [ ] Document service placement rationale
- [ ] Create runbooks for service relocation

## Relationship to Other Patterns

- [Service Virtualization](service-virtualization.md): Foundation enabling independent placement
- [Hybrid-cloud Elasticity](hybrid-cloud-elasticity.md): Services can be placed and scaled across locations
- [Boundaryless Information Flow](boundaryless-information-flow.md): Enables communication despite independent placement

## References

- [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)
- [Skupper Concepts](https://skupper.io/docs/refdog/concepts/)
- [Platform-Independent Connectivity](togaf-overview.md#platform-independent-connectivity)
