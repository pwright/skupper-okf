---
type: DocumentationLandscapePage
title: "Service Priorities"
id: service-priorities
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-priorities
tags:
  - skupper
  - docs-landscape
  - optimize
timestamp: 2026-07-23T21:00:00Z
---

# Service Priorities

Service priorities describe which application services need preferred routing, failover behavior, or weighted distribution during optimization.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Validation Inputs

## Sources

- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md) - Local source for service-level load balancing and failover controls.
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md) - MultiKeyListener resource reference.
- [human/skupper-docs/input/refdog/concepts/multi-key-listener.md](../../human/skupper-docs/input/refdog/concepts/multi-key-listener.md) - Concept source for multi-key listener behavior.
- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Generated source for routing-key matching.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Local source for declarative service exposure resources.

## Website Links

- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Multi-key listener concept](https://skupperproject.github.io/refdog/concepts/multi-key-listener.html)
- [MultiKeyListener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)

## Draft Notes

- Document priority as business and reliability intent before choosing a Skupper configuration.
- Use routing keys to make the relationship between service intent and traffic distribution explicit.
- Add examples for primary/backup and weighted split scenarios after confirming the exact resource syntax.
