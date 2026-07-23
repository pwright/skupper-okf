---
type: DocumentationLandscapePage
title: "Site Identity"
id: site-identity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-identity
tags:
  - skupper
  - docs-landscape
  - extend
timestamp: 2026-07-23T20:01:23Z
---

# Site Identity

Site Identity records how a site is named, represented, and authenticated in the application network. Local sources describe each site as having router identity through certificates and site CA material, with links secured by mutual TLS.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Controls

## Sources

- [Skupper security overview](../../human/skupper-docs/input/overview/security.md): Primary local source for mutual TLS, private CA, and router certificates.
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md): Local source for site CA, local CA, and site-related Kubernetes secrets.
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md): Local concept source for site names, platform association, and network membership.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for custom certificates and link identity considerations.
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md): Local resource reference candidate for site identity fields and status.

## Website Links

- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Refdog site concept](https://skupperproject.github.io/refdog/concepts/site.html)

## Draft Notes

- Record site name, namespace or host context, owner, and certificate expectations.
- Do not conflate human-friendly site names with certificate or secret internals unless sourced.
- Point custom certificate requirements to secure-link or identity-policy topics.
