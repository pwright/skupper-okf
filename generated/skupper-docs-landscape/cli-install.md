---
type: DocumentationLandscapePage
title: "Install the Skupper CLI"
id: cli-install
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-install
tags:
  - skupper
  - docs-landscape
  - get-started
related:
  - starter-prerequisites
timestamp: 2026-07-23T19:49:37Z
---

# Install the Skupper CLI

Install the Skupper CLI covers the command-line tool needed for the starter workflow. The local installation guide points to the Skupper install script for the latest release and to GitHub releases for a specific version.

## Appears in

- [Get Started with Skupper](./get-started.md) / Starter Setup

## Dependencies

- [Cluster or Host Prerequisites](./starter-prerequisites.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for installing or updating the CLI and for local-system controller installation.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source that verifies CLI installation with `skupper version`.
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md): Local command reference for checking installed component versions.
- [Skupper source entry](../../sources/skupper.md): Local source record for the upstream Skupper repository.

## Website Links

- [Skupper releases page](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Skupper install script](https://skupper.io/v2/install.sh)

## Draft Notes

- Keep command snippets aligned with the install guide rather than hard-coding a version.
- Include a verification step with `skupper version`.
- Add platform-specific installation caveats only when sourced from current installation docs.
