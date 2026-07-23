---
type: DocumentationLandscapePage
title: "Routing Mode"
id: routing-mode
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/routing-mode
tags:
  - skupper
  - docs-landscape
  - configure
related: []
timestamp: 2026-07-23T20:17:03Z
---

# Routing Mode

Routing mode describes the service-level choice for how traffic should be distributed across matching backends, including simple routing-key matching and multi-key listener strategies.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Inputs

## Sources

- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md) - Source guidance that prefers multi-key listeners for per-service load balancing and failover.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - MultiKeyListener YAML examples.
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md) - MultiKeyListener resource reference.
- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Routing key and MultiKeyListener behavior.
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md) - Link cost details and caveats.

## Website Links

- [Load balancing overview](https://skupper.io/docs/overview/load-balancing.html)
- [Multi-key listener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)

## Draft Notes

- Cover weighted and priority multi-key listener strategies with examples sourced from the YAML docs.
- Keep link cost in a caveats section because the source docs position it as broader link-level behavior, not the preferred per-service mechanism.
- Add validation guidance using matching listener and connector status fields.
