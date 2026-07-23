---
type: DocumentationLandscapePage
title: "Managed Kubernetes Pattern"
id: managed-platform-pattern
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/managed-platform-pattern
tags:
  - skupper
  - docs-landscape
  - platform
related:
  - platform-profile
  - cloud-network-rules
timestamp: 2026-07-23T22:00:00Z
---

# Managed Kubernetes Pattern

The managed Kubernetes pattern adapts the general cluster workflow to environments where ingress, load balancers, routes, storage classes, and network controls are cloud-managed.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Patterns

## Dependencies

- [Platform Compatibility Profile](./platform-profile.md)
- [Cloud Network Rules](./cloud-network-rules.md)

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for link access defaults and firewall placement.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Kubernetes YAML site configuration source.
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - Kubernetes CLI site configuration source.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Console source for ingress, route, TLS, persistence, and metrics services.
- [human/skupper-docs/input/refdog/resources/router-access.md](../../human/skupper-docs/input/refdog/resources/router-access.md) - RouterAccess resource reference.

## Website Links

- [Kubernetes YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Kubernetes CLI site configuration](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [RouterAccess resource reference](https://skupperproject.github.io/refdog/resources/router-access.html)

## Draft Notes

- Keep cloud-specific rules generic until provider-specific source material exists.
- Focus on external access type, firewall rules, DNS or hostnames, and storage assumptions.
- Include checks for whether a LoadBalancer, Route, or Ingress is actually provisioned.
