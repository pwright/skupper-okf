---
type: DocumentationLandscapePage
title: "Cluster or Host Prerequisites"
id: starter-prerequisites
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/starter-prerequisites
tags:
  - skupper
  - docs-landscape
  - get-started
timestamp: 2026-07-23T19:49:37Z
---

# Cluster or Host Prerequisites

Cluster or Host Prerequisites collects the conditions a new user should satisfy before following the starter workflow. Local coverage is strongest for Kubernetes controller installation and CLI availability, with additional notes that local systems use the CLI and system install path.

## Appears in

- [Get Started with Skupper](./get-started.md) / Starter Setup

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for Kubernetes controller requirements, controller installation methods, CLI installation, and local-system setup.
- [Kubernetes CLI overview](../../human/skupper-docs/input/kube-cli/index.md): Local source describing CLI use after the Skupper controller is installed.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source listing prerequisites for creating a simple Kubernetes site.
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md): Local concept source for supported platform terminology.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

## Draft Notes

- Split Kubernetes and local-system prerequisites clearly.
- Avoid expanding into full platform support promises unless backed by a current source.
- Include access assumptions, such as controller installation requiring appropriate cluster permissions.
