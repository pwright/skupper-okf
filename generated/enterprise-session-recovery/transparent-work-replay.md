---
type: EnterpriseSessionRecoveryPage
title: "Transparent Replay (session and work)"
id: transparent-work-replay
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/transparent-work-replay
tags:
  - skupper
  - enterprise-session-recovery
  - recovery-semantics
related:
  - automatic-reconnect-failover
  - oracle-tac-stack
  - tracked-session-state
  - transaction-outcome
---

# Transparent Replay (session and work)

This recovery behavior sits above TCP. Skupper can make the replacement path reachable, but the protocol or client must restore the logical state.

## Skupper Suitability

Skupper can support transparent work replay when a higher-level stack records calls, session state, and transaction outcomes. The replay mechanism is outside Skupper; Skupper only needs to provide a replacement path to a suitable endpoint.

## Appears in

- Enterprise TCP Sessions and Recovery / Recovery Semantics

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Tracked Session State, Known Transaction Outcome, Automatic Reconnect (and failover).

Dependencies:

- [Tracked Session State](./tracked-session-state.md)
- [Known Transaction Outcome](./transaction-outcome.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)

Used by:

- [Oracle TAC (JDBC Replay + UCP)](./oracle-tac-stack.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
