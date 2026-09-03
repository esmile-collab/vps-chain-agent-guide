# Troubleshooting

Restore the last known-good layer, collect evidence, then change one variable.

## Layer 1: local Agent and terminal

| Symptom | Check | Safe action |
|---|---|---|
| Agent refuses before connecting | Model policy and unofficial gateway | Run the willingness check; switch to a compatible model |
| Commands are not available | OS version, Git, SSH, Agent tool permission | Install from official sources; keep manual permissions |
| Secret appears in output | Shell history, logs, screenshots, Git status | Stop, rotate the secret, remove local traces, then clean history if committed |

## Layer 2: SSH and VPS

| Symptom | Check | Safe action |
|---|---|---|
| Port 22 times out | VPS power, IPv4, provider console, local network | Verify through the provider console; do not reinstall repeatedly |
| Host-key warning after a known rebuild | Provider console and recorded fingerprint | Accept only after confirming the expected IP or rebuild |
| Key login fails | `authorized_keys`, permissions, SELinux context, SSH logs | Keep the working password session open |
| Locked out after SSH change | Provider emergency console | Restore backed-up SSH configuration |
| Existing ports or services found | Process owner, containers, packages, user data | Stop and ask whether to preserve or use an empty VPS |

## Layer 3: Reality inbound

| Symptom | Check | Safe action |
|---|---|---|
| Xray service fails | Configuration test, unit file, journal | Restore last config; avoid repeated full reinstall |
| 443 is not listening | Service, firewall, port conflict | Identify the owner; do not kill an unknown process |
| Client times out | Address, port, network filtering, server firewall | Verify TCP reachability before changing Reality keys |
| Handshake fails | UUID, public key, short ID, SNI, fingerprint, target | Compare protected local values with server config without printing them |
| Service works until reboot | enable state, dependencies, time sync | Fix startup ordering and rerun the reboot gate |

## Layer 4: SOCKS5 exit

| Symptom | Check | Safe action |
|---|---|---|
| Standalone SOCKS5 test fails | Host, port, authentication, expiry, IP whitelist | Ask the user to check the vendor dashboard; keep Reality direct |
| IP changes between checks | Product type, rotation, DNS, pool behavior | Confirm the user bought a static product |
| Location differs | Exact IP, vendor allocation, geo databases | Compare multiple sources and the invoice; contact vendor if needed |
| Web works but UDP app fails | SOCKS5 UDP support and application protocol | Record limitation or change product with user approval |

## Layer 5: Xray chained outbound

| Symptom | Check | Safe action |
|---|---|---|
| Reality works, exit stays Japan | Active Xray outbound and routing tags | Validate the applied route and reload safely |
| Chain causes total outage | SOCKS5 test, route replacement, Xray logs | Restore backup and prove Japan direct again |
| Only some destinations fail | Vendor policy, DNS, IPv6, route rules | Compare one failing and one working destination; avoid global rewrites |

## Layer 6: client

| Symptom | Check | Safe action |
|---|---|---|
| v2rayN import fails | Client version, URI integrity, Reality support | Re-export locally and update from official release |
| Browser works, desktop app fails | Whether the app follows system proxy | Evaluate TUN only for that verified need |
| iPhone works on Wi-Fi only | Cellular permission, route mode, carrier network | Test the same profile without regenerating credentials |
| All clients fail at the same time | VPS bill, VPS service, exit expiry | Start at provider state, then work through layers in order |

## Recovery hierarchy

1. Disable the SOCKS5 global route and restore Japan direct.
2. Restore the latest root-only `/etc/v2ray-agent` backup.
3. Restore the provider snapshot if one was created and its age is understood.
4. Reinstall only on a confirmed empty VPS with user approval and a tested emergency console.
