# Layout

```text
skupper-okf-mvp/
  README.md
  plan.md
  justfile
  scripts/
    init-layout.sh
    sync-human-skupper-docs.sh
    sync-human-skupper-example-hello-world.sh
  prompts/
    extract-from-human.md
    promote-generated.md
    generate-blockscape.md
    context-pack.md
  _system/
    AGENTS.md
  human/
    skupper-docs/
      _source.md
      ...snapshot of skupper-docs...
    skupper-example-hello-world/
      _source.md
      ...snapshot of skupper-example-hello-world...
  sources/
    skupper-docs.md
    skupper-example-hello-world.md
  generated/
  reviewed/
  indexes/
  maps/
  context-packs/
```

Each `human/<repo-name>/` source tree is intentionally copied rather than symlinked. This makes the OKF repo portable and records exactly which upstream commit was used.

## Test scope

The smoke test validates the generic layout and one representative source sync path. It should not add a fixture or assertion for every repository under `human/`; additional upstream repositories are covered by their sync scripts and source records.
