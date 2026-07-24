---
type: EnterpriseSessionRecoveryPage
title: "RDP"
id: rdp
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/rdp
tags:
  - skupper
  - enterprise-session-recovery
  - web-interactive
related:
  - reconnectable-session
  - remote-access
  - tcp
  - udp
---

# RDP

This protocol family has mixed fit with Skupper: TCP-based HTTP and gRPC are natural candidates, while QUIC requires a non-Skupper UDP path or a protocol translation layer.

## Skupper Suitability

Skupper is a weak fit for RDP in normal desktop-access scenarios. RDP may use UDP and has interactive-session expectations; only consider Skupper for TCP-only access where reconnect behavior and user-visible interruption are acceptable.

## Appears in

- Enterprise Traffic Patterns / Web and Interactive

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Reconnectable Session, TCP, UDP.

Dependencies:

- [Reconnectable Session](./reconnectable-session.md)
- [TCP](./tcp.md)
- [UDP](./udp.md)

Used by:

- [Remote Access](./remote-access.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
