# Skupper Integration and E2E Tests

## Overview

The Skupper test suite consists of two main categories:

1. **Integration Tests** - Go-based tests using envtest (Kubernetes API server + etcd) to test controller logic
2. **E2E Tests** - Ansible-based scenario tests that validate Skupper functionality across real clusters

---

## Integration Tests

**Location**: `tests/integration/kube/controller/`

### Purpose

Go integration tests validate Skupper components against a real Kubernetes API server using [envtest](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/envtest). These tests sit between unit tests (which use fake clients) and full E2E tests (which require real clusters with cross-site networking).

### Architecture

- Uses envtest framework (kube-apiserver + etcd) without requiring a full cluster
- Runs in-process controller instance
- Tests are tagged with `//go:build integration` to separate from unit tests
- Shared controller instance per test suite for performance

### Test Suite Structure

```
tests/integration/kube/controller/
├── suite_test.go      # Test suite setup and shared controller
├── site_test.go       # Site resource tests
├── listener_test.go   # Listener resource tests
└── helpers_test.go    # Test utilities and helpers
```

### Test Cases

#### Site Tests (`site_test.go`)

**TestSimpleSite**
- Validates basic Site resource creation and reconciliation
- Creates a Site resource in namespace `simple-site`
- Verifies Site status conditions reach `Configured=True`
- Validates router Deployment is created with:
  - Labels: `skupper.io/component=router`, `application=skupper-router`
  - 2 containers in pod template
- Checks Site status is `Pending` with message "Not Running"

#### Listener Tests (`listener_test.go`)

**TestSiteWithListener**
- Validates Listener resource creation and Service exposure
- Creates Site and Listener resources in namespace `site-with-listener`
- Verifies:
  - Listener status condition `Configured=True`
  - Kubernetes Service created matching Listener spec
  - Service selector matches router: `skupper.io/component=router`, `application=skupper-router`
  - Service port matches Listener port (8080)
  - Service labeled with `internal.skupper.io/listener=mylistener`
  - Router ConfigMap contains listener configuration entry

### Prerequisites

- Go 1.21+
- `setup-envtest` binary (installed via go.mod tool directive)
- Kubernetes test binaries v1.33.0 (auto-downloaded)

### Running Integration Tests

#### From Repository Root

```bash
# Using Make (recommended)
make -C tests test-integration

# Or directly with go test
export KUBEBUILDER_ASSETS=$(go tool setup-envtest use 1.33.0 -p path)
go test -tags=integration -v ./tests/integration/kube/controller/...
```

#### From tests/ Directory

```bash
make test-integration
```

#### Against Existing Cluster

By default, tests use envtest's local API server. To run against a real cluster:

```bash
# Ensure kubectl context is correct
kubectl config current-context

# Run tests against existing cluster
USE_EXISTING_CLUSTER=true make -C tests test-integration
```

**Warning**: Tests create/delete namespaces and resources. Use development clusters only.

### Test Execution Details

- **Timeout**: ~1 minute per test suite
- **Parallelization**: Tests run sequentially (shared controller)
- **Isolation**: Fresh namespace per test case
- **Controller**: Single shared instance for all tests in suite
- **Build Tag**: `integration` (excluded from default `make test`)

### Known Behavior

- Gateway, Contour, and OpenShift Route CRD warnings in logs are expected (CRDs not installed)
- Teardown warning about kube-apiserver shutdown may appear (envtest quirk, not a failure)

---

## End-to-End (E2E) Tests

**Location**: `tests/e2e/scenarios/`

### Purpose

Ansible-based scenario tests that validate Skupper functionality across real Kubernetes clusters and Podman environments. Tests verify complete workflows including site creation, linking, service exposure, and application connectivity.

### Architecture

- **Framework**: Ansible with custom collections (`e2e.tests`, `skupper.v2`)
- **Execution**: Python 3.9+ virtual environment
- **Orchestration**: Make-based test runner with namespace isolation
- **CI Integration**: Subset of tests run in continuous integration

### Test Scenario Catalog

#### Hello World (`hello-world/`)

**Purpose**: Demonstrates fundamental Skupper setup between two clusters
- **Topology**: 2 sites (west, east)
- **Workflow**:
  1. Create Skupper sites in `west` and `east` namespaces
  2. Deploy frontend application in `west`
  3. Deploy backend application in `east`
  4. Link sites via Connector/AccessGrant
  5. Expose backend service to `west` via Listener/Connector
  6. Validate frontend can reach backend across clusters
- **Validation**: HTTP connectivity test from frontend to backend
- **CI Status**: ✅ Included in CI suite

#### Attached Connector (`attached-connector/`)

**Purpose**: Validates Skupper connectivity and measures network performance using iperf3
- **Topology**: 3 sites (hub, client, workload)
- **Architecture**:
  - **Hub Site**: Central connection manager
  - **Client Site**: Runs iperf3 client
  - **Workload Site**: Runs iperf3 server
- **Workflow**:
  1. Create Skupper sites in all namespaces
  2. Link sites through hub (star topology)
  3. Deploy iperf3 server in workload site
  4. Create Attached Connector linking to server
  5. Deploy iperf3 client in client site
  6. Execute performance tests
- **Validation**:
  - Site creation successful
  - Attached Connector configuration
  - Network connectivity through Skupper
  - Performance metrics collection
- **CI Status**: ✅ Included in CI suite

#### High Availability (`ha/`)

**Purpose**: Validates Skupper router high availability during pod failures
- **Topology**: 2 sites (westha, eastha) with HA enabled
- **HA Configuration**: 2 router instances per site
- **Load Generator**: Locust HTTP load testing
- **Workflow**:
  1. Create HA-enabled Skupper sites (2 routers each)
  2. Deploy backend application in `eastha`
  3. Expose backend to `westha` via Listener/Connector
  4. Start Locust job generating HTTP POST load
  5. During load test:
     - Terminate `router1` pod
     - Wait for recovery
     - Terminate `router2` pod
     - Repeat cycle
  6. Collect Locust logs and analyze failure rate
- **Validation**:
  - Service continuity during pod terminations
  - Acceptable failure rate under chaos
  - Router pod recovery
- **Success Criteria**: Minimal HTTP failures during router disruptions
- **CI Status**: ✅ Included in CI suite

#### Redis Multi-Cloud HA (`redis/`)

**Purpose**: Demonstrates highly available Redis architecture across multiple environments
- **Topology**: 4 sites (west, east, north Kubernetes + Podman)
- **Redis Architecture**:
  - Redis Server deployments across sites
  - Redis Sentinel for automatic failover
  - Skupper-connected Redis cluster
- **Workflow**:
  1. Create Skupper sites across Kubernetes clusters and Podman
  2. Deploy Redis Server instances in each site
  3. Deploy Redis Sentinel instances
  4. Link all sites via Skupper
  5. Expose Redis services via Listener/Connector
  6. Validate distributed caching and replication
  7. Test Sentinel failover capabilities
- **Validation**:
  - Redis cluster formation across sites
  - Data persistence and replication
  - Sentinel-based failover
  - Cross-environment connectivity (K8s ↔ Podman)
- **CI Status**: ❌ Not in CI suite (requires multi-cluster + Podman setup)

#### Labels and Annotations (`labels-and-annotations/`)

**Purpose**: Validates Skupper's ability to apply custom labels/annotations to components via ConfigMap
- **Test Scenarios**:

  **Scenario 1: Pre-existing Component**
  - Component exists before ConfigMap
  - Deploy ConfigMap with custom metadata
  - Verify component is automatically labeled/annotated
  - With `includePods: true`, verify Deployment pod template receives metadata

  **Scenario 2: New Component**
  - ConfigMap exists first
  - Create new component
  - Verify component is created with metadata pre-applied
  - Verify pod template metadata when `includePods: true`

  **Scenario 3: Removal**
  - Remove ConfigMap
  - Verify all custom labels/annotations removed from components
  - Verify removal regardless of component creation order

- **Validation**:
  - Label/annotation application on Deployments
  - Pod template metadata propagation
  - Automatic reconciliation on ConfigMap changes
  - Clean removal on ConfigMap deletion
- **CI Status**: ✅ Included in CI suite

#### Expose Pods by Name (`expose-pods-by-name/`)

**Purpose**: Validates exposing individual pods by name with dynamic updates on pod changes
- **Topology**: 2 sites (west, east)
- **Configuration**: `exposePodsByName: true` in Connector and Listener
- **Workflow**:
  1. Create linked Skupper sites
  2. Deploy backend with 3 replicas in `east`
  3. Expose pods by name to `west`
  4. **Phase 1 Validation**: Verify exposed services match pod names
  5. Restart backend Deployment (triggers new pod names)
  6. **Phase 2 Validation**: Verify exposed services updated to new pod names only
- **Validation**:
  - Service names match backend pod names
  - Service count matches replica count
  - Services automatically update on pod recreation
  - Old service names removed after pod deletion
- **CI Status**: ❌ Not in CI suite (issue [#2251](https://github.com/skupperproject/skupper/issues/2251))

#### Service Scale (`service-scale/`)

**Purpose**: Validates Skupper performance with large numbers of Listener/Connector pairs
- **Topology**: 2 sites (west, east)
- **Scale Dimensions**:
  - Number of Listeners (west site)
  - Number of Connectors (east site)
  - All routing to single backend application
- **Configuration**:
  - Single backend app in `east`
  - N Listener/Connector pairs
  - Unique ports per Listener
  - Routing keys for traffic differentiation
- **Workflow**:
  1. Create Skupper sites
  2. Deploy single backend in `east`
  3. Create N Listener/Connector pairs
  4. Execute smoke test on one service
  5. Run readiness checks on all services
- **Validation**:
  - All Listeners reach Ready state
  - All Connectors reach Ready state
  - Services remain functional under scale
  - Controller performance under high resource count
- **CI Status**: ❌ Not in CI suite (resource-intensive)

### E2E Test Framework

#### Directory Structure

Each test scenario follows this structure:

```
e2e/scenarios/<test-name>/
├── ansible.cfg           # Ansible configuration
├── collections/
│   └── requirements.yml  # Ansible collection dependencies
├── inventory/
│   ├── hosts.yml        # Cluster inventory
│   ├── group_vars/
│   │   └── all.yml      # Global variables
│   └── host_vars/       # Per-cluster variables
├── README.md            # Test documentation
├── requirements.txt     # Python dependencies
└── test.yml             # Main test playbook
```

#### Ansible Collections

Required collections:

- `ansible.posix` - POSIX utilities
- `ansible.scm` - Source control management
- `ansible.utils` - Ansible utilities
- `kubernetes.core` - Kubernetes resource management
- `skupper.v2` - Skupper V2 operations
- `e2e.tests` - E2E test roles and utilities
- `containers.podman` - Podman integration (Redis test)

### Running E2E Tests

#### Prerequisites

1. **Skupper V2**: Installed cluster-wide on target cluster(s)
2. **Kubernetes Access**: Valid kubeconfig with appropriate permissions
3. **Python**: 3.9+ with required dependencies
4. **Ansible**: Core packages and collections

#### Setup Virtual Environment

```bash
# Create virtual environment (one-time or force refresh)
make create-venv FORCE=true
```

This creates `/tmp/e2e-venv` with:
- Python virtual environment
- pip dependencies from `requirements.txt`
- Ansible collections from `collections/requirements.yml`

#### Build Test Images (Optional)

If testing code changes:

```bash
# From repository root
make podman-build
```

#### Quick Cluster Setup

Create kind cluster for testing:

```bash
# Creates kind cluster with MetalLB load balancer
KUBECONFIG=~/.kube/config ./scripts/kind-dev-cluster -r --metallb -i podman
```

#### Run Individual Test

```bash
# From tests/ directory
make test TEST="hello-world"
```

This will:
1. Activate virtual environment
2. Generate random namespace prefix (5 chars)
3. Run test playbook
4. Log to `/tmp/e2e/<test-name>/ansible_<timestamp>.log`

#### Run Multiple Tests

```bash
# Run all tests sequentially
make e2e-tests

# Run subset in parallel
make test-subset TESTS="hello-world,attached-connector,ha"

# Run CI test suite
make ci-tests
```

#### Test Role Individually

```bash
make test-role ROLE="role_name"
```

### Configuration

#### Resource Multipliers (`vars.yml`)

Adjust retry/delay behavior for flaky environments:

```yaml
RESOURCE_RETRY_MULTIPLIER: 2    # 2x retry attempts
RESOURCE_DELAY_MULTIPLIER: 3    # 3x delay between retries
```

Used in playbooks:

```yaml
retries: "{{ resource_retry_value * RESOURCE_RETRY_MULTIPLIER }}"
delay: "{{ resource_delay_value * RESOURCE_DELAY_MULTIPLIER }}"
```

#### Namespace Isolation

Tests automatically generate unique namespace prefixes to avoid conflicts:

```bash
# Generated format: <prefix>-west, <prefix>-east
# Example: a3k9x-west, a3k9x-east
```

### CI Test Suite

Tests included in continuous integration:

```makefile
TESTS_CI := attached-connector,ha,hello-world,labels-and-annotations
```

Excluded from CI (require special setup or have open issues):
- `redis` - Requires multi-cluster + Podman environment
- `expose-pods-by-name` - Issue #2251
- `service-scale` - Resource-intensive

---

## Test Comparison Matrix

| Aspect | Integration Tests | E2E Tests |
|--------|------------------|-----------|
| **Language** | Go | Ansible/Python |
| **Scope** | Controller logic | Full scenarios |
| **Environment** | envtest (local API) | Real clusters |
| **Duration** | ~1 minute | 5-15 minutes/test |
| **Isolation** | In-process | Cross-cluster |
| **Networking** | No real networking | Real cross-site links |
| **CI Frequency** | Every commit | PR validation |
| **Setup Complexity** | Low (auto-download) | Medium (clusters required) |
| **Debugging** | Easy (in-process) | Complex (distributed) |

---

## Test Coverage Map

### What Integration Tests Cover

- ✅ Site resource reconciliation
- ✅ Listener resource reconciliation
- ✅ Service creation from Listener
- ✅ Router Deployment creation
- ✅ ConfigMap generation
- ✅ Status condition updates
- ❌ Cross-site networking (no real network)
- ❌ AccessGrant/Connector linking (requires 2 sites)
- ❌ Application connectivity (no pods running)

### What E2E Tests Cover

- ✅ Full site lifecycle (creation, linking, deletion)
- ✅ Cross-cluster networking
- ✅ Application connectivity end-to-end
- ✅ High availability scenarios
- ✅ Performance testing (iperf3)
- ✅ Load resilience (HA test)
- ✅ Multi-environment (K8s + Podman)
- ✅ Metadata management (labels/annotations)
- ✅ Scale testing (service-scale)

---

## Development Guidelines

### Adding Integration Tests

1. Create test file in `tests/integration/kube/controller/`
2. Add `//go:build integration` tag
3. Use shared `setup(t)` helper
4. Create isolated namespace per test
5. Use `waitFor()` for async reconciliation
6. Verify status conditions explicitly
7. Clean up via namespace deletion (automatic)

**Example Test Skeleton**:

```go
//go:build integration

func TestNewFeature(t *testing.T) {
    tc := setup(t)
    namespace := "test-new-feature"
    tc.createNamespace(namespace)

    // Create resources
    // Wait for reconciliation
    // Verify status
    // Assert expected state
}
```

### Adding E2E Tests

1. Copy `hello-world` scenario as template:
   ```bash
   cp -r tests/e2e/scenarios/hello-world tests/e2e/scenarios/my-test
   ```

2. Update test files:
   - `README.md` - Test documentation
   - `test.yml` - Main playbook
   - `inventory/` - Cluster configuration

3. Add to CI suite (if appropriate):
   ```makefile
   TESTS_CI := ...,my-test
   ```

4. Document in test catalog (this document)

### Test Best Practices

#### Integration Tests

- Use descriptive test names: `TestFeatureWithCondition`
- Verify status conditions explicitly
- Use `waitFor()` for async operations
- Assert on specific fields, not deep equality
- Clean up via namespace deletion
- Don't assume controller timing

#### E2E Tests

- Use unique namespace prefixes
- Document topology in README with diagrams
- Add resource multipliers for retry logic
- Validate both positive and negative cases
- Clean up resources in playbook teardown
- Log ansible output to `/tmp/e2e/`

---

## Troubleshooting

### Integration Tests

**Problem**: `setup-envtest: command not found`

```bash
# From repository root
go install sigs.k8s.io/controller-runtime/tools/setup-envtest@latest
```

**Problem**: Test hangs on reconciliation

- Increase timeout in `waitFor()` call
- Check controller logs for errors
- Verify CRDs loaded correctly
- Check resource events: `kubectl describe <resource>`

**Problem**: envtest teardown warnings

- Expected behavior, not a test failure
- Related to kube-apiserver shutdown sequence

### E2E Tests

**Problem**: `Virtual environment does not exist`

```bash
make create-venv FORCE=true
```

**Problem**: Ansible collection not found

```bash
# From tests/
ANSIBLE_CONFIG=e2e/ansible.cfg \
ansible-galaxy collection install -r e2e/collections/ansible_collections/requirements.yml --force
```

**Problem**: Test fails with "namespace already exists"

- Old test didn't clean up
- Delete manually: `kubectl delete ns <prefix>-*`
- Use unique prefix: generated automatically by Makefile

**Problem**: Skupper site not reaching Ready

- Check controller logs: `kubectl logs -n skupper-system deploy/skupper-controller`
- Verify Skupper installed cluster-wide
- Check resource events: `kubectl describe site -n <namespace>`
- Increase retry multipliers in `vars.yml`

**Problem**: Image pull errors

- Build images: `make podman-build` from repository root
- Check image availability in cluster
- Verify image pull policy in Skupper configuration

---

## Test Metrics

### Integration Test Performance

- **Suite Setup**: ~500ms (controller start)
- **Per Test**: ~2-5 seconds
- **Total Suite**: ~1 minute
- **Parallelization**: Sequential (shared controller)

### E2E Test Performance

| Test | Duration | Sites | Resources |
|------|----------|-------|-----------|
| hello-world | 5-7 min | 2 | ~10 |
| attached-connector | 8-10 min | 3 | ~15 |
| ha | 12-15 min | 2 HA | ~20 |
| redis | 15-20 min | 4 | ~30 |
| labels-and-annotations | 6-8 min | 1 | ~8 |
| service-scale | 10-20 min | 2 | N×2+5 |

*Durations vary based on cluster performance and network conditions*

---

## Future Test Enhancements

### Integration Tests

- [ ] Add Connector resource tests
- [ ] Add AccessGrant resource tests  
- [ ] Test link creation between sites
- [ ] Validate router ConfigMap content structure
- [ ] Test error conditions and validation
- [ ] Add tests for nonkube controller

### E2E Tests

- [ ] Fix expose-pods-by-name (issue #2251)
- [ ] Add observability validation
- [ ] Add certificate rotation test
- [ ] Add network policy test
- [ ] Add upgrade/downgrade test
- [ ] Add disaster recovery scenario
- [ ] Performance baseline tracking

---

## References

- **Integration Test Framework**: [envtest documentation](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/envtest)
- **E2E Test Collections**: `tests/e2e/collections/ansible_collections/`
- **Test Makefile**: `tests/Makefile`
- **Integration README**: `tests/integration/README.md`
- **E2E README**: `tests/README.md`
- **Issue Tracker**: [skupperproject/skupper/issues](https://github.com/skupperproject/skupper/issues)

---

**Document Version**: 1.0  
**Last Updated**: 2026-08-21  
**Skupper Version**: V2 (main branch)
