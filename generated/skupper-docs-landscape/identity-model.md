---
type: DocumentationLandscapePage
title: "Certificates and Identity"
id: identity-model
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/identity-model
tags:
  - skupper
  - docs-landscape
  - discover
timestamp: 2026-07-23T19:44:12Z
---

# Certificates and Identity

The Skupper identity model covers the certificates, credentials, and trust relationships that let sites authenticate links and protect application-network connectivity. This page should introduce identity as a prerequisite for trusted links and private service connectivity.

## Appears in

- [Discover Skupper](./discover-skupper.md) / Foundations

## Sources

- [Security overview](../../human/skupper-docs/input/overview/security.md): Local overview source for security model framing.
- [Router TLS topic](../../human/skupper-docs/input/refdog/topics/router-tls.md): Local source for router TLS behavior.
- [Application TLS topic](../../human/skupper-docs/input/refdog/topics/application-tls.md): Local source for application-level TLS considerations.
- [System TLS credentials topic](../../human/skupper-docs/input/refdog/topics/system-tls-credentials.md): Local source for local-system TLS credential handling.
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md): Local concept source for token and credential relationships.

## Website Links

- [Security overview](https://skupper.io/docs/overview/security.html)
- [Access token concept reference](https://skupper.io/docs/refdog/concepts/access-token.html)

## Draft Notes

- Separate router/link identity from application TLS between clients and workloads.
- Include certificate lifecycle details later under the security map.
