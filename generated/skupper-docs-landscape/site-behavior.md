---
type: DocumentationLandscapePage
title: "Configured Site Behavior"
id: site-behavior
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-behavior
tags:
  - skupper
  - docs-landscape
  - configure
related:
  - site-config
  - runtime-settings
timestamp: 2026-07-23T20:17:03Z
---

# Configured Site Behavior

Configured site behavior covers the site-level settings that determine how a Skupper site participates in the application network, including identity, link access, availability posture, and runtime resource choices.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configured Behavior

## Dependencies

- [Site Configuration](./site-config.md)
- [Runtime Settings](./runtime-settings.md)

## Sources

- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - CLI procedures for creating, updating, deleting, and checking a site.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - YAML procedures for site creation, high availability, and site resources.
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md) - Site resource fields and status reference.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Deployment concerns for resource allocation, high availability, and link access.
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md) - Overview of resources created and managed by Skupper.

## Website Links

- [Site configuration with CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)

## Draft Notes

- Frame this as an outcome page, not a resource reference: the reader should know what behavior changes when site settings change.
- Add a matrix later for link access, high availability, resource settings, and platform-specific support.
- Keep security-sensitive identity and certificate details linked to the security map when that map is expanded.
