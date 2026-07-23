---
type: DocumentationLandscapePage
title: "Resource Automation Interface"
id: resource-automation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-automation
tags:
  - skupper
  - docs-landscape
  - integrate
timestamp: 2026-07-23T21:45:00Z
---

# Resource Automation Interface

The resource automation interface applies Skupper YAML resources through Kubernetes tools, local-system resource files, or automation modules.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Platform Interfaces

## Sources

- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md) - Local source index for Kubernetes YAML workflows.
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md) - Local source index for system YAML workflows.
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md) - Generated source for applying Skupper resource YAML.
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md) - Resource reference index.
- [human/skupper-docs/input/refdog/commands/site/generate.md](../../human/skupper-docs/input/refdog/commands/site/generate.md) - Command reference for generating site YAML.

## Website Links

- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Site generate command](https://skupperproject.github.io/refdog/commands/site/generate.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Describe which automation path owns which resource lifecycle.
- Include status validation after resource application.
- Add guidance for generated YAML review before applying it in shared environments.
