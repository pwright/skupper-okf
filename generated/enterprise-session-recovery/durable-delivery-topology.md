---
type: EnterpriseSessionRecoveryPage
title: "Durable Delivery State (and topology)"
id: durable-delivery-topology
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/durable-delivery-topology
tags:
  - skupper
  - enterprise-session-recovery
  - protocol-state
related:
  - broker-database-endpoints
  - topology-reconstruction
---

# Durable Delivery State (and topology)

This is protocol or application state. Skupper does not store it, but it can keep the required endpoints reachable after a path or site change.

## Skupper Suitability

Skupper is a good fit when delivery state and topology are durable in the broker or recreated by the client after reconnect. It should not be credited with preserving queues, subscriptions, consumer positions, or acknowledgements.

## Appears in

- Enterprise TCP Sessions and Recovery / State Above TCP

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Broker (and database endpoints).

Dependencies:

- [Broker (and database endpoints)](./broker-database-endpoints.md)

Used by:

- [Topology Reconstruction (and subscriptions)](./topology-reconstruction.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)
- [Traffic baseline](../skupper-docs-landscape/traffic-baseline.md)
- [Evidence bundle](../skupper-docs-landscape/evidence-bundle.md)
- [Listener concept](../concepts/listener.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
