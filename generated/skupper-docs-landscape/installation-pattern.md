---
type: DocumentationLandscapePage
title: "Installation Pattern"
id: installation-pattern
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/installation-pattern
tags:
  - skupper
  - docs-landscape
  - platform
related:
  - platform-profile
timestamp: 2026-07-23T22:00:00Z
---

# Installation Pattern

An installation pattern selects the appropriate Skupper install path and follows it with site initialization and validation for the target platform.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Inputs

## Dependencies

- [Platform Compatibility Profile](./platform-profile.md)

## Sources

- [human/skupper-docs/input/install/index.md](../../human/skupper-docs/input/install/index.md) - Local installation entry point.
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - Kubernetes CLI site creation source.
- [human/skupper-docs/input/system-cli/site-configuration.md](../../human/skupper-docs/input/system-cli/site-configuration.md) - System CLI site creation source.
- [human/skupper-docs/input/refdog/commands/system/install.md](../../human/skupper-docs/input/refdog/commands/system/install.md) - System install command reference.
- [human/skupper-docs/input/refdog/commands/site/create.md](../../human/skupper-docs/input/refdog/commands/site/create.md) - Site create command reference.

## Website Links

- [Installation](https://skupper.io/docs/install/index.html)
- [Kubernetes CLI site configuration](https://skupper.io/docs/kube-cli/site-configuration.html)
- [System CLI site configuration](https://skupper.io/docs/system-cli/site-configuration.html)
- [System install command](https://skupperproject.github.io/refdog/commands/system/install.html)
- [Site create command](https://skupperproject.github.io/refdog/commands/site/create.html)

## Draft Notes

- Keep installation, site creation, and service exposure as separate phases.
- Add platform-specific pre-checks before installation commands.
- Include a post-install validation step with site status or debug checks.
