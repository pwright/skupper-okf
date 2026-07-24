---
type: Concept
title: Client to Listener to Router to Connector Reconnects
id: skupper-concept-client-listener-router-connector-reconnects
status: needs-review
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source_paths:
  - generated/concepts/listener.md
  - generated/concepts/connector.md
  - generated/concepts/routing-key.md
  - generated/maps/enterprise-session-recovery.md
tags:
  - skupper
  - listener
  - connector
  - routing-key
  - reconnects
  - tcp
related:
  - skupper-concept-listener
  - skupper-concept-connector
  - skupper-concept-routing-key
  - enterprise-session-recovery
timestamp: 2026-07-24T00:00:00Z
---

# Client to Listener to Router to Connector Reconnects

This page explains what happens to a client connection that enters Skupper through a listener, crosses one or more routers, and leaves through a connector, especially when part of the path fails and reconnects.

The short version: Skupper can re-establish network reachability between listeners, routers, and connectors, but it does not make one broken TCP connection remain the same TCP connection. If the client-visible connection is broken, application recovery depends on the client protocol and application stack above TCP.

## Path

For a normal TCP service exposed with a Skupper listener and connector, the path is:

```text
client -> listener host:port -> local Skupper router -> remote Skupper router -> connector -> server
```

The listener gives the client a local address. The connector represents the server-side workload. The routing key is the service identity that lets routers match the listener side to a compatible connector side.

There are multiple physical connections in this path:

- `client -> listener`: the client-visible TCP connection.
- `listener/router -> router`: one or more inter-router connections in the Skupper network.
- `connector -> server`: the server-side TCP connection opened by the connector side.

Those are not one continuous operating-system TCP socket from client to server. Skupper bridges traffic across router-managed connections.

## Reconnect Boundaries

When the inter-router path fails and returns, Skupper can reconnect routers and restore routing reachability for the service. New client connections can then flow again to matching connectors.

When a connector can no longer reach its target server, Skupper can detect that the backend side is unavailable and later use the connector again after the backend endpoint is reachable.

When a listener no longer has a matching connector, the listener can still exist as a local endpoint, but service usability depends on whether the router network has a reachable connector for the same routing key.

For an already-established client TCP connection, a failure in any segment of the bridged path can cause that client connection to fail. After that, the client normally needs to open a new TCP connection. Skupper reconnects the transport path; it does not replay arbitrary application state.

## What Skupper Recovers

Skupper is primarily recovering service reachability:

- the listener remains the stable address clients use;
- the routing key remains the stable service identity inside the application network;
- routers can reconnect to other routers after link or site-path interruption;
- connectors can become usable again when their selected backend workload is reachable.

That recovery is valuable because clients do not need to know the remote site address, backend pod address, or inter-site route. The Skupper service identity remains the listener and routing key.

## What Skupper Does Not Recover

Skupper does not generally provide same-TCP-session continuity across a broken path. It also does not know whether an application request was safe to replay unless the application protocol or client library provides that semantic.

Examples:

- A plain JDBC connection through Skupper should be treated as a physical connection that can be replaced after failure, not as a transparent continuation of the same database session.
- A messaging client with durable subscriptions, offsets, acknowledgements, or a client session identity may rebuild more state after reconnect, but that recovery is provided by the messaging protocol, broker, and client library.
- A request-response protocol can retry safely only when the operation is idempotent, fenced, deduplicated, or otherwise designed for retry.

## Recovery Model

Use [Enterprise TCP Sessions and Recovery](../maps/enterprise-session-recovery.md) as the reference model for this distinction.

In that map, Skupper itself sits closest to the lower layers:

- `TCP Connection`
- `End-to-End Network Path`
- `Connection Failure Detection`
- `Automatic Reconnect and Endpoint Failover`
- `Connection Replacement Only`

The green and amber outcomes in the map require state above TCP: logical session identity, durable checkpoints, transaction outcome tracking, durable delivery topology, or idempotency and fencing. Those capabilities belong to the application protocol, server, broker, database, or client library. Skupper can carry the new connection that participates in recovery, but it is not the component that reconstructs those higher-level semantics.

## Operator View

For operators, separate these questions when diagnosing reconnect behavior:

- Is the listener configured and bound to the expected host and port?
- Does the listener have a matching connector for the same routing key?
- Are routers connected across the sites needed for the route?
- Is the connector able to reach the backend workload?
- Did the client library reconnect and rebuild its own application state?
- If the client retried work, was the operation safe to repeat?

This distinction avoids over-reading a healthy Skupper route as a guarantee that old application sessions survived. A recovered route means the next connection has a path. A recovered application session requires recovery semantics above TCP.
