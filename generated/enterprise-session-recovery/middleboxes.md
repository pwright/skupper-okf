---
type: EnterpriseSessionRecoveryPage
title: "Middleboxes (NAT, firewall, LB)"
id: middleboxes
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/middleboxes
tags:
  - skupper
  - enterprise-session-recovery
  - transport
related:
  - keepalive-timeouts
  - network-path
  - reconnect-retry
---

# Middleboxes (NAT, firewall, LB)

This is transport or path behavior. Skupper is relevant where the workload speaks TCP through a listener and connector.

## Skupper Suitability

Skupper can reduce direct exposure to middleboxes by moving application connectivity onto Skupper links, but it does not eliminate firewall, NAT, load balancer, or proxy timeout constraints around the link itself.

## Appears in

- Enterprise Traffic Patterns / Transport and Path

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Network Path.

Dependencies:

- [Network Path](./network-path.md)

Used by:

- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [Reconnect (and Retry)](./reconnect-retry.md)

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
