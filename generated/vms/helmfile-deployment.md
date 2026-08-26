---
type: VmsLandscapePage
title: "Helmfile Deployment"
id: helmfile-deployment
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/helmfile-deployment
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Helmfile Deployment

Management plane deployed via Helmfile with PostgreSQL, cert-manager, and management-controller chart

## Appears in

- [VMS Control & Data Plane Architecture](./vms-overview.md) / Deployment Artifacts

## Topics

- This item has no documented dependencies.


## Helmfile Deployment

The `charts/helmfile` directory is a Helmfile environment that installs the VMS management plane on Kubernetes.

### Charts Installed

| Chart                 | Purpose                                                                                  |
| --------------------- | ---------------------------------------------------------------------------------------- |
| **cert-manager**      | Jetstack OCI chart (v1.20.0) - TLS issuers and certificates (optional)                   |
| **postgresql**        | Bitnami postgresql 18.3.0 - Application database with schema from `resources/db-setup.sql` |
| **management-server** | Local chart - VMS management controller                                                  |

Helmfile uses your current `kubectl` context.

### Prerequisites

- **kubectl** (1.15+)
- **Helm** and **Helmfile**
- **helm-diff** plugin: `helm plugin install https://github.com/databus23/helm-diff`
- Keycloak instance running and configured

### Required Secrets

Create these Kubernetes secrets **before** running Helmfile:

**postgres-credentials** (in PostgreSQL and management-server namespaces):
```shell
kubectl create secret generic postgres-credentials \
  --from-literal=postgres-password='REPLACE_SUPERUSER_PASSWORD' \
  --from-literal=app-user-password='REPLACE_APP_USER_PASSWORD' \
  --from-literal=app-system-password='REPLACE_APP_SYSTEM_PASSWORD' \
  -n <namespace>
```

**keycloak-config** (in management-server namespace):
```shell
kubectl create secret generic keycloak-config \
  --from-file=/path/to/your-keycloak.json \
  -n <management-server-namespace>
```

### Configuration

Edit `values/common.yaml` to configure:

- **releases.certManager.enabled** - Install cert-manager into `cert-manager` namespace
- **releases.postgresql.enabled** - Install PostgreSQL
- **releases.postgresql.namespace** - PostgreSQL namespace (or current namespace if empty)
- **releases.managementServer.enabled** - Install management controller

### Deployment

```shell
cd charts/helmfile
# Edit values/common.yaml for your environment
helmfile sync
```

## Source

Based on `human/vms/charts/helmfile/README.md`
