---
type: DocumentationLandscapePage
title: "Configuration and State Backup"
id: backup-state
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/backup-state
tags:
  - skupper
  - docs-landscape
  - upgrade
timestamp: 2026-07-23T20:03:45Z
---

# Configuration and State Backup

Configuration and State Backup identifies the resources and records needed before an upgrade. Local docs describe Skupper resources, generated Kubernetes resources, local-system resource locations, and debug dumps; use those as candidates rather than inventing a backup procedure.

## Appears in

- [Upgrade Skupper](./upgrade-skupper.md) / Upgrade Readiness

## Sources

- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md): Primary local source for input resources, generated runtime resources, and local-system resource storage.
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md): Local source for Kubernetes resources, secrets, services, and ConfigMaps created by Skupper.
- [Debug dump command](../../human/skupper-docs/input/refdog/commands/debug/dump.md): Local command reference candidate for collecting diagnostic state.
- [Debug dumps topic](../../human/skupper-docs/input/refdog/topics/debug-dumps.md): Local source candidate for support evidence bundles.
- [Skupper Ansible system module](../skupper-ansible/skupper-ansible-module-system.md): Generated local source for non-Kubernetes bundle actions.

## Website Links

- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Refdog debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)

## Draft Notes

- Record desired-state resources separately from generated runtime state.
- Include namespace, platform, version, and install method metadata with backups.
- Avoid handling secrets casually; define credential storage expectations before collecting state.
