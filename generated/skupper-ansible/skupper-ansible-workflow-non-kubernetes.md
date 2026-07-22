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
title: Skupper Ansible non-Kubernetes workflow
id: skupper-ansible-workflow-non-kubernetes
source_paths:
- human/skupper-ansible/README.md
- human/skupper-ansible/plugins/modules/resource.py
- human/skupper-ansible/plugins/modules/system.py
- human/skupper-ansible/plugins/modules/controller.py
related:
- skupper-ansible-module-resource
- skupper-ansible-module-system
- skupper-ansible-module-controller
- skupper-ansible-overview
- skupper-ansible-workflow-mixed-sites
decision:
  authoring:
  - ansible
  platform:
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

# Skupper Ansible non-Kubernetes workflow

For Podman, Docker, and Linux sites, the Ansible collection separates resource placement from lifecycle actions. Use `skupper.v2.resource` to place resource YAML in the namespace definition, then use `skupper.v2.system` to start, reload, stop, or bundle the site.

## Flow

```text
resource module -> namespace resource files
system module   -> start/reload/stop site
token module    -> static Link when link access is enabled
```

## Notes

- `skupper.v2.system` is only valid for non-Kubernetes platforms.
- Podman is the default engine for system-site lifecycle actions.
- Docker mode expects a real Docker daemon, not `podman-docker`.
- `skupper.v2.controller` manages the controller container for system sites.

## Source

- `human/skupper-ansible/README.md`
- `human/skupper-ansible/plugins/modules/resource.py`
- `human/skupper-ansible/plugins/modules/system.py`
- `human/skupper-ansible/plugins/modules/controller.py`
