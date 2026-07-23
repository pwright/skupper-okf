---
type: DocumentationLandscapePage
title: "Operator Package"
id: operator-package
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/operator-package
tags:
  - skupper
  - docs-landscape
  - install
related:
  - platform-prerequisites
timestamp: 2026-07-23T19:57:36Z
---

# Operator Package

Operator Package tracks the artifact or catalog source for installing Skupper through an operator. Current local docs identify Operator as an installation method but do not provide active detailed package instructions, so this page should act as a source placeholder and verification checklist.

## Appears in

- [Install Skupper](./install-skupper.md) / Prerequisites and Validation

## Dependencies

- [Kubernetes Platform Prerequisites](./platform-prerequisites.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source that lists Operator as a controller installation method and contains disabled draft notes.
- [Skupper source entry](../../sources/skupper.md): Local source record for upstream release and packaging verification.
- [Skupper releases](../../sources/skupper.md): Local source candidate that should be paired with upstream release artifacts.
- [Controller configuration topic](../../human/skupper-docs/input/refdog/topics/controller-configuration.md): Local source candidate for controller configuration constraints.
- [Skupper resources overview](../../human/skupper-docs/input/refdog/resources/index.md): Local source for what the controller reconciles after installation.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Skupper GitHub repository](https://github.com/skupperproject/skupper)

## Draft Notes

- Verify current operator catalog, channel, and supported platforms before adding procedural instructions.
- Record package provenance and version compatibility alongside the installation method.
- Keep this separate from Helm and direct YAML controller installation.
