#!/usr/bin/env python3
"""List headings users can encounter in the Skupper MkDocs site."""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - depends on local environment
    raise SystemExit("PyYAML is required: python3 -m pip install pyyaml") from exc


ATX_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
HTML_HEADING = re.compile(r"<h([1-6])\b[^>]*>(.*?)</h\1>", re.IGNORECASE)
TAG = re.compile(r"<[^>]+>")


@dataclass
class Bullet:
    text: str
    children: list["Bullet"] = field(default_factory=list)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Read human/skupper-docs/mkdocs.yml and emit a bulleted outline of "
            "MkDocs navigation entries plus headings from reachable Markdown pages."
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
        "--headings-only",
        action="store_true",
        help="Do not include MkDocs navigation labels, only page headings.",
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


def clean_heading(value: str) -> str:
    value = TAG.sub("", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "")
    return html.unescape(value).strip()


def strip_frontmatter(lines: list[str]) -> list[str]:
    if not lines or lines[0].strip() != "---":
        return lines

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return lines[index + 1 :]

    return lines


def extract_headings(path: Path) -> list[Bullet]:
    lines = strip_frontmatter(path.read_text(encoding="utf-8").splitlines())
    headings: list[tuple[int, str]] = []
    in_fence = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue

        if in_fence:
            continue

        atx_match = ATX_HEADING.match(line)
        if atx_match:
            headings.append((len(atx_match.group(1)), clean_heading(atx_match.group(2))))
            continue

        for html_match in HTML_HEADING.finditer(line):
            headings.append((int(html_match.group(1)), clean_heading(html_match.group(2))))

    return nest_headings([(level, text) for level, text in headings if text])


def nest_headings(headings: list[tuple[int, str]]) -> list[Bullet]:
    root: list[Bullet] = []
    stack: list[tuple[int, Bullet]] = []

    for level, text in headings:
        bullet = Bullet(text)
        while stack and stack[-1][0] >= level:
            stack.pop()

        if stack:
            stack[-1][1].children.append(bullet)
        else:
            root.append(bullet)

        stack.append((level, bullet))

    return root


def page_bullet(label: str, path: Path, headings_only: bool) -> Bullet | list[Bullet]:
    headings = extract_headings(path)
    if headings_only:
        return headings
    return Bullet(label, headings)


def normalize_nav_path(value: str) -> str:
    return value.split("#", 1)[0].strip("/")


def resolve_nav_target(docs_dir: Path, base_dir: Path, value: str) -> tuple[Path, Path]:
    rel_path = base_dir / normalize_nav_path(value)
    full_path = docs_dir / rel_path
    return rel_path, full_path


def read_pages_nav(dir_path: Path) -> tuple[str | None, list[Any] | None]:
    pages_file = dir_path / ".pages"
    if not pages_file.exists():
        return None, None

    data = load_yaml(pages_file) or {}
    return data.get("title"), data.get("nav")


def directory_label(dir_path: Path) -> str:
    pages_title, _ = read_pages_nav(dir_path)
    if pages_title:
        return str(pages_title)
    return dir_path.name.replace("-", " ").title()


def expand_directory(
    docs_dir: Path,
    rel_dir: Path,
    visited: set[Path],
    headings_only: bool,
) -> list[Bullet]:
    directory = docs_dir / rel_dir
    _, pages_nav = read_pages_nav(directory)
    bullets: list[Bullet] = []

    if pages_nav:
        for item in pages_nav:
            bullets.extend(expand_nav_item(item, docs_dir, rel_dir, visited, headings_only))
        return bullets

    entries = sorted(directory.iterdir(), key=lambda path: (path.is_file(), path.name))
    index_file = directory / "index.md"
    if index_file.exists():
        entries = [index_file] + [entry for entry in entries if entry != index_file]

    for entry in entries:
        if entry.name.startswith("."):
            continue
        if entry.is_dir():
            children = expand_directory(docs_dir, entry.relative_to(docs_dir), visited, headings_only)
            if children and not headings_only:
                bullets.append(Bullet(directory_label(entry), children))
            else:
                bullets.extend(children)
        elif entry.suffix == ".md":
            rel_path = entry.relative_to(docs_dir)
            visited.add(rel_path)
            expanded = page_bullet(entry.stem.replace("-", " ").title(), entry, headings_only)
            bullets.extend(expanded if isinstance(expanded, list) else [expanded])

    return bullets


def expand_nav_item(
    item: Any,
    docs_dir: Path,
    base_dir: Path,
    visited: set[Path],
    headings_only: bool,
) -> list[Bullet]:
    if isinstance(item, str):
        if item == "...":
            return expand_remaining(docs_dir, visited, headings_only)

        rel_path, full_path = resolve_nav_target(docs_dir, base_dir, item)
        if full_path.is_dir():
            return expand_directory(docs_dir, rel_path, visited, headings_only)
        if full_path.exists():
            visited.add(rel_path)
            expanded = page_bullet(full_path.stem.replace("-", " ").title(), full_path, headings_only)
            return expanded if isinstance(expanded, list) else [expanded]
        print(f"warning: nav target not found: {item}", file=sys.stderr)
        return []

    if isinstance(item, dict):
        bullets: list[Bullet] = []
        for label, value in item.items():
            if isinstance(value, str):
                rel_path, full_path = resolve_nav_target(docs_dir, base_dir, value)
                if full_path.is_dir():
                    children = expand_directory(docs_dir, rel_path, visited, headings_only)
                    if headings_only:
                        bullets.extend(children)
                    else:
                        bullets.append(Bullet(str(label), children))
                elif full_path.exists():
                    visited.add(rel_path)
                    expanded = page_bullet(str(label), full_path, headings_only)
                    bullets.extend(expanded if isinstance(expanded, list) else [expanded])
                else:
                    print(f"warning: nav target not found: {value}", file=sys.stderr)
            elif isinstance(value, list):
                children: list[Bullet] = []
                for child in value:
                    children.extend(expand_nav_item(child, docs_dir, base_dir, visited, headings_only))
                if headings_only:
                    bullets.extend(children)
                else:
                    bullets.append(Bullet(str(label), children))
        return bullets

    return []


def expand_remaining(docs_dir: Path, visited: set[Path], headings_only: bool) -> list[Bullet]:
    bullets: list[Bullet] = []
    top_level = sorted(docs_dir.iterdir(), key=lambda path: (path.is_file(), path.name))

    for entry in top_level:
        if entry.name.startswith("."):
            continue
        if entry.is_dir():
            remaining = [
                path.relative_to(docs_dir)
                for path in sorted(entry.rglob("*.md"))
                if path.relative_to(docs_dir) not in visited
            ]
            if not remaining:
                continue
            children = expand_directory(docs_dir, entry.relative_to(docs_dir), visited, headings_only)
            if children and not headings_only:
                bullets.append(Bullet(directory_label(entry), children))
            else:
                bullets.extend(children)
        elif entry.suffix == ".md":
            rel_path = entry.relative_to(docs_dir)
            if rel_path in visited:
                continue
            visited.add(rel_path)
            expanded = page_bullet(entry.stem.replace("-", " ").title(), entry, headings_only)
            bullets.extend(expanded if isinstance(expanded, list) else [expanded])

    return bullets


def print_bullets(bullets: list[Bullet], indent: int = 0) -> None:
    for bullet in bullets:
        print(f"{'  ' * indent}- {bullet.text}")
        print_bullets(bullet.children, indent + 1)


def main() -> None:
    args = parse_args()
    docs_root = args.docs_root
    mkdocs_yml = args.mkdocs_yml or docs_root / "mkdocs.yml"
    config = load_yaml(mkdocs_yml)
    docs_dir = resolve_docs_dir(docs_root, config.get("docs_dir", "docs"))

    visited: set[Path] = set()
    bullets: list[Bullet] = []
    for item in config.get("nav", []):
        bullets.extend(expand_nav_item(item, docs_dir, Path(), visited, args.headings_only))

    print_bullets(bullets)


if __name__ == "__main__":
    main()
