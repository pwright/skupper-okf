---
type: DocumentationLandscapePage
title: "Recovery Procedure"
id: recovery-procedure
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/recovery-procedure
tags:
  - skupper
  - docs-landscape
  - troubleshoot
timestamp: 2026-07-23T21:15:00Z
---

# Recovery Procedure

A recovery procedure is a documented sequence for restoring a known Skupper failure mode and validating the result without losing the evidence needed for follow-up.

## Appears in

- [Troubleshoot Skupper](./troubleshoot-skupper.md) / Diagnostic Evidence

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for recovery-oriented diagnostics.
- [human/skupper-docs/input/refdog/commands/site/reload.md](../../human/skupper-docs/input/refdog/commands/site/reload.md) - Site reload command reference.
- [human/skupper-docs/input/refdog/commands/site/start.md](../../human/skupper-docs/input/refdog/commands/site/start.md) - Site start command reference.
- [human/skupper-docs/input/refdog/commands/link/generate.md](../../human/skupper-docs/input/refdog/commands/link/generate.md) - Link generation command reference.
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md) - Generated source for local-system start, reload, stop, and bundle actions.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Site reload command](https://skupperproject.github.io/refdog/commands/site/reload.html)
- [Site start command](https://skupperproject.github.io/refdog/commands/site/start.html)
- [Link generate command](https://skupperproject.github.io/refdog/commands/link/generate.html)

## Draft Notes

- Write procedures for specific failure modes; avoid one universal recovery sequence.
- Require pre-checks, change steps, validation checks, and rollback or escalation criteria.
- Separate local-system recovery actions from Kubernetes resource remediation.
