---
type: EnterpriseSessionRecoveryPage
title: "Topology Reconstruction (and subscriptions)"
id: topology-reconstruction
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/topology-reconstruction
tags:
  - skupper
  - enterprise-session-recovery
  - recovery-semantics
related:
  - automatic-reconnect-failover
  - durable-delivery-topology
  - mqtt-paho-stack
  - rabbitmq-qpid-stack
---

# Topology Reconstruction (and subscriptions)

This recovery behavior sits above TCP. Skupper can make the replacement path reachable, but the protocol or client must restore the logical state.

## Skupper Suitability

Skupper is a reasonable fit for topology reconstruction when clients can reconnect and rebuild channels, subscriptions, consumers, or service declarations. It provides the path for reconstruction; the protocol defines what must be rebuilt and what remains durable.

## Appears in

- Enterprise TCP Sessions and Recovery / Recovery Semantics

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Durable Delivery State (and topology), Automatic Reconnect (and failover).

Dependencies:

- [Durable Delivery State (and topology)](./durable-delivery-topology.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)

Used by:

- [MQTT (Paho Java)](./mqtt-paho-stack.md)
- [AMQP (RabbitMQ or Qpid JMS)](./rabbitmq-qpid-stack.md)

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
