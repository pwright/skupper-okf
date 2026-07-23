---
type: DocumentationLandscapePage
title: "Link Operations"
id: link-operations
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-operations
tags:
  - skupper
  - docs-landscape
  - administer
related:
  - link-status
  - link-credentials
timestamp: 2026-07-23T20:10:12Z
---

# Link Operations

Link Operations covers ongoing administration of site links: checking readiness, issuing or rotating credentials, understanding link direction, and preserving evidence for troubleshooting.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Administrative Workflows

## Dependencies

- [Link Status](./link-status.md)
- [Link Credentials](./link-credentials.md)

## Sources

- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for token, link-resource, proxy, and link-status workflows.
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md): Local command reference for link status.
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Local concept source for link access and bidirectional traffic.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking sites, links, connectors, listeners, and collecting debug evidence.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for operational checks, link constraints, resources, and traffic direction.

## Website Links

- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog link status command](https://skupperproject.github.io/refdog/commands/link/status.html)
- [Refdog link concept](https://skupperproject.github.io/refdog/concepts/link.html)

## Draft Notes

- Check link status from the linking site.
- Treat token files and link bundles as sensitive operational artifacts.
- Record link cost, proxy settings, and link-access decisions when they affect operations.
