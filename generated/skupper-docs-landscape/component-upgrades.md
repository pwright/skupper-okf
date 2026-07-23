---
type: DocumentationLandscapePage
title: "CLI, Operator, and Router Upgrades"
id: component-upgrades
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/component-upgrades
tags:
  - skupper
  - docs-landscape
  - upgrade
related:
  - upgrade-sequence
  - backup-state
timestamp: 2026-07-23T20:03:45Z
---

# CLI, Operator, and Router Upgrades

CLI, Operator, and Router Upgrades covers the component-specific work inside an upgrade. The local installation guide documents updating the CLI, upgrading Kubernetes controllers through the same installation method, and reloading or reinstalling local-system controllers.

## Appears in

- [Upgrade Skupper](./upgrade-skupper.md) / Upgrade Execution

## Dependencies

- [Site Upgrade Sequence](./upgrade-sequence.md)
- [Configuration and State Backup](./backup-state.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for CLI updates, controller upgrade methods, local `system reload`, and local controller reinstall notes.
- [System install command](../../human/skupper-docs/input/refdog/commands/system/install.md): Local command reference for local-system controller setup.
- [System reload command](../../human/skupper-docs/input/refdog/commands/system/reload.md): Local command reference candidate for refreshing local-system definitions.
- [Skupper Ansible controller module](../skupper-ansible/skupper-ansible-module-controller.md): Generated local source for non-Kubernetes controller lifecycle automation.
- [Skupper Ansible system module](../skupper-ansible/skupper-ansible-module-system.md): Generated local source for start, reload, stop, and bundle actions on non-Kubernetes sites.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Refdog system install command](https://skupperproject.github.io/refdog/commands/system/install.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)

## Draft Notes

- Separate CLI upgrade, Kubernetes controller upgrade, local controller upgrade, and site reload steps.
- Capture the original installation method because controller upgrades should follow that method.
- Verify whether operator-specific upgrade guidance exists before documenting operator actions.
