---
type: EnterpriseSessionRecoveryPage
title: "Connection Replacement"
id: connection-replacement
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/connection-replacement
tags:
  - skupper
  - enterprise-session-recovery
  - recovery-semantics
related:
  - connection-pool
  - failure-detection
  - ordinary-jdbc-stack
---

# Connection Replacement

This recovery behavior sits above TCP. Skupper can make the replacement path reachable, but the protocol or client must restore the logical state.

## Skupper Suitability

Skupper fits connection replacement patterns well because clients can reconnect to the same exposed service address while Skupper manages private reachability to the target endpoint. It does not decide whether an operation is safe to retry.

## Appears in

- Enterprise TCP Sessions and Recovery / Recovery Semantics

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Connection Pool, Failure Detection.

Dependencies:

- [Connection Pool](./connection-pool.md)
- [Failure Detection](./failure-detection.md)

Used by:

- [JDBC (PostgreSQL or MySQL + HikariCP)](./ordinary-jdbc-stack.md)

## Related Skupper Docs

- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
