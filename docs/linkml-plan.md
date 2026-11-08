# LinkML architecture model: implementation plan

Status: the first implementation slice (milestones 1 and 2) is implemented.
Resource/code extraction and the Blockscape exporter remain later milestones.
See `../model/linkml/README.md` for setup, commands, and validation limitations.

Based on `../linkml.md`, particularly the distinction between source structure,
domain knowledge, evidence, and visualization. Uses the mattpocock codebase-design
principles: a small interface, locality of extraction rules, and tests through the
same interface callers use.

## Outcome

Build a reproducible, file-based architecture dataset from selected snapshots in
`human/` and notes in `generated/`. Maintain its LinkML schema explicitly. Scripts
populate **instances conforming to that schema**; they do not need to discover or
rewrite the schema on each run.

Start by answering:

1. Which source documents describe Listener, Connector, and RoutingKey?
2. Which relationships between these concepts have explicit supporting evidence?
3. Which evidence is generated, missing, or from an older source snapshot?

Later, extend this to: which resource definitions and Go types implement those
concepts? A documentation link alone must not establish an implementation claim.

## Current repository constraints

- `human/skupper-docs/`, example snapshots, and `human/skupper-ansible/` exist.
- `human/skupper/` is now populated at commit
  `88fde51af5891df577b37fb617c369478b1dc1bb`. `sources/skupper.md` still records
  `ef654a9697cec455ff87773b8955527b78d59c9c`; report this provenance mismatch.
- Existing sync scripts already own fetching and snapshot provenance. Extraction
  should read their outputs, without silently fetching or updating sources.
- `generated/concepts/{listener,connector,routing-key}.md` provide a useful pilot.
  Some recorded paths are missing and some provenance is incomplete or older
  than the current docs snapshot. Report this rather than repairing it by guess.
- Source records vary: some use `repo`, others `url`; some snapshots record
  `source_commit`. Normalize these variants explicitly and detect disagreements.
- Existing Blockscape maps contain view-specific grouping and some legacy paths.
  Preserve them while evaluating a separately generated view.
- Keep `human/` read-only; keep `reviewed/` promotion manual. Do not edit staged
  `quartz/content/`.

## Proposed files and ownership

| Location | Purpose | Ownership |
| --- | --- | --- |
| `model/linkml/architecture.yaml` | Maintained schema | Human/agent authored, reviewed in git |
| `model/linkml/sources.yaml` | Explicit repository roots and selected input globs | Maintained configuration |
| `model/linkml/mappings.yaml` | Domain identities and evidence-backed relationship assertions | Maintained configuration; never overwritten |
| `scripts/linkml_model.py` | Small command interface to build and validate the dataset | Implementation |
| `generated/linkml/architecture.yaml` | Extracted entities, evidence, relationships | Rebuildable |
| `generated/linkml/architecture.schema.json` | Generated JSON Schema | Rebuildable |
| `indexes/linkml-report.json` | Machine-readable coverage and diagnostics | Rebuildable |
| `indexes/linkml-report.md` | Readable coverage, stale evidence, and unresolved references | Rebuildable |
| `tests/fixtures/linkml/` | Small offline source trees and expected failure cases | Test inputs |

Keep derived files under `generated/linkml/` out of the configured input globs.
Select sources explicitly; do not recursively traverse embedded `.git`, build
outputs, dependencies, or every nested repository by default.

## Milestone 1: agree and validate a small model

Tasks:

1. Define a `ArchitectureDataset` container with collections of repositories,
   source documents, domain concepts, evidence, and relationships.
2. Give every entity a stable, namespaced identifier. Preserve usable existing
   page IDs, qualify them where needed, and report collisions. Keep identity
   independent of a snapshot commit; evidence records carry the revision.
3. Define `Repository`, `SourceDocument`, `DomainConcept`, `Evidence`, and
   `Relationship`. Keep evidence references on relationships as well as entities.
4. Model relationship source/target as references to a common entity class, with
   an initial controlled set of predicates: `documents`, `related_to`, `uses`.
   `related_to` records an explicit cross-reference, not a dependency or runtime
   fact. Require evidence for every relationship.
5. Evidence records carry repository identity, relative path, declared commit
   when known, locator such as a heading, extraction method, and original review
   metadata. Track availability and snapshot mismatch separately from review
   status. Represent unknown provenance explicitly; never use the latest commit
   as a substitute for a generated note's missing source revision.
6. Create a small hand-authored dataset for the three pilot concepts. Add
   `uses` only where inspected source text supports it, with an exact locator.
7. Pin the LinkML toolchain in a dedicated dependency file after checking the
   selected version's commands. Validate the schema and sample data and generate
   JSON Schema. Keep this dependency optional for the existing repo workflow.

Acceptance: valid sample data passes; a missing required field, invalid predicate,
and wrong field type fail. Duplicate IDs and dangling references are checked
explicitly rather than assumed to be handled by schema validation.

## Milestone 2: automate population from existing docs

Tasks:

1. Implement `build` and `validate` commands in `scripts/linkml_model.py`, with
   explicit config/output arguments and `build --dry-run`.
2. Build reads the selected source records, Markdown front matter, source paths,
   and explicit domain mappings. YAML parsing must be safe and must not execute
   code from upstream files.
3. Resolve paths against declared repository roots; reject escapes. Read source
   provenance from both generated notes and snapshot records, retaining both
   when they disagree. Multiple source files may contribute separate evidence.
4. Extract document identities and declared cross-references deterministically.
   Source paths give provenance links; `related` gives `related_to` links.
   Neither automatically establishes `uses`, `implements`, or `depends_on`.
5. Keep semantic assertions in `mappings.yaml` initially, with explicit evidence
   and review metadata. This is the small manual step that avoids pretending
   prose extraction is already reliable.
6. Produce a report of scanned/skipped inputs, missing roots and files, duplicate
   identities, unresolved links, unknown commits, and snapshot mismatches.
7. Validate candidate outputs before replacing prior successful output. Keep
   records sorted and outputs deterministic; put run timestamps in reports only.
8. Add `just linkml-build` and `just linkml-check`. Do not attach this pilot to
   `just init`, `just sync-human`, or the publishing workflow yet.

Failure policy: malformed configuration/data, collisions, path escapes, and
dangling model references fail the build. Missing optional roots and unavailable
historical evidence are reported and retained as unresolved evidence; a configured
required root fails. `validate --strict` also fails on unresolved provenance.

Acceptance: an offline fixture containing two snapshots and generated notes
rebuilds identically. Tests exercise the command interface for stale/missing
evidence, malformed front matter, collision, dangling reference, and path escape.
Dry-run writes nothing. Existing content and maintained mappings remain intact.

**Decision gate:** inspect the three pilot answers before expanding. If the
dataset offers no useful traceability beyond existing Markdown, stop here or
retain only the provenance checks. A generic code-analysis platform is optional.

## Milestone 3: connect resource definitions to domain concepts

The Skupper code snapshot is available. Before extraction, check its actual commit
against the source record and report disagreement. Use the existing sync workflow
for future refreshes; extraction must not silently update the snapshot or its record.

Tasks:

1. Start with the verified CRDs
   `human/skupper/config/crd/bases/skupper_listener_crd.yaml` and
   `human/skupper/config/crd/bases/skupper_connector_crd.yaml`. The Network Observer
   specification is at `human/skupper/cmd/network-observer/spec/openapi.yaml`;
   include it only when it contributes to a pilot question. Recheck paths on
   source refresh rather than assuming directory layouts are permanent.
2. Extend the schema with `ResourceDefinition` and `Field` only as needed for the
   pilot. Extract kind, group/version, field path, declared type, and requiredness
   from structured definitions. Keep versioned definitions distinct.
3. Define explicit mappings from Listener/Connector concepts to their resource
   definitions, supported by evidence; keep concept and resource identities distinct.
4. Extend to `CodeSymbol` only if the resource definitions cannot answer the
   implementation question. A focused Go helper using `go/ast` can extract named
   declarations and field locations; resolved type/call relationships require
   additional tooling and separate scope. Do not parse Go declarations with regex.
5. Keep source line ranges revision-specific. Report ambiguous mappings instead
   of picking a symbol because its name resembles a concept.

Acceptance: trace at least one Listener and one Connector definition to exact
source locations and commits. Any implementation relationship has inspected
support. Tests use offline CRD/Go fixtures; extracting Go must not require building
Skupper or contacting a package registry.

## Milestone 4: demonstrate one downstream architecture view

Tasks:

1. Add an `export-blockscape` command consuming only the validated dataset and a
   maintained view configuration. Extraction rules stay out of the exporter.
2. Generate a new `maps/skupper-linkml-pilot.bs` using the repository's existing
   map format, with stable IDs and source links. Never overwrite existing maps.
3. Configure categories and stages in the view; do not make layout choices
   mandatory properties of every domain entity.
4. Include only relationships whose evidence/review state meets an explicit view
   policy. Clearly distinguish documentation assertions from implementation facts.
5. Run the existing `just maps` workflow to produce the Markdown wrapper and
   inspect the view before adding it to navigation or publishing.

Acceptance: every displayed relationship can be traced to evidence, map IDs and
dependencies resolve, and the same dataset remains usable without Blockscape.

## Module design and deferred work

Keep source loading, normalization, validation, and reporting behind the small
command interface. Tests use that interface. Start with one Python module; split
it only when implementation complexity warrants it. Add an adapter at an internal
seam when a second input format actually needs different extraction behaviour.

Defer automatic schema inference, whole-repo symbol graphs, Java/C extraction,
runtime topology collection, RDF/OWL, databases, and LLM extraction. Introduce
each only to answer a concrete question the existing dataset cannot answer.
LLM proposals, if introduced, must remain evidence-bearing unreviewed assertions.

## First implementation slice

Implement milestones 1 and 2 for the three named concepts only. Deliver one
schema, source configuration, maintained mappings, one build/validation script,
offline fixtures, two just recipes, and a coverage report. Leave source syncing,
code extraction, and map publication outside this slice.

LinkML validation reference:
https://linkml.io/linkml/data/validating-data.html

The schema validates representation; repository-specific checks validate
references and provenance. Neither proves an architectural claim is true.
