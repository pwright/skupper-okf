---
title: Application Developers
type: SkupperPersona
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
persona_order: 1
coverage: Partial — concepts and a starter workflow exist
missing_target_count: 2
audience_message: >-
  Your application can use services that run outside its cluster. Skupper provides local connection endpoints for those services, so you can develop and deploy your application while its dependencies remain in environments managed by other teams.
tags:
  - skupper
  - personas
  - application-development
  - missing-targets
---

# Application Developers

> Your application can use services that run outside its cluster. Skupper provides local connection endpoints for those services, so you can develop and deploy your application while its dependencies remain in environments managed by other teams.

For this audience, Skupper turns a remote service relationship into a local connection endpoint. The application still owns its protocol behavior, authentication, timeouts, retries, and response to connection loss.

## Relevant existing pages

- [Connected Service Across Sites](../skupper-docs-landscape/first-connected-service.md) — the smallest end-to-end outcome.
- [Service Exposure](../skupper-docs-landscape/service-exposure.md) — how listeners, connectors, and routing keys work together.
- [Listener](../concepts/listener.md) — the local endpoint used by a consuming application.
- [Connector](../concepts/connector.md) — how the providing workload becomes reachable.
- [Connectivity Validation](../skupper-docs-landscape/first-validation.md) — validation from site readiness through an application request.

