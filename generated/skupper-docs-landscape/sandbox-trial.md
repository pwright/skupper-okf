---
type: DocumentationLandscapePage
title: "Sandbox Trial"
id: sandbox-trial
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/sandbox-trial
tags:
  - skupper
  - docs-landscape
  - previews
related:
  - preview-installation
  - test-plan
timestamp: 2026-07-23T19:46:31Z
---

# Sandbox Trial

A sandbox trial is a contained preview evaluation in a non-production environment. This page should outline how to install the preview safely, run the validation plan, collect evidence, and avoid leaking experimental assumptions into production automation.

## Appears in

- [Skupper Technology Previews](./skupper-previews.md) / Validate Safely

## Dependencies

- [Preview Installation](./preview-installation.md)
- [Validation Test Plan](./test-plan.md)

## Sources

- [Preview installation](./preview-installation.md): Dependency page for installing preview components.
- [Validation test plan](./test-plan.md): Dependency page for trial acceptance checks.
- [Install docs](../../human/skupper-docs/input/install/index.md): Local source for standard installation paths to compare against preview-specific instructions.
- [Troubleshooting docs](../../human/skupper-docs/input/troubleshooting/index.md): Local source for diagnostic flow during trial failures.
- [Debug dumps topic](../../human/skupper-docs/input/refdog/topics/debug-dumps.md): Local source for gathering version, configuration, and status evidence.

## Website Links

- [Skupper install docs](https://skupper.io/docs/install/index.html)
- [Skupper troubleshooting docs](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Make the sandbox disposable and isolated from production credentials.
- Capture exact versions, manifests, flags, and environment assumptions before testing.
