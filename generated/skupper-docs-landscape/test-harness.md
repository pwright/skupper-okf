---
type: DocumentationLandscapePage
title: "Integration Test Harness"
id: test-harness
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/test-harness
tags:
  - skupper
  - docs-landscape
  - develop
related:
  - examples
timestamp: 2026-07-23T21:30:00Z
---

# Integration Test Harness

An integration test harness provisions a representative Skupper environment, runs application connectivity checks, and collects evidence that the desired resources are working.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Developer Foundations

## Dependencies

- [Reference Examples](./examples.md)

## Sources

- [generated/workflows/skupper-examples.md](../workflows/skupper-examples.md) - Generated source for example application flows.
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - Local source for site setup and status checks.
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - Local source for linking sites.
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md) - Local source for exposing and validating services.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local source for diagnostic checks after test failures.

## Website Links

- [Site configuration with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper examples](https://github.com/skupperproject/skupper-example-hello-world)

## Draft Notes

- Include setup, exercise, assertion, diagnostics, and teardown phases.
- Use examples as starting points but keep test assertions tied to the local application under test.
- Capture site, link, listener, connector, and application reachability evidence on failure.
