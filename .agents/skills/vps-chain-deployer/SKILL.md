---
name: vps-chain-deployer
description: Select and execute an authorized personal self-hosted network plan, from direct VPS to a VLESS Reality chain with an authenticated static SOCKS5 or ISP exit, then configure clients, test, maintain, and troubleshoot it. Use when a beginner asks an Agent to compare VPS providers, choose a route, configure Xray or v2ray-agent, or use v2rayN or Shadowrocket. Stop public-proxy, resale, attack, evasion, credential-harvesting, and unauthorized-system requests.
---

# VPS Chain Deployer

## Goal

Complete and verify one personal network plan on assets the user owns or is authorized to manage:

```text
direct: device → VLESS + Reality + Vision → VPS → website
chain:  device → VLESS + Reality + Vision → entry VPS → authenticated SOCKS5/ISP exit → website
```

The default server inbound is one `VLESS + Reality + Vision` entry and does not need a domain or Cloudflare. Choose direct first when a fixed foreign exit is not needed. Add an authenticated static SOCKS5/ISP exit only after the user confirms the extra cost and failure layer. A second VPS can be used as an exit or backup when the user explicitly accepts the extra maintenance.

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
4. If a chain is selected, the user accepts that it has an extra failure point and that either hop can interrupt service.

Stop out-of-scope capability work. You may still help shut down services, revoke credentials, or recover the user's server.

## Secret rules

- Never request payment credentials, email passwords, Apple ID passwords, one-time codes, SSH private keys, full VLESS links, Reality private keys, or SOCKS5 passwords in chat.
- Have the user type passwords into a hidden local terminal prompt.
- Keep secrets out of command-line arguments, shell history, Git, screenshots, QR websites, and execution records.
- Generate QR codes locally and store them outside the repository.
- If any credential appeared publicly, rotate it before continuing.

Read [references/agent-bootstrap.md](references/agent-bootstrap.md) and [references/intake-and-gates.md](references/intake-and-gates.md) before collecting inputs or asking for approval. Read [references/plan-selector.md](references/plan-selector.md) before recommending a provider or topology.

## Workflow

### Stage 0: choose the plan and initialize

1. Create a private local working directory outside the public repository for logs and generated credentials.
2. Copy the non-secret project brief and execution-record templates.
3. Verify the local Agent can read this repository, run terminal commands, and use SSH. If the user has no Agent, pause and provide [docs/get-an-agent.md](../../../docs/get-an-agent.md).
4. Ask one question at a time about location/ISP, target country, fixed-IP need, devices, UDP need, traffic volume, maintenance tolerance, budget, and billing preference.
5. Compare direct VPS, entry-plus-static-SOCKS5/ISP, two-VPS, and backup-entry paths. Read [references/plan-selector.md](references/plan-selector.md) and [references/provider-matrix.md](references/provider-matrix.md). Give one recommended plan and one fallback; do not force a chain.
6. If the Agent uses an unofficial model gateway, run the capability and willingness check in the intake reference before connecting to a server.

### Stage 1: compare and purchase the VPS

1. Navigate only to a provider's official page. Common starting points are BandwagonHost, DMIT Tokyo, RackNerd, and Hetzner Cloud; read [references/provider-matrix.md](references/provider-matrix.md).
2. Read the live checkout page. Confirm billing period, total, available location, traffic limit, refund terms, renewal behavior, IPv4 availability, and whether the route fits the user's location.
3. Recalculate monthly cost from the live bill. Do not reuse historical prices.
4. Stop before final purchase. The user accepts terms, completes verification, and pays.
5. After activation, verify the provider control panel, selected location, public IPv4, OS, traffic reset date, and recovery console. For BandwagonHost this includes KiwiVM.

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

### Stage 4: purchase and test an optional exit

1. If the selected plan has an exit, use the supplier the user selected. `cliproxy.com` is one starting point; alternatives and terminology are in [references/provider-matrix.md](references/provider-matrix.md). Read the live product page and confirm the exact plan before payment.
2. Confirm static allocation, target location, SOCKS5 support, authentication method, expiry, traffic limits, concurrent-device policy, UDP capability, refund terms, KYC, acceptable-use and regional restrictions.
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

- Windows and macOS: use the official `2dust/v2rayN` release and import the local VLESS share link. Choose the release asset matching x64 or arm64.
- Apple: use the user's own Apple ID and the App Store listing with ID `932747118`; import with a locally generated QR code.
- Start with the system proxy or normal proxy mode. Enable TUN only for a verified need and after user approval.

### Stage 7: accept and hand off

1. Run every acceptance check in the client reference and [references/network-testing.md](references/network-testing.md).
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
