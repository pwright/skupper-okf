---
type: VmsLandscapePage
title: "Backbone Site"
id: backbone-site
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/backbone-site
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Backbone Site

Relay point on the backbone - typically deployed to strategic network locations or DMZs

## Appears in

- [VMS Network Topology Management](./vms-overview.md) / Topology Capabilities

## Topics

### Dependencies

- [Site Controller](./site-controller.md)


## Backbone Site

Relay point on the backbone network - typically deployed to strategic network locations or DMZs. Each site runs a site controller and Skupper router.

### Purpose

Backbone sites provide relay infrastructure for:

- **Multi-tenant VAN traffic** - Carry application traffic for multiple VANs
- **Management traffic** - Relay communication between site controllers and management controller
- **Inter-site routing** - Connect sites across network boundaries

### Deployment

Each backbone site includes:

- **Site controller** - Manages local router and communicates with management controller
- **Skupper router** - Handles data plane traffic
- **TLS certificates** - Signed by backbone CA for mutual authentication
- **Access points** - Ingress points for different traffic types

### Access Points

Backbone sites can have multiple access point types:

| Kind   | Purpose                         |
| ------ | ------------------------------- |
| manage | Management traffic              |
| peer   | Inter-router connections        |
| van    | VAN application traffic         |
| claim  | Invitation claim redemption     |
| member | Member site connections         |

### Strategic Placement

Sites are typically placed considering:

**Geography:**
- Near application deployments
- Reduce latency for VAN traffic
- Data sovereignty requirements

**Network boundaries:**
- DMZ deployment to bridge restricted networks
- Firewall/NAT traversal points
- Cross-cloud relay points

**Infrastructure:**
- High-bandwidth locations
- Reliable connectivity
- HA/failover capability

### Bootstrap Process

Backbone sites are deployed via three-step bootstrap:

1. **Initial YAML** - Deploy site controller and router with temporary config
2. **Ingress upload** - Report actual ingress addresses to management controller
3. **Final YAML** - Apply access point configuration with real endpoints

### State Synchronization

Site controller syncs state with management controller:

**Receives from management:**
- TLS certificates
- Access point definitions
- Link configurations

**Reports to management:**
- Access point status (host/port)
- Site heartbeat
- Deployment state

### Lifecycle States

- **Created** - Defined in management controller
- **Ready-bootstrap** - Eligible for bootstrap deployment
- **Deployed** - Successfully bootstrapped and connected
- **Active** - Carrying traffic
- **Failed** - Deployment or connectivity issues

## Source

Based on `human/vms/README.md` and `human/vms/docs/notes/bootstrap.md`
