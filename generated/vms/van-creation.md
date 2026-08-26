---
type: VmsLandscapePage
title: "VAN Creation"
id: van-creation
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/van-creation
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# VAN Creation

Define application network on a backbone with optional time bounds - VAN CA created immediately for invitation signing

## Appears in

- [VMS Application Network Lifecycle](./vms-overview.md) / VAN Workflows

## Topics

### Dependencies

- van-ca-creation


## VAN Creation

Users create application networks (VANs) on permitted backbones - the first step in building a distributed application network.

### Creation Process

1. **User creates VAN** - Via VMS console or CLI
2. **Specify backbone** - Choose which backbone will carry VAN traffic
3. **Optional time bounds** - Set start and end times for the VAN
4. **VAN CA created** - Certificate authority generated immediately
5. **VAN registered** - Stored in PostgreSQL with lifecycle state

### VAN Properties

**Required:**
- **Name** - Identifier for the VAN
- **Backbone** - Which backbone network to use

**Optional:**
- **Start time** - When VAN becomes active (default: immediate)
- **End time** - When VAN automatically expires (default: none)

### Certificate Authority Timing

The VAN CA is created immediately when the VAN is defined, even if the start time is in the future. This allows:

- **Pre-signing invitations** - Invitations can be generated before VAN starts
- **Controlled activation** - VAN CA not loaded into backbone until start time
- **Prevented premature access** - Invitation certificates won't work until VAN starts

### Lifecycle States

- **Pending** - VAN created but start time not reached
- **Active** - VAN CA loaded into backbone, invitations can be redeemed
- **Expired** - End time reached, VAN CA unloaded
- **Evicted** - Force-removed by admin

### Permissions

Who can create VANs:

- **Service administrators** - Can create VANs on any backbone
- **Backbone administrators** - Can create VANs on assigned backbones
- **VAN users** - Can create VANs on permitted backbones (configured by admin)

### After Creation

Once a VAN is created, the owner can:

1. **Create invitations** - Generate invitation claims for participants
2. **Monitor members** - View who has joined
3. **Manage members** - Evict individual members
4. **Configure access points** - Define service exposure (future feature)
5. **Evict VAN** - Remove entire VAN and all members

## Source

Based on `human/vms/README.md` and `human/vms/docs/notes/keycloak-setup.md`
