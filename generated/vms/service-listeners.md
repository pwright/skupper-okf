---
type: VmsLandscapePage
title: "Service Listeners"
id: service-listeners
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/service-listeners
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Service Listeners

Access points that listen for service traffic - consume services from the VAN

## Appears in

- [VMS Control & Data Plane Architecture](./vms-overview.md) / Data Plane (Skupper Routers)

## Topics

### Dependencies

- [Skupper Router Network](./skupper-router.md)


## Service Listeners

Access points that listen for service traffic - consume services from the VAN exposed by remote connectors.

### Purpose

Listeners make remote services available locally:

- **Consume remote service** - Access service running on another VAN member
- **Inbound connections** - Listener accepts connections from local applications
- **Location transparent** - Applications connect locally, traffic routed to remote service
- **Automatic routing** - Router selects optimal connector based on cost

### How Listeners Work

1. **Remote service exposed** - Another VAN member has connector for a service
2. **Create listener** - Define access point listening for that service
3. **Local access** - Applications connect to listener as if service is local
4. **Router routes traffic** - Skupper router forwards to appropriate connector
5. **Connector proxies** - Establishes connection to actual service

### Listener Configuration

Listeners define:

- **Routing key** - Service name to consume (matches connector's routing key)
- **Host** - Local bind address (e.g., "localhost" or "0.0.0.0")
- **Port** - Local port where listener accepts connections
- **Protocol** - Application protocol (must match connector)

### VAN Access Pattern

**Application flow:**
```
Application → Listener → Router → Backbone → Router → Connector → Service
```

The application connects to what appears to be a local service, but traffic is transparently routed through the VAN to the remote service.

### Multiple Connectors

If multiple members expose the same service (same routing key):

- **Load distribution** - Listener connections distributed across available connectors
- **Failover** - If one connector fails, traffic routes to others
- **Cost-based routing** - Lower-cost paths preferred
- **Geographic preference** - Closer connectors preferred

### Deployment

**Management controller pushes config** to member sites:
- Access point definition sent via in-band sync
- Site controller generates Kubernetes CR
- Participant approves or auto-deploys
- Listener begins accepting connections

**Participant approval** (interactive mode):
- Access point config presented to participant
- Participant reviews listener definition
- Local deployment after approval
- Applications can now connect

### Example Use Case

**Database consumption:**

Site A runs PostgreSQL with connector (`routing-key: "postgres"`).
Site B wants to access the database.

1. Site B creates listener: `routing-key: "postgres"`, `host: "localhost"`, `port: 5432`
2. Listener binds to localhost:5432 on Site B
3. Application on Site B connects to localhost:5432
4. Traffic routed through VAN to Site A's connector
5. Connector connects to actual PostgreSQL
6. Application on Site B uses database without knowing its location

From the application's perspective, PostgreSQL is running locally.

### Service Discovery

Applications don't need service discovery:

- **Fixed address** - Applications connect to listener's host:port
- **Consistent name** - Same routing key across VAN
- **No DNS updates** - No need to track service locations
- **Configuration simplicity** - Connection strings don't change

## Source

Based on `human/vms/docs/notes/model.md`
