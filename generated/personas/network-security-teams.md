---
title: Network and Security Teams
type: SkupperPersona
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
persona_order: 5
coverage: Partial — individual controls exist, no consolidated model
missing_target_count: 2
audience_message: >-
  Skupper connects selected application services across network boundaries. Its explicit connectors and listeners let you represent where services are offered and consumed. Govern who can configure those relationships, secure the underlying paths, and retain the services’ own access controls.
tags:
  - skupper
  - personas
  - networking
  - security
  - missing-targets
---

# Network and Security Teams

> Skupper connects selected application services across network boundaries. Its explicit connectors and listeners let you represent where services are offered and consumed. Govern who can configure those relationships, secure the underlying paths, and retain the services’ own access controls.

For this audience, explicit service exposure is the key unit of review. Skupper link security and platform authorization complement rather than replace application authentication and authorization.

## Relevant existing pages

- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md) — the current security topic map; useful as an outline but still a stub.
- [Network Isolation](../skupper-docs-landscape/network-isolation.md) — namespaces, selected exposure, link access, and firewall-crossing paths.
- [Service Exposure Policy](../skupper-docs-landscape/service-policy.md) — decisions governing addresses, ports, routing keys, and workloads.
- [Role-Based Access Control](../skupper-docs-landscape/rbac.md) — platform authorization for Skupper resources.
- [Access Grants and Tokens](../concepts/access-grants-and-tokens.md) and [Certificate Manager](../concepts/certificate-manager.md) — enrollment and mTLS implementation details.

