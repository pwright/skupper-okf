---
type: EnterpriseSessionRecoveryPage
title: "Keepalive (and Timeouts)"
id: keepalive-timeouts
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/keepalive-timeouts
tags:
  - skupper
  - enterprise-session-recovery
  - transport
related:
  - middleboxes
  - mqtt
  - multiplexed-session
  - pooled-reuse
  - socket-bound
  - ssh-sftp
  - tcp
  - websocket
---

# Keepalive (and Timeouts)

This is transport or path behavior. Skupper is relevant where the workload speaks TCP through a listener and connector.

## Skupper Suitability

Skupper is affected by keepalive and timeout settings like any TCP path. It can provide a stable service route, but applications should use explicit timeouts and reconnect rather than relying on idle sockets surviving indefinitely.

## Appears in

- Enterprise Traffic Patterns / Transport and Path

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: TCP, Middleboxes (NAT, firewall, LB).

Dependencies:

- [TCP](./tcp.md)
- [Middleboxes (NAT, firewall, LB)](./middleboxes.md)

Used by:

- [MQTT](./mqtt.md)
- [Multiplexed Session](./multiplexed-session.md)
- [Pooled Reuse](./pooled-reuse.md)
- [Socket-Bound Session](./socket-bound.md)
- [SSH (and SFTP)](./ssh-sftp.md)
- [WebSocket](./websocket.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
