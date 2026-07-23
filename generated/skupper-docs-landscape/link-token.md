---
type: DocumentationLandscapePage
title: "Link Credential or Token"
id: link-token
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-token
tags:
  - skupper
  - docs-landscape
  - extend
related:
  - site-identity
timestamp: 2026-07-23T20:01:23Z
---

# Link Credential or Token

Link Credential or Token covers the artifact used to let one site establish a link to another. Local docs describe access tokens as short-lived credentials with redemption and time limits, and warn that token files must be protected.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Controls

## Dependencies

- [Site Identity](./site-identity.md)

## Sources

- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Primary local source for enabling link access, issuing tokens, redeeming tokens, and protecting token files.
- [Token issue command](../../human/skupper-docs/input/refdog/commands/token/issue.md): Local command reference for expiration windows and redemption limits.
- [Token redeem command](../../human/skupper-docs/input/refdog/commands/token/redeem.md): Local command reference for creating a link from a token file.
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md): Local concept source for access token terminology.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for token characteristics and secure exchange notes.

## Website Links

- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog token issue command](https://skupperproject.github.io/refdog/commands/token/issue.html)
- [Refdog access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)

## Draft Notes

- Handle token files as sensitive material.
- Record expiration and redemption policy for each expansion wave.
- Use new tokens when status checks show expired or already-used credentials.
