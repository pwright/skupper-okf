---
type: EnterpriseSessionRecoveryPage
title: "Durable Checkpoint (offset or cursor)"
id: durable-checkpoint
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/durable-checkpoint
tags:
  - skupper
  - enterprise-session-recovery
  - protocol-state
related:
  - broker-database-endpoints
  - durable-position-recovery
---

# Durable Checkpoint (offset or cursor)

This is protocol or application state. Skupper does not store it, but it can keep the required endpoints reachable after a path or site change.

## Skupper Suitability

Skupper supports durable checkpoint patterns indirectly by restoring TCP reachability to the service that owns the checkpoint. It does not store or advance checkpoints, so correctness depends on the consumer, broker, database, or workflow engine.

## Appears in

- Enterprise TCP Sessions and Recovery / State Above TCP

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Broker (and database endpoints).

Dependencies:

- [Broker (and database endpoints)](./broker-database-endpoints.md)

Used by:

- [Durable-Position Recovery](./durable-position-recovery.md)

## Related Skupper Docs

- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)
- [Traffic baseline](../skupper-docs-landscape/traffic-baseline.md)
- [Evidence bundle](../skupper-docs-landscape/evidence-bundle.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Listener concept](../concepts/listener.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
