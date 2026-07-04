#!/usr/bin/env bash
set -Eeuo pipefail

source_repo="human/skupper-router"
output_dir="generated/skupper-router"
dry_run="false"

log() {
  printf 'copy-router-markdown: %s\n' "$*" >&2
}

die() {
  printf 'copy-router-markdown: ERROR: %s\n' "$*" >&2
  exit 1
}

usage() {
  cat <<'DOC'
Usage:
  copy-router-markdown.sh [options]

Copy all markdown files from skupper-router to sources/ with proper naming and frontmatter.

Options:
  --source-repo DIR  Source repository directory, default: human/skupper-router
  --output-dir DIR   Output directory for copied markdown, default: generated/skupper-router
  --dry-run          Show what would happen without modifying files
  -h, --help         Show help

Stdout:
  Prints 'success' on successful copy.

Stderr:
  Progress and diagnostic messages.

Generates:
  generated/skupper-router/router-*.md - Markdown files from the router repo with frontmatter
DOC
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --source-repo)
      source_repo="${2:-}"
      shift 2
      ;;
    --output-dir)
      output_dir="${2:-}"
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

[[ -n "$source_repo" ]] || die "--source-repo must not be empty"
[[ -n "$output_dir" ]] || die "--output-dir must not be empty"
[[ -d "$source_repo" ]] || die "source repository not found: $source_repo (run sync-human-skupper-router.sh first)"

if [[ "$dry_run" == "true" ]]; then
  log "dry run enabled; no files changed"
  printf 'dry-run\n'
  exit 0
fi

generated_at="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
mkdir -p "$output_dir"

copied_count=0

# Find all markdown files, excluding _source.md and node_modules
while IFS= read -r -d '' md_file; do
  # Skip _source.md files we created
  if [[ "$(basename "$md_file")" == "_source.md" ]]; then
    continue
  fi

  log "found: $md_file"

  # Generate output filename from path
  # human/skupper-router/docs/notes/code-conventions.md -> router-docs-notes-code-conventions.md
  # human/skupper-router/decisions/0001-record-architecture-decisions.md -> router-decisions-0001-record-architecture-decisions.md

  # Remove the source_repo prefix
  relative_path="${md_file#$source_repo/}"

  # Replace / with - and prepend "router-"
  output_name="router-$(echo "$relative_path" | tr '/' '-')"

  # Extract title from the markdown file (first # heading)
  title=$(grep -m 1 '^# ' "$md_file" 2>/dev/null | sed 's/^# //' || echo "")

  # If no title found, generate from filename
  if [[ -z "$title" ]]; then
    title=$(basename "$md_file" .md | tr '-' ' ' | sed 's/\b\(.\)/\u\1/g')
  fi

  # Generate ID from output filename
  id="${output_name%.md}"

  # Create output file with frontmatter
  cat > "${output_dir}/${output_name}" <<DOC
---
type: RouterDocs
title: $title
id: $id
source_file: ../$md_file
generated_at: $generated_at
generator: copy-router-markdown.sh
---

DOC

  # Append the original content
  cat "$md_file" >> "${output_dir}/${output_name}"

  log "wrote ${output_dir}/${output_name}"
  : $((copied_count++))
done < <(find "$source_repo" -name "*.md" -type f -print0)

if [[ $copied_count -eq 0 ]]; then
  log "warning: no markdown files found"
  printf 'no-files-copied\n'
else
  log "copied $copied_count markdown files"
  printf 'success\n'
fi
