---
type: DocumentationLandscapePage
title: "Preview Installation"
id: preview-installation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/preview-installation
tags:
  - skupper
  - docs-landscape
  - previews
related:
  - compatibility-checks
timestamp: 2026-07-23T19:46:31Z
---

# Preview Installation

Preview installation documents the controlled path for installing a preview capability after compatibility is checked. This page should make clear where standard installation applies and where preview-specific manifests, flags, images, charts, or configuration are required.

## Appears in

- [Skupper Technology Previews](./skupper-previews.md) / Preview Controls

## Dependencies

- [Compatibility Checks](./compatibility-checks.md)

## Sources

- [Compatibility checks](./compatibility-checks.md): Dependency page for pre-install readiness.
- [Install docs](../../human/skupper-docs/input/install/index.md): Local source for stable CLI, YAML, Helm, Operator, and local-system installation paths.
- [System install command](../../human/skupper-docs/input/refdog/commands/system/install.md): Local command reference for local-system controller installation.
- [Console installation docs](../../human/skupper-docs/input/console/index.md): Local source for Network Observer installation when a preview affects console/observer behavior.

## Website Links

- [Skupper install docs](https://skupper.io/docs/install/index.html)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

## Draft Notes

- Preview installation instructions should be versioned and reversible.
- Do not reuse production credentials or namespaces for exploratory preview installs.
