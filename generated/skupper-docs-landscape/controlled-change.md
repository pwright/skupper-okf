---
type: DocumentationLandscapePage
title: "Controlled Administrative Change"
id: controlled-change
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/controlled-change
tags:
  - skupper
  - docs-landscape
  - administer
related:
  - change-workflow
  - access-controls
timestamp: 2026-07-23T20:10:12Z
---

# Controlled Administrative Change

Controlled Administrative Change is the outcome where a Skupper configuration or operational change is planned, applied, validated, and recorded. Source coverage is indirect, so this page frames control as evidence and process around Skupper resources.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Operational Outcomes

## Dependencies

- [Change Workflow](./change-workflow.md)
- [Administrative Access Controls](./access-controls.md)

## Sources

- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md): Local source for desired resources, generated resources, and platform-specific operations.
- [Skupper Ansible resource module](../skupper-ansible/skupper-ansible-module-resource.md): Generated local source for applying, updating, and removing Skupper resource YAML.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking sites, links, connectors, listeners, and collecting debug evidence.
- [Configuration Backup](./configuration-backup.md): Local landscape source for pre-change backup expectations.
- [Audit Records](./audit-records.md): Local landscape source for recording change evidence.

## Website Links

- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Capture before state, intended change, applied resources, validation result, and rollback note.
- Assign a change owner and reviewer for sensitive link or credential changes.
- Do not treat generated internal labels as stable automation inputs.
