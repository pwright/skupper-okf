---
type: DocumentationLandscapePage
title: "CLI Automation"
id: cli-automation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-automation
tags:
  - skupper
  - docs-landscape
  - develop
related:
  - cli-contract
  - error-handling
timestamp: 2026-07-23T21:30:00Z
---

# CLI Automation

CLI automation uses Skupper commands in scripts or pipelines to create, update, validate, and remove application-network resources.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Development Interfaces

## Dependencies

- [CLI Command Contract](./cli-contract.md)
- [Exit Codes and Error Handling](./error-handling.md)

## Sources

- [human/skupper-docs/input/kube-cli/index.md](../../human/skupper-docs/input/kube-cli/index.md) - Local index for Kubernetes CLI workflows.
- [human/skupper-docs/input/system-cli/index.md](../../human/skupper-docs/input/system-cli/index.md) - Local index for local-system CLI workflows.
- [human/skupper-docs/input/refdog/commands/index.md](../../human/skupper-docs/input/refdog/commands/index.md) - Local command reference index.
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md) - Debug check command reference for automation validation.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local source for validating command outcomes.

## Website Links

- [Kubernetes CLI workflows](https://skupper.io/docs/kube-cli/index.html)
- [System CLI workflows](https://skupper.io/docs/system-cli/index.html)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)

## Draft Notes

- Document command sequencing, expected outputs, and status checks for automation use.
- Treat generated YAML commands as a bridge from CLI workflow to configuration-as-code workflow.
- Add error handling examples only where command behavior is source-backed.
