---
type: EnterpriseSessionRecoveryPage
title: "SMB (Samba)"
id: smb
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/smb
tags:
  - skupper
  - enterprise-session-recovery
  - file-identity
related:
  - dns
  - file-sharing
  - reconnectable-session
  - tcp
---

# SMB (Samba)

File and identity services may work when TCP reachability is enough, but session recovery and name resolution must be tested carefully.

## Skupper Suitability

Skupper can expose SMB over TCP in a constrained scenario, but it is not a default recommendation for general file sharing. Validate name resolution, locking, reconnect behavior, and user-visible file operation failures before relying on it.

## Appears in

- Enterprise Traffic Patterns / File and Identity

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Reconnectable Session, TCP, DNS.

Dependencies:

- [Reconnectable Session](./reconnectable-session.md)
- [TCP](./tcp.md)
- [DNS](./dns.md)

Used by:

- [File Sharing](./file-sharing.md)

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
