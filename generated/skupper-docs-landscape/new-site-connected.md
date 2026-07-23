---
type: DocumentationLandscapePage
title: "New Site Connected"
id: new-site-connected
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/new-site-connected
tags:
  - skupper
  - docs-landscape
  - extend
related:
  - site-onboarding
  - link-establishment
timestamp: 2026-07-23T20:01:23Z
---

# New Site Connected

New Site Connected is the expansion outcome where an additional site has been initialized and joined to an existing Skupper application network. The page should focus on the evidence that the new site is part of the network before any new service exposure is added.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Outcomes

## Dependencies

- [Onboard a Site](./site-onboarding.md)
- [Establish a Link](./link-establishment.md)

## Sources

- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local planning source for adding sites, link access, link constraints, and validation checks.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for creating and updating sites with the CLI.
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for creating links and checking link status.
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md): Local concept source for sites and dynamic network membership.
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Local concept source for links joining sites into a network.

## Website Links

- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog site concept](https://skupperproject.github.io/refdog/concepts/site.html)

## Draft Notes

- Use site and link status as the initial acceptance evidence.
- Do not add service reachability claims until listener/connector matching has been validated.
- Capture whether the new site needs link access for future expansion.
