---
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper-ansible.git
source_branch: main
source_commit: 632478a5245d1b71bd0eabb4b8e414f91c5b020b
generated_at: '2026-07-22T21:20:39Z'
generator: generate-ansible-docs.py
tags:
- skupper
- ansible
type: Workflow
title: Skupper Ansible mixed Kubernetes and system workflow
id: skupper-ansible-workflow-mixed-sites
source_paths:
- human/skupper-ansible/README.md
- human/skupper-ansible/plugins/modules/resource.py
- human/skupper-ansible/plugins/modules/token.py
- human/skupper-ansible/plugins/modules/system.py
related:
- skupper-ansible-module-resource
- skupper-ansible-module-token
- skupper-ansible-module-system
- skupper-ansible-workflow-kubernetes
- skupper-ansible-workflow-non-kubernetes
decision:
  authoring:
  - ansible
  platform:
  - kubernetes
  - podman
  - docker
  - linux
  setupStep:
  - identify-sites
  - decide-link-access
  - join-sites
  - validate
  resource:
  - site
  - listener
  - connector
  - link
---

# Skupper Ansible mixed Kubernetes and system workflow

Use Link resources when an Ansible playbook joins a Kubernetes site to a local system site. In these examples, `podman` represents the local system platform; use `docker` or `linux` when that is the actual system platform.

## West Kubernetes, East Local System

The Kubernetes site in `west` produces a Link resource bundle. The local system site in `east` applies that bundle as resource YAML.

```yaml
- hosts: west
  tasks:
    - skupper.v2.resource:
        path: "{{ west_resources_path }}"
        platform: kubernetes
        namespace: west
        kubeconfig: "{{ kubeconfig }}"

    - skupper.v2.token:
        name: west
        type: link
        platform: kubernetes
        namespace: west
        kubeconfig: "{{ kubeconfig }}"
      register: west_link

- hosts: east
  tasks:
    - skupper.v2.resource:
        path: "{{ east_resources_path }}"
        platform: podman
        namespace: east

    - skupper.v2.resource:
        def: "{{ hostvars['west']['west_link']['token'] }}"
        platform: podman
        namespace: east

    - skupper.v2.system:
        platform: podman
        namespace: east
```

## West Local System, East Kubernetes

The local system site in `west` starts first and returns static Link resources. The Kubernetes site in `east` applies the selected Link resource bundle.

```yaml
- hosts: west
  tasks:
    - skupper.v2.resource:
        path: "{{ west_resources_path }}"
        platform: podman
        namespace: west

    - skupper.v2.system:
        platform: podman
        namespace: west
      register: west_system

- hosts: east
  tasks:
    - skupper.v2.resource:
        path: "{{ east_resources_path }}"
        platform: kubernetes
        namespace: east
        kubeconfig: "{{ kubeconfig }}"

    - skupper.v2.resource:
        def: "{{ hostvars['west']['west_system']['links']['0.0.0.0'] }}"
        platform: kubernetes
        namespace: east
        kubeconfig: "{{ kubeconfig }}"
```

## Notes

- The Link resource bundle is applied with `skupper.v2.resource`; the playbook does not redeem an access token on the peer site.
- For system sites, `skupper.v2.system` starts or reloads the local namespace after resource files are present.
- For Kubernetes sites, the Skupper controller reconciles the applied Link and Secret resources.

## Source

- `human/skupper-ansible/README.md`
- `human/skupper-ansible/plugins/modules/resource.py`
- `human/skupper-ansible/plugins/modules/token.py`
- `human/skupper-ansible/plugins/modules/system.py`
