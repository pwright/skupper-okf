#!/usr/bin/env python3
"""Build and validate an evidence-bearing LinkML dataset without changing sources."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

try:
    import yaml
    from jsonschema.validators import validator_for
    from linkml.generators.jsonschemagen import JsonSchemaGenerator
    from linkml_runtime.linkml_model.meta import SchemaDefinition
except ImportError as error:
    raise SystemExit("Install requirements-linkml.txt in .venv-linkml first") from error


PROJECT = Path(__file__).resolve().parents[1]
COLLECTIONS = ("repositories", "documents", "concepts", "evidence", "relationships")


class ModelError(ValueError):
    pass


def mapping(value, label):
    if not isinstance(value, dict):
        raise ModelError(f"{label}: expected a mapping")
    return value


def sequence(value, label):
    if not isinstance(value, list):
        raise ModelError(f"{label}: expected a list")
    return value


def strings(value, label):
    sequence(value, label)
    if any(not isinstance(item, str) or not item for item in value):
        raise ModelError(f"{label}: expected nonempty strings")
    return value


def load(path, markdown=False):
    text = path.read_text(encoding="utf-8")
    if markdown:
        lines = text.splitlines()
        if not lines or lines[0] != "---":
            return {}
        try:
            end = lines.index("---", 1)
        except ValueError as error:
            raise ModelError(f"{path}: unclosed front matter") from error
        text = "\n".join(lines[1:end])
    return mapping(yaml.safe_load(text) or {}, str(path))


def safe_path(root, value):
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ModelError(f"expected a relative path: {value!r}")
    if ".." in Path(value).parts:
        raise ModelError(f"path escape: {value}")
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ModelError(f"path escape: {value}")
    return path


def identifier(prefix, *values):
    return prefix + ":" + hashlib.sha256(
        json.dumps(values, sort_keys=True).encode()
    ).hexdigest()[:24]


def metadata_commit(data):
    if data.get("source_commit") and data.get("commit") and data["source_commit"] != data["commit"]:
        raise ModelError("conflicting commit and source_commit in source metadata")
    return data.get("source_commit") or data.get("commit")


def known_revision(value):
    return isinstance(value, str) and bool(value.strip()) and value.lower() not in {"unknown", "null", "none"}


def schema_json(path):
    # Validate the authored schema against LinkML's metamodel before using it.
    SchemaDefinition(**load(path))
    return json.loads(JsonSchemaGenerator(str(path)).serialize())


def validate_dataset(data, schema, strict=False):
    mapping(data, "dataset")
    validator = validator_for(schema)
    validator.check_schema(schema)
    errors = sorted(validator(schema).iter_errors(data), key=lambda e: str(e.path))
    if errors:
        raise ModelError("schema validation: " + "; ".join(
            f"{'/'.join(map(str, e.path))}: {e.message}" for e in errors
        ))
    groups = {name: {row["id"] for row in data[name]} for name in COLLECTIONS}
    seen = set()
    for name in COLLECTIONS:
        for row in data[name]:
            if row["id"] in seen:
                raise ModelError(f"duplicate identity: {row['id']}")
            seen.add(row["id"])
    entities = groups["repositories"] | groups["documents"] | groups["concepts"]
    for name in COLLECTIONS:
        for row in data[name]:
            for ref in row.get("evidence", []):
                if ref not in groups["evidence"]:
                    raise ModelError(f"dangling evidence reference: {ref}")
            if "repository" in row and row["repository"] not in groups["repositories"]:
                raise ModelError(f"dangling repository reference: {row['repository']}")
            if name == "relationships":
                for key in ("source", "target"):
                    if row[key] not in entities:
                        raise ModelError(f"dangling entity reference: {row[key]}")
            if name in ("documents", "concepts", "relationships") and not row.get("evidence"):
                raise ModelError(f"{row['id']}: evidence must not be empty")
            if name == "evidence" and row["revision_state"] != "unknown":
                declared, snapshot = row.get("declared_commit"), row.get("snapshot_commit")
                if not known_revision(declared) or not known_revision(snapshot) or \
                        ((declared == snapshot) != (row["revision_state"] == "matches")):
                    raise ModelError(f"{row['id']}: inconsistent revision state")
    if strict:
        unresolved = [e["id"] for e in data["evidence"]
                      if e["availability"] != "present" or e["revision_state"] != "matches"]
        unresolved += [r["id"] for r in data["repositories"]
                       if not known_revision(r.get("snapshot_commit")) or
                       r.get("record_commit") != r.get("snapshot_commit")]
        if unresolved:
            raise ModelError(f"unresolved provenance: {', '.join(unresolved)}")


def build(root, config_path, mappings_path):
    config = load(config_path)
    mappings = load(mappings_path)
    data = {name: [] for name in COLLECTIONS}
    diagnostics = []
    roots = []
    documents = {}
    aliases = {}
    frontmatter = {}
    scanned = []
    skipped = []

    def diagnostic(code, path, detail):
        diagnostics.append({"code": code, "path": path, "detail": detail})

    for entry in sequence(config.get("repositories"), "repositories"):
        entry = mapping(entry, "repository configuration")
        repo_id = entry["id"]
        local = safe_path(root, entry["root"])
        if not isinstance(entry.get("required", False), bool):
            raise ModelError("required must be boolean")
        if not local.is_dir():
            if entry.get("required", False):
                raise ModelError(f"missing required root: {entry['root']}")
            diagnostic("missing_root", entry["root"], "optional snapshot is unavailable")
        record_path = safe_path(root, entry["record"]) if entry.get("record") else None
        record = load(record_path, True) if record_path and record_path.exists() else {}
        if record_path and not record_path.exists():
            diagnostic("missing_record", entry["record"], "source record is unavailable")
        snapshot_path = local / "_source.md"
        snapshot = load(snapshot_path, True) if snapshot_path.is_file() else {}
        urls = {str(value).removesuffix(".git").rstrip("/") for value in
                (record.get("repo"), record.get("url"), snapshot.get("source_repo"), snapshot.get("repo"))
                if value}
        if len(urls) > 1:
            diagnostic("repository_mismatch", entry["root"], "conflicting repository URLs: " + ", ".join(sorted(urls)))
        commit = metadata_commit(snapshot)
        if (local / ".git").exists():
            result = subprocess.run(["git", "-C", str(local), "rev-parse", "HEAD"],
                                    capture_output=True, text=True, check=True)
            actual = result.stdout.strip()
            if commit and actual != commit:
                diagnostic("snapshot_mismatch", entry["root"], f"_source.md {commit}; git {actual}")
            commit = actual
        if not local.is_dir():
            commit = None
        repo = {"id": repo_id, "name": repo_id.split(":")[-1], "root": entry["root"]}
        for key, value in (("url", record.get("repo") or record.get("url") or
                            snapshot.get("source_repo") or snapshot.get("repo")),
                           ("record_commit", metadata_commit(record)), ("snapshot_commit", commit)):
            if value is not None:
                repo[key] = value
        if not known_revision(commit):
            diagnostic("unknown_commit", entry["root"], "snapshot revision is unknown")
        if metadata_commit(record) and metadata_commit(record) != commit:
            diagnostic("snapshot_mismatch", entry["root"],
                       f"source record {metadata_commit(record)}; snapshot {commit or 'unknown'}")
        data["repositories"].append(repo)
        roots.append((local, repo))
        for pattern in strings(entry.get("include", []), "include"):
            safe_path(local, pattern)
            matches = sorted(local.glob(pattern))
            if not matches:
                diagnostic("missing_input", str(local.relative_to(root) / pattern), "no selected file")
            for path in matches:
                resolved = safe_path(local, str(path.relative_to(local)))
                rel = str(resolved.relative_to(root))
                if any(part in {".git", "node_modules", "__pycache__"} for part in path.parts) or \
                        resolved.is_relative_to(root / "generated/linkml") or not path.is_file():
                    skipped.append(rel)
                    continue
                if rel in documents:
                    raise ModelError(f"duplicate input: {rel}")
                meta = load(path, True)
                original_id = meta.get("id")
                if original_id is not None and not isinstance(original_id, str):
                    raise ModelError(f"{rel}: id must be a string")
                doc_id = f"doc:{repo_id.removeprefix('repo:')}:{original_id or path.relative_to(local)}"
                doc = {"id": doc_id, "name": meta.get("title") or path.stem,
                       "path": rel, "repository": repo_id, "evidence": []}
                if original_id:
                    if original_id in aliases:
                        raise ModelError(f"duplicate identity: {original_id}")
                    aliases[original_id] = doc_id
                    doc["original_id"] = original_id
                documents[rel] = doc
                frontmatter[rel] = meta
                data["documents"].append(doc)
                scanned.append(rel)

    def evidence(path, method, declared=None, meta=None, locator=None, quote=None):
        target = safe_path(root, path)
        meta = meta or {}
        candidates = [(local, repo) for local, repo in roots if target.is_relative_to(local)]
        owner = max(candidates, key=lambda item: len(item[0].parts))[1] if candidates else None
        snapshot_commit = owner.get("snapshot_commit") if owner else None
        state = "unknown" if not known_revision(declared) or not known_revision(snapshot_commit) else (
            "matches" if declared == snapshot_commit else "mismatch")
        declared_repo = meta.get("source_repo") if method == "source_path" else None
        if declared_repo and owner and owner.get("url") and \
                declared_repo.removesuffix(".git").rstrip("/") != owner["url"].removesuffix(".git").rstrip("/"):
            state = "unknown"
            diagnostic("repository_mismatch", path,
                       f"note declares {declared_repo}; path belongs to {owner['url']}")
        row = {"path": path, "availability": "present" if target.is_file() else "missing",
               "revision_state": state, "method": method}
        if owner:
            row["repository"] = owner["id"]
        for key, value in (("declared_commit", declared), ("snapshot_commit", snapshot_commit),
                           ("locator", locator), ("quote", quote), ("declared_repo", declared_repo),
                           ("declared_branch", meta.get("source_branch") if method == "source_path" else None)):
            if value is not None:
                row[key] = value
        for key in ("status", "reviewed", "confidence"):
            if key in meta:
                row[key] = meta[key]
        row["id"] = identifier("evidence", row)
        if row not in data["evidence"]:
            data["evidence"].append(row)
            if row["availability"] == "missing":
                diagnostic("missing_evidence", path, "referenced source is unavailable")
            if state != "matches":
                diagnostic("revision_" + state, path,
                           f"declared {declared or 'unknown'}; snapshot {snapshot_commit or 'unknown'}")
        return row["id"]

    def relationship(source, target, predicate, refs):
        data["relationships"].append({"id": identifier("relationship", source, predicate, target, refs),
                                      "source": source, "target": target,
                                      "predicate": predicate, "evidence": refs})

    for path, doc in documents.items():
        meta = frontmatter[path]
        repo = next(repo for _, repo in roots if repo["id"] == doc["repository"])
        # A note's upstream commit never describes the revision of the note itself.
        own_commit = repo.get("snapshot_commit")
        doc["evidence"].append(evidence(path, "frontmatter", own_commit, meta))
        for source_path in strings(meta.get("source_paths", []), f"{path}: source_paths"):
            doc["evidence"].append(evidence(source_path, "source_path", meta.get("source_commit"), meta))
        for related in strings(meta.get("related", []), f"{path}: related"):
            if related in aliases:
                relationship(doc["id"], aliases[related], "related_to", [doc["evidence"][0]])
            else:
                diagnostic("unresolved_link", path, related + " is outside the selected dataset")

    for concept in sequence(mappings.get("concepts"), "concepts"):
        concept = mapping(concept, "concept")
        refs = []
        for path in strings(concept.get("documents"), "concept documents"):
            safe_path(root, path)
            if path not in documents:
                raise ModelError(f"mapping references an unselected document: {path}")
            refs.extend(documents[path]["evidence"])
            relationship(documents[path]["id"], concept["id"], "documents", documents[path]["evidence"])
        data["concepts"].append({"id": concept["id"], "name": concept["name"],
                                  "evidence": sorted(set(refs))})
    for assertion in sequence(mappings.get("assertions", []), "assertions"):
        assertion = mapping(assertion, "assertion")
        path = assertion["path"]
        target = safe_path(root, path)
        if path not in documents:
            raise ModelError(f"assertion references an unselected document: {path}")
        if not assertion.get("locator") or not assertion.get("quote"):
            raise ModelError("assertions require a locator and supporting quote")
        if target.is_file():
            text = target.read_text(encoding="utf-8")
            if assertion["locator"] not in text or assertion["quote"] not in text:
                raise ModelError(f"assertion evidence no longer matches: {path}")
        repo = next(repo for _, repo in roots if repo["id"] == documents[path]["repository"])
        # For generated notes, take their declared source revision, never a fresh upstream one.
        declared = frontmatter[path].get("source_commit") if path.startswith("generated/") else repo.get("snapshot_commit")
        ref = evidence(path, "maintained_mapping", declared, assertion,
                       assertion["locator"], assertion["quote"])
        relationship(assertion["source"], assertion["target"], assertion["predicate"], [ref])
    for name in COLLECTIONS:
        data[name].sort(key=lambda row: row["id"])
    report = {"counts": {name: len(data[name]) for name in COLLECTIONS},
              "scanned": sorted(scanned), "skipped": sorted(skipped),
              "diagnostics": sorted(diagnostics, key=lambda row: (row["code"], row["path"], row["detail"]))}
    return data, report


def report_markdown(data, report):
    lines = ["# LinkML pilot report", "", "## Concept traceability", ""]
    evidence = {row["id"]: row for row in data["evidence"]}
    for concept in data["concepts"]:
        lines += [f"### {concept['name']}", ""]
        for ref in concept["evidence"]:
            row = evidence[ref]
            lines.append(f"- `{row['path']}`: {row['method']}; {row['availability']}; revision {row['revision_state']}")
        lines.append("")
    lines += ["## Semantic assertions", ""]
    for relation in data["relationships"]:
        if relation["predicate"] == "uses":
            lines.append(f"- `{relation['source']}` uses `{relation['target']}`")
            for ref in relation["evidence"]:
                row = evidence[ref]
                lines.append(f"  - `{row['path']}` at `{row.get('locator', '')}`; reviewed: {row.get('reviewed', 'unknown')}")
    lines += ["", "## Coverage", "", json.dumps(report["counts"], sort_keys=True), "", "## Diagnostics", ""]
    lines += [f"- **{row['code']}** `{row['path']}`: {row['detail']}" for row in report["diagnostics"]]
    return "\n".join(lines) + "\n"


def write_outputs(outputs):
    # Stage all content before replacing any previous artifact.
    staged = []
    try:
        for path, content in outputs:
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                             delete=False) as handle:
                handle.write(content)
                staged.append((Path(handle.name), path))
        for temporary, path in staged:
            os.replace(temporary, path)
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "validate"])
    parser.add_argument("--root", type=Path, default=PROJECT)
    parser.add_argument("--config", default="model/linkml/sources.yaml")
    parser.add_argument("--mappings", default="model/linkml/mappings.yaml")
    parser.add_argument("--schema", type=Path, default=PROJECT / "model/linkml/architecture.yaml")
    parser.add_argument("--output", default="generated/linkml")
    parser.add_argument("--report", default="indexes/linkml-report")
    parser.add_argument("--data", default="generated/linkml/architecture.yaml")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        schema = schema_json(args.schema)
        if args.command == "validate":
            data = load(safe_path(root, args.data))
            validate_dataset(data, schema, args.strict)
        else:
            data, report = build(root, safe_path(root, args.config), safe_path(root, args.mappings))
            validate_dataset(data, schema, args.strict)
            output = safe_path(root, args.output)
            report_path = safe_path(root, args.report)
            # Keep outputs within disposable trees, even with alternate arguments.
            if not output.is_relative_to(root / "generated") or not report_path.is_relative_to(root / "indexes"):
                raise ModelError("output must be under generated/ and report under indexes/")
            outputs = [(output / "architecture.yaml", yaml.safe_dump(data, sort_keys=False)),
                       (output / "architecture.schema.json", json.dumps(schema, indent=2, sort_keys=True) + "\n"),
                       (Path(str(report_path) + ".json"), json.dumps(report, indent=2, sort_keys=True) + "\n"),
                       (Path(str(report_path) + ".md"), report_markdown(data, report))]
            if not args.dry_run:
                write_outputs(outputs)
            print(json.dumps(report["counts"], sort_keys=True), file=sys.stderr)
        print("dry-run" if args.dry_run else "success")
    except (ModelError, OSError, ValueError, KeyError, TypeError, yaml.YAMLError,
            subprocess.CalledProcessError) as error:
        print(f"linkml-model: ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
