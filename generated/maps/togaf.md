---
title: "TOGAF Patterns Enabled by a Skupper Network"
type: BlockscapeMap
status: generated
source_path: maps/togaf.bs
tags:
  - skupper
  - blockscape
---

# TOGAF Patterns Enabled by a Skupper Network

Edit: [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/togaf.bs)

```bs full
{
"id": "togaf-skupper-solution-patterns",
"title": "TOGAF Patterns Enabled by a Skupper Network",
"abstract": "Architecture patterns in which location-independent application connectivity is part of the solution. The upper categories describe architecture outcomes and reusable patterns. Lower categories show the connectivity capabilities and Skupper solution building blocks that can realize those patterns without making Skupper the complete solution.",
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
]
},
{
"id": "boundaryless-applications",
"name": "Boundaryless applications",
"deps": [
"boundaryless-information-flow",
"integration-layer"
]
},
{
"id": "deployment-freedom",
"name": "Deployment freedom",
"deps": [
"independent-service-placement",
"hybrid-cloud-elasticity"
]
},
{
"id": "incremental-modernization",
"name": "Incremental modernization",
"deps": [
"legacy-modernization"
]
},
{
"id": "cross-location-resilience",
"name": "Cross-location resilience",
"deps": [
"resilient-service-instances",
"hybrid-cloud-elasticity"
]
},
{
"id": "infrastructure-decoupling",
"name": "Application topology decoupled from infrastructure topology",
"deps": [
"service-virtualization",
"integration-layer"
]
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
"external": "[https://www.opengroup.org/soa/source-book/soa_refarch/p13.htm](https://www.opengroup.org/soa/source-book/soa_refarch/p13.htm)"
},
{
"id": "integration-layer",
"name": "Integration Layer",
"deps": [
"service-connectivity",
"cross-boundary-routing",
"secure-transport"
],
"external": "[https://www.opengroup.org/soa/source-book/togaf/p4.htm](https://www.opengroup.org/soa/source-book/togaf/p4.htm)"
},
{
"id": "boundaryless-information-flow",
"name": "Boundaryless Information Flow",
"deps": [
"cross-boundary-routing",
"platform-independent-connectivity",
"secure-transport"
],
"external": "[https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm](https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm)"
},
{
"id": "independent-service-placement",
"name": "Independent Microservice Placement",
"deps": [
"logical-service-identity",
"platform-independent-connectivity",
"location-transparent-routing"
],
"external": "[https://www.opengroup.org/soa/source-book/msawp/p2.htm](https://www.opengroup.org/soa/source-book/msawp/p2.htm)"
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
"external": "[https://www.opengroup.org/soa/source-book/msawp/p2.htm](https://www.opengroup.org/soa/source-book/msawp/p2.htm)"
},
{
"id": "legacy-modernization",
"name": "Legacy Modernization / Wrapper",
"deps": [
"private-service-access",
"platform-independent-connectivity",
"endpoint-abstraction"
],
"external": "[https://www.opengroup.org/soa/source-book/togaf/p4.htm](https://www.opengroup.org/soa/source-book/togaf/p4.htm)"
},
{
"id": "resilient-service-instances",
"name": "Resilient Parallel Service Instances",
"deps": [
"multi-location-service",
"connection-distribution",
"service-failover"
],
"external": "[https://www.opengroup.org/soa/source-book/msawp/p2.htm](https://www.opengroup.org/soa/source-book/msawp/p2.htm)"
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
]
},
{
"id": "endpoint-abstraction",
"name": "Endpoint abstraction",
"deps": [
"listener",
"connector",
"routing-key"
]
},
{
"id": "service-connectivity",
"name": "Application service connectivity",
"deps": [
"listener",
"connector"
]
},
{
"id": "location-transparent-routing",
"name": "Location-transparent routing",
"deps": [
"routing-key",
"skupper-router"
]
},
{
"id": "cross-boundary-routing",
"name": "Cross-boundary routing",
"deps": [
"site-link",
"skupper-router"
]
},
{
"id": "secure-transport",
"name": "Secure transport between locations",
"deps": [
"site-link",
"skupper-router"
]
},
{
"id": "platform-independent-connectivity",
"name": "Platform-independent connectivity",
"deps": [
"listener",
"connector"
]
},
{
"id": "private-service-access",
"name": "Private service access without public exposure",
"deps": [
"listener",
"connector",
"site-link"
]
},
{
"id": "multi-location-service",
"name": "One logical service across locations",
"deps": [
"routing-key",
"connector",
"skupper-router"
]
},
{
"id": "connection-distribution",
"name": "Connection distribution",
"deps": [
"skupper-router",
"connector"
]
},
{
"id": "service-failover",
"name": "Service instance failover",
"deps": [
"skupper-router",
"multi-provider-routing"
]
},
{
"id": "location-preference",
"name": "Location preference",
"deps": [
"skupper-router",
"routing-cost"
]
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
]
},
{
"id": "connector",
"name": "Connector",
"deps": [
"routing-key",
"service-provider"
]
},
{
"id": "routing-key",
"name": "Routing Key",
"deps": [
"skupper-router"
]
},
{
"id": "site-link",
"name": "Site Link",
"deps": [
"skupper-router",
"network-reachability"
]
},
{
"id": "skupper-router",
"name": "Skupper Router",
"deps": []
},
{
"id": "multi-provider-routing",
"name": "Multiple providers for one routing key",
"deps": [
"routing-key",
"connector",
"skupper-router"
]
},
{
"id": "routing-cost",
"name": "Routing Cost",
"deps": [
"site-link",
"skupper-router"
]
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
"deps": []
},
{
"id": "service-provider",
"name": "Service provider",
"deps": []
},
{
"id": "cloud-environment",
"name": "Cloud environment",
"deps": [
"network-reachability"
]
},
{
"id": "datacenter-environment",
"name": "Datacenter environment",
"deps": [
"network-reachability"
]
},
{
"id": "edge-environment",
"name": "Edge / branch environment",
"deps": [
"network-reachability"
]
},
{
"id": "network-reachability",
"name": "Underlying network reachability",
"deps": []
}
]
}
]
}
```
