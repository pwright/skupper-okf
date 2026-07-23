---
type: DocumentationLandscapePage
title: "Runtime Resource Tuning"
id: resource-tuning
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-tuning
tags:
  - skupper
  - docs-landscape
  - optimize
related:
  - resource-profile
  - load-tests
timestamp: 2026-07-23T21:00:00Z
---

# Runtime Resource Tuning

Runtime resource tuning changes CPU, memory, and related runtime settings for Skupper and observer components after profiling current behavior.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Optimization Levers

## Dependencies

- [CPU and Memory Profile](./resource-profile.md)
- [Load Tests](./load-tests.md)

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for router CPU allocation and performance caveats.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Local source for site resource settings.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer, Prometheus, and proxy resource settings.
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md) - Site resource reference.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local source for diagnostics after tuning changes.

## Website Links

- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Keep Kubernetes resource settings separate from local-system lifecycle controls.
- Add before-and-after validation steps for each tuning change.
- Document resource changes as operational changes that need rollback criteria.
