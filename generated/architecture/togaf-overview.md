# TOGAF Architecture Patterns with Skupper

## Overview

This document describes how Skupper functions as a **Solution Building Block (SBB)** within TOGAF architecture patterns. The key framing principle is:

> **Skupper is usually the connectivity part of the solution, not the complete architectural pattern.**

TOGAF describes patterns as combinations of building blocks. The implementation-specific building blocks that realize these patterns emerge as Solution Building Blocks. Skupper provides the location-transparent connectivity fabric that enables several important architecture patterns.

## Skupper's Role in TOGAF

### Architecture Building Block to Solution Building Block

The TOGAF methodology distinguishes between:

- **Architecture Building Blocks (ABBs)**: Technology-agnostic descriptions of capability required
- **Solution Building Blocks (SBBs)**: Specific implementations that realize those capabilities

Skupper functions as an SBB that realizes location-transparent service connectivity requirements across multiple TOGAF patterns.

```
Business Requirement
         ↓
Architecture Outcome: Location-independent services
         ↓
Architecture Building Block: Location-transparent connectivity
         ↓
Solution Building Block: Skupper application network
         ↓
    Implementation:
    - Listeners
    - Connectors
    - Routing Keys
    - Site Links
```

## Architecture Outcomes

### Location-independent services {#location-independent-services}

Services can be deployed, relocated, or scaled without affecting consumers or changing application addressing. The service's logical identity remains stable regardless of where it physically runs.

**Skupper's contribution**: Routing keys provide logical service identity; listeners and connectors abstract endpoint location.

### Boundaryless applications {#boundaryless-applications}

Application components communicate across organizational, infrastructure, and platform boundaries without those boundaries becoming application boundaries.

**Skupper's contribution**: Secure application network that carries application connections independently of underlying infrastructure topology.

### Deployment freedom {#deployment-freedom}

Services can be independently placed in the most appropriate location (cloud, datacenter, edge) without constraint from application connectivity requirements.

**Skupper's contribution**: Platform-independent connectivity allows workloads to communicate regardless of where they are deployed.

### Incremental modernization {#incremental-modernization}

Legacy systems can be wrapped with new services and incrementally replaced without requiring immediate relocation or public exposure of legacy workloads.

**Skupper's contribution**: Connects new wrappers to legacy systems privately, without flattening networks or opening inbound firewall ports.

### Cross-location resilience {#cross-location-resilience}

Services can run in parallel across multiple locations with automatic failover and load distribution to survive location failures.

**Skupper's contribution**: Multi-location routing with connection distribution and failover across service instances.

### Application topology decoupled from infrastructure topology {#infrastructure-decoupling}

Application design does not need to mirror or conform to infrastructure boundaries, network topology, or platform constraints.

**Skupper's contribution**: Application network layer that abstracts infrastructure topology from application topology.

## Required Connectivity Capabilities

These capabilities are required to realize the architecture patterns. Skupper provides these as part of the solution.

### Logical service identity {#logical-service-identity}

Services are addressed by stable logical names rather than location-specific network addresses.

**Implemented by**: Routing keys

### Endpoint abstraction {#endpoint-abstraction}

Service endpoints are abstracted from physical network locations, allowing endpoints to change without affecting consumers.

**Implemented by**: Listeners, connectors, and routing keys working together

### Application service connectivity {#service-connectivity}

Distributed application components can establish connections regardless of platform or location.

**Implemented by**: Listeners and connectors

### Location-transparent routing {#location-transparent-routing}

Connections are routed to appropriate service instances without consumers needing to know the location.

**Implemented by**: Routing keys and Skupper router

### Cross-boundary routing {#cross-boundary-routing}

Connections traverse organizational, network, and platform boundaries securely.

**Implemented by**: Site links and Skupper router

### Secure transport between locations {#secure-transport}

All inter-location traffic is encrypted and authenticated without requiring application-level security implementation.

**Implemented by**: Site links and Skupper router provide mutual TLS

### Platform-independent connectivity {#platform-independent-connectivity}

Services can communicate regardless of whether they run on Kubernetes, VMs, containers, or other platforms.

**Implemented by**: Listeners and connectors support multiple platforms

### Private service access without public exposure {#private-service-access}

Services can be accessed across locations without exposing them through public IPs or inbound firewall rules.

**Implemented by**: Listeners, connectors, and site links establish outbound-only connections

### One logical service across locations {#multi-location-service}

Multiple instances of a service in different locations appear as a single logical service.

**Implemented by**: Shared routing key across multiple connectors

### Connection distribution {#connection-distribution}

New connections are distributed across available service instances for load balancing.

**Implemented by**: Skupper router distributes connections across connectors

### Service instance failover {#service-failover}

Connections automatically fail over to available instances when a service instance becomes unavailable.

**Implemented by**: Skupper router detects connector availability and redirects traffic

### Location preference {#location-preference}

Traffic can be preferentially routed to instances in specific locations with spillover to others.

**Implemented by**: Routing cost on site links influences routing decisions

## Skupper Solution Building Blocks

These are the specific Skupper components that implement the required capabilities.

### Skupper Router {#skupper-router}

The application-layer message router that provides location-transparent routing across the network.

### Site Link {#site-link}

Encrypted, authenticated connection between Skupper routers in different sites, forming the application network backbone.

### Multi-provider routing {#multi-provider-routing}

Multiple connectors share the same routing key, allowing the router to distribute connections across providers and fail over when needed.

### Routing Cost {#routing-cost}

Numeric value assigned to site links that influences routing decisions, allowing implementation of location preference policies.

## Solution Environment

### Service consumer {#service-consumer}

Application component that initiates connections to services. Connects through listeners to access remote services.

### Service provider {#service-provider}

Application workload that serves requests. Exposed to the network through connectors.

### Cloud environment {#cloud-environment}

Public or private cloud platform (AWS, Azure, GCP, etc.) hosting application workloads.

### Datacenter environment {#datacenter-environment}

On-premises datacenter or colocation facility hosting application workloads.

### Edge / branch environment {#edge-environment}

Edge computing location or branch office hosting application workloads.

### Network reachability {#network-reachability}

Underlying IP network connectivity between sites. Skupper requires at least one outbound path between sites but does not require mutual reachability or public IPs.

## Integration with Other Architecture Components

Skupper handles connectivity but is typically combined with other components in a complete architecture:

| Component Type | Skupper's Role | Not Skupper |
|----------------|----------------|-------------|
| **Integration Layer** | Service communication, routing, secure transport | Message transformation, process orchestration, API management |
| **Service Mesh** | Cross-location connectivity | Within-cluster traffic management, policy enforcement |
| **API Gateway** | Connect gateway to backend services | API versioning, rate limiting, authentication |
| **Message Broker** | Connect applications to broker | Message queuing, pub/sub, message transformation |

## References

- [The Open Group Architecture Forum](https://www.opengroup.org/architecture)
- [TOGAF SOA Reference Architecture](https://www.opengroup.org/soa/source-book/soa_refarch)
- [TOGAF for SOA](https://www.opengroup.org/soa/source-book/togaf)
- [Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp)
