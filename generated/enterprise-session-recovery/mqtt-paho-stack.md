---
type: EnterpriseSessionRecoveryPage
title: "MQTT (Paho Java)"
id: mqtt-paho-stack
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/mqtt-paho-stack
tags:
  - skupper
  - enterprise-session-recovery
  - software-stacks
related:
  - bounded-session-resumption
  - logical-session-resume
  - recoverable-messaging-topology
  - topology-reconstruction
---

# MQTT (Paho Java)

This stack can use Skupper as private TCP reachability between client and service endpoints; recovery semantics remain owned by the client library, broker, or database.

## Skupper Suitability

Skupper is a reasonable fit for Paho MQTT clients over TCP when client IDs, session expiry, keepalives, and automatic reconnect are deliberately configured. Skupper provides reachability; MQTT session settings determine what is resumed.

## Appears in

- Enterprise TCP Sessions and Recovery / Enterprise Software and Java Clients

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Session Resumption, Topology Reconstruction (and subscriptions).

Dependencies:

- [Session Resumption](./logical-session-resume.md)
- [Topology Reconstruction (and subscriptions)](./topology-reconstruction.md)

Used by:

- [Bounded Resumption](./bounded-session-resumption.md)
- [Recoverable Topology](./recoverable-messaging-topology.md)

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
