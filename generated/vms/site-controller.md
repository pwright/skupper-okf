---
type: VmsLandscapePage
title: "Site Controller"
id: site-controller
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/site-controller
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Site Controller

Runs at backbone and member sites communicating with management controller in-band via data plane

## Appears in

- [VMS Control & Data Plane Architecture](./vms-overview.md) / Site Controller (Distributed)

## Topics

- This item has no documented dependencies.


## Site Controller

The site controller runs at backbone sites and application network member sites. It orchestrates local deployment and communicates in-band with the management controller.

### Responsibilities

**Local Orchestration**
- Deploy and configure data plane (Skupper routers)
- Apply site certificates and access point configuration
- Manage Kubernetes custom resources (RouterAccess, NetworkAccess, Link)

**Management Communication**
- Register with management controller via in-band communication
- Report status and heartbeat
- Receive configuration updates (access points, links, certificates)

**Claim Redemption**
- Contact management controller with invitation claim certificate
- Exchange claim cert for member certificate
- Reconfigure data plane with full member access

**Local API**
- Provide API for participants to view and manage local access points
- Support interactive approval of access point deployment
- Enable local console access without central authentication

### Deployment Artifacts

Site controllers are deployed via:

- **Backbone sites** - Bootstrap YAML (3-step process)
- **Member sites** - Invitation YAML (self-contained)

### State Synchronization

Site controller syncs state with management controller:

**Downstream (Management → Site)**
- TLS secrets (certificates)
- Access points
- Links

**Upstream (Site → Management)**
- Access point status (host/port from ingress)
- Site heartbeat

All sync uses in-band communication via data plane - no separate management network required.

## Source

Based on `human/vms/README.md` and `human/vms/docs/notes/objects.md`
