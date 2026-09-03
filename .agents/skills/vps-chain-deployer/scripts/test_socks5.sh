#!/usr/bin/env bash
set -euo pipefail

if ! command -v curl >/dev/null 2>&1; then
  printf 'curl is required.\n' >&2
  exit 1
fi

read -r -p 'SOCKS5 host: ' socks_host
read -r -p 'SOCKS5 port: ' socks_port
read -r -p 'SOCKS5 username: ' socks_user
read -r -s -p 'SOCKS5 password: ' socks_pass
printf '\n'

if [[ ! "$socks_host" =~ ^[[:alnum:].:_-]+$ ]]; then
  printf 'Host contains unsupported characters.\n' >&2
  exit 1
fi

case "$socks_port" in
  ''|*[!0-9]*)
    printf 'Port must be numeric.\n' >&2
    exit 1
    ;;
esac

if (( socks_port < 1 || socks_port > 65535 )); then
  printf 'Port must be between 1 and 65535.\n' >&2
  exit 1
fi

if [[ -z "$socks_user" || -z "$socks_pass" ]]; then
  printf 'This workflow requires an authenticated SOCKS5 account.\n' >&2
  exit 1
fi

umask 077
curl_config="$(mktemp "${TMPDIR:-/tmp}/vps-chain-curl.XXXXXX")"

cleanup() {
  socks_pass=''
  unset socks_pass
  if command -v shred >/dev/null 2>&1; then
    shred -u "$curl_config" 2>/dev/null || rm -f "$curl_config"
  else
    rm -f "$curl_config"
  fi
}
trap cleanup EXIT HUP INT TERM

escape_curl_value() {
  printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g'
}

safe_host="$(escape_curl_value "$socks_host")"
safe_user="$(escape_curl_value "$socks_user")"
safe_pass="$(escape_curl_value "$socks_pass")"

{
  printf 'proxy = "socks5h://%s:%s"\n' "$safe_host" "$socks_port"
  printf 'proxy-user = "%s:%s"\n' "$safe_user" "$safe_pass"
  printf 'fail\n'
  printf 'silent\n'
  printf 'show-error\n'
  printf 'connect-timeout = 10\n'
  printf 'max-time = 20\n'
} >"$curl_config"

unset safe_pass socks_pass

printf 'Check 1: '
curl --config "$curl_config" https://api.ipify.org
printf '\nCheck 2: '
curl --config "$curl_config" https://ifconfig.me/ip
printf '\n'

printf 'The two values should match the purchased static US IP. Do not commit this output.\n'
