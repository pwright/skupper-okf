---
type: DocumentationLandscapePage
title: "Supported Platform Deployment"
id: supported-deployment
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/supported-deployment
tags:
  - skupper
  - docs-landscape
  - platform
related:
  - platform-profile
  - installation-pattern
timestamp: 2026-07-23T22:00:00Z
---

# Supported Platform Deployment

Supported platform deployment means choosing a Skupper installation and configuration path that matches the target Kubernetes or local-system environment.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Outcomes

## Dependencies

- [Platform Compatibility Profile](./platform-profile.md)
- [Installation Pattern](./installation-pattern.md)

## Sources

- [human/skupper-docs/input/install/index.md](../../human/skupper-docs/input/install/index.md) - Local source for installation entry points.
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - Kubernetes CLI site setup source.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Kubernetes YAML site setup source.
- [human/skupper-docs/input/system-cli/site-configuration.md](../../human/skupper-docs/input/system-cli/site-configuration.md) - Local-system CLI site setup source.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for platform and production deployment concerns.

## Website Links

- [Installation](https://skupper.io/docs/install/index.html)
- [Kubernetes CLI site configuration](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Kubernetes YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [System site configuration](https://skupper.io/docs/system-cli/site-configuration.html)

## Draft Notes

- Expand with platform prerequisites, chosen installation method, site creation, link access, and validation.
- Keep support claims tied to documented platform modes rather than inferred environment compatibility.
- Add a decision table for Kubernetes, managed Kubernetes, and local-system deployment paths.
