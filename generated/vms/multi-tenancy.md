---
type: VmsLandscapePage
title: "Multi-tenant Isolation"
id: multi-tenancy
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/multi-tenancy
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Multi-tenant Isolation

Multiple VANs share a backbone network with hierarchical CA-based isolation - efficient infrastructure use

## Appears in

- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md) / VMS Automation Value

## Topics

### Dependencies

- [Network Topology Management](./vms-network-topology.md)
- [Security & PKI](./vms-security-pki.md)


## Multi-tenant Isolation

VMS enables multiple VANs to share a single backbone network with hierarchical CA-based isolation. This provides efficient infrastructure use while maintaining security.

### How Multi-tenancy Works

**Shared Backbone Infrastructure**
- One backbone serves multiple VANs
- Backbone routers carry traffic for all VANs simultaneously
- Reduces infrastructure overhead vs. per-VAN backbones

**Certificate-based Isolation**
- Each VAN has its own CA under the backbone CA
- VAN certificates cannot be used to access other VANs
- Routers use certificate-based addressing to route traffic

**Hierarchical CA Structure**
```
Backbone CA
  ├─ VAN 1 CA
  │    ├─ VAN 1 Member Certificates
  │    └─ VAN 1 Invitation Certificates
  ├─ VAN 2 CA
  │    ├─ VAN 2 Member Certificates
  │    └─ VAN 2 Invitation Certificates
  └─ VAN N CA
       └─ ...
```

### Isolation Properties

**Cryptographic Isolation**
- VANs cannot impersonate each other
- Certificate validation prevents cross-VAN access
- Separate CA subtrees for each VAN

**Independent Lifecycles**
- Evicting one VAN doesn't affect others
- VAN-specific start/end times
- Per-VAN invitation policies

**Resource Efficiency**
- Shared backbone relay infrastructure
- Shared management plane
- Reduced operational overhead

### Backbone Configuration

Backbones can be configured as:

- **Multi-tenant** (default) - Supports multiple VANs
- **Single-tenant** - Dedicated to one VAN (via `--no-multitenant` flag)

## Source

Based on `human/vms/README.md` and `human/vms/cli/vms`
