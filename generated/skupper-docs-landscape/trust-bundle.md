---
type: DocumentationLandscapePage
title: "Trust Bundle"
id: trust-bundle
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/trust-bundle
tags:
  - skupper
  - docs-landscape
  - secure
timestamp: 2026-07-23T20:30:00Z
---

# Trust Bundle

A trust bundle is the trust material a Skupper component uses to validate a peer during secure link or router communication.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Identity Foundations

## Sources

- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md) - Local source candidate for router TLS trust behavior.
- [human/skupper-docs/input/refdog/concepts/access-token.md](../../human/skupper-docs/input/refdog/concepts/access-token.md) - Concept source for exchanging trust material during token-based linking.
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md) - Access token resource reference.
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md) - Link resource reference.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source candidate for link trust notes.

## Website Links

- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)
- [Access token resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)

## Draft Notes

- Confirm the public vocabulary before expanding; local sources may refer to CA data, certificates, and token payloads more often than "trust bundle".
- Add a short explanation of what must match between two sites for link authentication to succeed.
- Include renewal and replacement handling only where it is directly supported by source material.
