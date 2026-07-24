---
type: EnterpriseSessionRecoveryPage
title: "Bounded Resumption"
id: bounded-session-resumption
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/bounded-session-resumption
tags:
  - skupper
  - enterprise-session-recovery
  - outcomes
related:
  - mqtt-paho-stack
  - zookeeper-curator-stack
---

# Bounded Resumption

This outcome is an application-level recovery goal, not a property of the network path alone.

## Skupper Suitability

Skupper can support bounded session resumption when the protocol has an explicit resume window and clients reconnect promptly. Skupper helps restore the path, but the timeout budget must account for client detection, Skupper link recovery, and server-side session expiry.

## Appears in

- Enterprise TCP Sessions and Recovery / Application Outcomes

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: ZooKeeper (Curator), MQTT (Paho Java).

Dependencies:

- [ZooKeeper (Curator)](./zookeeper-curator-stack.md)
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
