#!/usr/bin/env bash
set -u

section() {
  printf '\n[%s]\n' "$1"
}

run_if_present() {
  local command_name="$1"
  shift
  if command -v "$command_name" >/dev/null 2>&1; then
    "$@" 2>&1 || true
  else
    printf '%s is unavailable\n' "$command_name"
  fi
}

section "identity"
id 2>&1 || true
hostname 2>&1 || true

section "operating system"
if [[ -r /etc/os-release ]]; then
  sed -n '1,40p' /etc/os-release
fi
uname -a 2>&1 || true

section "resources"
run_if_present df df -h
run_if_present free free -h
run_if_present uptime uptime

section "time"
date -Is 2>&1 || date 2>&1 || true
run_if_present timedatectl timedatectl status

section "listening ports"
if command -v ss >/dev/null 2>&1; then
  ss -lntup 2>&1 || true
elif command -v netstat >/dev/null 2>&1; then
  netstat -lntup 2>&1 || true
else
  printf 'ss and netstat are unavailable\n'
fi

section "failed services"
run_if_present systemctl systemctl --failed --no-pager

section "known server software"
for command_name in xray nginx apache2 httpd caddy docker podman mysql mysqld mariadbd postgres wg sing-box; do
  if command -v "$command_name" >/dev/null 2>&1; then
    command -v "$command_name"
  fi
done

section "firewall"
run_if_present firewall-cmd firewall-cmd --state
run_if_present ufw ufw status
run_if_present nft nft list ruleset

section "ssh effective settings"
if command -v sshd >/dev/null 2>&1; then
  sshd -T 2>/dev/null | awk '
    $1 == "port" ||
    $1 == "permitrootlogin" ||
    $1 == "passwordauthentication" ||
    $1 == "kbdinteractiveauthentication" ||
    $1 == "pubkeyauthentication" { print }
  '
fi

printf '\nPreflight is read-only. Review all listeners and software before changing this VPS.\n'

