# Layout

```text
skupper-okf-mvp/
  README.md
  plan.md
  justfile
  scripts/
    init-layout.sh
    sync-human-skupper-docs.sh
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
      ...future upstream snapshot...
  sources/
    skupper-docs.md
  generated/
  reviewed/
  indexes/
  maps/
  context-packs/
```

Each `human/<repo-name>/` source tree is intentionally copied rather than symlinked. This makes the OKF repo portable and records exactly which upstream commit was used.
