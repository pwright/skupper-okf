---
type: EnterpriseSessionRecoveryPage
title: "WebSocket"
id: websocket
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/websocket
tags:
  - skupper
  - enterprise-session-recovery
  - web-interactive
related:
  - keepalive-timeouts
  - socket-bound
  - tcp
  - tls
  - web-api-access
---

# WebSocket

This protocol family has mixed fit with Skupper: TCP-based HTTP and gRPC are natural candidates, while QUIC requires a non-Skupper UDP path or a protocol translation layer.

## Skupper Suitability

Skupper can provide private TCP reachability for WebSocket, but it does not preserve the same TCP socket across link, router, NAT, proxy, or endpoint failure. Treat Skupper as a connection-replacement path and require explicit application recovery.

## Appears in

- Enterprise Traffic Patterns / Web and Interactive

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Socket-Bound Session, Keepalive (and Timeouts), TLS, TCP.

Dependencies:

- [Socket-Bound Session](./socket-bound.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)

Used by:

- [Web (and APIs)](./web-api-access.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
