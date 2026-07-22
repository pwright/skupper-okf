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
  - access-grant
  - access-token
  joinMethod:
  - access-grant-token
---

# Skupper Ansible Kubernetes workflow

The Kubernetes Ansible path applies Skupper resource YAML with `skupper.v2.resource`, issues or retrieves an AccessToken with `skupper.v2.token`, and applies the token on another site with `skupper.v2.resource`.

## Flow

```text
resource module -> Site/Listener/Connector YAML
token module    -> AccessGrant/AccessToken
resource module -> apply token on peer site
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
        kubeconfig: "{{ kubeconfig }}"
        namespace: "{{ namespace }}"
      register: accesstoken

- hosts: east
  tasks:
    - skupper.v2.resource:
        def: "{{ hostvars['west']['accesstoken']['token'] }}"
        kubeconfig: "{{ kubeconfig }}"
        namespace: "{{ namespace }}"
```

## Source

- `human/skupper-ansible/README.md`
- `human/skupper-ansible/plugins/modules/resource.py`
- `human/skupper-ansible/plugins/modules/token.py`
