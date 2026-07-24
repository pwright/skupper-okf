---
type: EnterpriseSessionRecoveryPage
title: "Office Operations"
id: office-operations
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/office-operations
tags:
  - skupper
  - enterprise-session-recovery
  - uses
related:
  - dhcp
  - ipp
  - mail
  - sip-rtp
  - snmp
  - syslog
---

# Office Operations

This is an enterprise traffic use case. Skupper fit depends on whether the workload can run over TCP and tolerate connection replacement.

## Skupper Suitability

Skupper is a selective fit for office operations. TCP services such as HTTPS, SMTP submission, IPP, or TLS syslog can be reasonable; DNS, DHCP, SNMP over UDP, and real-time media are normally poor fits and should use platform networking.

## Appears in

- Enterprise Traffic Patterns / Enterprise Uses

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: SMTP (and IMAP), IPP (Printing), SIP (and RTP), SNMP, Syslog, DHCP.

Dependencies:

- [SMTP (and IMAP)](./mail.md)
- [IPP (Printing)](./ipp.md)
- [SIP (and RTP)](./sip-rtp.md)
- [SNMP](./snmp.md)
- [Syslog](./syslog.md)
- [DHCP](./dhcp.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
