---
type: DocumentationLandscapePage
title: "Mutual Authentication"
id: mutual-authentication
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/mutual-authentication
tags:
  - skupper
  - docs-landscape
  - secure
related:
  - site-certificates
  - trust-bundle
timestamp: 2026-07-23T20:30:00Z
---

# Mutual Authentication

Mutual authentication is the link security model where connected Skupper sites prove identity with certificate material instead of relying only on network reachability.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Security Controls

## Dependencies

- [Site Certificates](./site-certificates.md)
- [Trust Bundle](./trust-bundle.md)

## Sources

- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md) - Local topic source for router TLS configuration.
- [human/skupper-docs/input/refdog/concepts/access-token.md](../../human/skupper-docs/input/refdog/concepts/access-token.md) - Concept source for token exchange as part of link creation.
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md) - Resource reference for links.
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md) - Resource reference for access tokens.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source with conservative notes on mutual TLS for inter-site traffic.

## Website Links

- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Access token resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)

## Draft Notes

- Explain authentication at the site-link level before discussing token issue or redemption commands.
- Avoid claiming exact certificate internals unless sourced from the router TLS or resource reference pages.
- Add a future troubleshooting table for failed authentication, expired credentials, and mismatched trust material.
