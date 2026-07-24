---
type: EnterpriseSessionRecoveryPage
title: "TCP Connection"
id: tcp-connection
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/tcp-connection
tags:
  - skupper
  - enterprise-session-recovery
  - transport
related:
  - connection-pool
  - failure-detection
  - heartbeat-and-keepalive
  - network-path
  - same-tcp-continuity
---

# TCP Connection

This is transport or path behavior. Skupper is relevant where the workload speaks TCP through a listener and connector.

## Skupper Suitability

Skupper is a good fit for providing private TCP reachability, not for guaranteeing lifetime continuity of a single TCP connection. Designs should assume connections can break and verify client reconnect behavior.

## Appears in

- Enterprise TCP Sessions and Recovery / TCP and Network Path

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Network Path.

Dependencies:

- [Network Path](./network-path.md)

Used by:

- [Connection Pool](./connection-pool.md)
- [Failure Detection](./failure-detection.md)
- [Heartbeats (and TCP keepalive)](./heartbeat-and-keepalive.md)
- [Same TCP Connection](./same-tcp-continuity.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
