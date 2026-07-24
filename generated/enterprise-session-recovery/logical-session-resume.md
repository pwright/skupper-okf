---
type: EnterpriseSessionRecoveryPage
title: "Session Resumption"
id: logical-session-resume
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/logical-session-resume
tags:
  - skupper
  - enterprise-session-recovery
  - recovery-semantics
related:
  - automatic-reconnect-failover
  - ibm-mq-jms-stack
  - mqtt-paho-stack
  - session-expiry-window
  - session-identity
  - zookeeper-curator-stack
---

# Session Resumption

This recovery behavior sits above TCP. Skupper can make the replacement path reachable, but the protocol or client must restore the logical state.

## Skupper Suitability

Skupper works well with protocols that have logical session resume because the application can create a new TCP connection through Skupper and reattach to server-side state. Skupper does not hold or validate the session identity or expiry window.

## Appears in

- Enterprise TCP Sessions and Recovery / Recovery Semantics

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Session Identity, Session Resume Window, Automatic Reconnect (and failover).

Dependencies:

- [Session Identity](./session-identity.md)
- [Session Resume Window](./session-expiry-window.md)
- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)

Used by:

- [IBM MQ (JMS)](./ibm-mq-jms-stack.md)
- [MQTT (Paho Java)](./mqtt-paho-stack.md)
- [ZooKeeper (Curator)](./zookeeper-curator-stack.md)

## Related Skupper Docs

- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
