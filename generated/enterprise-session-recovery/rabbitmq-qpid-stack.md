---
type: EnterpriseSessionRecoveryPage
title: "AMQP (RabbitMQ or Qpid JMS)"
id: rabbitmq-qpid-stack
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/rabbitmq-qpid-stack
tags:
  - skupper
  - enterprise-session-recovery
  - software-stacks
related:
  - reconnect-and-retry
  - recoverable-messaging-topology
  - topology-reconstruction
---

# AMQP (RabbitMQ or Qpid JMS)

This stack can use Skupper as private TCP reachability between client and service endpoints; recovery semantics remain owned by the client library, broker, or database.

## Skupper Suitability

Skupper is a reasonable fit for RabbitMQ or Qpid JMS when clients can reconnect and reconstruct channels, consumers, and subscriptions. Treat topology reconstruction and acknowledgement behavior as application or broker responsibilities, not Skupper guarantees.

## Appears in

- Enterprise TCP Sessions and Recovery / Enterprise Software and Java Clients

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Topology Reconstruction (and subscriptions), Reconnect (and retry).

Dependencies:

- [Topology Reconstruction (and subscriptions)](./topology-reconstruction.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)

Used by:

- [Recoverable Topology](./recoverable-messaging-topology.md)

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
