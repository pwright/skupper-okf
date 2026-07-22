# Prompt: extract OKF from human source docs

Use `human/<repo-name>/` as read-only source material. Create small OKF-style Markdown pages under `generated/`.

Rules:

- Preserve source provenance in YAML front matter.
- Prefer one concept, command, resource, or workflow per file.
- Do not rewrite the original documentation as marketing copy.
- Do not invent source paths.
- Always include the repo-name segment in source paths, for example `human/skupper-docs/input/index.md`.
- Mark all outputs as `status: generated` and `reviewed: false`.
- Add `decision` frontmatter only when the source clearly maps to a Skupper setup decision, platform, resource, or authoring mode. Omit unclear fields rather than guessing.

Suggested front matter:

```yaml
type: Concept
title: <title>
id: skupper-concept-<slug>
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper-docs.git
source_branch: main
source_commit: <commit from sources/skupper-docs.md>
source_paths:
  - human/skupper-docs/<path>
tags: []
related: []
# Optional Decision Lens metadata. Include only fields supported by the source.
decision:
  platform:
    - kubernetes
  setupStep:
    - configure-connector
  resource:
    - connector
```

## Decision Lens metadata

Use Decision Lens metadata to make generated pages ready for runtime soft filtering in the Quartz wiki. This is not access control; it is a browsing and search aid.

Allowed `decision.platform` values:

- `kubernetes`
- `openshift`
- `podman`
- `docker`
- `linux`
- `local-system`

Allowed `decision.setupStep` values:

- `identify-sites`
- `classify-workloads`
- `define-routing-key`
- `configure-listener`
- `configure-connector`
- `decide-link-access`
- `join-sites`
- `validate`

Optional facets when explicit in the source:

- `decision.workloadRole`: `client`, `server`, `both`
- `decision.resource`: `site`, `listener`, `connector`, `link`, `access-grant`, `access-token`, `attached-connector`, `attached-connector-binding`
- `decision.authoring`: `cli`, `yaml`, `ansible`
- `decision.linkAccess`: `openshift-route`, `loadbalancer`, `default`, `none`
- `decision.joinMethod`: `cli-token`, `access-grant-token`

Map source content to the Skupper v2 setup journey:

1. Identify sites.
2. Classify workloads per site.
3. Define the routing key.
4. Configure client access with a Listener.
5. Configure server binding with a Connector.
6. Decide link access.
7. Join sites.
8. Validate readiness and client connectivity.

Examples:

```yaml
decision:
  setupStep:
    - decide-link-access
  platform:
    - kubernetes
    - openshift
  linkAccess:
    - openshift-route
    - loadbalancer
```

```yaml
decision:
  setupStep:
    - join-sites
  joinMethod:
    - cli-token
    - access-grant-token
```

```yaml
decision:
  setupStep:
    - configure-connector
  resource:
    - connector
  workloadRole:
    - server
```

Output directories:

```text
generated/concepts/
generated/resources/
generated/workflows/
generated/architecture/
```
