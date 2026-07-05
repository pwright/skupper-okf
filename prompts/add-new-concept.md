# Prompt: Add a New Concept to the Repository

This guide describes the complete workflow for adding a new concept to the Skupper OKF repository, ensuring proper source tracking, cross-references, and map integration.

## Overview

Adding a new concept involves four main steps:
1. **Source Material** — Ensure human sources exist or add them
2. **Concept Document** — Create the generated concept file
3. **Cross-References** — Add bidirectional links to related concepts
4. **Map Integration** — Add the concept to relevant Blockscape maps

## Step 1: Source Material

### Check Existing Sources

First, verify if the concept is covered in existing human sources:

```bash
# List current human sources
ls -la human/

# Check sources registry
ls -la sources/

# Search for the concept in existing docs
grep -r "routing key" human/skupper-docs/
```

### Add New Human Sources (if needed)

If the concept requires new source material:

#### For Git Repositories

1. Create a sync script (see `scripts/sync-human-skupper-example-hello-world.sh` as template):

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

repo_url="https://github.com/skupperproject/<repo-name>.git"
branch="main"
dest="human/<repo-name>"
sources_dir="sources"
source_name="<repo-name>"
source_title="<Human Readable Title>"
# ... rest of script
```

2. Make it executable and run it:

```bash
chmod +x scripts/sync-human-<source-name>.sh
./scripts/sync-human-<source-name>.sh
```

#### For Single Files (e.g., OpenAPI specs, raw YAML)

1. Create a sync script (see `scripts/sync-human-openapi-spec.sh` as template):

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

source_url="https://raw.githubusercontent.com/skupperproject/skupper/main/path/to/file.yaml"
dest="human/<source-name>"
sources_dir="sources"
source_name="<source-name>"
source_title="<Human Readable Title>"
# ... rest of script
```

2. Run the sync script to fetch the source.

### Source Metadata Files

Each human source should create:
- `human/<source-name>/_source.md` — Local metadata and refresh instructions
- `sources/<source-name>.md` — Provenance record (repo URL, commit, retrieved timestamp)

## Step 2: Create the Concept Document

### File Location

Place the concept file in the appropriate directory:

```text
generated/concepts/       # Core concepts (routing-key, connector, listener)
generated/resources/      # Kubernetes resources and CRDs
generated/workflows/      # Procedures and workflows
generated/architecture/   # Architectural patterns
```

### Frontmatter Template

```yaml
---
type: Concept
title: <Concept Name>
id: skupper-concept-<kebab-case-slug>
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source_url: "<optional external source URL>"
source_paths:
  - human/<repo-name>/path/to/source.md
  - human/<repo-name>/path/to/related.md
human_sources:
  - <Human-readable source description>
  - <Another source>
tags:
  - skupper
  - <concept-tag>
  - <feature-tag>
related:
  - skupper-concept-<related-concept-1>
  - skupper-concept-<related-concept-2>
# Optional Decision Lens metadata. Include only fields clearly supported by sources.
decision:
  setupStep:
    - <setup-step>
  platform:
    - <platform>
timestamp: <ISO 8601 timestamp>
---
```

### Decision Lens metadata

Decision Lens metadata prepares pages for runtime soft filtering in the Quartz wiki. Add it when a concept, resource, or workflow clearly belongs to one or more Skupper setup decisions.

Allowed setup steps:

```text
identify-sites
classify-workloads
define-routing-key
configure-listener
configure-connector
decide-link-access
join-sites
validate
```

Allowed platforms:

```text
kubernetes
openshift
podman
docker
linux
local-system
```

Optional facets:

```yaml
decision:
  workloadRole:
    - client
  resource:
    - listener
  authoring:
    - yaml
  linkAccess:
    - openshift-route
  joinMethod:
    - cli-token
```

Use these examples as patterns:

```yaml
# Link access decision on Kubernetes/OpenShift
decision:
  setupStep:
    - decide-link-access
  platform:
    - kubernetes
    - openshift
  linkAccess:
    - openshift-route
    - loadbalancer
```

```yaml
# Joining sites
decision:
  setupStep:
    - join-sites
  resource:
    - link
  joinMethod:
    - cli-token
    - access-grant-token
```

```yaml
# Server-side binding
decision:
  setupStep:
    - configure-connector
  resource:
    - connector
  workloadRole:
    - server
```

Leave `decision` out for generic concepts unless the source clearly establishes applicability.

### Content Structure

Follow this structure for concept documents:

```markdown
# <Concept Name>

<One-paragraph summary of what this concept is and its role>

## Outcome

<What the user achieves by understanding/using this concept>

```text
<ASCII diagram showing the concept in action>
```

## How <Concept> Works

### <Subsection 1>

<Detailed explanation with code examples>

### <Subsection 2>

<More details>

## Key Properties

- **Property 1**: Description
- **Property 2**: Description

## References

- [Human Source Name](../human/<source-name>/file.md)
- [Related Concept](./related-concept.md)
- [External Source](https://example.com/source)
```

### Include Code Examples

When referencing implementation details, include code snippets from sources:

```yaml
# Example from Listener spec
apiVersion: skupper.io/v2alpha1
kind: Listener
spec:
  routingKey: backend
  host: backend-svc
  port: 8080
```

```go
// Example from controller code
config.AddTcpListener(qdr.TcpEndpoint{
    Address: listener.Spec.RoutingKey,
    // ...
})
```

## Step 3: Add Cross-References

### Identify Related Concepts

Determine which existing concepts relate to the new one:
- What does this concept depend on?
- What depends on this concept?
- What concepts are peers or alternatives?

### Update Related Concept Files

For each related concept (e.g., `connector.md`, `listener.md`):

1. **Add to frontmatter**:
```yaml
related:
  - skupper-concept-routing-key  # Add this line
```

2. **Add inline links** where the concept is mentioned:
```markdown
The connector uses a [routing key](./routing-key.md) to match with listeners.
```

3. **Add to References section** (if not already linked inline):
```markdown
## References

- [Routing Key Concept](./routing-key.md)
```

### Verify Bidirectional Links

Check that links work both ways:

```bash
# Check links to the new concept
grep -n "routing-key.md" generated/concepts/listener.md
grep -n "routing-key.md" generated/concepts/connector.md

# Check links from the new concept
grep -n "listener.md\|connector.md" generated/concepts/routing-key.md
```

## Step 4: Update Blockscape Maps

### Determine Map Placement

Identify which maps should include the new concept:

- `maps/skupper.bs` — Main Skupper application network map
- `maps/listeners.bs` — Listener-focused map
- `maps/connectors.bs` — Connector-focused map

### Add to Map Source Paths

Update the map's `source_paths` array:

```json
{
  "id": "skupper-application-network-map",
  "source_paths": [
    "human/skupper-docs/input/overview/index.md",
    "generated/concepts/listener.md",
    "generated/concepts/connector.md",
    "generated/concepts/routing-key.md"  // Add this
  ],
  "categories": [...]
}
```

### Create or Update Category

#### Option A: Create New Category

If the concept represents a new category of things (e.g., "Enablers"):

```json
{
  "id": "enablers",
  "title": "Enablers",
  "items": [
    {
      "id": "routing-key",
      "name": "Routing key",
      "source": "generated/concepts/routing-key.md",
      "external": "https://pwright.github.io/skupper-okf/generated/concepts/routing-key",
      "deps": []
    }
  ]
}
```

#### Option B: Add to Existing Category

If the concept fits in an existing category:

```json
{
  "id": "service-exposure-primitives",
  "title": "Service exposure primitives",
  "items": [
    {
      "id": "skupper-listeners-map",
      "name": "Listeners",
      "deps": ["routing-key"]  // Add dependency
    },
    // ... other items
  ]
}
```

### Update Dependencies

Add the concept as a dependency for items that rely on it:

```json
{
  "id": "distributed-applications-communicate",
  "name": "Distributed applications communicate",
  "deps": [
    "routing-key",           // Add this
    "skupper-listeners-map",
    "skupper-connectors-map"
  ]
}
```

### Validate Map JSON

```bash
# Verify valid JSON
cat maps/skupper.bs | jq '.[0].categories[] | {id, title, items: [.items[] | {id, name, deps}]}'

# Check that all dependency IDs exist
jq '.[0].categories[].items[] | select(.deps != null) | .deps[]' maps/skupper.bs | sort -u
```

## Checklist

Before considering the concept complete, verify:

- [ ] Human sources exist and are documented in `sources/`
- [ ] Sync script exists and works for human sources (if applicable)
- [ ] Concept file created in `generated/concepts/` (or appropriate directory)
- [ ] Frontmatter is complete with source_paths, tags, related concepts
- [ ] Content follows standard structure (Outcome, How It Works, Key Properties, References)
- [ ] Code examples are included where relevant
- [ ] Related concepts updated with bidirectional links (frontmatter + inline)
- [ ] Concept added to relevant Blockscape map(s)
- [ ] Map dependencies correctly reflect the concept's relationships
- [ ] Map JSON validates with `jq`
- [ ] All cross-reference links work (`grep` verification)

## Example: Routing Key Concept

See the routing key addition as a reference implementation:

1. **Source**: Created `scripts/sync-human-openapi-spec.sh` for Network Observer OpenAPI spec
2. **Concept**: Created `generated/concepts/routing-key.md` with comprehensive coverage
3. **Cross-refs**: 
   - Added 4 links in `listener.md` → `routing-key.md`
   - Added 5 links in `connector.md` → `routing-key.md`
   - Added 2 links in `routing-key.md` → `connector.md`, `listener.md`
4. **Map**: 
   - Added new "Enablers" category in `maps/skupper.bs`
   - Made listeners and connectors depend on routing-key
   - Made user outcomes depend on routing-key

## References

- [Extract from Human Sources](./extract-from-human.md)
- [Generate Blockscape](./generate-blockscape.md)
- Example sync scripts: `scripts/sync-human-*.sh`
- Example concept files: `generated/concepts/*.md`
- Example maps: `maps/*.bs`
