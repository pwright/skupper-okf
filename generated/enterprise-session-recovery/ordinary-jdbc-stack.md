---
type: EnterpriseSessionRecoveryPage
title: "JDBC (PostgreSQL or MySQL + HikariCP)"
id: ordinary-jdbc-stack
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/ordinary-jdbc-stack
tags:
  - skupper
  - enterprise-session-recovery
  - software-stacks
related:
  - connection-replacement
  - explicit-application-recovery
  - same-tcp-continuity
---

# JDBC (PostgreSQL or MySQL + HikariCP)

This stack can use Skupper as private TCP reachability between client and service endpoints; recovery semantics remain owned by the client library, broker, or database.

## Skupper Suitability

Skupper can provide private TCP reachability for JDBC clients, including PostgreSQL or MySQL through HikariCP, but it does not preserve the same database connection after path failure. Use pool replacement, bounded retries, transaction outcome checks, and application idempotency.

## Appears in

- Enterprise TCP Sessions and Recovery / Enterprise Software and Java Clients

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Same TCP Connection, Connection Replacement.

Dependencies:

- [Same TCP Connection](./same-tcp-continuity.md)
- [Connection Replacement](./connection-replacement.md)

Used by:

- [Application Recovery](./explicit-application-recovery.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
