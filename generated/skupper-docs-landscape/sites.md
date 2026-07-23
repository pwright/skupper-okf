---
type: DocumentationLandscapePage
title: "Sites"
id: sites
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/sites
tags:
  - skupper
  - docs-landscape
  - discover
timestamp: 2026-07-23T19:44:12Z
---

# Sites

A Skupper site is a participating environment in the application network, such as a Kubernetes namespace or a local-system namespace. Sites host listeners, connectors, links, router components, and the configuration that defines local Skupper behavior.

## Appears in

- [Discover Skupper](./discover-skupper.md) / Foundations

## Sources

- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md): Primary local concept source for sites.
- [Site configuration topic](../../human/skupper-docs/input/refdog/topics/site-configuration.md): Local topic source for configuring sites.
- [Kubernetes YAML site configuration](../../human/skupper-docs/input/kube-yaml/site-configuration.md): Local procedural source for Kubernetes site configuration.
- [System YAML site configuration](../../human/skupper-docs/input/system-yaml/site-configuration.md): Local procedural source for local-system site configuration.

## Website Links

- [Site concept reference](https://skupper.io/docs/refdog/concepts/site.html)
- [Kubernetes site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)

## Draft Notes

- Clarify that a site is the unit that joins a Skupper network; it is not synonymous with an entire cluster in every platform.
- Use platform-specific pages for namespace and host details.
