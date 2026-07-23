---
type: DocumentationLandscapePage
title: "Namespace Scope"
id: namespace-scope
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/namespace-scope
tags:
  - skupper
  - docs-landscape
  - configure
related: []
timestamp: 2026-07-23T20:17:03Z
---

# Namespace Scope

Namespace scope describes where Skupper site resources, service exposure resources, and workload bindings are created, and how that placement affects what the site can select or attach to.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Inputs

## Sources

- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - Site creation and update commands that operate in a Kubernetes namespace.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - YAML examples showing namespace placement for Site resources.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Listener, Connector, and attached connector examples across site and workload namespaces.
- [generated/concepts/connector.md](../concepts/connector.md) - Attached connector discussion and namespace split between site and workload namespaces.
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md) - Overview of resources created in and managed by Skupper.

## Website Links

- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Attached connector resource reference](https://skupperproject.github.io/refdog/resources/attached-connector.html)
- [Connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)

## Draft Notes

- Add a future table for site namespace, workload namespace, attached connector namespace, and binding namespace.
- Avoid overgeneralizing cluster-wide requirements; attached connector behavior should be sourced directly from the attached connector docs.
- Cross-link this page from site configuration, connector configuration, and security/access policy pages.
