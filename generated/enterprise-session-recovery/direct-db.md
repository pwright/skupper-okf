---
type: EnterpriseSessionRecoveryPage
title: "Direct DB (JDBC/native)"
id: direct-db
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/direct-db
tags:
  - skupper
  - enterprise-session-recovery
  - data-messaging
related:
  - database-access
  - pooled-reuse
  - socket-bound
  - tcp
  - tls
---

# Direct DB (JDBC/native)

Data and messaging protocols vary sharply: durable brokers fit better than direct, socket-bound databases.

## Skupper Suitability

Skupper can expose a direct database endpoint over TCP, but it is not a database session recovery mechanism. Treat disconnects as connection loss, rely on pooling and application retry, and avoid assuming in-flight transactions survive.

## Appears in

- Enterprise Traffic Patterns / Data and Messaging

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Socket-Bound Session, Pooled Reuse, TLS, TCP.

Dependencies:

- [Socket-Bound Session](./socket-bound.md)
- [Pooled Reuse](./pooled-reuse.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)

Used by:

- [Database Access](./database-access.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
