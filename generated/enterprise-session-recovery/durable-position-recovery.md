---
type: EnterpriseSessionRecoveryPage
title: "Durable-Position Recovery"
id: durable-position-recovery
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/durable-position-recovery
tags:
  - skupper
  - enterprise-session-recovery
  - recovery-semantics
related:
  - automatic-reconnect-failover
  - durable-checkpoint
  - ibm-mq-jms-stack
  - idempotency-and-fencing
  - kafka-java-stack
---

# Durable-Position Recovery

This recovery behavior sits above TCP. Skupper can make the replacement path reachable, but the protocol or client must restore the logical state.

## Skupper Suitability

Skupper is a good fit for durable-position recovery when clients can reconnect and resume from committed offsets, cursors, or checkpoints. The important validation is that reconnect paths, duplicate handling, and checkpoint advancement behave correctly during Skupper link or endpoint failure.

## Appears in

- Enterprise TCP Sessions and Recovery / Recovery Semantics

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Durable Checkpoint (offset or cursor), Idempotency (deduplication and fencing), Automatic Reconnect (and failover).

Dependencies:

- [Durable Checkpoint (offset or cursor)](./durable-checkpoint.md)
- [Idempotency (deduplication and fencing)](./idempotency-and-fencing.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)

Used by:

- [IBM MQ (JMS)](./ibm-mq-jms-stack.md)
- [Kafka (Java Client or Spring)](./kafka-java-stack.md)

## Related Skupper Docs

- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)
- [Traffic baseline](../skupper-docs-landscape/traffic-baseline.md)
- [Evidence bundle](../skupper-docs-landscape/evidence-bundle.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
