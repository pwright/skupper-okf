---
type: EnterpriseSessionRecoveryPage
title: "SIP (and RTP)"
id: sip-rtp
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/sip-rtp
tags:
  - skupper
  - enterprise-session-recovery
  - office-ops
related:
  - office-operations
  - reconnectable-session
  - tcp
  - udp
---

# SIP (and RTP)

Office operations protocols are mixed; TCP request flows fit better than UDP broadcast or real-time media flows.

## Skupper Suitability

Skupper is generally a poor fit for SIP and RTP as a complete voice or media path because RTP commonly uses UDP port ranges and real-time behavior. A TCP-only SIP control endpoint might be reachable through Skupper, but media traversal should be designed separately.

## Appears in

- Enterprise Traffic Patterns / Office and Operations

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Reconnectable Session, UDP, TCP.

Dependencies:

- [Reconnectable Session](./reconnectable-session.md)
- [UDP](./udp.md)
- [TCP](./tcp.md)

Used by:

- [Office Operations](./office-operations.md)

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
