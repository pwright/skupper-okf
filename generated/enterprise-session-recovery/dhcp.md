---
type: EnterpriseSessionRecoveryPage
title: "DHCP"
id: dhcp
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/dhcp
tags:
  - skupper
  - enterprise-session-recovery
  - office-ops
related:
  - independent-request
  - network-path
  - office-operations
  - udp
---

# DHCP

Office operations protocols are mixed; TCP request flows fit better than UDP broadcast or real-time media flows.

## Skupper Suitability

Skupper is not a suitable fit for DHCP. DHCP relies on local network broadcast and UDP behavior that Skupper service exposure does not provide, so DHCP should remain on the local network or be handled by infrastructure designed for it.

## Appears in

- Enterprise Traffic Patterns / Office and Operations

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Independent Exchange, UDP, Network Path.

Dependencies:

- [Independent Exchange](./independent-request.md)
- [UDP](./udp.md)
- [Network Path](./network-path.md)

Used by:

- [Office Operations](./office-operations.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)
- [Link status](../skupper-docs-landscape/link-status.md)
- [Secure links](../skupper-docs-landscape/secure-links.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
