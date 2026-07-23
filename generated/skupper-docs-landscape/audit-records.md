---
type: DocumentationLandscapePage
title: "Audit Records"
id: audit-records
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/audit-records
tags:
  - skupper
  - docs-landscape
  - administer
timestamp: 2026-07-23T20:10:12Z
---

# Audit Records

Audit Records are the administrative records that show what changed, who approved it, what evidence was collected, and whether validation passed. Source coverage is process-oriented rather than product-specific, so keep this page as a practical evidence checklist.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Governance Controls

## Sources

- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking sites, links, connectors, listeners, and collecting debug evidence.
- [Debug dump command](../../human/skupper-docs/input/refdog/commands/debug/dump.md): Local command reference for diagnostic archive generation.
- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md): Local source for desired resources, generated resources, and platform-specific operations.
- [Skupper Ansible resource module](../skupper-ansible/skupper-ansible-module-resource.md): Generated local source for declarative apply/update/remove operations.
- [Controlled Administrative Change](./controlled-change.md): Local landscape source for change outcome framing.

## Website Links

- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

## Draft Notes

- Record command outputs, resource versions, applied definitions, and validation results.
- Store sensitive artifacts separately from general audit notes.
- Document known residual risks and follow-up actions after each change.
