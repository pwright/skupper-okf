---
type: EnterpriseSessionRecoveryPage
title: "Durable Progress"
id: durable-processing-progress
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/durable-processing-progress
tags:
  - skupper
  - enterprise-session-recovery
  - outcomes
related:
  - ibm-mq-jms-stack
  - kafka-java-stack
---

# Durable Progress

This outcome is an application-level recovery goal, not a property of the network path alone.

## Skupper Suitability

Skupper is a good fit for durable progress patterns because reconnecting over a new TCP path is usually enough for the client to continue from stored offsets, cursors, or acknowledgements. The durable store, broker, and consumer logic provide correctness; Skupper provides private reachability and useful traffic visibility.

## Appears in

- Enterprise TCP Sessions and Recovery / Application Outcomes

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Kafka (Java Client or Spring), IBM MQ (JMS).

Dependencies:

- [Kafka (Java Client or Spring)](./kafka-java-stack.md)
- [IBM MQ (JMS)](./ibm-mq-jms-stack.md)

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
