---
type: DocumentationLandscapePage
title: "Select Installation Method"
id: installation-method
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/installation-method
tags:
  - skupper
  - docs-landscape
  - install
related:
  - cli-installation
  - operator-installation
  - host-installation
timestamp: 2026-07-23T19:57:36Z
---

# Select Installation Method

Select Installation Method helps users choose between Kubernetes controller installation paths and local-system installation. The local installation guide supports direct YAML, Helm chart, Operator as a named method, and CLI-driven local-system setup.

## Appears in

- [Install Skupper](./install-skupper.md) / Installation Methods

## Dependencies

- [CLI Installation](./cli-installation.md)
- [Operator Installation](./operator-installation.md)
- [Host Installation](./host-installation.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for available controller installation methods and local-system CLI requirements.
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md): Local concept source for platform categories.
- [Kubernetes CLI overview](../../human/skupper-docs/input/kube-cli/index.md): Local source for CLI-driven Kubernetes workflows after controller installation.
- [Skupper resources overview](../../human/skupper-docs/input/refdog/resources/index.md): Local source for the controller/resource model behind installation.
- [Skupper Ansible overview](../skupper-ansible/skupper-ansible-overview.md): Generated local source for automation-driven installation context.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Refdog platform concept](https://skupperproject.github.io/refdog/concepts/platform.html)

## Draft Notes

- Use a decision table: platform, permissions, preferred automation style, and desired controller scope.
- Keep Operator guidance marked as source-thin until current public procedure coverage exists.
- Connect this page directly to site initialization after the method is selected.
