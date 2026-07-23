---
type: DocumentationLandscapePage
title: "Link the Sites"
id: first-link
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/first-link
tags:
  - skupper
  - docs-landscape
  - get-started
related:
  - first-sites
  - link-credentials
timestamp: 2026-07-23T19:49:37Z
---

# Link the Sites

Link the Sites explains how two existing Skupper sites become part of one application network. The starter path should emphasize token-based linking first, because it is the clearest introductory flow, while noting that link resources are available for YAML-driven or proxy-sensitive setups.

## Appears in

- [Get Started with Skupper](./get-started.md) / Starter Workflow

## Dependencies

- [Create Two Sites](./first-sites.md)
- [Link Credentials](./link-credentials.md)

## Sources

- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Primary local source for token-based linking, link resources, and link status checks.
- [Token issue command](../../human/skupper-docs/input/refdog/commands/token/issue.md): Local command reference for issuing a token file from a site.
- [Token redeem command](../../human/skupper-docs/input/refdog/commands/token/redeem.md): Local command reference for redeeming a token file on another site.
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md): Local command reference for validating the link after creation.
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Local concept source for link behavior and terminology.

## Website Links

- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog token issue command](https://skupperproject.github.io/refdog/commands/token/issue.html)
- [Refdog token redeem command](https://skupperproject.github.io/refdog/commands/token/redeem.html)

## Draft Notes

- Keep the first version to token issue and redeem unless there is room for an advanced branch.
- Call out that token files are sensitive because local sources explicitly warn that access to the file grants network access.
- Add link resource coverage later for GitOps and HTTP proxy scenarios.
