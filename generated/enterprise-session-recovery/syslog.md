---
type: EnterpriseSessionRecoveryPage
title: "Syslog"
id: syslog
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/syslog
tags:
  - skupper
  - enterprise-session-recovery
  - office-ops
related:
  - independent-request
  - office-operations
  - tcp
  - tls
  - udp
---

# Syslog

Office operations protocols are mixed; TCP request flows fit better than UDP broadcast or real-time media flows.

## Skupper Suitability

Skupper can fit syslog only for TCP or TLS syslog flows where private service reachability is the requirement. It is a poor fit for traditional UDP fire-and-forget syslog because delivery behavior and backpressure need to be handled by the logging pipeline, not hidden by the network path.

## Appears in

- Enterprise Traffic Patterns / Office and Operations

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Independent Exchange, UDP, TCP, TLS.

Dependencies:

- [Independent Exchange](./independent-request.md)
- [UDP](./udp.md)
- [TCP](./tcp.md)
- [TLS](./tls.md)

Used by:

- [Office Operations](./office-operations.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
