---
type: DocumentationLandscapePage
title: "Availability Targets"
id: availability-targets
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/availability-targets
tags:
  - skupper
  - docs-landscape
  - plan
timestamp: 2026-07-23T19:54:51Z
---

# Availability Targets

Availability Targets define the level of continuity expected from the application network and the services carried over it. The local docs support high-availability site behavior, connection failover patterns, and the important limit that Skupper does not orchestrate stateful application failover.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Planning Inputs

## Sources

- [Network deployment concerns](../concepts/network-deployment-concerns.md): Primary generated local source for high availability sites, router restarts, node failure behavior, and capacity caveats.
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md): Local source for new TCP connection balancing, failover, link cost, and stateful failover limits.
- [Kubernetes site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for high availability site creation with the CLI.
- [Kubernetes site configuration with YAML](../../human/skupper-docs/input/kube-yaml/site-configuration.md): Local source candidate for HA site configuration as code.
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Local source for dynamic links and bidirectional application traffic.

## Website Links

- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Creating a high availability site with the CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Refdog link concept](https://skupperproject.github.io/refdog/concepts/link.html)

## Draft Notes

- Record target behavior for router restart, node failure, link loss, and backend service loss separately.
- Do not imply HA mode solves loss of network connectivity between sites.
- For stateful applications, document the external orchestration requirement rather than promising Skupper-managed failover.
