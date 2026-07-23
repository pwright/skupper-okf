---
type: DocumentationLandscapePage
title: "Change Workflow"
id: change-workflow
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/change-workflow
tags:
  - skupper
  - docs-landscape
  - administer
related:
  - configuration-backup
  - audit-records
timestamp: 2026-07-23T20:10:12Z
---

# Change Workflow

Change Workflow is the administrative process for modifying Skupper resources or operational settings. It covers pre-change capture, reviewed resource changes, application, validation, and post-change records.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Administrative Workflows

## Dependencies

- [Configuration Backup](./configuration-backup.md)
- [Audit Records](./audit-records.md)

## Sources

- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md): Local source for desired resources, generated resources, and platform-specific operations.
- [Skupper Ansible resource module](../skupper-ansible/skupper-ansible-module-resource.md): Generated local source for resource state management.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking sites, links, connectors, listeners, and collecting debug evidence.
- [Debug dump command](../../human/skupper-docs/input/refdog/commands/debug/dump.md): Local command reference for collecting site diagnostics.
- [Controlled Administrative Change](./controlled-change.md): Local landscape source for change outcome framing.

## Website Links

- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Refdog debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Use before and after evidence for every meaningful change.
- Prefer declarative resource changes when they are part of an audited workflow.
- Avoid depending on internal labels or generated implementation details.
