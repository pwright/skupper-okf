---
type: EnterpriseSessionRecoveryPage
title: "Independent Exchange"
id: independent-request
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/independent-request
tags:
  - skupper
  - enterprise-session-recovery
  - session-behaviour
related:
  - dhcp
  - dns
  - http3-quic
  - ipp
  - kerberos
  - network-path
  - snmp
  - syslog
---

# Independent Exchange

This behavior describes how much state survives connection loss. Skupper does not convert socket-bound state into resumable state.

## Skupper Suitability

Skupper is a good fit for independent request and response traffic when it runs over TCP, especially HTTP APIs. It is not a fit for independent exchanges that depend on UDP broadcast, multicast, or local subnet behavior.

## Appears in

- Enterprise Traffic Patterns / Session Behaviour

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Network Path.

Dependencies:

- [Network Path](./network-path.md)

Used by:

- [DHCP](./dhcp.md)
- [DNS](./dns.md)
- [HTTP/3 (QUIC)](./http3-quic.md)
- [IPP (Printing)](./ipp.md)
- [Kerberos](./kerberos.md)
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
