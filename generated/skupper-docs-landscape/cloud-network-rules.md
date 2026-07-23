---
type: DocumentationLandscapePage
title: "Cloud Network Rules"
id: cloud-network-rules
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cloud-network-rules
tags:
  - skupper
  - docs-landscape
  - platform
timestamp: 2026-07-23T22:00:00Z
---

# Cloud Network Rules

Cloud network rules describe the managed load balancer, route, ingress, firewall, and egress allowances needed for Skupper link access and observer access.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Inputs

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for link access and firewall placement.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Site configuration source for link access.
- [human/skupper-docs/input/refdog/resources/router-access.md](../../human/skupper-docs/input/refdog/resources/router-access.md) - RouterAccess resource reference.
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md) - Network console placement source.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Console ingress, route, TLS, and metrics endpoint source.

## Website Links

- [Kubernetes YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [RouterAccess resource reference](https://skupperproject.github.io/refdog/resources/router-access.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)

## Draft Notes

- Avoid provider-specific port or firewall claims until source docs exist.
- Document the difference between link access ingress and internal service routing.
- Include observer and metrics endpoint exposure cautions.
