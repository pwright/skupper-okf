---
type: EnterpriseSessionRecoveryPage
title: "Kerberos"
id: kerberos
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/kerberos
tags:
  - skupper
  - enterprise-session-recovery
  - file-identity
related:
  - dns
  - identity-naming
  - independent-request
  - tcp
  - udp
---

# Kerberos

File and identity services may work when TCP reachability is enough, but session recovery and name resolution must be tested carefully.

## Skupper Suitability

Skupper is usually a poor fit for Kerberos as core identity infrastructure because Kerberos often depends on DNS, UDP, strict timing, and local realm assumptions. A TCP-only KDC endpoint could be exposed for a narrow case, but this should be treated as exceptional and tested carefully.

## Appears in

- Enterprise Traffic Patterns / File and Identity

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Independent Exchange, UDP, TCP, DNS.

Dependencies:

- [Independent Exchange](./independent-request.md)
- [UDP](./udp.md)
- [TCP](./tcp.md)
- [DNS](./dns.md)

Used by:

- [Identity (and Naming)](./identity-naming.md)

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
