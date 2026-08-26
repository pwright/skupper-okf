---
type: VmsLandscapePage
title: "Claim Redemption Protocol"
id: claim-redemption
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/claim-redemption
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Claim Redemption Protocol

Site controller contacts management controller via backbone using claim cert - validated claim exchanged for member cert

## Appears in

- [VMS Application Network Lifecycle](./vms-overview.md) / VAN Capabilities

## Topics

### Dependencies

- [Invitation Claim Certificate](./invitation-claim-cert.md)


## Claim Redemption Protocol

The claim redemption process exchanges an invitation claim certificate for a full member certificate, enabling a participant to join a VAN.

### Bootstrapping Sequence

From invitation creation to member site establishment:

1. **Invitation created** - Certificate signed by VAN CA
2. **Invitation YAML generated** - Self-contained with certificate and metadata
3. **Invitation delivered** - Via any channel (email, docs, repo)
4. **Invitee applies YAML** - Deploys site controller
5. **Site controller deployed** - Uses invitation claim certificate to connect
6. **Backbone validates claim cert** - Restricts traffic to claim redemption protocol
7. **Site controller contacts management controller** - Via backbone, provides claim
8. **Management controller validates claim** - Creates new member site with member certificate
9. **Member certificate sent back** - Via in-band communication
10. **Site reconfigures** - Uses member certificate for full VAN access
11. **Configuration pushed** - Management controller sends access point definitions

### Restricted Access

The invitation claim certificate grants **restricted access**:

- Can only use claim redemption protocol
- Cannot access VAN services
- Cannot communicate with other members

This prevents invitation leakage from providing unauthorized VAN access.

### In-band Delivery

All communication happens via the backbone data plane:

- No out-of-band coordination required
- No separate management network needed
- Site controller uses data plane to reach management controller

## Source

Based on `human/vms/README.md`
