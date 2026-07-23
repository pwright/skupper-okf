---
type: DocumentationLandscapePage
title: "Validation Constraints"
id: constraints
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/constraints
tags:
  - skupper
  - docs-landscape
  - reference
timestamp: 2026-07-23T22:15:00Z
---

# Validation Constraints

Validation constraints are the field requirements, option combinations, platform limits, and status rules that Skupper commands and resources enforce.

## Appears in

- [Skupper Reference](./skupper-reference.md) / Defaults and Diagnostics

## Sources

- [generated/skupper/skupper-crd-sites-skupper-io.md](../skupper/skupper-crd-sites-skupper-io.md) - Generated Site CRD constraints.
- [generated/skupper/skupper-crd-listeners-skupper-io.md](../skupper/skupper-crd-listeners-skupper-io.md) - Generated Listener CRD constraints.
- [generated/skupper/skupper-crd-connectors-skupper-io.md](../skupper/skupper-crd-connectors-skupper-io.md) - Generated Connector CRD constraints.
- [human/skupper-docs/refdog/scripts/validate_crds_vs_yaml.py](../../human/skupper-docs/refdog/scripts/validate_crds_vs_yaml.py) - Local validation utility source.
- [human/skupper-docs/refdog/scripts/validate_yaml_vs_clidoc.py](../../human/skupper-docs/refdog/scripts/validate_yaml_vs_clidoc.py) - Local validation utility source.

## Website Links

- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

## Draft Notes

- Build constraint summaries from CRD schemas and refdog validation scripts.
- Keep required fields, enum values, mutual exclusions, and platform-specific requirements separate.
- Add examples only after verifying the exact validation message source.
