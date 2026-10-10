#!/usr/bin/env python3
"""Recreate Markdown files from schema-validated document JSON Lines."""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "markdown-document.schema.json"
MODULES = ROOT / "tools" / "mq"


def command_json(command, content):
    result = subprocess.run(command, input=content, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def frontmatter_text(frontmatter):
    """Use the preserved source header; detect stale edits to its parsed data."""
    raw = frontmatter["raw"]
    nodes = command_json(["mq", "-I", "markdown", "-F", "json", "self"], raw)
    expected = {"yaml": "Yaml", "toml": "Toml"}[frontmatter["format"]]
    if len(nodes) != 1 or nodes[0]["type"] != expected:
        raise ValueError("frontmatter.raw must contain only a complete header matching its format")
    data = command_json([
        "mq", "-I", frontmatter["format"], "-F", "json", "self",
    ], nodes[0]["value"])
    if data != frontmatter["data"]:
        raise ValueError("frontmatter.raw and frontmatter.data disagree; update both before generating")
    return raw


def heading_text(section):
    heading = section["heading"]
    level = int(section["level"])
    if "\n" in heading or "\r" in heading:
        if level not in (1, 2):
            raise ValueError("multiline headings can only be represented at levels 1 and 2")
        return heading + "\n" + ("=" if level == 1 else "-") * 3
    if not heading:
        return "#" * level
    # A final literal hash must not become an ATX closing marker.
    closing_marker = " #" if re.search(r"(^|[ \t])#+$", heading) else ""
    return "#" * level + " " + heading + closing_marker


def body_parts(children, parent_level=0):
    saw_section = False
    for child in children:
        if child["type"] == "section":
            saw_section = True
            if child["level"] <= parent_level:
                raise ValueError("a nested section must have a higher heading level than its parent")
            yield heading_text(child)
            yield from body_parts(child["children"], child["level"])
        else:
            if saw_section:
                raise ValueError("a block after a child section cannot retain its parent in Markdown")
            yield child["markdown"]


def render_document(document):
    body = "\n\n".join(body_parts(document["children"]))
    header = frontmatter_text(document["frontmatter"]) if "frontmatter" in document else ""
    if not body:
        return header
    if header:
        separator = "\n" if header.endswith(("\n", "\r")) else "\n\n"
        return header + separator + body + "\n"
    return body + "\n"


def output_path(output_dir, document):
    relative = PurePosixPath(document["path"])
    if (
        relative.is_absolute() or ".." in relative.parts or "\\" in document["path"]
        or document["path"] != relative.as_posix()
        or relative.name != document["filename"] or relative.suffix.lower() != ".md"
    ):
        raise ValueError(f"invalid Markdown output path or filename: {document['path']}")
    target = output_dir.joinpath(*relative.parts)
    if target.is_symlink() or not target.resolve().is_relative_to(output_dir):
        raise ValueError(f"output path escapes the output directory: {document['path']}")
    return target


def generate(input_file, output_dir, overwrite=False):
    output_dir = output_dir.resolve()
    if output_dir.exists() and not output_dir.is_dir():
        raise ValueError(f"not an output directory: {output_dir}")
    schema = SCHEMA.read_text(encoding="utf-8")
    validation_command = [
        "mq", "-I", "json", "-F", "json", "-L", str(MODULES),
        'import "jsonschema" | jsonschema::validate(self, schema)',
        "--argjson", "schema", schema,
    ]
    outputs = []
    seen = set()
    with input_file.open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            try:
                document = json.loads(line)
                errors = command_json(validation_command, line)
                if errors:
                    raise ValueError(f"schema validation failed: {json.dumps(errors)}")
                target = output_path(output_dir, document)
                if target in seen:
                    raise ValueError(f"duplicate document path: {document['path']}")
                seen.add(target)
                if target.exists() and (not overwrite or not target.is_file()):
                    raise ValueError(f"output exists: {target} (use --overwrite to replace regular files)")
                for parent in target.parents:
                    if parent.exists() and not parent.is_dir():
                        raise ValueError(f"output parent is not a directory: {parent}")
                    if parent == output_dir:
                        break
                outputs.append((target, render_document(document)))
            except ValueError as error:
                raise ValueError(f"{input_file}:{line_number}: {error}") from error
            if len(outputs) % 50 == 0:
                print(f"Validated {len(outputs)} documents", file=sys.stderr)
    # Validate every input and output path before writing any document.
    for target, markdown in outputs:
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", encoding="utf-8", newline="", dir=target.parent, delete=False,
            ) as destination:
                temporary = Path(destination.name)
                destination.write(markdown)
            temporary.replace(target)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
    print(f"Wrote {len(outputs)} Markdown documents under {output_dir}", file=sys.stderr)
    return len(outputs)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="document JSON Lines report")
    parser.add_argument("output_directory", type=Path, help="root directory for recreated repository-relative paths")
    parser.add_argument("--overwrite", action="store_true", help="replace existing regular Markdown files")
    args = parser.parse_args()
    try:
        generate(args.input, args.output_directory, args.overwrite)
    except subprocess.CalledProcessError as error:
        parser.error(error.stderr or f"command failed: {error.cmd}")
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
