---
type: VmsLandscapePage
title: "PostgreSQL Database"
id: postgresql
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/postgresql
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# PostgreSQL Database

Central persistent store for topology, state, and configuration - relational database for audit and history

## Appears in

- [VMS Control & Data Plane Architecture](./vms-overview.md) / Management Plane (Centralized)

## Topics

### Dependencies

- [Management Controller](./management-controller.md)


## PostgreSQL Database

The central persistent store for VMS configuration and state. All backbone, VAN, certificate, and site data is stored in PostgreSQL.

### Schema

The database schema is defined in `charts/helmfile/resources/db-setup.sql` and includes tables for:

- **Backbones** - Backbone networks and their configuration
- **InteriorSites** - Backbone sites
- **BackboneAccessPoints** - Access points on backbone sites
- **BackboneLinks** - Links between backbone sites
- **ApplicationNetworks** (VANs) - Application networks
- **Invitations** - Invitation claims for VANs
- **MemberSites** - VAN member sites
- **TlsCertificates** - All certificates in the system
- **CertificateRequests** - Work queue for certificate engine

### Deployment

Deployed via Helmfile using Bitnami PostgreSQL chart (version 18.3.0):

```shell
cd charts/helmfile
helmfile sync
```

The schema is applied automatically on first init via a ConfigMap containing `db-setup.sql`.

### Database Users

Two application users are created (passwords from `postgres-credentials` secret):

- **app_user** - Primary application user with read/write access
- **app_system** - System user for administrative operations

### Access

- Management controller connects using `APP_USER_PASSWORD` from environment
- Connection details configured via environment variables:
  - `PGHOST` - Database host
  - `PGDATABASE` - Database name (default: `studiodb`)
  - `PGUSER` - Database user (default: `access`)

### State Management

PostgreSQL is the **source of truth** for all VMS state:

- Management controller reads/writes topology and configuration
- Certificate engine driven by CertificateRequests table
- Site controllers receive state via in-band sync (not direct DB access)

### Maintenance

Optional teardown script available at `charts/helmfile/resources/drop.sql` (not used by Helmfile, manual use only).

## Source

Based on `human/vms/README.md` and `human/vms/charts/helmfile/README.md`
