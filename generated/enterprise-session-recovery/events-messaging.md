---
type: EnterpriseSessionRecoveryPage
title: "Events (and Messaging)"
id: events-messaging
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/events-messaging
tags:
  - skupper
  - enterprise-session-recovery
  - uses
related:
  - amqp-jms
  - kafka
  - mqtt
---

# Events (and Messaging)

This is an enterprise traffic use case. Skupper fit depends on whether the workload can run over TCP and tolerate connection replacement.

## Skupper Suitability

Skupper is a strong fit for many event and messaging systems because brokers and clients commonly include reconnect, acknowledgements, durable queues, or durable offsets. Validate broker endpoint discovery and duplicate-message behavior rather than expecting transport continuity.

## Appears in

- Enterprise Traffic Patterns / Enterprise Uses

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Kafka, AMQP (and JMS), MQTT.

Dependencies:

- [Kafka](./kafka.md)
- [AMQP (and JMS)](./amqp-jms.md)
- [MQTT](./mqtt.md)

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
