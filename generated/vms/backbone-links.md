---
type: VmsLandscapePage
title: "Backbone Links"
id: backbone-links
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/backbone-links
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Backbone Links

Cost-weighted connections between backbone sites - defines relay topology

## Appears in

- [VMS Network Topology Management](./vms-overview.md) / Topology Capabilities

## Topics

### Dependencies

- [Backbone Site](./backbone-site.md)


## Backbone Links

Cost-weighted connections between backbone sites define the relay topology. Links enable routers to forward traffic through the multi-tenant backbone.

### Link Configuration

Links are created between backbone sites with properties:

- **Access point** - The access point on one site (peer type)
- **Connecting site** - The site that will connect to the access point
- **Cost** - Routing metric (default: 1, configurable via `--cost` flag)

### Sync to Sites

Links are synchronized from management controller to site controllers:

**Sync payload** (record key: `link-<link-id>`):
- host
- port
- cost

**Target object** (Kubernetes CR):
```yaml
apiVersion: skupper.io/v2alpha1
kind: Link
metadata:
  name: vms-link-<link-id>
spec:
  endpoints:
  - group: skupper-router
    host: <host>
    name: inter-router
    port: <port>
  tlsCredentials: vms-site-<local-site-id>
  cost: <cost>
```

### Cost-weighted Routing

Routers use link costs to calculate optimal paths:

- Lower cost = preferred path
- Multiple paths available for failover
- Automatic route calculation by Skupper router
- No manual route configuration required

### Link Creation Workflow

1. **Service admin creates link** - Via VMS console or CLI
2. **Management controller stores link** - In PostgreSQL
3. **Hash notification sent** - To affected site controllers
4. **Site controllers sync** - Generate Link CRs on their routers
5. **Routers connect** - Establish inter-router connection
6. **Routes calculated** - Routers determine optimal paths based on costs

### Topology Planning

Admins design backbone topology considering:

- **Geographic distribution** - Place sites near application deployments
- **Network boundaries** - Use DMZ sites to bridge restricted networks
- **Performance** - Low cost for high-bandwidth/low-latency links
- **Availability** - Multiple paths for redundancy

## Source

Based on `human/vms/docs/notes/objects.md`
