---
type: VmsLandscapePage
title: "Automatic Certificate Rotation"
id: auto-cert-rotation
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/auto-cert-rotation
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Automatic Certificate Rotation

Management controller monitors expiration and rotates certificates seamlessly - zero downtime rotation

## Appears in

- [VMS Security & PKI](./vms-overview.md) / Certificate Automation

## Topics

### Dependencies

- [Rotation Monitoring](./rotation-monitoring.md)


## Certificate Rotation

Certificate rotation is orchestrated automatically by the certificate engine module. The module generates work for itself by inserting rows into the CertificateRequests table.

### Rotation Architecture

To support seamless rotation, VMS uses a "container" model for certificates:

- **InteriorSite**, **MemberSite**, and **InteriorAccessPoint** serve as stable containers
- The contained **TlsCertificate** is replaced during rotation
- SSL profiles on routers are correlated with the container, not the specific certificate

### Rotation Ordinals

Each TlsCertificate has attributes for tracking rotation:

- **RotationOrdinal** - Incremented in the superseding certificate
- **Supercedes** - Reference to the superseded certificate
- **Invariant**: `this.RotationOrdinal = this.Supercedes.RotationOrdinal + 1`

### SSL Profile Management

During rotation:

1. SSL profiles are overwritten with new certificate data
2. Rotation ordinals are updated: `current version`, `last-valid-version`
3. Old certificates are kept in database until expiry
4. Routers can optionally close connections using expired certificates

### Zero Downtime

The rotation process ensures:

- New certificates are generated before old ones expire
- Both old and new certificates are valid during transition
- SSL profiles update without service interruption
- No manual intervention required

## Source

Based on `human/vms/docs/notes/objects.md`
