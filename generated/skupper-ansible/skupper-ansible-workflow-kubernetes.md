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
title: Skupper Ansible Kubernetes workflow
id: skupper-ansible-workflow-kubernetes
source_paths:
- human/skupper-ansible/README.md
- human/skupper-ansible/plugins/modules/resource.py
- human/skupper-ansible/plugins/modules/token.py
related:
- skupper-concept-listener
- skupper-concept-connector
- skupper-ansible-module-resource
- skupper-ansible-module-token
- skupper-ansible-workflow-mixed-sites
decision:
  authoring:
  - ansible
  platform:
  - kubernetes
  setupStep:
  - configure-listener
  - configure-connector
  - join-sites
  - validate
  resource:
  - site
  - listener
  - connector
  - link
---

# Skupper Ansible Kubernetes workflow

The Kubernetes Ansible path applies Skupper resource YAML with `skupper.v2.resource`, retrieves a Link resource bundle with `skupper.v2.token`, and applies that bundle on the peer site with `skupper.v2.resource`.

## Flow

```text
resource module -> Site/Listener/Connector YAML
token module    -> Link/Secret YAML
resource module -> apply Link/Secret on peer site
```

## Playbook Shape

```yaml
- hosts: all
  tasks:
    - skupper.v2.resource:
        path: "{{ resources_path }}"
        kubeconfig: "{{ kubeconfig }}"
        namespace: "{{ namespace }}"

- hosts: west
  tasks:
    - skupper.v2.token:
        name: west
        type: link
        kubeconfig: "{{ kubeconfig }}"
        namespace: "{{ namespace }}"
      register: west_link

- hosts: east
  tasks:
    - skupper.v2.resource:
        def: "{{ hostvars['west']['west_link']['token'] }}"
        kubeconfig: "{{ kubeconfig }}"
        namespace: "{{ namespace }}"
```

## Source

- `human/skupper-ansible/README.md`
- `human/skupper-ansible/plugins/modules/resource.py`
- `human/skupper-ansible/plugins/modules/token.py`
