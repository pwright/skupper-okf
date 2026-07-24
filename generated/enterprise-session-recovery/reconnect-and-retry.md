---
type: EnterpriseSessionRecoveryPage
title: "Reconnect (and retry)"
id: reconnect-and-retry
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/reconnect-and-retry
tags:
  - skupper
  - enterprise-session-recovery
  - recovery-semantics
related:
  - automatic-reconnect-failover
  - idempotency-and-fencing
  - kafka-java-stack
  - rabbitmq-qpid-stack
  - retry-policy
---

# Reconnect (and retry)

This recovery behavior sits above TCP. Skupper can make the replacement path reachable, but the protocol or client must restore the logical state.

## Skupper Suitability

Skupper fits reconnect-and-retry semantics when a replacement TCP path is enough for the client to continue. It should be paired with clear timeout settings, bounded retry, and idempotency rules.

## Appears in

- Enterprise TCP Sessions and Recovery / Recovery Semantics

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Idempotency (deduplication and fencing), Bounded Retry (and backoff), Automatic Reconnect (and failover).

Dependencies:

- [Idempotency (deduplication and fencing)](./idempotency-and-fencing.md)
- [Bounded Retry (and backoff)](./retry-policy.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)

Used by:

- [Kafka (Java Client or Spring)](./kafka-java-stack.md)
- [AMQP (RabbitMQ or Qpid JMS)](./rabbitmq-qpid-stack.md)

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
