---
type: EnterpriseSessionRecoveryPage
title: "Database Access"
id: database-access
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/database-access
tags:
  - skupper
  - enterprise-session-recovery
  - uses
related:
  - direct-db
  - redis
---

# Database Access

This is an enterprise traffic use case. Skupper fit depends on whether the workload can run over TCP and tolerate connection replacement.

## Skupper Suitability

Skupper is a mixed fit for database access. It is useful for private TCP reachability to a database endpoint, but direct database sessions are often socket-bound; production designs need connection pools, retry rules, transaction outcome handling, and idempotency.

## Appears in

- Enterprise Traffic Patterns / Enterprise Uses

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Direct DB (JDBC/native), Redis Protocol.

Dependencies:

- [Direct DB (JDBC/native)](./direct-db.md)
- [Redis Protocol](./redis.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
