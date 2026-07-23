---
type: DocumentationLandscapePage
title: "Link Credentials"
id: link-credentials
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-credentials
tags:
  - skupper
  - docs-landscape
  - get-started
  - administer
timestamp: 2026-07-23T20:10:12Z
---

# Link Credentials

Link Credentials explains operational handling of tokens and link credential material. Local docs describe token files as a secure method for linking sites, with default limits and a warning to protect the file.

## Appears in

- [Get Started with Skupper](./get-started.md) / Starter Setup
- [Administer Skupper](./administer-skupper.md) / Operational State

## Sources

- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for token, link-resource, proxy, and link-status workflows.
- [Token issue command](../../human/skupper-docs/input/refdog/commands/token/issue.md): Local command reference for token defaults and options.
- [Token redeem command](../../human/skupper-docs/input/refdog/commands/token/redeem.md): Local command reference for using a token file to create a link.
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md): Local concept source for token terminology.
- [AccessToken resource](../../human/skupper-docs/input/refdog/resources/access-token.md): Local resource reference candidate for YAML-driven expansion.

## Website Links

- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog token issue command](https://skupperproject.github.io/refdog/commands/token/issue.html)
- [Refdog access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)

## Draft Notes

- Treat token files as sensitive artifacts throughout their lifecycle.
- Record who issued, transferred, redeemed, and removed each credential.
- Explain default one-use and time-limited behavior only where it remains backed by current command docs.
