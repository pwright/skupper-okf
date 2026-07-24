---
type: EnterpriseSessionRecoveryPage
title: "NAT (and firewall state)"
id: nat-firewall-state
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/nat-firewall-state
tags:
  - skupper
  - enterprise-session-recovery
  - transport
related:
  - heartbeat-and-keepalive
  - network-path
---

# NAT (and firewall state)

This is transport or path behavior. Skupper is relevant where the workload speaks TCP through a listener and connector.

## Skupper Suitability

Skupper can help avoid many application-specific firewall openings by concentrating traffic into Skupper links. It does not preserve NAT or firewall state for an existing application TCP socket after failure.

## Appears in

- Enterprise TCP Sessions and Recovery / TCP and Network Path

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Network Path.

Dependencies:

- [Network Path](./network-path.md)

Used by:

- [Heartbeats (and TCP keepalive)](./heartbeat-and-keepalive.md)

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
