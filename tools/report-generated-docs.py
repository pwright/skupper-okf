#!/usr/bin/env python3
"""Export Markdown documents as JSON Lines, validated with jsonschema.mq."""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "markdown-document.schema.json"
MODULES = ROOT / "tools" / "mq"
KINDS = {
    "Heading": "section",
    "Code": "code",
    "List": "list",
    "TableCell": "table",
    "TableAlign": "table",
    "Blockquote": "blockquote",
    "HorizontalRule": "thematicBreak",
    "Html": "html",
}
INLINE_TYPES = {
    "Text", "Strong", "Emphasis", "Delete", "CodeInline", "Link", "Image",
    "Break", "FootnoteReference", "LinkReference", "ImageReference",
    "Definition", "FootnoteDefinition", "Math", "MathInline", "Embed",
    "LinkRef", "ImageRef", "FootnoteRef",
}


def command_json(command, content):
    result = subprocess.run(command, input=content, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def node_range(node):
    """mq flattens list items and table cells; ranges retain their source syntax."""
    position = node["position"]
    start = position["start"]["line"] - 1
    end = position["end"]["line"]
    if position["end"]["column"] == 1 and end > start + 1:
        end -= 1
    return start, end


def blocks(source, nodes):
    """Collect mq's inline nodes, list items, and table cells into source blocks."""
    lines = source.splitlines(keepends=True)
    groups = []
    for node in nodes:
        start, end = node_range(node)
        node_type = node["type"]
        if node_type in ("Yaml", "Toml"):
            groups.append({"kind": "frontmatter", "start": start, "end": end, "node": node})
            continue
        if node_type not in KINDS and node_type not in INLINE_TYPES:
            raise ValueError(f"unsupported mq node type: {node_type}")
        kind = KINDS.get(node_type, "paragraph")
        if groups:
            previous = groups[-1]
            # mq emits soft newlines between inline HTML tags as Text nodes.
            # Keep an HTML-only run together rather than splitting its kind
            # according to whitespace tokens that disappear on regeneration.
            if node_type == "Text" and not node["value"].strip() and previous["kind"] == "html":
                kind = "html"
            same_line = start < previous["end"]
            adjacent_paragraph = (
                kind == previous["kind"] == "paragraph"
                and not any(not line.strip() for line in lines[previous["end"]:start])
            )
            same_list = (
                kind == previous["kind"] == "list"
                and (node.get("level", 0) > 0 or node.get("index", 0) > 0)
            )
            same_table = (
                kind == previous["kind"] == "table"
                and not (node_type == "TableCell" and node["row"] == node["column"] == 0)
            )
            adjacent_html = (
                kind == previous["kind"] == "html"
                and not any(not line.strip() for line in lines[previous["end"]:start])
            )
            if same_line or adjacent_paragraph or same_list or same_table or adjacent_html:
                previous["end"] = max(previous["end"], end)
                if (
                    same_line
                    and previous["kind"] in ("paragraph", "html")
                    and kind in ("paragraph", "html")
                    and "paragraph" in (previous["kind"], kind)
                ):
                    previous["kind"] = "paragraph"
                continue
        groups.append({"kind": kind, "start": start, "end": end, "node": node})

    cursor = 0
    for group in groups:
        # Keep source constructs omitted from mq's flattened output, such as
        # reference definitions, rather than silently dropping their Markdown.
        gap = "".join(lines[cursor:group["start"]]).strip("\r\n")
        if gap.strip():
            yield {"kind": "paragraph", "markdown": gap}
        cursor = group["end"]
        if group["kind"] == "frontmatter":
            continue
        markdown = "".join(lines[group["start"]:group["end"]]).rstrip("\r\n")
        yield {"kind": group["kind"], "markdown": markdown, "node": group["node"]}
    tail = "".join(lines[cursor:]).strip("\r\n")
    if tail.strip():
        yield {"kind": "paragraph", "markdown": tail}


def heading_content(markdown):
    lines = markdown.splitlines()
    if re.match(r"^ {0,3}#{1,6}(?:[ \t]|$)", lines[0]):
        value = re.sub(r"^ {0,3}#{1,6}", "", lines[0])
        return re.sub(r"[ \t]+#+[ \t]*$", "", value).strip()
    # Setext heading: the final underline is syntax, not heading content.
    return "\n".join(lines[:-1]).strip()


def frontmatter_model(source, nodes):
    lines = source.splitlines(keepends=True)
    for node in nodes:
        if node["type"] not in ("Yaml", "Toml"):
            continue
        start, end = node_range(node)
        format_name = {"Yaml": "yaml", "Toml": "toml"}[node["type"]]
        data = command_json(
            ["mq", "-I", format_name, "-F", "json", "self"], node["value"],
        )
        return {"format": format_name, "raw": "".join(lines[start:end]), "data": data}
    return None


def document_model(path, repo, commit):
    with path.open(encoding="utf-8", newline="") as source_file:
        source = source_file.read()
    nodes = command_json(["mq", "-I", "markdown", "-F", "json", "self"], source)
    relative = path.relative_to(repo).as_posix()
    document_id = "document:" + relative
    document = {
        "type": "document", "id": document_id, "path": relative,
        "filename": path.name, "git_commit": commit, "children": [],
    }
    frontmatter = frontmatter_model(source, nodes)
    if frontmatter is not None:
        document["frontmatter"] = frontmatter
    sections = [document]
    for index, block in enumerate(blocks(source, nodes), start=1):
        node_id = f"{document_id}#node-{index}"
        if block["kind"] == "section":
            level = block["node"]["depth"]
            while len(sections) > 1 and sections[-1]["level"] >= level:
                sections.pop()
            section = {
                "type": "section", "id": node_id,
                "heading": heading_content(block["markdown"]), "level": level,
                "children": [],
            }
            sections[-1]["children"].append(section)
            sections.append(section)
        else:
            sections[-1]["children"].append({
                "type": "block", "id": node_id, "kind": block["kind"],
                "markdown": block["markdown"],
            })
    return document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="directory tree containing Markdown files in a Git repository")
    parser.add_argument(
        "--output", type=Path, default=ROOT / "reports" / "generated-docs.jsonl",
        help="JSON Lines output path (default: reports/generated-docs.jsonl)",
    )
    args = parser.parse_args()
    docs_dir = args.directory.resolve()
    if not docs_dir.is_dir():
        parser.error(f"not a directory: {args.directory}")

    temporary = None
    try:
        repo = Path(subprocess.check_output(
            ["git", "-C", str(docs_dir), "rev-parse", "--show-toplevel"], text=True,
        ).strip()).resolve()
        commit = subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True,
        ).strip()
        schema = SCHEMA.read_text(encoding="utf-8")
        validation_command = [
            "mq", "-I", "json", "-F", "json", "-L", str(MODULES),
            'import "jsonschema" | jsonschema::validate(self, schema)',
            "--argjson", "schema", schema,
        ]
        docs = sorted(docs_dir.rglob("*.md"))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=args.output.parent, delete=False,
        ) as output:
            temporary = Path(output.name)
            for index, path in enumerate(docs, start=1):
                if path.is_symlink():
                    raise ValueError(f"symlink source is unsupported: {path}")
                document = document_model(path, repo, commit)
                serialized = json.dumps(document, ensure_ascii=False)
                errors = command_json(validation_command, serialized)
                if errors:
                    raise ValueError(f"schema validation failed for {path}: {json.dumps(errors)}")
                output.write(serialized + "\n")
                if index % 50 == 0:
                    print(f"Validated {index}/{len(docs)} documents", file=sys.stderr)
        temporary.replace(args.output)
        temporary = None
        print(f"Wrote {args.output} ({len(docs)} schema-valid documents)", file=sys.stderr)
    except subprocess.CalledProcessError as error:
        parser.error(error.stderr or f"command failed: {error.cmd}")
    except (OSError, ValueError) as error:
        parser.error(str(error))
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
