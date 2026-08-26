---
type: VmsLandscapePage
title: "Keycloak"
id: keycloak
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/keycloak
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Keycloak

Identity and access management authenticates service admins and VAN users - no participant authentication

## Appears in

- [VMS Control & Data Plane Architecture](./vms-overview.md) / Management Plane (Centralized)

## Topics

### Dependencies

- [Management Controller](./management-controller.md)


## Keycloak

Keycloak provides identity and access management for the VMS management controller API and console. Authenticates service admins and VAN users - participants do not require authentication.

### Integration

The management controller uses `openid-client` with:

- **Keycloak adapter** - Client metadata and secret from `keycloak.json`
- **Realm roles** - Authorization on each API route
- **Access tokens** - Verified with realm JWKS (using `jose`)
- **PostgreSQL RLS** - Row-level security using Keycloak groups and user ID from access token

### Configuration Steps

**1. Create Realm**
- Create or choose a realm in Keycloak admin console

**2. Create OIDC Client**
- Confidential client with client authentication enabled
- Standard flow (authorization code)
- Set valid redirect URIs (e.g., `http://localhost:8085/*`)
- Configure group membership mapper:
  - Token claim name: `clientGroups`
  - Full group path: OFF

**3. Download adapter config**
- Download `keycloak.json` from client settings
- Place in `components/management-controller/keycloak.json` (local dev)
- Or create Kubernetes secret `keycloak-config` (deployment)

**4. Create Realm Roles**

Primary roles:
- `admin` - Full access
- `application-deployer`
- `application-owner`
- `backbone-owner`
- `van-owner`
- `certificate-manager`

Additional roles for shared permissions:
- `can-list-accesspoints-backbone`
- `can-list-applications`
- `can-list-backbones`
- `can-list-vans`

**5. Configure Groups**
- Groups enable row-level security in PostgreSQL
- Users assigned to groups for scoped access to backbones/VANs

### Authentication Flow

1. User accesses VMS console or API
2. Redirected to Keycloak for authentication
3. Authorization code flow completes at `/auth/callback`
4. Access token contains user ID and groups
5. Management controller verifies token with realm JWKS
6. PostgreSQL RLS enforces access based on token claims

### Who Needs Keycloak

**Require authentication:**
- Service administrators
- Backbone administrators
- VAN users

**No authentication required:**
- Participants (invitation claim certificate is credential)

## Source

Based on `human/vms/docs/notes/keycloak-setup.md`
