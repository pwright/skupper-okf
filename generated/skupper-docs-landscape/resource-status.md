---
type: DocumentationLandscapePage
title: "Resource Status"
id: resource-status
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-status
tags:
  - skupper
  - docs-landscape
  - reference
timestamp: 2026-07-23T22:15:00Z
---

# Resource Status

Resource status records the observed state of Skupper resources, including readiness conditions, matching state, generated endpoint information, and error signals.

## Appears in

- [Skupper Reference](./skupper-reference.md) / Syntax and Schema

## Sources

- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md) - Local resource status topic.
- [generated/skupper/skupper-crd-sites-skupper-io.md](../skupper/skupper-crd-sites-skupper-io.md) - Generated Site CRD status source.
- [generated/skupper/skupper-crd-links-skupper-io.md](../skupper/skupper-crd-links-skupper-io.md) - Generated Link CRD status source.
- [generated/concepts/listener.md](../concepts/listener.md) - Generated source for listener matching and readiness.
- [generated/concepts/connector.md](../concepts/connector.md) - Generated source for connector matching and readiness.

## Website Links

- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

## Draft Notes

- Add per-resource status summaries after verifying exact current fields.
- Separate status conditions from command status output and observer API state.
- Include common "not ready" causes only where source-backed.
