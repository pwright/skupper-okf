---
type: EnterpriseSessionRecoveryPage
title: "Durable Position"
id: durable-position
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/durable-position
tags:
  - skupper
  - enterprise-session-recovery
  - session-behaviour
related:
  - amqp-jms
  - kafka
  - reconnect-retry
---

# Durable Position

This behavior describes how much state survives connection loss. Skupper does not convert socket-bound state into resumable state.

## Skupper Suitability

Skupper fits durable-position workloads well because the application can replace a broken TCP connection and continue from a stored position. Skupper should be evaluated for reachability, latency, and flow visibility, while the broker or application owns offset correctness.

## Appears in

- Enterprise Traffic Patterns / Session Behaviour

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Reconnect (and Retry).

Dependencies:

- [Reconnect (and Retry)](./reconnect-retry.md)

Used by:

- [AMQP (and JMS)](./amqp-jms.md)
- [Kafka](./kafka.md)

## Related Skupper Docs

- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
