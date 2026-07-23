---
type: DocumentationLandscapePage
title: "Firewall and Egress Controls"
id: network-controls
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/network-controls
tags:
  - skupper
  - docs-landscape
  - platform
timestamp: 2026-07-23T22:00:00Z
---

# Firewall and Egress Controls

Firewall and egress controls define which network paths must be allowed for Skupper sites to link and for optional observer or console endpoints to be reached.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Inputs

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for firewall and link access considerations.
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - Kubernetes site linking source.
- [human/skupper-docs/input/system-cli/site-linking.md](../../human/skupper-docs/input/system-cli/site-linking.md) - System site linking source.
- [human/skupper-docs/input/refdog/resources/router-access.md](../../human/skupper-docs/input/refdog/resources/router-access.md) - RouterAccess resource reference.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Console ingress, route, metrics, and TLS configuration source.

## Website Links

- [Kubernetes site linking](https://skupper.io/docs/kube-cli/site-linking.html)
- [System site linking](https://skupper.io/docs/system-cli/site-linking.html)
- [RouterAccess resource reference](https://skupperproject.github.io/refdog/resources/router-access.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)

## Draft Notes

- Keep network-control guidance tied to link access direction and exposed endpoints.
- Separate data-plane service traffic from control-plane link establishment and console access.
- Add environment-specific firewall tables only after source coverage exists.
