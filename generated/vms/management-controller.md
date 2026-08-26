---
type: VmsLandscapePage
title: "Management Controller"
id: management-controller
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/management-controller
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Management Controller

Orchestrates backbones, VANs, invitations, sites, and certificates - provides REST API for console and tooling

## Appears in

- [VMS Control & Data Plane Architecture](./vms-overview.md) / Management Plane (Centralized)

## Topics

- This item has no documented dependencies.


## Management Controller

The management controller orchestrates the setup and maintenance of:

- Backbone networks
- Application networks (VANs)
- Invitation claims
- Member sites
- Certificate creation, deletion, and rotation

### REST API

Provides administrative API consumed by console and CLI. The API is versioned at `/api/v1alpha1`:

**Backbone Management**
- `/backbones` - List/create backbones
- `/backbone/{bid}/sites` - Manage backbone sites
- `/backbonesite/{bsid}/kube` - Generate bootstrap YAML
- `/backbonesite/{bsid}/ingress` - Upload ingress data (POST)
- `/backbonesite/{bsid}/links/incoming/kube` - Generate link YAML

**VAN Management**
- `/vans` - List/create VANs
- `/van/{vid}/invitations` - Manage invitations
- `/invitation/{iid}/kube` - Generate invitation YAML

**Certificate Management**
- Driven by CertificateRequests table
- Integrates with cert-manager for CA and certificate operations
- Monitors expiration and orchestrates rotation

### Architecture

- Runs on Kubernetes (OpenShift routes required for API access)
- Uses PostgreSQL for persistent state storage
- Integrates with Keycloak for authentication
- Communicates with site controllers in-band via data plane

## Source

Based on `human/vms/README.md` and `human/vms/docs/notes/api.md`
