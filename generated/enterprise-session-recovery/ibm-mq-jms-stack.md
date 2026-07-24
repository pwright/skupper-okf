---
type: EnterpriseSessionRecoveryPage
title: "IBM MQ (JMS)"
id: ibm-mq-jms-stack
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/ibm-mq-jms-stack
tags:
  - skupper
  - enterprise-session-recovery
  - software-stacks
related:
  - durable-position-recovery
  - durable-processing-progress
  - logical-session-resume
---

# IBM MQ (JMS)

This stack can use Skupper as private TCP reachability between client and service endpoints; recovery semantics remain owned by the client library, broker, or database.

## Skupper Suitability

Skupper is a good fit for IBM MQ JMS when clients use reconnect, acknowledgements, durable destinations, and redelivery semantics. Skupper provides the private TCP path; MQ and JMS configuration determine whether in-flight work is recovered safely.

## Appears in

- Enterprise TCP Sessions and Recovery / Enterprise Software and Java Clients

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Session Resumption, Durable-Position Recovery.

Dependencies:

- [Session Resumption](./logical-session-resume.md)
- [Durable-Position Recovery](./durable-position-recovery.md)

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
