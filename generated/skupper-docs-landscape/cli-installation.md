---
type: DocumentationLandscapePage
title: "CLI Installation"
id: cli-installation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-installation
tags:
  - skupper
  - docs-landscape
  - install
related:
  - platform-prerequisites
  - cli-package
timestamp: 2026-07-23T19:57:36Z
---

# CLI Installation

CLI Installation covers the path where users install Skupper tooling and then create or manage sites through the `skupper` command. On Kubernetes, the local docs require the Skupper controller before creating a site; on local systems, the CLI is the required entry point.

## Appears in

- [Install Skupper](./install-skupper.md) / Installation Methods

## Dependencies

- [Kubernetes Platform Prerequisites](./platform-prerequisites.md)
- [CLI Package](./cli-package.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for CLI installation, controller installation, and upgrade commands.
- [Kubernetes CLI overview](../../human/skupper-docs/input/kube-cli/index.md): Local source describing CLI use after the controller is installed.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for checking CLI installation and creating a simple site.
- [CLI command overview](../../human/skupper-docs/refdog/config/commands/overview.md): Local source for CLI role, platform context, and command groups.
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md): Local command reference for validating CLI and component versions.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper Kubernetes CLI overview](https://skupper.io/docs/kube-cli/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

## Draft Notes

- Make it clear whether the page is installing only the CLI or also installing the Kubernetes controller.
- Keep version-specific command examples aligned with the installation guide.
- Point Kubernetes users to controller scope decisions before site creation.
