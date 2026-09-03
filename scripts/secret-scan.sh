#!/usr/bin/env bash
set -euo pipefail

secret_pattern='-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|vless://[A-Za-z0-9]|socks5h?://[^[:space:]/]+:[^[:space:]@]+@'

scan_status=1

if command -v rg >/dev/null 2>&1; then
  rg -n --hidden \
    --glob '!.git/**' \
    --glob '!scripts/secret-scan.sh' \
    --regexp "$secret_pattern" . && scan_status=0 || scan_status=$?
else
  while IFS= read -r -d '' scan_file; do
    if grep -InE -- "$secret_pattern" "$scan_file"; then
      scan_status=0
    else
      grep_status=$?
      if [[ "$grep_status" -gt 1 ]]; then
        scan_status="$grep_status"
        break
      fi
    fi
  done < <(
    find . -type f \
      ! -path './.git/*' \
      ! -path './scripts/secret-scan.sh' \
      \( -name '*.md' -o -name '*.yml' -o -name '*.yaml' -o -name '*.sh' -o -name '*.py' -o -name '*.json' -o -name '*.txt' \) \
      -print0
  )
fi

if [[ "$scan_status" -eq 0 ]]; then
  printf 'Potential secret detected. Remove or mask it before committing.\n' >&2
  exit 1
fi

if [[ "$scan_status" -gt 1 ]]; then
  printf 'Secret scan failed with status %s.\n' "$scan_status" >&2
  exit "$scan_status"
fi

printf 'No high-risk secret pattern detected.\n'
