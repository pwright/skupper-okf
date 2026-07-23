---
type: DocumentationLandscapePage
title: "CLI Command Contract"
id: cli-contract
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-contract
tags:
  - skupper
  - docs-landscape
  - develop
timestamp: 2026-07-23T21:30:00Z
---

# CLI Command Contract

The CLI command contract is the set of command names, options, generated artifacts, status outputs, and behavior that automation can depend on.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Developer Foundations

## Sources

- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md) - Local command reference index.
- [human/skupper-docs/refdog/config/commands/overview.md](../../human/skupper-docs/refdog/config/commands/overview.md) - Local command metadata overview.
- [human/skupper-docs/refdog/config/commands/options.yaml](../../human/skupper-docs/refdog/config/commands/options.yaml) - Local command option metadata.
- [human/skupper-docs/input/refdog/commands/site/index.md](../../human/skupper-docs/input/refdog/commands/site/index.md) - Site command reference.
- [human/skupper-docs/input/refdog/commands/link/index.md](../../human/skupper-docs/input/refdog/commands/link/index.md) - Link command reference.

## Website Links

- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Site commands](https://skupperproject.github.io/refdog/commands/site/index.html)
- [Link commands](https://skupperproject.github.io/refdog/commands/link/index.html)
- [Listener commands](https://skupperproject.github.io/refdog/commands/listener/index.html)
- [Connector commands](https://skupperproject.github.io/refdog/commands/connector/index.html)

## Draft Notes

- Focus on stable behavior useful to scripts: inputs, outputs, generated files, and status commands.
- Avoid documenting exit-code guarantees until the local command references explicitly provide them.
- Add contract checks for command metadata if the refdog validation scripts become part of the docs workflow.
