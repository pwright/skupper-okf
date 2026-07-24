---
type: EnterpriseSessionRecoveryPage
title: "Kafka (Java Client or Spring)"
id: kafka-java-stack
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/kafka-java-stack
tags:
  - skupper
  - enterprise-session-recovery
  - software-stacks
related:
  - durable-position-recovery
  - durable-processing-progress
  - reconnect-and-retry
---

# Kafka (Java Client or Spring)

This stack can use Skupper as private TCP reachability between client and service endpoints; recovery semantics remain owned by the client library, broker, or database.

## Skupper Suitability

Skupper is a good fit for Kafka Java or Spring clients when broker addresses, retries, durable offsets, and idempotent processing are configured correctly. Skupper provides private TCP reachability and flow visibility; Kafka provides correctness after reconnect.

## Appears in

- Enterprise TCP Sessions and Recovery / Enterprise Software and Java Clients

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Durable-Position Recovery, Reconnect (and retry).

Dependencies:

- [Durable-Position Recovery](./durable-position-recovery.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)

Used by:

- [Durable Progress](./durable-processing-progress.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
