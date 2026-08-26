---
type: VmsLandscapePage
title: "Backbone Network"
id: backbone-network
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/backbone-network
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Backbone Network

Multi-tenant constellation of relay points - carries traffic for multiple VANs with isolation

## Appears in

- [VMS Network Topology Management](./vms-overview.md) / Topology Capabilities

## Topics

### Dependencies

- [Skupper Router Network](./skupper-router.md)


## Network Topology Model

The VMS model divides the Service into two independent parts: **Network Topology** and **Application Topology**.

### Network Topology

The Network Topology is concerned with:

- The set of sites in the Service
- How those sites are securely interconnected
- The various ephemeral Application Networks
- Which sites participate in each Application Network

### Multi-tenant Constellation

A backbone network is a multi-tenant constellation of relay points that:

- Carries traffic for multiple VANs with isolation via certificate-based addressing
- Uses Skupper routers as the data plane
- Provides cost-weighted routing between strategically-placed sites
- Supports DMZ deployment for bridging restricted networks

### Backbone Components

1. **Backbone Sites** - Relay points deployed to strategic network locations
2. **Backbone Links** - Cost-weighted connections defining relay topology
3. **Access Points** - Ingress points for management and VAN traffic

## Source

Based on `human/vms/README.md` and `human/vms/docs/notes/model.md`
