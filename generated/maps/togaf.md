---
title: "Togaf"
type: BlockscapeMap
status: generated
source_path: maps/togaf.bs
tags:
  - skupper
  - blockscape
---

# Togaf

Edit: [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/togaf.bs)

```bs full
[
  {
    "id": "togaf-skupper-solution-patterns",
    "title": "TOGAF Patterns Enabled by a Skupper Network",
    "abstract": "Architecture patterns in which location-independent application connectivity is part of the solution. The upper categories describe architecture outcomes and reusable patterns. Lower categories show the connectivity capabilities and Skupper solution building blocks that can realize those patterns without making Skupper the complete solution.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/architecture/togaf-overview.md",
      "generated/architecture/service-virtualization.md",
      "generated/architecture/integration-layer.md",
      "generated/architecture/boundaryless-information-flow.md",
      "generated/architecture/independent-service-placement.md",
      "generated/architecture/hybrid-cloud-elasticity.md",
      "generated/architecture/legacy-modernization.md",
      "generated/architecture/resilient-service-instances.md"
    ],
    "categories": [
      {
        "id": "architecture-outcomes",
        "title": "Architecture Outcomes",
        "items": [
          {
            "id": "location-independent-services",
            "name": "Location-independent services",
            "deps": [
              "service-virtualization",
              "independent-service-placement"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#location-independent-services"
          },
          {
            "id": "boundaryless-applications",
            "name": "Boundaryless applications",
            "deps": [
              "boundaryless-information-flow",
              "integration-layer"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#boundaryless-applications"
          },
          {
            "id": "deployment-freedom",
            "name": "Deployment freedom",
            "deps": [
              "independent-service-placement",
              "hybrid-cloud-elasticity"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#deployment-freedom"
          },
          {
            "id": "incremental-modernization",
            "name": "Incremental modernization",
            "deps": [
              "legacy-modernization"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#incremental-modernization"
          },
          {
            "id": "cross-location-resilience",
            "name": "Cross-location resilience",
            "deps": [
              "resilient-service-instances",
              "hybrid-cloud-elasticity"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#cross-location-resilience"
          },
          {
            "id": "infrastructure-decoupling",
            "name": "Application topology decoupled from infrastructure topology",
            "deps": [
              "service-virtualization",
              "integration-layer"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#infrastructure-decoupling"
          }
        ]
      },
      {
        "id": "patterns",
        "title": "Architecture Patterns",
        "items": [
          {
            "id": "service-virtualization",
            "name": "Service Virtualization / Location Transparency",
            "deps": [
              "logical-service-identity",
              "endpoint-abstraction",
              "location-transparent-routing"
            ],
            "source": "generated/architecture/service-virtualization.md",
            "external": "https://www.opengroup.org/soa/source-book/soa_refarch/p13.htm"
          },
          {
            "id": "integration-layer",
            "name": "Integration Layer",
            "deps": [
              "service-connectivity",
              "cross-boundary-routing",
              "secure-transport"
            ],
            "source": "generated/architecture/integration-layer.md",
            "external": "https://www.opengroup.org/soa/source-book/togaf/p4.htm"
          },
          {
            "id": "boundaryless-information-flow",
            "name": "Boundaryless Information Flow",
            "deps": [
              "cross-boundary-routing",
              "platform-independent-connectivity",
              "secure-transport"
            ],
            "source": "generated/architecture/boundaryless-information-flow.md",
            "external": "https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm"
          },
          {
            "id": "independent-service-placement",
            "name": "Independent Microservice Placement",
            "deps": [
              "logical-service-identity",
              "platform-independent-connectivity",
              "location-transparent-routing"
            ],
            "source": "generated/architecture/independent-service-placement.md",
            "external": "https://www.opengroup.org/soa/source-book/msawp/p2.htm"
          },
          {
            "id": "hybrid-cloud-elasticity",
            "name": "Hybrid-cloud Elasticity",
            "deps": [
              "multi-location-service",
              "cross-boundary-routing",
              "connection-distribution",
              "location-preference"
            ],
            "source": "generated/architecture/hybrid-cloud-elasticity.md",
            "external": "https://www.opengroup.org/soa/source-book/msawp/p2.htm"
          },
          {
            "id": "legacy-modernization",
            "name": "Legacy Modernization / Wrapper",
            "deps": [
              "private-service-access",
              "platform-independent-connectivity",
              "endpoint-abstraction"
            ],
            "source": "generated/architecture/legacy-modernization.md",
            "external": "https://www.opengroup.org/soa/source-book/togaf/p4.htm"
          },
          {
            "id": "resilient-service-instances",
            "name": "Resilient Parallel Service Instances",
            "deps": [
              "multi-location-service",
              "connection-distribution",
              "service-failover"
            ],
            "source": "generated/architecture/resilient-service-instances.md",
            "external": "https://www.opengroup.org/soa/source-book/msawp/p2.htm"
          }
        ]
      },
      {
        "id": "architecture-capabilities",
        "title": "Required Connectivity Capabilities",
        "items": [
          {
            "id": "logical-service-identity",
            "name": "Logical service identity",
            "deps": [
              "routing-key"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#logical-service-identity"
          },
          {
            "id": "endpoint-abstraction",
            "name": "Endpoint abstraction",
            "deps": [
              "listener",
              "connector",
              "routing-key"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#endpoint-abstraction"
          },
          {
            "id": "service-connectivity",
            "name": "Application service connectivity",
            "deps": [
              "listener",
              "connector"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#service-connectivity"
          },
          {
            "id": "location-transparent-routing",
            "name": "Location-transparent routing",
            "deps": [
              "routing-key",
              "skupper-router"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#location-transparent-routing"
          },
          {
            "id": "cross-boundary-routing",
            "name": "Cross-boundary routing",
            "deps": [
              "site-link",
              "skupper-router"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#cross-boundary-routing"
          },
          {
            "id": "secure-transport",
            "name": "Secure transport between locations",
            "deps": [
              "site-link",
              "skupper-router"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#secure-transport"
          },
          {
            "id": "platform-independent-connectivity",
            "name": "Platform-independent connectivity",
            "deps": [
              "listener",
              "connector"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#platform-independent-connectivity"
          },
          {
            "id": "private-service-access",
            "name": "Private service access without public exposure",
            "deps": [
              "listener",
              "connector",
              "site-link"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#private-service-access"
          },
          {
            "id": "multi-location-service",
            "name": "One logical service across locations",
            "deps": [
              "routing-key",
              "connector",
              "skupper-router"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#multi-location-service"
          },
          {
            "id": "connection-distribution",
            "name": "Connection distribution",
            "deps": [
              "skupper-router",
              "connector"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#connection-distribution"
          },
          {
            "id": "service-failover",
            "name": "Service instance failover",
            "deps": [
              "skupper-router",
              "multi-provider-routing"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#service-failover"
          },
          {
            "id": "location-preference",
            "name": "Location preference",
            "deps": [
              "skupper-router",
              "routing-cost"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#location-preference"
          }
        ]
      },
      {
        "id": "skupper-solution",
        "title": "Skupper Solution Building Blocks",
        "items": [
          {
            "id": "listener",
            "name": "Listener",
            "deps": [
              "routing-key"
            ],
            "source": "generated/concepts/listener.md",
            "external": "https://pwright.github.io/skupper-okf/generated/concepts/listener"
          },
          {
            "id": "connector",
            "name": "Connector",
            "deps": [
              "routing-key",
              "service-provider"
            ],
            "source": "generated/concepts/connector.md",
            "external": "https://pwright.github.io/skupper-okf/generated/concepts/connector"
          },
          {
            "id": "routing-key",
            "name": "Routing Key",
            "deps": [
              "skupper-router"
            ],
            "source": "generated/concepts/routing-key.md",
            "external": "https://pwright.github.io/skupper-okf/generated/concepts/routing-key"
          },
          {
            "id": "site-link",
            "name": "Site Link",
            "deps": [
              "skupper-router",
              "network-reachability"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#site-link"
          },
          {
            "id": "skupper-router",
            "name": "Skupper Router",
            "deps": [],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#skupper-router"
          },
          {
            "id": "multi-provider-routing",
            "name": "Multiple providers for one routing key",
            "deps": [
              "routing-key",
              "connector",
              "skupper-router"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#multi-provider-routing"
          },
          {
            "id": "routing-cost",
            "name": "Routing Cost",
            "deps": [
              "site-link",
              "skupper-router"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#routing-cost"
          }
        ]
      },
      {
        "id": "solution-environment",
        "title": "Solution Environment",
        "items": [
          {
            "id": "service-consumer",
            "name": "Service consumer",
            "deps": [],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#service-consumer"
          },
          {
            "id": "service-provider",
            "name": "Service provider",
            "deps": [],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#service-provider"
          },
          {
            "id": "cloud-environment",
            "name": "Cloud environment",
            "deps": [
              "network-reachability"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#cloud-environment"
          },
          {
            "id": "datacenter-environment",
            "name": "Datacenter environment",
            "deps": [
              "network-reachability"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#datacenter-environment"
          },
          {
            "id": "edge-environment",
            "name": "Edge / branch environment",
            "deps": [
              "network-reachability"
            ],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#edge-environment"
          },
          {
            "id": "network-reachability",
            "name": "Underlying network reachability",
            "deps": [],
            "source": "generated/architecture/togaf-overview.md",
            "external": "https://pwright.github.io/skupper-okf/generated/architecture/togaf-overview#network-reachability"
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  }
]
```
