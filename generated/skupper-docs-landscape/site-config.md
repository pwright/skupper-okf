---
type: DocumentationLandscapePage
title: "Site Configuration"
id: site-config
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-config
tags:
  - skupper
  - docs-landscape
  - configure
related:
  - site-identity-config
  - namespace-scope
timestamp: 2026-07-23T20:17:03Z
---

# Site Configuration

Site configuration defines the Skupper site resource and the site-level settings that control how the local namespace or system joins and serves the application network.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Resources

## Dependencies

- [Site Identity Settings](./site-identity-config.md)
- [Namespace Scope](./namespace-scope.md)

## Sources

- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - CLI path for creating a site, enabling link access, checking status, and updating a site.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Declarative Site resource examples, including high availability and resource configuration.
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md) - Detailed Site resource reference.
- [human/skupper-docs/input/refdog/concepts/site.md](../../human/skupper-docs/input/refdog/concepts/site.md) - Conceptual description of a Skupper site.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Notes on resource allocation, high availability, and link access.

## Website Links

- [Site configuration with CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Site concept](https://skupperproject.github.io/refdog/concepts/site.html)

## Draft Notes

- Split future content into creation, update, and validation flows so it serves both first-time setup and day-two configuration.
- Include examples for `linkAccess` and high availability only where the source docs explicitly support them.
- Add cautions around direct edits to generated or controller-managed resources, using the resources overview as the source.
