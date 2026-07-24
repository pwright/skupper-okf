---
type: EnterpriseSessionRecoveryPage
title: "Kafka"
id: kafka
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/kafka
tags:
  - skupper
  - enterprise-session-recovery
  - data-messaging
related:
  - durable-position
  - events-messaging
  - reconnect-retry
  - tcp
  - tls
---

# Kafka

Data and messaging protocols vary sharply: durable brokers fit better than direct, socket-bound databases.

## Skupper Suitability

Skupper is a good fit for Kafka clients that already use broker discovery, reconnect, durable offsets, and idempotent processing patterns. The design must still validate advertised listener configuration and observe reconnect behavior under link failure.

## Appears in

- Enterprise Traffic Patterns / Data and Messaging

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Durable Position, Reconnect (and Retry), TLS, TCP.

Dependencies:

- [Durable Position](./durable-position.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)

Used by:

- [Events (and Messaging)](./events-messaging.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
