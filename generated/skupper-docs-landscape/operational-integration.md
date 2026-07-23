---
type: DocumentationLandscapePage
title: "Operational Toolchain Integration"
id: operational-integration
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/operational-integration
tags:
  - skupper
  - docs-landscape
  - integrate
related:
  - observability-integration
  - security-integration
  - delivery-integration
timestamp: 2026-07-23T21:45:00Z
---

# Operational Toolchain Integration

Operational toolchain integration connects Skupper with monitoring, logging, security, and delivery systems that operators already use.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Integration Outcomes

## Dependencies

- [Observability Integration](./observability-integration.md)
- [Security Tooling Integration](./security-integration.md)
- [CI/CD Integration](./delivery-integration.md)

## Sources

- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer metrics, TLS, auth, logging, and resource settings.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console APIs, metrics queries, and errors.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer API monitoring use cases.
- [generated/skupper-ansible/skupper-ansible-overview.md](../skupper-ansible/skupper-ansible-overview.md) - Generated source for automation integration.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local source for diagnostic evidence collection.

## Website Links

- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Treat this as an integration inventory page, not a replacement for observability or security details.
- Document boundaries between Skupper-provided interfaces and platform-owned tooling.
- Add examples only after identifying a stable monitoring or delivery stack target.
