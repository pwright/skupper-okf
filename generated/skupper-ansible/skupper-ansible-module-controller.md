---
type: GeneratedDocs
title: 'Skupper Ansible module: controller'
id: skupper-ansible-module-controller
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper-ansible.git
source_branch: main
source_commit: 632478a5245d1b71bd0eabb4b8e414f91c5b020b
source_paths:
- human/skupper-ansible/plugins/modules/controller.py
generated_at: '2026-07-22T21:20:39Z'
generator: generate-ansible-docs.py
tags:
- skupper
- ansible
- module
- controller
related:
- skupper-ansible-overview
- skupper-ansible-workflow-kubernetes
- skupper-ansible-workflow-non-kubernetes
- skupper-ansible-workflow-mixed-sites
decision:
  authoring:
  - ansible
  setupStep:
  - identify-sites
  - validate
  platform:
  - podman
  - docker
---


# Skupper Ansible module: controller

Manages the lifecycle of the skupper-controller for system sites

## Description

Manages the lifecycle of the skupper-controller. Prepares the environment and runs the skupper-controller for system sites Runs with podman (default) or docker engines With podman-docker (Docker CLI using Podman), use the podman platform; the docker platform requires a real Docker daemon.

## Options

| Option | Type | Default | Choices | Description |
| --- | --- | --- | --- | --- |
| `action` | str | install | install, uninstall | V(install) - Prepares the environment and runs the skupper-controller V(uninstall) - Adjusts the local environment and removes the skupper-controller |
| `image` | str | quay.io/skupper/system-controller:v2-dev |  | The controller-image to use |
| `platform` | str | podman | podman, docker | The platform used to run the controller for system sites |
| `reload_type` | str | manual | auto, manual | The type of reload of input custom resources |

## Requirements

- `python >= 3.9`
- `PyYAML >= 3.11`

## Examples

```yaml
# Installs the skupper-controller using podman
- name: Installs the skupper-controller using podman
  skupper.v2.controller:
    action: install
    platform: podman
    reload_type: auto

# Uninstalls the skupper-controller
- name: Uninstalls the skupper-controller
  skupper.v2.controller:
    action: uninstall
```

## Source

- `human/skupper-ansible/plugins/modules/controller.py`
