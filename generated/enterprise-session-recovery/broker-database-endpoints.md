---
type: EnterpriseSessionRecoveryPage
title: "Broker (and database endpoints)"
id: broker-database-endpoints
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/broker-database-endpoints
tags:
  - skupper
  - enterprise-session-recovery
  - transport
related:
  - durable-checkpoint
  - durable-delivery-topology
  - endpoint-discovery
  - failure-detection
  - idempotency-and-fencing
  - network-path
  - session-identity
---

# Broker (and database endpoints)

This is transport or path behavior. Skupper is relevant where the workload speaks TCP through a listener and connector.

## Skupper Suitability

Skupper is a strong fit for broker endpoints and a conditional fit for database endpoints. Brokers usually have reconnect and durable delivery semantics; databases need more application care around connection pools and transaction recovery.

## Appears in

- Enterprise TCP Sessions and Recovery / TCP and Network Path

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Network Path.

Dependencies:

- [Network Path](./network-path.md)

Used by:

- [Durable Checkpoint (offset or cursor)](./durable-checkpoint.md)
- [Durable Delivery State (and topology)](./durable-delivery-topology.md)
- [Endpoint Discovery](./endpoint-discovery.md)
- [Failure Detection](./failure-detection.md)
- [Idempotency (deduplication and fencing)](./idempotency-and-fencing.md)
- [Session Identity](./session-identity.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Listener concept](../concepts/listener.md)
- [Connector concept](../concepts/connector.md)
- [Routing key concept](../concepts/routing-key.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
