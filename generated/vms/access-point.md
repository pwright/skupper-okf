---
type: VmsLandscapePage
title: "Access Point"
id: access-point
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/access-point
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Access Point

Ingress points on backbone sites - separate access points for management traffic and VAN traffic

## Appears in

- [VMS Network Topology Management](./vms-overview.md) / Topology Capabilities

## Topics

### Dependencies

- [Backbone Site](./backbone-site.md)


## Access Point Types

Access points define ingress to backbone sites with different kinds:

| Kind    | Purpose                          | CR Type        | Router Role   |
|---------|----------------------------------|----------------|---------------|
| manage  | Management traffic from sites    | RouterAccess   | normal        |
| peer    | Inter-router backbone links      | RouterAccess   | inter-router  |
| claim   | Invitation claim redemption      | RouterAccess   | normal        |
| member  | Member site connections          | RouterAccess   | edge          |
| van     | VAN application traffic          | NetworkAccess  | N/A           |

### Configuration

Access points are configured with:

- **kind** - Type of access point
- **accessType** - Deployment type: `local`, `loadbalancer`, or `route`
- **bindhost** - Optional hostname for socket binding
- **tlsCredentials** - Certificate for mutual TLS

### Sync Process

Access points are synchronized from management controller to site controller:

- Record key: `access-<access-point-id>`
- Site controller generates Kubernetes CR (RouterAccess or NetworkAccess)
- Site reports back host/port status to management controller

## Source

Based on `human/vms/docs/notes/objects.md`
