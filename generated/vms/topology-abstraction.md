---
type: VmsLandscapePage
title: "Topology Abstraction"
id: topology-abstraction
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/topology-abstraction
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Topology Abstraction

VAN owners specify participants, not router topology - VMS handles optimal backbone routing

## Appears in

- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md) / VMS Automation Value

## Topics

### Dependencies

- [Network Topology Management](./vms-network-topology.md)


## Topology Abstraction

VAN owners specify participants, not router topology - VMS handles optimal backbone routing automatically.

### Separation of Concerns

VMS divides the model into two orthogonal parts:

**Network Topology** (Admin responsibility):
- Which sites exist in the backbone
- How sites are interconnected
- Cost-weighted routing paths
- DMZ and network boundary placement

**Application Topology** (VAN owner responsibility):
- Which participants join the VAN
- What services are exposed
- How application components interact
- Service placement across sites

### VAN Owner Experience

**What VAN owners specify:**
- Create VAN on a backbone
- Generate invitations for participants
- Define access points (connectors/listeners)
- Monitor member participation

**What VAN owners don't need to know:**
- How many backbone sites exist
- Which sites relay their traffic
- What the optimal routing paths are
- How backbone links are configured

### Automatic Routing

VMS and Skupper router handle routing automatically:

1. **VAN created** - Owner selects a backbone
2. **Participants join** - Each applies invitation YAML to their site
3. **Member sites connect** - To backbone via nearest access point
4. **Routers calculate paths** - Based on link costs through backbone
5. **Traffic flows** - Along optimal paths without VAN owner involvement

### Benefits

**Simplified VAN creation:**
- No topology planning required
- No understanding of underlying network
- Focus on application concerns only
- Backbone infrastructure reused

**Flexible infrastructure:**
- Admin can add/remove backbone sites
- Admin can adjust link costs
- Topology changes don't affect VANs
- VANs automatically use improved paths

**Video-conference analogy:**
- Creating VAN = scheduling meeting
- Inviting participants = sending meeting link
- Joining = clicking link and joining
- Network topology = telecom infrastructure (invisible to users)

### Contrast with Manual Skupper

**Manual Skupper** (VMS eliminates):
- Application owner plans router topology
- Decides which sites connect to which
- Calculates optimal paths manually
- Coordinates link creation across sites
- Mixes application and network concerns

**VMS Topology Abstraction**:
- Network admin manages backbone (once)
- VAN owner manages application (ongoing)
- Clear separation of concerns
- Reusable infrastructure

## Source

Based on `human/vms/README.md` and `human/vms/docs/notes/model.md`
