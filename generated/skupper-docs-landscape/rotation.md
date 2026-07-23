---
type: DocumentationLandscapePage
title: "Certificate Rotation"
id: rotation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rotation
tags:
  - skupper
  - docs-landscape
  - secure
related:
  - issuance
timestamp: 2026-07-23T20:30:00Z
---

# Certificate Rotation

Certificate rotation is the process of replacing or refreshing certificate material used by Skupper sites and links without leaving stale trust assumptions undocumented.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Isolation Foundations

## Dependencies

- [Certificate Issuance](./issuance.md)

## Sources

- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md) - Local source candidate for TLS certificate behavior.
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - CLI source for creating new token and link material.
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md) - YAML source for declarative link resources.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Troubleshooting source for collecting status and debug information.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source candidate for token expiry and link replacement considerations.

## Website Links

- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Source coverage for explicit rotation procedures is thin; keep this as a candidate page until supported steps are confirmed.
- Start future expansion with detection and replacement scenarios rather than assuming automatic behavior.
- Link back to issuance because most practical recovery procedures begin by creating fresh link material.
