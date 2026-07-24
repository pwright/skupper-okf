---
type: EnterpriseSessionRecoveryPage
title: "SNMP"
id: snmp
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/snmp
tags:
  - skupper
  - enterprise-session-recovery
  - office-ops
related:
  - independent-request
  - office-operations
  - tcp
  - udp
---

# SNMP

Office operations protocols are mixed; TCP request flows fit better than UDP broadcast or real-time media flows.

## Skupper Suitability

Skupper is usually a poor fit for SNMP polling or traps because SNMP is commonly UDP-based infrastructure traffic. Use Skupper only for a deliberately TCP-based management endpoint, and prefer standard network-management access patterns for normal SNMP.

## Appears in

- Enterprise Traffic Patterns / Office and Operations

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Independent Exchange, UDP, TCP.

Dependencies:

- [Independent Exchange](./independent-request.md)
- [UDP](./udp.md)
- [TCP](./tcp.md)

Used by:

- [Office Operations](./office-operations.md)

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
