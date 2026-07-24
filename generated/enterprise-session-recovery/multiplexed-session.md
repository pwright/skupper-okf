---
type: EnterpriseSessionRecoveryPage
title: "Multiplexed Session"
id: multiplexed-session
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/multiplexed-session
tags:
  - skupper
  - enterprise-session-recovery
  - session-behaviour
related:
  - http2-grpc
  - http3-quic
  - keepalive-timeouts
  - tcp
---

# Multiplexed Session

This behavior describes how much state survives connection loss. Skupper does not convert socket-bound state into resumable state.

## Skupper Suitability

Skupper is a good fit for multiplexed TCP protocols such as HTTP/2 when callers can retry interrupted streams. It does not preserve an individual stream across a broken connection.

## Appears in

- Enterprise Traffic Patterns / Session Behaviour

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: TCP, Keepalive (and Timeouts).

Dependencies:

- [TCP](./tcp.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)

Used by:

- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [HTTP/3 (QUIC)](./http3-quic.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
