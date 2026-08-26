---
type: VmsLandscapePage
title: "Invitation Flow"
id: invitation-flow
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/invitation-flow
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Invitation Flow

Create invitation with access controls, generate YAML, distribute via any channel - video-conference meeting workflow

## Appears in

- [VMS Application Network Lifecycle](./vms-overview.md) / VAN Workflows

## Topics

### Dependencies

- [Invitation Creation](./invitation-creation.md)
- [Invitation YAML Generation](./invitation-yaml-generation.md)


## Invitation-based Participation

The workflow for application network setup is similar to that of setting up a video-conference meeting.

### Invitation Workflow

1. **VAN owner creates invitation** - Defines access controls, instance limits, deadline, and site class
2. **Generate invitation YAML** - Self-contained deployment artifact with certificate and metadata
3. **Distribute via any channel** - Email, docs, repository, chat - no secure channel required
4. **Participant applies YAML** - Deploys site controller and data plane to their environment
5. **Automatic claim redemption** - Site controller contacts management controller, exchanges claim cert for member cert
6. **Full VAN access granted** - Site reconfigures with member certificate for unrestricted access

### Invitation Properties

- **Claim access** - Access type for initial claim redemption
- **Primary access** - Main VAN access after claim redeemed
- **Instance limit** - Single-use or multi-instance invitations
- **Join deadline** - Optional time limit for redeeming invitation
- **Site class** - Optional grouping for similar sites (e.g., "warehouse", "storefront")
- **Interactive mode** - Whether participant must approve configuration

### Security Model

- Invitation claim certificate grants restricted access to claim redemption protocol only
- Management controller validates claim and issues full member certificate
- No central authentication required - invitation claim is the only credential

## Source

Based on `human/vms/README.md` and `human/vms/docs/notes/getting-started.md`
