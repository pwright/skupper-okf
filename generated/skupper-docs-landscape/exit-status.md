---
type: DocumentationLandscapePage
title: "Exit Status and Errors"
id: exit-status
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/exit-status
tags:
  - skupper
  - docs-landscape
  - reference
timestamp: 2026-07-23T22:15:00Z
---

# Exit Status and Errors

Exit status and errors describe how Skupper commands and APIs report failure conditions to users and automation.

## Appears in

- [Skupper Reference](./skupper-reference.md) / Syntax and Schema

## Sources

- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md) - Local command reference index.
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md) - Debug check command reference.
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md) - Debug dump command reference.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting guide.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console API error handling.

## Website Links

- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Source coverage for numeric exit statuses is thin; avoid inventing exit-code tables.
- Focus on diagnostic paths: capture output, run debug checks, collect dumps, and inspect resource status.
- Add API error examples only where generated console or API sources provide stable wording.
