---
type: DocumentationLandscapePage
title: "Link Status"
id: link-status
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-status
tags:
  - skupper
  - docs-landscape
  - administer
timestamp: 2026-07-23T20:10:12Z
---

# Link Status

Link Status records whether site-to-site links are present and ready from the perspective of the linking site. It is the main operational signal for whether sites can exchange traffic across the application network.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Operational State

## Sources

- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md): Primary local command reference for link status.
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for token, link-resource, proxy, and link-status workflows.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking sites, links, connectors, listeners, and collecting debug evidence.
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Local concept source for link behavior.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for operational checks, link constraints, resources, and traffic direction.

## Website Links

- [Refdog link status command](https://skupperproject.github.io/refdog/commands/link/status.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Run link status on the linking site.
- Record link name, status, cost, and message.
- Check token expiry and link access when a new link remains pending or absent.
