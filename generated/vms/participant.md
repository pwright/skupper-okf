---
type: VmsLandscapePage
title: "Participant"
id: participant
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/participant
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Participant

Accepts invitations and manages local access points - no central authentication required, invitation claim is the only credential

## Appears in

- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md) / User Personas

## Topics

- This item has no documented dependencies.


## Participant Persona

Participants join VANs by accepting invitations. They manage local access points but require no central authentication.

### Responsibilities

- **Accept VAN invitations** - Apply invitation YAML to their environment
- **Manage local access points** - View and deploy connectors/listeners for their services
- **Monitor local site status** - View site health and connectivity
- **Approve configuration** - Optionally approve access point deployment (interactive mode)

### Access Level

- **No central authentication required** - Invitation claim certificate is the only credential
- Local-only view via site controller API
- Cannot see other VAN members
- Cannot create or manage VANs

### Invitation-based Onboarding

1. **Receive invitation** - VAN owner delivers invitation YAML via any channel (email, docs, repo)
2. **Apply YAML** - Deploy to local environment with `kubectl apply` or equivalent
3. **Automatic join** - Site controller handles claim redemption and certificate exchange
4. **Access granted** - Participant can now use VAN services and expose their own

### Typical Workflows

1. **Join VAN** - Apply invitation YAML to join application network
2. **Deploy access points** - Configure local connectors to expose services
3. **Monitor connectivity** - Check site status and VAN accessibility
4. **Leave VAN** - Remove site controller deployment when participation ends

### Tools

- Site controller local API/console
- Standard Kubernetes tooling (`kubectl`)
- Application-specific deployment tools

### Security Model

- **Distributed domain of trust** - No need to authenticate to other participants
- **Network isolation** - Only explicitly exposed services are accessible
- **Temporal access** - Invitation may have join deadline
- **Revocation** - VAN owner can evict participant at any time

## Source

Based on `human/vms/README.md`
