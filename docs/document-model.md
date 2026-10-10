# Markdown document export

Run `just report-generated-docs` to export every `*.md` file under `generated/`
to `reports/generated-docs.jsonl`. Each line is a complete document object
matching [the document schema](../schemas/markdown-document.schema.json).

To recreate Markdown from the report, see [round trips](#recreate-markdown-from-a-report).

To process another directory in a Git repository:

```bash
python3 tools/report-generated-docs.py path/to/docs --output reports/docs.jsonl
```

The exporter requires Python 3.9+, Git, and `mq` (developed with mq 0.9.2).
It uses mq's Markdown parser and validates each document with the vendored
`harehare/jsonschema.mq` module before replacing the output file. No network
access is needed when exporting. Progress is written to stderr.

The schema extends the supplied document model with required file metadata:

| Field | Meaning |
| --- | --- |
| `path` | Source file path relative to its Git repository root, using `/` separators |
| `filename` | Basename including the Markdown extension |
| `git_commit` | Full repository HEAD hash at the start of the export |
| `frontmatter` | Optional source metadata with its format, original text, and parsed data |

Content is read from the working tree, so it can include uncommitted changes.
`git_commit` records the repository revision used as context; it does not claim
that the content matches the committed version of the file.

Sections nest beneath the nearest preceding heading with a lower level.
Content before the first heading is stored directly in the document's children.
Headings retain inline Markdown, and blocks retain their original source syntax.
Lists and tables are complete blocks rather than individual items or cells.
YAML/TOML front matter is stored on the document, separate from body children.
Reference definitions and wiki embeds are retained as
paragraph blocks. Blank lines separating blocks are not represented as nodes.

IDs use the repository-relative path and a source-order node number. They are
deterministic for unchanged documents; inserting a block changes subsequent
node numbers. The schema enforces nonempty IDs, while the exporter assigns
unique IDs within each document.

## Front matter representation

Documents with front matter contain a `frontmatter` object:

```json
{
  "format": "yaml",
  "raw": "---\ntitle: Example\nreviewed: false\ntags: [skupper]\n---\n",
  "data": {
    "title": "Example",
    "reviewed": false,
    "tags": ["skupper"]
  }
}
```

`format` is `yaml` for `---` delimiters or `toml` for `+++` delimiters.
`raw` retains delimiters, comments, quoting, and original line endings.
`data` is parsed by mq's YAML/TOML module and preserves arbitrary keys and
nested JSON values. Existing fields such as `type`, `id`, `source`,
`generated_by`, `reviewed`, `confidence`, `tags`, and `timestamp` remain under
`data`; they do not override the export's document fields. An empty YAML header
has `data: null`. Documents without front matter omit `frontmatter`.

The schema validates the wrapper's shape while leaving source metadata keys
unrestricted. Typed JSON values cannot preserve comments, quotes, or every
YAML/TOML-specific type; `raw` preserves the source representation.

## Changing document front matter

1. Find the source Markdown file using the exported `path`. For generated
   pages, inspect `generated_by` or `source_path` to identify the generator or
   source template that owns the header. Change that generator or template
   and rerun it so the edit survives regeneration. For a manually maintained
   draft, edit its header in `generated/` directly. Upstream snapshots under
   `human/` are read-only.
2. Add or edit keys between the existing delimiters. Preserve source provenance
   and unrelated metadata. Keep intended value types: for example,
   `reviewed: false` is a boolean and `tags: [skupper]` is an array. Changing
   front matter's `id` changes `frontmatter.data.id`; the exported document ID
   continues to derive from its repository-relative path.
3. Rerun the owning generator if applicable (`just maps` regenerates map pages),
   then run `just report-generated-docs`. The export reparses front matter and
   validates all document models before replacing the report. Invalid YAML or
   TOML stops the export and leaves the previous report intact.
4. Inspect `frontmatter.raw` and `frontmatter.data` in the exported document.
   They are derived output; apply corrections in the Markdown or generator.
   If publishing these changes through Quartz, run `just quartz-stage`.

Adding a source metadata key does not require a schema change. To change the
exported front matter representation or introduce constraints on `data`, update
`definitions.frontmatter` in the schema, the exporter, this documentation, and
the integration checks together. Check existing metadata before adding required
keys or restricting value types. Verify and regenerate with:

```bash
python3 -m unittest discover -s tests -p 'test_document_model.py'
just report-generated-docs
```

## Exporting the human Skupper documentation snapshot

To export all Markdown in the copied upstream repository, including tooling
and bundled library documentation:

```bash
python3 tools/report-generated-docs.py human/skupper-docs --output reports/human-skupper-docs.jsonl
```

To export the site content under `input/`:

```bash
python3 tools/report-generated-docs.py human/skupper-docs/input --output reports/skupper-docs-input.jsonl
```

Both commands read the snapshot and write a separate report. Only `*.md` files
are processed; reStructuredText and configuration files are outside this model.
HTML anchors and content-type comments are retained as HTML blocks. Front
matter is optional, so pages without a header still produce valid documents.

The sync script excludes upstream `.git`, so these exports record the enclosing
`skupper-okf` repository's HEAD in `git_commit`, with paths such as
`human/skupper-docs/input/index.md`. The upstream repository URL and source
revision are recorded in `human/skupper-docs/_source.md`; a full snapshot export
includes these in that document's `frontmatter.data`. They are not automatically
inherited by every exported page, and an `input/`-only export does not include
`_source.md`. Use the snapshot record when interpreting upstream provenance.

## Recreate Markdown from a report

```bash
python3 tools/generate-docs.py reports/generated-docs.jsonl output-dir/
# Or:
just generate-docs reports/generated-docs.jsonl output-dir/
```

Each document is written to `output-dir/<path>`. For example,
`generated/vms/out-of-band-bootstrap.md` becomes
`output-dir/generated/vms/out-of-band-bootstrap.md`. A report of the human
snapshot recreates files beneath `output-dir/human/skupper-docs/`. Choose a
separate output directory for restored copies of upstream snapshots.

The generator validates every JSONL record with `jsonschema.mq`, checks all
output paths, and renders all documents before writing files. Duplicate paths,
paths that escape the output directory, and mismatched filenames are rejected.
Existing files are preserved unless `--overwrite` is explicitly supplied:

```bash
python3 tools/generate-docs.py reports/generated-docs.jsonl output-dir/ --overwrite
```

Blocks retain their stored Markdown, and front matter is copied from `raw`.
The generator checks that `raw` parses to the supplied `data`; if you edit
front matter in JSONL, update both representations consistently. The export's
`id`, `path`, `filename`, and `git_commit` are bookkeeping fields and are not
added to the recreated Markdown header.

This is a document-model round trip. The report does not retain heading styles,
blank lines between nodes, leading/trailing blank lines, or whether the original
file ended with a newline, so regenerated files need not match their original
bytes. The generator uses ATX headings (Setext for multiline level 1/2 headings),
blank lines between body nodes, and a final body newline. Raw front matter and
Markdown inside each block remain preserved.

If you edit the section tree, preserve Markdown's heading hierarchy: nested
sections must have higher levels than their parent, and a parent's blocks must
precede its child sections. Otherwise the generator rejects a tree that cannot
be represented faithfully as Markdown. To re-export a restored copy, the
exporter still requires a Git repository with a HEAD commit; paths and commit
metadata then describe the restored copy's repository context.

Check export and regeneration behavior with:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```
