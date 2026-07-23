---
type: DocumentationLandscapePage
title: "Operator Installation"
id: operator-installation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/operator-installation
tags:
  - skupper
  - docs-landscape
  - install
related:
  - platform-prerequisites
  - operator-package
timestamp: 2026-07-23T19:57:36Z
---

# Operator Installation

Operator Installation is the Kubernetes installation path where a platform operator installs or manages the Skupper controller through an operator mechanism. The current local installation guide names Operator as an install method but keeps the detailed operator procedure disabled, so this page should remain conservative until a current source is available.

## Appears in

- [Install Skupper](./install-skupper.md) / Installation Methods

## Dependencies

- [Kubernetes Platform Prerequisites](./platform-prerequisites.md)
- [Operator Package](./operator-package.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source that lists Operator as a controller installation method and contains a disabled draft procedure.
- [Skupper resources overview](../../human/skupper-docs/input/refdog/resources/index.md): Local source for controller responsibilities after installation.
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md): Local concept source for supported platform terminology.
- [Controller configuration topic](../../human/skupper-docs/input/refdog/topics/controller-configuration.md): Local source candidate for controller-level configuration considerations.
- [Skupper source entry](../../sources/skupper.md): Local source record for the upstream Skupper repository when operator packaging details need verification.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub repository](https://github.com/skupperproject/skupper)

## Draft Notes

- Do not publish a step-by-step operator procedure from the disabled draft without current verification.
- Capture package source, channel, scope, and required platform permissions when reliable operator docs are available.
- Link users to YAML or Helm controller installation paths when operator coverage is incomplete.
