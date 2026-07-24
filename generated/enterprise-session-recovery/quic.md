---
type: EnterpriseSessionRecoveryPage
title: "QUIC"
id: quic
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/quic
tags:
  - skupper
  - enterprise-session-recovery
  - transport
related:
  - http3-quic
  - udp
---

# QUIC

This is transport or path behavior. Skupper is relevant where the workload speaks TCP through a listener and connector.

## Skupper Suitability

Skupper is a poor fit for native QUIC because QUIC runs over UDP and depends on transport behavior Skupper does not expose as a service path. Use HTTP/1.1 or HTTP/2 to bring web traffic through Skupper, or provide a protocol translation layer outside Skupper.

## Appears in

- Enterprise Traffic Patterns / Transport and Path

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: UDP.

Dependencies:

- [UDP](./udp.md)

Used by:

- [HTTP/3 (QUIC)](./http3-quic.md)

## Related Skupper Docs

- No direct Skupper documentation link is specific enough yet; use the map dependencies above to navigate to related topics.

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
