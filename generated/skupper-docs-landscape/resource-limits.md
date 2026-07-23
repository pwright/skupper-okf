---
type: DocumentationLandscapePage
title: "Resource Limits"
id: resource-limits
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-limits
tags:
  - skupper
  - docs-landscape
  - configure
related: []
timestamp: 2026-07-23T20:17:03Z
---

# Resource Limits

Resource limits cover the site resource settings used to allocate CPU and memory to Skupper components, especially the router, when default resource behavior is not sufficient.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Inputs

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Site performance and resource allocation summary.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Site resource configuration examples.
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md) - Site resource reference for supported fields.
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md) - Overview of Skupper-managed Kubernetes resources.
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - CLI site update and status procedures.

## Website Links

- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Site configuration with CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Network deployment concerns](https://pwright.github.io/skupper-okf/generated/concepts/network-deployment-concerns)

## Draft Notes

- Add a small sizing discussion only after confirming current product guidance; do not turn examples into recommendations without source support.
- Link to Kubernetes QoS concepts only if the public docs page is added as an accepted external source in a later pass.
- Include verification steps that show the effective resource settings on deployed Skupper pods.
