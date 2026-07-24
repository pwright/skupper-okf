---
type: EnterpriseSessionRecoveryPage
title: "SMTP (and IMAP)"
id: mail
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/mail
tags:
  - skupper
  - enterprise-session-recovery
  - office-ops
related:
  - office-operations
  - pooled-reuse
  - reconnect-retry
  - tcp
  - tls
---

# SMTP (and IMAP)

Office operations protocols are mixed; TCP request flows fit better than UDP broadcast or real-time media flows.

## Skupper Suitability

Skupper can be a reasonable fit for SMTP, IMAP, or submission over TCP/TLS when the requirement is private reachability to a mail service. It is not a mail-delivery guarantee; queueing, duplicate handling, authentication, and retry semantics remain with the mail clients and servers.

## Appears in

- Enterprise Traffic Patterns / Office and Operations

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Pooled Reuse, Reconnect (and Retry), TLS, TCP.

Dependencies:

- [Pooled Reuse](./pooled-reuse.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)

Used by:

- [Office Operations](./office-operations.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
