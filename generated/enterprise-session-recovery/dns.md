---
type: EnterpriseSessionRecoveryPage
title: "DNS"
id: dns
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/dns
tags:
  - skupper
  - enterprise-session-recovery
  - office-ops
related:
  - identity-naming
  - independent-request
  - kerberos
  - ldap
  - network-path
  - nfs
  - smb
  - tcp
  - udp
---

# DNS

Office operations protocols are mixed; TCP request flows fit better than UDP broadcast or real-time media flows.

## Skupper Suitability

Skupper is generally a poor fit for DNS as infrastructure. Most DNS use is UDP-based, latency-sensitive, and part of the substrate needed before applications can connect; exposing DNS through Skupper is usually a workaround for a narrow TCP DNS service, not a normal Skupper use case.

## Appears in

- Enterprise Traffic Patterns / Office and Operations

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Independent Exchange, UDP, TCP, Network Path.

Dependencies:

- [Independent Exchange](./independent-request.md)
- [UDP](./udp.md)
- [TCP](./tcp.md)
- [Network Path](./network-path.md)

Used by:

- [Identity (and Naming)](./identity-naming.md)
- [Kerberos](./kerberos.md)
- [LDAP](./ldap.md)
- [NFS](./nfs.md)
- [SMB (Samba)](./smb.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Links](../skupper-docs-landscape/links.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
