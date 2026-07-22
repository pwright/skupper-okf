---
type: GeneratedDocs
title: 'Skupper Ansible module: resource'
id: skupper-ansible-module-resource
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper-ansible.git
source_branch: main
source_commit: 632478a5245d1b71bd0eabb4b8e414f91c5b020b
source_paths:
- human/skupper-ansible/plugins/modules/resource.py
generated_at: '2026-07-22T21:20:39Z'
generator: generate-ansible-docs.py
tags:
- skupper
- ansible
- module
- resource
related:
- skupper-ansible-overview
- skupper-ansible-workflow-kubernetes
- skupper-ansible-workflow-non-kubernetes
- skupper-ansible-workflow-mixed-sites
decision:
  authoring:
  - ansible
  setupStep:
  - configure-listener
  - configure-connector
  - join-sites
  resource:
  - site
  - listener
  - connector
  - link
  - access-token
  platform:
  - kubernetes
  - podman
  - docker
  - linux
---


# Skupper Ansible module: resource

Place skupper resources (yaml) in the provided namespace

## Description

Place skupper resources (yaml) in the provided namespace. If platform is kubernetes (default) the resources are applied to the respective namespace. In case a different platform is used, the resources will be placed into the correct location for the namespace on the file system.

## Options

| Option | Type | Default | Choices | Description |
| --- | --- | --- | --- | --- |
| `def` | str |  |  | YAML representation of a custom resource. It can contain multiple YAML documents. |
| `path` | str |  |  | Path where resources are located (yaml and yml files). Path can be a directory, a file or an http URL. If remote is true (default is V(false)), the resources will not be copied from the control node. URLs are always fetch from the inventory host. Mutually exclusive with def |
| `redeem` | bool | False |  | For non-kubernetes platforms (for example V(podman), V(docker), or V(linux)), redeem C(AccessToken) documents without keeping them in the namespace; only Secret and Link are applied. Other documents in the same definition are applied first. With C(spec.url) and C(spec.code), uses HTTP (as C(skupper token redeem)). When V(platform) is V(kubernetes), this option is ignored and a warning is issued; the Skupper V2 controller on Kubernetes already handles AccessToken resources. |
| `remote` | bool | False |  | Determines if the resources are located at the inventory host instead of the control node. |
| `state` | str | present | present, latest, absent | V(present) means that if the resource does not exist, it will be created. If it exists, no change is made. V(latest) means that if the resource does not exist it will be created or updated with the latest provided definition. V(absent) means that the resource will be removed. |

## Shared Options

This module extends the `skupper.v2.common_options` documentation fragment for common Skupper connection options such as `platform`, `namespace`, `kubeconfig`, and `context`.

## Requirements

- `python >= 3.9`
- `kubernetes >= 24.2.0`
- `PyYAML >= 3.11`

## Examples

```yaml
# Applying resources to a kubernetes cluster
- name: Apply Skupper Resources
  skupper.v2.resource:
    path: /home/user/west/crs
    platform: kubernetes
    namespace: west

# Applying remote resources to a kubernetes cluster
- name: Apply Skupper Resources
  skupper.v2.resource:
    path: /remote/home/user/west/crs
    remote: true
    platform: kubernetes
    namespace: west

# Applying resources to a non-kube namespace
- name: Apply Skupper Resources
  skupper.v2.resource:
    path: /home/user/west/crs
    platform: podman
    namespace: west

# Define a single resource
- name: Define resources for west site
  skupper.v2.resource:
    namespace: west
    def: |
      ---
      apiVersion: skupper.io/v2alpha1
      kind: Site
      metadata:
        name: west
      spec:
        linkAccess: default
      ---
      apiVersion: skupper.io/v2alpha1
      kind: Listener
      metadata:
        name: backend
      spec:
        host: backend
        port: 8080
        routingKey: backend

- name: Redeem access token on a non-kubernetes site (apply Secret/Link only)
  skupper.v2.resource:
    namespace: east
    platform: podman
    def: "{{ access_token_yaml }}"
    redeem: true
  register: out
```

## Return Values

```yaml
redeemed_links:
  description: >
    List of YAML strings per redeemed token when C(redeem=true) on a non-kubernetes
    platform. Each string contains all Secret documents from the redeem response, then
    all Link documents (each group in server response order).
  type: list
  returned: when redeem is used on non-kubernetes and AccessToken documents were present
redeem_failures:
  description: >
    List of dicts C(name), C(msg) for HTTP redemption failures on non-kubernetes. The
    module does not fail; warnings are issued so a repeat run can stay idempotent (for
    example unchanged with a warning).
  type: list
  returned: when one or more AccessToken redemptions failed
```

## Source

- `human/skupper-ansible/plugins/modules/resource.py`
