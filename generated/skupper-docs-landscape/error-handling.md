---
type: DocumentationLandscapePage
title: "Exit Codes and Error Handling"
id: error-handling
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/error-handling
tags:
  - skupper
  - docs-landscape
  - develop
timestamp: 2026-07-23T21:30:00Z
---

# Exit Codes and Error Handling

Exit codes and error handling define how automation should detect failed Skupper commands, capture diagnostics, and decide whether to retry, roll back, or escalate.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Developer Foundations

## Sources

- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md) - Local command reference index.
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md) - Debug check command reference.
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md) - Debug dump command reference.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for diagnostic capture.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console API error behavior.

## Website Links

- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Source coverage for exact exit-code contracts appears thin; keep future text focused on observable failures and diagnostics.
- Include capture of stdout, stderr, status commands, and debug dumps in automation failure paths.
- Add retry guidance only when the failed operation is known to be idempotent.
