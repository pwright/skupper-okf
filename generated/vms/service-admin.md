---
type: VmsLandscapePage
title: "Service Administrator"
id: service-admin
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/service-admin
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Service Administrator

Creates and manages all backbones and application networks - enterprise-level infrastructure control

## Appears in

- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md) / User Personas

## Topics

- This item has no documented dependencies.


## Service Administrator Persona

The Service Administrator has enterprise-level control over VMS infrastructure and all application networks.

### Responsibilities

- **Create and manage all backbones** - Define multi-tenant relay infrastructure
- **Create and manage all application networks** - Full control over VANs across the enterprise
- **Assign backbone administrators** - Delegate backbone management
- **Configure user permissions** - Control who can create VANs on which backbones
- **Monitor enterprise-wide topology** - View all backbones, VANs, sites, and members
- **Manage certificate infrastructure** - Oversee PKI and CA hierarchy

### Access Level

- Full access to VMS management controller API
- Can perform all operations on all resources
- Enterprise-level view of infrastructure
- Authenticated via Keycloak

### Typical Workflows

1. **Backbone Setup** - Create backbones, add strategically-placed sites, configure links
2. **Permission Management** - Grant users access to specific backbones
3. **Infrastructure Monitoring** - Track backbone health, site deployment, certificate expiration
4. **Capacity Planning** - Analyze VAN distribution across backbones
5. **Incident Response** - Force-evict compromised VANs or sites

### Tools

- VMS Console (web UI)
- VMS CLI (`vms` command-line tool)
- Management Controller REST API

## Source

Based on `human/vms/README.md`
