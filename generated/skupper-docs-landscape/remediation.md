---
type: DocumentationLandscapePage
title: "Remediation"
id: remediation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/remediation
tags:
  - skupper
  - docs-landscape
  - troubleshoot
related:
  - root-cause-record
  - recovery-procedure
timestamp: 2026-07-23T21:15:00Z
---

# Remediation

Remediation applies a source-backed change to fix an isolated Skupper fault, then verifies that connectivity and observable state are healthy again.

## Appears in

- [Troubleshoot Skupper](./troubleshoot-skupper.md) / Diagnostic Workflow

## Dependencies

- [Root Cause Record](./root-cause-record.md)
- [Recovery Procedure](./recovery-procedure.md)

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for checks and recovery-oriented evidence.
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - CLI source for link creation and status checks.
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md) - CLI source for listener and connector management.
- [human/skupper-docs/input/refdog/commands/site/update.md](../../human/skupper-docs/input/refdog/commands/site/update.md) - Site update command reference.
- [human/skupper-docs/input/refdog/commands/link/delete.md](../../human/skupper-docs/input/refdog/commands/link/delete.md) - Link delete command reference for controlled replacement scenarios.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Site update command](https://skupperproject.github.io/refdog/commands/site/update.html)

## Draft Notes

- Tie each remediation step to the fault isolated earlier; avoid generic repair scripts.
- Require validation after every resource change, especially link or service exposure changes.
- Include a rollback path when remediation changes production traffic or identity material.
