---
type: VmsLandscapePage
title: "Backbone CA"
id: backbone-ca
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/backbone-ca
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Backbone CA

Intermediate CA per backbone signs backbone sites and VAN CAs - backbone-level isolation

## Appears in

- [VMS Security & PKI](./vms-overview.md) / Certificate Hierarchy

## Topics

### Dependencies

- [External Root CA](./external-root-ca.md)


## Backbone CA

Intermediate certificate authority for each backbone network. Signs backbone site certificates and VAN CAs.

### Certificate Hierarchy Position

```
Root CA (customer-provided)
  └─ Backbone CA (one per backbone)
       ├─ Backbone Site Certificates
       └─ VAN CAs (one per VAN on this backbone)
            ├─ Invitation Certificates
            └─ Member Certificates
```

### Created Automatically

When a backbone is created:

1. Service admin creates backbone via API
2. Management controller requests backbone CA from cert-manager
3. Backbone CA certificate signed by root CA
4. Backbone CA stored in TlsCertificates table
5. Backbone ready to sign site certificates

### Signing Authority

The backbone CA signs:

- **Backbone site certificates** - For sites that relay traffic
- **VAN CAs** - Intermediate CAs for application networks on this backbone

### Multi-tenancy Enabler

Each backbone has its own CA:

- **Isolation between backbones** - Backbone A certs can't access backbone B
- **Independent lifecycle** - Backbones can be created/deleted independently
- **Delegated administration** - Backbone admin controls their CA's subtree

### Backbone-level Eviction

Revoking a backbone CA would invalidate its entire subtree:

- All backbone site certificates
- All VAN CAs on that backbone
- All invitation and member certificates for those VANs

This provides instant removal of an entire backbone and all its VANs.

### Integration with Customer PKI

The backbone CA is signed by the customer's root CA:

- **Trust anchor** - Customer controls root CA
- **PKI integration** - VMS certificates trusted by customer infrastructure
- **Policy enforcement** - Customer can revoke backbone CA if needed

## Source

Based on `human/vms/README.md`
