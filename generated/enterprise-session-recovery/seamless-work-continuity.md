---
type: EnterpriseSessionRecoveryPage
title: "Seamless Continuity"
id: seamless-work-continuity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/seamless-work-continuity
tags:
  - skupper
  - enterprise-session-recovery
  - outcomes
related:
  - oracle-tac-stack
---

# Seamless Continuity

This outcome is an application-level recovery goal, not a property of the network path alone.

## Skupper Suitability

Skupper alone does not provide seamless work continuity. It can support this outcome only when the application stack, such as Oracle TAC, records enough session and transaction state to replay work after a new connection is established.

## Appears in

- Enterprise TCP Sessions and Recovery / Application Outcomes

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Oracle TAC (JDBC Replay + UCP).

Dependencies:

- [Oracle TAC (JDBC Replay + UCP)](./oracle-tac-stack.md)

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
