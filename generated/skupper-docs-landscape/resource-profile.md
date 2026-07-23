---
type: DocumentationLandscapePage
title: "CPU and Memory Profile"
id: resource-profile
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-profile
tags:
  - skupper
  - docs-landscape
  - optimize
timestamp: 2026-07-23T21:00:00Z
---

# CPU and Memory Profile

A CPU and memory profile captures current resource allocation and observed utilization for Skupper routers, controllers, observer services, and related monitoring components.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Validation Inputs

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for router CPU allocation and performance notes.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Local source for site resource settings.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for network observer, Prometheus, and proxy resource limits.
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md) - Site resource reference.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local diagnostic source for collecting evidence.

## Website Links

- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Capture configured requests and limits separately from observed utilization.
- Include observer and Prometheus resources when the network console is part of the deployment.
- Add repeatable measurement steps for pre-change and post-change comparison.
