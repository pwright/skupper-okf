#!/usr/bin/env bash
set -Eeuo pipefail

repo_url="https://github.com/skupperproject/skupper"
dest="human/skupper"
sources_dir="sources"
source_name="skupper"
source_title="Skupper Main Repository"
dry_run="false"

log() {
  printf 'sync-human-skupper: %s\n' "$*" >&2
}

die() {
  printf 'sync-human-skupper: ERROR: %s\n' "$*" >&2
  exit 1
}

usage() {
  cat <<'DOC'
Usage:
  sync-human-skupper.sh [options]

Clone or update the full skupper repository for API and CRD documentation generation.

Options:
  --repo URL         Repository URL, default: https://github.com/skupperproject/skupper
  --dest DIR         Destination directory, default: human/skupper
  --sources-dir DIR  Provenance directory, default: sources
  --dry-run          Show what would happen without modifying files
  -h, --help         Show help

Stdout:
  Prints 'success' on successful clone/update.

Stderr:
  Progress and diagnostic messages.
DOC
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      repo_url="${2:-}"
      shift 2
      ;;
    --dest)
      dest="${2:-}"
      shift 2
      ;;
    --sources-dir)
      sources_dir="${2:-}"
      shift 2
      ;;
    --dry-run)
      dry_run="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
done

[[ -n "$repo_url" ]] || die "--repo must not be empty"
[[ -n "$dest" ]] || die "--dest must not be empty"
[[ -n "$sources_dir" ]] || die "--sources-dir must not be empty"

case "$dest" in
  /|.|..|human|"" )
    die "refusing unsafe destination: $dest"
    ;;
esac

command -v git >/dev/null 2>&1 || die "git is required"

log "repository URL: $repo_url"
log "destination: $dest"

if [[ "$dry_run" == "true" ]]; then
  log "dry run enabled; no files changed"
  printf 'dry-run\n'
  exit 0
fi

retrieved_at="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

mkdir -p "$sources_dir"

if [[ -d "$dest/.git" ]]; then
  log "updating existing clone"
  (cd "$dest" && git fetch origin && git reset --hard origin/main) || die "failed to update $dest"
else
  log "cloning repository"
  git clone --depth 1 --single-branch --branch main "$repo_url" "$dest" || die "failed to clone $repo_url"
fi

commit_hash=$(cd "$dest" && git rev-parse HEAD)
commit_date=$(cd "$dest" && git show -s --format=%ci HEAD)

cat > "$dest/_source.md" <<DOC
---
type: SourceSnapshot
title: $source_title
source_url: $repo_url
retrieved_at: $retrieved_at
commit: $commit_hash
commit_date: $commit_date
status: human-source-snapshot
---

# $source_title

This directory contains a clone of the Skupper main repository.

Do not edit this directory directly. Refresh it with:

\`\`\`bash
./scripts/sync-human-skupper.sh
\`\`\`

## Purpose

This clone is used to generate documentation from:
- OpenAPI specifications
- CRD definitions
- API types

Generated documentation is written to \`sources/\` via \`scripts/generate-api-docs.sh\`.
DOC

cat > "$sources_dir/$source_name.md" <<DOC
---
type: SourceFile
title: $source_title
id: source-$source_name
url: $repo_url
retrieved_at: $retrieved_at
commit: $commit_hash
commit_date: $commit_date
local_snapshot: ../$dest
---

# $source_title

This source entry records the Skupper repository clone used for API/CRD documentation generation.

- URL: \`$repo_url\`
- Retrieved: \`$retrieved_at\`
- Commit: \`$commit_hash\`
- Commit date: \`$commit_date\`
- Local snapshot: \`../$dest/\`

## Description

The Skupper project provides hybrid cloud communication infrastructure.
This clone provides source material for generating API and CRD documentation.

## Generated Documentation

Run \`./scripts/generate-api-docs.sh\` to generate documentation from:
- OpenAPI specs
- CRD definitions
- API type definitions
DOC

log "wrote $dest/_source.md"
log "wrote $sources_dir/$source_name.md"
printf 'success\n'
