---
type: VmsLandscapePage
title: "VAN User"
id: van-user
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/van-user
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# VAN User

Creates VANs, invites participants, and manages application topology on permitted backbones

## Appears in

- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md) / User Personas

## Topics

- This item has no documented dependencies.


## VAN User Persona

VAN users create and manage application networks on permitted backbones. They invite participants and manage application topology but don't administer backbone infrastructure.

### Responsibilities

- **Create VANs** - Define new application networks on permitted backbones
- **Generate invitations** - Create invitation claims for participants
- **Monitor VAN membership** - View who has joined and their status
- **Manage access points** - Define connectors/listeners for service exposure (future feature)
- **Evict members** - Remove individual participants when needed
- **Evict VANs** - Remove entire application network when collaboration ends

### Access Level

- Authenticated via Keycloak (realm role: `van-owner`)
- Can create VANs on backbones they have permission for
- Can manage their own VANs
- Cannot create or manage backbones
- Cannot see other users' VANs (unless shared via row-level security groups)

### Typical Workflows

**VAN creation:**
1. Select backbone from permitted list
2. Create VAN with name and optional time bounds
3. VAN CA generated automatically

**Participant invitation:**
1. Create invitation with access controls
2. Set instance limits and deadline
3. Download invitation YAML
4. Distribute to participants via email, docs, chat

**Member management:**
1. Monitor VAN member list
2. View join times and heartbeats
3. Evict compromised or unauthorized members
4. Evict entire VAN when project completes

### Permissions Model

Row-level security in PostgreSQL controls access:

- **Owner field** - VANs owned by creating user
- **OwnerGroup field** - VANs can be shared with Keycloak groups
- **Realm roles** - van-owner role grants VAN creation/management

Service admins can assign VAN users to groups for shared access to VANs.

### Tools

- VMS Console (web UI)
- VMS REST API
- Future: CLI tool for VAN operations

### What VAN Users Don't Need

**No topology knowledge:**
- Don't need to understand backbone layout
- Don't know which sites relay their traffic
- Don't plan router connections
- Focus on application concerns only

**No certificate management:**
- Certificates generated automatically
- Distribution handled by VMS
- Rotation transparent to VAN users
- Revocation via eviction API

**No infrastructure administration:**
- Can't create backbone sites
- Can't modify backbone links
- Can't access other users' VANs
- Delegate infrastructure to admins

## Source

Based on `human/vms/README.md` and `human/vms/docs/notes/keycloak-setup.md`
