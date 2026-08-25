# Legacy Modernization / Wrapper Pattern

## Pattern Overview

The legacy modernization pattern involves wrapping existing applications with new services or APIs rather than replacing them immediately. This allows incremental modernization where new components interact with legacy systems during a transition period.

The critical challenge that often appears immediately after creating a wrapper is: **How does the new component securely reach the old system without flattening networks, opening inbound firewall ports, or relocating the legacy workload?**

**Reference**: [The Open Group - Using TOGAF for SOA](https://www.opengroup.org/soa/source-book/togaf/p4.htm)

## TOGAF Context

### Architecture Building Block

**Legacy system integration**: New service-oriented components must be able to interact with existing applications without requiring those applications to be relocated, refactored, or exposed to public networks.

### Solution Building Block

**Skupper application network**: Connects new wrappers to legacy systems privately using listeners and connectors, without requiring inbound firewall rules or VPN configuration.

## Problem Statement

Organizations have legacy applications that:

- Run on specific platforms (VMs, bare metal, older container systems)
- Cannot easily be moved to cloud or Kubernetes
- Should not be exposed to public networks due to security requirements
- Lack modern API interfaces
- Are scheduled for eventual replacement but must continue operating during modernization

Common modernization approaches create a wrapper service that:

- Provides a modern API (REST, gRPC, etc.)
- Translates requests to the legacy system's protocol
- Implements modern authentication and authorization
- May add caching, monitoring, or other cross-cutting concerns

But this creates a **connectivity problem**: the wrapper (often deployed in cloud or Kubernetes) needs to reach the legacy system (typically in a datacenter or private network).

### Traditional Solutions and Their Drawbacks

| Approach | Drawback |
|----------|----------|
| **Expose legacy system publicly** | Security risk; legacy systems often not hardened for internet exposure |
| **VPN between wrapper and legacy** | Complex to configure; can create broad network access rather than scoped service access |
| **Relocate legacy system** | May not be technically feasible; disrupts operations |
| **Flatten network boundaries** | Security teams resist; violates network segmentation principles |
| **Reverse proxy with public IP** | Requires public endpoint; firewall rule changes |

## Solution with Skupper

Skupper solves this by creating an **outbound-only connection** from the legacy location to the wrapper location, then routing wrapper traffic back through that connection.

### Architecture Diagram

```
New Application (Cloud/K8s)
          ↓
    Modern Wrapper
          ↓
    Listener: legacy-db:5432
          ↓
    Skupper Network
          ↓
    [Outbound-only link]
          ↓
    Connector: legacy-db
          ↓
    Legacy Database
    (Private datacenter)
```

### Key Components

#### 1. Connector at Legacy Location

The connector runs at the legacy system's location and establishes an **outbound** connection to the Skupper network. No inbound firewall rules are required.

```yaml
# In datacenter namespace
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: legacy-orders-db
spec:
  routingKey: orders-db
  host: legacy-db.internal.corp
  port: 5432
```

This connector:
- Connects to `legacy-db.internal.corp:5432` (the actual legacy system)
- Uses outbound-only connection to Skupper network
- No changes to legacy system firewall rules required

#### 2. Listener at Wrapper Location

The listener runs where the wrapper service is deployed and provides a stable local endpoint.

```yaml
# In cloud namespace
apiVersion: skupper.io/v2alpha1
kind: Listener
metadata:
  name: orders-db
spec:
  routingKey: orders-db
  host: orders-db.svc.cluster.local
  port: 5432
```

The wrapper connects to `orders-db.svc.cluster.local:5432` as if it were a local service.

#### 3. Traffic Flow

```
1. Wrapper initiates connection to local listener endpoint
2. Listener forwards to Skupper router
3. Router forwards through network to datacenter site
4. Router at datacenter site delivers to connector
5. Connector proxies connection to legacy system
6. Responses follow the same path in reverse
```

## Key Benefits

### No Inbound Firewall Rules

The datacenter only needs **outbound** connectivity. The Skupper link is established outbound, and application traffic flows back through that link. Datacenter firewall rules remain unchanged.

### No VPN Required

Unlike VPN solutions that create broad network access, Skupper creates scoped application-level connectivity. Only the specific legacy service is accessible, not the entire datacenter network.

### No Legacy System Changes

The legacy system continues to listen on its existing port and address. It does not need Skupper-specific configuration, libraries, or awareness.

### Wrapper Simplicity

The wrapper service uses a normal local connection (e.g., database connection string points to `orders-db.svc.cluster.local:5432`). No special client libraries or connection handling required.

### Security Boundary Preservation

Network segmentation remains intact. The legacy system is not exposed publicly or to untrusted networks. Skupper provides mutual TLS for traffic encryption.

## Example Scenarios

### Scenario 1: Strangler Fig Migration

**Situation**: Migrating from monolithic legacy system to microservices. Want to incrementally extract functionality.

**Approach**:
1. Create new microservice that wraps part of legacy functionality
2. Deploy microservice in Kubernetes
3. Use Skupper connector to let microservice access legacy system
4. Route some traffic to new microservice, fallback to legacy
5. Incrementally move more traffic to new service
6. Eventually decommission legacy system

**Skupper's role**: Allows new microservices to coexist with legacy system during multi-year migration without relocating legacy system or creating complex network changes.

### Scenario 2: API Gateway in Front of Legacy App

**Situation**: Legacy application uses custom protocol. Want to expose REST API without modifying legacy app.

**Approach**:
1. Deploy API gateway in cloud
2. Gateway translates REST to legacy protocol
3. Skupper listener at gateway location
4. Skupper connector at legacy app location
5. Gateway connects through listener to legacy app

**Skupper's role**: Connects cloud-based API gateway to datacenter legacy app without exposing legacy app or requiring inbound firewall rules.

### Scenario 3: Modernizing Database Access

**Situation**: Legacy application uses Oracle database in datacenter. New cloud-native applications need read access.

**Approach**:
1. Create read replica or reporting database wrapper
2. Deploy wrapper in cloud with caching, connection pooling
3. Wrapper connects to datacenter Oracle through Skupper
4. New applications connect to wrapper

**Skupper's role**: Allows wrapper to access datacenter database without database relocation or VPN configuration.

## Implementation Patterns

### Pattern A: Direct Wrapper

Wrapper directly accesses legacy system through Skupper.

```
New Service → Listener → Connector → Legacy System
```

Use when:
- Legacy system protocol is standard (HTTP, SQL, etc.)
- Wrapper handles all translation logic
- Direct access is acceptable

### Pattern B: Adapter Service

Dedicated adapter service sits between wrapper and legacy system.

```
New Service → Adapter → Listener → Connector → Legacy System
```

Use when:
- Complex protocol translation required
- Multiple new services need same legacy access
- Want to centralize legacy interaction logic

### Pattern C: Data Synchronization

Synchronize data from legacy to modern system, use Skupper for sync connection.

```
Modern DB ← Sync Service → Listener → Connector → Legacy DB
```

Use when:
- Read-mostly access pattern
- Can tolerate eventual consistency
- Want to reduce load on legacy system

## Security Considerations

### Authentication

Skupper handles network-level authentication (mutual TLS), but application-level authentication must still be implemented:

- Wrapper should authenticate to legacy system using existing credentials
- Legacy system access controls remain in effect
- Consider credential management (secrets, vaults) for wrapper

### Authorization

- Legacy system should validate that wrapper is authorized to access requested data/functions
- Implement principle of least privilege for wrapper's legacy system access
- Audit wrapper access to legacy system

### Network Isolation

- Skupper connector only exposes the specific port of the legacy system
- Legacy system remains on private network
- No broad network access created

### Encryption

- Skupper encrypts traffic between sites using mutual TLS
- Application-level encryption (e.g., database TLS) can be layered on top if required

## Migration Path

A typical modernization journey using this pattern:

```
Phase 1: Assessment
├─ Identify legacy system dependencies
├─ Design wrapper architecture
└─ Plan incremental migration

Phase 2: Initial Wrapper (← Skupper introduced here)
├─ Deploy wrapper service
├─ Establish Skupper connectivity to legacy
├─ Implement basic translation logic
└─ Test with limited traffic

Phase 3: Incremental Traffic Shift
├─ Route increasing traffic to wrapper
├─ Monitor wrapper performance
├─ Iterate on wrapper functionality
└─ Reduce legacy system direct access

Phase 4: Legacy Decomposition
├─ Migrate legacy data to modern systems
├─ Decompose legacy functionality
└─ Eventually decommission legacy system

Phase 5: Full Modernization (← Skupper may no longer be needed)
├─ All functionality in modern services
└─ Legacy system retired
```

Skupper is part of the **transitional architecture**. Once legacy systems are fully retired, the Skupper connectivity for those systems is no longer needed (though Skupper may still be used for other patterns).

## Anti-Patterns to Avoid

### ❌ Over-Reliance on Legacy

Using Skupper as an excuse to defer real modernization. The wrapper should progressively take on more functionality, not indefinitely proxy to legacy.

### ❌ Bypassing Security Review

Connecting new services to legacy systems is a significant change. Involve security teams in reviewing the connection pattern.

### ❌ Tight Coupling

Wrapper should not expose legacy system's internal data model directly. Abstract and translate to modern representations.

### ❌ Shared State Without Coordination

If both wrapper and legacy system modify the same data, implement proper coordination (transactions, locking, etc.).

## Relationship to Other Patterns

- [Service Virtualization](service-virtualization.md): The wrapper itself may be virtualized and relocated
- [Hybrid-cloud Elasticity](hybrid-cloud-elasticity.md): Wrapper may scale in cloud while legacy remains on-premises
- [Boundaryless Information Flow](boundaryless-information-flow.md): Enables information flow from legacy to modern systems across boundaries

## Implementation Checklist

- [ ] Document legacy system access requirements (protocol, ports, auth)
- [ ] Design wrapper service interface and translation logic
- [ ] Deploy wrapper service in target environment
- [ ] Install Skupper at both wrapper and legacy locations
- [ ] Create connector at legacy location pointing to legacy system
- [ ] Create listener at wrapper location with stable endpoint
- [ ] Configure wrapper to connect through listener
- [ ] Test wrapper → legacy connectivity
- [ ] Implement application-level authentication and authorization
- [ ] Conduct security review of wrapper access pattern
- [ ] Monitor wrapper performance and legacy system impact
- [ ] Plan incremental traffic migration
- [ ] Document eventual legacy retirement plan

## References

- [The Open Group - Using TOGAF for SOA](https://www.opengroup.org/soa/source-book/togaf/p4.htm)
- [Skupper Private Service Access](togaf-overview.md#private-service-access)
- [Skupper Listener Concept](../concepts/listener.md)
- [Skupper Connector Concept](../concepts/connector.md)
