---
type: DocumentationLandscapePage
title: "Load Tests"
id: load-tests
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/load-tests
tags:
  - skupper
  - docs-landscape
  - optimize
timestamp: 2026-07-23T21:00:00Z
---

# Load Tests

Load tests apply controlled application traffic through Skupper so tuning changes can be evaluated against repeatable evidence rather than anecdotal symptoms.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Validation Inputs

## Sources

- [generated/workflows/skupper-examples.md](../workflows/skupper-examples.md) - Generated source for example applications and validation workflows.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for measuring connections, services, and flows during tests.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console time-series and traffic views.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local source for capturing symptoms and diagnostics.
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md) - Local source for validating load balancing and failover choices.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Skupper examples repository](https://github.com/skupperproject/skupper-example-hello-world)

## Draft Notes

- Keep load-test procedures workload-specific and record topology, service definitions, and traffic generator settings.
- Include a warm-up period and a steady-state measurement window when documenting future tests.
- Do not infer benchmark numbers from examples; examples are useful for shape and validation flow.
