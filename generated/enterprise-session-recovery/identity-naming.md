---
type: EnterpriseSessionRecoveryPage
title: "Identity (and Naming)"
id: identity-naming
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/identity-naming
tags:
  - skupper
  - enterprise-session-recovery
  - uses
related:
  - dns
  - kerberos
  - ldap
---

# Identity (and Naming)

This is an enterprise traffic use case. Skupper fit depends on whether the workload can run over TCP and tolerate connection replacement.

## Skupper Suitability

Skupper is a mixed fit for identity and naming. LDAP over TCP can be a reasonable service exposure, but DNS, Kerberos, and other foundational naming or authentication paths are usually better provided by platform infrastructure before Skupper-routed applications start.

## Appears in

- Enterprise Traffic Patterns / Enterprise Uses

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: LDAP, Kerberos, DNS.

Dependencies:

- [LDAP](./ldap.md)
- [Kerberos](./kerberos.md)
- [DNS](./dns.md)

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
