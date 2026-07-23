---
type: DocumentationLandscapePage
title: "Logging Settings"
id: logging-settings
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/logging-settings
tags:
  - skupper
  - docs-landscape
  - configure
related: []
timestamp: 2026-07-23T20:17:03Z
---

# Logging Settings

Logging settings are the configuration and diagnostic entry points used to inspect Skupper behavior, collect logs, and support troubleshooting. The local source coverage is strongest for troubleshooting commands and debug dumps rather than a broad logging configuration reference.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Inputs

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Troubleshooting procedures that reference logs, checks, and debug information.
- [human/skupper-docs/input/refdog/topics/debug-dumps.md](../../human/skupper-docs/input/refdog/topics/debug-dumps.md) - Topic reference for debug dump collection.
- [human/skupper-docs/input/refdog/commands/debug/index.md](../../human/skupper-docs/input/refdog/commands/debug/index.md) - Debug command group reference.
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md) - Debug check command reference.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Console configuration source with observer-related settings; use only where it matches the page scope.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug dump topic](https://skupperproject.github.io/refdog/topics/debug-dumps.html)
- [Debug command reference](https://skupperproject.github.io/refdog/commands/debug/index.html)
- [Console configuration](https://skupper.io/docs/console/configuration.html)

## Draft Notes

- Keep this page clearly labeled as thinly sourced until a dedicated logging configuration reference is available.
- Separate log collection, debug checks, and configurable log levels if future sources support that split.
- Add command examples for gathering router and controller logs only where the troubleshooting docs already show them.
