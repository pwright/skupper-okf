---
type: EnterpriseSessionRecoveryPage
title: "UDP"
id: udp
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/udp
tags:
  - skupper
  - enterprise-session-recovery
  - transport
related:
  - dhcp
  - dns
  - kerberos
  - network-path
  - quic
  - rdp
  - sip-rtp
  - snmp
  - syslog
---

# UDP

This is transport or path behavior. Skupper is relevant where the workload speaks TCP through a listener and connector.

## Skupper Suitability

Skupper is not a general UDP transport. It is relevant only when a UDP-based application has a TCP gateway or protocol adapter; native UDP, broadcast, multicast, real-time media, and QUIC traffic should use another network mechanism.

## Appears in

- Enterprise Traffic Patterns / Transport and Path

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Network Path.

Dependencies:

- [Network Path](./network-path.md)

Used by:

- [DHCP](./dhcp.md)
- [DNS](./dns.md)
- [Kerberos](./kerberos.md)
- [QUIC](./quic.md)
- [RDP](./rdp.md)
- [SIP (and RTP)](./sip-rtp.md)
- [SNMP](./snmp.md)
- [Syslog](./syslog.md)

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
