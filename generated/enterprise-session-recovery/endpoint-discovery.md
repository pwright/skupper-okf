---
type: EnterpriseSessionRecoveryPage
title: "Endpoint Discovery"
id: endpoint-discovery
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/endpoint-discovery
tags:
  - skupper
  - enterprise-session-recovery
  - connection-management
related:
  - automatic-reconnect-failover
  - broker-database-endpoints
  - network-path
---

# Endpoint Discovery

This is client-side connection behavior. Skupper helps by providing service addresses and links, while the client detects failures and reconnects.

## Skupper Suitability

Skupper can simplify endpoint discovery by giving clients a stable service address while connectors target workloads elsewhere. It does not replace protocol-specific discovery such as Kafka advertised listeners unless those settings are aligned with the Skupper-exposed addresses.

## Appears in

- Enterprise TCP Sessions and Recovery / Client Connection Management

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Broker (and database endpoints), Network Path.

Dependencies:

- [Broker (and database endpoints)](./broker-database-endpoints.md)
- [Network Path](./network-path.md)

Used by:

- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Listener concept](../concepts/listener.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
