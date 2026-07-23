---
type: DocumentationLandscapePage
title: "Validated Installation"
id: validated-install
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/validated-install
tags:
  - skupper
  - docs-landscape
  - install
related:
  - installed-site
  - health-checks
timestamp: 2026-07-23T19:57:36Z
---

# Validated Installation

Validated Installation confirms that the installed Skupper components can report a healthy site state and are ready for the next workflow. This page should collect the post-install evidence, while leaving deeper troubleshooting to the troubleshooting map.

## Appears in

- [Install Skupper](./install-skupper.md) / Installed Environment

## Dependencies

- [Operational Skupper Site](./installed-site.md)
- [Post-install Health Checks](./health-checks.md)

## Sources

- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Local source for checking controller, site, connector, listener, and link status.
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md): Local command reference for site readiness.
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md): Local command reference for installed component versions.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for `skupper version` and site creation validation.
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source for install paths that should be validated.

## Website Links

- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Refdog version command](https://skupperproject.github.io/refdog/commands/version.html)

## Draft Notes

- Treat validation as evidence collection: command used, namespace or platform, expected state, and actual state.
- Keep application traffic validation in getting-started or service exposure pages.
- Include failed validation pointers only when backed by troubleshooting sources.
