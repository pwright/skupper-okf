# Integration Layer Pattern

## Pattern Overview

The Integration Layer is a fundamental architectural pattern from The Open Group SOA Reference Architecture. It provides the infrastructure for integration and communication between application building blocks, enabling services to discover, interact with, and compose each other.

Importantly, **Skupper provides one subset of the Integration Layer**: the connectivity, routing, and secure transport capabilities. It does not replace ESBs, message brokers, or API management platforms.

**Reference**: [The Open Group SOA Reference Architecture - Using TOGAF for SOA](https://www.opengroup.org/soa/source-book/togaf/p4.htm)

## TOGAF Context

### Architecture Building Block

**Integration infrastructure**: Services require infrastructure for communication, routing, transformation, orchestration, and composition.

### Solution Building Block

**Skupper for connectivity**: Skupper provides the application network connectivity, service endpoint abstraction, and secure routing portions of the integration layer.

## Integration Layer Capabilities

The Open Group defines the Integration Layer as including:

```
Integration Layer
├── Service communication       ← Skupper
├── Service endpoint abstraction ← Skupper
├── Routing and addressing      ← Skupper
├── Secure transport            ← Skupper
├── Message transformation      ← NOT Skupper
├── Service composition         ← NOT Skupper
├── Process orchestration       ← NOT Skupper
├── Complex event processing    ← NOT Skupper
└── API management              ← NOT Skupper
```

This distinction is critical: Skupper is **not an ESB**. It provides the network-level connectivity that sits underneath integration components.

## Skupper's Role in the Integration Layer

### What Skupper Provides

#### 1. Service Communication

Skupper enables distributed services to communicate regardless of their deployment location or platform.

```
Service A (Cloud) → Listener → Skupper Network → Connector → Service B (Datacenter)
```

**Value**: Services can be deployed independently and communicate transparently.

#### 2. Service Endpoint Abstraction

Listeners abstract service endpoints from consumers, allowing providers to move or scale without affecting consumers.

```
Consumer → orders:8080 (stable endpoint)
          ↓
      Routing key: orders
          ↓
  Actual endpoint changes transparently
```

**Value**: Endpoint location changes don't require consumer updates.

#### 3. Routing and Load Distribution

Skupper routers forward connections to appropriate service instances, distributing load across available providers.

```
Multiple backends share routing key
       ↓
Router distributes connections
       ↓
Load balanced across instances
```

**Value**: Built-in load distribution without external load balancer.

#### 4. Secure Transport

All cross-site communication is encrypted using mutual TLS, providing secure transport without application-level implementation.

```
Site A ←[mutual TLS]→ Site B
```

**Value**: Security is handled at the network layer, not in each application.

### What Skupper Does Not Provide

#### Message Transformation

Skupper does not inspect, parse, or transform message content. Services communicate using their native protocols.

**For transformation**, use:
- Message brokers (RabbitMQ, Kafka)
- Integration platforms (Apache Camel, MuleSoft)
- API gateways with transformation capabilities

#### Service Composition

Skupper does not orchestrate calls to multiple services or implement composition patterns like scatter-gather or aggregate.

**For composition**, use:
- Workflow engines
- Orchestration platforms (Temporal, Camunda)
- Service mesh (within a cluster)
- Application-level composition logic

#### Process Orchestration

Skupper does not manage multi-step business processes or maintain process state.

**For orchestration**, use:
- Business process management (BPM) platforms
- Workflow engines
- Event-driven orchestration platforms

#### API Management

Skupper does not provide API versioning, rate limiting, API keys, or developer portals.

**For API management**, use:
- API gateways (Kong, Apigee, AWS API Gateway)
- Skupper connects API gateway to backend services

## Integration Patterns with Skupper

### Pattern 1: Skupper Connects ESB Components

An ESB deployed across multiple locations needs its components to communicate.

```
Location A:
  - ESB Gateway
  - Listener: esb-broker

Location B:
  - ESB Message Broker
  - Connector: esb-broker

ESB components communicate through Skupper
ESB handles transformation, orchestration, routing logic
Skupper provides the cross-location connectivity
```

### Pattern 2: Skupper Connects API Gateway to Backends

API gateway in cloud needs to reach backend services in datacenter.

```
Cloud:
  - API Gateway (handles auth, rate limiting, versioning)
  - Listener: orders
  - Listener: inventory

Datacenter:
  - Orders Service
  - Connector: orders
  - Inventory Service
  - Connector: inventory

API Gateway → Skupper → Backend Services
```

**Division of responsibility**:
- API Gateway: API management, authentication, rate limiting
- Skupper: Connectivity from gateway to backends
- Backend services: Business logic

### Pattern 3: Skupper Connects to Message Broker

Applications in multiple locations need to publish/subscribe to a central message broker.

```
Cloud Applications:
  - Listener: kafka-broker:9092

Datacenter:
  - Kafka Cluster
  - Connector: kafka-broker:9092

Cloud applications publish/subscribe through Skupper
Kafka handles message queuing, topics, partitions
Skupper provides connectivity to Kafka
```

### Pattern 4: Skupper Enables Distributed Microservices

Microservices span multiple locations and need service-to-service communication.

```
Location A:
  - Frontend (calls Orders, Inventory)
  - Listener: orders
  - Listener: inventory

Location B:
  - Orders Service (calls Inventory)
  - Connector: orders
  - Listener: inventory

Location C:
  - Inventory Service
  - Connector: inventory

Skupper provides service mesh-like connectivity across locations
Service mesh (if used) operates within each location
```

## Architecture Layers

Understanding where Skupper sits in the overall architecture:

```
┌─────────────────────────────────────┐
│     Application Services            │  Business logic
├─────────────────────────────────────┤
│  Integration Middleware             │  ESB, message brokers,
│  (Transformation, Orchestration)    │  workflow engines
├─────────────────────────────────────┤
│  Skupper Application Network        │  ← Connectivity layer
│  (Connectivity, Routing, Security)  │
├─────────────────────────────────────┤
│  Infrastructure Network             │  IP networks, VPNs,
│  (IP, DNS, Firewalls)               │  cloud networks
└─────────────────────────────────────┘
```

Skupper sits **above** infrastructure networking but **below** integration middleware and application services.

## Integration Scenarios

### Scenario 1: Hybrid Integration Platform

**Situation**: Integration platform with on-premises ESB and cloud-based API gateway needs to work together.

**Without Skupper**:
- VPN between cloud and datacenter
- Or, expose ESB endpoints publicly
- Complex network configuration for each integration flow

**With Skupper**:
```
Cloud:
  - API Gateway
  - Listener: esb-services

Datacenter:
  - ESB
  - Connector: esb-services
  - Listener: cloud-apis

Integration components communicate through Skupper
Each component handles its integration responsibilities
Skupper provides network-level connectivity
```

### Scenario 2: Multi-Cloud Message Backbone

**Situation**: Message-driven architecture with services across AWS, Azure, and on-premises. Central message broker in datacenter.

**Without Skupper**:
- Expose message broker publicly (security risk)
- Or, VPN from each cloud to datacenter
- Or, replicate broker in each cloud (consistency issues)

**With Skupper**:
```
Datacenter:
  - Kafka Cluster
  - Connector: kafka:9092

AWS:
  - Services A, B
  - Listener: kafka:9092

Azure:
  - Services C, D
  - Listener: kafka:9092

All services reach Kafka through Skupper
Kafka remains private in datacenter
No public exposure or complex VPN mesh
```

### Scenario 3: Service Mesh Federation

**Situation**: Service meshes deployed in multiple Kubernetes clusters need cross-cluster communication.

**Without Skupper**:
- Service mesh federation features (complex, mesh-specific)
- Or, expose services at cluster boundaries
- Or, VPN between clusters

**With Skupper**:
```
Cluster A (Service Mesh A):
  - Services within cluster use service mesh
  - Export services via Skupper connectors

Cluster B (Service Mesh B):
  - Services within cluster use service mesh
  - Import services via Skupper listeners

Within cluster: Service mesh manages traffic
Across clusters: Skupper provides connectivity
```

**Benefit**: Service mesh and Skupper handle their respective domains; cleaner separation of concerns.

## Capabilities Mapping

| Capability | TOGAF Integration Layer | Skupper | Complementary Technology |
|------------|------------------------|---------|-------------------------|
| **Service discovery** | ✓ Required | Listeners provide stable endpoints | Service registries, DNS |
| **Message routing** | ✓ Required | Routing keys, connection distribution | Message brokers, ESB |
| **Secure transport** | ✓ Required | ✓ Mutual TLS | API gateways, service mesh |
| **Protocol mediation** | ✓ Required | ✗ Transparent proxy | ESB, API gateway |
| **Message transformation** | ✓ Required | ✗ No inspection | ESB, integration platforms |
| **Service orchestration** | ✓ Required | ✗ Point-to-point only | Workflow engines, BPM |
| **Event processing** | ✓ Required | ✗ No event semantics | CEP platforms, stream processing |
| **Transaction management** | ✓ Optional | ✗ No transaction context | Transaction managers, databases |
| **API management** | ✓ Optional | ✗ No API versioning/keys | API gateways |

## When to Use Skupper in Integration Architecture

### Good Fit

- Services are distributed across multiple locations
- Need connectivity without VPN complexity
- Integration middleware needs cross-location communication
- API gateway needs to reach backends in different locations
- Message broker needs to be accessible from remote locations

### Not the Right Tool

- Need message transformation or protocol conversion → Use ESB/integration platform
- Need process orchestration → Use workflow engine
- Need API versioning and developer portal → Use API gateway
- Need complex event processing → Use CEP platform
- All services within single Kubernetes cluster → Use service mesh

### Complement to Integration Middleware

Skupper works best **alongside** integration middleware:

```
Integration Requirement: Transform XML to JSON and route to appropriate service

Solution Architecture:
1. ESB receives XML message
2. ESB transforms XML → JSON
3. ESB routes to service based on business rules
4. Skupper provides connectivity if service is in remote location

Skupper role: Connectivity from ESB to remote service
ESB role: Transformation and business routing logic
```

## Design Considerations

### Network Topology

Plan Skupper network topology to support integration flows:

- **Hub-and-spoke**: Central integration hub with remote services
- **Mesh**: Integration components distributed across locations
- **Tiered**: Hierarchical integration layers

### Service Exposure

Be intentional about which services are exposed across locations:

- **Internal services**: May not need cross-location exposure
- **Integration endpoints**: Likely need exposure
- **Databases**: Consider if direct access or API wrapper is better

### Security Zones

Map Skupper links to security zones:

```
Public Zone ←[Skupper]→ DMZ ←[Skupper]→ Internal Zone

Connectors in each zone expose only appropriate services
Listeners in each zone access only authorized services
```

### Performance

Consider latency and throughput for integration patterns:

- **Synchronous integration**: Latency-sensitive; prefer colocated services
- **Asynchronous integration**: More tolerant of latency; message broker in one location ok
- **High-volume integration**: Monitor Skupper router throughput

## Implementation Checklist

- [ ] Identify integration requirements and flows
- [ ] Determine which capabilities need integration middleware vs. Skupper
- [ ] Map services to locations
- [ ] Design Skupper network topology
- [ ] Deploy integration middleware components
- [ ] Create Skupper connectors for services that need cross-location access
- [ ] Create Skupper listeners where integration components consume remote services
- [ ] Verify integration flows work across Skupper network
- [ ] Test failure scenarios (site unavailable, service unavailable)
- [ ] Monitor integration flow performance
- [ ] Document which services are exposed and why

## Anti-Patterns to Avoid

### ❌ Using Skupper as an ESB

Don't try to implement transformation, routing logic, or orchestration with Skupper. Use actual integration middleware and connect it via Skupper.

### ❌ Exposing Too Much

Don't create connectors for every service. Only expose services that actually need cross-location access from integration flows.

### ❌ Ignoring Integration Middleware

Don't bypass proper integration middleware thinking Skupper is sufficient. Skupper provides connectivity; you still need transformation, orchestration, etc.

### ❌ Point-to-Point Integration Sprawl

Use Skupper to connect integration hubs or middleware, not to create N² point-to-point connections between all services.

## Relationship to Other Patterns

- [Service Virtualization](service-virtualization.md): Core capability provided by Integration Layer
- [Boundaryless Information Flow](boundaryless-information-flow.md): Integration Layer enables flow across boundaries
- [Legacy Modernization](legacy-modernization.md): Integration Layer connects modern and legacy systems

## References

- [The Open Group SOA Reference Architecture](https://www.opengroup.org/soa/source-book/soa_refarch)
- [Using TOGAF for SOA](https://www.opengroup.org/soa/source-book/togaf/p4.htm)
- [Skupper Concepts](https://skupper.io/docs/refdog/concepts/)
