---
type: DocumentationLandscapePage
title: "Site Configuration"
id: site-configuration
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-configuration
tags:
  - skupper
  - docs-landscape
  - administer
timestamp: 2026-07-23T20:10:12Z
---

# Site Configuration

Site Configuration is the current desired state for a Skupper site, including site name, namespace or platform, link access, HA, resource settings, and generated resources that reflect that desired state.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Operational State

## Sources

- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for site create, update, HA, status, and delete workflows.
- [Kubernetes YAML site configuration](../../human/skupper-docs/input/kube-yaml/site-configuration.md): Local source candidate for declarative site configuration.
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md): Local resource reference for Site fields.
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md): Local source for Kubernetes resources created by the controller and site.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for operational checks, link constraints, resources, and traffic direction.

## Website Links

- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Skupper YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Refdog site resource](https://skupperproject.github.io/refdog/resources/site.html)

## Draft Notes

- Distinguish desired configuration from runtime status.
- Document changes to link access and HA carefully because they affect link behavior.
- Do not edit generated ConfigMaps directly unless source docs explicitly direct it.
