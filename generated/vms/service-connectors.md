---
type: VmsLandscapePage
title: "Service Connectors"
id: service-connectors
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/service-connectors
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Service Connectors

Access points that connect to local services - expose services to the VAN

## Appears in

- [VMS Control & Data Plane Architecture](./vms-overview.md) / Data Plane (Skupper Routers)

## Topics

### Dependencies

- [Skupper Router Network](./skupper-router.md)


## Service Connectors

Access points that connect to local services - expose services to the VAN so remote members can consume them.

### Purpose

Connectors make local services available across the VAN:

- **Expose service** - Local service becomes accessible to VAN members
- **Outbound connections** - Connector establishes connections to local service
- **Location transparent** - Remote consumers don't know service location
- **Load balancing** - Multiple connectors for same service distribute load

### How Connectors Work

1. **VAN member has local service** - e.g., database running on localhost:5432
2. **Create connector** - Define access point connecting to that service
3. **Service exposed to VAN** - Other members can access via service name
4. **Router forwards traffic** - Skupper router routes requests to connector
5. **Connector proxies** - Establishes connection to local service

### Connector Configuration

Connectors define:

- **Routing key** - Service name used by consumers
- **Host** - Local hostname or IP where service runs
- **Port** - Local port where service listens
- **Protocol** - Application protocol (HTTP, TCP, etc.)

### VAN Access Pattern

**Consumer (uses listener):**
```
Application → Listener → Router → Backbone → Router → Connector → Service
```

The application connects to a listener, which appears local but actually routes through the VAN to the connector, which connects to the real service.

### Multiple Connectors

Multiple members can expose the same service:

- **Load distribution** - Connections distributed across connectors
- **High availability** - Service remains available if one site fails
- **Geographic distribution** - Service replicas in multiple locations
- **Routing preference** - Lower-cost paths preferred

### Deployment

**Management controller pushes config** to member sites:
- Access point definition sent via in-band sync
- Site controller generates Kubernetes CR
- Participant approves or auto-deploys
- Router begins accepting traffic

**Participant approval** (interactive mode):
- Access point config presented to participant
- Participant reviews and approves
- Local deployment after approval

### Example Use Case

**Database exposure:**

Site A runs PostgreSQL locally on port 5432.

1. Site A creates connector: `routing-key: "postgres"`, `host: "localhost"`, `port: 5432`
2. VAN members can connect to "postgres" service
3. Listener on Site B accepts connections for "postgres"
4. Application on Site B connects to listener
5. Traffic routed through VAN to Site A's connector
6. Connector establishes connection to localhost:5432

Application on Site B uses database on Site A without knowing its location.

## Source

Based on `human/vms/docs/notes/model.md`
