---
type: VmsLandscapePage
title: "Skupper Router Network"
id: skupper-router
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/skupper-router
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Skupper Router Network

Application-layer message routing provides abstract, flexible data plane independent of IP topology

## Appears in

- [VMS Control & Data Plane Architecture](./vms-overview.md) / Data Plane (Skupper Routers)

## Topics

- This item has no documented dependencies.


## Skupper Router Network

Application-layer message routing provides abstract, flexible data plane independent of IP topology. VMS uses Skupper router as the data plane for backbone and VAN traffic.

### Data Plane Architecture

**VMS uses Skupper router for:**
- Backbone inter-site connectivity
- VAN member-to-member communication
- In-band management traffic (site controller ↔ management controller)
- Service exposure (connectors and listeners)

**Router characteristics:**
- **Application-layer routing** - Not IP routing, operates on TCP connections and messages
- **Location-transparent** - Services addressable by name, not IP
- **Cost-weighted paths** - Automatic route calculation based on link costs
- **Multi-tenant** - Backbone routers carry traffic for multiple VANs with isolation

### Multi-tenancy

Backbone routers handle traffic for multiple VANs simultaneously:

- **Certificate-based addressing** - Each VAN's traffic identified by certificate
- **Isolation** - VANs cannot access each other's traffic
- **Shared infrastructure** - One router carries many VANs
- **Efficient resource use** - No per-VAN routers needed

### Narrow Coupling

VMS architecture has narrow coupling to Skupper router:

- **Data plane abstraction** - VMS manages topology, router handles traffic
- **Potential future options** - Architecture allows for alternative data planes
- **Clear interface** - Site controller configures router via Kubernetes CRs
- **Independent evolution** - VMS and router can evolve separately

### Router Configuration

Site controllers generate Kubernetes custom resources:

- **RouterAccess** - Defines router ingress points (manage, peer, member)
- **NetworkAccess** - Defines VAN ingress points
- **Link** - Defines inter-router connections
- **Certificates** - TLS credentials for mutual authentication

### Integration Points

**VMS → Router:**
- Site controller deploys router pods
- Configuration via Kubernetes CRs
- Certificate distribution via secrets
- Cost configuration via Link CRs

**Router → VMS:**
- Access point status (host/port from ingress)
- Connection status (implicit via heartbeat)
- Router logs (for debugging)

## Source

Based on `human/vms/README.md` and `human/vms/docs/notes/objects.md`
