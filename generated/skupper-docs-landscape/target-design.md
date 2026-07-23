---
type: DocumentationLandscapePage
title: "Target Deployment Design"
id: target-design
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/target-design
tags:
  - skupper
  - docs-landscape
  - migrate
timestamp: 2026-07-23T20:07:08Z
---

# Target Deployment Design

Target Deployment Design defines the Skupper deployment, topology, resources, and service exposure model that will replace or coexist with the source deployment. It should translate source behavior into explicit v2-style sites, links, connectors, listeners, and routing keys where applicable.

## Appears in

- [Migrate to or Between Skupper Deployments](./migrate-skupper.md) / Migration Readiness

## Sources

- [Migrating from Skupper v1](../../human/skupper-docs/input/overview/migrating.md): Local source for v2 site, link, connector, listener, and routing-key terminology.
- [Target Application Network Topology](./target-topology.md): Local landscape source for topology design.
- [Service Definition](./service-definition.md): Local landscape source for service-level definitions.
- [Routing Policy](./routing-policy.md): Local landscape source for routing keys, distribution, and failover choices.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for site, link, service, and traffic-direction planning.

## Website Links

- [Migrating from Skupper v1](https://skupper.io/docs/overview/migrating.html)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Skupper YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)

## Draft Notes

- Design the target as explicit resources and validation expectations, not just a copy of the source.
- Record every source service that needs a target connector/listener pair.
- Include platform, namespace, and ownership changes as part of the target design.
