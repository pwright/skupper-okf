---
type: EnterpriseSessionRecoveryPage
title: "Same TCP Connection"
id: same-tcp-continuity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/same-tcp-continuity
tags:
  - skupper
  - enterprise-session-recovery
  - recovery-semantics
related:
  - heartbeat-and-keepalive
  - ordinary-jdbc-stack
  - tcp-connection
---

# Same TCP Connection

This recovery behavior sits above TCP. Skupper can make the replacement path reachable, but the protocol or client must restore the logical state.

## Skupper Suitability

Skupper is a poor fit if the requirement is preserving the exact same TCP connection across failures. Skupper can reconnect routers and re-establish service paths, but existing application sockets still break and must be replaced.

## Appears in

- Enterprise TCP Sessions and Recovery / Recovery Semantics

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Heartbeats (and TCP keepalive), TCP Connection.

Dependencies:

- [Heartbeats (and TCP keepalive)](./heartbeat-and-keepalive.md)
- [TCP Connection](./tcp-connection.md)

Used by:

- [JDBC (PostgreSQL or MySQL + HikariCP)](./ordinary-jdbc-stack.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
