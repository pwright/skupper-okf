---
type: VmsLandscapePage
title: "Centralized Topology Visibility"
id: centralized-topology-visibility
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/centralized-topology-visibility
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Centralized Topology Visibility

Single view of all backbones, sites, links, and their states - eliminates distributed topology tracking

## Appears in

- [VMS Network Topology Management](./vms-overview.md) / Topology Outcomes

## Topics

### Dependencies

- [Topology State Store](./topology-state-store.md)


## Centralized Topology Visibility

Single view of all backbones, sites, links, and their states - eliminates distributed topology tracking.

### What's Visible

**Backbone level:**
- All backbone networks
- Backbone lifecycle states
- Multi-tenant vs single-tenant configuration

**Site level:**
- All backbone and member sites
- Deployment states (created, ready-bootstrap, deployed, failed)
- Site heartbeats and last contact time
- First active time

**Link level:**
- All backbone links
- Link costs
- Connected sites
- Link status

**Access point level:**
- All access points on sites
- Access point kinds (manage, peer, van, claim, member)
- Ingress host and port
- Lifecycle states

**VAN level:**
- All application networks
- VAN lifecycle states
- Start and end times
- Member counts

**Member level:**
- All VAN members
- Join times
- Heartbeats
- Invitation source

### Contrast with Distributed Skupper

**Manual Skupper** (no VMS):
- Each site knows only its local state
- No central view of who's connected
- Manual tracking required across sites
- No aggregated health monitoring

**VMS centralized visibility:**
- PostgreSQL stores all topology state
- Management controller provides unified view
- Console displays real-time status
- API allows programmatic access

### Data Sources

**Management controller:**
- Creates topology definitions
- Stores in PostgreSQL
- Serves via REST API

**Site controllers:**
- Report heartbeats
- Send access point status
- Update deployment states

**Certificate engine:**
- Tracks certificate validity
- Monitors expiration dates
- Records rotation state

### User Interfaces

**Console (Web UI):**
- Visual topology views
- Site deployment status
- VAN membership lists
- Certificate status

**CLI:**
- List backbones, sites, links
- Query VAN membership
- Check deployment states

**API:**
- Programmatic access to all topology
- Export for monitoring systems
- Integration with automation

### Operational Benefits

**Troubleshooting:**
- See which sites are connected
- Identify deployment failures
- Track heartbeat gaps
- Monitor certificate expiration

**Capacity planning:**
- Count VANs per backbone
- Track member distribution
- Identify heavily-used backbones
- Plan backbone expansion

**Audit and compliance:**
- Who joined which VAN and when
- VAN lifecycle history
- Certificate issuance records
- Site deployment history

## Source

Based on `human/vms/README.md` and `human/vms/cli/vms`
