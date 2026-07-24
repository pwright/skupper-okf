---
type: EnterpriseSessionRecoveryPage
title: "AMQP (and JMS)"
id: amqp-jms
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/amqp-jms
tags:
  - skupper
  - enterprise-session-recovery
  - data-messaging
related:
  - durable-position
  - events-messaging
  - reconnectable-session
  - tcp
  - tls
---

# AMQP (and JMS)

Data and messaging protocols vary sharply: durable brokers fit better than direct, socket-bound databases.

## Skupper Suitability

Skupper is a good fit for AMQP and JMS traffic when the broker and client library provide reconnect, durable queues, acknowledgements, and redelivery semantics. Skupper handles the private TCP path; the messaging layer owns delivery guarantees.

## Appears in

- Enterprise Traffic Patterns / Data and Messaging

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Reconnectable Session, Durable Position, TLS, TCP.

Dependencies:

- [Reconnectable Session](./reconnectable-session.md)
- [Durable Position](./durable-position.md)
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
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
