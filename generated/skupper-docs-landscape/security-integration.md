---
type: DocumentationLandscapePage
title: "Security Tooling Integration"
id: security-integration
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/security-integration
tags:
  - skupper
  - docs-landscape
  - integrate
related:
  - certificate-interface
  - policy-interface
timestamp: 2026-07-23T21:45:00Z
---

# Security Tooling Integration

Security tooling integration connects Skupper certificate, token, access, and policy surfaces with platform controls and operational review.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Integration Patterns

## Dependencies

- [Certificate Interface](./certificate-interface.md)
- [Policy Interface](./policy-interface.md)

## Sources

- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md) - Local source for router TLS behavior.
- [human/skupper-docs/input/refdog/topics/application-tls.md](../../human/skupper-docs/input/refdog/topics/application-tls.md) - Local source for application TLS topics.
- [human/skupper-docs/input/refdog/topics/system-tls-credentials.md](../../human/skupper-docs/input/refdog/topics/system-tls-credentials.md) - Local source for system TLS credentials.
- [human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml) - Local CRD candidate for policy controls.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for mutual TLS, tokens, and custom certificates.

## Website Links

- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Application TLS topic](https://skupperproject.github.io/refdog/topics/application-tls.html)
- [System TLS credentials topic](https://skupperproject.github.io/refdog/topics/system-tls-credentials.html)
- [AccessToken resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)

## Draft Notes

- Keep certificate lifecycle, token handling, and policy enforcement as separate integration concerns.
- Validate cluster policy behavior from primary sources before documenting a workflow.
- Include redaction and secret-handling notes for logs and automation output.
