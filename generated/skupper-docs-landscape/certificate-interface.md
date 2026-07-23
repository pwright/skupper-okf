---
type: DocumentationLandscapePage
title: "Certificate Interface"
id: certificate-interface
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/certificate-interface
tags:
  - skupper
  - docs-landscape
  - integrate
timestamp: 2026-07-23T21:45:00Z
---

# Certificate Interface

The certificate interface covers the TLS certificates and credential bundles Skupper uses for links, routers, listeners, connectors, and console access.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Operations Interfaces

## Sources

- [human/skupper-docs/input/refdog/topics/router-tls.md](../../human/skupper-docs/input/refdog/topics/router-tls.md) - Local source for router TLS.
- [human/skupper-docs/input/refdog/topics/application-tls.md](../../human/skupper-docs/input/refdog/topics/application-tls.md) - Local source for application TLS.
- [human/skupper-docs/input/refdog/topics/system-tls-credentials.md](../../human/skupper-docs/input/refdog/topics/system-tls-credentials.md) - Local source for system TLS credentials.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for console TLS configuration.
- [generated/skupper/skupper-crd-certificates-skupper-io.md](../skupper/skupper-crd-certificates-skupper-io.md) - Generated CRD source for Certificate resources.

## Website Links

- [Router TLS topic](https://skupperproject.github.io/refdog/topics/router-tls.html)
- [Application TLS topic](https://skupperproject.github.io/refdog/topics/application-tls.html)
- [System TLS credentials topic](https://skupperproject.github.io/refdog/topics/system-tls-credentials.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)

## Draft Notes

- Separate router link identity from application TLS and console TLS.
- Confirm current certificate resource behavior before documenting field-level operations.
- Include certificate replacement and trust-boundary notes only where source-backed.
