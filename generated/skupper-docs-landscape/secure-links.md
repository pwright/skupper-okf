---
type: DocumentationLandscapePage
title: "Secure Links"
id: secure-links
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/secure-links
tags:
  - skupper
  - docs-landscape
  - discover
related:
  - links
  - identity-model
timestamp: 2026-07-23T19:44:12Z
---

# Secure Links

Secure links are authenticated connections between Skupper sites. This page should explain that links are the transport relationships that let sites exchange reachability and forward application traffic while relying on Skupper identity and credentials.

## Appears in

- [Discover Skupper](./discover-skupper.md) / Core Concepts

## Dependencies

- [Site Links](./links.md)
- [Certificates and Identity](./identity-model.md)

## Sources

- [Site linking topic](../../human/skupper-docs/input/refdog/topics/site-linking.md): Local topic source for site linking concepts.
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Local concept source for link model and behavior.
- [Kubernetes YAML site linking](../../human/skupper-docs/input/kube-yaml/site-linking.md): Local procedural source for Kubernetes link resources.
- [System YAML site linking](../../human/skupper-docs/input/system-yaml/site-linking.md): Local procedural source for local-system link resources.
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md): Local source for token-based link access flow.

## Website Links

- [Kubernetes site linking](https://skupper.io/docs/kube-yaml/site-linking.html)
- [System site linking](https://skupper.io/docs/system-yaml/site-linking.html)

## Draft Notes

- Call out link access and credential generation before describing remote link creation.
- Tie link trust to certificate and token concepts, not to generic network reachability.
