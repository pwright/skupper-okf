---
type: EnterpriseSessionRecoveryPage
title: "LDAP"
id: ldap
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/ldap
tags:
  - skupper
  - enterprise-session-recovery
  - file-identity
related:
  - dns
  - identity-naming
  - pooled-reuse
  - reconnect-retry
  - tcp
  - tls
---

# LDAP

File and identity services may work when TCP reachability is enough, but session recovery and name resolution must be tested carefully.

## Skupper Suitability

Skupper can be a reasonable fit for LDAP or LDAPS when clients need private TCP reachability to a directory service and can retry failed binds or queries. It should not be treated as a replacement for DNS, Kerberos, or local identity infrastructure.

## Appears in

- Enterprise Traffic Patterns / File and Identity

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Pooled Reuse, Reconnect (and Retry), TLS, TCP, DNS.

Dependencies:

- [Pooled Reuse](./pooled-reuse.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)
- [DNS](./dns.md)

Used by:

- [Identity (and Naming)](./identity-naming.md)

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
