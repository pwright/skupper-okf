---
type: DocumentationLandscapePage
title: "Traffic Cutover"
id: cutover
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cutover
tags:
  - skupper
  - docs-landscape
  - migrate
related:
  - parallel-run
  - rollback-path
timestamp: 2026-07-23T20:07:08Z
---

# Traffic Cutover

Traffic Cutover is the controlled switch from source connectivity to target connectivity for a migration wave. It should describe the chosen traffic mechanism, validation gate, and rollback decision point without assuming that Skupper orchestrates every application-level change.

## Appears in

- [Migrate to or Between Skupper Deployments](./migrate-skupper.md) / Migration Execution

## Dependencies

- [Parallel Run](./parallel-run.md)
- [Rollback Path](./rollback-path.md)

## Sources

- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md): Local source for traffic distribution, failover, and stateful-application caveats.
- [Routing key concept](../concepts/routing-key.md): Generated local source for listener/connector matching and service binding behavior.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for service exposure and status checks at cutover.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Local source for confirming site, link, connector, and listener status.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for traffic direction and validation checks.

## Website Links

- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)

## Draft Notes

- Define exactly what changes at cutover: routing key, listener, connector, application config, DNS, or another control.
- Include a stop/go validation gate immediately after the switch.
- For stateful applications, document external orchestration separately because local docs do not promise Skupper-managed stateful failover.
