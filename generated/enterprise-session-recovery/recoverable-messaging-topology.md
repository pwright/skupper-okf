---
type: EnterpriseSessionRecoveryPage
title: "Recoverable Topology"
id: recoverable-messaging-topology
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/recoverable-messaging-topology
tags:
  - skupper
  - enterprise-session-recovery
  - outcomes
related:
  - mqtt-paho-stack
  - rabbitmq-qpid-stack
---

# Recoverable Topology

This outcome is an application-level recovery goal, not a property of the network path alone.

## Skupper Suitability

Skupper is a good fit for recoverable messaging topologies when clients can reconnect, redeclare or recover topology, and rely on broker acknowledgements or durable subscriptions. Treat topology recovery as broker/client behavior, not Skupper behavior.

## Appears in

- Enterprise TCP Sessions and Recovery / Application Outcomes

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: AMQP (RabbitMQ or Qpid JMS), MQTT (Paho Java).

Dependencies:

- [AMQP (RabbitMQ or Qpid JMS)](./rabbitmq-qpid-stack.md)
- [MQTT (Paho Java)](./mqtt-paho-stack.md)

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
