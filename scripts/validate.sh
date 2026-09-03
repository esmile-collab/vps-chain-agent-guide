#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

required_files=(
  "README.md"
  "AGENTS.md"
  "CLAUDE.md"
  ".agents/skills/vps-chain-deployer/SKILL.md"
  ".agents/skills/vps-chain-deployer/agents/openai.yaml"
  "templates/execution-record.md"
)

for required_file in "${required_files[@]}"; do
  if [[ ! -f "$required_file" ]]; then
    printf 'Missing required file: %s\n' "$required_file" >&2
    exit 1
  fi
done

bash -n scripts/*.sh .agents/skills/vps-chain-deployer/scripts/*.sh
python3 scripts/validate_skill.py
bash scripts/secret-scan.sh
git diff --check
git diff --cached --check

style_status=1
if command -v rg >/dev/null 2>&1; then
  rg -n --hidden \
    --glob '!.git/**' \
    --glob '!scripts/validate.sh' \
    '不是.{0,40}而是' . && style_status=0 || style_status=$?
else
  grep -RInE \
    --exclude-dir='.git' \
    --exclude='validate.sh' \
    '不是.{0,40}而是' . && style_status=0 || style_status=$?
fi

if [[ "$style_status" -eq 0 ]]; then
  printf 'Found a disallowed contrast phrase. Rewrite it directly.\n' >&2
  exit 1
fi

if [[ "$style_status" -gt 1 ]]; then
  printf 'Style scan failed with status %s.\n' "$style_status" >&2
  exit "$style_status"
fi

printf 'Repository validation passed.\n'
