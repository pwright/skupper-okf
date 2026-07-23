---
type: DocumentationLandscapePage
title: "Logging Interface"
id: logging-interface
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/logging-interface
tags:
  - skupper
  - docs-landscape
  - integrate
timestamp: 2026-07-23T21:45:00Z
---

# Logging Interface

The logging interface covers Skupper component logs, observer logs, and debug bundle material used by operational logging systems.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Operations Interfaces

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for logs and diagnostics.
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md) - Debug dump command reference.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer logging profile.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console error handling.
- [generated/skupper-docs-landscape/runtime-logs.md](./runtime-logs.md) - Related landscape page for runtime logs.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Separate runtime logs, observer logs, and generated debug bundles.
- Add redaction guidance for shared log bundles.
- Include logging-profile details only where the observer configuration source supports them.
