---
type: DocumentationLandscapePage
title: "Establish a Link"
id: link-establishment
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-establishment
tags:
  - skupper
  - docs-landscape
  - extend
related:
  - link-token
  - network-policy
timestamp: 2026-07-23T20:01:23Z
---

# Establish a Link

Establish a Link covers joining the onboarded site to another site in the application network. The common path uses an access token issued at one site and redeemed at another; local docs also describe link resources for YAML-driven cases.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Workflow

## Dependencies

- [Link Credential or Token](./link-token.md)
- [Network Policy](./network-policy.md)

## Sources

- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Primary local source for token-based linking, link resources, HTTP proxy notes, and link status checks.
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Local concept source for link access and bidirectional application traffic.
- [Token issue command](../../human/skupper-docs/input/refdog/commands/token/issue.md): Local command reference for issuing link tokens and setting limits.
- [Token redeem command](../../human/skupper-docs/input/refdog/commands/token/redeem.md): Local command reference for creating a link from a token.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for link constraints and custom certificate considerations.

## Website Links

- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog link concept](https://skupperproject.github.io/refdog/concepts/link.html)
- [Refdog token issue command](https://skupperproject.github.io/refdog/commands/token/issue.html)

## Draft Notes

- Document which site issues credentials and which site redeems or applies them.
- Validate with link status before exposing new services.
- Use link resources instead of token-only flow when proxy or GitOps requirements demand it.
