#!/usr/bin/env python3
"""Generate OKF pages from the Skupper Ansible collection snapshot."""

from __future__ import annotations

import argparse
import ast
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as error:  # pragma: no cover
    raise SystemExit("PyYAML is required to generate Ansible docs") from error


SOURCE_REPO_URL = "https://github.com/skupperproject/skupper-ansible.git"
DEFAULT_SOURCE_REPO = Path("human/skupper-ansible")
DEFAULT_OUTPUT_DIR = Path("generated/skupper-ansible")


def log(message: str) -> None:
    print(f"generate-ansible-docs: {message}", file=sys.stderr)


def die(message: str) -> None:
    raise SystemExit(f"generate-ansible-docs: ERROR: {message}")


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def read_source_record(path: Path) -> dict[str, str]:
    if not path.exists():
        return {
            "repo": SOURCE_REPO_URL,
            "branch": "main",
            "commit": "unknown",
        }

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {"repo": SOURCE_REPO_URL, "branch": "main", "commit": "unknown"}

    frontmatter = text.split("---", 2)[1]
    data = yaml.safe_load(frontmatter) or {}
    return {
        "repo": str(data.get("repo") or SOURCE_REPO_URL),
        "branch": str(data.get("branch") or "main"),
        "commit": str(data.get("commit") or "unknown"),
    }


def extract_assignments(path: Path) -> dict[str, str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    values: dict[str, str] = {}

    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        name = node.targets[0].id
        if name not in {"DOCUMENTATION", "EXAMPLES", "RETURN"}:
            continue
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            values[name] = node.value.value.strip()

    return values


def parse_doc_yaml(raw: str) -> dict[str, Any]:
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        die("unexpected module DOCUMENTATION shape")
    return data


def normalize_description(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(str(item).strip() for item in value if str(item).strip())
    return str(value).strip()


def format_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def yaml_frontmatter(data: dict[str, Any]) -> str:
    return "---\n" + yaml.safe_dump(data, sort_keys=False).strip() + "\n---\n\n"


def render_options(options: dict[str, Any]) -> list[str]:
    if not options:
        return ["No module-specific options are documented."]

    lines = [
        "| Option | Type | Default | Choices | Description |",
        "| --- | --- | --- | --- | --- |",
    ]

    for name, data in sorted(options.items()):
        data = data or {}
        description = normalize_description(data.get("description")).replace("\n", " ")
        option_type = format_value(data.get("type"))
        default = format_value(data.get("default"))
        choices = format_value(data.get("choices"))
        lines.append(f"| `{name}` | {option_type} | {default} | {choices} | {description} |")

    return lines


def decision_for_module(module: str) -> dict[str, Any]:
    base = {"authoring": ["ansible"]}
    if module == "resource":
        base.update(
            {
                "setupStep": [
                    "configure-listener",
                    "configure-connector",
                    "join-sites",
                ],
                "resource": [
                    "site",
                    "listener",
                    "connector",
                    "link",
                    "access-token",
                ],
                "platform": ["kubernetes", "podman", "docker", "linux"],
            }
        )
    elif module == "token":
        base.update(
            {
                "setupStep": ["join-sites"],
                "resource": ["access-grant", "access-token", "link"],
                "platform": ["kubernetes", "podman", "docker", "linux"],
                "joinMethod": ["access-grant-token"],
            }
        )
    elif module == "system":
        base.update(
            {
                "setupStep": ["identify-sites", "decide-link-access", "validate"],
                "platform": ["podman", "docker", "linux"],
            }
        )
    elif module == "controller":
        base.update(
            {
                "setupStep": ["identify-sites", "validate"],
                "platform": ["podman", "docker"],
            }
        )
    return base


def render_module_page(
    module_path: Path,
    source_repo: Path,
    source_record: dict[str, str],
    generated_at: str,
) -> tuple[str, str]:
    assignments = extract_assignments(module_path)
    if "DOCUMENTATION" not in assignments:
        die(f"missing DOCUMENTATION in {module_path}")

    doc = parse_doc_yaml(assignments["DOCUMENTATION"])
    module = str(doc.get("module") or module_path.stem)
    title = f"Skupper Ansible module: {module}"
    page_id = f"skupper-ansible-module-{slugify(module)}"
    source_path = f"human/skupper-ansible/{module_path.relative_to(source_repo)}"

    frontmatter = {
        "type": "GeneratedDocs",
        "title": title,
        "id": page_id,
        "status": "generated",
        "reviewed": False,
        "source_repo": source_record["repo"],
        "source_branch": source_record["branch"],
        "source_commit": source_record["commit"],
        "source_paths": [source_path],
        "generated_at": generated_at,
        "generator": "generate-ansible-docs.py",
        "tags": ["skupper", "ansible", "module", module],
        "related": [
            "skupper-ansible-overview",
            "skupper-ansible-workflow-kubernetes",
            "skupper-ansible-workflow-non-kubernetes",
            "skupper-ansible-workflow-mixed-sites",
        ],
        "decision": decision_for_module(module),
    }

    lines = [yaml_frontmatter(frontmatter), f"# {title}", ""]
    if doc.get("short_description"):
        lines.extend([str(doc["short_description"]).strip(), ""])

    description = normalize_description(doc.get("description"))
    if description:
        lines.extend(["## Description", "", description, ""])

    lines.extend(["## Options", "", *render_options(doc.get("options") or {}), ""])

    if doc.get("extends_documentation_fragment"):
        lines.extend(
            [
                "## Shared Options",
                "",
                "This module extends the `skupper.v2.common_options` documentation fragment for common Skupper connection options such as `platform`, `namespace`, `kubeconfig`, and `context`.",
                "",
            ]
        )

    requirements = doc.get("requirements") or []
    if requirements:
        lines.extend(["## Requirements", ""])
        lines.extend(f"- `{item}`" for item in requirements)
        lines.append("")

    examples = assignments.get("EXAMPLES", "").strip()
    if examples:
        lines.extend(["## Examples", "", "```yaml", examples, "```", ""])

    returns = assignments.get("RETURN", "").strip()
    if returns:
        lines.extend(["## Return Values", "", "```yaml", returns, "```", ""])

    lines.extend(["## Source", "", f"- `{source_path}`", ""])

    return f"{page_id}.md", "\n".join(lines).rstrip() + "\n"


def render_curated_pages(source_record: dict[str, str], generated_at: str) -> dict[str, str]:
    common = {
        "status": "generated",
        "reviewed": False,
        "source_repo": source_record["repo"],
        "source_branch": source_record["branch"],
        "source_commit": source_record["commit"],
        "generated_at": generated_at,
        "generator": "generate-ansible-docs.py",
        "tags": ["skupper", "ansible"],
    }

    pages: dict[str, str] = {}

    overview_fm = {
        **common,
        "type": "Concept",
        "title": "Skupper Ansible collection",
        "id": "skupper-ansible-overview",
        "source_paths": [
            "human/skupper-ansible/README.md",
            "human/skupper-ansible/plugins/doc_fragments/common_options.py",
        ],
        "related": [
            "skupper-ansible-module-resource",
            "skupper-ansible-module-token",
            "skupper-ansible-module-system",
            "skupper-ansible-module-controller",
            "skupper-ansible-workflow-mixed-sites",
        ],
        "decision": {
            "authoring": ["ansible"],
            "platform": ["kubernetes", "podman", "docker", "linux"],
        },
    }
    pages["skupper-ansible-overview.md"] = (
        yaml_frontmatter(overview_fm)
        + """# Skupper Ansible collection

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
"""
    )

    kube_fm = {
        **common,
        "type": "Workflow",
        "title": "Skupper Ansible Kubernetes workflow",
        "id": "skupper-ansible-workflow-kubernetes",
        "source_paths": [
            "human/skupper-ansible/README.md",
            "human/skupper-ansible/plugins/modules/resource.py",
            "human/skupper-ansible/plugins/modules/token.py",
        ],
        "related": [
            "skupper-concept-listener",
            "skupper-concept-connector",
            "skupper-ansible-module-resource",
            "skupper-ansible-module-token",
            "skupper-ansible-workflow-mixed-sites",
        ],
        "decision": {
            "authoring": ["ansible"],
            "platform": ["kubernetes"],
            "setupStep": [
                "configure-listener",
                "configure-connector",
                "join-sites",
                "validate",
            ],
            "resource": ["site", "listener", "connector", "link"],
        },
    }
    pages["skupper-ansible-workflow-kubernetes.md"] = (
        yaml_frontmatter(kube_fm)
        + """# Skupper Ansible Kubernetes workflow

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
"""
    )

    nonkube_fm = {
        **common,
        "type": "Workflow",
        "title": "Skupper Ansible non-Kubernetes workflow",
        "id": "skupper-ansible-workflow-non-kubernetes",
        "source_paths": [
            "human/skupper-ansible/README.md",
            "human/skupper-ansible/plugins/modules/resource.py",
            "human/skupper-ansible/plugins/modules/system.py",
            "human/skupper-ansible/plugins/modules/controller.py",
        ],
        "related": [
            "skupper-ansible-module-resource",
            "skupper-ansible-module-system",
            "skupper-ansible-module-controller",
            "skupper-ansible-overview",
            "skupper-ansible-workflow-mixed-sites",
        ],
        "decision": {
            "authoring": ["ansible"],
            "platform": ["podman", "docker", "linux"],
            "setupStep": ["identify-sites", "decide-link-access", "join-sites", "validate"],
            "resource": ["site", "listener", "connector", "link"],
        },
    }
    pages["skupper-ansible-workflow-non-kubernetes.md"] = (
        yaml_frontmatter(nonkube_fm)
        + """# Skupper Ansible non-Kubernetes workflow

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
"""
    )

    mixed_fm = {
        **common,
        "type": "Workflow",
        "title": "Skupper Ansible mixed Kubernetes and system workflow",
        "id": "skupper-ansible-workflow-mixed-sites",
        "source_paths": [
            "human/skupper-ansible/README.md",
            "human/skupper-ansible/plugins/modules/resource.py",
            "human/skupper-ansible/plugins/modules/token.py",
            "human/skupper-ansible/plugins/modules/system.py",
        ],
        "related": [
            "skupper-ansible-module-resource",
            "skupper-ansible-module-token",
            "skupper-ansible-module-system",
            "skupper-ansible-workflow-kubernetes",
            "skupper-ansible-workflow-non-kubernetes",
        ],
        "decision": {
            "authoring": ["ansible"],
            "platform": ["kubernetes", "podman", "docker", "linux"],
            "setupStep": ["identify-sites", "decide-link-access", "join-sites", "validate"],
            "resource": ["site", "listener", "connector", "link"],
        },
    }
    pages["skupper-ansible-workflow-mixed-sites.md"] = (
        yaml_frontmatter(mixed_fm)
        + """# Skupper Ansible mixed Kubernetes and system workflow

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
"""
    )

    return pages


def generate(source_repo: Path, output_dir: Path, dry_run: bool) -> str:
    if dry_run:
        log("dry run enabled; no files changed")
        return "dry-run"

    if not source_repo.is_dir():
        die(f"source repository not found: {source_repo} (run sync-human-skupper-ansible.sh first)")

    modules_dir = source_repo / "plugins" / "modules"
    if not modules_dir.is_dir():
        die(f"module directory not found: {modules_dir}")

    module_paths = sorted(modules_dir.glob("*.py"))
    if not module_paths:
        die(f"no Ansible modules found in {modules_dir}")

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    source_record = read_source_record(Path("sources/skupper-ansible.md"))

    output_dir.mkdir(parents=True, exist_ok=True)

    generated: dict[str, str] = {}
    for module_path in module_paths:
        filename, text = render_module_page(module_path, source_repo, source_record, generated_at)
        generated[filename] = text

    generated.update(render_curated_pages(source_record, generated_at))

    for stale in output_dir.glob("*.md"):
        stale.unlink()

    for filename, text in sorted(generated.items()):
        target = output_dir / filename
        target.write_text(text, encoding="utf-8")
        log(f"wrote {target}")

    return "success"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-repo", type=Path, default=DEFAULT_SOURCE_REPO)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without modifying files")
    args = parser.parse_args()

    print(generate(args.source_repo, args.output_dir, args.dry_run))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
