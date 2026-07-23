---
type: DocumentationLandscapePage
title: "Site Configuration Template"
id: site-template
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-template
tags:
  - skupper
  - docs-landscape
  - extend
timestamp: 2026-07-23T20:01:23Z
---

# Site Configuration Template

Site Configuration Template is the reusable site definition used when adding sites consistently. It should capture platform, namespace or local context, link access choice, resource settings, labels or annotations, and any high availability setting that is part of the standard deployment pattern.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Controls

## Sources

- [Kubernetes YAML site configuration](../../human/skupper-docs/input/kube-yaml/site-configuration.md): Primary local source candidate for declarative Site resource configuration.
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md): Local resource reference for Site fields and status.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for CLI options that may map into template choices.
- [Custom labels guide](../../human/skupper-docs/input/kube-yaml/custom-labels.md): Local source for propagating labels and annotations to generated resources.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for high availability and site resource considerations.

## Website Links

- [Skupper YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Refdog site resource](https://skupperproject.github.io/refdog/resources/site.html)
- [Skupper custom labels guide](https://skupper.io/docs/kube-yaml/custom-labels.html)

## Draft Notes

- Keep the template source-controlled if the deployment is declarative.
- Separate required fields from site-specific overrides.
- Include review notes for link access, resource limits, HA, and labels before reuse.
