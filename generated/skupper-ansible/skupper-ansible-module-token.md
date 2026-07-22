---
type: GeneratedDocs
title: 'Skupper Ansible module: token'
id: skupper-ansible-module-token
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper-ansible.git
source_branch: main
source_commit: 632478a5245d1b71bd0eabb4b8e414f91c5b020b
source_paths:
- human/skupper-ansible/plugins/modules/token.py
generated_at: '2026-07-22T21:20:39Z'
generator: generate-ansible-docs.py
tags:
- skupper
- ansible
- module
- token
related:
- skupper-ansible-overview
- skupper-ansible-workflow-kubernetes
- skupper-ansible-workflow-non-kubernetes
- skupper-ansible-workflow-mixed-sites
decision:
  authoring:
  - ansible
  setupStep:
  - join-sites
  resource:
  - access-grant
  - access-token
  - link
  platform:
  - kubernetes
  - podman
  - docker
  - linux
  joinMethod:
  - access-grant-token
---


# Skupper Ansible module: token

Issue or retrieve access tokens and static links

## Description

Manages Skupper Access Tokens and static links Generates an AccessGrant and return a corresponding AccessToken (kubernetes platform only) Returns an AccessToken for an existing AccessGrant (kubernetes platform only) Retrieves a static Link based on provided subject alternative name or host (podman, docker and linux platforms)

## Options

| Option | Type | Default | Choices | Description |
| --- | --- | --- | --- | --- |
| `expiration_window` | str | 15m |  | Duration of the generated AccessGrant Sample values V(10m), V(2h) Only used when platform is V(kubernetes) and type is V(token) |
| `host` | str |  |  | Static link hostname Only used when platform is V(podman), V(docker), V(linux) |
| `name` | str |  |  | Name of the AccessGrant (to be generated or consumed) and AccessToken (kubernetes platform only) when using type V(token) Name of the Link and Certificate (to be generated or consumed) (kubernetes platform only) when using type V(link) Name of a RouterAccess (podman, docker or linux platforms) |
| `redemptions_allowed` | int | 1 |  | The number of claims the generated AccessGrant is valid for Only used when platform is V(kubernetes) and type is V(token) |
| `type` | str | token | token, link | Type of token to produce or consume Only meaningful when platform is V(kubernetes) Always set to V(link) when platform is V(podman), V(docker), V(linux) |

## Shared Options

This module extends the `skupper.v2.common_options` documentation fragment for common Skupper connection options such as `platform`, `namespace`, `kubeconfig`, and `context`.

## Requirements

- `python >= 3.9`
- `kubernetes >= 24.2.0`
- `PyYAML >= 3.11`

## Examples

```yaml
# Retrieve or issue an AccessToken (if my-grant does not exist or can be redeemed)
- name: Retrieve or issue my-grant AccessToken
  skupper.v2.token:
    name: my-grant
    platform: kubernetes
    namespace: west

# Retrieve or issue a Link (if my-link does not exist)
- name: Retrieve or create my-link Link
  skupper.v2.token:
    name: my-link
    type: link
    platform: kubernetes
    namespace: west

# Retrieving or generate a static Link
- name: Retrieve token
  skupper.v2.token:
    name: west-link
    type: link
    platform: kubernetes
    namespace: west

# Retrieving an accesstoken for any valid accessgrant
- name: Retrieve token
  skupper.v2.token:
    platform: kubernetes
    namespace: west

# Retrieving a Link for any existing site client certificate
- name: Retrieve Link
  skupper.v2.token:
    platform: kubernetes
    type: link
    namespace: west

# Retrieve a static Link for host my.nonkube.host
- name: Retrieve a static link
  skupper.v2.token:
    host: my.nonkube.host
    platform: podman
```

## Return Values

```yaml
token:
  description:
  - AccessToken resource (yaml)
  - Link and Secret (yaml)
  returned: success
  type: str
```

## Source

- `human/skupper-ansible/plugins/modules/token.py`
