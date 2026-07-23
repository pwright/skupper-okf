---
type: DocumentationLandscapePage
title: "Certificate Lifecycle"
id: certificate-lifecycle
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/certificate-lifecycle
tags:
  - skupper
  - docs-landscape
  - secure
related:
  - issuance
  - rotation
timestamp: 2026-07-23T20:30:00Z
---

# Certificate Lifecycle

Certificate lifecycle covers how Skupper obtains, stores, and refreshes certificate material used for site identity and link authentication.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Security Controls

## Dependencies

- [Certificate Issuance](./issuance.md)
- [Certificate Rotation](./rotation.md)

## Sources

- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md) - Local topic source for router TLS behavior.
- [human/skupper-docs/input/refdog/resources/access-grant.md](../../human/skupper-docs/input/refdog/resources/access-grant.md) - Resource reference for granting link access.
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md) - Resource reference for token redemption.
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md) - Link resource reference.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source candidate for certificate and token lifecycle notes.

## Website Links

- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Access grant resource reference](https://skupperproject.github.io/refdog/resources/access-grant.html)
- [Access token resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)

## Draft Notes

- Build the expanded page around issuance, storage, status checks, expiry, and replacement.
- Keep rotation guidance conservative until the exact supported procedures are confirmed from source docs.
- Include separate notes for Kubernetes and local-system platforms if their certificate handling differs.
