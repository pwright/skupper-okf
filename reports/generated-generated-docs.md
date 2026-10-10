# Generated documentation report

Documents: **631**  
Headings: **4231**  
Links: **4757**  
Code blocks: **566**

Each document entry lists headings, links, and code block languages extracted by `mq`.

## `generated/archify.md`

Headings (9):
- # Archify diagrams
- ## Prerequisites
- ## Editing an existing diagram
- ## Creating a new diagram from scratch
- ## Diagram types
- ## Key JSON fields
- ### Component types
- ### Connection label placement
- ## Diagrams in this directory

Links (9):
- [Archify](https://github.com/skupperproject/skupper-okf)
- [](skupper-combined.architecture.json)
- [](skupper-combined.html)
- [](skupper-datapath.architecture.json)
- [](skupper-datapath.html)
- [](skupper-deployment.architecture.json)
- [](skupper-deployment.html)
- [](skupper-network-observer.architecture.json)
- [](skupper-network-observer.html)

Code blocks (7):
- `bash`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `bash`
- `jsonc`

## `generated/architecture/boundaryless-information-flow.md`

Headings (53):
- # Boundaryless Information Flow Pattern
- ## Pattern Overview
- ## TOGAF Context
- ### Architecture Building Block
- ### Solution Building Block
- ## Problem Statement
- ### Infrastructure Boundaries
- ### Network Boundaries
- ### Platform Boundaries
- ### Organizational Boundaries
- ### Traditional Solutions Create Coupling
- ## Solution with Skupper
- ### Architecture Diagram
- ### Key Principles
- #### 1. Application Topology ≠ Infrastructure Topology
- #### 2. Outbound-Only Boundary Crossing
- #### 3. Platform-Independent Connectivity
- #### 4. Location-Independent Addressing
- ## Example Scenarios
- ### Scenario 1: Multi-Cloud Application
- ### Scenario 2: Hybrid Cloud Application
- ### Scenario 3: Edge-to-Core Application
- ### Scenario 4: Partner Organization Integration
- ### Scenario 5: Acquired Company Integration
- ## Implementation Patterns
- ### Pattern A: Hub-and-Spoke
- ### Pattern B: Mesh
- ### Pattern C: Tiered
- ### Pattern D: Selective Bridging
- ## Boundary Types and Skupper Solutions
- ## Security Across Boundaries
- ### Encryption
- ### Authorization
- ### Scoped Access
- ### Audit and Monitoring
- ## Operational Considerations
- ### Link Management
- ### Service Discovery
- ### Namespace and Naming
- ### Change Management
- ## When Skupper Complements Other Technologies
- ### Service Mesh
- ### API Gateway
- ### Message Queue
- ## Anti-Patterns to Avoid
- ### ❌ Using Skupper as a Persistent Message Broker
- ### ❌ Exposing Everything
- ### ❌ Ignoring Network Latency
- ### ❌ Bypassing Security Review
- ## Implementation Checklist
- ## Relationship to Other Patterns
- ## Value Proposition
- ## References

Links (8):
- [TOGAF Integrated Information Infrastructure Reference Model](https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm)
- [Service Virtualization](service-virtualization.md)
- [Integration Layer](integration-layer.md)
- [Hybrid-cloud Elasticity](hybrid-cloud-elasticity.md)
- [Legacy Modernization](legacy-modernization.md)
- [TOGAF Integrated Information Infrastructure Reference Model](https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm)
- [Skupper Concepts](https://skupper.io/docs/refdog/concepts/)
- [Cross-boundary Routing Capability](togaf-overview.md#cross-boundary-routing)

Code blocks (16):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/architecture/hybrid-cloud-elasticity.md`

Headings (49):
- # Hybrid-Cloud Elasticity Pattern
- ## Pattern Overview
- ## TOGAF Context
- ### Architecture Building Block
- ### Solution Building Block
- ## Problem Statement
- ## Solution with Skupper
- ### Architecture Diagram
- ## Key Components
- ### 1. Shared Routing Key
- ### 2. Multiple Connectors
- ### 3. Location Preference via Routing Cost
- ### 4. Single Listener
- ## Traffic Distribution Behavior
- ### Normal Operation (Datacenter Available)
- ### Datacenter at Capacity
- ### Datacenter Unavailable
- ### Gradual Recovery
- ## Use Cases
- ### Use Case 1: Cost Optimization with Burst Capacity
- ### Use Case 2: Gradual Cloud Migration
- ### Use Case 3: Multi-Cloud Resilience
- ### Use Case 4: Compliance and Performance Balance
- ## Configuration Patterns
- ### Pattern A: Equal Distribution
- ### Pattern B: Strong Preference
- ### Pattern C: Gradual Spillover
- ### Pattern D: Multi-Region Active-Active
- ## Operational Considerations
- ### Monitoring
- ### Capacity Planning
- ### Cost Management
- ### Scaling Automation
- ## Performance Characteristics
- ### Latency
- ### Throughput
- ### Connection Distribution Timing
- ## Security Considerations
- ### Data Residency
- ### Access Controls
- ### Encryption
- ## Integration with Auto-Scaling
- ## Troubleshooting
- ### Issue: Cloud not receiving overflow traffic
- ### Issue: Uneven distribution despite equal costs
- ### Issue: Slow failover during datacenter outage
- ## Implementation Checklist
- ## Related Patterns
- ## References

Links (7):
- [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)
- [Service Virtualization](service-virtualization.md)
- [Resilient Service Instances](resilient-service-instances.md)
- [Independent Microservice Placement](independent-service-placement.md)
- [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)
- [Skupper Routing](https://skupper.io/docs/overview/routing.html)
- [Skupper Load Balancing](https://skupper.io/docs/overview/load-balancing.html)

Code blocks (16):
- `unspecified`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/architecture/independent-service-placement.md`

Headings (51):
- # Independent Microservice Placement Pattern
- ## Pattern Overview
- ## TOGAF Context
- ### Architecture Building Block
- ### Solution Building Block
- ## Problem Statement
- ### Placement Constraints
- ### Traditional Connectivity Creates Coupling
- ## Solution with Skupper
- ### Architecture Diagram
- ## Key Principles
- ### 1. Logical Service Identity
- ### 2. Platform Independence
- ### 3. Independent Scaling
- ### 4. Independent Deployment
- ## Placement Decision Framework
- ### Factors to Consider
- #### Cost
- #### Latency
- #### Compliance
- #### Resource Requirements
- #### Integration Requirements
- #### Operational Concerns
- ### Example Placement Matrix
- ## Implementation Patterns
- ### Pattern A: Cloud Frontend, Datacenter Backend
- ### Pattern B: Multi-Cloud Service Distribution
- ### Pattern C: Specialized Resource Placement
- ### Pattern D: Gradual Cloud Migration
- ## Example Scenarios
- ### Scenario 1: E-Commerce Application
- ### Scenario 2: SaaS Application with Regional Data
- ### Scenario 3: Microservices with Mixed Maturity
- ## Operational Considerations
- ### Service Discovery
- ### Deployment Coordination
- ### Monitoring and Observability
- ### Cost Tracking
- ## Benefits
- ### Optimal Cost
- ### Regulatory Compliance
- ### Performance Optimization
- ### Technology Flexibility
- ### Risk Reduction
- ## Limitations and Considerations
- ### Network Latency
- ### Data Gravity
- ### Complexity
- ## Implementation Checklist
- ## Relationship to Other Patterns
- ## References

Links (7):
- [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)
- [Service Virtualization](service-virtualization.md)
- [Hybrid-cloud Elasticity](hybrid-cloud-elasticity.md)
- [Boundaryless Information Flow](boundaryless-information-flow.md)
- [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)
- [Skupper Concepts](https://skupper.io/docs/refdog/concepts/)
- [Platform-Independent Connectivity](togaf-overview.md#platform-independent-connectivity)

Code blocks (14):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/architecture/index.md`

Headings (3):
- # Architecture
- ## Diagrams
- ## Patterns

Links (10):
- [Skupper Combined Architecture](https://pwright.github.io/skupper-okf/generated/architecture/skupper-combined.html)
- [Skupper Network Observer Architecture](https://pwright.github.io/skupper-okf/generated/architecture/skupper-network-observer.html)
- [Boundaryless Information Flow](boundaryless-information-flow.md)
- [Hybrid Cloud Elasticity](hybrid-cloud-elasticity.md)
- [Independent Service Placement](independent-service-placement.md)
- [Integration Layer](integration-layer.md)
- [Legacy Modernization](legacy-modernization.md)
- [Resilient Service Instances](resilient-service-instances.md)
- [Service Virtualization](service-virtualization.md)
- [TOGAF Overview](togaf-overview.md)

Code blocks (0):
- None

## `generated/architecture/integration-layer.md`

Headings (45):
- # Integration Layer Pattern
- ## Pattern Overview
- ## TOGAF Context
- ### Architecture Building Block
- ### Solution Building Block
- ## Integration Layer Capabilities
- ## Skupper's Role in the Integration Layer
- ### What Skupper Provides
- #### 1. Service Communication
- #### 2. Service Endpoint Abstraction
- #### 3. Routing and Load Distribution
- #### 4. Secure Transport
- ### What Skupper Does Not Provide
- #### Message Transformation
- #### Service Composition
- #### Process Orchestration
- #### API Management
- ## Integration Patterns with Skupper
- ### Pattern 1: Skupper Connects ESB Components
- ### Pattern 2: Skupper Connects API Gateway to Backends
- ### Pattern 3: Skupper Connects to Message Broker
- ### Pattern 4: Skupper Enables Distributed Microservices
- ## Architecture Layers
- ## Integration Scenarios
- ### Scenario 1: Hybrid Integration Platform
- ### Scenario 2: Multi-Cloud Message Backbone
- ### Scenario 3: Service Mesh Federation
- ## Capabilities Mapping
- ## When to Use Skupper in Integration Architecture
- ### Good Fit
- ### Not the Right Tool
- ### Complement to Integration Middleware
- ## Design Considerations
- ### Network Topology
- ### Service Exposure
- ### Security Zones
- ### Performance
- ## Implementation Checklist
- ## Anti-Patterns to Avoid
- ### ❌ Using Skupper as an ESB
- ### ❌ Exposing Too Much
- ### ❌ Ignoring Integration Middleware
- ### ❌ Point-to-Point Integration Sprawl
- ## Relationship to Other Patterns
- ## References

Links (7):
- [The Open Group SOA Reference Architecture - Using TOGAF for SOA](https://www.opengroup.org/soa/source-book/togaf/p4.htm)
- [Service Virtualization](service-virtualization.md)
- [Boundaryless Information Flow](boundaryless-information-flow.md)
- [Legacy Modernization](legacy-modernization.md)
- [The Open Group SOA Reference Architecture](https://www.opengroup.org/soa/source-book/soa_refarch)
- [Using TOGAF for SOA](https://www.opengroup.org/soa/source-book/togaf/p4.htm)
- [Skupper Concepts](https://skupper.io/docs/refdog/concepts/)

Code blocks (15):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/architecture/legacy-modernization.md`

Headings (41):
- # Legacy Modernization / Wrapper Pattern
- ## Pattern Overview
- ## TOGAF Context
- ### Architecture Building Block
- ### Solution Building Block
- ## Problem Statement
- ### Traditional Solutions and Their Drawbacks
- ## Solution with Skupper
- ### Architecture Diagram
- ### Key Components
- #### 1. Connector at Legacy Location
- #### 2. Listener at Wrapper Location
- #### 3. Traffic Flow
- ## Key Benefits
- ### No Inbound Firewall Rules
- ### No VPN Required
- ### No Legacy System Changes
- ### Wrapper Simplicity
- ### Security Boundary Preservation
- ## Example Scenarios
- ### Scenario 1: Strangler Fig Migration
- ### Scenario 2: API Gateway in Front of Legacy App
- ### Scenario 3: Modernizing Database Access
- ## Implementation Patterns
- ### Pattern A: Direct Wrapper
- ### Pattern B: Adapter Service
- ### Pattern C: Data Synchronization
- ## Security Considerations
- ### Authentication
- ### Authorization
- ### Network Isolation
- ### Encryption
- ## Migration Path
- ## Anti-Patterns to Avoid
- ### ❌ Over-Reliance on Legacy
- ### ❌ Bypassing Security Review
- ### ❌ Tight Coupling
- ### ❌ Shared State Without Coordination
- ## Relationship to Other Patterns
- ## Implementation Checklist
- ## References

Links (8):
- [The Open Group - Using TOGAF for SOA](https://www.opengroup.org/soa/source-book/togaf/p4.htm)
- [Service Virtualization](service-virtualization.md)
- [Hybrid-cloud Elasticity](hybrid-cloud-elasticity.md)
- [Boundaryless Information Flow](boundaryless-information-flow.md)
- [The Open Group - Using TOGAF for SOA](https://www.opengroup.org/soa/source-book/togaf/p4.htm)
- [Skupper Private Service Access](togaf-overview.md#private-service-access)
- [Skupper Listener Concept](../concepts/listener.md)
- [Skupper Connector Concept](../concepts/connector.md)

Code blocks (8):
- `unspecified`
- `yaml`
- `yaml`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/architecture/resilient-service-instances.md`

Headings (51):
- # Resilient Parallel Service Instances Pattern
- ## Pattern Overview
- ## TOGAF Context
- ### Architecture Building Block
- ### Solution Building Block
- ## Problem Statement
- ### Failure Domains
- ### Traditional Resilience Solutions
- ## Solution with Skupper
- ### Architecture Diagram
- ## Resilience Patterns
- ### Pattern A: Active-Active Multi-Location
- ### Pattern B: Active-Standby Multi-Location
- ### Pattern C: Active-Active Within Location, Active-Standby Across Locations
- ### Pattern D: Multi-Region Active-Active with Affinity
- ## Failover Behavior
- ### Detection
- ### Failover Timing
- ### Recovery
- ## Implementation Example
- ### Setup
- ### Normal Operation
- ### Azure Failure
- ### Azure Recovery
- ## Testing Resilience
- ### Chaos Engineering Practices
- #### Test 1: Single Instance Failure
- #### Test 2: Connector Failure
- #### Test 3: Location Failure
- #### Test 4: Network Partition
- ### Metrics to Monitor
- ## Capacity Planning
- ### N+1 Capacity Model
- ### N+2 for Critical Services
- ## Operational Considerations
- ### Monitoring
- ### Alerting
- ### Runbooks
- ### Cost Optimization
- ## Security Considerations
- ### Data Consistency
- ### Session Management
- ### Data Synchronization
- ## Anti-Patterns
- ### ❌ Testing Failover Only in Production
- ### ❌ Insufficient Capacity
- ### ❌ Shared Failure Domains
- ### ❌ Neglecting Data Consistency
- ## Implementation Checklist
- ## Relationship to Other Patterns
- ## References

Links (7):
- [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)
- [Hybrid-cloud Elasticity](hybrid-cloud-elasticity.md)
- [Service Virtualization](service-virtualization.md)
- [Independent Service Placement](independent-service-placement.md)
- [The Open Group - Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp/p2.htm)
- [Skupper Load Balancing](https://skupper.io/docs/overview/load-balancing.html)
- [Service Failover Capability](togaf-overview.md#service-failover)

Code blocks (17):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `yaml`
- `unspecified`
- `unspecified`
- `unspecified`
- `bash`
- `bash`
- `bash`
- `bash`
- `unspecified`
- `unspecified`

## `generated/architecture/service-virtualization.md`

Headings (26):
- # Service Virtualization / Location Transparency
- ## Pattern Overview
- ## TOGAF Context
- ### Architecture Building Block
- ### Solution Building Block
- ## Problem Statement
- ## Solution with Skupper
- ### 1. Routing Key (Logical Service Identity)
- ### 2. Listener (Consumer-side Abstraction)
- ### 3. Connector (Provider-side Abstraction)
- ## Architecture Diagram
- ## Key Benefits
- ### Location Independence
- ### Transparent Failover
- ### Zero Application Changes
- ### Platform Independence
- ## Comparison to Alternative Approaches
- ## When to Use This Pattern
- ## When Skupper Complements Other Solutions
- ## Example Scenarios
- ### Scenario 1: Hybrid Cloud Deployment
- ### Scenario 2: Incremental Migration
- ### Scenario 3: Development/Production Parity
- ## Implementation Checklist
- ## Related Patterns
- ## References

Links (8):
- [The Open Group SOA Reference Architecture - Service Virtualization](https://www.opengroup.org/soa/source-book/soa_refarch/p13.htm)
- [Integration Layer](integration-layer.md)
- [Independent Microservice Placement](independent-service-placement.md)
- [Boundaryless Information Flow](boundaryless-information-flow.md)
- [The Open Group SOA Reference Architecture](https://www.opengroup.org/soa/source-book/soa_refarch/p13.htm)
- [Skupper Listener Concept](../concepts/listener.md)
- [Skupper Connector Concept](../concepts/connector.md)
- [Skupper Routing Key Concept](../concepts/routing-key.md)

Code blocks (4):
- `yaml`
- `yaml`
- `yaml`
- `unspecified`

## `generated/architecture/togaf-overview.md`

Headings (38):
- # TOGAF Architecture Patterns with Skupper
- ## Overview
- ## Skupper's Role in TOGAF
- ### Architecture Building Block to Solution Building Block
- ## Architecture Outcomes
- ### Location-independent services {#location-independent-services}
- ### Boundaryless applications {#boundaryless-applications}
- ### Deployment freedom {#deployment-freedom}
- ### Incremental modernization {#incremental-modernization}
- ### Cross-location resilience {#cross-location-resilience}
- ### Application topology decoupled from infrastructure topology {#infrastructure-decoupling}
- ## Required Connectivity Capabilities
- ### Logical service identity {#logical-service-identity}
- ### Endpoint abstraction {#endpoint-abstraction}
- ### Application service connectivity {#service-connectivity}
- ### Location-transparent routing {#location-transparent-routing}
- ### Cross-boundary routing {#cross-boundary-routing}
- ### Secure transport between locations {#secure-transport}
- ### Platform-independent connectivity {#platform-independent-connectivity}
- ### Private service access without public exposure {#private-service-access}
- ### One logical service across locations {#multi-location-service}
- ### Connection distribution {#connection-distribution}
- ### Service instance failover {#service-failover}
- ### Location preference {#location-preference}
- ## Skupper Solution Building Blocks
- ### Skupper Router {#skupper-router}
- ### Site Link {#site-link}
- ### Multi-provider routing {#multi-provider-routing}
- ### Routing Cost {#routing-cost}
- ## Solution Environment
- ### Service consumer {#service-consumer}
- ### Service provider {#service-provider}
- ### Cloud environment {#cloud-environment}
- ### Datacenter environment {#datacenter-environment}
- ### Edge / branch environment {#edge-environment}
- ### Network reachability {#network-reachability}
- ## Integration with Other Architecture Components
- ## References

Links (4):
- [The Open Group Architecture Forum](https://www.opengroup.org/architecture)
- [TOGAF SOA Reference Architecture](https://www.opengroup.org/soa/source-book/soa_refarch)
- [TOGAF for SOA](https://www.opengroup.org/soa/source-book/togaf)
- [Microservices Architecture White Paper](https://www.opengroup.org/soa/source-book/msawp)

Code blocks (1):
- `unspecified`

## `generated/concepts/access-grants-and-tokens.md`

Headings (11):
- # Access Grants and Tokens
- ## Prerequisites
- ## The two-sided ceremony
- ## Grant server ()
- ### reconciliation
- ### HTTP redemption endpoint
- ## Token generation ()
- ## Token redemption ()
- ## Security properties
- ## AccessGrant vs AccessToken
- ## References

Links (7):
- [Default Site](./default-site.md)
- [](../human/skupper/internal/kube/grants/grants.go)
- [](../human/skupper/internal/kube/grants/redeem.go)
- [](../human/skupper/internal/kube/grants/tokens.go)
- [Inter-Site Link concept](./inter-site-link.md)
- [Site Controller concept](./site-controller.md)
- [Default Site concept](./default-site.md)

Code blocks (8):
- `unspecified`
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`

## `generated/concepts/certificate-manager.md`

Headings (11):
- # Certificate Manager
- ## Role in the system
- ## interface
- ## Internal reconcile flow
- ### 
- ### Detecting stale secrets
- ## Multi-owner host merging
- ## Recovery at startup
- ## Certificates created for a default site
- ## Integration with kube-adaptor
- ## References

Links (7):
- [cert-manager.io](https://cert-manager.io/)
- [Kube Adaptor](./kube-adaptor.md)
- [](../human/skupper/internal/kube/certificates/mgr.go)
- [](../human/skupper/internal/kube/certificates/ownermappings.go)
- [Site Controller concept](./site-controller.md)
- [Kube Adaptor concept](./kube-adaptor.md)
- [SecuredAccess concept](./secured-access.md)

Code blocks (7):
- `unspecified`
- `go`
- `unspecified`
- `go`
- `go`
- `unspecified`
- `go`

## `generated/concepts/client-listener-router-connector-reconnects.md`

Headings (7):
- # Client to Listener to Router to Connector Reconnects
- ## Path
- ## Reconnect Boundaries
- ## What Skupper Recovers
- ## What Skupper Does Not Recover
- ## Recovery Model
- ## Operator View

Links (1):
- [Enterprise TCP Sessions and Recovery](../maps/enterprise-session-recovery.md)

Code blocks (1):
- `text`

## `generated/concepts/connector.md`

Headings (9):
- # Connector
- ## Outcome
- ## Key ideas
- ## Common fields
- ## Creation paths
- ## Connector variants
- ## Verify
- ## Observability
- ## Caveats

Links (12):
- [routing key](./routing-key.md)
- [routing key](./routing-key.md)
- [routing key](./routing-key.md)
- [Creating a connector using YAML (Kubernetes)](../input/kube-yaml/service-exposure.md#kube-creating-connector-yaml)
- [Creating a connector using YAML (local systems)](../input/system-yaml/service-exposure.md)
- [Creating a connector using CLI (local systems)](../input/system-cli/service-exposure.md)
- [Skupper Ansible resource module](../skupper-ansible/skupper-ansible-module-resource.md)
- [Creating a connector for a different namespace using YAML](../input/kube-yaml/service-exposure.md#kube-creating-attachedconnector-yaml)
- [Network Observer API](./network-observer-api.md)
- [Network Observer API Reference](../sources/skupper-openapi-spec-api-reference.md#getapiv2alpha1connectors)
- [routing key](./routing-key.md)
- [routing key](./routing-key.md)

Code blocks (12):
- `text`
- `yaml`
- `bash`
- `yaml`
- `yaml`
- `bash`
- `bash`
- `text`
- `bash`
- `text`
- `bash`
- `text`

## `generated/concepts/default-site.md`

Headings (8):
- # Default Site (No Link Access, No HA)
- ## What "no link access" means at the resource level
- ## The two router ports never open by default
- ## What the default site can and cannot do
- ## Enabling link access
- ## No HA by default
- ## Minimum viable two-site network
- ## References

Links (3):
- [CRD](../human/skupper/config/crd/bases/skupper_routeraccess_crd.yaml)
- [CRD](../human/skupper/config/crd/bases/skupper_site_crd.yaml)
- [Inter-Site Link concept](./inter-site-link.md)

Code blocks (9):
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`
- `sh`
- `yaml`
- `unspecified`

## `generated/concepts/inter-site-link.md`

Headings (11):
- # Inter-Site Link
- ## Relationship to routing keys
- ## Link model
- ## Resources involved
- ## Linking with a token (CLI)
- ## Linking with YAML (Kubernetes)
- ## Link resource structure
- ## Link cost
- ## Status conditions
- ## References
- ## Inter-site link — consolidated summary

Links (10):
- [routing key](./routing-key.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Site linking with CLI (Kubernetes)](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Site linking with YAML (Kubernetes)](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [Link CRD](../skupper/skupper-crd-links-skupper-io.md)
- [AccessToken CRD](../skupper/skupper-crd-accesstokens-skupper-io.md)
- [AccessGrant CRD](../skupper/skupper-crd-accessgrants-skupper-io.md)
- [1](#4-0)
- [2](#4-1)
- [3](#4-2)

Code blocks (22):
- `text`
- `bash`
- `bash`
- `yaml`
- `bash`
- `bash`
- `yaml`
- `yaml`
- `bash`
- `unspecified`
- `unspecified`
- `go`
- `yaml`
- `yaml`
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`

## `generated/concepts/kube-adaptor.md`

Headings (14):
- # Kube Adaptor
- ## Why it exists
- ## Deployment position
- ## Init phase:
- ## Run phase:
- ### How the AMQP management sync works
- ### Secret rotation
- ## Collector: flow data and site status
- ### 
- ### 
- ## Startup sequence
- ## Environment variables
- ## Relationship to the site controller
- ## References

Links (8):
- [](../human/skupper/internal/kube/adaptor/config_init.go)
- [](../human/skupper/internal/kube/adaptor/config_sync.go)
- [](../human/skupper/cmd/kube-adaptor/main.go)
- [](../human/skupper/internal/kube/adaptor/config_sync.go)
- [](../human/skupper/internal/kube/adaptor/config_init.go)
- [](../human/skupper/internal/kube/adaptor/collector.go)
- [](../human/skupper/internal/qdr/sync_router_ops.go)
- [](../human/skupper/internal/kube/site/resources/skupper-router-deployment.yaml)

Code blocks (9):
- `unspecified`
- `yaml`
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`
- `unspecified`

## `generated/concepts/listener.md`

Headings (9):
- # Listener
- ## Outcome
- ## Key ideas
- ## Common fields
- ## Creation paths
- ## Verify
- ## Listener-side routing policy
- ## Observability
- ## Caveats

Links (11):
- [routing key](./routing-key.md)
- [routing key](./routing-key.md)
- [Creating a listener using YAML (Kubernetes)](../input/kube-yaml/service-exposure.md#kube-creating-listener-yaml)
- [Creating a listener-side routing policy using YAML](../input/kube-yaml/service-exposure.md#kube-creating-multikeylistener-yaml)
- [Creating a listener using YAML (local systems)](../input/system-yaml/service-exposure.md)
- [Creating a listener using CLI (local systems)](../input/system-cli/service-exposure.md)
- [Skupper Ansible resource module](../skupper-ansible/skupper-ansible-module-resource.md)
- [Network Observer API](./network-observer-api.md)
- [Network Observer API Reference](../sources/skupper-openapi-spec-api-reference.md#getapiv2alpha1listeners)
- [routing key](./routing-key.md)
- [routing key](./routing-key.md)

Code blocks (8):
- `text`
- `yaml`
- `bash`
- `yaml`
- `yaml`
- `bash`
- `bash`
- `text`

## `generated/concepts/network-deployment-concerns.md`

Headings (19):
- # Network Deployment Concerns
- ## Appears in
- ## Outcome
- ## Sites
- ### Site Performance and Resource Allocation
- ### High Availability Sites
- ## Links
- ### Link Access
- ### Linking Methods
- #### Access Token Characteristics
- ### Link Constraints
- ### Custom Certificates for Links
- ## Services
- ### Observing Services
- ### Traffic Direction
- #### Listener-side Routing Policy (Recommended)
- #### Link Cost
- ## Verify
- ## References

Links (34):
- [connectors](./connector.md)
- [listeners](./listener.md)
- [routing keys](./routing-key.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [site](../human/skupper-docs/input/refdog/concepts/site.md)
- [Pod Quality of Service Classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)
- [Setting site resources](../human/skupper-docs/input/kube-yaml/site-configuration.md#kube-site-resources-yaml)
- [Creating a high availability site using YAML](../human/skupper-docs/input/kube-yaml/site-configuration.md#kube-ha-yaml)
- [Links](../human/skupper-docs/input/refdog/concepts/link.md)
- [Site resource](../human/skupper-docs/input/refdog/resources/site.md)
- [access tokens](../human/skupper-docs/input/refdog/concepts/access-token.md)
- [Site linking using tokens](../human/skupper-docs/input/kube-cli/site-linking.md#kube-token-cli)
- [Propagating custom labels and annotations using YAML](../human/skupper-docs/input/kube-yaml/custom-labels.md)
- [connector](./connector.md)
- [listener](./listener.md)
- [routing key](./routing-key.md)
- [API endpoint](./network-observer-api.md)
- [Using the Skupper network console](../human/skupper-docs/input/console/index.md)
- [Service exposure](../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [Load balancing and failover](../human/skupper-docs/input/overview/load-balancing.md)
- [Site concept](../human/skupper-docs/input/refdog/concepts/site.md)
- [Link concept](../human/skupper-docs/input/refdog/concepts/link.md)
- [Access token concept](../human/skupper-docs/input/refdog/concepts/access-token.md)
- [Site resource](../human/skupper-docs/input/refdog/resources/site.md)
- [Creating a site on Kubernetes using YAML](../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [Linking sites on Kubernetes using the CLI](../human/skupper-docs/input/kube-cli/site-linking.md)
- [Load balancing and failover](../human/skupper-docs/input/overview/load-balancing.md)
- [Using the Skupper network console](../human/skupper-docs/input/console/index.md)
- [Connector concept](./connector.md)
- [Listener concept](./listener.md)
- [Routing key concept](./routing-key.md)
- [Network Observer API](./network-observer-api.md)

Code blocks (8):
- `yaml`
- `yaml`
- `bash`
- `text`
- `bash`
- `text`
- `bash`
- `text`

## `generated/concepts/network-observer-api.md`

Headings (22):
- # Network Observer API
- ## Outcome
- ## API Overview
- ## Listeners and Connectors
- ### Listener Endpoints
- #### GET
- #### GET
- ### Connector Endpoints
- #### GET
- #### GET
- ## Listener Schema
- ### Listener Properties
- ## Connector Schema
- ### Connector Properties
- ## Key Relationship: Routing Keys
- ### Service Binding Status
- ## Difference from Configuration API
- ### Example Workflow
- ## Additional Resources
- ## Key Properties
- ## Use Cases
- ## References

Links (7):
- [Console documentation](../input/console/index.md)
- [Console configuration](../input/console/configuration.md)
- [Skupper Network Observer OpenAPI Specification](../human/skupper-openapi-spec/openapi.yaml)
- [DeepWiki: Network Observer API](https://deepwiki.com/search/what-parts-of-api-at-httpsgith_b41ecad0-e4e7-450a-8997-72ecb4efb16c?mode=deep)
- [Listener Concept](./listener.md)
- [Connector Concept](./connector.md)
- [Routing Key Concept](./routing-key.md)

Code blocks (8):
- `text`
- `json`
- `json`
- `text`
- `json`
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/concepts/router-bindings.md`

Headings (13):
- # Router Bindings
- ## Where bindings sit in the architecture
- ## struct ()
- ## Listener →
- ## Connector →
- ### Host-based connector
- ### Pod-selector connector (Kubernetes)
- ### Bridge entry structure
- ## Pod watcher ()
- ## Multi-key listeners
- ## Listener services (Kubernetes)
- ## Binding status conditions
- ## References

Links (9):
- [Routing Key](./routing-key.md)
- [Routing Key](./routing-key.md)
- [](../human/skupper/internal/site/bindings.go)
- [](../human/skupper/internal/site/connector.go)
- [](../human/skupper/internal/site/listener.go)
- [](../human/skupper/internal/kube/site/bindings.go)
- [Routing Key concept](./routing-key.md)
- [Site Controller concept](./site-controller.md)
- [Kube Adaptor concept](./kube-adaptor.md)

Code blocks (8):
- `unspecified`
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`

## `generated/concepts/routing-key.md`

Headings (17):
- # Routing Key
- ## Outcome
- ## How Routing Keys Work
- ### API Level
- ### Router Network Level
- ## Status Feedback
- ## Per-Pod Qualified Addresses
- ## Listener-side Routing Policy — Multiple Routing Keys on One Endpoint
- ### Priority Strategy
- ### Weighted Strategy
- ## Network Observer API
- ### Service Resource
- ### Connection Resource
- ### Flow Aggregate Resource
- ## Summary Flow
- ## Key Properties
- ## References

Links (9):
- [Service exposure with YAML (Kubernetes)](../input/kube-yaml/service-exposure.md)
- [Service exposure with YAML (local systems)](../input/system-yaml/service-exposure.md)
- [Service exposure with CLI (local systems)](../input/system-cli/service-exposure.md)
- [Network Observer API](./network-observer-api.md)
- [Network Observer API Reference](../sources/skupper-openapi-spec-api-reference.md)
- [Skupper Network Observer OpenAPI Specification](../human/skupper-openapi-spec/openapi.yaml)
- [DeepWiki: Routing Keys](https://deepwiki.com/search/describe-routing-keys_2253deab-7e55-44b3-a894-d02a8eeba282?mode=deep)
- [Skupper Connector Concept](./connector.md)
- [Skupper Listener Concept](./listener.md)

Code blocks (14):
- `text`
- `yaml`
- `yaml`
- `go`
- `yaml`
- `yaml`
- `go`
- `yaml`
- `go`
- `yaml`
- `go`
- `json`
- `json`
- `text`

## `generated/concepts/secured-access.md`

Headings (10):
- # SecuredAccess
- ## The chain:  →  →
- ## Access types
- ## SecuredAccessManager internals
- ### Reconcile flow
- ### The  interface
- ## Relationship to
- ## Recovery
- ## Environment variables / flags
- ## References

Links (5):
- [](../human/skupper/internal/kube/securedaccess/access.go)
- [](../human/skupper/internal/kube/securedaccess/config.go)
- [Site Controller concept](./site-controller.md)
- [Default Site concept](./default-site.md)
- [Certificate Manager concept](./certificate-manager.md)

Code blocks (8):
- `unspecified`
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`
- `go`

## `generated/concepts/site-controller.md`

Headings (12):
- # Site Controller
- ## Role in the architecture
- ## Controller struct and sub-managers
- ## Namespace scope
- ## Informers registered at startup
- ## Initialisation sequence
- ## Per-namespace Site objects
- ## What  does
- ## AccessToken handling
- ## Network status propagation
- ## Configuration reference
- ## References

Links (13):
- [kube-adaptor](./kube-adaptor.md)
- [](../human/skupper/internal/kube/controller/controller.go)
- [](../human/skupper/internal/kube/site/site.go)
- [Default Site](./default-site.md)
- [Access Grants and Tokens](./access-grants-and-tokens.md)
- [](../human/skupper/internal/kube/controller/controller.go)
- [](../human/skupper/internal/kube/controller/config.go)
- [](../human/skupper/internal/kube/site/site.go)
- [Kube Adaptor concept](./kube-adaptor.md)
- [Default Site concept](./default-site.md)
- [SecuredAccess concept](./secured-access.md)
- [Certificate Manager concept](./certificate-manager.md)
- [Access Grants and Tokens concept](./access-grants-and-tokens.md)

Code blocks (6):
- `unspecified`
- `go`
- `unspecified`
- `go`
- `go`
- `go`

## `generated/concepts/system-controller.md`

Headings (12):
- # System Controller (Non-Kubernetes)
- ## Contrast with the Kubernetes path
- ## Entry point
- ## Namespace discovery ()
- ## Per-namespace handler chain
- ### 
- ### 
- ### (auto-reload mode only)
- ### 
- ## Config file location
- ## Environment variables
- ## References

Links (7):
- [site controller](./site-controller.md)
- [](../human/skupper/cmd/system-controller/main.go)
- [](../human/skupper/internal/nonkube/controller/system_adaptor.go)
- [](../human/skupper/internal/nonkube/controller/system_adaptor_handler.go)
- [](../human/skupper/internal/nonkube/controller/router_state_handler.go)
- [Site Controller concept](./site-controller.md)
- [Kube Adaptor concept](./kube-adaptor.md)

Code blocks (5):
- `unspecified`
- `go`
- `go`
- `go`
- `unspecified`

## `generated/enterprise-session-recovery/amqp-jms.md`

Headings (6):
- # AMQP (and JMS)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Reconnectable Session](./reconnectable-session.md)
- [Durable Position](./durable-position.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [Events (and Messaging)](./events-messaging.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/automatic-reconnect-failover.md`

Headings (6):
- # Automatic Reconnect (and failover)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (14):
- [Failure Detection](./failure-detection.md)
- [Endpoint Discovery](./endpoint-discovery.md)
- [Durable-Position Recovery](./durable-position-recovery.md)
- [Session Resumption](./logical-session-resume.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)
- [Topology Reconstruction (and subscriptions)](./topology-reconstruction.md)
- [Transparent Replay (session and work)](./transparent-work-replay.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/bounded-session-resumption.md`

Headings (6):
- # Bounded Resumption
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (8):
- [ZooKeeper (Curator)](./zookeeper-curator-stack.md)
- [MQTT (Paho Java)](./mqtt-paho-stack.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/broker-database-endpoints.md`

Headings (6):
- # Broker (and database endpoints)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (14):
- [Network Path](./network-path.md)
- [Durable Checkpoint (offset or cursor)](./durable-checkpoint.md)
- [Durable Delivery State (and topology)](./durable-delivery-topology.md)
- [Endpoint Discovery](./endpoint-discovery.md)
- [Failure Detection](./failure-detection.md)
- [Idempotency (deduplication and fencing)](./idempotency-and-fencing.md)
- [Session Identity](./session-identity.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Listener concept](../concepts/listener.md)
- [Connector concept](../concepts/connector.md)
- [Routing key concept](../concepts/routing-key.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/connection-pool.md`

Headings (6):
- # Connection Pool
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Failure Detection](./failure-detection.md)
- [TCP Connection](./tcp-connection.md)
- [Connection Replacement](./connection-replacement.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/connection-replacement.md`

Headings (6):
- # Connection Replacement
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Connection Pool](./connection-pool.md)
- [Failure Detection](./failure-detection.md)
- [JDBC (PostgreSQL or MySQL + HikariCP)](./ordinary-jdbc-stack.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/database-access.md`

Headings (6):
- # Database Access
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (8):
- [Direct DB (JDBC/native)](./direct-db.md)
- [Redis Protocol](./redis.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/dhcp.md`

Headings (6):
- # DHCP
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Independent Exchange](./independent-request.md)
- [UDP](./udp.md)
- [Network Path](./network-path.md)
- [Office Operations](./office-operations.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)
- [Link status](../skupper-docs-landscape/link-status.md)
- [Secure links](../skupper-docs-landscape/secure-links.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/direct-db.md`

Headings (6):
- # Direct DB (JDBC/native)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Socket-Bound Session](./socket-bound.md)
- [Pooled Reuse](./pooled-reuse.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [Database Access](./database-access.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/dns.md`

Headings (6):
- # DNS
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (16):
- [Independent Exchange](./independent-request.md)
- [UDP](./udp.md)
- [TCP](./tcp.md)
- [Network Path](./network-path.md)
- [Identity (and Naming)](./identity-naming.md)
- [Kerberos](./kerberos.md)
- [LDAP](./ldap.md)
- [NFS](./nfs.md)
- [SMB (Samba)](./smb.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Links](../skupper-docs-landscape/links.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/durable-checkpoint.md`

Headings (6):
- # Durable Checkpoint (offset or cursor)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (9):
- [Broker (and database endpoints)](./broker-database-endpoints.md)
- [Durable-Position Recovery](./durable-position-recovery.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)
- [Traffic baseline](../skupper-docs-landscape/traffic-baseline.md)
- [Evidence bundle](../skupper-docs-landscape/evidence-bundle.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Listener concept](../concepts/listener.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/durable-delivery-topology.md`

Headings (6):
- # Durable Delivery State (and topology)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (9):
- [Broker (and database endpoints)](./broker-database-endpoints.md)
- [Topology Reconstruction (and subscriptions)](./topology-reconstruction.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)
- [Traffic baseline](../skupper-docs-landscape/traffic-baseline.md)
- [Evidence bundle](../skupper-docs-landscape/evidence-bundle.md)
- [Listener concept](../concepts/listener.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/durable-position-recovery.md`

Headings (6):
- # Durable-Position Recovery
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Durable Checkpoint (offset or cursor)](./durable-checkpoint.md)
- [Idempotency (deduplication and fencing)](./idempotency-and-fencing.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)
- [IBM MQ (JMS)](./ibm-mq-jms-stack.md)
- [Kafka (Java Client or Spring)](./kafka-java-stack.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)
- [Traffic baseline](../skupper-docs-landscape/traffic-baseline.md)
- [Evidence bundle](../skupper-docs-landscape/evidence-bundle.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/durable-position.md`

Headings (6):
- # Durable Position
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (9):
- [Reconnect (and Retry)](./reconnect-retry.md)
- [AMQP (and JMS)](./amqp-jms.md)
- [Kafka](./kafka.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/durable-processing-progress.md`

Headings (6):
- # Durable Progress
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (9):
- [Kafka (Java Client or Spring)](./kafka-java-stack.md)
- [IBM MQ (JMS)](./ibm-mq-jms-stack.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/endpoint-discovery.md`

Headings (6):
- # Endpoint Discovery
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Broker (and database endpoints)](./broker-database-endpoints.md)
- [Network Path](./network-path.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Listener concept](../concepts/listener.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/events-messaging.md`

Headings (6):
- # Events (and Messaging)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Kafka](./kafka.md)
- [AMQP (and JMS)](./amqp-jms.md)
- [MQTT](./mqtt.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/explicit-application-recovery.md`

Headings (6):
- # Application Recovery
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (7):
- [JDBC (PostgreSQL or MySQL + HikariCP)](./ordinary-jdbc-stack.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/failure-detection.md`

Headings (6):
- # Failure Detection
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (14):
- [TCP Connection](./tcp-connection.md)
- [Broker (and database endpoints)](./broker-database-endpoints.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)
- [Connection Pool](./connection-pool.md)
- [Connection Replacement](./connection-replacement.md)
- [Bounded Retry (and backoff)](./retry-policy.md)
- [Session Resume Window](./session-expiry-window.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)
- [Traffic baseline](../skupper-docs-landscape/traffic-baseline.md)
- [Evidence bundle](../skupper-docs-landscape/evidence-bundle.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/file-sharing.md`

Headings (6):
- # File Sharing
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (2):
- [SMB (Samba)](./smb.md)
- [NFS](./nfs.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/heartbeat-and-keepalive.md`

Headings (6):
- # Heartbeats (and TCP keepalive)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (11):
- [TCP Connection](./tcp-connection.md)
- [NAT (and firewall state)](./nat-firewall-state.md)
- [Idle Timeout (load balancer or proxy)](./load-balancer-proxy-timeout.md)
- [Same TCP Connection](./same-tcp-continuity.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/http1.md`

Headings (6):
- # HTTP/1.1
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Pooled Reuse](./pooled-reuse.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [Web (and APIs)](./web-api-access.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/http2-grpc.md`

Headings (6):
- # HTTP/2 (and gRPC)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Multiplexed Session](./multiplexed-session.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [Web (and APIs)](./web-api-access.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/http3-quic.md`

Headings (6):
- # HTTP/3 (QUIC)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (8):
- [Independent Exchange](./independent-request.md)
- [Multiplexed Session](./multiplexed-session.md)
- [TLS](./tls.md)
- [QUIC](./quic.md)
- [Web (and APIs)](./web-api-access.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/ibm-mq-jms-stack.md`

Headings (6):
- # IBM MQ (JMS)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Session Resumption](./logical-session-resume.md)
- [Durable-Position Recovery](./durable-position-recovery.md)
- [Durable Progress](./durable-processing-progress.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/idempotency-and-fencing.md`

Headings (6):
- # Idempotency (deduplication and fencing)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (11):
- [Broker (and database endpoints)](./broker-database-endpoints.md)
- [Durable-Position Recovery](./durable-position-recovery.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)
- [Known Transaction Outcome](./transaction-outcome.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Listener concept](../concepts/listener.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/identity-naming.md`

Headings (6):
- # Identity (and Naming)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [LDAP](./ldap.md)
- [Kerberos](./kerberos.md)
- [DNS](./dns.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/independent-request.md`

Headings (6):
- # Independent Exchange
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (14):
- [Network Path](./network-path.md)
- [DHCP](./dhcp.md)
- [DNS](./dns.md)
- [HTTP/3 (QUIC)](./http3-quic.md)
- [IPP (Printing)](./ipp.md)
- [Kerberos](./kerberos.md)
- [SNMP](./snmp.md)
- [Syslog](./syslog.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)
- [Link status](../skupper-docs-landscape/link-status.md)
- [Secure links](../skupper-docs-landscape/secure-links.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/index.md`

Headings (6):
- # Enterprise Session Recovery
- ## Map
- ## Dependency Check
- ## Topics
- ### Enterprise TCP Sessions and Recovery
- ### Enterprise Traffic Patterns

Links (81):
- [Blockscape map wrapper](../maps/enterprise-session-recovery.md)
- [Seamless Continuity](./seamless-work-continuity.md)
- [Bounded Resumption](./bounded-session-resumption.md)
- [Durable Progress](./durable-processing-progress.md)
- [Recoverable Topology](./recoverable-messaging-topology.md)
- [Application Recovery](./explicit-application-recovery.md)
- [Oracle TAC (JDBC Replay + UCP)](./oracle-tac-stack.md)
- [IBM MQ (JMS)](./ibm-mq-jms-stack.md)
- [ZooKeeper (Curator)](./zookeeper-curator-stack.md)
- [Kafka (Java Client or Spring)](./kafka-java-stack.md)
- [MQTT (Paho Java)](./mqtt-paho-stack.md)
- [AMQP (RabbitMQ or Qpid JMS)](./rabbitmq-qpid-stack.md)
- [JDBC (PostgreSQL or MySQL + HikariCP)](./ordinary-jdbc-stack.md)
- [Transparent Replay (session and work)](./transparent-work-replay.md)
- [Session Resumption](./logical-session-resume.md)
- [Durable-Position Recovery](./durable-position-recovery.md)
- [Topology Reconstruction (and subscriptions)](./topology-reconstruction.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)
- [Connection Replacement](./connection-replacement.md)
- [Same TCP Connection](./same-tcp-continuity.md)
- [Tracked Session State](./tracked-session-state.md)
- [Known Transaction Outcome](./transaction-outcome.md)
- [Session Identity](./session-identity.md)
- [Session Resume Window](./session-expiry-window.md)
- [Durable Checkpoint (offset or cursor)](./durable-checkpoint.md)
- [Durable Delivery State (and topology)](./durable-delivery-topology.md)
- [Idempotency (deduplication and fencing)](./idempotency-and-fencing.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)
- [Failure Detection](./failure-detection.md)
- [Bounded Retry (and backoff)](./retry-policy.md)
- [Connection Pool](./connection-pool.md)
- [Heartbeats (and TCP keepalive)](./heartbeat-and-keepalive.md)
- [Endpoint Discovery](./endpoint-discovery.md)
- [TCP Connection](./tcp-connection.md)
- [Network Path](./network-path.md)
- [NAT (and firewall state)](./nat-firewall-state.md)
- [Idle Timeout (load balancer or proxy)](./load-balancer-proxy-timeout.md)
- [Broker (and database endpoints)](./broker-database-endpoints.md)
- [Web (and APIs)](./web-api-access.md)
- [Remote Access](./remote-access.md)
- [Database Access](./database-access.md)
- [Events (and Messaging)](./events-messaging.md)
- [File Sharing](./file-sharing.md)
- [Identity (and Naming)](./identity-naming.md)
- [Office Operations](./office-operations.md)
- [HTTP/1.1](./http1.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [HTTP/3 (QUIC)](./http3-quic.md)
- [WebSocket](./websocket.md)
- [SSH (and SFTP)](./ssh-sftp.md)
- [RDP](./rdp.md)
- [Direct DB (JDBC/native)](./direct-db.md)
- [Kafka](./kafka.md)
- [AMQP (and JMS)](./amqp-jms.md)
- [MQTT](./mqtt.md)
- [Redis Protocol](./redis.md)
- [SMB (Samba)](./smb.md)
- [NFS](./nfs.md)
- [LDAP](./ldap.md)
- [Kerberos](./kerberos.md)
- [DNS](./dns.md)
- [DHCP](./dhcp.md)
- [SMTP (and IMAP)](./mail.md)
- [IPP (Printing)](./ipp.md)
- [SIP (and RTP)](./sip-rtp.md)
- [SNMP](./snmp.md)
- [Syslog](./syslog.md)
- [Independent Exchange](./independent-request.md)
- [Pooled Reuse](./pooled-reuse.md)
- [Multiplexed Session](./multiplexed-session.md)
- [Socket-Bound Session](./socket-bound.md)
- [Reconnectable Session](./reconnectable-session.md)
- [Durable Position](./durable-position.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TCP](./tcp.md)
- [UDP](./udp.md)
- [QUIC](./quic.md)
- [TLS](./tls.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [Middleboxes (NAT, firewall, LB)](./middleboxes.md)
- [Network Path](./network-path.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/ipp.md`

Headings (6):
- # IPP (Printing)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Independent Exchange](./independent-request.md)
- [Pooled Reuse](./pooled-reuse.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [Office Operations](./office-operations.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/kafka-java-stack.md`

Headings (6):
- # Kafka (Java Client or Spring)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Durable-Position Recovery](./durable-position-recovery.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)
- [Durable Progress](./durable-processing-progress.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/kafka.md`

Headings (6):
- # Kafka
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Durable Position](./durable-position.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [Events (and Messaging)](./events-messaging.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/keepalive-timeouts.md`

Headings (6):
- # Keepalive (and Timeouts)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (15):
- [TCP](./tcp.md)
- [Middleboxes (NAT, firewall, LB)](./middleboxes.md)
- [MQTT](./mqtt.md)
- [Multiplexed Session](./multiplexed-session.md)
- [Pooled Reuse](./pooled-reuse.md)
- [Socket-Bound Session](./socket-bound.md)
- [SSH (and SFTP)](./ssh-sftp.md)
- [WebSocket](./websocket.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/kerberos.md`

Headings (6):
- # Kerberos
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (11):
- [Independent Exchange](./independent-request.md)
- [UDP](./udp.md)
- [TCP](./tcp.md)
- [DNS](./dns.md)
- [Identity (and Naming)](./identity-naming.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/ldap.md`

Headings (6):
- # LDAP
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (13):
- [Pooled Reuse](./pooled-reuse.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [DNS](./dns.md)
- [Identity (and Naming)](./identity-naming.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/load-balancer-proxy-timeout.md`

Headings (6):
- # Idle Timeout (load balancer or proxy)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (8):
- [Network Path](./network-path.md)
- [Heartbeats (and TCP keepalive)](./heartbeat-and-keepalive.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)
- [Link status](../skupper-docs-landscape/link-status.md)
- [Secure links](../skupper-docs-landscape/secure-links.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/logical-session-resume.md`

Headings (6):
- # Session Resumption
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (13):
- [Session Identity](./session-identity.md)
- [Session Resume Window](./session-expiry-window.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)
- [IBM MQ (JMS)](./ibm-mq-jms-stack.md)
- [MQTT (Paho Java)](./mqtt-paho-stack.md)
- [ZooKeeper (Curator)](./zookeeper-curator-stack.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/mail.md`

Headings (6):
- # SMTP (and IMAP)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Pooled Reuse](./pooled-reuse.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [Office Operations](./office-operations.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/middleboxes.md`

Headings (6):
- # Middleboxes (NAT, firewall, LB)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (9):
- [Network Path](./network-path.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)
- [Link status](../skupper-docs-landscape/link-status.md)
- [Secure links](../skupper-docs-landscape/secure-links.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/mqtt-paho-stack.md`

Headings (6):
- # MQTT (Paho Java)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Session Resumption](./logical-session-resume.md)
- [Topology Reconstruction (and subscriptions)](./topology-reconstruction.md)
- [Bounded Resumption](./bounded-session-resumption.md)
- [Recoverable Topology](./recoverable-messaging-topology.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/mqtt.md`

Headings (6):
- # MQTT
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Reconnectable Session](./reconnectable-session.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [Events (and Messaging)](./events-messaging.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/multiplexed-session.md`

Headings (6):
- # Multiplexed Session
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (11):
- [TCP](./tcp.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [HTTP/3 (QUIC)](./http3-quic.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/nat-firewall-state.md`

Headings (6):
- # NAT (and firewall state)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (8):
- [Network Path](./network-path.md)
- [Heartbeats (and TCP keepalive)](./heartbeat-and-keepalive.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)
- [Link status](../skupper-docs-landscape/link-status.md)
- [Secure links](../skupper-docs-landscape/secure-links.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/network-path.md`

Headings (6):
- # Network Path
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (19):
- [Broker (and database endpoints)](./broker-database-endpoints.md)
- [DHCP](./dhcp.md)
- [DNS](./dns.md)
- [Endpoint Discovery](./endpoint-discovery.md)
- [Independent Exchange](./independent-request.md)
- [Idle Timeout (load balancer or proxy)](./load-balancer-proxy-timeout.md)
- [Middleboxes (NAT, firewall, LB)](./middleboxes.md)
- [NAT (and firewall state)](./nat-firewall-state.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TCP](./tcp.md)
- [TCP Connection](./tcp-connection.md)
- [TLS](./tls.md)
- [UDP](./udp.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)
- [Link status](../skupper-docs-landscape/link-status.md)
- [Secure links](../skupper-docs-landscape/secure-links.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/nfs.md`

Headings (6):
- # NFS
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Reconnectable Session](./reconnectable-session.md)
- [TCP](./tcp.md)
- [DNS](./dns.md)
- [File Sharing](./file-sharing.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/office-operations.md`

Headings (6):
- # Office Operations
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [SMTP (and IMAP)](./mail.md)
- [IPP (Printing)](./ipp.md)
- [SIP (and RTP)](./sip-rtp.md)
- [SNMP](./snmp.md)
- [Syslog](./syslog.md)
- [DHCP](./dhcp.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/oracle-tac-stack.md`

Headings (6):
- # Oracle TAC (JDBC Replay + UCP)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (8):
- [Transparent Replay (session and work)](./transparent-work-replay.md)
- [Seamless Continuity](./seamless-work-continuity.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/ordinary-jdbc-stack.md`

Headings (6):
- # JDBC (PostgreSQL or MySQL + HikariCP)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Same TCP Connection](./same-tcp-continuity.md)
- [Connection Replacement](./connection-replacement.md)
- [Application Recovery](./explicit-application-recovery.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/pooled-reuse.md`

Headings (6):
- # Pooled Reuse
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (14):
- [TCP](./tcp.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [Direct DB (JDBC/native)](./direct-db.md)
- [HTTP/1.1](./http1.md)
- [IPP (Printing)](./ipp.md)
- [LDAP](./ldap.md)
- [SMTP (and IMAP)](./mail.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/quic.md`

Headings (6):
- # QUIC
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (2):
- [UDP](./udp.md)
- [HTTP/3 (QUIC)](./http3-quic.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/rabbitmq-qpid-stack.md`

Headings (6):
- # AMQP (RabbitMQ or Qpid JMS)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Topology Reconstruction (and subscriptions)](./topology-reconstruction.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)
- [Recoverable Topology](./recoverable-messaging-topology.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/rdp.md`

Headings (6):
- # RDP
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Reconnectable Session](./reconnectable-session.md)
- [TCP](./tcp.md)
- [UDP](./udp.md)
- [Remote Access](./remote-access.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/reconnect-and-retry.md`

Headings (6):
- # Reconnect (and retry)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (11):
- [Idempotency (deduplication and fencing)](./idempotency-and-fencing.md)
- [Bounded Retry (and backoff)](./retry-policy.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)
- [Kafka (Java Client or Spring)](./kafka-java-stack.md)
- [AMQP (RabbitMQ or Qpid JMS)](./rabbitmq-qpid-stack.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/reconnect-retry.md`

Headings (6):
- # Reconnect (and Retry)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (17):
- [Network Path](./network-path.md)
- [Middleboxes (NAT, firewall, LB)](./middleboxes.md)
- [Durable Position](./durable-position.md)
- [HTTP/1.1](./http1.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [Kafka](./kafka.md)
- [LDAP](./ldap.md)
- [SMTP (and IMAP)](./mail.md)
- [Reconnectable Session](./reconnectable-session.md)
- [Redis Protocol](./redis.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/reconnectable-session.md`

Headings (6):
- # Reconnectable Session
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (13):
- [Reconnect (and Retry)](./reconnect-retry.md)
- [AMQP (and JMS)](./amqp-jms.md)
- [MQTT](./mqtt.md)
- [NFS](./nfs.md)
- [RDP](./rdp.md)
- [SIP (and RTP)](./sip-rtp.md)
- [SMB (Samba)](./smb.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/recoverable-messaging-topology.md`

Headings (6):
- # Recoverable Topology
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (8):
- [AMQP (RabbitMQ or Qpid JMS)](./rabbitmq-qpid-stack.md)
- [MQTT (Paho Java)](./mqtt-paho-stack.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/redis.md`

Headings (6):
- # Redis Protocol
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Socket-Bound Session](./socket-bound.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [Database Access](./database-access.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/remote-access.md`

Headings (6):
- # Remote Access
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (8):
- [SSH (and SFTP)](./ssh-sftp.md)
- [RDP](./rdp.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/retry-policy.md`

Headings (6):
- # Bounded Retry (and backoff)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (9):
- [Failure Detection](./failure-detection.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)
- [Traffic baseline](../skupper-docs-landscape/traffic-baseline.md)
- [Evidence bundle](../skupper-docs-landscape/evidence-bundle.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/same-tcp-continuity.md`

Headings (6):
- # Same TCP Connection
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Heartbeats (and TCP keepalive)](./heartbeat-and-keepalive.md)
- [TCP Connection](./tcp-connection.md)
- [JDBC (PostgreSQL or MySQL + HikariCP)](./ordinary-jdbc-stack.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/seamless-work-continuity.md`

Headings (6):
- # Seamless Continuity
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (7):
- [Oracle TAC (JDBC Replay + UCP)](./oracle-tac-stack.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/session-expiry-window.md`

Headings (6):
- # Session Resume Window
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (9):
- [Failure Detection](./failure-detection.md)
- [Session Resumption](./logical-session-resume.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/session-identity.md`

Headings (6):
- # Session Identity
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Broker (and database endpoints)](./broker-database-endpoints.md)
- [Session Resumption](./logical-session-resume.md)
- [Tracked Session State](./tracked-session-state.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Listener concept](../concepts/listener.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/sip-rtp.md`

Headings (6):
- # SIP (and RTP)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Reconnectable Session](./reconnectable-session.md)
- [UDP](./udp.md)
- [TCP](./tcp.md)
- [Office Operations](./office-operations.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/smb.md`

Headings (6):
- # SMB (Samba)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Reconnectable Session](./reconnectable-session.md)
- [TCP](./tcp.md)
- [DNS](./dns.md)
- [File Sharing](./file-sharing.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/snmp.md`

Headings (6):
- # SNMP
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (10):
- [Independent Exchange](./independent-request.md)
- [UDP](./udp.md)
- [TCP](./tcp.md)
- [Office Operations](./office-operations.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/socket-bound.md`

Headings (6):
- # Socket-Bound Session
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (13):
- [TCP](./tcp.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [Direct DB (JDBC/native)](./direct-db.md)
- [Redis Protocol](./redis.md)
- [SSH (and SFTP)](./ssh-sftp.md)
- [WebSocket](./websocket.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/ssh-sftp.md`

Headings (6):
- # SSH (and SFTP)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (11):
- [Socket-Bound Session](./socket-bound.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [TCP](./tcp.md)
- [Remote Access](./remote-access.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/syslog.md`

Headings (6):
- # Syslog
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Independent Exchange](./independent-request.md)
- [UDP](./udp.md)
- [TCP](./tcp.md)
- [TLS](./tls.md)
- [Office Operations](./office-operations.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/tcp-connection.md`

Headings (6):
- # TCP Connection
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Network Path](./network-path.md)
- [Connection Pool](./connection-pool.md)
- [Failure Detection](./failure-detection.md)
- [Heartbeats (and TCP keepalive)](./heartbeat-and-keepalive.md)
- [Same TCP Connection](./same-tcp-continuity.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/tcp.md`

Headings (6):
- # TCP
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (32):
- [Network Path](./network-path.md)
- [AMQP (and JMS)](./amqp-jms.md)
- [Direct DB (JDBC/native)](./direct-db.md)
- [DNS](./dns.md)
- [HTTP/1.1](./http1.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [IPP (Printing)](./ipp.md)
- [Kafka](./kafka.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [Kerberos](./kerberos.md)
- [LDAP](./ldap.md)
- [SMTP (and IMAP)](./mail.md)
- [MQTT](./mqtt.md)
- [Multiplexed Session](./multiplexed-session.md)
- [NFS](./nfs.md)
- [Pooled Reuse](./pooled-reuse.md)
- [RDP](./rdp.md)
- [Redis Protocol](./redis.md)
- [SIP (and RTP)](./sip-rtp.md)
- [SMB (Samba)](./smb.md)
- [SNMP](./snmp.md)
- [Socket-Bound Session](./socket-bound.md)
- [SSH (and SFTP)](./ssh-sftp.md)
- [Syslog](./syslog.md)
- [WebSocket](./websocket.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Links](../skupper-docs-landscape/links.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/tls.md`

Headings (6):
- # TLS
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (21):
- [Network Path](./network-path.md)
- [AMQP (and JMS)](./amqp-jms.md)
- [Direct DB (JDBC/native)](./direct-db.md)
- [HTTP/1.1](./http1.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [HTTP/3 (QUIC)](./http3-quic.md)
- [IPP (Printing)](./ipp.md)
- [Kafka](./kafka.md)
- [LDAP](./ldap.md)
- [SMTP (and IMAP)](./mail.md)
- [MQTT](./mqtt.md)
- [Redis Protocol](./redis.md)
- [Syslog](./syslog.md)
- [WebSocket](./websocket.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/topology-reconstruction.md`

Headings (6):
- # Topology Reconstruction (and subscriptions)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (11):
- [Durable Delivery State (and topology)](./durable-delivery-topology.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)
- [MQTT (Paho Java)](./mqtt-paho-stack.md)
- [AMQP (RabbitMQ or Qpid JMS)](./rabbitmq-qpid-stack.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/tracked-session-state.md`

Headings (6):
- # Tracked Session State
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (8):
- [Session Identity](./session-identity.md)
- [Transparent Replay (session and work)](./transparent-work-replay.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/transaction-outcome.md`

Headings (6):
- # Known Transaction Outcome
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (5):
- [Idempotency (deduplication and fencing)](./idempotency-and-fencing.md)
- [Transparent Replay (session and work)](./transparent-work-replay.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/transparent-work-replay.md`

Headings (6):
- # Transparent Replay (session and work)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (11):
- [Tracked Session State](./tracked-session-state.md)
- [Known Transaction Outcome](./transaction-outcome.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)
- [Oracle TAC (JDBC Replay + UCP)](./oracle-tac-stack.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/udp.md`

Headings (6):
- # UDP
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (15):
- [Network Path](./network-path.md)
- [DHCP](./dhcp.md)
- [DNS](./dns.md)
- [Kerberos](./kerberos.md)
- [QUIC](./quic.md)
- [RDP](./rdp.md)
- [SIP (and RTP)](./sip-rtp.md)
- [SNMP](./snmp.md)
- [Syslog](./syslog.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)
- [Link status](../skupper-docs-landscape/link-status.md)
- [Secure links](../skupper-docs-landscape/secure-links.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/web-api-access.md`

Headings (6):
- # Web (and APIs)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (11):
- [HTTP/1.1](./http1.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [HTTP/3 (QUIC)](./http3-quic.md)
- [WebSocket](./websocket.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/websocket.md`

Headings (6):
- # WebSocket
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (12):
- [Socket-Bound Session](./socket-bound.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [Web (and APIs)](./web-api-access.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

Code blocks (0):
- None

## `generated/enterprise-session-recovery/zookeeper-curator-stack.md`

Headings (6):
- # ZooKeeper (Curator)
- ## Skupper Suitability
- ## Appears in
- ## Dependency Check
- ## Related Skupper Docs
- ## Draft Notes

Links (8):
- [Session Resumption](./logical-session-resume.md)
- [Bounded Resumption](./bounded-session-resumption.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)

Code blocks (0):
- None

## `generated/maps/enterprise-session-recovery.md`

Headings (1):
- # Enterprise Traffic Patterns

Links (1):
- [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/enterprise-session-recovery.bs)

Code blocks (1):
- `bs`

## `generated/maps/platforms.md`

Headings (1):
- # Platforms

Links (1):
- [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/platforms.bs)

Code blocks (1):
- `bs`

## `generated/maps/skupper-adoption-bridge.md`

Headings (1):
- # Skupper Adoption Bridge

Links (1):
- [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/skupper-adoption-bridge.bs)

Code blocks (1):
- `bs`

## `generated/maps/skupper-docs-landscape.md`

Headings (1):
- # Skupper Documentation Landscape

Links (1):
- [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/skupper-docs-landscape.bs)

Code blocks (1):
- `bs`

## `generated/maps/skupper-value-perspectives.md`

Headings (1):
- # skupper-series series

Links (1):
- [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/skupper-value-perspectives.bs)

Code blocks (1):
- `bs`

## `generated/maps/skupper.md`

Headings (1):
- # Skupper

Links (1):
- [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/skupper.bs)

Code blocks (1):
- `bs`

## `generated/maps/togaf.md`

Headings (1):
- # Togaf

Links (1):
- [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/togaf.bs)

Code blocks (1):
- `bs`

## `generated/maps/vms.md`

Headings (1):
- # Vms

Links (1):
- [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/vms.bs)

Code blocks (1):
- `bs`

## `generated/personas/application-developers.md`

Headings (5):
- # Application Developers (Resource Consumers)
- ## Access boundary
- ### On Kubernetes
- ### On Linux hosts
- ## Relevant existing pages

Links (5):
- [Connected Service Across Sites](../skupper-docs-landscape/first-connected-service.md)
- [Service Exposure](../skupper-docs-landscape/service-exposure.md)
- [Listener](../concepts/listener.md)
- [Connector](../concepts/connector.md)
- [Connectivity Validation](../skupper-docs-landscape/first-validation.md)

Code blocks (0):
- None

## `generated/personas/cluster-administrators.md`

Headings (4):
- # Cluster Administrators
- ## Responsibilities
- ## Boundary with Resource Owners
- ## Relevant existing pages

Links (9):
- [Install Skupper](../skupper-docs-landscape/install-skupper.md)
- [Operator Installation](../skupper-docs-landscape/operator-installation.md)
- [Role-Based Access Control](../skupper-docs-landscape/rbac.md)
- [Certificate Manager](../concepts/certificate-manager.md)
- [Site Controller](../concepts/site-controller.md)
- [System Controller](../concepts/system-controller.md)
- [Upgrade Sequence](../skupper-docs-landscape/upgrade-sequence.md)
- [Network Isolation](../skupper-docs-landscape/network-isolation.md)
- [Service Exposure Policy](../skupper-docs-landscape/service-policy.md)

Code blocks (0):
- None

## `generated/personas/database-engineers.md`

Headings (2):
- # Database Engineers
- ## Relevant existing pages

Links (5):
- [Database Access](../enterprise-session-recovery/database-access.md)
- [Direct DB (JDBC/native)](../enterprise-session-recovery/direct-db.md)
- [Connection Pool](../enterprise-session-recovery/connection-pool.md)
- [Connector](../concepts/connector.md)
- [Network Deployment Concerns](../concepts/network-deployment-concerns.md)

Code blocks (0):
- None

## `generated/personas/enterprise-architects.md`

Headings (2):
- # Enterprise Architects
- ## Relevant existing pages

Links (5):
- [Independent Microservice Placement Pattern](../architecture/independent-service-placement.md)
- [Integration Layer Pattern](../architecture/integration-layer.md)
- [Legacy Modernization / Wrapper Pattern](../architecture/legacy-modernization.md)
- [Hybrid-Cloud Elasticity Pattern](../architecture/hybrid-cloud-elasticity.md)
- [Network Deployment Concerns](../concepts/network-deployment-concerns.md)

Code blocks (0):
- None

## `generated/personas/network-security-teams.md`

Headings (2):
- # Network and Security Teams
- ## Relevant existing pages

Links (6):
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Network Isolation](../skupper-docs-landscape/network-isolation.md)
- [Service Exposure Policy](../skupper-docs-landscape/service-policy.md)
- [Role-Based Access Control](../skupper-docs-landscape/rbac.md)
- [Access Grants and Tokens](../concepts/access-grants-and-tokens.md)
- [Certificate Manager](../concepts/certificate-manager.md)

Code blocks (0):
- None

## `generated/personas/platform-engineers.md`

Headings (3):
- # Platform Engineers (Resource Owners)
- ## Responsibilities
- ## Relevant existing pages

Links (5):
- [Hybrid Environment Connectivity](../skupper-docs-landscape/hybrid-environment.md)
- [Kubernetes Cluster Pattern](../skupper-docs-landscape/cluster-pattern.md)
- [Linux Host Pattern](../skupper-docs-landscape/host-pattern.md)
- [Declarative Resources](../skupper-docs-landscape/declarative-resources.md)
- [Mixed Kubernetes and System Workflow](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md)

Code blocks (0):
- None

## `generated/personas/skupper-personas.md`

Headings (1):
- # Skupper Personas

Links (0):
- None

Code blocks (0):
- None

## `generated/personas/technology-leaders.md`

Headings (2):
- # Technology Leaders and Migration Sponsors
- ## Relevant existing pages

Links (6):
- [Legacy Modernization / Wrapper Pattern](../architecture/legacy-modernization.md)
- [Independent Microservice Placement Pattern](../architecture/independent-service-placement.md)
- [Use Case Alignment](../skupper-adoption-bridge/use-case-alignment.md)
- [Incremental Cloud Migration](../skupper-value-perspectives/migration-flexibility.md)
- [Reduced Integration Risk](../skupper-value-perspectives/reduced-integration-risk.md)
- [Workload Placement Freedom](../skupper-value-perspectives/workload-placement.md)

Code blocks (0):
- None

## `generated/skupper/integration-tests.md`

Headings (62):
- # Skupper Integration and E2E Tests
- ## Overview
- ## Integration Tests
- ### Purpose
- ### Architecture
- ### Test Suite Structure
- ### Test Cases
- #### Site Tests ()
- #### Listener Tests ()
- ### Prerequisites
- ### Running Integration Tests
- #### From Repository Root
- #### From tests/ Directory
- #### Against Existing Cluster
- ### Test Execution Details
- ### Known Behavior
- ## End-to-End (E2E) Tests
- ### Purpose
- ### Architecture
- ### Test Scenario Catalog
- #### Hello World ()
- #### Attached Connector ()
- #### High Availability ()
- #### Redis Multi-Cloud HA ()
- #### Labels and Annotations ()
- #### Expose Pods by Name ()
- #### Service Scale ()
- ### E2E Test Framework
- #### Directory Structure
- #### Ansible Collections
- ### Running E2E Tests
- #### Prerequisites
- #### Setup Virtual Environment
- #### Build Test Images (Optional)
- #### Quick Cluster Setup
- #### Run Individual Test
- #### Run Multiple Tests
- #### Test Role Individually
- ### Configuration
- #### Resource Multipliers ()
- #### Namespace Isolation
- ### CI Test Suite
- ## Test Comparison Matrix
- ## Test Coverage Map
- ### What Integration Tests Cover
- ### What E2E Tests Cover
- ## Development Guidelines
- ### Adding Integration Tests
- ### Adding E2E Tests
- ### Test Best Practices
- #### Integration Tests
- #### E2E Tests
- ## Troubleshooting
- ### Integration Tests
- ### E2E Tests
- ## Test Metrics
- ### Integration Test Performance
- ### E2E Test Performance
- ## Future Test Enhancements
- ### Integration Tests
- ### E2E Tests
- ## References

Links (4):
- [envtest](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/envtest)
- [#2251](https://github.com/skupperproject/skupper/issues/2251)
- [envtest documentation](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/envtest)
- [skupperproject/skupper/issues](https://github.com/skupperproject/skupper/issues)

Code blocks (21):
- `unspecified`
- `bash`
- `bash`
- `bash`
- `unspecified`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `yaml`
- `yaml`
- `bash`
- `makefile`
- `go`
- `unspecified`
- `unspecified`
- `bash`
- `bash`
- `bash`

## `generated/skupper/skupper-api-network-observer.md`

Headings (144):
- # Skupper Network Observer HTTP API.
- ## Path Table
- ## Reference Table
- ## Path Details
- ### [GET]/api/v2alpha1/sites
- #### Responses
- ### [GET]/api/v2alpha1/sites/{id}
- #### Responses
- ### [GET]/api/v2alpha1/processes
- #### Responses
- ### [GET]/api/v2alpha1/processes/{id}
- #### Responses
- ### [GET]/api/v2alpha1/routers
- #### Responses
- ### [GET]/api/v2alpha1/routers/{id}
- #### Responses
- ### [GET]/api/v2alpha1/listeners
- #### Responses
- ### [GET]/api/v2alpha1/listeners/{id}
- #### Responses
- ### [GET]/api/v2alpha1/connectors
- #### Responses
- ### [GET]/api/v2alpha1/connectors/{id}
- #### Responses
- ### [GET]/api/v2alpha1/services
- #### Responses
- ### [GET]/api/v2alpha1/services/{id}
- #### Responses
- ### [GET]/api/v2alpha1/components
- #### Responses
- ### [GET]/api/v2alpha1/components/{id}
- #### Responses
- ### [GET]/api/v2alpha1/sitepairs
- #### Responses
- ### [GET]/api/v2alpha1/sitepairs/{id}
- #### Responses
- ### [GET]/api/v2alpha1/componentpairs
- #### Responses
- ### [GET]/api/v2alpha1/componentpairs/{id}
- #### Responses
- ### [GET]/api/v2alpha1/processpairs
- #### Responses
- ### [GET]/api/v2alpha1/processpairs/{id}
- #### Responses
- ### [GET]/api/v2alpha1/routerlinks
- #### Responses
- ### [GET]/api/v2alpha1/routerlinks/{id}
- #### Responses
- ### [GET]/api/v2alpha1/routeraccess
- #### Responses
- ### [GET]/api/v2alpha1/routeraccess/{id}
- #### Responses
- ### [GET]/api/v2alpha1/hosts
- #### Responses
- ### [GET]/api/v2alpha1/hosts/{id}
- #### Responses
- ### [GET]/api/v2alpha1/connections
- #### Responses
- ### [GET]/api/v2alpha1/applicationflows
- #### Responses
- ### [GET]/api/v2alpha1/sites/{id}/processes
- #### Responses
- ### [GET]/api/v2alpha1/sites/{id}/routers
- #### Responses
- ### [GET]/api/v2alpha1/sites/{id}/hosts
- #### Responses
- ### [GET]/api/v2alpha1/services/{id}/processes
- #### Responses
- ### [GET]/api/v2alpha1/services/{id}/processpairs
- #### Responses
- ### [GET]/api/v2alpha1/services/{id}/connections
- #### Responses
- ## References
- ### /components/parameters/pathID
- ### /components/responses/notSupported
- ### /components/responses/errorNotFound
- ### /components/responses/errorBadRequest
- ### /components/responses/getSites
- ### /components/responses/getRouters
- ### /components/responses/getProcesses
- ### /components/responses/getListeners
- ### /components/responses/getConnectors
- ### /components/responses/getServices
- ### /components/responses/getComponents
- ### /components/responses/getFlowAggregates
- ### /components/responses/getRouterLinks
- ### /components/responses/getRouterAccess
- ### /components/responses/getConnections
- ### /components/responses/getApplicationFlows
- ### /components/responses/getSiteByID
- ### /components/responses/getProcessByID
- ### /components/responses/getRouterByID
- ### /components/responses/getListenerByID
- ### /components/responses/getConnectorByID
- ### /components/responses/getServiceByID
- ### /components/responses/getComponentByID
- ### /components/responses/getFlowAggregateByID
- ### /components/responses/getRouterLinkByID
- ### /components/responses/getRouterAccessByID
- ### /components/schemas/collectionResponse
- ### /components/schemas/ErrorResponse
- ### /components/schemas/SiteResponse
- ### /components/schemas/SiteListResponse
- ### /components/schemas/ProcessResponse
- ### /components/schemas/ProcessListResponse
- ### /components/schemas/ListenerResponse
- ### /components/schemas/ListenerListResponse
- ### /components/schemas/ConnectorResponse
- ### /components/schemas/ConnectorListResponse
- ### /components/schemas/RouterListResponse
- ### /components/schemas/RouterResponse
- ### /components/schemas/ServiceListResponse
- ### /components/schemas/ServiceResponse
- ### /components/schemas/ComponentListResponse
- ### /components/schemas/ComponentResponse
- ### /components/schemas/FlowAggregateListResponse
- ### /components/schemas/FlowAggregateResponse
- ### /components/schemas/RouterLinkListResponse
- ### /components/schemas/RouterLinkResponse
- ### /components/schemas/RouterAccessListResponse
- ### /components/schemas/RouterAccessResponse
- ### /components/schemas/ConnectionListResponse
- ### /components/schemas/ConnectionResponse
- ### /components/schemas/ApplicationFlowResponse
- ### /components/schemas/baseRecord
- ### /components/schemas/sitePlatformType
- ### /components/schemas/processBindingType
- ### /components/schemas/serviceIdentifierType
- ### /components/schemas/linkRoleType
- ### /components/schemas/proxyProtocolType
- ### /components/schemas/SiteRecord
- ### /components/schemas/ProcessRecord
- ### /components/schemas/RouterRecord
- ### /components/schemas/ListenerRecord
- ### /components/schemas/ConnectorRecord
- ### /components/schemas/ServiceRecord
- ### /components/schemas/ComponentRecord
- ### /components/schemas/flowAggregatePairType
- ### /components/schemas/FlowAggregateRecord
- ### /components/schemas/operStatusType
- ### /components/schemas/RouterLinkRecord
- ### /components/schemas/RouterAccessRecord
- ### /components/schemas/ConnectionRecord
- ### /components/schemas/ApplicationFlowRecord

Links (105):
- [/api/v2alpha1/sites](#getapiv2alpha1sites)
- [/api/v2alpha1/sites/{id}](#getapiv2alpha1sitesid)
- [/api/v2alpha1/processes](#getapiv2alpha1processes)
- [/api/v2alpha1/processes/{id}](#getapiv2alpha1processesid)
- [/api/v2alpha1/routers](#getapiv2alpha1routers)
- [/api/v2alpha1/routers/{id}](#getapiv2alpha1routersid)
- [/api/v2alpha1/listeners](#getapiv2alpha1listeners)
- [/api/v2alpha1/listeners/{id}](#getapiv2alpha1listenersid)
- [/api/v2alpha1/connectors](#getapiv2alpha1connectors)
- [/api/v2alpha1/connectors/{id}](#getapiv2alpha1connectorsid)
- [/api/v2alpha1/services](#getapiv2alpha1services)
- [/api/v2alpha1/services/{id}](#getapiv2alpha1servicesid)
- [/api/v2alpha1/components](#getapiv2alpha1components)
- [/api/v2alpha1/components/{id}](#getapiv2alpha1componentsid)
- [/api/v2alpha1/sitepairs](#getapiv2alpha1sitepairs)
- [/api/v2alpha1/sitepairs/{id}](#getapiv2alpha1sitepairsid)
- [/api/v2alpha1/componentpairs](#getapiv2alpha1componentpairs)
- [/api/v2alpha1/componentpairs/{id}](#getapiv2alpha1componentpairsid)
- [/api/v2alpha1/processpairs](#getapiv2alpha1processpairs)
- [/api/v2alpha1/processpairs/{id}](#getapiv2alpha1processpairsid)
- [/api/v2alpha1/routerlinks](#getapiv2alpha1routerlinks)
- [/api/v2alpha1/routerlinks/{id}](#getapiv2alpha1routerlinksid)
- [/api/v2alpha1/routeraccess](#getapiv2alpha1routeraccess)
- [/api/v2alpha1/routeraccess/{id}](#getapiv2alpha1routeraccessid)
- [/api/v2alpha1/hosts](#getapiv2alpha1hosts)
- [/api/v2alpha1/hosts/{id}](#getapiv2alpha1hostsid)
- [/api/v2alpha1/connections](#getapiv2alpha1connections)
- [/api/v2alpha1/applicationflows](#getapiv2alpha1applicationflows)
- [/api/v2alpha1/sites/{id}/processes](#getapiv2alpha1sitesidprocesses)
- [/api/v2alpha1/sites/{id}/routers](#getapiv2alpha1sitesidrouters)
- [/api/v2alpha1/sites/{id}/hosts](#getapiv2alpha1sitesidhosts)
- [/api/v2alpha1/services/{id}/processes](#getapiv2alpha1servicesidprocesses)
- [/api/v2alpha1/services/{id}/processpairs](#getapiv2alpha1servicesidprocesspairs)
- [/api/v2alpha1/services/{id}/connections](#getapiv2alpha1servicesidconnections)
- [#/components/parameters/pathID](#componentsparameterspathid)
- [#/components/responses/notSupported](#componentsresponsesnotsupported)
- [#/components/responses/errorNotFound](#componentsresponseserrornotfound)
- [#/components/responses/errorBadRequest](#componentsresponseserrorbadrequest)
- [#/components/responses/getSites](#componentsresponsesgetsites)
- [#/components/responses/getRouters](#componentsresponsesgetrouters)
- [#/components/responses/getProcesses](#componentsresponsesgetprocesses)
- [#/components/responses/getListeners](#componentsresponsesgetlisteners)
- [#/components/responses/getConnectors](#componentsresponsesgetconnectors)
- [#/components/responses/getServices](#componentsresponsesgetservices)
- [#/components/responses/getComponents](#componentsresponsesgetcomponents)
- [#/components/responses/getFlowAggregates](#componentsresponsesgetflowaggregates)
- [#/components/responses/getRouterLinks](#componentsresponsesgetrouterlinks)
- [#/components/responses/getRouterAccess](#componentsresponsesgetrouteraccess)
- [#/components/responses/getConnections](#componentsresponsesgetconnections)
- [#/components/responses/getApplicationFlows](#componentsresponsesgetapplicationflows)
- [#/components/responses/getSiteByID](#componentsresponsesgetsitebyid)
- [#/components/responses/getProcessByID](#componentsresponsesgetprocessbyid)
- [#/components/responses/getRouterByID](#componentsresponsesgetrouterbyid)
- [#/components/responses/getListenerByID](#componentsresponsesgetlistenerbyid)
- [#/components/responses/getConnectorByID](#componentsresponsesgetconnectorbyid)
- [#/components/responses/getServiceByID](#componentsresponsesgetservicebyid)
- [#/components/responses/getComponentByID](#componentsresponsesgetcomponentbyid)
- [#/components/responses/getFlowAggregateByID](#componentsresponsesgetflowaggregatebyid)
- [#/components/responses/getRouterLinkByID](#componentsresponsesgetrouterlinkbyid)
- [#/components/responses/getRouterAccessByID](#componentsresponsesgetrouteraccessbyid)
- [#/components/schemas/collectionResponse](#componentsschemascollectionresponse)
- [#/components/schemas/ErrorResponse](#componentsschemaserrorresponse)
- [#/components/schemas/SiteResponse](#componentsschemassiteresponse)
- [#/components/schemas/SiteListResponse](#componentsschemassitelistresponse)
- [#/components/schemas/ProcessResponse](#componentsschemasprocessresponse)
- [#/components/schemas/ProcessListResponse](#componentsschemasprocesslistresponse)
- [#/components/schemas/ListenerResponse](#componentsschemaslistenerresponse)
- [#/components/schemas/ListenerListResponse](#componentsschemaslistenerlistresponse)
- [#/components/schemas/ConnectorResponse](#componentsschemasconnectorresponse)
- [#/components/schemas/ConnectorListResponse](#componentsschemasconnectorlistresponse)
- [#/components/schemas/RouterListResponse](#componentsschemasrouterlistresponse)
- [#/components/schemas/RouterResponse](#componentsschemasrouterresponse)
- [#/components/schemas/ServiceListResponse](#componentsschemasservicelistresponse)
- [#/components/schemas/ServiceResponse](#componentsschemasserviceresponse)
- [#/components/schemas/ComponentListResponse](#componentsschemascomponentlistresponse)
- [#/components/schemas/ComponentResponse](#componentsschemascomponentresponse)
- [#/components/schemas/FlowAggregateListResponse](#componentsschemasflowaggregatelistresponse)
- [#/components/schemas/FlowAggregateResponse](#componentsschemasflowaggregateresponse)
- [#/components/schemas/RouterLinkListResponse](#componentsschemasrouterlinklistresponse)
- [#/components/schemas/RouterLinkResponse](#componentsschemasrouterlinkresponse)
- [#/components/schemas/RouterAccessListResponse](#componentsschemasrouteraccesslistresponse)
- [#/components/schemas/RouterAccessResponse](#componentsschemasrouteraccessresponse)
- [#/components/schemas/ConnectionListResponse](#componentsschemasconnectionlistresponse)
- [#/components/schemas/ConnectionResponse](#componentsschemasconnectionresponse)
- [#/components/schemas/ApplicationFlowResponse](#componentsschemasapplicationflowresponse)
- [#/components/schemas/baseRecord](#componentsschemasbaserecord)
- [#/components/schemas/sitePlatformType](#componentsschemassiteplatformtype)
- [#/components/schemas/processBindingType](#componentsschemasprocessbindingtype)
- [#/components/schemas/serviceIdentifierType](#componentsschemasserviceidentifiertype)
- [#/components/schemas/linkRoleType](#componentsschemaslinkroletype)
- [#/components/schemas/proxyProtocolType](#componentsschemasproxyprotocoltype)
- [#/components/schemas/SiteRecord](#componentsschemassiterecord)
- [#/components/schemas/ProcessRecord](#componentsschemasprocessrecord)
- [#/components/schemas/RouterRecord](#componentsschemasrouterrecord)
- [#/components/schemas/ListenerRecord](#componentsschemaslistenerrecord)
- [#/components/schemas/ConnectorRecord](#componentsschemasconnectorrecord)
- [#/components/schemas/ServiceRecord](#componentsschemasservicerecord)
- [#/components/schemas/ComponentRecord](#componentsschemascomponentrecord)
- [#/components/schemas/flowAggregatePairType](#componentsschemasflowaggregatepairtype)
- [#/components/schemas/FlowAggregateRecord](#componentsschemasflowaggregaterecord)
- [#/components/schemas/operStatusType](#componentsschemasoperstatustype)
- [#/components/schemas/RouterLinkRecord](#componentsschemasrouterlinkrecord)
- [#/components/schemas/RouterAccessRecord](#componentsschemasrouteraccessrecord)
- [#/components/schemas/ConnectionRecord](#componentsschemasconnectionrecord)
- [#/components/schemas/ApplicationFlowRecord](#componentsschemasapplicationflowrecord)

Code blocks (71):
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`
- `typescript`

## `generated/skupper/skupper-contour-access-guide.md`

Headings (47):
- # Using Contour HTTPProxy Access for Skupper Sites
- ## Overview
- ### When to Use Contour HTTPProxy Access
- ### How HTTPProxy Differs from Ingress
- ## Prerequisites
- ## Controller Configuration
- ### Required Environment Variables
- ### Optional Environment Variables
- ### Configuration via Deployment YAML
- ### Configuration via Helm Chart
- ## Using Contour HTTPProxy with Sites
- ### Method 1: Site linkAccess
- ### Method 2: RouterAccess Resource
- ### Method 3: SecuredAccess Resource
- ## How Contour HTTPProxy Access Works
- ### HTTPProxy Naming and Hostname Generation
- ### HTTPProxy Resource Structure
- ### How TLS Passthrough Works
- ### Endpoint Resolution
- ## Contour Deployment Considerations
- ### Verify Contour is Running
- ### Verify HTTPProxy CRD
- ### Contour Configuration for TLS Passthrough
- ## DNS Configuration
- ### Option 1: Wildcard DNS
- ### Option 2: Specific DNS Records
- ### Option 3: nip.io (Development/Testing)
- ## Dynamic Client and Resource Management
- ## Troubleshooting
- ### HTTPProxy not created
- ### HTTPProxy created but no routing
- ### Endpoints not resolving
- ### Remote site cannot connect
- ### TLS errors
- ## Verification Commands
- ### Check Controller Configuration
- ### Check HTTPProxy Resources
- ### Check HTTPProxy Status
- ### Check Site Endpoints
- ### Test Connectivity
- ### Check Envoy Configuration
- ## Comparison: HTTPProxy vs Ingress
- ## References
- ### Related Documentation
- ### Source Code References
- ### External Resources
- ## Summary

Links (8):
- [Skupper Site CRD](./skupper-crd-sites-skupper-io.md)
- [Skupper RouterAccess CRD](./skupper-crd-routeraccesses-skupper-io.md)
- [Skupper SecuredAccess CRD](./skupper-crd-securedaccesses-skupper-io.md)
- [Skupper Ingress Access Guide](./skupper-ingress-access-guide.md)
- [Contour Documentation](https://projectcontour.io/)
- [HTTPProxy API](https://projectcontour.io/docs/main/config/api/)
- [TLS Passthrough Guide](https://projectcontour.io/docs/main/config/tls-termination/#tls-passthrough)
- [Envoy SNI Routing](https://www.envoyproxy.io/docs/envoy/latest/faq/configuration/sni)

Code blocks (31):
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `bash`
- `unspecified`
- `bash`
- `bash`
- `unspecified`
- `unspecified`
- `yaml`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`

## `generated/skupper/skupper-crd-accessgrants-skupper-io.md`

Headings (1):
- # Skupper CRD: accessgrants-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-accesstokens-skupper-io.md`

Headings (1):
- # Skupper CRD: accesstokens-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-attachedconnectorbindings-skupper-io.md`

Headings (1):
- # Skupper CRD: attachedconnectorbindings-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-attachedconnectors-skupper-io.md`

Headings (1):
- # Skupper CRD: attachedconnectors-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-certificates-skupper-io.md`

Headings (1):
- # Skupper CRD: certificates-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-connectors-skupper-io.md`

Headings (1):
- # Skupper CRD: connectors-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-links-skupper-io.md`

Headings (1):
- # Skupper CRD: links-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-listeners-skupper-io.md`

Headings (1):
- # Skupper CRD: listeners-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-multikeylisteners-skupper-io.md`

Headings (1):
- # Skupper CRD: multikeylisteners-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-routeraccesses-skupper-io.md`

Headings (1):
- # Skupper CRD: routeraccesses-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-securedaccesses-skupper-io.md`

Headings (1):
- # Skupper CRD: securedaccesses-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-crd-sites-skupper-io.md`

Headings (1):
- # Skupper CRD: sites-skupper-io

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper/skupper-gateway-access-guide.md`

Headings (50):
- # Using Gateway API Access for Skupper Sites
- ## Overview
- ### When to Use Gateway API Access
- ### Gateway API Architecture
- ## Prerequisites
- ## Controller Configuration
- ### Required Environment Variables
- ### Optional Environment Variables
- ### Configuration via Deployment YAML
- ### Configuration via Helm Chart
- ### Validation
- ## Using Gateway API with Sites
- ### Method 1: Site linkAccess
- ### Method 2: RouterAccess Resource
- ### Method 3: SecuredAccess Resource
- ## How Gateway API Access Works
- ### Gateway Creation
- ### TLSRoute Creation
- ### TLSRoute Resource Structure
- ### How TLS Passthrough Works with Gateway API
- ### Endpoint Resolution
- ### Domain Auto-Deduction
- ## Gateway API Deployment Considerations
- ### Verify Gateway API CRDs
- ### Verify GatewayClass Exists
- ### Verify Gateway Controller
- ### Check Skupper-Created Gateway
- ## DNS Configuration
- ### Option 1: Wildcard DNS
- ### Option 2: Specific DNS Records
- ### Option 3: Auto-Deduced Domain
- ## Troubleshooting
- ### Gateway not created
- ### TLSRoute not created
- ### Endpoints not resolving
- ### Remote site cannot connect
- ### TLS errors
- ### Gateway controller not accepting resources
- ## Verification Commands
- ### Check Controller Configuration
- ### Check Gateway Resources
- ### Check TLSRoute Resources
- ### Check Site Endpoints
- ### Test Connectivity
- ## Comparison: Gateway API vs Alternatives
- ## References
- ### Related Documentation
- ### Source Code References
- ### External Resources
- ## Summary

Links (10):
- [Skupper Site CRD](./skupper-crd-sites-skupper-io.md)
- [Skupper RouterAccess CRD](./skupper-crd-routeraccesses-skupper-io.md)
- [Skupper SecuredAccess CRD](./skupper-crd-securedaccesses-skupper-io.md)
- [Skupper Ingress Access Guide](./skupper-ingress-access-guide.md)
- [Skupper Contour Access Guide](./skupper-contour-access-guide.md)
- [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/)
- [TLSRoute Reference](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1alpha2.TLSRoute)
- [Gateway API Implementations](https://gateway-api.sigs.k8s.io/implementations/)
- [Istio Gateway](https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/)
- [Envoy Gateway](https://gateway.envoyproxy.io/)

Code blocks (38):
- `yaml`
- `yaml`
- `unspecified`
- `unspecified`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `go`
- `yaml`
- `bash`
- `bash`
- `bash`
- `bash`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`

## `generated/skupper/skupper-ingress-access-guide.md`

Headings (44):
- # Using Ingress Access for Skupper Sites
- ## Overview
- ### When to Use Ingress Access
- ### Difference Between  and
- ## Prerequisites
- ## Controller Configuration
- ### Required Environment Variables
- ### Optional Environment Variables
- ### Configuration via Deployment YAML
- #### For NGINX Ingress Controller
- #### For Generic Ingress Controller
- ### Configuration via Helm Chart
- ## Using Ingress with Sites
- ### Method 1: Site linkAccess
- ### Method 2: RouterAccess Resource
- ### Method 3: SecuredAccess Resource
- ## How Ingress Access Works
- ### Hostname Generation
- ### Ingress Resource Structure
- ### Endpoint Resolution
- ## NGINX Ingress Controller Configuration
- ### Enable TLS Passthrough
- ### Annotations Added by Skupper
- ## DNS Configuration
- ### Option 1: Wildcard DNS
- ### Option 2: Specific DNS Records
- ### Option 3: nip.io (Development/Testing)
- ## Troubleshooting
- ### Ingress not created
- ### Endpoints not resolving
- ### Remote site cannot connect
- ### SSL passthrough not working (NGINX)
- ### Wrong IngressClass used
- ## Verification Commands
- ### Check Controller Configuration
- ### Check Ingress Resources
- ### Check Site Endpoints
- ### Test Connectivity
- ## Comparison: ingress vs ingress-nginx
- ## References
- ### Related Documentation
- ### Source Code References
- ### External Resources
- ## Summary

Links (8):
- [Skupper Site CRD](./skupper-crd-sites-skupper-io.md)
- [Skupper RouterAccess CRD](./skupper-crd-routeraccesses-skupper-io.md)
- [Skupper SecuredAccess CRD](./skupper-crd-securedaccesses-skupper-io.md)
- [Skupper NodePort Access Guide](./skupper-nodeport-access-guide.md)
- [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/)
- [NGINX TLS Passthrough](https://kubernetes.github.io/ingress-nginx/user-guide/tls/#ssl-passthrough)
- [Kubernetes IngressClass](https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-class)

Code blocks (26):
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `bash`
- `yaml`
- `unspecified`
- `unspecified`
- `yaml`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `bash`
- `bash`
- `bash`
- `bash`

## `generated/skupper/skupper-nodeport-access-guide.md`

Headings (31):
- # Using NodePort Access for Skupper Sites
- ## Overview
- ### When to Use NodePort
- ### How NodePort Works
- ## Prerequisites
- ## Controller Configuration
- ### Required Environment Variables
- ### Configuration via Deployment YAML
- ### Configuration via Helm Chart
- ### Validation
- ## Using NodePort with Sites
- ### Method 1: Site linkAccess
- ### Method 2: RouterAccess Resource
- ### Method 3: SecuredAccess Resource
- ## Kind-Specific Considerations
- ### The Problem
- ### Solution 1: extraPortMappings (Recommended for Development)
- ### Solution 2: Container Network Routing
- ### Solution 3: Docker Network Sharing
- ## Minikube Considerations
- ## Troubleshooting
- ### Error: "nodeport access type requires cluster-host to be set"
- ### Error: "default access type must be in enabled access types"
- ### Site endpoints not resolving
- ### Remote site cannot connect
- ### Verifying NodePort Configuration
- ## References
- ### Related Documentation
- ### Source Code References
- ### External Resources
- ## Summary

Links (7):
- [Controller Configuration](#controller-configuration)
- [Skupper Site CRD](./skupper-crd-sites-skupper-io.md)
- [Skupper RouterAccess CRD](./skupper-crd-routeraccesses-skupper-io.md)
- [Skupper SecuredAccess CRD](./skupper-crd-securedaccesses-skupper-io.md)
- [Kubernetes NodePort Service](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport)
- [Kind ExtraPortMappings](https://kind.sigs.k8s.io/docs/user/configuration/#extra-port-mappings)
- [Minikube Networking](https://minikube.sigs.k8s.io/docs/handbook/accessing/)

Code blocks (18):
- `yaml`
- `yaml`
- `unspecified`
- `unspecified`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `bash`
- `yaml`
- `bash`
- `bash`
- `yaml`
- `unspecified`
- `unspecified`
- `unspecified`
- `bash`

## `generated/skupper-adoption-bridge/next-steps.md`

Headings (3):
- # Next Steps: Get Started
- ## Appears in
- ## Notes

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-adoption-bridge/protocol-port-requirements.md`

Headings (3):
- # Protocol and Port Requirements (TCP, Stable Ports)
- ## Appears in
- ## Notes

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-adoption-bridge/ready-to-implement.md`

Headings (3):
- # Implementation Readiness Gate
- ## Appears in
- ## Notes

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-adoption-bridge/use-case-alignment.md`

Headings (3):
- # Use Case Alignment
- ## Appears in
- ## Notes

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-ansible/skupper-ansible-module-controller.md`

Headings (6):
- # Skupper Ansible module: controller
- ## Description
- ## Options
- ## Requirements
- ## Examples
- ## Source

Links (0):
- None

Code blocks (1):
- `yaml`

## `generated/skupper-ansible/skupper-ansible-module-resource.md`

Headings (8):
- # Skupper Ansible module: resource
- ## Description
- ## Options
- ## Shared Options
- ## Requirements
- ## Examples
- ## Return Values
- ## Source

Links (0):
- None

Code blocks (2):
- `yaml`
- `yaml`

## `generated/skupper-ansible/skupper-ansible-module-system.md`

Headings (8):
- # Skupper Ansible module: system
- ## Description
- ## Options
- ## Shared Options
- ## Requirements
- ## Examples
- ## Return Values
- ## Source

Links (0):
- None

Code blocks (2):
- `yaml`
- `yaml`

## `generated/skupper-ansible/skupper-ansible-module-token.md`

Headings (8):
- # Skupper Ansible module: token
- ## Description
- ## Options
- ## Shared Options
- ## Requirements
- ## Examples
- ## Return Values
- ## Source

Links (0):
- None

Code blocks (2):
- `yaml`
- `yaml`

## `generated/skupper-ansible/skupper-ansible-overview.md`

Headings (4):
- # Skupper Ansible collection
- ## Module Map
- ## Shared Options
- ## Source

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-ansible/skupper-ansible-systemd-architecture.md`

Headings (57):
- # Skupper Ansible Systemd Architecture
- ## Overview
- ## Architecture Components
- ### 1. Container Image
- ### 2. Systemd Service
- ### 3. Startup Scripts
- ## Installation Flow
- ### 1. Pre-flight Checks
- ### 2. Enable Podman Socket (Podman only)
- ### 3. Create Container
- ### 4. Create Startup Scripts
- ### 5. Create Systemd Service
- ### 6. Enable and Start Service
- ## Uninstallation Flow
- ### 1. Stop and Remove Service
- ### 2. Remove Container
- ### 3. Clean Data Directory
- ## Platform-Specific Behaviors
- ### Podman (Default)
- ### Docker
- ## Directory Layout
- ### Data Directory ()
- ### Service Directory ()
- ### Runtime Directory ()
- ## Systemd Integration Details
- ### Service Lifecycle
- ### Why Not Mount D-Bus?
- ### Service Monitoring
- ### Auto-restart on Failure
- ## Role Separation
- ### CLI Binary: Development and Testing
- ### Ansible Collection: Production and Automation
- ## Reload Types
- ### Manual Reload ()
- ### Auto Reload ()
- ## Security Considerations
- ### SELinux Context
- ### Security Options
- ### User Namespace Isolation
- ### Network Mode
- ## Troubleshooting
- ### Container Exists but Service Doesn't Start
- ### Podman Socket Not Available
- ### Service Starts but Controller Not Running
- ### Docker Group Not Found
- ## Comparison with Other Deployment Methods
- ### vs. Kubernetes Operator
- ### vs. Manual CLI Installation
- ## Future Enhancements
- ### Automatic Restart
- ### Health Checks
- ### Resource Limits
- ### Graceful Updates
- ## Related Documentation
- ## References
- ### Source Code
- ### External Documentation

Links (6):
- [skupper-ansible-module-controller](skupper-ansible-module-controller.md)
- [skupper-ansible-workflow-non-kubernetes](skupper-ansible-workflow-non-kubernetes.md)
- [skupper-ansible-workflow-mixed-sites](skupper-ansible-workflow-mixed-sites.md)
- [Systemd service unit documentation](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
- [Podman systemd integration](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)

Code blocks (35):
- `bash`
- `bash`
- `python`
- `python`
- `bash`
- `unspecified`
- `ini`
- `bash`
- `python`
- `bash`
- `python`
- `python`
- `yaml`
- `yaml`
- `unspecified`
- `unspecified`
- `unspecified`
- `bash`
- `ini`
- `yaml`
- `yaml`
- `yaml`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `yaml`
- `bash`
- `bash`
- `yaml`
- `ini`
- `ini`
- `ini`
- `yaml`

## `generated/skupper-ansible/skupper-ansible-workflow-kubernetes.md`

Headings (4):
- # Skupper Ansible Kubernetes workflow
- ## Flow
- ## Playbook Shape
- ## Source

Links (0):
- None

Code blocks (2):
- `text`
- `yaml`

## `generated/skupper-ansible/skupper-ansible-workflow-mixed-sites.md`

Headings (5):
- # Skupper Ansible mixed Kubernetes and system workflow
- ## West Kubernetes, East Local System
- ## West Local System, East Kubernetes
- ## Notes
- ## Source

Links (0):
- None

Code blocks (2):
- `yaml`
- `yaml`

## `generated/skupper-ansible/skupper-ansible-workflow-non-kubernetes.md`

Headings (4):
- # Skupper Ansible non-Kubernetes workflow
- ## Flow
- ## Notes
- ## Source

Links (0):
- None

Code blocks (1):
- `text`

## `generated/skupper-ansible-examples.md`

Headings (35):
- # Skupper Ansible Examples
- ## Example Categories
- ### Production Examples
- #### Hello World with Ansible
- ### End-to-End Test Scenarios
- #### 1. Hello World Test
- #### 2. Redis Multicloud High Availability Test
- #### 3. Labels and Annotations Test
- #### 4. Service Scale Test
- #### 5. Attached Connector Test
- #### 6. Expose Pods by Name Test
- #### 7. High Availability (HA) Test
- ## Common Ansible Patterns
- ### Pattern 1: Resource Application
- ### Pattern 2: Token Generation and Redemption
- ### Pattern 3: Cross-Host Variable Access
- ### Pattern 4: Conditional Execution by Host
- ### Pattern 5: Non-Kubernetes Platforms
- ## Reusable Roles
- ### 
- ### 
- ### 
- ### 
- ### 
- ### 
- ## Running the Examples
- ### Prerequisites
- ### Running Hello World Example
- ### Running E2E Tests
- ## Key Differences: Production vs. E2E Tests
- ## Best Practices from the Examples
- ## Troubleshooting
- ### Common Issues
- ## Source References
- ## Related Documentation

Links (3):
- [https://galaxy.ansible.com/ui/repo/published/skupper/v2/](https://galaxy.ansible.com/ui/repo/published/skupper/v2/)
- [https://github.com/skupperproject/skupper-ansible](https://github.com/skupperproject/skupper-ansible)
- [https://raw.githubusercontent.com/skupperproject/skupper-ansible/refs/heads/main/requirements.txt](https://raw.githubusercontent.com/skupperproject/skupper-ansible/refs/heads/main/requirements.txt)

Code blocks (19):
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `unspecified`
- `unspecified`
- `unspecified`
- `bash`
- `bash`
- `unspecified`
- `unspecified`

## `generated/skupper-console/console.md`

Headings (57):
- # Skupper Console API Calls
- ## Overview
- ## Base URL
- ## REST API Endpoints
- ### Authentication Endpoints
- #### getUser
- #### logout
- ### Site Endpoints
- #### getAllSites
- #### getSiteById
- ### Router Link Endpoints
- #### getAllLinks
- #### getLinkById
- ### Component Endpoints
- #### getAllComponents
- #### getComponentById
- ### Process Endpoints
- #### getAllProcesses
- #### getProcessById
- ### Service Endpoints
- #### getAllServices
- #### getServiceById
- ### Listener Endpoints
- #### getAllListeners
- ### Connector Endpoints
- #### getAllConnectors
- ### TCP Connection Endpoints
- #### getAllTcpConnections
- #### getTcpConnectionById
- ### HTTP Request Endpoints
- #### getAllHttpRequests
- #### getHttpRequestById
- ### Site Pair Endpoints
- #### getAllSitePairs
- #### getSitePairById
- ### Component Pair Endpoints
- #### getAllComponentPairs
- #### getComponentPairById
- ### Process Pair Endpoints
- #### getAllProcessPairs
- #### getProcessPairById
- #### getProcessPairsByServiceId
- ## REST Resource Mapping
- ## Prometheus Metrics API
- ### Query Types
- ### Metrics Endpoints
- #### Traffic Metrics
- #### HTTP Request Metrics
- #### Latency Metrics
- ## Query Parameters
- ## Data Flow
- ## Authentication
- ## Implementation Details
- ### Client Library
- ### Field Mapping
- ### Error Handling
- ## Related Documentation

Links (2):
- [Skupper Network Observer OpenAPI Spec](skupper-api-network-observer.md)
- [Skupper Console Repository](https://github.com/skupperproject/skupper-console)

Code blocks (1):
- `unspecified`

## `generated/skupper-docs-landscape/acceptance-tests.md`

Headings (5):
- # Acceptance Tests
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Connector status command](../../human/skupper-docs/input/refdog/commands/connector/status.md)
- [Listener status command](../../human/skupper-docs/input/refdog/commands/listener/status.md)
- [Network Observer API concept](../concepts/network-observer-api.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)
- [Refdog listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/access-controls.md`

Headings (5):
- # Administrative Access Controls
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Administer Skupper](./administer-skupper.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Skupper security overview](../../human/skupper-docs/input/overview/security.md)
- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/access-policy.md`

Headings (6):
- # Access Policy
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Secure Skupper](./secure-skupper.md)
- [Role-Based Access Control](./rbac.md)
- [Service Exposure Policy](./service-policy.md)
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md)
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md)
- [human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/administer-skupper.md`

Headings (8):
- # Administer Skupper
- ## Appears in
- ## Topics
- ### Operational Outcomes
- ### Administrative Workflows
- ### Operational State
- ### Governance Controls
- ## Notes

Links (16):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Healthy Application Network](./healthy-network.md)
- [Controlled Administrative Change](./controlled-change.md)
- [Site Operations](./site-operations.md)
- [Link Operations](./link-operations.md)
- [Service Operations](./service-operations.md)
- [Change Workflow](./change-workflow.md)
- [Site Status](./site-status.md)
- [Site Configuration](./site-configuration.md)
- [Link Status](./link-status.md)
- [Link Credentials](./link-credentials.md)
- [Service Status](./service-status.md)
- [Service Configuration](./service-configuration.md)
- [Configuration Backup](./configuration-backup.md)
- [Administrative Access Controls](./access-controls.md)
- [Audit Records](./audit-records.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/application-inventory.md`

Headings (5):
- # Application and Service Inventory
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Connector concept](../concepts/connector.md)
- [Listener concept](../concepts/listener.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Workload concept](../../human/skupper-docs/input/refdog/concepts/workload.md)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)
- [Refdog workload concept](https://skupperproject.github.io/refdog/concepts/workload.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/application-network.md`

Headings (6):
- # Application Network
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Discover Skupper](./discover-skupper.md)
- [Sites](./sites.md)
- [Site Links](./links.md)
- [Network concept](../../human/skupper-docs/input/refdog/concepts/network.md)
- [Skupper overview topic](../../human/skupper-docs/input/refdog/topics/skupper-overview.md)
- [Overview index](../../human/skupper-docs/input/overview/index.md)
- [Existing generated concept](../concepts/network-observer-api.md)
- [Skupper overview](https://skupper.io/docs/overview/index.html)
- [Skupper concepts reference](https://skupper.io/docs/refdog/concepts/network.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/audit-records.md`

Headings (5):
- # Audit Records
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Administer Skupper](./administer-skupper.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Debug dump command](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md)
- [Skupper Ansible resource module](../skupper-ansible/skupper-ansible-module-resource.md)
- [Controlled Administrative Change](./controlled-change.md)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/automated-connectivity.md`

Headings (6):
- # Automated Application Connectivity
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Develop with Skupper](./develop-skupper.md)
- [Declarative Resources](./declarative-resources.md)
- [CI/CD Integration](./pipeline-integration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [generated/skupper-ansible/skupper-ansible-overview.md](../skupper-ansible/skupper-ansible-overview.md)
- [generated/skupper-ansible/skupper-ansible-workflow-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-kubernetes.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/automation-interface.md`

Headings (5):
- # Automation Interface
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Integrate Skupper](./integrate-skupper.md)
- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md)
- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md)
- [generated/skupper-ansible/skupper-ansible-overview.md](../skupper-ansible/skupper-ansible-overview.md)
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md)
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/availability-targets.md`

Headings (5):
- # Availability Targets
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md)
- [Kubernetes site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Kubernetes site configuration with YAML](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Creating a high availability site with the CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Refdog link concept](https://skupperproject.github.io/refdog/concepts/link.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/backend-endpoint.md`

Headings (5):
- # Backend Endpoint
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Configure Skupper](./configure-skupper.md)
- [generated/concepts/connector.md](../concepts/connector.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md)
- [human/skupper-docs/input/refdog/concepts/workload.md](../../human/skupper-docs/input/refdog/concepts/workload.md)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)
- [Connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)
- [Workload concept](https://skupperproject.github.io/refdog/concepts/workload.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/backup-state.md`

Headings (5):
- # Configuration and State Backup
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md)
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md)
- [Debug dump command](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [Debug dumps topic](../../human/skupper-docs/input/refdog/topics/debug-dumps.md)
- [Skupper Ansible system module](../skupper-ansible/skupper-ansible-module-system.md)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Refdog debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/basic-observation.md`

Headings (6):
- # Check Network Status
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Get Started with Skupper](./get-started.md)
- [Create Two Sites](./first-sites.md)
- [Link the Sites](./first-link.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/behavior-changes.md`

Headings (6):
- # Behavior Changes
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [What's New in Skupper](./skupper-whats-new.md)
- [Release Notes](./release-notes.md)
- [Upgrade Notes](./upgrade-notes.md)
- [Release notes](./release-notes.md)
- [Upgrade notes](./upgrade-notes.md)
- [Install and upgrade source](../../human/skupper-docs/input/install/index.md)
- [Troubleshooting source](../../human/skupper-docs/input/troubleshooting/index.md)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper docs](https://skupper.io/docs/)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/capacity-plan.md`

Headings (6):
- # Capacity Plan
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Traffic Flow Requirements](./traffic-flows.md)
- [Availability Targets](./availability-targets.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Kubernetes site configuration with YAML](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md)
- [Network console guide](../../human/skupper-docs/input/console/index.md)
- [Network Observer API concept](../concepts/network-observer-api.md)
- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Skupper YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Skupper network console](https://skupper.io/docs/console/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/capacity-tuning.md`

Headings (6):
- # Capacity Tuning
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Optimize Skupper](./optimize-skupper.md)
- [Traffic Baseline](./traffic-baseline.md)
- [Capacity Headroom Model](./headroom-model.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/certificate-interface.md`

Headings (5):
- # Certificate Interface
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Integrate Skupper](./integrate-skupper.md)
- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md)
- [human/skupper-docs/input/refdog/topics/application-tls.md](../../human/skupper-docs/input/refdog/topics/application-tls.md)
- [human/skupper-docs/input/refdog/topics/system-tls-credentials.md](../../human/skupper-docs/input/refdog/topics/system-tls-credentials.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper/skupper-crd-certificates-skupper-io.md](../skupper/skupper-crd-certificates-skupper-io.md)
- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Application TLS topic](https://skupperproject.github.io/refdog/topics/application-tls.html)
- [System TLS credentials topic](https://skupperproject.github.io/refdog/topics/system-tls-credentials.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/certificate-lifecycle.md`

Headings (6):
- # Certificate Lifecycle
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Secure Skupper](./secure-skupper.md)
- [Certificate Issuance](./issuance.md)
- [Certificate Rotation](./rotation.md)
- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md)
- [human/skupper-docs/input/refdog/resources/access-grant.md](../../human/skupper-docs/input/refdog/resources/access-grant.md)
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md)
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Access grant resource reference](https://skupperproject.github.io/refdog/resources/access-grant.html)
- [Access token resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/change-workflow.md`

Headings (6):
- # Change Workflow
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Administer Skupper](./administer-skupper.md)
- [Configuration Backup](./configuration-backup.md)
- [Audit Records](./audit-records.md)
- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md)
- [Skupper Ansible resource module](../skupper-ansible/skupper-ansible-module-resource.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Debug dump command](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [Controlled Administrative Change](./controlled-change.md)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Refdog debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/cli-automation.md`

Headings (6):
- # CLI Automation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Develop with Skupper](./develop-skupper.md)
- [CLI Command Contract](./cli-contract.md)
- [Exit Codes and Error Handling](./error-handling.md)
- [human/skupper-docs/input/kube-cli/index.md](../../human/skupper-docs/input/kube-cli/index.md)
- [human/skupper-docs/input/system-cli/index.md](../../human/skupper-docs/input/system-cli/index.md)
- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md)
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [Kubernetes CLI workflows](https://skupper.io/docs/kube-cli/index.html)
- [System CLI workflows](https://skupper.io/docs/system-cli/index.html)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/cli-contract.md`

Headings (5):
- # CLI Command Contract
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Develop with Skupper](./develop-skupper.md)
- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md)
- [human/skupper-docs/refdog/config/commands/overview.md](../../human/skupper-docs/refdog/config/commands/overview.md)
- [human/skupper-docs/refdog/config/commands/options.yaml](../../human/skupper-docs/refdog/config/commands/options.yaml)
- [human/skupper-docs/input/refdog/commands/site/index.md](../../human/skupper-docs/input/refdog/commands/site/index.md)
- [human/skupper-docs/input/refdog/commands/link/index.md](../../human/skupper-docs/input/refdog/commands/link/index.md)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Site commands](https://skupperproject.github.io/refdog/commands/site/index.html)
- [Link commands](https://skupperproject.github.io/refdog/commands/link/index.html)
- [Listener commands](https://skupperproject.github.io/refdog/commands/listener/index.html)
- [Connector commands](https://skupperproject.github.io/refdog/commands/connector/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/cli-install.md`

Headings (6):
- # Install the Skupper CLI
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Get Started with Skupper](./get-started.md)
- [Cluster or Host Prerequisites](./starter-prerequisites.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md)
- [Skupper source entry](../../sources/skupper.md)
- [Skupper releases page](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Skupper install script](https://skupper.io/v2/install.sh)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/cli-installation.md`

Headings (6):
- # CLI Installation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Install Skupper](./install-skupper.md)
- [Kubernetes Platform Prerequisites](./platform-prerequisites.md)
- [CLI Package](./cli-package.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Kubernetes CLI overview](../../human/skupper-docs/input/kube-cli/index.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [CLI command overview](../../human/skupper-docs/refdog/config/commands/overview.md)
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper Kubernetes CLI overview](https://skupper.io/docs/kube-cli/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/cli-package.md`

Headings (6):
- # CLI Package
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Install Skupper](./install-skupper.md)
- [Kubernetes Platform Prerequisites](./platform-prerequisites.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md)
- [Skupper source entry](../../sources/skupper.md)
- [Skupper Docs source entry](../../sources/skupper-docs.md)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Skupper install script](https://skupper.io/v2/install.sh)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/cli-reference.md`

Headings (6):
- # CLI Reference
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Skupper Reference](./skupper-reference.md)
- [Command Syntax](./command-syntax.md)
- [Exit Status and Errors](./exit-status.md)
- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md)
- [human/skupper-docs/refdog/config/commands/overview.md](../../human/skupper-docs/refdog/config/commands/overview.md)
- [human/skupper-docs/refdog/config/commands/options.yaml](../../human/skupper-docs/refdog/config/commands/options.yaml)
- [human/skupper-docs/input/refdog/commands/site/index.md](../../human/skupper-docs/input/refdog/commands/site/index.md)
- [human/skupper-docs/input/refdog/commands/debug/index.md](../../human/skupper-docs/input/refdog/commands/debug/index.md)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Site commands](https://skupperproject.github.io/refdog/commands/site/index.html)
- [Link commands](https://skupperproject.github.io/refdog/commands/link/index.html)
- [Debug commands](https://skupperproject.github.io/refdog/commands/debug/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/cloud-network-rules.md`

Headings (5):
- # Cloud Network Rules
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/refdog/resources/router-access.md](../../human/skupper-docs/input/refdog/resources/router-access.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [Kubernetes YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [RouterAccess resource reference](https://skupperproject.github.io/refdog/resources/router-access.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/cluster-pattern.md`

Headings (6):
- # Kubernetes Cluster Pattern
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [Platform Compatibility Profile](./platform-profile.md)
- [Operator or CLI Choice](./operator-or-cli.md)
- [human/skupper-docs/input/kube-cli/index.md](../../human/skupper-docs/input/kube-cli/index.md)
- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md)
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [generated/skupper-ansible/skupper-ansible-workflow-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-kubernetes.md)
- [Kubernetes CLI workflows](https://skupper.io/docs/kube-cli/index.html)
- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/command-syntax.md`

Headings (5):
- # Command Syntax
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Reference](./skupper-reference.md)
- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md)
- [human/skupper-docs/refdog/config/commands/options.yaml](../../human/skupper-docs/refdog/config/commands/options.yaml)
- [human/skupper-docs/refdog/config/commands/site.yaml](../../human/skupper-docs/refdog/config/commands/site.yaml)
- [human/skupper-docs/refdog/config/commands/link.yaml](../../human/skupper-docs/refdog/config/commands/link.yaml)
- [human/skupper-docs/refdog/config/commands/listener.yaml](../../human/skupper-docs/refdog/config/commands/listener.yaml)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Site commands](https://skupperproject.github.io/refdog/commands/site/index.html)
- [Link commands](https://skupperproject.github.io/refdog/commands/link/index.html)
- [Listener commands](https://skupperproject.github.io/refdog/commands/listener/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/compatibility-checks.md`

Headings (6):
- # Compatibility Checks
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Skupper Technology Previews](./skupper-previews.md)
- [Preview Catalog](./preview-catalog.md)
- [Preview catalog](./preview-catalog.md)
- [Compatibility matrix](./compatibility-matrix.md)
- [Install docs](../../human/skupper-docs/input/install/index.md)
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md)
- [Generated platform map](../maps/platforms.md)
- [Skupper install docs](https://skupper.io/docs/install/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/compatibility-matrix.md`

Headings (5):
- # Compatibility Matrix
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (7):
- [What's New in Skupper](./skupper-whats-new.md)
- [Install docs](../../human/skupper-docs/input/install/index.md)
- [Platform concept source](../../human/skupper-docs/refdog/config/concepts/platform.yaml)
- [Platform guides page](./platform-guides.md)
- [Version matrix page](./version-matrix.md)
- [Skupper install docs](https://skupper.io/docs/install/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/compatibility-reference.md`

Headings (6):
- # Compatibility Reference
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Skupper Reference](./skupper-reference.md)
- [Version Matrix](./version-matrix.md)
- [Platform Matrix](./platform-matrix.md)
- [human/skupper-docs/input/install/index.md](../../human/skupper-docs/input/install/index.md)
- [human/skupper-docs/input/refdog/commands/version.md](../../human/skupper-docs/input/refdog/commands/version.md)
- [human/skupper-docs/input/system-cli/index.md](../../human/skupper-docs/input/system-cli/index.md)
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md)
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md)
- [Installation](https://skupper.io/docs/install/index.html)
- [Version command](https://skupperproject.github.io/refdog/commands/version.html)
- [System CLI workflows](https://skupper.io/docs/system-cli/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/compatibility-review.md`

Headings (6):
- # Compatibility Review
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Version Compatibility](./version-compatibility.md)
- [Release Differences](./release-differences.md)
- [Release Notes](./release-notes.md)
- [Compatibility Matrix](./compatibility-matrix.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md)
- [Skupper releases source](../../sources/skupper.md)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Refdog version command](https://skupperproject.github.io/refdog/commands/version.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/component-upgrades.md`

Headings (6):
- # CLI, Operator, and Router Upgrades
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Site Upgrade Sequence](./upgrade-sequence.md)
- [Configuration and State Backup](./backup-state.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [System install command](../../human/skupper-docs/input/refdog/commands/system/install.md)
- [System reload command](../../human/skupper-docs/input/refdog/commands/system/reload.md)
- [Skupper Ansible controller module](../skupper-ansible/skupper-ansible-module-controller.md)
- [Skupper Ansible system module](../skupper-ansible/skupper-ansible-module-system.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Refdog system install command](https://skupperproject.github.io/refdog/commands/system/install.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/configuration-as-code.md`

Headings (6):
- # Configuration as Code
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Develop with Skupper](./develop-skupper.md)
- [Declarative Resources](./declarative-resources.md)
- [Version Control](./version-control.md)
- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md)
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md)
- [human/skupper-docs/input/kube-yaml/custom-labels.md](../../human/skupper-docs/input/kube-yaml/custom-labels.md)
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md)
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md)
- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [Custom labels with YAML](https://skupper.io/docs/kube-yaml/custom-labels.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/configuration-backup.md`

Headings (5):
- # Configuration Backup
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Administer Skupper](./administer-skupper.md)
- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md)
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md)
- [Debug dump command](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Skupper Ansible system module](../skupper-ansible/skupper-ansible-module-system.md)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Refdog debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/configuration-reference.md`

Headings (6):
- # Configuration Reference
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Skupper Reference](./skupper-reference.md)
- [Default Values](./defaults.md)
- [Validation Constraints](./constraints.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/system-yaml/site-configuration.md](../../human/skupper-docs/input/system-yaml/site-configuration.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [human/skupper-docs/input/refdog/topics/resource-settings.md](../../human/skupper-docs/input/refdog/topics/resource-settings.md)
- [Kubernetes YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Kubernetes YAML service exposure](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [System YAML site configuration](https://skupper.io/docs/system-yaml/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/configure-skupper.md`

Headings (7):
- # Configure Skupper
- ## Appears in
- ## Topics
- ### Configured Behavior
- ### Configuration Resources
- ### Configuration Inputs
- ## Notes

Links (15):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Configured Service Connectivity](./service-connectivity.md)
- [Configured Site Behavior](./site-behavior.md)
- [Site Configuration](./site-config.md)
- [Listener Configuration](./listener-config.md)
- [Connector Configuration](./connector-config.md)
- [Service Routing Configuration](./service-routing.md)
- [Runtime Settings](./runtime-settings.md)
- [Site Identity Settings](./site-identity-config.md)
- [Namespace Scope](./namespace-scope.md)
- [Service Address](./service-address.md)
- [Backend Endpoint](./backend-endpoint.md)
- [Routing Mode](./routing-mode.md)
- [Resource Limits](./resource-limits.md)
- [Logging Settings](./logging-settings.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/connector-config.md`

Headings (6):
- # Connector Configuration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Configure Skupper](./configure-skupper.md)
- [Backend Endpoint](./backend-endpoint.md)
- [generated/concepts/connector.md](../concepts/connector.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md)
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)
- [Connector command reference](https://skupperproject.github.io/refdog/commands/connector/create.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Attached connector resource reference](https://skupperproject.github.io/refdog/resources/attached-connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/constraints.md`

Headings (5):
- # Validation Constraints
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Reference](./skupper-reference.md)
- [generated/skupper/skupper-crd-sites-skupper-io.md](../skupper/skupper-crd-sites-skupper-io.md)
- [generated/skupper/skupper-crd-listeners-skupper-io.md](../skupper/skupper-crd-listeners-skupper-io.md)
- [generated/skupper/skupper-crd-connectors-skupper-io.md](../skupper/skupper-crd-connectors-skupper-io.md)
- [human/skupper-docs/refdog/scripts/validate_crds_vs_yaml.py](../../human/skupper-docs/refdog/scripts/validate_crds_vs_yaml.py)
- [human/skupper-docs/refdog/scripts/validate_yaml_vs_clidoc.py](../../human/skupper-docs/refdog/scripts/validate_yaml_vs_clidoc.py)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/controlled-change.md`

Headings (6):
- # Controlled Administrative Change
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Administer Skupper](./administer-skupper.md)
- [Change Workflow](./change-workflow.md)
- [Administrative Access Controls](./access-controls.md)
- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md)
- [Skupper Ansible resource module](../skupper-ansible/skupper-ansible-module-resource.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Configuration Backup](./configuration-backup.md)
- [Audit Records](./audit-records.md)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/corrective-actions.md`

Headings (6):
- # Corrective Actions
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [Root Cause Record](./root-cause-record.md)
- [Monitoring Improvements](./monitoring-improvements.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-docs-landscape/root-cause-record.md](./root-cause-record.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper project](https://skupper.io/)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/cutover.md`

Headings (6):
- # Traffic Cutover
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Parallel Run](./parallel-run.md)
- [Rollback Path](./rollback-path.md)
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md)
- [Routing key concept](../concepts/routing-key.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/dashboards.md`

Headings (6):
- # Dashboards and Alerts
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Observe Skupper](./observe-skupper.md)
- [Metrics Export](./metrics-export.md)
- [Log Collection](./log-collection.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [sources/skupper-console.md](../../sources/skupper-console.md)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Prometheus](https://prometheus.io/)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/declarative-resources.md`

Headings (6):
- # Declarative Resources
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Develop with Skupper](./develop-skupper.md)
- [Resource Schemas](./resource-schema.md)
- [Reference Examples](./examples.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md)
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/defaults.md`

Headings (5):
- # Default Values
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Reference](./skupper-reference.md)
- [human/skupper-docs/refdog/config/commands/options.yaml](../../human/skupper-docs/refdog/config/commands/options.yaml)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/delivery-integration.md`

Headings (6):
- # CI/CD Integration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Integrate Skupper](./integrate-skupper.md)
- [Automation Interface](./automation-interface.md)
- [Secrets Interface](./secrets-interface.md)
- [generated/skupper-ansible/skupper-ansible-overview.md](../skupper-ansible/skupper-ansible-overview.md)
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md)
- [generated/skupper-ansible/skupper-ansible-module-token.md](../skupper-ansible/skupper-ansible-module-token.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/deprecations.md`

Headings (6):
- # Deprecations
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (8):
- [What's New in Skupper](./skupper-whats-new.md)
- [Release Notes](./release-notes.md)
- [Release notes](./release-notes.md)
- [Command reference source](../../human/skupper-docs/refdog/config/commands/overview.md)
- [Resource reference source](../../human/skupper-docs/refdog/config/resources/overview.md)
- [Generated API reference](../skupper/skupper-api-network-observer.md)
- [Skupper docs reference](https://skupper.io/docs/refdog/)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/develop-skupper.md`

Headings (7):
- # Develop with Skupper
- ## Appears in
- ## Topics
- ### Developer Outcomes
- ### Development Interfaces
- ### Developer Foundations
- ## Notes

Links (14):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Automated Application Connectivity](./automated-connectivity.md)
- [Repeatable Skupper Environments](./repeatable-environments.md)
- [Declarative Resources](./declarative-resources.md)
- [CLI Automation](./cli-automation.md)
- [CI/CD Integration](./pipeline-integration.md)
- [Configuration as Code](./configuration-as-code.md)
- [Resource Schemas](./resource-schema.md)
- [Reference Examples](./examples.md)
- [CLI Command Contract](./cli-contract.md)
- [Exit Codes and Error Handling](./error-handling.md)
- [Secrets Injection](./secrets-injection.md)
- [Version Control](./version-control.md)
- [Integration Test Harness](./test-harness.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/discover-skupper.md`

Headings (7):
- # Discover Skupper
- ## Appears in
- ## Topics
- ### User Value
- ### Core Concepts
- ### Foundations
- ## Notes

Links (10):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Connect Applications Across Sites](./multi-site-connectivity.md)
- [Keep Services Private](./private-connectivity.md)
- [Application Network](./application-network.md)
- [Service Exposure](./service-exposure.md)
- [Secure Links](./secure-links.md)
- [Sites](./sites.md)
- [Site Links](./links.md)
- [Service Routing](./routing.md)
- [Certificates and Identity](./identity-model.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/dual-connectivity.md`

Headings (6):
- # Dual Connectivity Plan
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Source Deployment Assessment](./source-assessment.md)
- [Target Deployment Design](./target-design.md)
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md)
- [Routing key concept](../concepts/routing-key.md)
- [Network Observer API concept](../concepts/network-observer-api.md)
- [Skupper Ansible mixed Kubernetes and system workflow](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Refdog routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)
- [Skupper network console](https://skupper.io/docs/console/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/efficient-operation.md`

Headings (6):
- # Efficient Resource Use
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Optimize Skupper](./optimize-skupper.md)
- [Runtime Resource Tuning](./resource-tuning.md)
- [Traffic Shaping](./traffic-shaping.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Network console](https://skupper.io/docs/console/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/error-handling.md`

Headings (5):
- # Exit Codes and Error Handling
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Develop with Skupper](./develop-skupper.md)
- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md)
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md)
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/event-codes.md`

Headings (5):
- # Event and Diagnostic Codes
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Reference](./skupper-reference.md)
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md)
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/event-collection.md`

Headings (5):
- # Event Collection
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Observe Skupper](./observe-skupper.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/skupper-docs-landscape/event-codes.md](./event-codes.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/event-stream.md`

Headings (6):
- # Events
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Observe Skupper](./observe-skupper.md)
- [Event Collection](./event-collection.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md)
- [generated/skupper-docs-landscape/event-codes.md](./event-codes.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/evidence-bundle.md`

Headings (5):
- # Logs, Events, Metrics, and Configuration
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/examples.md`

Headings (5):
- # Reference Examples
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Develop with Skupper](./develop-skupper.md)
- [generated/workflows/skupper-examples.md](../workflows/skupper-examples.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/topics/service-exposure.md](../../human/skupper-docs/input/refdog/topics/service-exposure.md)
- [human/skupper-docs/input/refdog/topics/site-linking.md](../../human/skupper-docs/input/refdog/topics/site-linking.md)
- [Skupper examples organization](https://github.com/skupperproject)
- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Service exposure topic](https://skupperproject.github.io/refdog/topics/service-exposure.html)
- [Site linking topic](https://skupperproject.github.io/refdog/topics/site-linking.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/exit-status.md`

Headings (5):
- # Exit Status and Errors
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Reference](./skupper-reference.md)
- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md)
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md)
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/extend-skupper.md`

Headings (7):
- # Extend a Skupper Application Network
- ## Appears in
- ## Topics
- ### Expansion Outcomes
- ### Expansion Workflow
- ### Expansion Controls
- ## Notes

Links (12):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [New Site Connected](./new-site-connected.md)
- [New Service Reachable](./new-service-reachable.md)
- [Onboard a Site](./site-onboarding.md)
- [Establish a Link](./link-establishment.md)
- [Onboard a Service](./service-onboarding.md)
- [Site Configuration Template](./site-template.md)
- [Site Identity](./site-identity.md)
- [Link Credential or Token](./link-token.md)
- [Network Policy](./network-policy.md)
- [Service Definition](./service-definition.md)
- [Routing Policy](./routing-policy.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/fault-isolation.md`

Headings (6):
- # Fault Isolation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [Symptom Capture](./symptom-capture.md)
- [Site, Link, Route, and Service Checks](./layered-checks.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md)
- [generated/concepts/listener.md](../concepts/listener.md)
- [generated/concepts/connector.md](../concepts/connector.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)
- [Listener command reference](https://skupperproject.github.io/refdog/commands/listener/status.html)
- [Connector command reference](https://skupperproject.github.io/refdog/commands/connector/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/feedback-loop.md`

Headings (6):
- # Feedback and Issue Reporting
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Skupper Technology Previews](./skupper-previews.md)
- [Sandbox Trial](./sandbox-trial.md)
- [Known Issues](./known-issues.md)
- [Sandbox trial](./sandbox-trial.md)
- [Known issues](./known-issues.md)
- [Debug dump command](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [Troubleshooting docs](../../human/skupper-docs/input/troubleshooting/index.md)
- [Skupper GitHub issues](https://github.com/skupperproject/skupper/issues)
- [Skupper discussions](https://github.com/skupperproject/skupper/discussions)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/firewall-rules.md`

Headings (5):
- # Firewall Rules
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Secure Skupper](./secure-skupper.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/refdog/resources/router-access.md](../../human/skupper-docs/input/refdog/resources/router-access.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [Site configuration with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [RouterAccess resource reference](https://skupperproject.github.io/refdog/resources/router-access.html)
- [Network console](https://skupper.io/docs/console/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/first-connected-service.md`

Headings (6):
- # Connected Service Across Sites
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Get Started with Skupper](./get-started.md)
- [Create Two Sites](./first-sites.md)
- [Link the Sites](./first-link.md)
- [Expose a Service](./first-exposure.md)
- [Kubernetes CLI overview](../../human/skupper-docs/input/kube-cli/index.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Skupper Kubernetes CLI overview](https://skupper.io/docs/kube-cli/index.html)
- [Skupper Hello World example](https://github.com/skupperproject/skupper-example-hello-world)
- [Skupper examples](https://skupper.io/examples/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/first-exposure.md`

Headings (6):
- # Expose a Service
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Get Started with Skupper](./get-started.md)
- [Create Two Sites](./first-sites.md)
- [Choose a Test Service](./service-selection.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Connector create command](../../human/skupper-docs/input/refdog/commands/connector/create.md)
- [Listener create command](../../human/skupper-docs/input/refdog/commands/listener/create.md)
- [Connector concept](../../human/skupper-docs/input/refdog/concepts/connector.md)
- [Listener concept](../../human/skupper-docs/input/refdog/concepts/listener.md)
- [Exposing services with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector create command](https://skupperproject.github.io/refdog/commands/connector/create.html)
- [Refdog listener create command](https://skupperproject.github.io/refdog/commands/listener/create.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/first-link.md`

Headings (6):
- # Link the Sites
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Get Started with Skupper](./get-started.md)
- [Create Two Sites](./first-sites.md)
- [Link Credentials](./link-credentials.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Token issue command](../../human/skupper-docs/input/refdog/commands/token/issue.md)
- [Token redeem command](../../human/skupper-docs/input/refdog/commands/token/redeem.md)
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog token issue command](https://skupperproject.github.io/refdog/commands/token/issue.html)
- [Refdog token redeem command](https://skupperproject.github.io/refdog/commands/token/redeem.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/first-sites.md`

Headings (6):
- # Create Two Sites
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Get Started with Skupper](./get-started.md)
- [Cluster or Host Prerequisites](./starter-prerequisites.md)
- [Install the Skupper CLI](./cli-install.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Site create command](../../human/skupper-docs/input/refdog/commands/site/create.md)
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Refdog site create command](https://skupperproject.github.io/refdog/commands/site/create.html)
- [Refdog site concept](https://skupperproject.github.io/refdog/concepts/site.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/first-validation.md`

Headings (6):
- # Connectivity Validation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Get Started with Skupper](./get-started.md)
- [Connected Service Across Sites](./first-connected-service.md)
- [Check Network Status](./basic-observation.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Skupper site linking guide](https://skupper.io/docs/kube-cli/site-linking.html)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog link status command](https://skupperproject.github.io/refdog/commands/link/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/flow-metrics.md`

Headings (6):
- # Flow Metrics
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Observe Skupper](./observe-skupper.md)
- [Metrics Export](./metrics-export.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper repository](https://github.com/skupperproject/skupper)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/get-started.md`

Headings (7):
- # Get Started with Skupper
- ## Appears in
- ## Topics
- ### First Working Network
- ### Starter Workflow
- ### Starter Setup
- ## Notes

Links (11):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Connected Service Across Sites](./first-connected-service.md)
- [Connectivity Validation](./first-validation.md)
- [Create Two Sites](./first-sites.md)
- [Link the Sites](./first-link.md)
- [Expose a Service](./first-exposure.md)
- [Check Network Status](./basic-observation.md)
- [Cluster or Host Prerequisites](./starter-prerequisites.md)
- [Install the Skupper CLI](./cli-install.md)
- [Generate Link Credentials](./link-credentials.md)
- [Choose a Test Service](./service-selection.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/getting-started-guide.md`

Headings (4):
- # Getting Started Guide
- ## Appears in
- ## Dependencies
- ## Notes

Links (3):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)
- [Guide Source Content](./guide-source.md)
- [Release Version Metadata](./release-version.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/glossary.md`

Headings (5):
- # Glossary
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Skupper Reference](./skupper-reference.md)
- [human/skupper-docs/input/refdog/concepts/index.md](../../human/skupper-docs/input/refdog/concepts/index.md)
- [human/skupper-docs/input/refdog/concepts/site.md](../../human/skupper-docs/input/refdog/concepts/site.md)
- [human/skupper-docs/input/refdog/concepts/link.md](../../human/skupper-docs/input/refdog/concepts/link.md)
- [human/skupper-docs/input/refdog/concepts/listener.md](../../human/skupper-docs/input/refdog/concepts/listener.md)
- [human/skupper-docs/input/refdog/concepts/connector.md](../../human/skupper-docs/input/refdog/concepts/connector.md)
- [Concepts reference](https://skupperproject.github.io/refdog/concepts/index.html)
- [Site concept](https://skupperproject.github.io/refdog/concepts/site.html)
- [Link concept](https://skupperproject.github.io/refdog/concepts/link.html)
- [Listener concept](https://skupperproject.github.io/refdog/concepts/listener.html)
- [Connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/guide-source.md`

Headings (3):
- # Guide Source Content
- ## Appears in
- ## Notes

Links (1):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/headroom-model.md`

Headings (5):
- # Capacity Headroom Model
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Optimize Skupper](./optimize-skupper.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [human/skupper-docs/input/refdog/topics/large-networks.md](../../human/skupper-docs/input/refdog/topics/large-networks.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Large networks topic](https://skupperproject.github.io/refdog/topics/large-networks.html)
- [Network console](https://skupper.io/docs/console/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/health-checks.md`

Headings (6):
- # Post-install Health Checks
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Install Skupper](./install-skupper.md)
- [Site Initialization](./site-initialization.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [Debug check command](../../human/skupper-docs/input/refdog/commands/debug/check.md)
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Refdog debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/healthy-network.md`

Headings (6):
- # Healthy Application Network
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Administer Skupper](./administer-skupper.md)
- [Site Operations](./site-operations.md)
- [Link Operations](./link-operations.md)
- [Service Operations](./service-operations.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Network Observer API concept](../concepts/network-observer-api.md)
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Refdog link status command](https://skupperproject.github.io/refdog/commands/link/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/host-identity.md`

Headings (5):
- # Host Identity
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Integrate Skupper](./integrate-skupper.md)
- [human/skupper-docs/input/system-cli/site-configuration.md](../../human/skupper-docs/input/system-cli/site-configuration.md)
- [human/skupper-docs/input/system-cli/site-linking.md](../../human/skupper-docs/input/system-cli/site-linking.md)
- [human/skupper-docs/input/refdog/topics/system-namespaces.md](../../human/skupper-docs/input/refdog/topics/system-namespaces.md)
- [human/skupper-docs/input/refdog/topics/system-tls-credentials.md](../../human/skupper-docs/input/refdog/topics/system-tls-credentials.md)
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md)
- [System site configuration](https://skupper.io/docs/system-cli/site-configuration.html)
- [System site linking](https://skupper.io/docs/system-cli/site-linking.html)
- [System namespaces topic](https://skupperproject.github.io/refdog/topics/system-namespaces.html)
- [System TLS credentials topic](https://skupperproject.github.io/refdog/topics/system-tls-credentials.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/host-installation.md`

Headings (6):
- # Host Installation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Install Skupper](./install-skupper.md)
- [Linux Host Prerequisites](./host-prerequisites.md)
- [Host Package](./host-package.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [System install command](../../human/skupper-docs/input/refdog/commands/system/install.md)
- [CLI command overview](../../human/skupper-docs/refdog/config/commands/overview.md)
- [System namespaces topic](../../human/skupper-docs/input/refdog/topics/system-namespaces.md)
- [Skupper Ansible non-Kubernetes workflow](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Refdog system install command](https://skupperproject.github.io/refdog/commands/system/install.html)
- [Refdog command reference](https://skupperproject.github.io/refdog/commands/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/host-integration.md`

Headings (6):
- # Linux Host Integration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Integrate Skupper](./integrate-skupper.md)
- [Host Service Binding](./host-service-binding.md)
- [Host Identity](./host-identity.md)
- [human/skupper-docs/input/system-cli/site-configuration.md](../../human/skupper-docs/input/system-cli/site-configuration.md)
- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md)
- [human/skupper-docs/input/system-yaml/site-configuration.md](../../human/skupper-docs/input/system-yaml/site-configuration.md)
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md)
- [generated/skupper-ansible/skupper-ansible-workflow-non-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md)
- [System site configuration](https://skupper.io/docs/system-cli/site-configuration.html)
- [System service exposure](https://skupper.io/docs/system-cli/service-exposure.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/host-package.md`

Headings (6):
- # Host Package
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Install Skupper](./install-skupper.md)
- [Linux Host Prerequisites](./host-prerequisites.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [System install command](../../human/skupper-docs/input/refdog/commands/system/install.md)
- [CLI command overview](../../human/skupper-docs/refdog/config/commands/overview.md)
- [Skupper Ansible controller module](../skupper-ansible/skupper-ansible-module-controller.md)
- [Skupper source entry](../../sources/skupper.md)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Refdog system install command](https://skupperproject.github.io/refdog/commands/system/install.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/host-pattern.md`

Headings (6):
- # Linux Host Pattern
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [Host Compatibility Profile](./host-profile.md)
- [System Service Configuration](./system-service.md)
- [human/skupper-docs/input/system-cli/index.md](../../human/skupper-docs/input/system-cli/index.md)
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md)
- [human/skupper-docs/input/refdog/topics/system-namespaces.md](../../human/skupper-docs/input/refdog/topics/system-namespaces.md)
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md)
- [generated/skupper-ansible/skupper-ansible-workflow-non-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md)
- [System CLI workflows](https://skupper.io/docs/system-cli/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [System namespaces topic](https://skupperproject.github.io/refdog/topics/system-namespaces.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/host-prerequisites.md`

Headings (5):
- # Linux Host Prerequisites
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Install Skupper](./install-skupper.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [System install command](../../human/skupper-docs/input/refdog/commands/system/install.md)
- [CLI command overview](../../human/skupper-docs/refdog/config/commands/overview.md)
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md)
- [Skupper Ansible non-Kubernetes workflow](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Refdog system install command](https://skupperproject.github.io/refdog/commands/system/install.html)
- [Refdog platform concept](https://skupperproject.github.io/refdog/concepts/platform.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/host-profile.md`

Headings (5):
- # Host Compatibility Profile
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [human/skupper-docs/input/system-cli/index.md](../../human/skupper-docs/input/system-cli/index.md)
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md)
- [human/skupper-docs/input/refdog/topics/system-namespaces.md](../../human/skupper-docs/input/refdog/topics/system-namespaces.md)
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md)
- [generated/skupper-ansible/skupper-ansible-module-controller.md](../skupper-ansible/skupper-ansible-module-controller.md)
- [System CLI workflows](https://skupper.io/docs/system-cli/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [System namespaces topic](https://skupperproject.github.io/refdog/topics/system-namespaces.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/host-service-binding.md`

Headings (5):
- # Host Service Binding
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Integrate Skupper](./integrate-skupper.md)
- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md)
- [human/skupper-docs/input/system-yaml/service-exposure.md](../../human/skupper-docs/input/system-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md)
- [generated/skupper/skupper-crd-connectors-skupper-io.md](../skupper/skupper-crd-connectors-skupper-io.md)
- [generated/skupper-ansible/skupper-ansible-workflow-non-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md)
- [System service exposure](https://skupper.io/docs/system-cli/service-exposure.html)
- [System YAML service exposure](https://skupper.io/docs/system-yaml/service-exposure.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/hybrid-environment.md`

Headings (6):
- # Hybrid Environment Connectivity
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (13):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [Kubernetes Cluster Pattern](./cluster-pattern.md)
- [Linux Host Pattern](./host-pattern.md)
- [Firewall and Egress Controls](./network-controls.md)
- [generated/skupper-ansible/skupper-ansible-workflow-mixed-sites.md](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/system-cli/site-linking.md](../../human/skupper-docs/input/system-cli/site-linking.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/refdog/topics/site-linking.md](../../human/skupper-docs/input/refdog/topics/site-linking.md)
- [Kubernetes site linking](https://skupper.io/docs/kube-cli/site-linking.html)
- [System site linking](https://skupper.io/docs/system-cli/site-linking.html)
- [Site linking topic](https://skupperproject.github.io/refdog/topics/site-linking.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/identity-model.md`

Headings (5):
- # Certificates and Identity
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (8):
- [Discover Skupper](./discover-skupper.md)
- [Security overview](../../human/skupper-docs/input/overview/security.md)
- [Router TLS topic](../../human/skupper-docs/input/refdog/topics/router-tls.md)
- [Application TLS topic](../../human/skupper-docs/input/refdog/topics/application-tls.md)
- [System TLS credentials topic](../../human/skupper-docs/input/refdog/topics/system-tls-credentials.md)
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md)
- [Security overview](https://skupper.io/docs/overview/security.html)
- [Access token concept reference](https://skupper.io/docs/refdog/concepts/access-token.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/identity-policy.md`

Headings (5):
- # Identity and Certificate Policy
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Skupper security overview](../../human/skupper-docs/input/overview/security.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md)
- [Token issue command](../../human/skupper-docs/input/refdog/commands/token/issue.md)
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md)
- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Refdog token issue command](https://skupperproject.github.io/refdog/commands/token/issue.html)
- [Refdog access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/index.md`

Headings (3):
- # Skupper Documentation Landscape
- ## Maps
- ## All Pages

Links (289):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [What's New in Skupper](./skupper-whats-new.md)
- [Discover Skupper](./discover-skupper.md)
- [Skupper Technology Previews](./skupper-previews.md)
- [Get Started with Skupper](./get-started.md)
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Install Skupper](./install-skupper.md)
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Upgrade Skupper](./upgrade-skupper.md)
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Administer Skupper](./administer-skupper.md)
- [Configure Skupper](./configure-skupper.md)
- [Secure Skupper](./secure-skupper.md)
- [Observe Skupper](./observe-skupper.md)
- [Optimize Skupper](./optimize-skupper.md)
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [Develop with Skupper](./develop-skupper.md)
- [Integrate Skupper](./integrate-skupper.md)
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [Skupper Reference](./skupper-reference.md)
- [Skupper Downloadable Guides](./skupper-pdf-library.md)
- [Acceptance Tests](./acceptance-tests.md)
- [Administrative Access Controls](./access-controls.md)
- [Access Policy](./access-policy.md)
- [Administer Skupper](./administer-skupper.md)
- [Application and Service Inventory](./application-inventory.md)
- [Application Network](./application-network.md)
- [Audit Records](./audit-records.md)
- [Automated Application Connectivity](./automated-connectivity.md)
- [Automation Interface](./automation-interface.md)
- [Availability Targets](./availability-targets.md)
- [Backend Endpoint](./backend-endpoint.md)
- [Configuration and State Backup](./backup-state.md)
- [Check Network Status](./basic-observation.md)
- [Behavior Changes](./behavior-changes.md)
- [Capacity Plan](./capacity-plan.md)
- [Capacity Tuning](./capacity-tuning.md)
- [Certificate Interface](./certificate-interface.md)
- [Certificate Lifecycle](./certificate-lifecycle.md)
- [Change Workflow](./change-workflow.md)
- [CLI Automation](./cli-automation.md)
- [CLI Command Contract](./cli-contract.md)
- [Install the Skupper CLI](./cli-install.md)
- [CLI Installation](./cli-installation.md)
- [CLI Package](./cli-package.md)
- [CLI Reference](./cli-reference.md)
- [Cloud Network Rules](./cloud-network-rules.md)
- [Kubernetes Cluster Pattern](./cluster-pattern.md)
- [Command Syntax](./command-syntax.md)
- [Compatibility Checks](./compatibility-checks.md)
- [Compatibility Matrix](./compatibility-matrix.md)
- [Compatibility Reference](./compatibility-reference.md)
- [Compatibility Review](./compatibility-review.md)
- [CLI, Operator, and Router Upgrades](./component-upgrades.md)
- [Configuration as Code](./configuration-as-code.md)
- [Configuration Backup](./configuration-backup.md)
- [Configuration Reference](./configuration-reference.md)
- [Configure Skupper](./configure-skupper.md)
- [Connector Configuration](./connector-config.md)
- [Validation Constraints](./constraints.md)
- [Controlled Administrative Change](./controlled-change.md)
- [Corrective Actions](./corrective-actions.md)
- [Traffic Cutover](./cutover.md)
- [Dashboards and Alerts](./dashboards.md)
- [Declarative Resources](./declarative-resources.md)
- [Default Values](./defaults.md)
- [CI/CD Integration](./delivery-integration.md)
- [Deprecations](./deprecations.md)
- [Develop with Skupper](./develop-skupper.md)
- [Discover Skupper](./discover-skupper.md)
- [Dual Connectivity Plan](./dual-connectivity.md)
- [Efficient Resource Use](./efficient-operation.md)
- [Exit Codes and Error Handling](./error-handling.md)
- [Event and Diagnostic Codes](./event-codes.md)
- [Event Collection](./event-collection.md)
- [Events](./event-stream.md)
- [Logs, Events, Metrics, and Configuration](./evidence-bundle.md)
- [Reference Examples](./examples.md)
- [Exit Status and Errors](./exit-status.md)
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Fault Isolation](./fault-isolation.md)
- [Feedback and Issue Reporting](./feedback-loop.md)
- [Firewall Rules](./firewall-rules.md)
- [Connected Service Across Sites](./first-connected-service.md)
- [Expose a Service](./first-exposure.md)
- [Link the Sites](./first-link.md)
- [Create Two Sites](./first-sites.md)
- [Connectivity Validation](./first-validation.md)
- [Flow Metrics](./flow-metrics.md)
- [Get Started with Skupper](./get-started.md)
- [Getting Started Guide](./getting-started-guide.md)
- [Glossary](./glossary.md)
- [Guide Source Content](./guide-source.md)
- [Capacity Headroom Model](./headroom-model.md)
- [Post-install Health Checks](./health-checks.md)
- [Healthy Application Network](./healthy-network.md)
- [Host Identity](./host-identity.md)
- [Host Installation](./host-installation.md)
- [Linux Host Integration](./host-integration.md)
- [Host Package](./host-package.md)
- [Linux Host Pattern](./host-pattern.md)
- [Linux Host Prerequisites](./host-prerequisites.md)
- [Host Compatibility Profile](./host-profile.md)
- [Host Service Binding](./host-service-binding.md)
- [Hybrid Environment Connectivity](./hybrid-environment.md)
- [Certificates and Identity](./identity-model.md)
- [Identity and Certificate Policy](./identity-policy.md)
- [Install Skupper](./install-skupper.md)
- [Select Installation Method](./installation-method.md)
- [Installation Pattern](./installation-pattern.md)
- [Operational Skupper Site](./installed-site.md)
- [Integrate Skupper](./integrate-skupper.md)
- [Certificate Issuance](./issuance.md)
- [Known Issues](./known-issues.md)
- [Known Limitations](./known-limitations.md)
- [Kubernetes Integration](./kubernetes-integration.md)
- [Site, Link, Route, and Service Checks](./layered-checks.md)
- [Least-Privilege Application Network](./least-privilege-network.md)
- [Link and Cross-reference Check](./link-check.md)
- [Link Credentials](./link-credentials.md)
- [Establish a Link](./link-establishment.md)
- [Link Metrics](./link-metrics.md)
- [Link Operations](./link-operations.md)
- [Link Status](./link-status.md)
- [Link Credential or Token](./link-token.md)
- [Site Links](./links.md)
- [Listener Configuration](./listener-config.md)
- [Load Tests](./load-tests.md)
- [Log Collection](./log-collection.md)
- [Logging Interface](./logging-interface.md)
- [Logging Settings](./logging-settings.md)
- [Maintenance and Communication Plan](./maintenance-plan.md)
- [Managed Kubernetes Pattern](./managed-platform-pattern.md)
- [Metrics Export](./metrics-export.md)
- [Metrics Interface](./metrics-interface.md)
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Migrated Application Connectivity](./migrated-connectivity.md)
- [Migration Acceptance](./migration-acceptance.md)
- [Migration Waves](./migration-wave.md)
- [Mixed Platform Pattern](./mixed-platform-pattern.md)
- [Monitoring Improvements](./monitoring-improvements.md)
- [Connect Applications Across Sites](./multi-site-connectivity.md)
- [Mutual Authentication](./mutual-authentication.md)
- [Namespace Controls](./namespace-controls.md)
- [Namespace Scope](./namespace-scope.md)
- [Network Console](./network-console.md)
- [Firewall and Egress Controls](./network-controls.md)
- [Network Health View](./network-health-view.md)
- [Network Isolation](./network-isolation.md)
- [Network Policy](./network-policy.md)
- [New Capabilities](./new-capabilities.md)
- [New Service Reachable](./new-service-reachable.md)
- [New Site Connected](./new-site-connected.md)
- [Observability Integration](./observability-integration.md)
- [Observe Skupper](./observe-skupper.md)
- [Operational Toolchain Integration](./operational-integration.md)
- [Operations Guide](./operations-guide.md)
- [Operator Installation](./operator-installation.md)
- [Operator or CLI Choice](./operator-or-cli.md)
- [Operator Package](./operator-package.md)
- [Optimize Skupper](./optimize-skupper.md)
- [Operational Ownership](./ownership-model.md)
- [Parallel Run](./parallel-run.md)
- [Path Selection Data](./path-selection.md)
- [PDF Build](./pdf-build.md)
- [Met Performance Targets](./performance-targets.md)
- [CI/CD Integration](./pipeline-integration.md)
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Platform-to-Platform Connectivity](./platform-connectivity.md)
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [Platform Matrix](./platform-matrix.md)
- [Kubernetes Platform Prerequisites](./platform-prerequisites.md)
- [Platform Compatibility Profile](./platform-profile.md)
- [Policy Interface](./policy-interface.md)
- [Post-upgrade Test Suite](./post-upgrade-tests.md)
- [Prevented Recurrence](./prevented-recurrence.md)
- [Preview Catalog](./preview-catalog.md)
- [Preview Evaluation](./preview-evaluation.md)
- [Preview Fit Assessment](./preview-fit.md)
- [Preview Installation](./preview-installation.md)
- [Preview Status](./preview-status.md)
- [Candidate Use Cases](./preview-use-cases.md)
- [Keep Services Private](./private-connectivity.md)
- [PDF Quality Review](./quality-review.md)
- [Rate Controls](./rate-controls.md)
- [Role-Based Access Control](./rbac.md)
- [Recovery Procedure](./recovery-procedure.md)
- [Reference Guide](./reference-guide.md)
- [Reference Source Content](./reference-source.md)
- [Release Differences](./release-differences.md)
- [Release Notes](./release-notes.md)
- [Release Publication](./release-publish.md)
- [Release Version Metadata](./release-version.md)
- [Remediation](./remediation.md)
- [Repeatable Skupper Environments](./repeatable-environments.md)
- [Resource Automation Interface](./resource-automation.md)
- [Resource Fields](./resource-fields.md)
- [Resource Limits](./resource-limits.md)
- [CPU and Memory Profile](./resource-profile.md)
- [Resource Reference](./resource-reference.md)
- [Resource Schemas](./resource-schema.md)
- [Resource Status](./resource-status.md)
- [Runtime Resource Tuning](./resource-tuning.md)
- [Restored Connectivity](./restored-connectivity.md)
- [Rollout Risk Assessment](./risk-assessment.md)
- [Rollback Path](./rollback-path.md)
- [Rollback Plan](./rollback-plan.md)
- [Rollout Plan](./rollout-plan.md)
- [Root Cause Record](./root-cause-record.md)
- [Certificate Rotation](./rotation.md)
- [Service Routing](./routing.md)
- [Routing Mode](./routing-mode.md)
- [Routing Policy](./routing-policy.md)
- [Routing Tuning](./routing-tuning.md)
- [Runtime Logs](./runtime-logs.md)
- [Runtime Settings](./runtime-settings.md)
- [Sandbox Trial](./sandbox-trial.md)
- [Secrets Injection](./secrets-injection.md)
- [Secrets Interface](./secrets-interface.md)
- [Secure Links](./secure-links.md)
- [Secure Skupper](./secure-skupper.md)
- [Security Guide](./security-guide.md)
- [Security Tooling Integration](./security-integration.md)
- [Security Requirements](./security-requirements.md)
- [Service Address](./service-address.md)
- [Service Configuration](./service-configuration.md)
- [Configured Service Connectivity](./service-connectivity.md)
- [Service Definition](./service-definition.md)
- [Service Discovery Interface](./service-discovery.md)
- [Service Exposure](./service-exposure.md)
- [Service Metrics](./service-metrics.md)
- [Onboard a Service](./service-onboarding.md)
- [Service Operations](./service-operations.md)
- [Service Exposure Policy](./service-policy.md)
- [Service Priorities](./service-priorities.md)
- [Service Routing Configuration](./service-routing.md)
- [Choose a Test Service](./service-selection.md)
- [Service Status](./service-status.md)
- [Configured Site Behavior](./site-behavior.md)
- [Site Certificates](./site-certificates.md)
- [Site Configuration](./site-config.md)
- [Site Configuration](./site-configuration.md)
- [Site Identity](./site-identity.md)
- [Site Identity Settings](./site-identity-config.md)
- [Site Initialization](./site-initialization.md)
- [Cluster and Host Inventory](./site-inventory.md)
- [Site Metrics](./site-metrics.md)
- [Onboard a Site](./site-onboarding.md)
- [Site Operations](./site-operations.md)
- [Site Status](./site-status.md)
- [Site Configuration Template](./site-template.md)
- [Sites](./sites.md)
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Skupper Downloadable Guides](./skupper-pdf-library.md)
- [Skupper Technology Previews](./skupper-previews.md)
- [Skupper Reference](./skupper-reference.md)
- [What's New in Skupper](./skupper-whats-new.md)
- [Source Deployment Assessment](./source-assessment.md)
- [Cluster or Host Prerequisites](./starter-prerequisites.md)
- [Status and Condition Reference](./status-reference.md)
- [Support Boundaries](./support-boundaries.md)
- [Supported Platform Deployment](./supported-deployment.md)
- [Symptom Capture](./symptom-capture.md)
- [System Service Configuration](./system-service.md)
- [Target Deployment Design](./target-design.md)
- [Target Application Network Topology](./target-topology.md)
- [Integration Test Harness](./test-harness.md)
- [Validation Test Plan](./test-plan.md)
- [Topology Analysis](./topology-analysis.md)
- [Trace Context](./trace-context.md)
- [Trace Correlation](./trace-correlation.md)
- [Traffic Baseline](./traffic-baseline.md)
- [Traffic Flow Requirements](./traffic-flows.md)
- [Traffic Insight](./traffic-insight.md)
- [Traffic Shaping](./traffic-shaping.md)
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [Trust Boundaries](./trust-boundaries.md)
- [Trust Bundle](./trust-bundle.md)
- [Trusted Site Connectivity](./trusted-connectivity.md)
- [Upgrade Decisions](./upgrade-decisions.md)
- [Upgrade Notes](./upgrade-notes.md)
- [Site Upgrade Sequence](./upgrade-sequence.md)
- [Upgrade Skupper](./upgrade-skupper.md)
- [Upgrade Validation](./upgrade-validation.md)
- [Upgraded Application Network](./upgraded-network.md)
- [Validated Installation](./validated-install.md)
- [Version Compatibility](./version-compatibility.md)
- [Version Control](./version-control.md)
- [Version Matrix](./version-matrix.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/install-skupper.md`

Headings (7):
- # Install Skupper
- ## Appears in
- ## Topics
- ### Installed Environment
- ### Installation Methods
- ### Prerequisites and Validation
- ## Notes

Links (14):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Operational Skupper Site](./installed-site.md)
- [Validated Installation](./validated-install.md)
- [CLI Installation](./cli-installation.md)
- [Operator Installation](./operator-installation.md)
- [Host Installation](./host-installation.md)
- [Select Installation Method](./installation-method.md)
- [Kubernetes Platform Prerequisites](./platform-prerequisites.md)
- [Linux Host Prerequisites](./host-prerequisites.md)
- [CLI Package](./cli-package.md)
- [Operator Package](./operator-package.md)
- [Host Package](./host-package.md)
- [Site Initialization](./site-initialization.md)
- [Post-install Health Checks](./health-checks.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/installation-method.md`

Headings (6):
- # Select Installation Method
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Install Skupper](./install-skupper.md)
- [CLI Installation](./cli-installation.md)
- [Operator Installation](./operator-installation.md)
- [Host Installation](./host-installation.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md)
- [Kubernetes CLI overview](../../human/skupper-docs/input/kube-cli/index.md)
- [Skupper resources overview](../../human/skupper-docs/input/refdog/resources/index.md)
- [Skupper Ansible overview](../skupper-ansible/skupper-ansible-overview.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Refdog platform concept](https://skupperproject.github.io/refdog/concepts/platform.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/installation-pattern.md`

Headings (6):
- # Installation Pattern
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [Platform Compatibility Profile](./platform-profile.md)
- [human/skupper-docs/input/install/index.md](../../human/skupper-docs/input/install/index.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/system-cli/site-configuration.md](../../human/skupper-docs/input/system-cli/site-configuration.md)
- [human/skupper-docs/input/refdog/commands/system/install.md](../../human/skupper-docs/input/refdog/commands/system/install.md)
- [human/skupper-docs/input/refdog/commands/site/create.md](../../human/skupper-docs/input/refdog/commands/site/create.md)
- [Installation](https://skupper.io/docs/install/index.html)
- [Kubernetes CLI site configuration](https://skupper.io/docs/kube-cli/site-configuration.html)
- [System CLI site configuration](https://skupper.io/docs/system-cli/site-configuration.html)
- [System install command](https://skupperproject.github.io/refdog/commands/system/install.html)
- [Site create command](https://skupperproject.github.io/refdog/commands/site/create.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/installed-site.md`

Headings (6):
- # Operational Skupper Site
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Install Skupper](./install-skupper.md)
- [Select Installation Method](./installation-method.md)
- [Site Initialization](./site-initialization.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Site create command](../../human/skupper-docs/input/refdog/commands/site/create.md)
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [Skupper resources overview](../../human/skupper-docs/input/refdog/resources/index.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/integrate-skupper.md`

Headings (8):
- # Integrate Skupper
- ## Appears in
- ## Topics
- ### Integration Outcomes
- ### Integration Patterns
- ### Platform Interfaces
- ### Operations Interfaces
- ## Notes

Links (18):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Platform-to-Platform Connectivity](./platform-connectivity.md)
- [Operational Toolchain Integration](./operational-integration.md)
- [Kubernetes Integration](./kubernetes-integration.md)
- [Linux Host Integration](./host-integration.md)
- [Observability Integration](./observability-integration.md)
- [Security Tooling Integration](./security-integration.md)
- [CI/CD Integration](./delivery-integration.md)
- [Service Discovery Interface](./service-discovery.md)
- [Resource Automation Interface](./resource-automation.md)
- [Host Service Binding](./host-service-binding.md)
- [Host Identity](./host-identity.md)
- [Metrics Interface](./metrics-interface.md)
- [Logging Interface](./logging-interface.md)
- [Certificate Interface](./certificate-interface.md)
- [Policy Interface](./policy-interface.md)
- [Automation Interface](./automation-interface.md)
- [Secrets Interface](./secrets-interface.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/issuance.md`

Headings (5):
- # Certificate Issuance
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Secure Skupper](./secure-skupper.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [human/skupper-docs/input/refdog/resources/access-grant.md](../../human/skupper-docs/input/refdog/resources/access-grant.md)
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md)
- [generated/skupper-ansible/skupper-ansible-module-token.md](../skupper-ansible/skupper-ansible-module-token.md)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [AccessGrant resource reference](https://skupperproject.github.io/refdog/resources/access-grant.html)
- [AccessToken resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/known-issues.md`

Headings (6):
- # Known Issues
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (8):
- [Skupper Technology Previews](./skupper-previews.md)
- [Preview Catalog](./preview-catalog.md)
- [Preview catalog](./preview-catalog.md)
- [Known limitations](./known-limitations.md)
- [Troubleshooting docs](../../human/skupper-docs/input/troubleshooting/index.md)
- [Debug dump command](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [Skupper GitHub issues](https://github.com/skupperproject/skupper/issues)
- [Skupper GitHub discussions](https://github.com/skupperproject/skupper/discussions)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/known-limitations.md`

Headings (6):
- # Known Limitations
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (8):
- [What's New in Skupper](./skupper-whats-new.md)
- [Release Notes](./release-notes.md)
- [Release notes](./release-notes.md)
- [Troubleshooting docs](../../human/skupper-docs/input/troubleshooting/index.md)
- [Debug dumps topic](../../human/skupper-docs/input/refdog/topics/debug-dumps.md)
- [Generated router notes](../skupper-router/)
- [Skupper docs](https://skupper.io/docs/)
- [GitHub issues](https://github.com/skupperproject/skupper/issues)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/kubernetes-integration.md`

Headings (6):
- # Kubernetes Integration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Integrate Skupper](./integrate-skupper.md)
- [Service Discovery Interface](./service-discovery.md)
- [Resource Automation Interface](./resource-automation.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md)
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md)
- [generated/skupper-ansible/skupper-ansible-workflow-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-kubernetes.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/layered-checks.md`

Headings (5):
- # Site, Link, Route, and Service Checks
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/commands/site/status.md](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [human/skupper-docs/input/refdog/commands/link/status.md](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [human/skupper-docs/input/refdog/commands/listener/status.md](../../human/skupper-docs/input/refdog/commands/listener/status.md)
- [human/skupper-docs/input/refdog/commands/connector/status.md](../../human/skupper-docs/input/refdog/commands/connector/status.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Link status command](https://skupperproject.github.io/refdog/commands/link/status.html)
- [Listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)
- [Connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/least-privilege-network.md`

Headings (6):
- # Least-Privilege Application Network
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Secure Skupper](./secure-skupper.md)
- [Access Policy](./access-policy.md)
- [Network Isolation](./network-isolation.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md)
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md)
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md)
- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/link-check.md`

Headings (3):
- # Link and Cross-reference Check
- ## Appears in
- ## Notes

Links (1):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/link-credentials.md`

Headings (5):
- # Link Credentials
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Get Started with Skupper](./get-started.md)
- [Administer Skupper](./administer-skupper.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Token issue command](../../human/skupper-docs/input/refdog/commands/token/issue.md)
- [Token redeem command](../../human/skupper-docs/input/refdog/commands/token/redeem.md)
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md)
- [AccessToken resource](../../human/skupper-docs/input/refdog/resources/access-token.md)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog token issue command](https://skupperproject.github.io/refdog/commands/token/issue.html)
- [Refdog access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/link-establishment.md`

Headings (6):
- # Establish a Link
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Link Credential or Token](./link-token.md)
- [Network Policy](./network-policy.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Token issue command](../../human/skupper-docs/input/refdog/commands/token/issue.md)
- [Token redeem command](../../human/skupper-docs/input/refdog/commands/token/redeem.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog link concept](https://skupperproject.github.io/refdog/concepts/link.html)
- [Refdog token issue command](https://skupperproject.github.io/refdog/commands/token/issue.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/link-metrics.md`

Headings (6):
- # Link Metrics
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Observe Skupper](./observe-skupper.md)
- [Metrics Export](./metrics-export.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/refdog/commands/link/status.md](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Link status command](https://skupperproject.github.io/refdog/commands/link/status.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Network console](https://skupper.io/docs/console/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/link-operations.md`

Headings (6):
- # Link Operations
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Administer Skupper](./administer-skupper.md)
- [Link Status](./link-status.md)
- [Link Credentials](./link-credentials.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog link status command](https://skupperproject.github.io/refdog/commands/link/status.html)
- [Refdog link concept](https://skupperproject.github.io/refdog/concepts/link.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/link-status.md`

Headings (5):
- # Link Status
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Administer Skupper](./administer-skupper.md)
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Refdog link status command](https://skupperproject.github.io/refdog/commands/link/status.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/link-token.md`

Headings (6):
- # Link Credential or Token
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Site Identity](./site-identity.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Token issue command](../../human/skupper-docs/input/refdog/commands/token/issue.md)
- [Token redeem command](../../human/skupper-docs/input/refdog/commands/token/redeem.md)
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog token issue command](https://skupperproject.github.io/refdog/commands/token/issue.html)
- [Refdog access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/links.md`

Headings (6):
- # Site Links
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (8):
- [Discover Skupper](./discover-skupper.md)
- [Sites](./sites.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Site linking topic](../../human/skupper-docs/input/refdog/topics/site-linking.md)
- [Link command reference config](../../human/skupper-docs/refdog/config/commands/link.yaml)
- [Link resource reference](../../human/skupper-docs/input/refdog/resources/link.md)
- [Link concept reference](https://skupper.io/docs/refdog/concepts/link.html)
- [Link command reference](https://skupper.io/docs/refdog/commands/link/)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/listener-config.md`

Headings (6):
- # Listener Configuration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Configure Skupper](./configure-skupper.md)
- [Service Address](./service-address.md)
- [generated/concepts/listener.md](../concepts/listener.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md)
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Listener command reference](https://skupperproject.github.io/refdog/commands/listener/create.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Service exposure with CLI](https://skupper.io/docs/kube-cli/service-exposure.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/load-tests.md`

Headings (5):
- # Load Tests
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Optimize Skupper](./optimize-skupper.md)
- [generated/workflows/skupper-examples.md](../workflows/skupper-examples.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Skupper examples repository](https://github.com/skupperproject/skupper-example-hello-world)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/log-collection.md`

Headings (5):
- # Log Collection
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Observe Skupper](./observe-skupper.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-docs-landscape/logging-interface.md](./logging-interface.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/logging-interface.md`

Headings (5):
- # Logging Interface
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Integrate Skupper](./integrate-skupper.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/skupper-docs-landscape/runtime-logs.md](./runtime-logs.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/logging-settings.md`

Headings (5):
- # Logging Settings
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Configure Skupper](./configure-skupper.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/topics/debug-dumps.md](../../human/skupper-docs/input/refdog/topics/debug-dumps.md)
- [human/skupper-docs/input/refdog/commands/debug/index.md](../../human/skupper-docs/input/refdog/commands/debug/index.md)
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug dump topic](https://skupperproject.github.io/refdog/topics/debug-dumps.html)
- [Debug command reference](https://skupperproject.github.io/refdog/commands/debug/index.html)
- [Console configuration](https://skupper.io/docs/console/configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/maintenance-plan.md`

Headings (5):
- # Maintenance and Communication Plan
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Operational Ownership](./ownership-model.md)
- [Post-upgrade Test Suite](./post-upgrade-tests.md)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/managed-platform-pattern.md`

Headings (6):
- # Managed Kubernetes Pattern
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [Platform Compatibility Profile](./platform-profile.md)
- [Cloud Network Rules](./cloud-network-rules.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [human/skupper-docs/input/refdog/resources/router-access.md](../../human/skupper-docs/input/refdog/resources/router-access.md)
- [Kubernetes YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Kubernetes CLI site configuration](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [RouterAccess resource reference](https://skupperproject.github.io/refdog/resources/router-access.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/metrics-export.md`

Headings (5):
- # Metrics Export
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Observe Skupper](./observe-skupper.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [sources/skupper-console.md](../../sources/skupper-console.md)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Prometheus](https://prometheus.io/)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/metrics-interface.md`

Headings (5):
- # Metrics Interface
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Integrate Skupper](./integrate-skupper.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md)
- [generated/skupper-docs-landscape/metrics-export.md](./metrics-export.md)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Prometheus](https://prometheus.io/)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/migrate-skupper.md`

Headings (7):
- # Migrate to or Between Skupper Deployments
- ## Appears in
- ## Topics
- ### Migration Outcome
- ### Migration Execution
- ### Migration Readiness
- ## Notes

Links (11):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Migrated Application Connectivity](./migrated-connectivity.md)
- [Migration Acceptance](./migration-acceptance.md)
- [Migration Waves](./migration-wave.md)
- [Parallel Run](./parallel-run.md)
- [Traffic Cutover](./cutover.md)
- [Source Deployment Assessment](./source-assessment.md)
- [Target Deployment Design](./target-design.md)
- [Dual Connectivity Plan](./dual-connectivity.md)
- [Rollback Path](./rollback-path.md)
- [Acceptance Tests](./acceptance-tests.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/migrated-connectivity.md`

Headings (6):
- # Migrated Application Connectivity
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Migration Waves](./migration-wave.md)
- [Traffic Cutover](./cutover.md)
- [Migrating from Skupper v1](../../human/skupper-docs/input/overview/migrating.md)
- [Skupper connectivity overview](../../human/skupper-docs/input/overview/connectivity.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Migrating from Skupper v1](https://skupper.io/docs/overview/migrating.html)
- [Skupper connectivity overview](https://skupper.io/docs/overview/connectivity.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/migration-acceptance.md`

Headings (6):
- # Migration Acceptance
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Migrated Application Connectivity](./migrated-connectivity.md)
- [Acceptance Tests](./acceptance-tests.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Network Observer API concept](../concepts/network-observer-api.md)
- [Migrating from Skupper v1](../../human/skupper-docs/input/overview/migrating.md)
- [Acceptance Tests](./acceptance-tests.md)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Migrating from Skupper v1](https://skupper.io/docs/overview/migrating.html)
- [Skupper examples](https://skupper.io/examples/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/migration-wave.md`

Headings (6):
- # Migration Waves
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Source Deployment Assessment](./source-assessment.md)
- [Target Deployment Design](./target-design.md)
- [Migrating from Skupper v1](../../human/skupper-docs/input/overview/migrating.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Target Application Network Topology](./target-topology.md)
- [Application and Service Inventory](./application-inventory.md)
- [Rollout Plan](./rollout-plan.md)
- [Migrating from Skupper v1](https://skupper.io/docs/overview/migrating.html)
- [Skupper connectivity overview](https://skupper.io/docs/overview/connectivity.html)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/mixed-platform-pattern.md`

Headings (6):
- # Mixed Platform Pattern
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [Kubernetes Cluster Pattern](./cluster-pattern.md)
- [Linux Host Pattern](./host-pattern.md)
- [generated/skupper-ansible/skupper-ansible-workflow-mixed-sites.md](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/system-cli/site-linking.md](../../human/skupper-docs/input/system-cli/site-linking.md)
- [human/skupper-docs/input/system-yaml/service-exposure.md](../../human/skupper-docs/input/system-yaml/service-exposure.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [Kubernetes site linking](https://skupper.io/docs/kube-cli/site-linking.html)
- [System site linking](https://skupper.io/docs/system-cli/site-linking.html)
- [Kubernetes service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [System service exposure with YAML](https://skupper.io/docs/system-yaml/service-exposure.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/monitoring-improvements.md`

Headings (5):
- # Monitoring Improvements
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-docs-landscape/dashboards.md](./dashboards.md)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Prometheus](https://prometheus.io/)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/multi-site-connectivity.md`

Headings (6):
- # Connect Applications Across Sites
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Discover Skupper](./discover-skupper.md)
- [Application Network](./application-network.md)
- [Service Exposure](./service-exposure.md)
- [Skupper overview](../../human/skupper-docs/input/overview/index.md)
- [Connectivity overview](../../human/skupper-docs/input/overview/connectivity.md)
- [Application network concept](./application-network.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Skupper overview](https://skupper.io/docs/overview/index.html)
- [Skupper examples on GitHub](https://github.com/skupperproject/skupper-example-hello-world)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/mutual-authentication.md`

Headings (6):
- # Mutual Authentication
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Secure Skupper](./secure-skupper.md)
- [Site Certificates](./site-certificates.md)
- [Trust Bundle](./trust-bundle.md)
- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md)
- [human/skupper-docs/input/refdog/concepts/access-token.md](../../human/skupper-docs/input/refdog/concepts/access-token.md)
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md)
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Access token resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/namespace-controls.md`

Headings (5):
- # Namespace Controls
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Secure Skupper](./secure-skupper.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/topics/attached-connectors.md](../../human/skupper-docs/input/refdog/topics/attached-connectors.md)
- [human/skupper-docs/input/refdog/resources/attached-connector.md](../../human/skupper-docs/input/refdog/resources/attached-connector.md)
- [Site configuration with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Attached connectors topic](https://skupperproject.github.io/refdog/topics/attached-connectors.html)
- [AttachedConnector resource reference](https://skupperproject.github.io/refdog/resources/attached-connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/namespace-scope.md`

Headings (5):
- # Namespace Scope
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Configure Skupper](./configure-skupper.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [generated/concepts/connector.md](../concepts/connector.md)
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Attached connector resource reference](https://skupperproject.github.io/refdog/resources/attached-connector.html)
- [Connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/network-console.md`

Headings (6):
- # Network Console
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Observe Skupper](./observe-skupper.md)
- [Metrics Export](./metrics-export.md)
- [Event Collection](./event-collection.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [sources/skupper-console.md](../../sources/skupper-console.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper project](https://skupper.io/)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/network-controls.md`

Headings (5):
- # Firewall and Egress Controls
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/system-cli/site-linking.md](../../human/skupper-docs/input/system-cli/site-linking.md)
- [human/skupper-docs/input/refdog/resources/router-access.md](../../human/skupper-docs/input/refdog/resources/router-access.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [Kubernetes site linking](https://skupper.io/docs/kube-cli/site-linking.html)
- [System site linking](https://skupper.io/docs/system-cli/site-linking.html)
- [RouterAccess resource reference](https://skupperproject.github.io/refdog/resources/router-access.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/network-health-view.md`

Headings (6):
- # Network Health View
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (13):
- [Observe Skupper](./observe-skupper.md)
- [Site Metrics](./site-metrics.md)
- [Link Metrics](./link-metrics.md)
- [Service Metrics](./service-metrics.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/network-isolation.md`

Headings (6):
- # Network Isolation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Secure Skupper](./secure-skupper.md)
- [Namespace Controls](./namespace-controls.md)
- [Firewall Rules](./firewall-rules.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [Site configuration with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Network console](https://skupper.io/docs/console/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/network-policy.md`

Headings (5):
- # Network Policy
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper connectivity overview](../../human/skupper-docs/input/overview/connectivity.md)
- [Skupper security overview](../../human/skupper-docs/input/overview/security.md)
- [Link resource](../../human/skupper-docs/input/refdog/resources/link.md)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Skupper connectivity overview](https://skupper.io/docs/overview/connectivity.html)
- [Skupper security overview](https://skupper.io/docs/overview/security.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/new-capabilities.md`

Headings (6):
- # New Capabilities
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [What's New in Skupper](./skupper-whats-new.md)
- [Release Notes](./release-notes.md)
- [Compatibility Matrix](./compatibility-matrix.md)
- [Skupper release artifacts](https://github.com/skupperproject/skupper/releases)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Skupper Console guide](../../human/skupper-docs/input/console/index.md)
- [Generated Skupper API notes](../skupper/skupper-api-network-observer.md)
- [Skupper releases](https://skupper.io/releases/index.html)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/new-service-reachable.md`

Headings (6):
- # New Service Reachable
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [New Site Connected](./new-site-connected.md)
- [Onboard a Service](./service-onboarding.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Connector concept](../concepts/connector.md)
- [Listener concept](../concepts/listener.md)
- [Routing key concept](../concepts/routing-key.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)
- [Refdog listener concept](https://skupperproject.github.io/refdog/concepts/listener.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/new-site-connected.md`

Headings (6):
- # New Site Connected
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Onboard a Site](./site-onboarding.md)
- [Establish a Link](./link-establishment.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog site concept](https://skupperproject.github.io/refdog/concepts/site.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/observability-integration.md`

Headings (6):
- # Observability Integration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Integrate Skupper](./integrate-skupper.md)
- [Metrics Interface](./metrics-interface.md)
- [Logging Interface](./logging-interface.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/observe-skupper.md`

Headings (7):
- # Observe Skupper
- ## Appears in
- ## Topics
- ### Operational Visibility
- ### Observability Signals
- ### Collection and Presentation
- ## Notes

Links (16):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Network Health View](./network-health-view.md)
- [Traffic Insight](./traffic-insight.md)
- [Site Metrics](./site-metrics.md)
- [Link Metrics](./link-metrics.md)
- [Service Metrics](./service-metrics.md)
- [Flow Metrics](./flow-metrics.md)
- [Events](./event-stream.md)
- [Runtime Logs](./runtime-logs.md)
- [Trace Correlation](./trace-correlation.md)
- [Metrics Export](./metrics-export.md)
- [Event Collection](./event-collection.md)
- [Log Collection](./log-collection.md)
- [Trace Context](./trace-context.md)
- [Network Console](./network-console.md)
- [Dashboards and Alerts](./dashboards.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/operational-integration.md`

Headings (6):
- # Operational Toolchain Integration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (13):
- [Integrate Skupper](./integrate-skupper.md)
- [Observability Integration](./observability-integration.md)
- [Security Tooling Integration](./security-integration.md)
- [CI/CD Integration](./delivery-integration.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-ansible/skupper-ansible-overview.md](../skupper-ansible/skupper-ansible-overview.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/operations-guide.md`

Headings (4):
- # Operations Guide
- ## Appears in
- ## Dependencies
- ## Notes

Links (3):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)
- [Guide Source Content](./guide-source.md)
- [Release Version Metadata](./release-version.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/operator-installation.md`

Headings (6):
- # Operator Installation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Install Skupper](./install-skupper.md)
- [Kubernetes Platform Prerequisites](./platform-prerequisites.md)
- [Operator Package](./operator-package.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Skupper resources overview](../../human/skupper-docs/input/refdog/resources/index.md)
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md)
- [Controller configuration topic](../../human/skupper-docs/input/refdog/topics/controller-configuration.md)
- [Skupper source entry](../../sources/skupper.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub repository](https://github.com/skupperproject/skupper)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/operator-or-cli.md`

Headings (5):
- # Operator or CLI Choice
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [human/skupper-docs/input/install/index.md](../../human/skupper-docs/input/install/index.md)
- [human/skupper-docs/input/kube-cli/index.md](../../human/skupper-docs/input/kube-cli/index.md)
- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md)
- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md)
- [generated/skupper-ansible/skupper-ansible-overview.md](../skupper-ansible/skupper-ansible-overview.md)
- [Installation](https://skupper.io/docs/install/index.html)
- [Kubernetes CLI workflows](https://skupper.io/docs/kube-cli/index.html)
- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/operator-package.md`

Headings (6):
- # Operator Package
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Install Skupper](./install-skupper.md)
- [Kubernetes Platform Prerequisites](./platform-prerequisites.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Skupper source entry](../../sources/skupper.md)
- [Skupper releases](../../sources/skupper.md)
- [Controller configuration topic](../../human/skupper-docs/input/refdog/topics/controller-configuration.md)
- [Skupper resources overview](../../human/skupper-docs/input/refdog/resources/index.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Skupper GitHub repository](https://github.com/skupperproject/skupper)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/optimize-skupper.md`

Headings (8):
- # Optimize Skupper
- ## Appears in
- ## Topics
- ### Optimization Outcomes
- ### Optimization Levers
- ### Analysis Inputs
- ### Validation Inputs
- ## Notes

Links (15):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Met Performance Targets](./performance-targets.md)
- [Efficient Resource Use](./efficient-operation.md)
- [Routing Tuning](./routing-tuning.md)
- [Capacity Tuning](./capacity-tuning.md)
- [Runtime Resource Tuning](./resource-tuning.md)
- [Traffic Shaping](./traffic-shaping.md)
- [Topology Analysis](./topology-analysis.md)
- [Path Selection Data](./path-selection.md)
- [Traffic Baseline](./traffic-baseline.md)
- [Capacity Headroom Model](./headroom-model.md)
- [CPU and Memory Profile](./resource-profile.md)
- [Load Tests](./load-tests.md)
- [Service Priorities](./service-priorities.md)
- [Rate Controls](./rate-controls.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/ownership-model.md`

Headings (5):
- # Operational Ownership
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md)
- [Network console guide](../../human/skupper-docs/input/console/index.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Skupper network console](https://skupper.io/docs/console/index.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/parallel-run.md`

Headings (6):
- # Parallel Run
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Migration Waves](./migration-wave.md)
- [Dual Connectivity Plan](./dual-connectivity.md)
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md)
- [Routing key concept](../concepts/routing-key.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Network Observer API concept](../concepts/network-observer-api.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Refdog routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/path-selection.md`

Headings (5):
- # Path Selection Data
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Optimize Skupper](./optimize-skupper.md)
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md)
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [MultiKeyListener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Network console](https://skupper.io/docs/console/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/pdf-build.md`

Headings (4):
- # PDF Build
- ## Appears in
- ## Dependencies
- ## Notes

Links (3):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)
- [Guide Source Content](./guide-source.md)
- [Reference Source Content](./reference-source.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/performance-targets.md`

Headings (6):
- # Met Performance Targets
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Optimize Skupper](./optimize-skupper.md)
- [Routing Tuning](./routing-tuning.md)
- [Capacity Tuning](./capacity-tuning.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md)
- [human/skupper-docs/input/refdog/topics/large-networks.md](../../human/skupper-docs/input/refdog/topics/large-networks.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Large networks topic](https://skupperproject.github.io/refdog/topics/large-networks.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/pipeline-integration.md`

Headings (6):
- # CI/CD Integration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Develop with Skupper](./develop-skupper.md)
- [CLI Automation](./cli-automation.md)
- [Secrets Injection](./secrets-injection.md)
- [generated/skupper-ansible/skupper-ansible-workflow-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-kubernetes.md)
- [generated/skupper-ansible/skupper-ansible-workflow-non-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md)
- [generated/skupper-ansible/skupper-ansible-module-token.md](../skupper-ansible/skupper-ansible-module-token.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/plan-skupper.md`

Headings (7):
- # Plan a Skupper Deployment
- ## Appears in
- ## Topics
- ### Deployment Design
- ### Requirements and Constraints
- ### Planning Inputs
- ## Notes

Links (13):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Target Application Network Topology](./target-topology.md)
- [Rollout Plan](./rollout-plan.md)
- [Traffic Flow Requirements](./traffic-flows.md)
- [Security Requirements](./security-requirements.md)
- [Capacity Plan](./capacity-plan.md)
- [Application and Service Inventory](./application-inventory.md)
- [Cluster and Host Inventory](./site-inventory.md)
- [Trust Boundaries](./trust-boundaries.md)
- [Identity and Certificate Policy](./identity-policy.md)
- [Availability Targets](./availability-targets.md)
- [Operational Ownership](./ownership-model.md)
- [Rollout Risk Assessment](./risk-assessment.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/platform-connectivity.md`

Headings (6):
- # Platform-to-Platform Connectivity
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Integrate Skupper](./integrate-skupper.md)
- [Kubernetes Integration](./kubernetes-integration.md)
- [Linux Host Integration](./host-integration.md)
- [generated/skupper-ansible/skupper-ansible-workflow-mixed-sites.md](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/system-cli/site-linking.md](../../human/skupper-docs/input/system-cli/site-linking.md)
- [human/skupper-docs/input/refdog/topics/site-linking.md](../../human/skupper-docs/input/refdog/topics/site-linking.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [System site linking](https://skupper.io/docs/system-cli/site-linking.html)
- [Site linking topic](https://skupperproject.github.io/refdog/topics/site-linking.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/platform-guides.md`

Headings (7):
- # Skupper Platform and Managed-Environment Guides
- ## Appears in
- ## Topics
- ### Platform Outcomes
- ### Platform Patterns
- ### Platform Inputs
- ## Notes

Links (14):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Supported Platform Deployment](./supported-deployment.md)
- [Hybrid Environment Connectivity](./hybrid-environment.md)
- [Kubernetes Cluster Pattern](./cluster-pattern.md)
- [Managed Kubernetes Pattern](./managed-platform-pattern.md)
- [Linux Host Pattern](./host-pattern.md)
- [Mixed Platform Pattern](./mixed-platform-pattern.md)
- [Platform Compatibility Profile](./platform-profile.md)
- [Host Compatibility Profile](./host-profile.md)
- [Installation Pattern](./installation-pattern.md)
- [Operator or CLI Choice](./operator-or-cli.md)
- [Cloud Network Rules](./cloud-network-rules.md)
- [System Service Configuration](./system-service.md)
- [Firewall and Egress Controls](./network-controls.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/platform-matrix.md`

Headings (5):
- # Platform Matrix
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Reference](./skupper-reference.md)
- [human/skupper-docs/input/kube-cli/index.md](../../human/skupper-docs/input/kube-cli/index.md)
- [human/skupper-docs/input/system-cli/index.md](../../human/skupper-docs/input/system-cli/index.md)
- [human/skupper-docs/input/refdog/concepts/platform.md](../../human/skupper-docs/input/refdog/concepts/platform.md)
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md)
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md)
- [Kubernetes CLI workflows](https://skupper.io/docs/kube-cli/index.html)
- [System CLI workflows](https://skupper.io/docs/system-cli/index.html)
- [Platform concept](https://skupperproject.github.io/refdog/concepts/platform.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/platform-prerequisites.md`

Headings (5):
- # Kubernetes Platform Prerequisites
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Install Skupper](./install-skupper.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md)
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md)
- [Controller configuration topic](../../human/skupper-docs/input/refdog/topics/controller-configuration.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/platform-profile.md`

Headings (5):
- # Platform Compatibility Profile
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [human/skupper-docs/input/install/index.md](../../human/skupper-docs/input/install/index.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Installation](https://skupper.io/docs/install/index.html)
- [Kubernetes CLI site configuration](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Kubernetes YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/policy-interface.md`

Headings (5):
- # Policy Interface
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Integrate Skupper](./integrate-skupper.md)
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml)
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md)
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/post-upgrade-tests.md`

Headings (5):
- # Post-upgrade Test Suite
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [Connector status command](../../human/skupper-docs/input/refdog/commands/connector/status.md)
- [Listener status command](../../human/skupper-docs/input/refdog/commands/listener/status.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)
- [Refdog listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/prevented-recurrence.md`

Headings (6):
- # Prevented Recurrence
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [Root Cause Record](./root-cause-record.md)
- [Corrective Actions](./corrective-actions.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/preview-catalog.md`

Headings (5):
- # Preview Catalog
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (7):
- [Skupper Technology Previews](./skupper-previews.md)
- [Release notes](./release-notes.md)
- [Preview status](./preview-status.md)
- [Skupper releases page](https://skupper.io/releases/index.html)
- [Generated router notes](../skupper-router/)
- [Skupper releases](https://skupper.io/releases/index.html)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/preview-evaluation.md`

Headings (6):
- # Preview Evaluation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [What's New in Skupper](./skupper-whats-new.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Preview Status](./preview-status.md)
- [Known Limitations](./known-limitations.md)
- [Preview status](./preview-status.md)
- [Known limitations](./known-limitations.md)
- [Skupper Technology Previews map](./skupper-previews.md)
- [Generated router design notes](../skupper-router/)
- [Skupper docs](https://skupper.io/docs/)
- [GitHub issues](https://github.com/skupperproject/skupper/issues)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/preview-fit.md`

Headings (6):
- # Preview Fit Assessment
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Technology Previews](./skupper-previews.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Candidate Use Cases](./preview-use-cases.md)
- [Compatibility Checks](./compatibility-checks.md)
- [Candidate use cases](./preview-use-cases.md)
- [Compatibility checks](./compatibility-checks.md)
- [Compatibility matrix](./compatibility-matrix.md)
- [Platform guides](./platform-guides.md)
- [Skupper install docs](https://skupper.io/docs/install/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/preview-installation.md`

Headings (6):
- # Preview Installation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (8):
- [Skupper Technology Previews](./skupper-previews.md)
- [Compatibility Checks](./compatibility-checks.md)
- [Compatibility checks](./compatibility-checks.md)
- [Install docs](../../human/skupper-docs/input/install/index.md)
- [System install command](../../human/skupper-docs/input/refdog/commands/system/install.md)
- [Console installation docs](../../human/skupper-docs/input/console/index.md)
- [Skupper install docs](https://skupper.io/docs/install/index.html)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/preview-status.md`

Headings (6):
- # Preview Status
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (8):
- [What's New in Skupper](./skupper-whats-new.md)
- [Release Notes](./release-notes.md)
- [Release notes](./release-notes.md)
- [Skupper Technology Previews](./skupper-previews.md)
- [Preview catalog](./preview-catalog.md)
- [Support boundaries](./support-boundaries.md)
- [Skupper docs](https://skupper.io/docs/)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/preview-use-cases.md`

Headings (6):
- # Candidate Use Cases
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Skupper Technology Previews](./skupper-previews.md)
- [Preview Catalog](./preview-catalog.md)
- [Support Boundaries](./support-boundaries.md)
- [Preview catalog](./preview-catalog.md)
- [Support boundaries](./support-boundaries.md)
- [Skupper overview](../../human/skupper-docs/input/overview/index.md)
- [Generated network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper docs](https://skupper.io/docs/)
- [Skupper GitHub issues](https://github.com/skupperproject/skupper/issues)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/private-connectivity.md`

Headings (6):
- # Keep Services Private
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Discover Skupper](./discover-skupper.md)
- [Secure Links](./secure-links.md)
- [Certificates and Identity](./identity-model.md)
- [Security overview](../../human/skupper-docs/input/overview/security.md)
- [Connectivity overview](../../human/skupper-docs/input/overview/connectivity.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md)
- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Skupper docs](https://skupper.io/docs/)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/quality-review.md`

Headings (4):
- # PDF Quality Review
- ## Appears in
- ## Dependencies
- ## Notes

Links (3):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)
- [PDF Build](./pdf-build.md)
- [Link and Cross-reference Check](./link-check.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/rate-controls.md`

Headings (5):
- # Rate Controls
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Optimize Skupper](./optimize-skupper.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/rbac.md`

Headings (5):
- # Role-Based Access Control
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Secure Skupper](./secure-skupper.md)
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Site configuration with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/recovery-procedure.md`

Headings (5):
- # Recovery Procedure
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/commands/site/reload.md](../../human/skupper-docs/input/refdog/commands/site/reload.md)
- [human/skupper-docs/input/refdog/commands/site/start.md](../../human/skupper-docs/input/refdog/commands/site/start.md)
- [human/skupper-docs/input/refdog/commands/link/generate.md](../../human/skupper-docs/input/refdog/commands/link/generate.md)
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Site reload command](https://skupperproject.github.io/refdog/commands/site/reload.html)
- [Site start command](https://skupperproject.github.io/refdog/commands/site/start.html)
- [Link generate command](https://skupperproject.github.io/refdog/commands/link/generate.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/reference-guide.md`

Headings (4):
- # Reference Guide
- ## Appears in
- ## Dependencies
- ## Notes

Links (3):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)
- [Reference Source Content](./reference-source.md)
- [Release Version Metadata](./release-version.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/reference-source.md`

Headings (3):
- # Reference Source Content
- ## Appears in
- ## Notes

Links (1):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/release-differences.md`

Headings (5):
- # Release Differences
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Release Notes](./release-notes.md)
- [Behavior Changes](./behavior-changes.md)
- [Deprecations](./deprecations.md)
- [Known Limitations](./known-limitations.md)
- [Skupper source entry](../../sources/skupper.md)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Skupper GitHub repository](https://github.com/skupperproject/skupper)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/release-notes.md`

Headings (5):
- # Release Notes
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (7):
- [What's New in Skupper](./skupper-whats-new.md)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Skupper releases page](https://skupper.io/releases/index.html)
- [Install source](../../human/skupper-docs/input/install/index.md)
- [Source record: skupper-docs](../../sources/skupper-docs.md)
- [Skupper releases](https://skupper.io/releases/index.html)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/release-publish.md`

Headings (4):
- # Release Publication
- ## Appears in
- ## Dependencies
- ## Notes

Links (3):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)
- [PDF Quality Review](./quality-review.md)
- [Release Version Metadata](./release-version.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/release-version.md`

Headings (3):
- # Release Version Metadata
- ## Appears in
- ## Notes

Links (1):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/remediation.md`

Headings (6):
- # Remediation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [Root Cause Record](./root-cause-record.md)
- [Recovery Procedure](./recovery-procedure.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/refdog/commands/site/update.md](../../human/skupper-docs/input/refdog/commands/site/update.md)
- [human/skupper-docs/input/refdog/commands/link/delete.md](../../human/skupper-docs/input/refdog/commands/link/delete.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Site update command](https://skupperproject.github.io/refdog/commands/site/update.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/repeatable-environments.md`

Headings (6):
- # Repeatable Skupper Environments
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Develop with Skupper](./develop-skupper.md)
- [Configuration as Code](./configuration-as-code.md)
- [Integration Test Harness](./test-harness.md)
- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md)
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md)
- [generated/workflows/skupper-examples.md](../workflows/skupper-examples.md)
- [generated/skupper-ansible/skupper-ansible-workflow-mixed-sites.md](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper examples](https://github.com/skupperproject/skupper-example-hello-world)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/resource-automation.md`

Headings (5):
- # Resource Automation Interface
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Integrate Skupper](./integrate-skupper.md)
- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md)
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md)
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md)
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md)
- [human/skupper-docs/input/refdog/commands/site/generate.md](../../human/skupper-docs/input/refdog/commands/site/generate.md)
- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Site generate command](https://skupperproject.github.io/refdog/commands/site/generate.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/resource-fields.md`

Headings (5):
- # Resource Fields
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Skupper Reference](./skupper-reference.md)
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md)
- [generated/skupper/skupper-crd-sites-skupper-io.md](../skupper/skupper-crd-sites-skupper-io.md)
- [generated/skupper/skupper-crd-links-skupper-io.md](../skupper/skupper-crd-links-skupper-io.md)
- [generated/skupper/skupper-crd-listeners-skupper-io.md](../skupper/skupper-crd-listeners-skupper-io.md)
- [generated/skupper/skupper-crd-connectors-skupper-io.md](../skupper/skupper-crd-connectors-skupper-io.md)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/resource-limits.md`

Headings (5):
- # Resource Limits
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Configure Skupper](./configure-skupper.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Site configuration with CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Network deployment concerns](https://pwright.github.io/skupper-okf/generated/concepts/network-deployment-concerns)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/resource-profile.md`

Headings (5):
- # CPU and Memory Profile
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Optimize Skupper](./optimize-skupper.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/resource-reference.md`

Headings (6):
- # Resource Reference
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (13):
- [Skupper Reference](./skupper-reference.md)
- [Resource Fields](./resource-fields.md)
- [Resource Status](./resource-status.md)
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md)
- [human/skupper-docs/refdog/resources.md](../../human/skupper-docs/refdog/resources.md)
- [generated/skupper/skupper-crd-sites-skupper-io.md](../skupper/skupper-crd-sites-skupper-io.md)
- [generated/skupper/skupper-crd-links-skupper-io.md](../skupper/skupper-crd-links-skupper-io.md)
- [generated/skupper/skupper-crd-listeners-skupper-io.md](../skupper/skupper-crd-listeners-skupper-io.md)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/resource-schema.md`

Headings (5):
- # Resource Schemas
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Develop with Skupper](./develop-skupper.md)
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md)
- [human/skupper-docs/refdog/crds/skupper_site_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_site_crd.yaml)
- [human/skupper-docs/refdog/crds/skupper_link_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_link_crd.yaml)
- [human/skupper-docs/refdog/crds/skupper_listener_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_listener_crd.yaml)
- [human/skupper-docs/refdog/crds/skupper_connector_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_connector_crd.yaml)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/resource-status.md`

Headings (5):
- # Resource Status
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Skupper Reference](./skupper-reference.md)
- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md)
- [generated/skupper/skupper-crd-sites-skupper-io.md](../skupper/skupper-crd-sites-skupper-io.md)
- [generated/skupper/skupper-crd-links-skupper-io.md](../skupper/skupper-crd-links-skupper-io.md)
- [generated/concepts/listener.md](../concepts/listener.md)
- [generated/concepts/connector.md](../concepts/connector.md)
- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/resource-tuning.md`

Headings (6):
- # Runtime Resource Tuning
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Optimize Skupper](./optimize-skupper.md)
- [CPU and Memory Profile](./resource-profile.md)
- [Load Tests](./load-tests.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/restored-connectivity.md`

Headings (6):
- # Restored Connectivity
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [Fault Isolation](./fault-isolation.md)
- [Remediation](./remediation.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md)
- [human/skupper-docs/input/refdog/commands/site/status.md](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [human/skupper-docs/input/refdog/commands/link/status.md](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)
- [Site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Link status command](https://skupperproject.github.io/refdog/commands/link/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/risk-assessment.md`

Headings (5):
- # Rollout Risk Assessment
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md)
- [Skupper security overview](../../human/skupper-docs/input/overview/security.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/rollback-path.md`

Headings (5):
- # Rollback Path
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Source Deployment Assessment](./source-assessment.md)
- [Configuration and State Backup](./backup-state.md)
- [Rollback Plan](./rollback-plan.md)
- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/rollback-plan.md`

Headings (6):
- # Rollback Plan
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Configuration and State Backup](./backup-state.md)
- [Version Compatibility](./version-compatibility.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Network console guide](../../human/skupper-docs/input/console/index.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Version Compatibility](./version-compatibility.md)
- [Release Notes](./release-notes.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper network console](https://skupper.io/docs/console/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/rollout-plan.md`

Headings (6):
- # Rollout Plan
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (16):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Target Application Network Topology](./target-topology.md)
- [Operational Ownership](./ownership-model.md)
- [Rollout Risk Assessment](./risk-assessment.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Kubernetes CLI overview](../../human/skupper-docs/input/kube-cli/index.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Skupper Kubernetes CLI overview](https://skupper.io/docs/kube-cli/index.html)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/root-cause-record.md`

Headings (6):
- # Root Cause Record
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [Fault Isolation](./fault-isolation.md)
- [Logs, Events, Metrics, and Configuration](./evidence-bundle.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/skupper-docs-landscape/evidence-bundle.md](./evidence-bundle.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/rotation.md`

Headings (6):
- # Certificate Rotation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Secure Skupper](./secure-skupper.md)
- [Certificate Issuance](./issuance.md)
- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/routing-mode.md`

Headings (5):
- # Routing Mode
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Configure Skupper](./configure-skupper.md)
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [Load balancing overview](https://skupper.io/docs/overview/load-balancing.html)
- [Multi-key listener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/routing-policy.md`

Headings (6):
- # Routing Policy
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Service Definition](./service-definition.md)
- [Routing key concept](../concepts/routing-key.md)
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [MultiKeyListener resource](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Refdog routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)
- [Refdog MultiKeyListener resource](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/routing-tuning.md`

Headings (6):
- # Routing Tuning
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Optimize Skupper](./optimize-skupper.md)
- [Topology Analysis](./topology-analysis.md)
- [Path Selection Data](./path-selection.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md)
- [human/skupper-docs/input/refdog/topics/load-balancing.md](../../human/skupper-docs/input/refdog/topics/load-balancing.md)
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md)
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Load balancing topic](https://skupperproject.github.io/refdog/topics/load-balancing.html)
- [MultiKeyListener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/routing.md`

Headings (6):
- # Service Routing
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Discover Skupper](./discover-skupper.md)
- [Sites](./sites.md)
- [Routing overview](../../human/skupper-docs/input/overview/routing.md)
- [Generated routing-key concept](../concepts/routing-key.md)
- [Listener concept](../concepts/listener.md)
- [Connector concept](../concepts/connector.md)
- [Load balancing overview](../../human/skupper-docs/input/overview/load-balancing.md)
- [Routing overview](https://skupper.io/docs/overview/routing.html)
- [Load balancing overview](https://skupper.io/docs/overview/load-balancing.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/runtime-logs.md`

Headings (6):
- # Runtime Logs
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Observe Skupper](./observe-skupper.md)
- [Log Collection](./log-collection.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-docs-landscape/logging-settings.md](./logging-settings.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/runtime-settings.md`

Headings (6):
- # Runtime Settings
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Configure Skupper](./configure-skupper.md)
- [Resource Limits](./resource-limits.md)
- [Logging Settings](./logging-settings.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/system-cli/site-configuration.md](../../human/skupper-docs/input/system-cli/site-configuration.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug command reference](https://skupperproject.github.io/refdog/commands/debug/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/sandbox-trial.md`

Headings (6):
- # Sandbox Trial
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Technology Previews](./skupper-previews.md)
- [Preview Installation](./preview-installation.md)
- [Validation Test Plan](./test-plan.md)
- [Preview installation](./preview-installation.md)
- [Validation test plan](./test-plan.md)
- [Install docs](../../human/skupper-docs/input/install/index.md)
- [Troubleshooting docs](../../human/skupper-docs/input/troubleshooting/index.md)
- [Debug dumps topic](../../human/skupper-docs/input/refdog/topics/debug-dumps.md)
- [Skupper install docs](https://skupper.io/docs/install/index.html)
- [Skupper troubleshooting docs](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/secrets-injection.md`

Headings (5):
- # Secrets Injection
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Develop with Skupper](./develop-skupper.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md)
- [human/skupper-docs/input/refdog/resources/access-grant.md](../../human/skupper-docs/input/refdog/resources/access-grant.md)
- [generated/skupper-ansible/skupper-ansible-module-token.md](../skupper-ansible/skupper-ansible-module-token.md)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [AccessToken resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)
- [AccessGrant resource reference](https://skupperproject.github.io/refdog/resources/access-grant.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/secrets-interface.md`

Headings (5):
- # Secrets Interface
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Integrate Skupper](./integrate-skupper.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md)
- [human/skupper-docs/input/refdog/resources/access-grant.md](../../human/skupper-docs/input/refdog/resources/access-grant.md)
- [generated/skupper-ansible/skupper-ansible-module-token.md](../skupper-ansible/skupper-ansible-module-token.md)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [AccessToken resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)
- [AccessGrant resource reference](https://skupperproject.github.io/refdog/resources/access-grant.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/secure-links.md`

Headings (6):
- # Secure Links
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Discover Skupper](./discover-skupper.md)
- [Site Links](./links.md)
- [Certificates and Identity](./identity-model.md)
- [Site linking topic](../../human/skupper-docs/input/refdog/topics/site-linking.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Kubernetes YAML site linking](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [System YAML site linking](../../human/skupper-docs/input/system-yaml/site-linking.md)
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md)
- [Kubernetes site linking](https://skupper.io/docs/kube-yaml/site-linking.html)
- [System site linking](https://skupper.io/docs/system-yaml/site-linking.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/secure-skupper.md`

Headings (8):
- # Secure Skupper
- ## Appears in
- ## Topics
- ### Security Outcomes
- ### Security Controls
- ### Identity Foundations
- ### Isolation Foundations
- ## Notes

Links (15):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Trusted Site Connectivity](./trusted-connectivity.md)
- [Least-Privilege Application Network](./least-privilege-network.md)
- [Mutual Authentication](./mutual-authentication.md)
- [Access Policy](./access-policy.md)
- [Network Isolation](./network-isolation.md)
- [Certificate Lifecycle](./certificate-lifecycle.md)
- [Site Certificates](./site-certificates.md)
- [Trust Bundle](./trust-bundle.md)
- [Role-Based Access Control](./rbac.md)
- [Service Exposure Policy](./service-policy.md)
- [Namespace Controls](./namespace-controls.md)
- [Firewall Rules](./firewall-rules.md)
- [Certificate Issuance](./issuance.md)
- [Certificate Rotation](./rotation.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/security-guide.md`

Headings (4):
- # Security Guide
- ## Appears in
- ## Dependencies
- ## Notes

Links (3):
- [Skupper Downloadable Guides](./skupper-pdf-library.md)
- [Guide Source Content](./guide-source.md)
- [Release Version Metadata](./release-version.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/security-integration.md`

Headings (6):
- # Security Tooling Integration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Integrate Skupper](./integrate-skupper.md)
- [Certificate Interface](./certificate-interface.md)
- [Policy Interface](./policy-interface.md)
- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md)
- [human/skupper-docs/input/refdog/topics/application-tls.md](../../human/skupper-docs/input/refdog/topics/application-tls.md)
- [human/skupper-docs/input/refdog/topics/system-tls-credentials.md](../../human/skupper-docs/input/refdog/topics/system-tls-credentials.md)
- [human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Application TLS topic](https://skupperproject.github.io/refdog/topics/application-tls.html)
- [System TLS credentials topic](https://skupperproject.github.io/refdog/topics/system-tls-credentials.html)
- [AccessToken resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/security-requirements.md`

Headings (6):
- # Security Requirements
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Trust Boundaries](./trust-boundaries.md)
- [Identity and Certificate Policy](./identity-policy.md)
- [Skupper security overview](../../human/skupper-docs/input/overview/security.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md)
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md)
- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-address.md`

Headings (5):
- # Service Address
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Configure Skupper](./configure-skupper.md)
- [generated/concepts/listener.md](../concepts/listener.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Listener concept](https://skupperproject.github.io/refdog/concepts/listener.html)
- [Routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)
- [Service exposure with CLI](https://skupper.io/docs/kube-cli/service-exposure.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-configuration.md`

Headings (5):
- # Service Configuration
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Administer Skupper](./administer-skupper.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Connector concept](../concepts/connector.md)
- [Listener concept](../concepts/listener.md)
- [Connector resource](../../human/skupper-docs/input/refdog/resources/connector.md)
- [Listener resource](../../human/skupper-docs/input/refdog/resources/listener.md)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector resource](https://skupperproject.github.io/refdog/resources/connector.html)
- [Refdog listener resource](https://skupperproject.github.io/refdog/resources/listener.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-connectivity.md`

Headings (6):
- # Configured Service Connectivity
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (13):
- [Configure Skupper](./configure-skupper.md)
- [Listener Configuration](./listener-config.md)
- [Connector Configuration](./connector-config.md)
- [Service Routing Configuration](./service-routing.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [generated/concepts/listener.md](../concepts/listener.md)
- [generated/concepts/connector.md](../concepts/connector.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [Service exposure with CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-definition.md`

Headings (5):
- # Service Definition
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Connector concept](../concepts/connector.md)
- [Listener concept](../concepts/listener.md)
- [Connector resource](../../human/skupper-docs/input/refdog/resources/connector.md)
- [Listener resource](../../human/skupper-docs/input/refdog/resources/listener.md)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector resource](https://skupperproject.github.io/refdog/resources/connector.html)
- [Refdog listener resource](https://skupperproject.github.io/refdog/resources/listener.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-discovery.md`

Headings (5):
- # Service Discovery Interface
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Integrate Skupper](./integrate-skupper.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [generated/concepts/listener.md](../concepts/listener.md)
- [generated/concepts/connector.md](../concepts/connector.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/topics/service-exposure.md](../../human/skupper-docs/input/refdog/topics/service-exposure.md)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Service exposure topic](https://skupperproject.github.io/refdog/topics/service-exposure.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)
- [Routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-exposure.md`

Headings (6):
- # Service Exposure
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Discover Skupper](./discover-skupper.md)
- [Sites](./sites.md)
- [Service Routing](./routing.md)
- [Service exposure topic](../../human/skupper-docs/input/refdog/topics/service-exposure.md)
- [Kubernetes YAML service exposure](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [System YAML service exposure](../../human/skupper-docs/input/system-yaml/service-exposure.md)
- [Generated listener concept](../concepts/listener.md)
- [Generated connector concept](../concepts/connector.md)
- [Kubernetes service exposure](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [System service exposure](https://skupper.io/docs/system-yaml/service-exposure.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-metrics.md`

Headings (6):
- # Service Metrics
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Observe Skupper](./observe-skupper.md)
- [Metrics Export](./metrics-export.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md)
- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-onboarding.md`

Headings (6):
- # Onboard a Service
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Service Definition](./service-definition.md)
- [Routing Policy](./routing-policy.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Kubernetes YAML service exposure](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [Connector create command](../../human/skupper-docs/input/refdog/commands/connector/create.md)
- [Listener create command](../../human/skupper-docs/input/refdog/commands/listener/create.md)
- [Routing key concept](../concepts/routing-key.md)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Skupper YAML service exposure guide](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Refdog routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-operations.md`

Headings (6):
- # Service Operations
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Administer Skupper](./administer-skupper.md)
- [Service Status](./service-status.md)
- [Service Configuration](./service-configuration.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Connector status command](../../human/skupper-docs/input/refdog/commands/connector/status.md)
- [Listener status command](../../human/skupper-docs/input/refdog/commands/listener/status.md)
- [Routing key concept](../concepts/routing-key.md)
- [Network Observer API concept](../concepts/network-observer-api.md)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)
- [Refdog listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-policy.md`

Headings (5):
- # Service Exposure Policy
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Secure Skupper](./secure-skupper.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/topics/service-exposure.md](../../human/skupper-docs/input/refdog/topics/service-exposure.md)
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md)
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md)
- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Service exposure topic](https://skupperproject.github.io/refdog/topics/service-exposure.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-priorities.md`

Headings (5):
- # Service Priorities
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Optimize Skupper](./optimize-skupper.md)
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md)
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md)
- [human/skupper-docs/input/refdog/concepts/multi-key-listener.md](../../human/skupper-docs/input/refdog/concepts/multi-key-listener.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Listener-side routing policy concept](https://skupperproject.github.io/refdog/concepts/multi-key-listener.html)
- [MultiKeyListener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-routing.md`

Headings (6):
- # Service Routing Configuration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Configure Skupper](./configure-skupper.md)
- [Service Address](./service-address.md)
- [Routing Mode](./routing-mode.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [generated/concepts/listener.md](../concepts/listener.md)
- [generated/concepts/connector.md](../concepts/connector.md)
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md)
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md)
- [Load balancing overview](https://skupper.io/docs/overview/load-balancing.html)
- [Multi-key listener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-selection.md`

Headings (5):
- # Choose a Test Service
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Get Started with Skupper](./get-started.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Skupper Hello World source entry](../../sources/skupper-example-hello-world.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Connector concept](../../human/skupper-docs/input/refdog/concepts/connector.md)
- [Listener concept](../../human/skupper-docs/input/refdog/concepts/listener.md)
- [Skupper Hello World example](https://github.com/skupperproject/skupper-example-hello-world)
- [Skupper examples](https://skupper.io/examples/index.html)
- [Exposing services with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/service-status.md`

Headings (5):
- # Service Status
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Administer Skupper](./administer-skupper.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Connector status command](../../human/skupper-docs/input/refdog/commands/connector/status.md)
- [Listener status command](../../human/skupper-docs/input/refdog/commands/listener/status.md)
- [Routing key concept](../concepts/routing-key.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)
- [Refdog listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-behavior.md`

Headings (6):
- # Configured Site Behavior
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Configure Skupper](./configure-skupper.md)
- [Site Configuration](./site-config.md)
- [Runtime Settings](./runtime-settings.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md)
- [Site configuration with CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-certificates.md`

Headings (5):
- # Site Certificates
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Secure Skupper](./secure-skupper.md)
- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-config.md`

Headings (6):
- # Site Configuration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Configure Skupper](./configure-skupper.md)
- [Site Identity Settings](./site-identity-config.md)
- [Namespace Scope](./namespace-scope.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [human/skupper-docs/input/refdog/concepts/site.md](../../human/skupper-docs/input/refdog/concepts/site.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Site configuration with CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Site concept](https://skupperproject.github.io/refdog/concepts/site.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-configuration.md`

Headings (5):
- # Site Configuration
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Administer Skupper](./administer-skupper.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Kubernetes YAML site configuration](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md)
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Skupper YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Refdog site resource](https://skupperproject.github.io/refdog/resources/site.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-identity-config.md`

Headings (5):
- # Site Identity Settings
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Configure Skupper](./configure-skupper.md)
- [human/skupper-docs/input/refdog/concepts/site.md](../../human/skupper-docs/input/refdog/concepts/site.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md)
- [Site concept](https://skupperproject.github.io/refdog/concepts/site.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Site configuration with CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-identity.md`

Headings (5):
- # Site Identity
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Skupper security overview](../../human/skupper-docs/input/overview/security.md)
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md)
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md)
- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Refdog site concept](https://skupperproject.github.io/refdog/concepts/site.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-initialization.md`

Headings (6):
- # Site Initialization
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Install Skupper](./install-skupper.md)
- [Select Installation Method](./installation-method.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Kubernetes YAML site configuration](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [Site create command](../../human/skupper-docs/input/refdog/commands/site/create.md)
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md)
- [Skupper resources overview](../../human/skupper-docs/input/refdog/resources/index.md)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Creating a site with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Refdog site create command](https://skupperproject.github.io/refdog/commands/site/create.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-inventory.md`

Headings (5):
- # Cluster and Host Inventory
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md)
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Refdog site concept](https://skupperproject.github.io/refdog/concepts/site.html)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-metrics.md`

Headings (6):
- # Site Metrics
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Observe Skupper](./observe-skupper.md)
- [Metrics Export](./metrics-export.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [human/skupper-docs/input/refdog/commands/site/status.md](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-onboarding.md`

Headings (6):
- # Onboard a Site
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Site Configuration Template](./site-template.md)
- [Site Identity](./site-identity.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Kubernetes YAML site configuration](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [Site create command](../../human/skupper-docs/input/refdog/commands/site/create.md)
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Creating a site with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Refdog site resource](https://skupperproject.github.io/refdog/resources/site.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-operations.md`

Headings (6):
- # Site Operations
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Administer Skupper](./administer-skupper.md)
- [Site Status](./site-status.md)
- [Site Configuration](./site-configuration.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Refdog site resource](https://skupperproject.github.io/refdog/resources/site.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-status.md`

Headings (5):
- # Site Status
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Administer Skupper](./administer-skupper.md)
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog site resource](https://skupperproject.github.io/refdog/resources/site.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/site-template.md`

Headings (5):
- # Site Configuration Template
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Extend a Skupper Application Network](./extend-skupper.md)
- [Kubernetes YAML site configuration](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Custom labels guide](../../human/skupper-docs/input/kube-yaml/custom-labels.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Refdog site resource](https://skupperproject.github.io/refdog/resources/site.html)
- [Skupper custom labels guide](https://skupper.io/docs/kube-yaml/custom-labels.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/sites.md`

Headings (5):
- # Sites
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (7):
- [Discover Skupper](./discover-skupper.md)
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md)
- [Site configuration topic](../../human/skupper-docs/input/refdog/topics/site-configuration.md)
- [Kubernetes YAML site configuration](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [System YAML site configuration](../../human/skupper-docs/input/system-yaml/site-configuration.md)
- [Site concept reference](https://skupper.io/docs/refdog/concepts/site.html)
- [Kubernetes site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/skupper-docs-series.md`

Headings (8):
- # Skupper Documentation Landscape
- ## Topics
- ### Orient
- ### Adopt
- ### Operate
- ### Build and Integrate
- ### Resources
- ## Notes

Links (20):
- [What's New](./skupper-whats-new.md)
- [Discover Skupper](./discover-skupper.md)
- [Technology Previews](./skupper-previews.md)
- [Get Started](./get-started.md)
- [Plan](./plan-skupper.md)
- [Install](./install-skupper.md)
- [Extend](./extend-skupper.md)
- [Upgrade](./upgrade-skupper.md)
- [Migrate](./migrate-skupper.md)
- [Administer](./administer-skupper.md)
- [Configure](./configure-skupper.md)
- [Secure](./secure-skupper.md)
- [Observe](./observe-skupper.md)
- [Optimize](./optimize-skupper.md)
- [Troubleshoot](./troubleshoot-skupper.md)
- [Develop](./develop-skupper.md)
- [Integrate](./integrate-skupper.md)
- [Platforms and Managed Environments](./platform-guides.md)
- [Reference](./skupper-reference.md)
- [Downloadable Guides](./skupper-pdf-library.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/skupper-pdf-library.md`

Headings (7):
- # Skupper Downloadable Guides
- ## Appears in
- ## Topics
- ### Downloadable Guides
- ### Publishing Workflow
- ### Source and Versioning
- ## Notes

Links (12):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Getting Started Guide](./getting-started-guide.md)
- [Operations Guide](./operations-guide.md)
- [Security Guide](./security-guide.md)
- [Reference Guide](./reference-guide.md)
- [PDF Build](./pdf-build.md)
- [PDF Quality Review](./quality-review.md)
- [Release Publication](./release-publish.md)
- [Guide Source Content](./guide-source.md)
- [Reference Source Content](./reference-source.md)
- [Release Version Metadata](./release-version.md)
- [Link and Cross-reference Check](./link-check.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/skupper-previews.md`

Headings (7):
- # Skupper Technology Previews
- ## Appears in
- ## Topics
- ### Evaluate Preview Value
- ### Validate Safely
- ### Preview Controls
- ## Notes

Links (11):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Candidate Use Cases](./preview-use-cases.md)
- [Preview Fit Assessment](./preview-fit.md)
- [Sandbox Trial](./sandbox-trial.md)
- [Feedback and Issue Reporting](./feedback-loop.md)
- [Preview Catalog](./preview-catalog.md)
- [Support Boundaries](./support-boundaries.md)
- [Compatibility Checks](./compatibility-checks.md)
- [Preview Installation](./preview-installation.md)
- [Validation Test Plan](./test-plan.md)
- [Known Issues](./known-issues.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/skupper-reference.md`

Headings (9):
- # Skupper Reference
- ## Appears in
- ## Topics
- ### Interface Reference
- ### Runtime Reference
- ### Syntax and Schema
- ### Defaults and Diagnostics
- ### Matrices and Terms
- ## Notes

Links (16):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [CLI Reference](./cli-reference.md)
- [Resource Reference](./resource-reference.md)
- [Configuration Reference](./configuration-reference.md)
- [Status and Condition Reference](./status-reference.md)
- [Compatibility Reference](./compatibility-reference.md)
- [Command Syntax](./command-syntax.md)
- [Exit Status and Errors](./exit-status.md)
- [Resource Fields](./resource-fields.md)
- [Resource Status](./resource-status.md)
- [Default Values](./defaults.md)
- [Validation Constraints](./constraints.md)
- [Event and Diagnostic Codes](./event-codes.md)
- [Version Matrix](./version-matrix.md)
- [Platform Matrix](./platform-matrix.md)
- [Glossary](./glossary.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/skupper-whats-new.md`

Headings (7):
- # What's New in Skupper
- ## Appears in
- ## Topics
- ### Release Highlights
- ### Adoption Impact
- ### Authoritative Sources
- ## Notes

Links (11):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [New Capabilities](./new-capabilities.md)
- [Behavior Changes](./behavior-changes.md)
- [Upgrade Decisions](./upgrade-decisions.md)
- [Preview Evaluation](./preview-evaluation.md)
- [Release Notes](./release-notes.md)
- [Upgrade Notes](./upgrade-notes.md)
- [Deprecations](./deprecations.md)
- [Preview Status](./preview-status.md)
- [Known Limitations](./known-limitations.md)
- [Compatibility Matrix](./compatibility-matrix.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/source-assessment.md`

Headings (5):
- # Source Deployment Assessment
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Migrating from Skupper v1](../../human/skupper-docs/input/overview/migrating.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md)
- [Application and Service Inventory](./application-inventory.md)
- [Site Inventory](./site-inventory.md)
- [Migrating from Skupper v1](https://skupper.io/docs/overview/migrating.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/starter-prerequisites.md`

Headings (5):
- # Cluster or Host Prerequisites
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (8):
- [Get Started with Skupper](./get-started.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Kubernetes CLI overview](../../human/skupper-docs/input/kube-cli/index.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/status-reference.md`

Headings (6):
- # Status and Condition Reference
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (13):
- [Skupper Reference](./skupper-reference.md)
- [Resource Status](./resource-status.md)
- [Event and Diagnostic Codes](./event-codes.md)
- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md)
- [human/skupper-docs/input/refdog/commands/site/status.md](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [human/skupper-docs/input/refdog/commands/link/status.md](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [human/skupper-docs/input/refdog/commands/listener/status.md](../../human/skupper-docs/input/refdog/commands/listener/status.md)
- [human/skupper-docs/input/refdog/commands/connector/status.md](../../human/skupper-docs/input/refdog/commands/connector/status.md)
- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Link status command](https://skupperproject.github.io/refdog/commands/link/status.html)
- [Listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)
- [Connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/support-boundaries.md`

Headings (5):
- # Support Boundaries
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (7):
- [Skupper Technology Previews](./skupper-previews.md)
- [Release notes](./release-notes.md)
- [Known limitations](./known-limitations.md)
- [Install docs](../../human/skupper-docs/input/install/index.md)
- [Platform guides](./platform-guides.md)
- [Skupper docs](https://skupper.io/docs/)
- [Skupper releases](https://skupper.io/releases/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/supported-deployment.md`

Headings (6):
- # Supported Platform Deployment
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [Platform Compatibility Profile](./platform-profile.md)
- [Installation Pattern](./installation-pattern.md)
- [human/skupper-docs/input/install/index.md](../../human/skupper-docs/input/install/index.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [human/skupper-docs/input/system-cli/site-configuration.md](../../human/skupper-docs/input/system-cli/site-configuration.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Installation](https://skupper.io/docs/install/index.html)
- [Kubernetes CLI site configuration](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Kubernetes YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [System site configuration](https://skupper.io/docs/system-cli/site-configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/symptom-capture.md`

Headings (5):
- # Symptom Capture
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Troubleshoot Skupper](./troubleshoot-skupper.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md)
- [generated/skupper-docs-landscape/runtime-logs.md](./runtime-logs.md)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper project](https://skupper.io/)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/system-service.md`

Headings (6):
- # System Service Configuration
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Skupper Platform and Managed-Environment Guides](./platform-guides.md)
- [Host Compatibility Profile](./host-profile.md)
- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md)
- [human/skupper-docs/input/system-yaml/service-exposure.md](../../human/skupper-docs/input/system-yaml/service-exposure.md)
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md)
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md)
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md)
- [System CLI service exposure](https://skupper.io/docs/system-cli/service-exposure.html)
- [System YAML service exposure](https://skupper.io/docs/system-yaml/service-exposure.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/target-design.md`

Headings (5):
- # Target Deployment Design
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Migrate to or Between Skupper Deployments](./migrate-skupper.md)
- [Migrating from Skupper v1](../../human/skupper-docs/input/overview/migrating.md)
- [Target Application Network Topology](./target-topology.md)
- [Service Definition](./service-definition.md)
- [Routing Policy](./routing-policy.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Migrating from Skupper v1](https://skupper.io/docs/overview/migrating.html)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Skupper YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/target-topology.md`

Headings (6):
- # Target Application Network Topology
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Cluster and Host Inventory](./site-inventory.md)
- [Traffic Flow Requirements](./traffic-flows.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper connectivity overview](../../human/skupper-docs/input/overview/connectivity.md)
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md)
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Skupper connectivity overview](https://skupper.io/docs/overview/connectivity.html)
- [Refdog site concept](https://skupperproject.github.io/refdog/concepts/site.html)
- [Refdog link concept](https://skupperproject.github.io/refdog/concepts/link.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/test-harness.md`

Headings (6):
- # Integration Test Harness
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Develop with Skupper](./develop-skupper.md)
- [Reference Examples](./examples.md)
- [generated/workflows/skupper-examples.md](../workflows/skupper-examples.md)
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [Site configuration with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper examples](https://github.com/skupperproject/skupper-example-hello-world)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/test-plan.md`

Headings (5):
- # Validation Test Plan
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (8):
- [Skupper Technology Previews](./skupper-previews.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Troubleshooting docs](../../human/skupper-docs/input/troubleshooting/index.md)
- [Debug dumps topic](../../human/skupper-docs/input/refdog/topics/debug-dumps.md)
- [Console validation section](../../human/skupper-docs/input/console/index.md#console-validation)
- [Network Observer API concept](../concepts/network-observer-api.md)
- [Skupper examples](https://github.com/skupperproject/skupper-example-hello-world)
- [Skupper troubleshooting docs](https://skupper.io/docs/troubleshooting/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/topology-analysis.md`

Headings (5):
- # Topology Analysis
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Optimize Skupper](./optimize-skupper.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/refdog/concepts/link.md](../../human/skupper-docs/input/refdog/concepts/link.md)
- [human/skupper-docs/input/refdog/topics/large-networks.md](../../human/skupper-docs/input/refdog/topics/large-networks.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Link concept](https://skupperproject.github.io/refdog/concepts/link.html)
- [Large networks topic](https://skupperproject.github.io/refdog/topics/large-networks.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/trace-context.md`

Headings (5):
- # Trace Context
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Observe Skupper](./observe-skupper.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-docs-landscape/trace-correlation.md](./trace-correlation.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper repository](https://github.com/skupperproject/skupper)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/trace-correlation.md`

Headings (6):
- # Trace Correlation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Observe Skupper](./observe-skupper.md)
- [Trace Context](./trace-context.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/skupper-docs-landscape/trace-context.md](./trace-context.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper repository](https://github.com/skupperproject/skupper)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/traffic-baseline.md`

Headings (5):
- # Traffic Baseline
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Optimize Skupper](./optimize-skupper.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md)
- [generated/skupper-docs-landscape/flow-metrics.md](./flow-metrics.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/traffic-flows.md`

Headings (6):
- # Traffic Flow Requirements
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Skupper Adoption Bridge](../skupper-adoption-bridge/skupper-adoption-bridge.md)
- [Application and Service Inventory](./application-inventory.md)
- [Connector concept](../concepts/connector.md)
- [Listener concept](../concepts/listener.md)
- [Routing key concept](../concepts/routing-key.md)
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)
- [Refdog listener concept](https://skupperproject.github.io/refdog/concepts/listener.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/traffic-insight.md`

Headings (6):
- # Traffic Insight
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Observe Skupper](./observe-skupper.md)
- [Flow Metrics](./flow-metrics.md)
- [Trace Correlation](./trace-correlation.md)
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md)
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md)
- [generated/skupper-console/console.md](../skupper-console/console.md)
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper repository](https://github.com/skupperproject/skupper)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/traffic-shaping.md`

Headings (6):
- # Traffic Shaping
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Optimize Skupper](./optimize-skupper.md)
- [Service Priorities](./service-priorities.md)
- [Rate Controls](./rate-controls.md)
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md)
- [human/skupper-docs/input/refdog/concepts/multi-key-listener.md](../../human/skupper-docs/input/refdog/concepts/multi-key-listener.md)
- [generated/concepts/routing-key.md](../concepts/routing-key.md)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Listener-side routing policy concept](https://skupperproject.github.io/refdog/concepts/multi-key-listener.html)
- [MultiKeyListener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/troubleshoot-skupper.md`

Headings (7):
- # Troubleshoot Skupper
- ## Appears in
- ## Topics
- ### Troubleshooting Outcomes
- ### Diagnostic Workflow
- ### Diagnostic Evidence
- ## Notes

Links (12):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Restored Connectivity](./restored-connectivity.md)
- [Prevented Recurrence](./prevented-recurrence.md)
- [Fault Isolation](./fault-isolation.md)
- [Root Cause Record](./root-cause-record.md)
- [Remediation](./remediation.md)
- [Corrective Actions](./corrective-actions.md)
- [Symptom Capture](./symptom-capture.md)
- [Site, Link, Route, and Service Checks](./layered-checks.md)
- [Logs, Events, Metrics, and Configuration](./evidence-bundle.md)
- [Recovery Procedure](./recovery-procedure.md)
- [Monitoring Improvements](./monitoring-improvements.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/trust-boundaries.md`

Headings (5):
- # Trust Boundaries
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Plan a Skupper Deployment](./plan-skupper.md)
- [Skupper security overview](../../human/skupper-docs/input/overview/security.md)
- [Skupper connectivity overview](../../human/skupper-docs/input/overview/connectivity.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md)
- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Skupper connectivity overview](https://skupper.io/docs/overview/connectivity.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/trust-bundle.md`

Headings (5):
- # Trust Bundle
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Secure Skupper](./secure-skupper.md)
- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md)
- [human/skupper-docs/input/refdog/concepts/access-token.md](../../human/skupper-docs/input/refdog/concepts/access-token.md)
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md)
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)
- [Access token resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/trusted-connectivity.md`

Headings (6):
- # Trusted Site Connectivity
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (12):
- [Secure Skupper](./secure-skupper.md)
- [Mutual Authentication](./mutual-authentication.md)
- [Certificate Lifecycle](./certificate-lifecycle.md)
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md)
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md)
- [human/skupper-docs/input/refdog/concepts/link.md](../../human/skupper-docs/input/refdog/concepts/link.md)
- [human/skupper-docs/input/refdog/concepts/access-token.md](../../human/skupper-docs/input/refdog/concepts/access-token.md)
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [Link concept](https://skupperproject.github.io/refdog/concepts/link.html)
- [Access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/upgrade-decisions.md`

Headings (6):
- # Upgrade Decisions
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [What's New in Skupper](./skupper-whats-new.md)
- [Behavior Changes](./behavior-changes.md)
- [Deprecations](./deprecations.md)
- [Behavior changes](./behavior-changes.md)
- [Deprecations](./deprecations.md)
- [Install guide upgrade section](../../human/skupper-docs/input/install/index.md#skupper-upgrading-sites)
- [Console upgrade section](../../human/skupper-docs/input/console/index.md#console-upgrade)
- [Skupper releases](https://skupper.io/releases/index.html)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/upgrade-notes.md`

Headings (6):
- # Upgrade Notes
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (8):
- [What's New in Skupper](./skupper-whats-new.md)
- [Release Notes](./release-notes.md)
- [Release notes](./release-notes.md)
- [Install guide upgrade section](../../human/skupper-docs/input/install/index.md#skupper-upgrading-sites)
- [Local site upgrade section](../../human/skupper-docs/input/install/index.md#skupper-upgrading-local-sites)
- [Console upgrade section](../../human/skupper-docs/input/console/index.md#console-upgrade)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper install docs](https://skupper.io/docs/install/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/upgrade-sequence.md`

Headings (6):
- # Site Upgrade Sequence
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Compatibility Review](./compatibility-review.md)
- [Maintenance and Communication Plan](./maintenance-plan.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Network deployment concerns](../concepts/network-deployment-concerns.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Version Compatibility](./version-compatibility.md)
- [Release Differences](./release-differences.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/upgrade-skupper.md`

Headings (7):
- # Upgrade Skupper
- ## Appears in
- ## Topics
- ### Upgrade Outcome
- ### Upgrade Execution
- ### Upgrade Readiness
- ## Notes

Links (12):
- [Skupper Documentation Landscape](./skupper-docs-series.md)
- [Upgraded Application Network](./upgraded-network.md)
- [Upgrade Validation](./upgrade-validation.md)
- [Site Upgrade Sequence](./upgrade-sequence.md)
- [CLI, Operator, and Router Upgrades](./component-upgrades.md)
- [Rollback Plan](./rollback-plan.md)
- [Compatibility Review](./compatibility-review.md)
- [Maintenance and Communication Plan](./maintenance-plan.md)
- [Configuration and State Backup](./backup-state.md)
- [Post-upgrade Test Suite](./post-upgrade-tests.md)
- [Version Compatibility](./version-compatibility.md)
- [Release Differences](./release-differences.md)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/upgrade-validation.md`

Headings (6):
- # Upgrade Validation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Upgraded Application Network](./upgraded-network.md)
- [Post-upgrade Test Suite](./post-upgrade-tests.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md)
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md)
- [Skupper example applications](../workflows/skupper-examples.md)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Refdog link status command](https://skupperproject.github.io/refdog/commands/link/status.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/upgraded-network.md`

Headings (6):
- # Upgraded Application Network
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Site Upgrade Sequence](./upgrade-sequence.md)
- [CLI, Operator, and Router Upgrades](./component-upgrades.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md)
- [Release Notes](./release-notes.md)
- [Compatibility Matrix](./compatibility-matrix.md)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/validated-install.md`

Headings (6):
- # Validated Installation
- ## Appears in
- ## Dependencies
- ## Sources
- ## Website Links
- ## Draft Notes

Links (11):
- [Install Skupper](./install-skupper.md)
- [Operational Skupper Site](./installed-site.md)
- [Post-install Health Checks](./health-checks.md)
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md)
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md)
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md)
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Refdog version command](https://skupperproject.github.io/refdog/commands/version.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/version-compatibility.md`

Headings (5):
- # Version Compatibility
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (9):
- [Upgrade Skupper](./upgrade-skupper.md)
- [Compatibility Matrix](./compatibility-matrix.md)
- [Release Notes](./release-notes.md)
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md)
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md)
- [Skupper source entry](../../sources/skupper.md)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Refdog version command](https://skupperproject.github.io/refdog/commands/version.html)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/version-control.md`

Headings (5):
- # Version Control
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Develop with Skupper](./develop-skupper.md)
- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md)
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md)
- [human/skupper-docs/input/kube-yaml/custom-labels.md](../../human/skupper-docs/input/kube-yaml/custom-labels.md)
- [generated/skupper-ansible/skupper-ansible-overview.md](../skupper-ansible/skupper-ansible-overview.md)
- [generated/workflows/skupper-examples.md](../workflows/skupper-examples.md)
- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [Custom labels with YAML](https://skupper.io/docs/kube-yaml/custom-labels.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-docs-landscape/version-matrix.md`

Headings (5):
- # Version Matrix
- ## Appears in
- ## Sources
- ## Website Links
- ## Draft Notes

Links (10):
- [Skupper Reference](./skupper-reference.md)
- [human/skupper-docs/_source.md](../../human/skupper-docs/_source.md)
- [sources/skupper-docs.md](../../sources/skupper-docs.md)
- [sources/skupper-ansible.md](../../sources/skupper-ansible.md)
- [human/skupper-docs/input/refdog/commands/version.md](../../human/skupper-docs/input/refdog/commands/version.md)
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md)
- [Version command](https://skupperproject.github.io/refdog/commands/version.html)
- [Skupper docs repository](https://github.com/skupperproject/skupper-docs)
- [Skupper repository](https://github.com/skupperproject/skupper)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

Code blocks (0):
- None

## `generated/skupper-router/router-decisions-0001-record-architecture-decisions.md`

Headings (5):
- # 1. Record architecture decisions
- ## Status
- ## Context
- ## Decision
- ## Consequences

Links (2):
- [described by Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)
- [adr-tools](https://github.com/npryce/adr-tools)

Code blocks (0):
- None

## `generated/skupper-router/router-decisions-0002-remove-link-routing-from-the-router.md`

Headings (5):
- # 2. Remove Link-Routing from the router
- ## Status
- ## Context
- ## Decision
- ## Consequences

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-router/router-decisions-0003-move-router-annotations-to-custom-section.md`

Headings (5):
- # 3. Move per message router annotations
- ## Status
- ## Context
- ## Decision
- ## Consequences

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-router/router-docs-notes-code-conventions.md`

Headings (7):
- # Code conventions
- ## C conventions
- ### Usage of  (per-line formatting)
- ### Formatting tips
- ### Usage of  (whole-file formatting)
- ### Format style definition file
- ## Python conventions

Links (4):
- [](https://github.com/llvm/llvm-project/blob/main/clang/tools/clang-format/git-clang-format)
- [https://clang.llvm.org/docs/ClangFormatStyleOptions.html](https://clang.llvm.org/docs/ClangFormatStyleOptions.html)
- [https://clang.llvm.org/docs/ClangFormat.html](https://clang.llvm.org/docs/ClangFormat.html)
- [http://www.python.org/dev/peps/pep-0008/[PEP-8](http://www.python.org/dev/peps/pep-0008/[PEP-8)

Code blocks (6):
- `unspecified`
- `unspecified`
- `c`
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/skupper-router/router-docs-notes-connection-upgrade.md`

Headings (7):
- # Inter-Router Connection Upgrade
- ## Introduction
- ## Implementation
- ### Inter-Router Connector
- ### The Group Ordinal
- ### The Upgrade Process
- ### Extra Credit: The Inter-router Link Identifier

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-router/router-docs-notes-cross-network.md`

Headings (12):
- # Cross (Inter) Network Communication
- ## Use Cases
- ### Central Management of Networks
- ### Inter-Network Federation
- ## Setting up Cross-Network Connectivity
- ### Router Configuration
- ### Listener and Connector Configuration
- ### Exposing Services Cross-Network
- ### Using Dynamic Addresses
- ## A Complete Example
- ## Using Cross-Network Connectivity as an Endpoint
- ## Backward Compatibility

Links (0):
- None

Code blocks (5):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/skupper-router/router-docs-notes-edge-router-addr-proxy.md`

Headings (5):
- # Edge/Interior Address Tracking
- # Overview
- # Interior Router
- # Edge Router
- # Certificate Rotation

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-router/router-docs-notes-multi-key-tcp-listeners.md`

Headings (5):
- # Multi address tcp listeners
- ## Router Configuration
- ### Address selection strategy
- ### New listener address entity
- ## Implementation notes

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-router/router-docs-notes-resend-released.md`

Headings (5):
- # Overview
- # How the feature works
- # How to access the feature
- ## As a messaging client
- ## As an in-process adaptor

Links (0):
- None

Code blocks (0):
- None

## `generated/skupper-router/router-docs-notes-sarif.md`

Headings (2):
- # SARIF (Static Analysis Results Interchange Format)
- ## Helpful tooling

Links (5):
- [Introduction from Microsoft](https://github.com/microsoft/sarif-tutorials)
- [SARIF validator](https://sarifweb.azurewebsites.net/Validation)
- [SARIF multitool for merging and manipulating .sarif files](https://github.com/microsoft/sarif-sdk/blob/main/docs/multitool-usage.md)
- [GitHub action to invoke the tool](https://github.com/marketplace/actions/sarif-multitool)
- [GitHub documentation about importing SARIF results](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)

Code blocks (0):
- None

## `generated/skupper-router/router-docs-notes-streaming.md`

Headings (9):
- # Overview
- # Technical Considerations
- ## Link allocation for streaming deliveries
- ## Determining when a delivery must be streamed
- ## Flow control for streaming deliveries
- ### A proposed change to flow control
- # Controlling Streaming Behavior
- ## As a messaging client
- ## As an in-process adaptor

Links (1):
- [#1173](https://github.com/skupperproject/skupper-router/issues/1173)

Code blocks (1):
- `unspecified`

## `generated/skupper-router/router-tests-fuzz-README.md`

Headings (5):
- # Fuzz testing http1 and http2 adaptors in skupper-router
- ## Basics
- ## skupper-router/tests/fuzz/CMakeLists.txt
- ## Containerfile
- ## Building and running Containerfile

Links (4):
- [https://github.com/google/fuzzing/blob/master/docs/glossary.md](https://github.com/google/fuzzing/blob/master/docs/glossary.md)
- [https://llvm.org/docs/LibFuzzer.html](https://llvm.org/docs/LibFuzzer.html)
- [https://github.com/google/AFL](https://github.com/google/AFL)
- [https://github.com/google/oss-fuzz](https://github.com/google/oss-fuzz)

Code blocks (6):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/skupper-router/router-tools-scraper-README.md`

Headings (12):
- # Scraper - Analyze qpid-dispatch log files
- ## Apache License, Version 2.0
- ## Normal Mode
- ## Split Mode
- ## AMQP performative legend
- ## Sequence generator
- ## Quick Start
- ## Scraper command line
- ### Switch --skip-all-data
- ### Switch --skip-detail
- ### Switch --skip-msg-progress
- ### Advanced

Links (0):
- None

Code blocks (6):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/skupper-value-perspectives/access-tokens.md`

Headings (3):
- # Controlled Site Enrollment
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/adaptive-routing.md`

Headings (3):
- # Application-Aware Routing
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/bridge-network.md`

Headings (3):
- # Bridge Networking
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/business-continuity.md`

Headings (3):
- # Business Continuity
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/capacity-spillover.md`

Headings (3):
- # Hybrid-Cloud Capacity Spillover
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/client.md`

Headings (3):
- # Client
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/cloud-cost-flexibility.md`

Headings (3):
- # Cloud Cost & Capacity Flexibility
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/cluster-network.md`

Headings (3):
- # Cluster Networking
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/connector.md`

Headings (3):
- # Connector
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/console.md`

Headings (3):
- # Console & Status
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/container-host-platform.md`

Headings (3):
- # Container Host
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/container-runtime.md`

Headings (3):
- # Container Runtime Interface
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/containerd-runtime.md`

Headings (3):
- # containerd
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/credentials.md`

Headings (3):
- # Link Credentials
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/crio-runtime.md`

Headings (3):
- # CRI-O
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/cross-site-resilience.md`

Headings (3):
- # Cross-Site Resilience & Failover
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/delivery-velocity.md`

Headings (3):
- # Faster Application Delivery
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/desired-state.md`

Headings (3):
- # Desired Network State
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/docker.md`

Headings (3):
- # Docker
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/east-site.md`

Headings (3):
- # East site
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/faster-change.md`

Headings (3):
- # Faster Business & Technology Change
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/host-network.md`

Headings (3):
- # Host Networking
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/inter-site-link.md`

Headings (3):
- # Inter-site Link
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/kube-adaptor.md`

Headings (3):
- # Kubernetes Adaptor
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/kube-api.md`

Headings (3):
- # Kubernetes API
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/kubelet.md`

Headings (3):
- # Kubelet
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/kubernetes-platform.md`

Headings (3):
- # Kubernetes
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/link-token.md`

Headings (3):
- # Link Token
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/linux-host.md`

Headings (3):
- # Linux Host
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/listener-connector.md`

Headings (3):
- # Listeners & Connectors
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/listener.md`

Headings (3):
- # Listener
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/listeners-connectors.md`

Headings (3):
- # Listeners & Connectors
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/local-platforms.md`

Headings (3):
- # Docker, Podman & Linux Systems
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/location-independence.md`

Headings (3):
- # Location-Independent Applications
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/market-reach.md`

Headings (3):
- # Faster Regional & Market Expansion
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/metrics.md`

Headings (3):
- # Metrics
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/migration-flexibility.md`

Headings (3):
- # Incremental Cloud Migration
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/mtls.md`

Headings (3):
- # Mutual TLS Protection
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/multi-site-services.md`

Headings (3):
- # Multi-Site Application Services
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/mutual-tls.md`

Headings (3):
- # Mutual TLS
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/network-intent.md`

Headings (3):
- # Network Intent Translation
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/network-reachability.md`

Headings (3):
- # Network Reachability
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/oci-runtime.md`

Headings (3):
- # OCI Runtime
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/ocp-platform.md`

Headings (3):
- # OpenShift Container Platform
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/openshift.md`

Headings (3):
- # OpenShift
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/platform.md`

Headings (3):
- # Platform
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/platform1.md`

Headings (3):
- # Platform
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/podman.md`

Headings (3):
- # Podman
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/reduced-integration-risk.md`

Headings (3):
- # Reduced Integration Risk
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/regional-deployment.md`

Headings (3):
- # Distributed Regional Deployment
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/route-discovery.md`

Headings (3):
- # Route Discovery
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/route-scc.md`

Headings (3):
- # Routes & SCC
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/router-api.md`

Headings (3):
- # Router API
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/router-core.md`

Headings (3):
- # Router Core
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/router.md`

Headings (3):
- # Skupper Router
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/routing-key.md`

Headings (3):
- # Routing Key
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/routing-keys.md`

Headings (3):
- # Application-Layer Service Addressing
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/routing-stack.md`

Headings (3):
- # Routing Stack
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/secret-store.md`

Headings (3):
- # Secret Store
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/secure-connectivity.md`

Headings (3):
- # Secure Private Application Connectivity
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/secure-transport.md`

Headings (3):
- # Secure Transport
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/server.md`

Headings (3):
- # Server
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/service-binding.md`

Headings (3):
- # Service Binding
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/service-connectivity.md`

Headings (3):
- # Transparent Service-to-Service Connectivity
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/service-exposure.md`

Headings (3):
- # Service Exposure
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/service-failover.md`

Headings (3):
- # Cross-Site Load Balancing & Failover
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/service-routing.md`

Headings (3):
- # Service Routing
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/service-sync.md`

Headings (3):
- # Service Sync
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/site-control-plane.md`

Headings (3):
- # Site Control Plane
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/site-controller.md`

Headings (3):
- # Site Controller
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/site-identity.md`

Headings (3):
- # Site Identity
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/site-linking.md`

Headings (3):
- # Site Linking
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/site-links.md`

Headings (3):
- # Secure Site-to-Site Links
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/site-router.md`

Headings (3):
- # Site Router
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/site-runtime.md`

Headings (3):
- # Site Runtime
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/skupper-application-engineering-pov.md`

Headings (3):
- # Declarative Application Networking
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/skupper-config.md`

Headings (3):
- # Skupper Configuration
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/skupper-network-engineering-pov.md`

Headings (3):
- # Cross-Platform Connectivity
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/skupper-platform-choices.md`

Headings (3):
- # Site Platform Choice
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/skupper-router.md`

Headings (3):
- # Skupper Router
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/skupper-site.md`

Headings (3):
- # Skupper Site
- ## Appears in
- ## Notes

Links (1):
- [Application Engineering POV - Skupper Layered Connectivity](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/skupper-sites.md`

Headings (3):
- # Skupper Sites
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/systemd.md`

Headings (3):
- # Systemd
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/tls-identity.md`

Headings (3):
- # TLS Identity
- ## Appears in
- ## Notes

Links (1):
- [Skupper Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/west-site.md`

Headings (3):
- # West site
- ## Appears in
- ## Notes

Links (1):
- [Network Engineering POV - Site Platform Choices](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/skupper-value-perspectives/workload-placement.md`

Headings (3):
- # Workload Placement Freedom
- ## Appears in
- ## Notes

Links (1):
- [Skupper Business Value Chain](./skupper-value-perspectives.md)

Code blocks (0):
- None

## `generated/vms/access-point-deployment.md`

Headings (5):
- # Access Point Deployment
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Access Point Push](./access-point-push.md)

Code blocks (0):
- None

## `generated/vms/access-point-management.md`

Headings (5):
- # Access Point Management
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Network Topology Management](./vms-overview.md)
- [Access Point](./access-point.md)

Code blocks (0):
- None

## `generated/vms/access-point-push.md`

Headings (5):
- # Access Point Push
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Management Controller](./management-controller.md)

Code blocks (0):
- None

## `generated/vms/access-point.md`

Headings (8):
- # Access Point
- ## Appears in
- ## Topics
- ### Dependencies
- ## Access Point Types
- ### Configuration
- ### Sync Process
- ## Source

Links (2):
- [VMS Network Topology Management](./vms-overview.md)
- [Backbone Site](./backbone-site.md)

Code blocks (0):
- None

## `generated/vms/auto-cert-distribution.md`

Headings (11):
- # Automatic Certificate Distribution
- ## Appears in
- ## Topics
- ### Dependencies
- ## Automatic Certificate Distribution
- ### Distribution Methods
- ### In-band Delivery
- ### Sync Mechanism
- ### Contrast with Manual Distribution
- ### Security Properties
- ## Source

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [In-band Certificate Delivery](./in-band-delivery.md)

Code blocks (0):
- None

## `generated/vms/auto-cert-generation.md`

Headings (9):
- # Automatic Certificate Generation
- ## Appears in
- ## Topics
- ### Dependencies
- ## Certificate Engine
- ### Responsibilities
- ### Integration with cert-manager
- ### No Manual CSR/Signing
- ## Source

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [cert-manager](./cert-manager-integration.md)

Code blocks (0):
- None

## `generated/vms/auto-cert-rotation.md`

Headings (10):
- # Automatic Certificate Rotation
- ## Appears in
- ## Topics
- ### Dependencies
- ## Certificate Rotation
- ### Rotation Architecture
- ### Rotation Ordinals
- ### SSL Profile Management
- ### Zero Downtime
- ## Source

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [Rotation Monitoring](./rotation-monitoring.md)

Code blocks (0):
- None

## `generated/vms/automatic-site-registration.md`

Headings (4):
- # Automatic Site Registration
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Network Topology Management](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/backbone-admin.md`

Headings (11):
- # Backbone Administrator
- ## Appears in
- ## Topics
- ## Backbone Administrator Persona
- ### Responsibilities
- ### Access Level
- ### Typical Workflows
- ### Delegation Model
- ### Tools
- ### Differences from Service Admin
- ## Source

Links (1):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/backbone-ca.md`

Headings (12):
- # Backbone CA
- ## Appears in
- ## Topics
- ### Dependencies
- ## Backbone CA
- ### Certificate Hierarchy Position
- ### Created Automatically
- ### Signing Authority
- ### Multi-tenancy Enabler
- ### Backbone-level Eviction
- ### Integration with Customer PKI
- ## Source

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [External Root CA](./external-root-ca.md)

Code blocks (1):
- `unspecified`

## `generated/vms/backbone-links.md`

Headings (11):
- # Backbone Links
- ## Appears in
- ## Topics
- ### Dependencies
- ## Backbone Links
- ### Link Configuration
- ### Sync to Sites
- ### Cost-weighted Routing
- ### Link Creation Workflow
- ### Topology Planning
- ## Source

Links (2):
- [VMS Network Topology Management](./vms-overview.md)
- [Backbone Site](./backbone-site.md)

Code blocks (1):
- `yaml`

## `generated/vms/backbone-network.md`

Headings (9):
- # Backbone Network
- ## Appears in
- ## Topics
- ### Dependencies
- ## Network Topology Model
- ### Network Topology
- ### Multi-tenant Constellation
- ### Backbone Components
- ## Source

Links (2):
- [VMS Network Topology Management](./vms-overview.md)
- [Skupper Router Network](./skupper-router.md)

Code blocks (0):
- None

## `generated/vms/backbone-provisioning.md`

Headings (9):
- # Backbone Provisioning
- ## Appears in
- ## Topics
- ### Dependencies
- ## Backbone Provisioning
- ### Provisioning Steps
- ### Design Considerations
- ### Centralized vs. Distributed
- ## Source

Links (4):
- [VMS Network Topology Management](./vms-overview.md)
- [Backbone Network](./backbone-network.md)
- [Backbone Site](./backbone-site.md)
- [Backbone Links](./backbone-links.md)

Code blocks (0):
- None

## `generated/vms/backbone-site-cert.md`

Headings (5):
- # Backbone Site Certificate
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [Backbone CA](./backbone-ca.md)

Code blocks (0):
- None

## `generated/vms/backbone-site.md`

Headings (13):
- # Backbone Site
- ## Appears in
- ## Topics
- ### Dependencies
- ## Backbone Site
- ### Purpose
- ### Deployment
- ### Access Points
- ### Strategic Placement
- ### Bootstrap Process
- ### State Synchronization
- ### Lifecycle States
- ## Source

Links (2):
- [VMS Network Topology Management](./vms-overview.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/bootstrap-yaml.md`

Headings (4):
- # Backbone Bootstrap YAML
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Network Topology Management](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/central-member-visibility.md`

Headings (5):
- # Central Member Visibility
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Member Monitoring](./member-monitoring.md)

Code blocks (0):
- None

## `generated/vms/centralized-management.md`

Headings (11):
- # Centralized Control
- ## Appears in
- ## Topics
- ### Dependencies
- ## Centralized Control
- ### Management Plane Components
- ### What Gets Centralized
- ### Benefits vs. Distributed Administration
- ### Deployment Flexibility
- ### API-Driven
- ## Source

Links (2):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)
- [Control & Data Plane Architecture](./vms-architecture.md)

Code blocks (0):
- None

## `generated/vms/centralized-topology-control.md`

Headings (5):
- # Centralized Topology Control
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Network Topology Management](./vms-overview.md)
- [Management Controller](./management-controller.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/centralized-topology-visibility.md`

Headings (11):
- # Centralized Topology Visibility
- ## Appears in
- ## Topics
- ### Dependencies
- ## Centralized Topology Visibility
- ### What's Visible
- ### Contrast with Distributed Skupper
- ### Data Sources
- ### User Interfaces
- ### Operational Benefits
- ## Source

Links (2):
- [VMS Network Topology Management](./vms-overview.md)
- [Topology State Store](./topology-state-store.md)

Code blocks (0):
- None

## `generated/vms/cert-manager-integration.md`

Headings (12):
- # cert-manager
- ## Appears in
- ## Topics
- ## cert-manager Integration
- ### Architecture
- ### Integration Flow
- ### Certificate Types
- ### Namespace Requirement
- ### Deployment
- ### Customer PKI Integration
- ### Automatic Operations
- ## Source

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (1):
- `yaml`

## `generated/vms/cert-manager.md`

Headings (5):
- # cert-manager
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Management Controller](./management-controller.md)

Code blocks (0):
- None

## `generated/vms/cert-revocation.md`

Headings (5):
- # Certificate Revocation
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [Revocation Enforcement](./revocation-enforcement.md)

Code blocks (0):
- None

## `generated/vms/cert-validity-periods.md`

Headings (5):
- # Certificate Validity Periods
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [VAN CA](./van-ca.md)

Code blocks (0):
- None

## `generated/vms/claim-redemption-handler.md`

Headings (5):
- # Claim Redemption Handler
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/claim-redemption.md`

Headings (9):
- # Claim Redemption Protocol
- ## Appears in
- ## Topics
- ### Dependencies
- ## Claim Redemption Protocol
- ### Bootstrapping Sequence
- ### Restricted Access
- ### In-band Delivery
- ## Source

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Invitation Claim Certificate](./invitation-claim-cert.md)

Code blocks (0):
- None

## `generated/vms/config-push.md`

Headings (5):
- # Configuration Push
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Management Controller](./management-controller.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/cost-weighted-routing.md`

Headings (5):
- # Cost-weighted Routing
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Network Topology Management](./vms-overview.md)
- [Backbone Links](./backbone-links.md)
- [Skupper Router Network](./skupper-router.md)

Code blocks (0):
- None

## `generated/vms/data-plane-communication.md`

Headings (5):
- # Data Plane Communication
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Skupper Router Network](./skupper-router.md)

Code blocks (0):
- None

## `generated/vms/decoupled-data-plane.md`

Headings (5):
- # Decoupled Data Plane
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Skupper Router Network](./skupper-router.md)

Code blocks (0):
- None

## `generated/vms/distributed-trust.md`

Headings (4):
- # Distributed Domain of Trust
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/dmz-deployment.md`

Headings (4):
- # DMZ Deployment
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Control & Data Plane Architecture](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/dmz-relay-support.md`

Headings (5):
- # DMZ Relay Support
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Network Topology Management](./vms-overview.md)
- [Backbone Site](./backbone-site.md)

Code blocks (0):
- None

## `generated/vms/external-root-ca.md`

Headings (4):
- # External Root CA
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/frictionless-participation.md`

Headings (5):
- # Frictionless Participation
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Invitation Flow](./invitation-flow.md)
- [Claim Redemption Protocol](./claim-redemption.md)

Code blocks (0):
- None

## `generated/vms/helmfile-deployment.md`

Headings (10):
- # Helmfile Deployment
- ## Appears in
- ## Topics
- ## Helmfile Deployment
- ### Charts Installed
- ### Prerequisites
- ### Required Secrets
- ### Configuration
- ### Deployment
- ## Source

Links (1):
- [VMS Control & Data Plane Architecture](./vms-overview.md)

Code blocks (3):
- `shell`
- `shell`
- `shell`

## `generated/vms/hierarchical-isolation.md`

Headings (5):
- # Hierarchical Isolation
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/in-band-delivery.md`

Headings (4):
- # In-band Certificate Delivery
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/in-band-management.md`

Headings (10):
- # In-band Management
- ## Appears in
- ## Topics
- ### Dependencies
- ## In-band Management
- ### Architecture
- ### Communication Flow
- ### Benefits
- ### Contrast with Management Plane Location
- ## Source

Links (3):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Site Controller](./site-controller.md)
- [Data Plane Communication](./data-plane-communication.md)

Code blocks (0):
- None

## `generated/vms/in-band-registration.md`

Headings (5):
- # In-band Registration
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Data Plane Communication](./data-plane-communication.md)

Code blocks (0):
- None

## `generated/vms/ingress-discovery.md`

Headings (11):
- # Ingress Discovery
- ## Appears in
- ## Topics
- ## Ingress Discovery
- ### The Problem
- ### Discovery Process
- ### Ingress Data Format
- ### Automation Opportunity
- ### Why This Matters
- ### Cluster Networking Adaptation
- ## Source

Links (1):
- [VMS Network Topology Management](./vms-overview.md)

Code blocks (2):
- `unspecified`
- `bash`

## `generated/vms/ingress-upload.md`

Headings (5):
- # Ingress Upload
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/instance-limit.md`

Headings (4):
- # Instance Limit
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Application Network Lifecycle](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/instant-access-revocation.md`

Headings (5):
- # Instant Access Revocation
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Security & PKI](./vms-overview.md)
- [Subtree Invalidation](./subtree-invalidation.md)
- [Certificate Revocation](./cert-revocation.md)

Code blocks (0):
- None

## `generated/vms/instant-eviction.md`

Headings (11):
- # Instant Eviction
- ## Appears in
- ## Topics
- ### Dependencies
- ## Instant Eviction
- ### VAN Eviction
- ### Member Eviction
- ### Certificate-based Enforcement
- ### Contrast with Manual Skupper
- ### Use Cases
- ## Source

Links (3):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)
- [Security & PKI](./vms-security-pki.md)
- [Application Network Lifecycle](./vms-application-lifecycle.md)

Code blocks (0):
- None

## `generated/vms/instant-teardown.md`

Headings (5):
- # Instant Teardown
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [VAN Eviction](./van-eviction.md)
- [Member Eviction](./member-eviction.md)

Code blocks (0):
- None

## `generated/vms/inter-router-links.md`

Headings (5):
- # Inter-router Links
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Skupper Router Network](./skupper-router.md)

Code blocks (0):
- None

## `generated/vms/invitation-based-access.md`

Headings (13):
- # Invitation-based Access
- ## Appears in
- ## Topics
- ### Dependencies
- ## Invitation-based Access
- ### Video Conference Analogy
- ### Workflow Simplicity
- ### Invitation Properties
- ### Distribution Flexibility
- ### No Central Authentication
- ### Scalability
- ### Security Model
- ## Source

Links (2):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)
- [Application Network Lifecycle](./vms-application-lifecycle.md)

Code blocks (0):
- None

## `generated/vms/invitation-claim-cert.md`

Headings (5):
- # Invitation Claim Certificate
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [VAN CA](./van-ca.md)

Code blocks (0):
- None

## `generated/vms/invitation-creation.md`

Headings (4):
- # Invitation Creation
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Application Network Lifecycle](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/invitation-deadline.md`

Headings (4):
- # Invitation Deadline
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Application Network Lifecycle](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/invitation-flow.md`

Headings (9):
- # Invitation Flow
- ## Appears in
- ## Topics
- ### Dependencies
- ## Invitation-based Participation
- ### Invitation Workflow
- ### Invitation Properties
- ### Security Model
- ## Source

Links (3):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Invitation Creation](./invitation-creation.md)
- [Invitation YAML Generation](./invitation-yaml-generation.md)

Code blocks (0):
- None

## `generated/vms/invitation-yaml-generation.md`

Headings (5):
- # Invitation YAML Generation
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Invitation Claim Certificate](./invitation-claim-cert.md)

Code blocks (0):
- None

## `generated/vms/invitation-yaml.md`

Headings (4):
- # Invitation YAML
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Control & Data Plane Architecture](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/keycloak.md`

Headings (10):
- # Keycloak
- ## Appears in
- ## Topics
- ### Dependencies
- ## Keycloak
- ### Integration
- ### Configuration Steps
- ### Authentication Flow
- ### Who Needs Keycloak
- ## Source

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Management Controller](./management-controller.md)

Code blocks (0):
- None

## `generated/vms/kubernetes-management.md`

Headings (4):
- # Kubernetes Management Plane
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Control & Data Plane Architecture](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/local-access-point-deployment.md`

Headings (5):
- # Local Access Point Deployment
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/logically-centralized-control.md`

Headings (5):
- # Logically Centralized Control
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Management Controller](./management-controller.md)
- [PostgreSQL Database](./postgresql.md)

Code blocks (0):
- None

## `generated/vms/management-controller.md`

Headings (7):
- # Management Controller
- ## Appears in
- ## Topics
- ## Management Controller
- ### REST API
- ### Architecture
- ## Source

Links (1):
- [VMS Control & Data Plane Architecture](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/member-cert-issuance.md`

Headings (5):
- # Member Certificate Issuance
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Claim Redemption Protocol](./claim-redemption.md)

Code blocks (0):
- None

## `generated/vms/member-eviction.md`

Headings (5):
- # Member Eviction
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Certificate Revocation](./cert-revocation.md)

Code blocks (0):
- None

## `generated/vms/member-monitoring.md`

Headings (5):
- # Member Monitoring
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/member-site-cert.md`

Headings (5):
- # Member Site Certificate
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [VAN CA](./van-ca.md)

Code blocks (0):
- None

## `generated/vms/multi-platform-sites.md`

Headings (5):
- # Multi-platform Sites
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/multi-tenancy.md`

Headings (9):
- # Multi-tenant Isolation
- ## Appears in
- ## Topics
- ### Dependencies
- ## Multi-tenant Isolation
- ### How Multi-tenancy Works
- ### Isolation Properties
- ### Backbone Configuration
- ## Source

Links (3):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)
- [Network Topology Management](./vms-network-topology.md)
- [Security & PKI](./vms-security-pki.md)

Code blocks (1):
- `unspecified`

## `generated/vms/multi-tenant-data-plane.md`

Headings (5):
- # Multi-tenant Data Plane
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Skupper Router Network](./skupper-router.md)

Code blocks (0):
- None

## `generated/vms/multi-tenant-routing.md`

Headings (5):
- # Multi-tenant Routing
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Network Topology Management](./vms-overview.md)
- [Skupper Router Network](./skupper-router.md)

Code blocks (0):
- None

## `generated/vms/network-isolation.md`

Headings (4):
- # Isolated Application Networks
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/no-participant-auth.md`

Headings (4):
- # No Participant Authentication
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/optimized-backbone-paths.md`

Headings (5):
- # Optimized Backbone Paths
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Network Topology Management](./vms-overview.md)
- [Backbone Links](./backbone-links.md)
- [Cost-weighted Routing](./cost-weighted-routing.md)

Code blocks (0):
- None

## `generated/vms/out-of-band-bootstrap.md`

Headings (5):
- # Out-of-band Bootstrap
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Bootstrap YAML Generation](./bootstrap-yaml.md)
- [Invitation YAML](./invitation-yaml.md)

Code blocks (0):
- None

## `generated/vms/participant-onboarding.md`

Headings (5):
- # Participant Onboarding
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [Claim Redemption Protocol](./claim-redemption.md)
- [Member Certificate Issuance](./member-cert-issuance.md)

Code blocks (0):
- None

## `generated/vms/participant.md`

Headings (11):
- # Participant
- ## Appears in
- ## Topics
- ## Participant Persona
- ### Responsibilities
- ### Access Level
- ### Invitation-based Onboarding
- ### Typical Workflows
- ### Tools
- ### Security Model
- ## Source

Links (1):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/pki-integration.md`

Headings (5):
- # Customer PKI Integration
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [External Root CA](./external-root-ca.md)

Code blocks (0):
- None

## `generated/vms/platform-flexibility.md`

Headings (5):
- # Platform Flexibility
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Site Controller](./site-controller.md)
- [Skupper Router Network](./skupper-router.md)

Code blocks (0):
- None

## `generated/vms/postgresql.md`

Headings (12):
- # PostgreSQL Database
- ## Appears in
- ## Topics
- ### Dependencies
- ## PostgreSQL Database
- ### Schema
- ### Deployment
- ### Database Users
- ### Access
- ### State Management
- ### Maintenance
- ## Source

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Management Controller](./management-controller.md)

Code blocks (1):
- `shell`

## `generated/vms/revocation-enforcement.md`

Headings (4):
- # Revocation Enforcement
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/rotation-monitoring.md`

Headings (4):
- # Rotation Monitoring
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/self-service-vans.md`

Headings (5):
- # Self-service VANs
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [VAN Creation](./van-creation.md)

Code blocks (0):
- None

## `generated/vms/service-admin.md`

Headings (9):
- # Service Administrator
- ## Appears in
- ## Topics
- ## Service Administrator Persona
- ### Responsibilities
- ### Access Level
- ### Typical Workflows
- ### Tools
- ## Source

Links (1):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/service-connectors.md`

Headings (13):
- # Service Connectors
- ## Appears in
- ## Topics
- ### Dependencies
- ## Service Connectors
- ### Purpose
- ### How Connectors Work
- ### Connector Configuration
- ### VAN Access Pattern
- ### Multiple Connectors
- ### Deployment
- ### Example Use Case
- ## Source

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Skupper Router Network](./skupper-router.md)

Code blocks (1):
- `unspecified`

## `generated/vms/service-listeners.md`

Headings (14):
- # Service Listeners
- ## Appears in
- ## Topics
- ### Dependencies
- ## Service Listeners
- ### Purpose
- ### How Listeners Work
- ### Listener Configuration
- ### VAN Access Pattern
- ### Multiple Connectors
- ### Deployment
- ### Example Use Case
- ### Service Discovery
- ## Source

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Skupper Router Network](./skupper-router.md)

Code blocks (1):
- `unspecified`

## `generated/vms/shared-relay-infrastructure.md`

Headings (5):
- # Shared Relay Infrastructure
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Network Topology Management](./vms-overview.md)
- [Backbone Network](./backbone-network.md)
- [Multi-tenant Routing](./multi-tenant-routing.md)

Code blocks (0):
- None

## `generated/vms/site-bootstrapping.md`

Headings (8):
- # Site Bootstrapping
- ## Appears in
- ## Topics
- ### Dependencies
- ## Bootstrap Process
- ### Eligibility
- ### Three-Step Process
- ## Source

Links (3):
- [VMS Network Topology Management](./vms-overview.md)
- [Bootstrap YAML Generation](./bootstrap-yaml.md)
- [Ingress Discovery](./ingress-discovery.md)

Code blocks (3):
- `unspecified`
- `unspecified`
- `unspecified`

## `generated/vms/site-controller.md`

Headings (8):
- # Site Controller
- ## Appears in
- ## Topics
- ## Site Controller
- ### Responsibilities
- ### Deployment Artifacts
- ### State Synchronization
- ## Source

Links (1):
- [VMS Control & Data Plane Architecture](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/site-heartbeat.md`

Headings (5):
- # Site Heartbeat
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/site-local-api.md`

Headings (5):
- # Site Local API
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/site-orchestration.md`

Headings (5):
- # Site Orchestration
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Site Controller](./site-controller.md)

Code blocks (0):
- None

## `generated/vms/skupper-router.md`

Headings (10):
- # Skupper Router Network
- ## Appears in
- ## Topics
- ## Skupper Router Network
- ### Data Plane Architecture
- ### Multi-tenancy
- ### Narrow Coupling
- ### Router Configuration
- ### Integration Points
- ## Source

Links (1):
- [VMS Control & Data Plane Architecture](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/subtree-invalidation.md`

Headings (5):
- # Subtree Invalidation
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/temporal-access-enforcement.md`

Headings (5):
- # Temporal Access Enforcement
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [Certificate Validity Periods](./cert-validity-periods.md)

Code blocks (0):
- None

## `generated/vms/time-boxed-access.md`

Headings (5):
- # Time-boxed Access
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (3):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [VAN Lifecycle](./van-lifecycle.md)
- [Invitation Deadline](./invitation-deadline.md)

Code blocks (0):
- None

## `generated/vms/tls-everywhere.md`

Headings (4):
- # Mutual TLS Everywhere
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Security & PKI](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/topology-abstraction.md`

Headings (11):
- # Topology Abstraction
- ## Appears in
- ## Topics
- ### Dependencies
- ## Topology Abstraction
- ### Separation of Concerns
- ### VAN Owner Experience
- ### Automatic Routing
- ### Benefits
- ### Contrast with Manual Skupper
- ## Source

Links (2):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)
- [Network Topology Management](./vms-network-topology.md)

Code blocks (0):
- None

## `generated/vms/topology-state-store.md`

Headings (4):
- # Topology State Store
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [VMS Network Topology Management](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/van-ca.md`

Headings (10):
- # VAN CA
- ## Appears in
- ## Topics
- ### Dependencies
- ## VAN Certificate Authority
- ### Certificate Hierarchy Position
- ### Lifecycle
- ### Signing Authority
- ### Isolation
- ## Source

Links (2):
- [VMS Security & PKI](./vms-overview.md)
- [Backbone CA](./backbone-ca.md)

Code blocks (1):
- `unspecified`

## `generated/vms/van-creation.md`

Headings (12):
- # VAN Creation
- ## Appears in
- ## Topics
- ### Dependencies
- ## VAN Creation
- ### Creation Process
- ### VAN Properties
- ### Certificate Authority Timing
- ### Lifecycle States
- ### Permissions
- ### After Creation
- ## Source

Links (1):
- [VMS Application Network Lifecycle](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/van-eviction.md`

Headings (5):
- # VAN Eviction
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (1):
- [VMS Application Network Lifecycle](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/van-lifecycle.md`

Headings (5):
- # VAN Lifecycle
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Application Network Lifecycle](./vms-overview.md)
- [VAN CA](./van-ca.md)

Code blocks (0):
- None

## `generated/vms/van-user.md`

Headings (11):
- # VAN User
- ## Appears in
- ## Topics
- ## VAN User Persona
- ### Responsibilities
- ### Access Level
- ### Typical Workflows
- ### Permissions Model
- ### Tools
- ### What VAN Users Don't Need
- ## Source

Links (1):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/vms-api.md`

Headings (5):
- # VMS REST API
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Management Controller](./management-controller.md)

Code blocks (0):
- None

## `generated/vms/vms-application-lifecycle.md`

Headings (4):
- # Application Network Lifecycle
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/vms-architecture.md`

Headings (4):
- # Control & Data Plane Architecture
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/vms-console.md`

Headings (11):
- # VMS Console
- ## Appears in
- ## Topics
- ### Dependencies
- ## VMS Console
- ### Features
- ### Navigation Structure
- ### Architecture
- ### Technology Stack
- ### Running the Console
- ## Source

Links (2):
- [VMS Control & Data Plane Architecture](./vms-overview.md)
- [Management Controller](./management-controller.md)

Code blocks (1):
- `shell`

## `generated/vms/vms-network-topology.md`

Headings (4):
- # Network Topology Management
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/vms-security-pki.md`

Headings (4):
- # Security & PKI
- ## Appears in
- ## Topics
- ## Notes

Links (1):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)

Code blocks (0):
- None

## `generated/vms/zero-touch-cert-lifecycle.md`

Headings (5):
- # Zero-touch Certificate Lifecycle
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (4):
- [VMS Security & PKI](./vms-overview.md)
- [Automatic Certificate Generation](./auto-cert-generation.md)
- [Automatic Certificate Distribution](./auto-cert-distribution.md)
- [Automatic Certificate Rotation](./auto-cert-rotation.md)

Code blocks (0):
- None

## `generated/vms/zero-touch-certificates.md`

Headings (5):
- # Zero-touch Certificate Lifecycle
- ## Appears in
- ## Topics
- ### Dependencies
- ## Notes

Links (2):
- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md)
- [Security & PKI](./vms-security-pki.md)

Code blocks (0):
- None

## `generated/workflows/skupper-examples.md`

Headings (5):
- # Skupper example applications
- ## Example scenarios
- ## Hello World
- ## gRPC / Online Boutique
- ## How to use these examples

Links (7):
- [skupper-plain](https://pwright.github.io/webernetes/?scenario=skupper-plain)
- [skupper-grpc](https://pwright.github.io/webernetes/?scenario=skupper-grpc)
- [https://pwright.github.io/webernetes/?scenario=skupper-plain](https://pwright.github.io/webernetes/?scenario=skupper-plain)
- [https://pwright.github.io/webernetes/?scenario=skupper-grpc](https://pwright.github.io/webernetes/?scenario=skupper-grpc)
- [Skupper overview](../input/overview/index.md)
- [Installation guide](../input/install/index.md)
- [Getting started with Kubernetes CLI](../input/kube-cli/index.md)

Code blocks (2):
- `text`
- `text`
