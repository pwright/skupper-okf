---
type: VmsLandscapePage
title: "cert-manager"
id: cert-manager-integration
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/cert-manager-integration
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# cert-manager

Kubernetes certificate controller orchestrates CA and certificate lifecycle - VMS management plane component

## Appears in

- [VMS Security & PKI](./vms-overview.md) / PKI Components

## Topics

- This item has no documented dependencies.


## cert-manager Integration

VMS integrates with the Jetstack cert-manager package for certificate generation and signing. The certificate engine drives cert-manager via Kubernetes custom resources.

### Architecture

**Management controller** contains:
- **Certificate engine module** - Drives certificate operations
- **CertificateRequests table** - Work queue for cert operations
- **TlsCertificates table** - Stores all valid certificates

**cert-manager** provides:
- **Issuers** - Define certificate authorities
- **Certificates** - Request certificates from issuers
- **Secrets** - Store generated certificate data

### Integration Flow

1. **Certificate needed** - Management controller inserts row into CertificateRequests
2. **Certificate engine polls** - Detects new request
3. **Create Issuer CR** - For CAs, certificate engine creates Issuer resource
4. **Create Certificate CR** - For leaf certificates, creates Certificate resource
5. **cert-manager generates** - Creates certificate and stores in Secret
6. **Certificate engine reads** - Retrieves certificate from Secret
7. **Store in database** - Saves to TlsCertificates table
8. **Distribute to sites** - Site controllers receive certificates via in-band sync

### Certificate Types

**CAs (Issuers):**
- Root CA (customer-provided, external to cert-manager)
- Backbone CA (one per backbone)
- VAN CA (one per VAN)

**Leaf Certificates:**
- Backbone site certificates
- Invitation claim certificates
- Member site certificates

### Namespace Requirement

cert-manager operates in the Kubernetes namespace where the management controller runs:

- Issuer and Certificate CRs created in that namespace
- Secrets containing certificates stored in same namespace
- Certificate engine has access to read/write these resources

### Deployment

cert-manager is deployed via Helmfile:

```yaml
releases:
  certManager:
    enabled: true  # Installs cert-manager into cert-manager namespace
```

Version: v1.20.0 (Jetstack OCI chart)

### Customer PKI Integration

The root CA is external to VMS:

- **Customer provides** - Root CA certificate and signing capability
- **VMS uses** - Backbone CAs signed by customer's root
- **Trust chain** - All VMS certificates chain to customer's root CA
- **Policy enforcement** - Customer can revoke VMS CAs if needed

### Automatic Operations

cert-manager handles automatically:

- **Certificate generation** - Creates private key and certificate
- **CSR signing** - Signs certificate signing requests with issuer CA
- **Secret creation** - Stores certificate in Kubernetes Secret
- **Renewal** - Automatically renews certificates before expiry (if configured)

VMS certificate engine coordinates these operations via Kubernetes API.

## Source

Based on `human/vms/docs/notes/certificate_engine.md` and `human/vms/charts/helmfile/README.md`
