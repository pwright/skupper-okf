---
type: VmsLandscapePage
title: "Backbone Administrator"
id: backbone-admin
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/backbone-admin
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Backbone Administrator

Manages assigned backbone and its application networks - delegated infrastructure control

## Appears in

- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md) / User Personas

## Topics

- This item has no documented dependencies.


## Backbone Administrator Persona

Backbone administrators manage assigned backbones and their application networks - delegated infrastructure control from service administrators.

### Responsibilities

- **Manage assigned backbone** - Control sites, links, and access points for one backbone
- **Manage VANs on backbone** - Oversee application networks using their backbone
- **Monitor backbone health** - Track site deployment, connectivity, certificates
- **Assign VAN permissions** - Grant users access to create VANs on this backbone
- **Evict VANs** - Remove application networks from the backbone
- **Respond to incidents** - Handle issues affecting the backbone

### Access Level

- Authenticated via Keycloak (realm role: `backbone-owner`)
- Full control over assigned backbone(s)
- Can create/manage VANs on assigned backbones
- Cannot create new backbones
- Cannot access other backbones
- Row-level security limits view to assigned backbones

### Typical Workflows

**Backbone operations:**
1. Add sites to strategic locations
2. Configure access points on sites
3. Create cost-weighted links between sites
4. Monitor site deployment state and heartbeats

**VAN oversight:**
1. View VANs running on the backbone
2. Monitor VAN membership and resource usage
3. Evict VANs when needed (policy violations, end of agreement)
4. Assist VAN users with connectivity issues

**User management:**
1. Grant VAN users permission to create VANs on this backbone
2. Assign users to groups for shared VAN access
3. Revoke permissions when access should end

### Delegation Model

Service administrators delegate backbone management:

- **Assign backbone** - Link backbone to admin via OwnerGroup
- **Transfer responsibility** - Offload day-to-day management
- **Retain oversight** - Service admin can still access all backbones
- **Scoped authority** - Backbone admin only sees their backbone(s)

### Tools

- VMS Console (web UI)
- VMS CLI for backbone operations
- Management Controller REST API

### Differences from Service Admin

**Backbone Admin:**
- Manages one or more assigned backbones
- Cannot create new backbones
- Cannot access other backbones
- Delegated authority

**Service Admin:**
- Manages all backbones
- Can create new backbones
- Enterprise-wide view
- Full authority

## Source

Based on `human/vms/README.md` and `human/vms/docs/notes/keycloak-setup.md`
