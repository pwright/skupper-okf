---
type: DocumentationLandscapePage
title: "Keep Services Private"
id: private-connectivity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/private-connectivity
tags:
  - skupper
  - docs-landscape
  - discover
related:
  - secure-links
  - identity-model
timestamp: 2026-07-23T19:44:12Z
---

# Keep Services Private

Private connectivity is the Skupper value proposition that remote services can be reached through the application network without exposing those services directly on the public internet. This page should introduce the security posture at a conceptual level, then point readers to links and identity for implementation details.

## Appears in

- [Discover Skupper](./discover-skupper.md) / User Value

## Dependencies

- [Secure Links](./secure-links.md)
- [Certificates and Identity](./identity-model.md)

## Sources

- [Security overview](../../human/skupper-docs/input/overview/security.md): Local source for secure connectivity framing.
- [Connectivity overview](../../human/skupper-docs/input/overview/connectivity.md): Local source for private cross-site access patterns.
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Local concept source for site-to-site link behavior.
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md): Local concept source for credentials used in access and linking workflows.

## Website Links

- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Skupper docs](https://skupper.io/docs/)

## Draft Notes

- Avoid implying that Skupper replaces all perimeter controls; describe what remains private and what link endpoints require.
- Connect privacy claims to authenticated links and certificate-backed identity.
