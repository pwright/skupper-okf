---
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper-ansible.git
source_branch: main
generated_at: '2026-08-11T00:00:00Z'
generator: claude-code
tags:
- skupper
- ansible
- examples
- testing
type: Reference
title: Skupper Ansible Examples
id: skupper-ansible-examples
related:
- skupper-ansible-overview
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

# Skupper Ansible Examples

This document provides a comprehensive overview of Ansible examples and end-to-end test scenarios available in the Skupper ecosystem. These examples demonstrate how to use the `skupper.v2` Ansible collection to automate Skupper deployments, establish site connectivity, and manage service networks across Kubernetes and non-Kubernetes platforms.

## Example Categories

### Production Examples

Located in `scripts/skewer-yamls/` and referenced documentation.

#### Hello World with Ansible

**File**: `skupper-example-ansible.yaml`

A complete walkthrough demonstrating frontend/backend deployment across two Kubernetes clusters using Ansible automation.

**What it demonstrates**:
- Installing the `skupper.v2` Ansible collection
- Using inventory files to manage multiple sites
- Applying Skupper resources with `skupper.v2.resource` module
- Generating and redeeming access tokens with `skupper.v2.token` module
- Establishing cross-cluster connectivity
- Teardown and cleanup automation

**Key Ansible modules used**:
- `skupper.v2.resource` - Apply Site, Listener, Connector resources
- `skupper.v2.token` - Issue AccessToken for site linking

**Architecture**:
- **West site**: Frontend application + Skupper Site with Listener
- **East site**: Backend application + Skupper Site with Connector
- **Link**: AccessGrant from west redeemed by east

**Inventory structure**:
```yaml
all:
  vars:
    ansible_connection: local
  hosts:
    west:
      kubeconfig: "{{ inventory_dir }}/kubeconfigs/west"
      namespace: west
      resources_path: "{{ playbook_dir }}/kubernetes/west.yaml"
    east:
      kubeconfig: "{{ inventory_dir }}/kubeconfigs/east"
      namespace: east
      resources_path: "{{ playbook_dir }}/kubernetes/east.yaml"
```

**Playbook pattern** (setup.yml):
```yaml
# Apply resources to all sites
- hosts: all
  tasks:
    - name: Apply site resources
      skupper.v2.resource:
        path: "{{ resources_path }}"
        kubeconfig: "{{ kubeconfig }}"
        namespace: "{{ namespace }}"

# Generate token from one site
- hosts: west
  tasks:
    - name: Create a token to the west site
      skupper.v2.token:
        name: "west"
        kubeconfig: "{{ kubeconfig }}"
        namespace: "{{ namespace }}"
      register: accesstoken

# Redeem token at another site
- hosts: east
  tasks:
    - name: Link east site to west
      skupper.v2.resource:
        def: "{{ hostvars['west']['accesstoken']['token'] }}"
        kubeconfig: "{{ kubeconfig }}"
        namespace: "{{ namespace }}"
```

---

### End-to-End Test Scenarios

Located in `human/skupper/tests/e2e/scenarios/`. These are comprehensive test playbooks that demonstrate various Skupper features and use cases.

#### 1. Hello World Test

**Directory**: `scenarios/hello-world/`

**Purpose**: Basic Skupper connectivity test between two Kubernetes clusters.

**Resources deployed**:
- **West cluster**: Frontend application, Site, Listener for backend service
- **East cluster**: Backend application, Site, Connector to backend

**Skupper resources**:
```yaml
# west/site.yml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: west
spec:
  linkAccess: default

# west/listener.yml
apiVersion: skupper.io/v2alpha1
kind: Listener
metadata:
  name: backend
spec:
  port: 8080
  host: backend
  routingKey: e2e-backend

# east/connector.yml
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: backend
spec:
  routingKey: e2e-backend
  port: 8080
  selector: app=backend
```

**Test flow**:
1. Environment validation (`e2e.tests.env_shakeout` role)
2. Namespace generation (`e2e.tests.generate_namespaces` role)
3. Create Skupper resources for both sites using `skupper-sites.yml` include
4. Issue AccessToken from west site (`skupper.v2.token` module)
5. Apply token to east site (`skupper.v2.resource` module)
6. Run connectivity test (`e2e.tests.run_curl` role)
7. Teardown (automatic cleanup)

**Key variables**:
- `namespace_prefix`: Base for generated namespace names
- `namespace_name`: Site-specific namespace suffix
- `run_curl_address`: Target endpoint for connectivity test
- `skip_teardown`: Skip cleanup (default: false)

---

#### 2. Redis Multicloud High Availability Test

**Directory**: `scenarios/redis/`

**Purpose**: Demonstrate distributed Redis with Sentinel across three Kubernetes clusters plus Podman.

**Architecture**:
- **West, East, North**: Kubernetes clusters with Redis Server + Sentinel
- **Podman site**: Non-Kubernetes environment connected via Skupper
- **Connectivity**: Hub-and-spoke from west to east, north, and podman

**What it demonstrates**:
- Multi-site connectivity (4 sites)
- Mixed platform deployment (Kubernetes + Podman)
- Stateful service networking (Redis with Sentinel failover)
- Multiple Listeners and Connectors per site
- `skupper.v2.system` module for Podman sites

**Test phases**:
1. **Kubernetes setup**: Sites, namespaces, Redis deployments
2. **Service networking**: Listeners and Connectors for Redis and Sentinel
3. **Site linking**: West issues token, east/north redeem
4. **Podman setup**: Network creation, site initialization, token redemption
5. **Validation**: Wait for pod readiness and site connectivity
6. **Teardown**: Cleanup across all platforms

**Podman-specific tasks**:
```yaml
- name: Create Skupper podman network
  containers.podman.podman_network:
    name: skupper
    state: present

- name: Create Skupper sites resources
  skupper.v2.resource:
    path: "{{ playbook_dir }}/resources/podman/"
    platform: podman

- name: Apply access token
  skupper.v2.resource:
    def: "{{ hostvars['west']['west_token']['token'] }}"
    platform: podman

- name: Initialize default namespace using podman
  skupper.v2.system:
    action: start
    platform: podman
```

---

#### 3. Labels and Annotations Test

**Directory**: `scenarios/labels-and-annotations/`

**Purpose**: Validate Skupper's ConfigMap-driven label and annotation propagation.

**Test scenarios**:
1. **Pre-existing component**: ConfigMap applied after Site creation → labels/annotations added
2. **New component**: ConfigMap exists before Site creation → labels/annotations present immediately
3. **Removal**: ConfigMap deleted → labels/annotations removed from all components

**What it demonstrates**:
- Dynamic component labeling via ConfigMap
- Skupper controller reconciliation behavior
- Validation using `kubernetes.core.k8s_info` module

**Test pattern**:
```yaml
- name: Deploy site before ConfigMap (Scenario 1)
  skupper.v2.resource:
    path: "{{ playbook_dir }}/resources/east/site.yml"
    namespace: "{{ namespace }}"

- name: Apply ConfigMap with custom labels/annotations
  kubernetes.core.k8s:
    state: present
    definition: "{{ lookup('file', 'configmap.yml') | from_yaml }}"

- name: Wait and verify labels appear
  kubernetes.core.k8s_info:
    kind: Deployment
    namespace: "{{ namespace }}"
    label_selectors:
      - "custom-label=custom-value"

- name: Delete ConfigMap
  kubernetes.core.k8s:
    state: absent
    # ...

- name: Verify labels removed
  # Assertion task
```

---

#### 4. Service Scale Test

**Directory**: `scenarios/service-scale/`

**Purpose**: Stress-test Skupper with large numbers of Listener/Connector pairs.

**Scale dimensions**:
- Number of Listeners (configurable, default varies)
- Number of Connectors (matches Listener count)
- All pairs route to single backend (differentiated by routing keys)

**What it demonstrates**:
- Dynamic resource generation at scale
- Performance validation under load
- Readiness polling for bulk resources

**Key variables**:
```yaml
service_count: 100  # Number of Listener/Connector pairs
service_name_prefix: svc
routing_key_prefix: svc
base_listener_port: 10080  # Incremented per service
backend_port: 8080
smoke_test_index: 1  # Which service to curl for validation
```

**Dynamic resource creation**:
```yaml
- name: Create N Listeners
  skupper.v2.resource:
    def:
      apiVersion: skupper.io/v2alpha1
      kind: Listener
      metadata:
        name: "{{ service_name_prefix }}{{ item }}"
      spec:
        port: "{{ base_listener_port + item }}"
        routingKey: "{{ routing_key_prefix }}{{ item }}"
  loop: "{{ range(1, service_count + 1) | list }}"

- name: Create N Connectors
  skupper.v2.resource:
    def:
      apiVersion: skupper.io/v2alpha1
      kind: Connector
      metadata:
        name: "{{ service_name_prefix }}{{ item }}"
      spec:
        port: "{{ backend_port }}"
        routingKey: "{{ routing_key_prefix }}{{ item }}"
        selector: "{{ backend_app_label }}"
  loop: "{{ range(1, service_count + 1) | list }}"
```

---

#### 5. Attached Connector Test

**Directory**: `scenarios/attached-connector/`

**Purpose**: Validate network connectivity and performance using iPerf3 and Skupper's Attached Connector feature.

**Architecture**:
- **Hub site**: Central Skupper site managing connections
- **Client site**: Runs iPerf3 client
- **Workload site**: Runs iPerf3 server

**What it demonstrates**:
- Attached Connectors (direct workload-to-router attachment)
- Performance testing integration (iPerf3)
- Three-site topology (hub-and-spoke)

---

#### 6. Expose Pods by Name Test

**Directory**: `scenarios/expose-pods-by-name/`

**Purpose**: Demonstrate exposing individual pods rather than services.

**What it demonstrates**:
- Pod-level service exposure
- Connector targeting specific pod names
- Use cases for stateful workloads or debugging

---

#### 7. High Availability (HA) Test

**Directory**: `scenarios/ha/`

**Purpose**: Validate Skupper's high availability and failover capabilities.

**What it demonstrates**:
- Multiple router instances per site
- Automatic failover on router failure
- Persistent connectivity during disruptions

---

## Common Ansible Patterns

### Pattern 1: Resource Application

Use `skupper.v2.resource` for all Skupper YAML resources:

```yaml
- name: Apply resources from directory
  skupper.v2.resource:
    path: "{{ playbook_dir }}/resources/west/"
    kubeconfig: "{{ kubeconfig }}"
    namespace: "{{ namespace }}"

- name: Apply inline resource definition
  skupper.v2.resource:
    def:
      apiVersion: skupper.io/v2alpha1
      kind: Site
      metadata:
        name: my-site
      spec:
        linkAccess: default
    kubeconfig: "{{ kubeconfig }}"
    namespace: "{{ namespace }}"

- name: Delete resources
  skupper.v2.resource:
    state: absent
    path: "{{ resources_path }}"
    kubeconfig: "{{ kubeconfig }}"
    namespace: "{{ namespace }}"
```

### Pattern 2: Token Generation and Redemption

```yaml
# Site A: Generate token
- name: Create access token
  skupper.v2.token:
    name: "site-a-grant"
    redemptions_allowed: 1
    namespace: "{{ namespace }}"
    kubeconfig: "{{ kubeconfig }}"
  register: site_a_token

# Site B: Redeem token
- name: Apply access token
  skupper.v2.resource:
    def: "{{ hostvars['site-a']['site_a_token']['token'] }}"
    namespace: "{{ namespace }}"
    kubeconfig: "{{ kubeconfig }}"
```

### Pattern 3: Cross-Host Variable Access

Use `hostvars` to share data between inventory hosts:

```yaml
# Playbook against host "west"
- hosts: west
  tasks:
    - name: Generate token
      skupper.v2.token:
        name: west-grant
      register: my_token

# Playbook against host "east"
- hosts: east
  tasks:
    - name: Use token from west
      skupper.v2.resource:
        def: "{{ hostvars['west']['my_token']['token'] }}"
```

### Pattern 4: Conditional Execution by Host

```yaml
- name: Task runs only on west
  skupper.v2.token:
    name: west-grant
  when: "'west' in inventory_hostname"

- name: Task runs only on east
  skupper.v2.resource:
    def: "{{ token }}"
  when: "'east' in inventory_hostname"
```

### Pattern 5: Non-Kubernetes Platforms

For Podman, Docker, or Linux sites:

```yaml
- name: Start Podman site
  skupper.v2.system:
    action: start
    platform: podman
    site_config_path: "{{ playbook_dir }}/podman-site.yaml"

- name: Apply resources to Podman
  skupper.v2.resource:
    path: "{{ playbook_dir }}/resources/"
    platform: podman

- name: Stop Podman site
  skupper.v2.system:
    action: stop
    platform: podman
```

---

## Reusable Roles

Located in `human/skupper/tests/e2e/collections/ansible_collections/e2e/tests/roles/`:

### `e2e.tests.env_shakeout`

Validates the test environment before proceeding.

**What it checks**:
- Cluster connectivity
- Required Kubernetes API access
- Ansible collection availability

### `e2e.tests.generate_namespaces`

Creates isolated namespaces for test runs.

**Variables**:
- `namespace_prefix`: Prefix for generated namespaces
- `generate_namespaces_namespace_label`: Label for cleanup identification

### `e2e.tests.run_curl`

Executes connectivity tests via curl.

**Variables**:
- `run_curl_address`: Target URL
- `run_curl_image`: Container image for curl pod
- `run_curl_retries`: Number of retry attempts
- `run_curl_delay`: Delay between retries (seconds)

### `e2e.tests.pod_wait`

Waits for pods to reach Running state.

**Variables**:
- `pod_wait_namespace`: Target namespace
- `pod_wait_label_selector`: Label selector for pods
- `pod_wait_timeout`: Timeout in seconds

### `e2e.tests.skupper_test_images`

Manages test container images.

**Provides variables**:
- `skupper_test_images_lanyard`: Image for HTTP testing

### `rescue`

Error recovery and cleanup tasks.

---

## Running the Examples

### Prerequisites

1. Install Ansible (2.15+):
   ```bash
   pip install ansible
   ```

2. Install required collections:
   ```bash
   ansible-galaxy collection install skupper.v2
   ansible-galaxy collection install kubernetes.core
   ansible-galaxy collection install containers.podman  # For Podman examples
   ```

3. Install Python dependencies:
   ```bash
   pip install -r https://raw.githubusercontent.com/skupperproject/skupper-ansible/refs/heads/main/requirements.txt
   ```

### Running Hello World Example

```bash
cd /path/to/skupper-example-ansible
ansible-galaxy collection install skupper.v2
ansible-playbook -i ansible/inventory.yml ansible/setup.yml
# Test the application
ansible-playbook -i ansible/inventory.yml ansible/teardown.yml
```

### Running E2E Tests

```bash
cd human/skupper/tests/e2e/scenarios/hello-world
ansible-playbook -i inventory/ test.yml

# Skip teardown for debugging
ansible-playbook -i inventory/ test.yml -e skip_teardown=true

# Override kubeconfig paths
ansible-playbook -i inventory/ test.yml \
  -e kubeconfig_1=/path/to/west.kubeconfig \
  -e kubeconfig_2=/path/to/east.kubeconfig
```

---

## Key Differences: Production vs. E2E Tests

| Aspect | Production Examples | E2E Tests |
|--------|-------------------|-----------|
| **Purpose** | Demonstrate real-world usage | Validate Skupper functionality |
| **Scope** | Single scenario (e.g., Hello World) | Multiple scenarios with variations |
| **Cleanup** | Manual (via teardown playbook) | Automatic (via `always` block) |
| **Namespace management** | User-provided | Auto-generated with labels |
| **Validation** | User-driven (port-forward, curl) | Automated (roles like `run_curl`) |
| **Inventory** | Simple, two hosts | Complex, with extensive variables |
| **Resource structure** | Bundled YAML files | Separated by site and resource type |

---

## Best Practices from the Examples

1. **Use inventory variables**: Define `kubeconfig`, `namespace`, and `resources_path` per host for flexibility.

2. **Leverage hostvars**: Share data (like tokens) between hosts without external files.

3. **Modularize with includes**: Use `include_tasks` or `include_role` for repeated operations (e.g., `skupper-sites.yml`).

4. **Always block for cleanup**: Wrap test tasks in a `block` with an `always` section for guaranteed teardown.

5. **Label resources**: Use labels like `e2e.id` for bulk cleanup via label selectors.

6. **Wait for readiness**: Use `kubernetes.core.k8s_info` with retries before testing services.

7. **Conditional tasks**: Use `when: "'hostname' in inventory_hostname"` for host-specific tasks.

8. **Platform abstraction**: Use the `platform` parameter (`kubernetes`, `podman`, `docker`, `linux`) for cross-platform playbooks.

---

## Troubleshooting

### Common Issues

1. **Module not found**:
   ```bash
   ansible-galaxy collection install skupper.v2 --force
   ```

2. **Python dependencies missing**:
   ```bash
   pip install kubernetes pyyaml jinja2
   ```

3. **Token redemption fails**:
   - Verify the token was registered: `debug: var=hostvars['source-host']['token_var']`
   - Check network connectivity between sites
   - Ensure `linkAccess: default` in Site spec

4. **Resources not deleted**:
   - Check for `state: absent` in `skupper.v2.resource`
   - Verify the `path` or `def` matches creation task
   - For namespace-level cleanup: `kubernetes.core.k8s` with `state: absent`

5. **Test results location**:
   - E2E tests store artifacts in `/tmp/ansible.<hostname>/`
   - Check `ansible.log` for detailed error messages

---

## Source References

- Production example: `scripts/skewer-yamls/skupper-example-ansible.yaml`
- E2E tests: `human/skupper/tests/e2e/scenarios/`
- Ansible collection: https://galaxy.ansible.com/ui/repo/published/skupper/v2/
- Collection source: https://github.com/skupperproject/skupper-ansible
- Requirements: https://raw.githubusercontent.com/skupperproject/skupper-ansible/refs/heads/main/requirements.txt

---

## Related Documentation

- [[skupper-ansible-overview]] - Overview of the Skupper Ansible collection
- [[skupper-ansible-module-resource]] - Resource module reference
- [[skupper-ansible-module-token]] - Token module reference
- [[skupper-ansible-module-system]] - System module reference (Podman/Docker/Linux)
- [[skupper-ansible-module-controller]] - Controller module reference
- [[skupper-ansible-workflow-kubernetes]] - Kubernetes workflow guide
- [[skupper-ansible-workflow-mixed-sites]] - Mixed-platform workflow guide
- [[skupper-ansible-workflow-non-kubernetes]] - Non-Kubernetes workflow guide
