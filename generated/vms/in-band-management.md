---
type: VmsLandscapePage
title: "In-band Management"
id: in-band-management
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/in-band-management
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# In-band Management

Site controllers communicate with management controller via data plane - no separate management network required

## Appears in

- [VMS Control & Data Plane Architecture](./vms-overview.md) / Architecture Outcomes

## Topics

### Dependencies

- [Site Controller](./site-controller.md)
- [Data Plane Communication](./data-plane-communication.md)


## In-band Management

Site controllers communicate with the management controller via the data plane - no separate management network required.

### Architecture

**Traditional approach** (VMS eliminates):
- Separate management network
- Out-of-band access to each site
- Firewall rules for management traffic
- VPN or direct connectivity requirements

**VMS in-band approach**:
- Site controllers use data plane (Skupper routers) to reach management controller
- Management traffic carried alongside application traffic
- Same TLS-secured connections
- No additional network infrastructure

### Communication Flow

1. **Site deployment** - Bootstrap YAML or invitation YAML includes connection info
2. **Site connects** - Site controller establishes connection via data plane
3. **Registration** - Site reports status and ingress information
4. **Configuration sync** - Management controller pushes TLS secrets, access points, links
5. **Heartbeat** - Site controller reports status periodically
6. **Status updates** - Access point status (host/port) pushed upstream

### Benefits

**No management network required**
- Participants don't need to reach management controller directly
- Works across network boundaries (DMZ, firewall, NAT)
- Backbone provides relay for management traffic

**Simplified deployment**
- No VPN setup
- No firewall rule changes
- No additional network infrastructure

**Same security model**
- Management traffic uses same mutual TLS as application traffic
- Certificate-based authentication
- Encrypted communication

### Contrast with Management Plane Location

The management plane (management controller, database) is **logically centralized** but doesn't need to be **network-accessible** to all sites:

- Sites may be behind firewalls that block inbound connections
- Sites in DMZs or restricted networks
- Sites with no direct connectivity to management plane

The backbone provides **relay** so in-band communication works across these boundaries.

## Source

Based on `human/vms/README.md`
