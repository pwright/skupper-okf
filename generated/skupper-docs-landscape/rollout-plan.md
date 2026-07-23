---
type: DocumentationLandscapePage
title: "Rollout Plan"
id: rollout-plan
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rollout-plan
tags:
  - skupper
  - docs-landscape
  - plan
related:
  - target-topology
  - ownership-model
  - risk-assessment
timestamp: 2026-07-23T19:54:51Z
---

# Rollout Plan

Rollout Plan turns the target topology into a staged implementation path. It should identify the first sites and services to connect, validation checkpoints, ownership handoffs, and rollback or pause points before broader adoption.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Deployment Design

## Dependencies

- [Target Application Network Topology](./target-topology.md)
- [Operational Ownership](./ownership-model.md)
- [Rollout Risk Assessment](./risk-assessment.md)

## Sources

- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for implementation concerns after getting started, including linking strategies and validation checks.
- [Kubernetes CLI overview](../../human/skupper-docs/input/kube-cli/index.md): Local source for the basic create sites, link sites, and expose services workflow.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local procedure source for creating the first site resources.
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local procedure source for staged link creation and status checks.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local procedure source for adding services after sites are linked.

## Website Links

- [Skupper Kubernetes CLI overview](https://skupper.io/docs/kube-cli/index.html)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)

## Draft Notes

- Build the first rollout around one low-risk service and an observable validation path.
- Capture sequencing dependencies: platform readiness, site creation, link access, service exposure, validation, then expansion.
- Keep rollback guidance conservative until paired with migration and operations pages.
