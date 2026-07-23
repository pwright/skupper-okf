---
type: DocumentationLandscapePage
title: "Cluster and Host Inventory"
id: site-inventory
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-inventory
tags:
  - skupper
  - docs-landscape
  - plan
timestamp: 2026-07-23T19:54:51Z
---

# Cluster and Host Inventory

Cluster and Host Inventory records where application components run and where Skupper sites could be created. It should include Kubernetes namespaces, local-system platforms, network reachability constraints, and any site that may need to accept links.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Planning Inputs

## Sources

- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md): Primary local concept source for sites, platforms, namespaces, workloads, and dynamic network membership.
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md): Local concept source for platform terminology.
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source for controller and CLI prerequisites across Kubernetes and local systems.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for namespace-context assumptions and site creation prerequisites.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for site-level router responsibilities and site resource concerns.

## Website Links

- [Refdog site concept](https://skupperproject.github.io/refdog/concepts/site.html)
- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)

## Draft Notes

- Capture platform, namespace or host, access permissions, expected workloads, and network boundary notes for each candidate site.
- Identify which sites can expose link access and which must initiate outbound links.
- Record resource constraints early because they affect capacity and console placement.
