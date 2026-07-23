---
type: DocumentationLandscapePage
title: "Connector Configuration"
id: connector-config
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/connector-config
tags:
  - skupper
  - docs-landscape
  - configure
related:
  - backend-endpoint
timestamp: 2026-07-23T20:17:03Z
---

# Connector Configuration

Connector configuration describes the backend endpoint Skupper should expose and the routing key that remote listeners use to reach that backend.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Resources

## Dependencies

- [Backend Endpoint](./backend-endpoint.md)

## Sources

- [generated/concepts/connector.md](../concepts/connector.md) - Connector concept, core fields, attached connector notes, and verification details.
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md) - CLI connector creation and status checks.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Connector and attached connector YAML examples.
- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md) - Local-system connector creation flow.
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md) - Connector resource field reference.

## Website Links

- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)
- [Connector command reference](https://skupperproject.github.io/refdog/commands/connector/create.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Attached connector resource reference](https://skupperproject.github.io/refdog/resources/attached-connector.html)

## Draft Notes

- Add examples for selector-based, workload-based, and host-based connectors after aligning them with the supported platform matrix.
- Keep attached connectors as a connector variant, with namespace and binding behavior delegated to a later detailed page.
- Include status interpretation for matching listeners, selected pods, and readiness once the source references are normalized.
