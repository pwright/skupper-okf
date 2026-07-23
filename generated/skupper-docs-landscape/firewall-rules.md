---
type: DocumentationLandscapePage
title: "Firewall Rules"
id: firewall-rules
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/firewall-rules
tags:
  - skupper
  - docs-landscape
  - secure
timestamp: 2026-07-23T20:30:00Z
---

# Firewall Rules

Firewall rules describe the network paths that must be allowed for Skupper links and externally exposed management surfaces such as the network console.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Isolation Foundations

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source candidate for firewall placement and link access concerns.
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - CLI source for link access configuration.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - YAML source for link access configuration.
- [human/skupper-docs/input/refdog/resources/router-access.md](../../human/skupper-docs/input/refdog/resources/router-access.md) - RouterAccess resource reference.
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md) - Local source with network console placement considerations.

## Website Links

- [Site configuration with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [RouterAccess resource reference](https://skupperproject.github.io/refdog/resources/router-access.html)
- [Network console](https://skupper.io/docs/console/index.html)

## Draft Notes

- Keep port and protocol requirements source-backed; do not infer environment-specific firewall rules.
- Distinguish link access ingress from service traffic that stays inside the Skupper application network.
- Add platform-specific notes for OpenShift Route, Kubernetes LoadBalancer, and local-system access only where the source docs support them.
