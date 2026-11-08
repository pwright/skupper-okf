# LinkML architecture pilot

This pilot connects Listener, Connector, and RoutingKey to documentation and
source evidence. The schema is maintained here; scripts populate instance data.
The implementation follows the small-interface guidance in the
`mattpocock-skills:codebase-design` skill.

From the repository root:

```bash
python3 -m venv .venv-linkml
.venv-linkml/bin/python -m pip install -r requirements-linkml.txt
just linkml-build
just linkml-check
just linkml-test
```

Without `just`, use `.venv-linkml/bin/python scripts/linkml_model.py build` or
`validate`. Run the tests with
`.venv-linkml/bin/python -m unittest discover -s tests -p test_linkml_model.py`.

Inspect `indexes/linkml-report.md` for the three pilot answers: supporting
documents, evidence-backed `uses` assertions, and missing/stale/unknown evidence.
Machine-readable reports are in `indexes/linkml-report.json`. These reports are
ignored by git and can be regenerated. The dataset and generated JSON Schema are
in `generated/linkml/`.

## Editing inputs

- `sources.yaml` selects repository roots and specific input files/globs. Paths
  are workspace-relative; globs are relative to each selected repository root.
  Source snapshots are never fetched or updated by the builder.
- `mappings.yaml` assigns documents to stable domain concept IDs. Semantic
  assertions require a selected source document, a locator, and a verbatim
  supporting excerpt. Their original status/review metadata is preserved.
- `architecture.yaml` defines the representation. Namespace URLs under
  `example.org` are provisional identifiers, not hosted resources.

For a separate fixture/workspace, pass `--root DIR`. Configuration and mapping
paths are relative to that root; `--schema FILE` can select another maintained
schema. `--output generated/DIR` and `--report indexes/NAME` choose artifact paths.
The report argument is a stem; `.md` and `.json` are appended.

```bash
.venv-linkml/bin/python scripts/linkml_model.py build --dry-run
just linkml-check --strict
```

Dry-run builds and validates in memory without writing outputs. Normal validation
checks schema constraints, ID uniqueness, evidence, and reference integrity.
Strict validation additionally rejects missing, mismatched, or unknown provenance.
The current pilot deliberately retains existing provenance gaps, so strict
validation is expected to fail until they are resolved. Validation checks the
recorded dataset; rebuild to refresh filesystem availability and source revisions.

Unselected `related` links are reported and omitted from the model; they never
become dangling relationships. A source path records provenance, and a `related`
entry records a cross-reference. Neither becomes an implementation claim.
Snapshot revision equality is not a content integrity check and does not establish
that an architectural assertion is correct. Missing revision metadata on local
generated notes remains unknown.

Invalid builds leave prior successful artifacts intact. Outputs are staged before
replacement, with atomic replacement per file; this is not a transaction across
all four artifacts if filesystem replacement itself fails.

The optional toolchain is pinned in `requirements-linkml.txt`. It uses LinkML's
JSON Schema generator plus explicit reference/provenance checks. Direct LinkML
validation is also available:

```bash
.venv-linkml/bin/linkml validate model/linkml/architecture.yaml
.venv-linkml/bin/linkml validate -s model/linkml/architecture.yaml \
  -C ArchitectureDataset generated/linkml/architecture.yaml
```

See the [implementation plan](../../docs/linkml-plan.md) for later resource/code
extraction and Blockscape work, and the
[LinkML validation documentation](https://linkml.io/linkml/data/validating-data.html)
for the upstream validation interface.
