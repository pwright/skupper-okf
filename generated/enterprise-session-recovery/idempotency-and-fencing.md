---
type: EnterpriseSessionRecoveryPage
title: "Idempotency (deduplication and fencing)"
id: idempotency-and-fencing
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/idempotency-and-fencing
tags:
  - skupper
  - enterprise-session-recovery
  - protocol-state
related:
  - broker-database-endpoints
  - durable-position-recovery
  - reconnect-and-retry
  - transaction-outcome
---

# Idempotency (deduplication and fencing)

This is protocol or application state. Skupper does not store it, but it can keep the required endpoints reachable after a path or site change.

## Skupper Suitability

Skupper does not provide idempotency or fencing. It can make retries possible by restoring connectivity, but the application, broker, or database must prevent duplicate side effects and stale writers.

## Appears in

- Enterprise TCP Sessions and Recovery / State Above TCP

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Broker (and database endpoints).

Dependencies:

- [Broker (and database endpoints)](./broker-database-endpoints.md)

Used by:

- [Durable-Position Recovery](./durable-position-recovery.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)
- [Known Transaction Outcome](./transaction-outcome.md)

## Related Skupper Docs

- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Listener concept](../concepts/listener.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
