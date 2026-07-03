#!/usr/bin/env bash
set -Eeuo pipefail

log() {
  printf 'smoke-test: %s\n' "$*" >&2
}

die() {
  printf 'smoke-test: ERROR: %s\n' "$*" >&2
  exit 1
}

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
work_dir="$(mktemp -d)"
trap 'rm -rf "$work_dir"' EXIT

log "copying project to temporary directory"
rsync -a --exclude human --exclude generated --exclude reviewed --exclude indexes --exclude maps "$repo_root/" "$work_dir/project/"
cd "$work_dir/project"

log "initializing layout"
./scripts/init-layout.sh >/tmp/skupper-okf-init.out

log "syncing from offline fixture"
commit="$(./scripts/sync-human-skupper-docs.sh --local-source tests/fixtures/fake-skupper-docs)"
[[ "$commit" == "local-fixture" ]] || die "unexpected fixture commit: $commit"

[[ -f human/_source.md ]] || die "missing human/_source.md"
[[ -f sources/skupper-docs.md ]] || die "missing sources/skupper-docs.md"
[[ -f human/docs/listener.md ]] || die "missing copied fixture page"

grep -q 'source_commit: local-fixture' human/_source.md || die "human source metadata missing commit"
grep -q 'local_snapshot: ../human' sources/skupper-docs.md || die "source record missing snapshot path"

log "checking expected directories"
while IFS= read -r dir; do
  [[ -d "$dir" ]] || die "missing directory: $dir"
done < tests/golden/expected-layout.txt

log "ok"
printf 'ok\n'
