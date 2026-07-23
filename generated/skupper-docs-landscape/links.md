---
type: DocumentationLandscapePage
title: "Site Links"
id: links
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/links
tags:
  - skupper
  - docs-landscape
  - discover
related:
  - sites
timestamp: 2026-07-23T19:44:12Z
---

# Site Links

Site links connect Skupper sites so traffic and reachability information can move through the application network. This page should introduce links as relationships between sites, then route readers to token, access, and resource details.

## Appears in

- [Discover Skupper](./discover-skupper.md) / Foundations

## Dependencies

- [Sites](./sites.md)

## Sources

- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Primary local concept source for links.
- [Site linking topic](../../human/skupper-docs/input/refdog/topics/site-linking.md): Local source for linking workflow and concepts.
- [Link command reference config](../../human/skupper-docs/refdog/config/commands/link.yaml): Local source for command behavior such as status and generate.
- [Link resource reference](../../human/skupper-docs/input/refdog/resources/link.md): Local source for declarative Link resource fields.

## Website Links

- [Link concept reference](https://skupper.io/docs/refdog/concepts/link.html)
- [Link command reference](https://skupper.io/docs/refdog/commands/link/)

## Draft Notes

- Describe link direction carefully: generating link material at one site and applying it at another creates the remote relationship.
- Keep link health/status separate from service exposure status.
