---
type: VmsLandscapePage
title: "Centralized Control"
id: centralized-management
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/centralized-management
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Centralized Control

Single management plane for all backbones and VANs across the enterprise - eliminates per-site administration

## Appears in

- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md) / VMS Automation Value

## Topics

### Dependencies

- [Control & Data Plane Architecture](./vms-architecture.md)


## Centralized Control

VMS provides a single management plane for all backbones and VANs across the enterprise - eliminating per-site administration.

### Management Plane Components

**Logically Centralized**
- Management controller
- PostgreSQL database
- Certificate engine
- Keycloak authentication

**Physically Distributed** (optional)
- Can be replicated for high availability
- Can scale for performance
- Remains logically single system

### What Gets Centralized

**Topology Management**
- All backbone definitions and configuration
- All VAN definitions and policies
- Site registration and status
- Link configuration

**Certificate Management**
- CA hierarchy
- Certificate generation and signing
- Rotation orchestration
- Revocation and expiration

**Access Control**
- User authentication (via Keycloak)
- Permission assignments
- Invitation creation and validation

**Monitoring & Audit**
- Site heartbeats
- Deployment status
- Certificate validity
- VAN membership

### Benefits vs. Distributed Administration

**Traditional Skupper** (VMS eliminates):
- Per-site initialization and configuration
- Distributed token generation and exchange
- Manual topology coordination
- Per-site certificate management
- Scattered state across sites

**VMS Centralized Approach**:
- Single source of truth (PostgreSQL)
- Declarative configuration via API
- Automated site bootstrapping
- Automatic certificate distribution
- Central visibility and control

### Deployment Flexibility

While the management plane is centralized, it doesn't need to be **network-accessible** to all sites:

- Sites communicate in-band via data plane
- Management controller can run behind firewall
- No requirement for sites to have direct access
- Backbone relays management traffic

### API-Driven

All management operations via REST API:
- VMS Console (web UI)
- VMS CLI tool
- External automation tools
- GitOps workflows

## Source

Based on `human/vms/README.md`
