---
type: VmsLandscapePage
title: "Automatic Certificate Generation"
id: auto-cert-generation
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/auto-cert-generation
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Automatic Certificate Generation

Management controller creates CAs and certificates via cert-manager - no manual CSR/signing workflow

## Appears in

- [VMS Security & PKI](./vms-overview.md) / Certificate Automation

## Topics

### Dependencies

- [cert-manager](./cert-manager-integration.md)


## Certificate Engine

The certificate engine module is responsible for maintaining the private-key-infrastructure for the overall service. It is driven by the **CertificateRequests** table in the database, which contains work to be performed.

### Responsibilities

- Manages the **TlsCertificates** table containing all valid certificates:
  - Service root certificate authority (CA)
  - CA for the interior router network (backbone)
  - CAs for individual application networks (VANs)
  - Individual certificates signed by the above CAs

- Generates work for itself by inserting rows into CertificateRequests
- Orchestrates certificate rotation automatically

### Integration with cert-manager

The actual certificate generation and signing is done using the external **cert-manager** package. The interface to cert-manager is via Kubernetes entities:

- **Issuers** - Define CAs
- **Certificates** - Request certificates from issuers
- **Secrets** - Store generated certificate data

The certificate engine operates within the Kubernetes namespace where the VMS Management Service runs.

### No Manual CSR/Signing

Users never need to:
- Create certificate signing requests (CSRs)
- Submit CSRs to a CA
- Wait for signed certificates
- Distribute certificates to sites

All certificate operations are automated through the database-driven certificate engine.

## Source

Based on `human/vms/docs/notes/certificate_engine.md`
