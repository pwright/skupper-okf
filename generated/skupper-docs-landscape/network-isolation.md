---
type: DocumentationLandscapePage
title: "Network Isolation"
id: network-isolation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/network-isolation
tags:
  - skupper
  - docs-landscape
  - secure
related:
  - namespace-controls
  - firewall-rules
timestamp: 2026-07-23T20:30:00Z
---

# Network Isolation

Network isolation describes the boundaries around a Skupper deployment: namespace scope, selected service exposure, link access placement, and the external network paths required for links.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Security Controls

## Dependencies

- [Namespace Controls](./namespace-controls.md)
- [Firewall Rules](./firewall-rules.md)

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for link access, firewall placement, and deployment concern notes.
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - CLI source for site creation and link access configuration.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - YAML source for site configuration.
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md) - Site resource reference including scope and access settings.
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md) - Local source with firewall placement considerations for the network console.

## Website Links

- [Site configuration with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Network console](https://skupper.io/docs/console/index.html)

## Draft Notes

- Keep this page focused on boundaries and placement; detailed service exposure belongs on the service policy page.
- Add diagrams that show link access sites, linking sites, and firewall-crossing paths.
- Verify Kubernetes NetworkPolicy coverage before adding prescriptive examples.
