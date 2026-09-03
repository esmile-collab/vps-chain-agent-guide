---
name: vps-chain-deployer
description: Guide and execute an authorized personal VPS chain setup from purchase through VLESS Reality, an authenticated SOCKS5 egress, client setup, acceptance, maintenance, and troubleshooting. Use when a beginner asks an Agent to select or configure a BandwagonHost VPS, Xray or v2ray-agent, a static US SOCKS5 exit, Shadowrocket, or v2rayN. Stop public-proxy, resale, attack, evasion, credential-harvesting, and unauthorized-system requests.
---

# VPS Chain Deployer

## Goal

Complete and verify this single-user chain on assets the user owns or is authorized to manage:

```text
device → VLESS + Reality + Vision → Japan VPS → authenticated US SOCKS5 → website
```

Maintain one server inbound. Do not add a domain, Cloudflare, WS + TLS, a web panel, another protocol, or a client-side second chain unless the user explicitly changes scope after understanding the added cost and failure modes.

This Skill contains reusable product procedure. For an existing installation, read a user-supplied local context directory outside the repository before changing anything. Never copy that context, instance parameters, invoices, or credentials into Git.

## Conversation contract

- Speak in the user's language and explain only the current step.
- Ask one question at a time when the answer requires the user.
- After every step report: `current stage`, `verified`, `unverified`, `next human action`, and `rollback point`.
- Separate observations, current vendor documentation, and inference.
- Do not claim completion until every acceptance gate passes.
- Keep an execution record using `../../../templates/execution-record.md` when working inside this repository. In a copied Skill, create an equivalent non-secret record.

## Scope gate

Before technical work, establish all of the following:

1. The user owns or has explicit authority over the VPS, proxy account, and client devices.
2. The setup is for personal or otherwise authorized use that follows local law and vendor terms.
3. No public endpoint, resale, scanning, attack, spam, fraud, traffic interception, platform-risk evasion, or credential collection is requested.
4. The user accepts that a single chain fails when either the VPS or US exit fails.

Stop out-of-scope capability work. You may still help shut down services, revoke credentials, or recover the user's server.

## Secret rules

- Never request payment credentials, email passwords, Apple ID passwords, one-time codes, SSH private keys, full VLESS links, Reality private keys, or SOCKS5 passwords in chat.
- Have the user type passwords into a hidden local terminal prompt.
- Keep secrets out of command-line arguments, shell history, Git, screenshots, QR websites, and execution records.
- Generate QR codes locally and store them outside the repository.
- If any credential appeared publicly, rotate it before continuing.

Read [references/intake-and-gates.md](references/intake-and-gates.md) before collecting inputs or asking for approval.

## Workflow

### Stage 0: initialize

1. Create a private local working directory outside the public repository for logs and generated credentials.
2. Copy the non-secret project brief and execution-record templates.
3. Confirm device type, location, lawful use, budget, billing preference, and whether a fixed US IP is actually needed.
4. If the Agent uses an unofficial model gateway, run the capability and willingness check in the intake reference before connecting to a server.

### Stage 1: purchase the VPS

1. Navigate only to `bandwagonhost.com` or a URL the user independently verifies.
2. Read the live checkout page. Confirm billing period, total, available Japan location, traffic limit, refund terms, and renewal behavior.
3. Recalculate monthly cost from the live bill. Do not reuse historical prices.
4. Stop before final purchase. The user accepts terms, completes verification, and pays.
5. After activation, verify KiwiVM access, Japan location, public IPv4, OS, traffic reset date, and emergency console.

### Stage 2: take over the VPS safely

1. Ask the user to type the temporary password only in the terminal prompt.
2. Run the read-only preflight script: `scripts/server_preflight.sh`.
3. Stop if the VPS has existing websites, databases, containers, user data, or unknown listeners.
4. Create a dedicated Ed25519 SSH key on the user's device. Keep the private key local.
5. Add the public key and verify a second SSH session while the first session stays open.
6. Change SSH authentication only after the key and KiwiVM recovery path both work.

Read [references/deployment-runbook.md](references/deployment-runbook.md) before any server mutation.

### Stage 3: deploy Reality

1. Confirm port 443 is free and the target OS is supported by the current installer.
2. Resolve the current `mack-a/v2ray-agent` commit, pin the downloaded installer to that commit, hash it, and inspect its system changes.
3. Present the install impact and rollback path; wait for approval.
4. Install only Xray-core with the menu option whose current label means no-domain Reality.
5. Generate fresh UUID, Reality keys, short ID, target, and share link. Never reuse repository examples or historical credentials.
6. Verify configuration syntax, service status, startup behavior, and listening port.
7. Import the node on one client and prove the exit is the Japan VPS before adding the US exit.

### Stage 4: purchase and test the US exit

1. Use `cliproxy.com` as the user's stated supplier. Read the live product page and confirm the exact plan before payment.
2. Confirm long-term static allocation, United States location, SOCKS5 support, authentication method, expiry, traffic limits, concurrent-device policy, UDP capability, refund terms, and regional restrictions.
3. Stop before payment. The user completes purchase and verification.
4. Test the SOCKS5 account from the VPS using `scripts/test_socks5.sh`; the password remains hidden and the temporary curl configuration is removed on exit.

### Stage 5: route Xray through SOCKS5

1. Back up `/etc/v2ray-agent` on the VPS with root-only permissions.
2. Inspect existing Xray routes and outbounds. Stop if custom WARP, IPv6, DNS, or other routing already exists.
3. Use the current `vasma` menu labels for SOCKS5 outbound and global forwarding; menu numbers may change.
4. Explain that global forwarding may replace existing split routes; wait for approval.
5. Enter the SOCKS5 password through the interactive terminal prompt.
6. Validate Xray syntax before reloading or restarting.
7. Verify that the original Reality client still connects and that two independent IP checks match the purchased US exit.
8. Revert to the backed-up direct configuration if the chain fails.

### Stage 6: configure clients

Read [references/client-and-acceptance.md](references/client-and-acceptance.md).

- Windows: use the official `2dust/v2rayN` release and import the local VLESS share link.
- Apple: use the user's own Apple ID and the App Store listing with ID `932747118`; import with a locally generated QR code.
- Start with the system proxy or normal proxy mode. Enable TUN only for a verified need and after user approval.

### Stage 7: accept and hand off

1. Run every acceptance check in the client reference.
2. Reboot the VPS once with user approval, then repeat SSH, service, Japan-entry, and US-exit checks.
3. Fill the non-secret execution record, renewal dates, restore path, pinned commit, hashes, versions, and remaining limits.
4. Store generated credentials in the user's password manager or encrypted storage.
5. Scan the repository and work log for secrets before any commit or share.

## Failure routing

Read [references/troubleshooting.md](references/troubleshooting.md) whenever a check fails. Diagnose one layer at a time:

```text
client → Reality inbound → Xray service → SOCKS5 account → destination
```

Restore the last verified layer before changing another layer. Reinstalling is a final recovery option for an empty VPS and still requires user approval.

## Completion response

Return a compact handoff with:

- architecture and current status;
- tests passed and tests not run;
- masked VPS and exit identifiers;
- versions, pinned commit, and installer hash;
- renewal dates and recovery route;
- known UDP, region, client, or vendor limits;
- exact next action if anything remains.
