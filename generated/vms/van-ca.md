---
type: VmsLandscapePage
title: "VAN CA"
id: van-ca
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/van-ca
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# VAN CA

Intermediate CA per VAN signs invitation and member certificates - VAN-level isolation

## Appears in

- [VMS Security & PKI](./vms-overview.md) / Certificate Hierarchy

## Topics

### Dependencies

- [Backbone CA](./backbone-ca.md)


## VAN Certificate Authority

Each VAN has its own intermediate CA under the backbone CA. This provides cryptographic isolation between VANs sharing the same backbone.

### Certificate Hierarchy Position

```
Root CA (customer-provided)
  └─ Backbone CA
       ├─ Backbone Site Certificates
       └─ VAN CA (one per VAN)
            ├─ Invitation Claim Certificates
            └─ Member Site Certificates
```

### Lifecycle

**VAN Creation**
- VAN CA created immediately when VAN is defined
- Allows invitation certificates to be signed before VAN starts

**Time-boxed Loading**
- VAN CA not loaded into backbone until VAN start time
- Prevents premature invitation redemption
- Automatic unloading at VAN end time

**VAN Eviction**
- Revoking VAN CA invalidates entire subtree
- All invitation and member certificates become invalid
- Single operation removes all VAN access

### Signing Authority

The VAN CA signs:

- **Invitation Claim Certificates** - Embedded in invitation YAML, restricted access
- **Member Site Certificates** - Issued after claim redemption, full VAN access

### Isolation

Each VAN's CA provides:

- **Cryptographic isolation** - VANs cannot impersonate each other
- **Independent lifecycle** - VAN eviction doesn't affect other VANs
- **Multi-tenant security** - Shared backbone carries isolated traffic

## Source

Based on `human/vms/README.md`
