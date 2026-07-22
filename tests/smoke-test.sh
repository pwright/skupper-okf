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
[[ "$commit" == "local-fixture" || "$commit" =~ ^[0-9a-f]{40}$ ]] || die "unexpected fixture commit: $commit"

[[ -f human/skupper-docs/_source.md ]] || die "missing human/skupper-docs/_source.md"
[[ -f sources/skupper-docs.md ]] || die "missing sources/skupper-docs.md"
[[ -f human/skupper-docs/docs/listener.md ]] || die "missing copied fixture page"

grep -Eq 'source_commit: local-fixture|source_commit: [0-9a-f]{40}' human/skupper-docs/_source.md || die "human source metadata missing commit"
grep -q 'local_snapshot: ../human/skupper-docs' sources/skupper-docs.md || die "source record missing snapshot path"

log "generating Ansible docs from offline fixture"
dry_run="$(./scripts/generate-ansible-docs.py --source-repo tests/fixtures/fake-skupper-ansible --output-dir generated/skupper-ansible --dry-run)"
[[ "$dry_run" == "dry-run" ]] || die "unexpected ansible dry-run output: $dry_run"
[[ ! -e generated/skupper-ansible/skupper-ansible-module-resource.md ]] || die "ansible dry-run wrote output"

result="$(./scripts/generate-ansible-docs.py --source-repo tests/fixtures/fake-skupper-ansible --output-dir generated/skupper-ansible)"
[[ "$result" == "success" ]] || die "unexpected ansible generation output: $result"
[[ -f generated/skupper-ansible/skupper-ansible-module-resource.md ]] || die "missing generated Ansible module page"
[[ -f generated/skupper-ansible/skupper-ansible-overview.md ]] || die "missing generated Ansible overview page"
grep -q 'id: skupper-ansible-module-resource' generated/skupper-ansible/skupper-ansible-module-resource.md || die "generated module page missing id"
grep -q 'source_paths:' generated/skupper-ansible/skupper-ansible-module-resource.md || die "generated module page missing source paths"
grep -q 'authoring:' generated/skupper-ansible/skupper-ansible-module-resource.md || die "generated module page missing Decision Lens authoring"

log "checking expected directories"
while IFS= read -r dir; do
  [[ -d "$dir" ]] || die "missing directory: $dir"
done < tests/golden/expected-layout.txt

log "ok"
printf 'ok\n'
