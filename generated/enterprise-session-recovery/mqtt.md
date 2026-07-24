---
type: EnterpriseSessionRecoveryPage
title: "MQTT"
id: mqtt
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/mqtt
tags:
  - skupper
  - enterprise-session-recovery
  - data-messaging
related:
  - events-messaging
  - keepalive-timeouts
  - reconnectable-session
  - tcp
  - tls
---

# MQTT

Data and messaging protocols vary sharply: durable brokers fit better than direct, socket-bound databases.

## Skupper Suitability

Skupper is a reasonable fit for MQTT over TCP when client IDs, clean-session settings, keepalives, and reconnect behavior are configured for the desired recovery semantics. It is not suitable for non-TCP MQTT transports.

## Appears in

- Enterprise Traffic Patterns / Data and Messaging

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Reconnectable Session, Keepalive (and Timeouts), TLS, TCP.

Dependencies:

- [Reconnectable Session](./reconnectable-session.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
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
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
