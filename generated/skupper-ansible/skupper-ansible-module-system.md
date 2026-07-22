---
type: GeneratedDocs
title: 'Skupper Ansible module: system'
id: skupper-ansible-module-system
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper-ansible.git
source_branch: main
source_commit: 632478a5245d1b71bd0eabb4b8e414f91c5b020b
source_paths:
- human/skupper-ansible/plugins/modules/system.py
generated_at: '2026-07-22T21:09:50Z'
generator: generate-ansible-docs.py
tags:
- skupper
- ansible
- module
- system
related:
- skupper-ansible-overview
- skupper-ansible-workflow-kubernetes
- skupper-ansible-workflow-non-kubernetes
decision:
  authoring:
  - ansible
  setupStep:
  - identify-sites
  - decide-link-access
  - validate
  platform:
  - podman
  - docker
  - linux
---


# Skupper Ansible module: system

Manages the lifecycle of non-kube namespaces

## Description

Manages the lifecycle of non-kube namespaces. Executes the provided action for a non-kube site definition on a given namespace It can be used to start, reload and stop a namespace definition It has the ability to produce site bundles (tarball or a self-extracting shell-script) Runs with podman (default) or docker binaries Only valid for platforms "podman", "docker" and "linux" When using podman-docker (Docker CLI that uses Podman underneath), use the podman platform, not docker. The docker platform expects a real Docker daemon and a system docker group; podman-docker does not satisfy these and will fail.

## Options

| Option | Type | Default | Choices | Description |
| --- | --- | --- | --- | --- |
| `action` | str | start | start, reload, stop, shell-script, tarball | The action to perform against a given namespace definition V(start) - a new site is initialized and started (no-op if namespace is already initialized) V(reload) - a site is created or re-initialized (Certificate Authorities are preserved) V(stop) - stops and removes a site definition V(shell-script) - generates a self-extracting bundle V(tarball) - generates a tarball bundle |
| `engine` | str | podman | podman, docker | The container engine used to manage a namespace or produce a bundle The default value is podman, but if platform is set to docker, it will use docker as the engine as well It is also used when the platform is set to systemd or when action is bundle or tarball (otherwise the platform value is used) |
| `image` | str | quay.io/skupper/cli:v2-dev |  | The image used to initialize your site or bundle |

## Shared Options

This module extends the `skupper.v2.common_options` documentation fragment for common Skupper connection options such as `platform`, `namespace`, `kubeconfig`, and `context`.

## Requirements

- `python >= 3.9`
- `PyYAML >= 3.11`

## Examples

```yaml
# Initializes the default namespace based on existing resources
- name: Initialize the default namespace using podman
  skupper.v2.system:
    action: start

# Initializes the west namespace using docker
- name: Initialize the west namespace using docker
  skupper.v2.system:
    platform: docker
    namespace: west

# Reloads the definitions for the west namespace
- name: Reloads the west namespace definition
  skupper.v2.system:
    action: reload
    namespace: west

# Removes a site definition from the west namespace
- name: Removes the west namespace
  skupper.v2.system:
    action: stop
    namespace: west

# Produces a self-extracting shell-script bundle based on the default namespace definitions
- name: Generate a self-extracting shell-script bundle based on the default namespace definitions
  skupper.v2.system:
    action: shell-script
    register: result

# Produces a tarball bundle based on the west namespace definitions
- name: Generate a tarball bundle based on west namespace definitions
  skupper.v2.system:
    action: tarball
    namespace: west
    register: result
```

## Return Values

```yaml
path:
    description:
        - Path to the generated namespace or to a produced site bundle
    returned: success
    type: str
bundle:
    description:
        - Base 64 encoded content of the generated shell-script or tarball bundle
        - Only populated when action is shell-script or tarball
    returned: success
    type: str
links:
    description:
        - Static links generated for non-kube sites with link access enabled (RouterAccess provided)
        - Dictionary keys are the target hostname or ip of the link
        - Each value has a valid link that can be applied to another site using the M(skupper.v2.resource) module
    returned: when platform in ('podman', 'docker', 'linux') and link access enabled (RouterAccess provided)
    type: dict
    sample: {'my.host': '---\napiVersion: skupper.io/v2alpha1...'}
```

## Source

- `human/skupper-ansible/plugins/modules/system.py`
