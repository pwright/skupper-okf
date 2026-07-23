---
type: DocumentationLandscapePage
title: "CLI Package"
id: cli-package
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-package
tags:
  - skupper
  - docs-landscape
  - install
related:
  - platform-prerequisites
timestamp: 2026-07-23T19:57:36Z
---

# CLI Package

CLI Package identifies the Skupper command-line artifact used by the installation and starter workflows. Local docs point to the Skupper install script for the latest release and GitHub releases for selecting a specific version.

## Appears in

- [Install Skupper](./install-skupper.md) / Prerequisites and Validation

## Dependencies

- [Kubernetes Platform Prerequisites](./platform-prerequisites.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for installing and updating the CLI.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for verifying the CLI with `skupper version`.
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md): Local command reference for version output.
- [Skupper source entry](../../sources/skupper.md): Local source record for upstream Skupper.
- [Skupper Docs source entry](../../sources/skupper-docs.md): Local source record for documentation snapshots.

## Website Links

- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Skupper install script](https://skupper.io/v2/install.sh)

## Draft Notes

- Avoid pinning a version in prose unless the release page is intentionally versioned.
- Include `skupper version` as the basic package verification step.
- Clarify when CLI package installation is separate from controller installation.
