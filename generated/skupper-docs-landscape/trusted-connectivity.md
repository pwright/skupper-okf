---
type: DocumentationLandscapePage
title: "Trusted Site Connectivity"
id: trusted-connectivity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/trusted-connectivity
tags:
  - skupper
  - docs-landscape
  - secure
related:
  - mutual-authentication
  - certificate-lifecycle
timestamp: 2026-07-23T20:30:00Z
---

# Trusted Site Connectivity

Trusted site connectivity is the security outcome where Skupper sites link through authenticated link resources and certificate material that is issued, exchanged, and maintained by supported Skupper workflows.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Security Outcomes

## Dependencies

- [Mutual Authentication](./mutual-authentication.md)
- [Certificate Lifecycle](./certificate-lifecycle.md)

## Sources

- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - CLI workflow for token-based site linking.
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md) - Declarative site-linking examples with link resources.
- [human/skupper-docs/input/refdog/concepts/link.md](../../human/skupper-docs/input/refdog/concepts/link.md) - Local concept source for the link model.
- [human/skupper-docs/input/refdog/concepts/access-token.md](../../human/skupper-docs/input/refdog/concepts/access-token.md) - Local concept source for token redemption and link credential exchange.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source candidate for link access, token restrictions, and firewall placement considerations.

## Website Links

- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [Link concept](https://skupperproject.github.io/refdog/concepts/link.html)
- [Access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)

## Draft Notes

- Expand around the complete link lifecycle: enable link access, issue or generate link material, apply it on the peer site, and confirm link status.
- Keep token handling separate from long-lived certificate behavior; the local sources describe tokens as exchange material, not as the link certificate itself.
- Add operational checks for expired, already redeemed, or misplaced link material once the troubleshooting source coverage is mapped.
