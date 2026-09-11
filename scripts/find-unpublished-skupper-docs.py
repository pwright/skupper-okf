#!/usr/bin/env python3
"""Find Markdown files in human/skupper-docs that MkDocs does not publish."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - depends on local environment
    raise SystemExit("PyYAML is required: python3 -m pip install pyyaml") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare all Markdown files under human/skupper-docs with the pages "
            "reachable through mkdocs.yml, then print unpublished files."
        )
    )
    parser.add_argument(
        "--docs-root",
        type=Path,
        default=Path("human/skupper-docs"),
        help="MkDocs project root (default: human/skupper-docs)",
    )
    parser.add_argument(
        "--mkdocs-yml",
        type=Path,
        help="Path to mkdocs.yml (default: <docs-root>/mkdocs.yml)",
    )
    parser.add_argument(
        "--docs-dir-only",
        action="store_true",
        help="Only check Markdown files inside the effective MkDocs docs_dir.",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def resolve_docs_dir(docs_root: Path, configured_docs_dir: str) -> Path:
    docs_dir = docs_root / configured_docs_dir
    if docs_dir.exists():
        return docs_dir

    fallback = docs_root / "input"
    if configured_docs_dir == "doc-input" and fallback.exists():
        print(
            f"warning: {docs_dir} does not exist; using {fallback} instead",
            file=sys.stderr,
        )
        return fallback

    raise SystemExit(f"Docs directory not found: {docs_dir}")


def normalize_nav_path(value: str) -> str:
    return value.split("#", 1)[0].strip("/")


def resolve_nav_target(docs_dir: Path, base_dir: Path, value: str) -> tuple[Path, Path]:
    rel_path = base_dir / normalize_nav_path(value)
    full_path = docs_dir / rel_path
    return rel_path, full_path


def read_pages_nav(dir_path: Path) -> list[Any] | None:
    pages_file = dir_path / ".pages"
    if not pages_file.exists():
        return None

    data = load_yaml(pages_file) or {}
    return data.get("nav")


def collect_directory_pages(docs_dir: Path, rel_dir: Path, published: set[Path]) -> None:
    directory = docs_dir / rel_dir
    pages_nav = read_pages_nav(directory)

    if pages_nav:
        for item in pages_nav:
            collect_nav_pages(item, docs_dir, rel_dir, published)
        return

    for path in sorted(directory.rglob("*.md")):
        published.add(path.relative_to(docs_dir))


def collect_remaining_pages(docs_dir: Path, published: set[Path]) -> None:
    for path in sorted(docs_dir.rglob("*.md")):
        rel_path = path.relative_to(docs_dir)
        if rel_path not in published:
            published.add(rel_path)


def collect_nav_pages(item: Any, docs_dir: Path, base_dir: Path, published: set[Path]) -> None:
    if isinstance(item, str):
        if item == "...":
            collect_remaining_pages(docs_dir, published)
            return

        rel_path, full_path = resolve_nav_target(docs_dir, base_dir, item)
        if full_path.is_dir():
            collect_directory_pages(docs_dir, rel_path, published)
        elif full_path.exists() and full_path.suffix == ".md":
            published.add(rel_path)
        else:
            print(f"warning: nav target not found: {item}", file=sys.stderr)
        return

    if isinstance(item, dict):
        for value in item.values():
            if isinstance(value, str):
                rel_path, full_path = resolve_nav_target(docs_dir, base_dir, value)
                if full_path.is_dir():
                    collect_directory_pages(docs_dir, rel_path, published)
                elif full_path.exists() and full_path.suffix == ".md":
                    published.add(rel_path)
                else:
                    print(f"warning: nav target not found: {value}", file=sys.stderr)
            elif isinstance(value, list):
                for child in value:
                    collect_nav_pages(child, docs_dir, base_dir, published)


def markdown_files(root: Path) -> set[Path]:
    return {path for path in root.rglob("*.md") if path.is_file()}


def main() -> None:
    args = parse_args()
    docs_root = args.docs_root
    mkdocs_yml = args.mkdocs_yml or docs_root / "mkdocs.yml"
    config = load_yaml(mkdocs_yml)
    docs_dir = resolve_docs_dir(docs_root, config.get("docs_dir", "docs"))

    published: set[Path] = set()
    for item in config.get("nav", []):
        collect_nav_pages(item, docs_dir, Path(), published)

    published_abs = {(docs_dir / path).resolve() for path in published}
    search_root = docs_dir if args.docs_dir_only else docs_root
    unpublished = [
        path
        for path in sorted(markdown_files(search_root))
        if path.resolve() not in published_abs
    ]

    for path in unpublished:
        print(path.relative_to(docs_root))


if __name__ == "__main__":
    main()
