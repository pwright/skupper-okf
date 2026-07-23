---
type: DocumentationLandscapePage
title: "Version Control"
id: version-control
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/version-control
tags:
  - skupper
  - docs-landscape
  - develop
timestamp: 2026-07-23T21:30:00Z
---

# Version Control

Version control provides review, history, and promotion discipline for Skupper YAML resources, automation playbooks, and example-derived configuration.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Developer Foundations

## Sources

- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md) - Local source index for YAML workflows.
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md) - Local source index for local-system YAML workflows.
- [human/skupper-docs/input/kube-yaml/custom-labels.md](../../human/skupper-docs/input/kube-yaml/custom-labels.md) - Local source for labels and annotations useful in managed resources.
- [generated/skupper-ansible/skupper-ansible-overview.md](../skupper-ansible/skupper-ansible-overview.md) - Generated source for automation modules and workflows.
- [generated/workflows/skupper-examples.md](../workflows/skupper-examples.md) - Generated source for example workflow material.

## Website Links

- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [Custom labels with YAML](https://skupper.io/docs/kube-yaml/custom-labels.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Define what belongs in version control: desired resources, automation code, test manifests, and documentation.
- Define what does not belong there: short-lived tokens, generated secrets, environment-specific credentials, and private debug bundles.
- Add review checks for resource ownership labels and environment-specific overlays.
