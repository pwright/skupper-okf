---
type: EnterpriseSessionRecoveryPage
title: "SSH (and SFTP)"
id: ssh-sftp
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/ssh-sftp
tags:
  - skupper
  - enterprise-session-recovery
  - web-interactive
related:
  - keepalive-timeouts
  - remote-access
  - socket-bound
  - tcp
---

# SSH (and SFTP)

This protocol family has mixed fit with Skupper: TCP-based HTTP and gRPC are natural candidates, while QUIC requires a non-Skupper UDP path or a protocol translation layer.

## Skupper Suitability

Skupper can carry SSH or SFTP as private TCP traffic, but it does not preserve an interactive session if the TCP connection breaks. It is more suitable for controlled administrative paths or batch file transfer than for highly available interactive access.

## Appears in

- Enterprise Traffic Patterns / Web and Interactive

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Socket-Bound Session, Keepalive (and Timeouts), TCP.

Dependencies:

- [Socket-Bound Session](./socket-bound.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [TCP](./tcp.md)

Used by:

- [Remote Access](./remote-access.md)

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
