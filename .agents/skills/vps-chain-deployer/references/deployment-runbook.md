# Deployment runbook

## 1. Local workspace

Create a private deployment workspace outside the cloned public repository. Generated configs, links, QR codes, logs, backups, and temporary credential files stay there. Use restrictive permissions.

On macOS/Linux, generate a dedicated SSH key:

```bash
ssh-keygen -t ed25519 -a 64 -f "$HOME/.ssh/vps_chain_ed25519"
```

On Windows PowerShell:

```powershell
ssh-keygen -t ed25519 -a 64 -f "$env:USERPROFILE\.ssh\vps_chain_ed25519"
```

The user chooses a passphrase. Never read or upload the private key.

## 2. First login and read-only preflight

The user types the temporary password at the SSH prompt:

```powershell
ssh root@<VPS_IP>
```

Copy `scripts/server_preflight.sh` to the VPS or run its commands individually. Review:

- OS and kernel;
- CPU, memory, disk, time, and failed services;
- listening ports and firewall state;
- existing users, web servers, databases, containers, Xray, and VPN software;
- current SSH configuration and emergency-console availability.

Existing data or unknown listeners create a stop condition. Explain what was found and ask whether to preserve, migrate, or use another empty VPS.

## 3. SSH key and recovery

Append only the `.pub` key to `/root/.ssh/authorized_keys`. Required modes:

```text
/root/.ssh                  700
/root/.ssh/authorized_keys  600
```

On SELinux systems, restore the context. Open a second terminal and test:

```powershell
ssh -i "$env:USERPROFILE\.ssh\vps_chain_ed25519" root@<VPS_IP>
```

On macOS/Linux:

```bash
ssh -i "$HOME/.ssh/vps_chain_ed25519" root@<VPS_IP>
```

Keep the first session open. Verify the provider's emergency recovery console (KiwiVM for BandwagonHost). Back up the SSH configuration, apply the approved authentication policy, run `sshd -t`, reload SSH, then prove:

- key login succeeds;
- password authentication is rejected;
- emergency recovery remains available.

## 4. Pin and inspect v2ray-agent

Official source:

```text
https://github.com/mack-a/v2ray-agent
```

Resolve the current commit from a trusted local or VPS shell:

```bash
git ls-remote https://github.com/mack-a/v2ray-agent.git refs/heads/master
```

Record the full SHA. Download the installer through HTTPS using that immutable SHA:

```bash
curl --proto '=https' --tlsv1.2 -fsSLo /root/v2ray-agent-install.sh \
  "https://raw.githubusercontent.com/mack-a/v2ray-agent/<FULL_COMMIT_SHA>/install.sh"
chmod 700 /root/v2ray-agent-install.sh
sha256sum /root/v2ray-agent-install.sh
```

Inspect the script and any scripts it downloads. At minimum search for download hosts, `systemctl`, package managers, firewall changes, cron or timers, SSH changes, destructive removal, telemetry, and uninstall behavior. Compare the current supported OS list with the VPS.

Do not use `--no-check-certificate`. Present the commit, file hash, system impact, and restore plan. Wait for approval before running:

```bash
bash /root/v2ray-agent-install.sh
```

## 5. Select the single inbound

Menu numbers change. Follow the current labels:

```text
no-domain Reality
→ Xray-core
→ VLESS + Reality + Vision
```

Use a fresh random UUID, Reality key pair, short ID, and a verified compatible Reality target. Prefer port 443 only when it is free. Do not terminate the process already owning the port.

Reject optional protocols, panels, domain setup, Cloudflare, WS + TLS, subscriptions, or public sharing.

## 6. Server validation

Find the actual service command and configuration paths first:

```bash
systemctl cat xray
systemctl is-active xray
systemctl is-enabled xray
ss -lntup
journalctl -u xray --no-pager -n 100
```

Use the installed Xray help output to choose its supported configuration-test flags. Common historical paths under v2ray-agent include:

```text
/etc/v2ray-agent/xray/xray
/etc/v2ray-agent/xray/conf
```

Do not print configuration files containing private keys or UUIDs into chat or logs.

## 7. Japan direct gate

Before SOCKS5 routing:

1. Generate the VLESS share URI locally or copy it through a protected channel.
2. Import it into one client.
3. Confirm a normal website loads.
4. Use two independent IP-check services and confirm the visible exit matches the Japan VPS.
5. Record only a masked IP and pass/fail result.

Stop and repair Reality when this gate fails.

## 8. Test the purchased SOCKS5

Use `scripts/test_socks5.sh` on the VPS. It asks for host, port, user, and password interactively, creates a mode-600 temporary curl config, checks two IP endpoints, and removes the file on exit.

Confirm the observed IP, country, city, ASN, static behavior, expiry, and UDP limitations against the order. A country match alone is insufficient when the product promises one fixed IP.

## 9. Add the global SOCKS5 outbound

Before mutation:

```bash
umask 077
mkdir -p /root/vps-chain-backups
tar -C /etc -czf "/root/vps-chain-backups/v2ray-agent-$(date +%Y%m%d-%H%M%S).tar.gz" v2ray-agent
```

The backup contains secrets. Keep it root-only on the VPS and do not download it into the public repository.

Open `vasma` and follow current labels similar to:

```text
routing tools
→ SOCKS5 routing
→ SOCKS5 outbound
→ global SOCKS5 forwarding
```

Inspect existing routing first. Global forwarding can replace split-routing rules. Wait for approval, then let the user type credentials into the terminal prompt.

Validate syntax before reloading. After reload, confirm:

- Xray remains active;
- Reality client still connects;
- two IP-check services show the exact purchased US IP;
- DNS and required applications behave as expected.

On failure, restore the newest known-good backup and prove the Japan direct gate again.

## 10. Reboot gate

After all client tests pass, ask for approval to reboot. Verify SSH key login, Xray active/enabled, listening port, client connection, and US exit again. A service that only works before reboot is not accepted.
