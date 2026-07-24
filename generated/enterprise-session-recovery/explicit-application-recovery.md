---
type: EnterpriseSessionRecoveryPage
title: "Application Recovery"
id: explicit-application-recovery
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/explicit-application-recovery
tags:
  - skupper
  - enterprise-session-recovery
  - outcomes
related:
  - ordinary-jdbc-stack
---

# Application Recovery

This outcome is an application-level recovery goal, not a property of the network path alone.

## Skupper Suitability

Skupper can support application recovery by restoring private reachability, but all correctness work remains in the application: detecting failure, replacing connections, retrying safe operations, and resolving unknown transaction outcomes.

## Appears in

- Enterprise TCP Sessions and Recovery / Application Outcomes

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: JDBC (PostgreSQL or MySQL + HikariCP).

Dependencies:

- [JDBC (PostgreSQL or MySQL + HikariCP)](./ordinary-jdbc-stack.md)

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
