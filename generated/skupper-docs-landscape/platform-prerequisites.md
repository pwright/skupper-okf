---
type: DocumentationLandscapePage
title: "Kubernetes Platform Prerequisites"
id: platform-prerequisites
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/platform-prerequisites
tags:
  - skupper
  - docs-landscape
  - install
timestamp: 2026-07-23T19:57:36Z
---

# Kubernetes Platform Prerequisites

Kubernetes Platform Prerequisites captures what must be true before installing Skupper on Kubernetes. Local docs explicitly call out cluster-admin access for controller installation and controller scope decisions that affect where sites can be created.

## Appears in

- [Install Skupper](./install-skupper.md) / Prerequisites and Validation

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for Kubernetes controller prerequisites and scope notes.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for prerequisites before creating a Kubernetes site.
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md): Local source for service accounts, roles, deployments, ConfigMaps, secrets, and services created by Skupper.
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md): Local concept source for Kubernetes as a supported platform.
- [Controller configuration topic](../../human/skupper-docs/input/refdog/topics/controller-configuration.md): Local source candidate for controller configuration inputs.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)

## Draft Notes

- Record cluster-admin or delegated permission requirements separately from namespace-level site ownership.
- Include controller scope because it changes which namespaces can host sites.
- Avoid distribution-specific assumptions until platform guide pages are processed.
