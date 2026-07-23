---
type: DocumentationLandscapePage
title: "Configuration Backup"
id: configuration-backup
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/configuration-backup
tags:
  - skupper
  - docs-landscape
  - administer
timestamp: 2026-07-23T20:10:12Z
---

# Configuration Backup

Configuration Backup captures the desired state and diagnostic evidence needed before administrative changes. It should separate user-authored Skupper resources from generated runtime state and protect any secret material.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Governance Controls

## Sources

- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md): Local source for desired resources, generated resources, and platform-specific operations.
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md): Local source for Kubernetes resources, ConfigMaps, secrets, and services.
- [Debug dump command](../../human/skupper-docs/input/refdog/commands/debug/dump.md): Local command reference for collecting diagnostic archives.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking sites, links, connectors, listeners, and collecting debug evidence.
- [Skupper Ansible system module](../skupper-ansible/skupper-ansible-module-system.md): Generated local source for non-Kubernetes bundle actions.

## Website Links

- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Refdog debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)

## Draft Notes

- Back up desired-state resources before changing them.
- Treat secrets and token material according to the credential policy.
- Use debug dumps for troubleshooting evidence, not as a casual public artifact.
