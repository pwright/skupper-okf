---
type: DocumentationLandscapePage
title: "Onboard a Site"
id: site-onboarding
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-onboarding
tags:
  - skupper
  - docs-landscape
  - extend
related:
  - site-template
  - site-identity
timestamp: 2026-07-23T20:01:23Z
---

# Onboard a Site

Onboard a Site describes the repeatable process for adding another location to an existing Skupper network. It should reuse the installation and site initialization material, then add expansion-specific checks such as site identity, link access, and ownership.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Workflow

## Dependencies

- [Site Configuration Template](./site-template.md)
- [Site Identity](./site-identity.md)

## Sources

- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for creating a site and enabling link access later.
- [Kubernetes YAML site configuration](../../human/skupper-docs/input/kube-yaml/site-configuration.md): Local source candidate for declarative site configuration.
- [Site create command](../../human/skupper-docs/input/refdog/commands/site/create.md): Local command reference for site creation and link access.
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md): Local resource reference for declarative site settings.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for site resource and high availability considerations.

## Website Links

- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Creating a site with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Refdog site resource](https://skupperproject.github.io/refdog/resources/site.html)

## Draft Notes

- Use a checklist: platform ready, site config selected, site created, status ready, identity recorded.
- Treat link access as an explicit decision, not a default assumption.
- Point host or non-Kubernetes onboarding to platform-specific install pages when needed.
