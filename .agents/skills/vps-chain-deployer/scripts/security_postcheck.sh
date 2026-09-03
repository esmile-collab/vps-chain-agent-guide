#!/usr/bin/env bash
set -u

section() {
  printf '\n[%s]\n' "$1"
}

section "identity"
id 2>&1 || true
hostname 2>&1 || true

section "ssh effective settings"
if command -v sshd >/dev/null 2>&1; then
  sshd -T 2>/dev/null | awk '
    $1 == "port" ||
    $1 == "listenaddress" ||
    $1 == "permitrootlogin" ||
    $1 == "passwordauthentication" ||
    $1 == "kbdinteractiveauthentication" ||
    $1 == "pubkeyauthentication" { print }
  '
else
  printf 'sshd is unavailable\n'
fi

section "ssh key permissions"
for path in /root/.ssh /root/.ssh/authorized_keys; do
  if [[ -e "$path" ]]; then
    stat -c '%A %a %n' "$path" 2>/dev/null || stat -f '%Sp %Lp %N' "$path" 2>/dev/null || true
  else
    printf 'missing: %s\n' "$path"
  fi
done

section "public listeners"
if command -v ss >/dev/null 2>&1; then
  ss -lntup 2>&1 || true
elif command -v lsof >/dev/null 2>&1; then
  lsof -nP -iTCP -sTCP:LISTEN 2>&1 || true
elif command -v netstat >/dev/null 2>&1; then
  netstat -lnt 2>&1 || true
else
  printf 'ss, lsof, and netstat are unavailable\n'
fi
printf 'Review every 0.0.0.0 or [::] listener; this script does not assume a port is safe from its number alone.\n'

section "firewall state"
if command -v firewall-cmd >/dev/null 2>&1; then
  firewall-cmd --state 2>&1 || true
fi
if command -v ufw >/dev/null 2>&1; then
  ufw status 2>&1 || true
fi
if command -v nft >/dev/null 2>&1; then
  nft list ruleset 2>&1 | sed -n '1,160p' || true
fi

section "xray service"
if command -v systemctl >/dev/null 2>&1; then
  systemctl is-active xray 2>&1 || true
  systemctl is-enabled xray 2>&1 || true
else
  printf 'systemctl is unavailable\n'
fi

section "configuration permissions"
if [[ -d /etc/v2ray-agent ]]; then
  find /etc/v2ray-agent -type f \( -perm -004 -o -perm -040 \) -print 2>/dev/null | sed -n '1,80p'
  printf 'The paths above are readable by other users and require review.\n'
else
  printf '/etc/v2ray-agent is absent\n'
fi

section "time and brute-force protection"
if command -v timedatectl >/dev/null 2>&1; then
  timedatectl status 2>&1 | sed -n '1,24p' || true
fi
if command -v fail2ban-client >/dev/null 2>&1; then
  fail2ban-client status 2>&1 || true
else
  printf 'fail2ban is unavailable; this is informational, not an automatic failure.\n'
fi

printf '\nSecurity postcheck is read-only. It never prints private keys, passwords, UUIDs, or full node links.\n'
