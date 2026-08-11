---
type: GeneratedDocs
title: Skupper Ansible Systemd Architecture
id: skupper-ansible-systemd-architecture
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper-ansible.git
source_branch: main
source_commit: 632478a5245d1b71bd0eabb4b8e414f91c5b020b
source_paths:
- human/skupper-ansible/plugins/modules/controller.py
- human/skupper-ansible/plugins/module_utils/system.py
generated_at: '2026-08-11T17:21:38Z'
generator: claude-code
tags:
- skupper
- ansible
- systemd
- architecture
- controller
related:
- skupper-ansible-module-controller
- skupper-ansible-workflow-non-kubernetes
- skupper-ansible-workflow-mixed-sites
decision:
  authoring:
  - ansible
  setupStep:
  - architecture
  platform:
  - podman
  - docker
---

# Skupper Ansible Systemd Architecture

How the Skupper Ansible collection uses systemd to manage the controller without requiring the CLI binary on the host.

## Overview

The Skupper Ansible collection employs a containerized approach to running the Skupper controller on non-Kubernetes systems. Rather than requiring the Skupper CLI binary to be installed directly on target hosts—which some customers reject due to security or policy constraints—the collection uses the CLI container image from Quay.io and manages it through systemd services.

This architecture provides:

- **No host binary requirement**: The Skupper CLI runs entirely within a container
- **Declarative management**: Systemd handles service lifecycle, monitoring, and automatic restarts
- **Platform flexibility**: Supports both Podman (default) and Docker container engines
- **User-mode operation**: Runs as a regular user without requiring root privileges (when using Podman)

## Architecture Components

### 1. Container Image

The controller runs from the official container image:
- Default image: `quay.io/skupper/system-controller:v2-dev`
- Configurable via the `image` parameter in the Ansible module
- Always pulled with `--pull always` to ensure latest version

### 2. Systemd Service

The Ansible collection creates a systemd service file that:
- Manages the controller container lifecycle
- Ensures the controller starts on boot
- Monitors the controller process
- Provides standard service management through `systemctl`

Service file location:
- User mode (non-root): `~/.config/systemd/user/skupper-controller.service`
- System mode (root): `/etc/systemd/system/skupper-controller.service`

### 3. Startup Scripts

The collection generates shell scripts to start and stop the container:

**Start script** (`~/.local/share/skupper/system-controller/internal/scripts/start.sh`):
```bash
#!/usr/bin/env sh
set -o errexit
set -o nounset
<engine> start <container-name>
```

**Stop script** (`~/.local/share/skupper/system-controller/internal/scripts/stop.sh`):
```bash
#!/usr/bin/env sh
set -o errexit
set -o nounset
<engine> stop -t 10 <container-name>
```

Where `<engine>` is `podman` or `docker`, and `<container-name>` is `<username>-skupper-controller`.

## Installation Flow

When the Ansible `controller` module is invoked with `action: install`, the following sequence occurs:

### 1. Pre-flight Checks

```python
# Check if service already exists
if self.service_exists():
    return False  # Nothing to do

# Check if container already exists
exists, platform = self.get_container_info()
if exists:
    return False  # Nothing to do
```

### 2. Enable Podman Socket (Podman only)

For Podman platforms, the collection enables the Podman socket service:

```python
if self._platform == "podman":
    enable_podman_socket(self.module)
```

This runs: `systemctl --user enable --now podman.socket`

The socket allows the containerized controller to communicate with the Podman daemon.

### 3. Create Container

The collection builds and executes a container run command with:

**Base command structure**:
```bash
podman run -d \
  --pull always \
  --name <username>-skupper-controller \
  --label=application=skupper-v2 \
  --network host \
  --security-opt label=disable \
  -u <uid>:<gid> \
  --userns=keep-id \
  <volume-mounts> \
  <environment-variables> \
  quay.io/skupper/system-controller:v2-dev
```

**Volume mounts**:
- Data directory: `~/.local/share/skupper:/output:z`
- Container socket (non-Linux): `<runtime>/podman/podman.sock:/podman.sock`

**Environment variables**:
- `SKUPPER_OUTPUT_PATH`: `~/.local/share/skupper`
- `SKUPPER_PLATFORM`: `podman` or `docker`
- `SKUPPER_SYSTEM_RELOAD_TYPE`: `auto` or `manual`
- `CONTAINER_ENDPOINT`: Socket path for container engine (platform-dependent)
- `SKUPPER_ROUTER_IMAGE`: Optional router image override

**User namespace handling**:
- Podman (non-root): `--userns=keep-id` maps the user's UID inside the container
- Docker: `--userns=host` uses the host's user namespace
- RunAs user/group: Ensures the container runs with correct permissions

### 4. Create Startup Scripts

The module writes the start and stop scripts to:
```
~/.local/share/skupper/system-controller/internal/scripts/
```

These scripts wrap the container start/stop commands for use by systemd.

### 5. Create Systemd Service

The module generates a systemd service file:

```ini
[Unit]
Description=skupper-controller
After=network-online.target
Wants=network-online.target
RequiresMountsFor=<mount-paths>

[Service]
TimeoutStopSec=70
RemainAfterExit=yes
Environment=SKUPPER_OUTPUT_PATH=<data-home>
Environment=SKUPPER_PLATFORM=<platform>
Environment=CONTAINER_ENDPOINT=<endpoint>
ExecStart=/bin/bash <scripts-path>/start.sh
ExecStop=/bin/bash <scripts-path>/stop.sh
Type=simple

[Install]
WantedBy=default.target
```

**Key service parameters**:

- `After=network-online.target`: Ensures network is available before starting
- `RequiresMountsFor`: Systemd waits for mount points to be ready
- `TimeoutStopSec=70`: Allows 70 seconds for graceful shutdown
- `RemainAfterExit=yes`: Keeps the service active after the start script completes
- `Type=simple`: Standard service type for foreground processes
- `WantedBy=default.target`: Enables auto-start on boot

### 6. Enable and Start Service

The module enables and starts the service:

```bash
systemctl --user daemon-reload
systemctl --user enable --now skupper-controller.service
```

This:
- Reloads systemd configuration to recognize the new service
- Enables the service for automatic start on boot
- Starts the service immediately

## Uninstallation Flow

When the Ansible `controller` module is invoked with `action: uninstall`:

### 1. Stop and Remove Service

```python
if self.service_exists():
    systemd_delete(self.module, self.service_name())
```

This executes:
```bash
systemctl --user disable --now skupper-controller.service
systemctl --user daemon-reload
systemctl --user reset-failed
```

And removes the service file from `~/.config/systemd/user/`.

### 2. Remove Container

```python
exists, platform = self.get_container_info()
if exists and platform:
    command = [platform, "rm", "--force", self.container_name()]
```

Uses the detected platform (Podman or Docker) to forcefully remove the container.

### 3. Clean Data Directory

```python
base_path = "{}/system-controller".format(data_home())
if os.path.exists(base_path):
    shutil.rmtree(base_path)
```

Removes the entire `~/.local/share/skupper/system-controller/` directory, including startup scripts and any generated artifacts.

## Platform-Specific Behaviors

### Podman (Default)

**Advantages**:
- Rootless by default
- No daemon required (socket-activated)
- Better security isolation with user namespaces
- Native systemd integration

**Configuration**:
```yaml
- name: Install controller with Podman
  skupper.v2.controller:
    action: install
    platform: podman
```

**Runtime requirements**:
- Podman installed on the target host
- Podman socket enabled: `systemctl --user enable --now podman.socket`
- User has XDG_RUNTIME_DIR set (typically `/run/user/<uid>`)

**Socket location**: `$XDG_RUNTIME_DIR/podman/podman.sock`

### Docker

**Advantages**:
- Widely deployed
- Familiar to many administrators

**Configuration**:
```yaml
- name: Install controller with Docker
  skupper.v2.controller:
    action: install
    platform: docker
```

**Runtime requirements**:
- Docker daemon running
- User is member of the `docker` group
- Docker socket accessible at `/run/docker.sock`

**Important**: If using `podman-docker` (Docker CLI compatibility layer for Podman), use `platform: podman` instead. The `docker` platform expects a real Docker daemon and will fail if the `docker` group doesn't exist.

## Directory Layout

The Ansible collection uses standard XDG base directory specifications:

### Data Directory (`~/.local/share/skupper/`)

```
~/.local/share/skupper/
└── system-controller/
    └── internal/
        └── scripts/
            ├── start.sh
            └── stop.sh
```

Purpose: Persistent data and internal scripts

### Service Directory (`~/.config/systemd/user/`)

```
~/.config/systemd/user/
└── skupper-controller.service
```

Purpose: User systemd service definitions

### Runtime Directory (`/run/user/<uid>/`)

```
/run/user/<uid>/
└── podman/
    └── podman.sock
```

Purpose: Runtime sockets and ephemeral data

## Systemd Integration Details

### Service Lifecycle

**Start sequence**:
1. Systemd waits for `network-online.target`
2. Systemd ensures all `RequiresMountsFor` paths are available
3. Systemd executes `ExecStart=/bin/bash .../start.sh`
4. Script runs `podman start <container-name>`
5. Podman starts the existing container
6. Service transitions to `active` state

**Stop sequence**:
1. Systemd executes `ExecStop=/bin/bash .../stop.sh`
2. Script runs `podman stop -t 10 <container-name>`
3. Podman sends SIGTERM to the container
4. Podman waits up to 10 seconds for graceful shutdown
5. If timeout, Podman sends SIGKILL
6. Service transitions to `inactive` state

### Why Not Mount D-Bus?

Earlier approaches considered mounting the D-Bus socket into the container to allow the containerized CLI to communicate with systemd. This was rejected because:

1. **Complexity**: Mounting D-Bus requires additional security context handling
2. **Security**: Exposing the system bus to containers increases attack surface
3. **Brittleness**: D-Bus socket paths vary across distributions
4. **Unnecessary**: Creating the systemd service file directly from the host is simpler and more reliable

Instead, the Ansible collection creates the systemd service file directly on the host filesystem, completely avoiding the need to interact with systemd from inside the container.

### Service Monitoring

Systemd automatically monitors the service:

```bash
# Check service status
systemctl --user status skupper-controller.service

# View logs
journalctl --user -u skupper-controller.service

# Follow logs in real-time
journalctl --user -u skupper-controller.service -f
```

### Auto-restart on Failure

The current service definition does not include automatic restart on failure. To add this capability:

```ini
[Service]
Restart=on-failure
RestartSec=5s
```

This would configure systemd to automatically restart the controller if the container exits unexpectedly.

## Role Separation

### CLI Binary: Development and Testing

The standalone Skupper CLI binary is intended for:
- Manual testing in development environments
- Interactive debugging sessions
- Ad-hoc operations by developers
- Exploration and learning

**Not intended for**:
- Production deployments
- Automated infrastructure management
- Enterprise security-hardened environments

### Ansible Collection: Production and Automation

The Skupper Ansible collection is the declarative tool for:
- Production deployments
- Automated provisioning
- Configuration management
- Compliance with enterprise security policies
- Idempotent infrastructure management

**Key advantages**:
- No binary installation required on target hosts
- Fully declarative playbook-driven workflow
- Integrates with existing Ansible automation
- Auditable and version-controlled configurations
- Consistent with enterprise IT practices

## Reload Types

The controller supports two reload types for custom resources:

### Manual Reload (`reload_type: manual`)

**Default behavior**: The controller only loads input resources when explicitly instructed.

**Use case**: Production environments where changes should be carefully controlled.

**Configuration**:
```yaml
- name: Install with manual reload
  skupper.v2.controller:
    action: install
    reload_type: manual
```

**How to trigger reload**: Use the `system` module to reload resources:
```yaml
- name: Reload resources
  skupper.v2.system:
    namespace: default
    reload: true
```

### Auto Reload (`reload_type: auto`)

**Behavior**: The controller automatically detects and loads changes to input resource files.

**Use case**: Development environments where rapid iteration is needed.

**Configuration**:
```yaml
- name: Install with auto reload
  skupper.v2.controller:
    action: install
    reload_type: auto
```

**Environment variable**: Sets `SKUPPER_SYSTEM_RELOAD_TYPE=auto` in the container.

## Security Considerations

### SELinux Context

Volume mounts use the `:z` flag:
```bash
-v ~/.local/share/skupper:/output:z
```

This automatically relabels the host directory with the appropriate SELinux context, allowing the container to access it even when SELinux is in enforcing mode.

### Security Options

The container runs with:
```bash
--security-opt label=disable
```

This disables SELinux label confinement for the container. In production environments with strict security requirements, this should be reviewed and potentially replaced with a custom SELinux policy.

### User Namespace Isolation

**Podman (rootless)**:
```bash
--userns=keep-id
```

Maps the current user's UID/GID into the container, ensuring files created in mounted volumes have the correct ownership.

**Docker**:
```bash
--userns=host
```

Uses the host's user namespace. Requires the user to be in the `docker` group.

### Network Mode

The container uses host networking:
```bash
--network host
```

This allows the controller to bind to host ports directly and communicate with other Skupper components. In security-conscious environments, consider whether network isolation is required.

## Troubleshooting

### Container Exists but Service Doesn't Start

**Symptom**: Service fails to start with "container already exists" error.

**Cause**: Container was created but systemd service was not installed, or previous installation was incomplete.

**Resolution**:
```yaml
# Uninstall to clean up
- name: Clean up
  skupper.v2.controller:
    action: uninstall

# Reinstall
- name: Reinstall
  skupper.v2.controller:
    action: install
```

### Podman Socket Not Available

**Symptom**: Error about `/run/user/<uid>/podman/podman.sock` not found.

**Cause**: Podman socket service not enabled.

**Resolution**:
```bash
systemctl --user enable --now podman.socket
```

The Ansible module does this automatically, but manual intervention may be needed if the service fails to start.

### Service Starts but Controller Not Running

**Symptom**: `systemctl status` shows active, but container is not running.

**Cause**: `RemainAfterExit=yes` keeps the service active even if the start script completes.

**Diagnosis**:
```bash
# Check container status
podman ps -a | grep skupper-controller

# Check container logs
podman logs <username>-skupper-controller

# Check systemd journal
journalctl --user -u skupper-controller.service -n 50
```

### Docker Group Not Found

**Symptom**: Error message "unable to determine docker group id".

**Cause**: Using `platform: docker` with `podman-docker` compatibility layer.

**Resolution**: Change to `platform: podman`:
```yaml
- name: Use Podman platform
  skupper.v2.controller:
    action: install
    platform: podman
```

## Comparison with Other Deployment Methods

### vs. Kubernetes Operator

**Kubernetes Operator**:
- Native Kubernetes resource management
- Leverages Kubernetes controllers and reconciliation loops
- Integrated with Kubernetes RBAC and admission control
- Automatic pod lifecycle management

**Ansible + Systemd**:
- Works on bare metal, VMs, and non-Kubernetes systems
- Uses systemd for process management and monitoring
- Integrates with existing Ansible automation
- Suitable for heterogeneous environments

### vs. Manual CLI Installation

**Manual CLI**:
- Simple for development and testing
- Quick to get started
- Interactive control
- Manual lifecycle management

**Ansible + Systemd**:
- Fully automated installation and configuration
- Declarative and idempotent
- No host binary requirement
- Production-ready monitoring and lifecycle management
- Consistent with enterprise IT practices

## Future Enhancements

Potential improvements to the systemd integration:

### Automatic Restart

Add restart configuration to the service:
```ini
[Service]
Restart=on-failure
RestartSec=5s
StartLimitInterval=60s
StartLimitBurst=3
```

### Health Checks

Integrate systemd watchdog for proactive health monitoring:
```ini
[Service]
WatchdogSec=30s
```

Requires the controller to support systemd watchdog protocol.

### Resource Limits

Apply cgroup resource constraints:
```ini
[Service]
MemoryMax=1G
CPUQuota=50%
```

### Graceful Updates

Support in-place updates without service disruption:
```yaml
- name: Update controller image
  skupper.v2.controller:
    action: update
    image: quay.io/skupper/system-controller:v2.1.0
```

Would require implementing a rolling update mechanism with graceful handoff.

## Related Documentation

- [skupper-ansible-module-controller](skupper-ansible-module-controller.md): Controller module reference
- [skupper-ansible-workflow-non-kubernetes](skupper-ansible-workflow-non-kubernetes.md): Non-Kubernetes deployment workflow
- [skupper-ansible-workflow-mixed-sites](skupper-ansible-workflow-mixed-sites.md): Mixed Kubernetes and non-Kubernetes sites

## References

### Source Code

- Controller module: `plugins/modules/controller.py`
- System utilities: `plugins/module_utils/system.py`
- Common utilities: `plugins/module_utils/common.py`

### External Documentation

- [Systemd service unit documentation](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
- [Podman systemd integration](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
