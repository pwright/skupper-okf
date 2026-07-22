---
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper-ansible.git
source_branch: main
source_commit: 632478a5245d1b71bd0eabb4b8e414f91c5b020b
generated_at: '2026-07-22T21:09:50Z'
generator: generate-ansible-docs.py
tags:
- skupper
- ansible
type: Concept
title: Skupper Ansible collection
id: skupper-ansible-overview
source_paths:
- human/skupper-ansible/README.md
- human/skupper-ansible/plugins/doc_fragments/common_options.py
related:
- skupper-ansible-module-resource
- skupper-ansible-module-token
- skupper-ansible-module-system
- skupper-ansible-module-controller
decision:
  authoring:
  - ansible
  platform:
  - kubernetes
  - podman
  - docker
  - linux
---

# Skupper Ansible collection

The Skupper Ansible collection provides `skupper.v2` modules for managing Skupper resources, access tokens, links, non-Kubernetes site lifecycle actions, and the system-site controller from Ansible playbooks.

Use this source when the setup path is Ansible-driven rather than direct CLI commands or hand-applied YAML. The collection still operates on the same Skupper concepts: sites, listeners, connectors, links, access grants, and access tokens.

## Module Map

| Module | Primary use |
| --- | --- |
| `skupper.v2.resource` | Apply, update, remove, or redeem Skupper resource YAML definitions. |
| `skupper.v2.token` | Issue or retrieve AccessToken resources and static links. |
| `skupper.v2.system` | Start, reload, stop, or bundle non-Kubernetes site definitions. |
| `skupper.v2.controller` | Install or uninstall the system-site controller for Podman or Docker. |

## Shared Options

Most modules use common options for `platform`, `namespace`, `kubeconfig`, and `context`. Kubernetes is the default platform where applicable. Non-Kubernetes workflows use `podman`, `docker`, or `linux`.

## Source

- `human/skupper-ansible/README.md`
- `human/skupper-ansible/plugins/doc_fragments/common_options.py`
