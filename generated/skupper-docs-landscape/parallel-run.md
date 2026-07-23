---
type: DocumentationLandscapePage
title: "Parallel Run"
id: parallel-run
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/parallel-run
tags:
  - skupper
  - docs-landscape
  - migrate
related:
  - migration-wave
  - dual-connectivity
timestamp: 2026-07-23T20:07:08Z
---

# Parallel Run

Parallel Run is the migration phase where source and target connectivity are both available long enough to validate the target before cutover. It should document which paths run in parallel, how traffic is selected or compared, and how the team avoids confusing duplicate service definitions.

## Appears in

- [Migrate to or Between Skupper Deployments](./migrate-skupper.md) / Migration Execution

## Dependencies

- [Migration Waves](./migration-wave.md)
- [Dual Connectivity Plan](./dual-connectivity.md)

## Sources

- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md): Local source for weighted and priority strategies plus link cost caveats.
- [Routing key concept](../concepts/routing-key.md): Generated local source for routing-key matching, many-to-many relationships, and service binding status.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for connector/listener status checks during parallel operation.
- [Network Observer API concept](../concepts/network-observer-api.md): Generated local source for observing runtime state and traffic flows.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local source for sample application paths to validate in parallel.

## Website Links

- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Refdog routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)

## Draft Notes

- Prefer explicit routing keys or multi-key listener configuration for test traffic rather than relying on implicit behavior.
- Record whether the parallel path carries production, shadow, or test-only traffic.
- Avoid using link cost for per-service migration control because it affects all services on a link.
