---
type: DocumentationLandscapePage
title: "Post-install Health Checks"
id: health-checks
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/health-checks
tags:
  - skupper
  - docs-landscape
  - install
related:
  - site-initialization
timestamp: 2026-07-23T19:57:36Z
---

# Post-install Health Checks

Post-install Health Checks give users a short verification path immediately after installing Skupper and initializing a site. The local troubleshooting guide supports checking the controller, site status, and later connector, listener, and link status as the network grows.

## Appears in

- [Install Skupper](./install-skupper.md) / Prerequisites and Validation

## Dependencies

- [Site Initialization](./site-initialization.md)

## Sources

- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking controller and site status after installation.
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md): Local command reference for site status checks.
- [Debug check command](../../human/skupper-docs/input/refdog/commands/debug/check.md): Local command reference candidate for broader health checks.
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md): Local command reference for component version checks.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for site readiness after creation.

## Website Links

- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Refdog debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)

## Draft Notes

- Start with controller and site status before checking links or services.
- Keep checks platform-aware: Kubernetes can inspect resources directly, while other platforms report sites for the user.
- Link to troubleshooting when health checks fail instead of embedding a full failure catalog here.
