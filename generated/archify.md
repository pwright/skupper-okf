# Archify diagrams

This directory contains architecture diagrams generated with the
[Archify](https://github.com/skupperproject/skupper-okf) skill bundled in Bob.
Each diagram is a pair of files:

| File | Purpose |
|---|---|
| `<name>.architecture.json` | Editable source spec |
| `<name>.html` | Self-contained rendered artifact (open in any browser) |
| `<name>.visual-check.*.png` | Screenshot sidecars produced by `visual-check` |

The JSON spec and the HTML are **independent**. Editing the JSON has no effect
on the HTML until you re-deliver.

---

## Prerequisites

```bash
node --version   # requires Node.js ≥ 18
```

The Archify CLI lives at:

```
~/.bob/skills/archify/bin/archify.mjs
```

All commands below assume you run them from the repo root
(`~/repos/sk/skupper-okf`).

---

## Editing an existing diagram

1. Open the `.architecture.json` file and make your changes.
2. Validate the spec:

   ```bash
   node ~/.bob/skills/archify/bin/archify.mjs \
     validate architecture generated/<name>.architecture.json \
     --quality showcase --json
   ```

   A showcase pass reports **9/9 checks, 0 errors, 0 warnings**.
   Fix any reported diagnostics before proceeding.

3. Deliver (re-render) the HTML:

   ```bash
   node ~/.bob/skills/archify/bin/archify.mjs \
     deliver architecture generated/<name>.architecture.json \
     generated/<name>.html --quality showcase
   ```

4. Regenerate the screenshot sidecars:

   ```bash
   node ~/.bob/skills/archify/bin/archify.mjs \
     visual-check generated/<name>.html
   ```

---

## Creating a new diagram from scratch

Ask Bob:

> "Use archify to create a diagram for &lt;topic&gt;, source code is in &lt;path&gt;"

Bob will inspect the code, author a candidate JSON, validate, deliver, and
run `visual-check` automatically.

The JSON lands in `debug/` during authoring (archify's working directory).
After delivery, copy it to `generated/`:

```bash
cp debug/<name>.architecture.json generated/<name>.architecture.json
```

---

## Diagram types

| Type | Use for |
|---|---|
| `architecture` | Components, services, boundaries, infrastructure |
| `workflow` | Processes, approval gates, CI/CD pipelines |
| `sequence` | API call chains, request lifecycles |
| `dataflow` | Pipelines, ETL/ELT, data lineage |
| `lifecycle` | State/status transitions, retries |

Replace `architecture` in every command above with the appropriate type.

---

## Key JSON fields

```jsonc
{
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "My Diagram",
    "output": "my-diagram.html",   // used by deliver for default output path
    "quality_profile": "showcase"  // required for showcase validation
  },
  "components": [
    // id, type, label, sublabel, pos [x,y], size [w,h]
    { "id": "api", "type": "backend", "label": "API Server", "pos": [100, 100], "size": [150, 60] }
  ],
  "boundaries": [
    // kind: "region" | "security-group" | "cluster"
    { "kind": "region", "label": "My Service", "wraps": ["api"] }
  ],
  "connections": [
    // from/to reference component ids; variant: "dashed" | "security" | "emphasis"
    { "id": "c1", "from": "client", "to": "api", "label": "REST", "variant": "emphasis" }
  ],
  "cards": [
    // supporting detail shown below the diagram
    { "dot": "cyan", "title": "My section", "items": ["Bullet one", "Bullet two"] }
  ]
}
```

### Component types
`frontend` · `backend` · `database` · `cloud` · `security` · `messagebus` · `external`

### Connection label placement
If a label overlaps a component or another label, use `labelAt: [x, y]` to pin
it to an explicit coordinate. The validator reports the exact suggested
coordinates in its diagnostic output.

---

## Diagrams in this directory

| Spec | HTML | Description |
|---|---|---|
| [`skupper-combined.architecture.json`](skupper-combined.architecture.json) | [`skupper-combined.html`](skupper-combined.html) | Skupper v2 deployment and data path |
| [`skupper-datapath.architecture.json`](skupper-datapath.architecture.json) | [`skupper-datapath.html`](skupper-datapath.html) | Skupper data path detail |
| [`skupper-deployment.architecture.json`](skupper-deployment.architecture.json) | [`skupper-deployment.html`](skupper-deployment.html) | Skupper deployment overview |
| [`skupper-network-observer.architecture.json`](skupper-network-observer.architecture.json) | [`skupper-network-observer.html`](skupper-network-observer.html) | Network Observer component architecture |
