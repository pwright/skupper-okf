---
type: Concept
title: Network Observer API
id: skupper-concept-network-observer-api
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source_url: "https://deepwiki.com/search/what-parts-of-api-at-httpsgith_b41ecad0-e4e7-450a-8997-72ecb4efb16c?mode=deep"
source_paths:
  - human/skupper-openapi-spec/openapi.yaml
  - human/skupper-docs/input/refdog/concepts/connector.md
  - human/skupper-docs/input/refdog/concepts/listener.md
human_sources:
  - Skupper Network Observer OpenAPI Specification v2alpha1
  - DeepWiki API analysis
tags:
  - skupper
  - network-observer
  - api
  - listener
  - connector
  - routing-key
  - observability
related:
  - skupper-concept-listener
  - skupper-concept-connector
  - skupper-concept-routing-key
timestamp: 2026-07-04T09:30:00Z
---

# Network Observer API

The **Skupper Network Observer API** is a read-only HTTP API that exposes runtime state about a Skupper application network. It provides programmatic access to listeners, connectors, services, connections, and traffic flows—enabling observability, monitoring, and network console frontends.

## Outcome

The Network Observer API gives operators and tools visibility into:

```text
API Query → Network Observer → Real-time state of:
  - Which listeners are configured and where
  - Which connectors are attached and to which processes
  - Whether routing keys are bound (listeners + connectors matched)
  - Active connections and traffic flows
  - Cross-site reachability and topology
```

## API Overview

**Base Path**: `/api/v2alpha1/`

**Format**: RESTful HTTP JSON API (OpenAPI 3.0 specification)

**Authentication**: None (read-only, network-internal service)

**Response Pattern**: All collection endpoints return paginated results with:
- `results`: Array of records
- `count`: Total number of records
- `timeRangeCount`: Number of records in requested time range

## Listeners and Connectors

### Listener Endpoints

#### GET `/api/v2alpha1/listeners`

Returns a paginated list of all listeners in the network.

**Response**: `200 OK` with `ListenerListResponse`

```json
{
  "results": [
    {
      "identity": "listener-abc123",
      "routerId": "router-xyz",
      "name": "backend-listener",
      "destHost": "backend-svc",
      "destPort": "8080",
      "protocol": "tcp",
      "routingKey": "backend",
      "serviceId": "service-backend@tcp",
      "siteId": "site-west",
      "siteName": "West Data Center",
      "startTime": 1720089600000000,
      "endTime": 0
    }
  ],
  "count": 1,
  "timeRangeCount": 1
}
```

#### GET `/api/v2alpha1/listeners/{id}`

Returns a single listener by identity.

**Response**: `200 OK` with `ListenerRecord` or `404 Not Found`

### Connector Endpoints

#### GET `/api/v2alpha1/connectors`

Returns a paginated list of all connectors in the network.

**Response**: `200 OK` with `ConnectorListResponse`

```json
{
  "results": [
    {
      "identity": "connector-def456",
      "routerId": "router-abc",
      "name": "backend-connector",
      "destHost": "10.1.2.3",
      "destPort": "8080",
      "protocol": "tcp",
      "routingKey": "backend",
      "serviceId": "service-backend@tcp",
      "processId": "process-workload-789",
      "target": "deployment/backend",
      "siteId": "site-east",
      "siteName": "East Data Center",
      "startTime": 1720089700000000,
      "endTime": 0
    }
  ],
  "count": 1,
  "timeRangeCount": 1
}
```

#### GET `/api/v2alpha1/connectors/{id}`

Returns a single connector by identity.

**Response**: `200 OK` with `ConnectorRecord` or `404 Not Found`

## Listener Schema

The `ListenerRecord` extends `baseRecord` and provides:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `identity` | string | ✓ | Unique identifier for the record |
| `routerId` | string | ✓ | The router this listener belongs to |
| `name` | string | ✓ | Listener name |
| `destHost` | string | ✓ | Destination hostname (local endpoint) |
| `destPort` | string | ✓ | Destination port (local endpoint) |
| `protocol` | string | ✓ | Transport protocol (tcp, http1, http2) |
| `routingKey` | string | ✓ | Key used to route traffic to matching connectors |
| `serviceId` | string |  | Associated service identifier |
| `siteId` | string | ✓ | Site this listener is in |
| `siteName` | string | ✓ | Human-readable site name |
| `startTime` | uint64 | ✓ | Creation time in microseconds (Unix timestamp) |
| `endTime` | uint64 | ✓ | End time in microseconds (0 = still active) |

### Listener Properties

- **Network-facing entry point**: Listeners accept incoming client connections
- **Local endpoint**: Defined by `destHost` and `destPort` (where clients connect)
- **Routing key binding**: The `routingKey` field links this listener to matching connectors
- **Site-scoped**: Each listener belongs to exactly one site and one router
- **No process binding**: Unlike connectors, listeners are not bound to a specific process

## Connector Schema

The `ConnectorRecord` extends `baseRecord` and provides:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `identity` | string | ✓ | Unique identifier for the record |
| `routerId` | string | ✓ | The router this connector belongs to |
| `name` | string | ✓ | Connector name |
| `destHost` | string | ✓ | Destination host (the backend workload IP) |
| `destPort` | string | ✓ | Destination port (the backend workload port) |
| `protocol` | string | ✓ | Transport protocol (tcp, http1, http2) |
| `routingKey` | string | ✓ | Must match a listener's routing key to form a service |
| `serviceId` | string |  | Associated service identifier |
| `processId` | string | ✓ | The process this connector targets |
| `target` | string | nullable | Target identifier (e.g., `deployment/backend`) |
| `siteId` | string | ✓ | Site this connector is in |
| `siteName` | string | ✓ | Human-readable site name |
| `startTime` | uint64 | ✓ | Creation time in microseconds (Unix timestamp) |
| `endTime` | uint64 | ✓ | End time in microseconds (0 = still active) |

### Connector Properties

- **Backend target**: Connectors deliver traffic to a running workload process
- **Process binding**: The `processId` field links the connector to a specific backend process
- **Routing key binding**: The `routingKey` field links this connector to matching listeners
- **Target metadata**: The optional `target` field provides human-readable context (e.g., Kubernetes workload reference)
- **Site-scoped**: Each connector belongs to exactly one site and one router

## Key Relationship: Routing Keys

**Listeners and connectors are paired by their shared `routingKey`.**

A listener accepts traffic on one side of the Skupper network, and a connector delivers it to a backend process on the other side. The routing key is the sole mechanism for cross-site service discovery.

```text
┌─────────────────────────────────────────────────────────────────┐
│                      Skupper Network                            │
│                                                                 │
│  Site A                                                Site B   │
│  ┌────────────────────┐                    ┌────────────────┐  │
│  │ Listener           │                    │ Connector      │  │
│  │ routingKey: backend│────────────────────│ routingKey:    │  │
│  │ destHost: backend  │   AMQP routing     │  backend       │  │
│  │ destPort: 8080     │                    │ processId: ... │  │
│  └────────────────────┘                    └────────────────┘  │
│           ↑                                        ↓            │
│      Client connects                    Traffic delivered to   │
│      to local endpoint                  backend workload       │
└─────────────────────────────────────────────────────────────────┘
```

### Service Binding Status

The `/api/v2alpha1/services` endpoint exposes service records grouped by routing key:

```json
{
  "identity": "service-backend@tcp",
  "name": "backend",
  "protocol": "tcp",
  "isBound": true,
  "hasListener": true,
  "listenerCount": 1,
  "connectorCount": 2
}
```

- **`isBound: true`**: Both listeners and connectors exist for this routing key
- **`hasListener: true`**: At least one listener is configured
- **`listenerCount`**: Number of listeners with this routing key
- **`connectorCount`**: Number of connectors with this routing key

This status information helps operators verify that cross-site routing is established.

## Difference from Configuration API

The Network Observer API is **read-only** and exposes **runtime state**, not configuration intent:

| Aspect | Configuration API (CRDs) | Network Observer API |
|--------|-------------------------|----------------------|
| **Purpose** | Define desired state | Observe actual state |
| **Scope** | Single site (namespace) | Entire network |
| **Access** | `kubectl`, Skupper CLI | HTTP JSON API |
| **Mutability** | Read-write (create, update, delete) | Read-only (GET only) |
| **Audience** | Operators, CI/CD | Monitoring tools, consoles |
| **Lifecycle** | Kubernetes resources | Ephemeral runtime records |

### Example Workflow

1. **Operator creates a Listener CRD** in Site A (configuration):
   ```yaml
   apiVersion: skupper.io/v2alpha1
   kind: Listener
   metadata:
     name: backend-listener
   spec:
     routingKey: backend
     host: backend-svc
     port: 8080
   ```

2. **Controller processes the CRD** and configures the router.

3. **Network Observer sees the listener** (runtime state):
   ```bash
   curl http://network-observer:8080/api/v2alpha1/listeners
   ```

4. **Monitoring tool checks if the service is bound**:
   ```bash
   curl http://network-observer:8080/api/v2alpha1/services/backend
   # {"isBound": true, "listenerCount": 1, "connectorCount": 2}
   ```

## Additional Resources

The Network Observer API also exposes:

- **Sites**: `/api/v2alpha1/sites` — Skupper sites in the network
- **Routers**: `/api/v2alpha1/routers` — Router instances
- **Processes**: `/api/v2alpha1/processes` — Backend processes
- **Services**: `/api/v2alpha1/services` — Grouped by routing key
- **Connections**: `/api/v2alpha1/connections` — Active network connections
- **Flows**: `/api/v2alpha1/flows` — Application-level traffic flows
- **Flow Aggregates**: `/api/v2alpha1/sitepairs`, `/componentpairs`, `/processpairs`
- **Links**: `/api/v2alpha1/routerlinks`, `/routeraccess` — Inter-router links

All endpoints follow the same paginated response pattern and provide timestamps for time-series analysis.

## Key Properties

- **Read-only**: No mutations allowed (GET-only API)
- **Network-wide scope**: Sees all sites, not just the local one
- **Real-time state**: Reflects current router and controller state
- **Paginated responses**: All collection endpoints support pagination
- **Time-series data**: `startTime` and `endTime` fields enable historical queries
- **Routing key as primary key**: Services, connections, and flows are keyed by routing key
- **No authentication**: Internal network service (not exposed externally)

## Use Cases

- **Network Console UI**: Display real-time topology and traffic flows
- **Monitoring and Alerting**: Query for unbound services, missing connectors, or stale listeners
- **Troubleshooting**: Inspect which processes are connected to which routing keys
- **Capacity Planning**: Analyze traffic volume by routing key over time
- **Automation**: Programmatically verify that service exposure is working before promoting a deployment

## References

- [Skupper Network Observer OpenAPI Specification](../human/skupper-openapi-spec/openapi.yaml)
- [DeepWiki: Network Observer API](https://deepwiki.com/search/what-parts-of-api-at-httpsgith_b41ecad0-e4e7-450a-8997-72ecb4efb16c?mode=deep)
- [Listener Concept](./listener.md)
- [Connector Concept](./connector.md)
- [Routing Key Concept](./routing-key.md)
