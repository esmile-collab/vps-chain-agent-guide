# Client setup and acceptance

## Windows with v2rayN

Official source:

```text
https://github.com/2dust/v2rayN
https://github.com/2dust/v2rayN/releases
```

1. Detect x64 or ARM64 before choosing a release asset.
2. Verify the downloaded file comes from the official GitHub release.
3. Extract it to a stable folder; do not run the executable inside the archive.
4. Copy the protected `vless://` URI locally and import it from the clipboard.
5. Name the profile `JP-REALITY-US`, select it, and enable the system proxy.
6. Test browser access and the exact US exit IP.
7. Test one non-browser application the user actually needs.

Start with the system proxy. TUN needs administrator permission and can change routing for all applications. Enable it only after a specific application fails to follow the system proxy and the user approves.

## Apple devices with Shadowrocket

Official App Store identifier:

```text
https://apps.apple.com/us/app/shadowrocket/id932747118
App ID: 932747118
Developer: Shadow Launch Technology Limited
```

1. Check the listing, device compatibility, current price, and availability in the user's own App Store region.
2. The user buys with their own Apple ID. Do not use shared accounts, resale accounts, cracked packages, or third-party installers.
3. Generate a QR code locally from the VLESS URI. Store it outside Git.
4. Import, name the profile `JP-REALITY-US`, and allow the OS VPN configuration.
5. Test Wi-Fi and cellular data separately when both matter.

If Shadowrocket is unavailable for the user's legitimate account or device, choose a currently maintained client that explicitly supports VLESS, XTLS Vision, and Reality. Verify the official source on the execution day.

## Local QR requirement

The VLESS URI grants access. Never send it to a QR web service. Use a locally installed QR tool or the client clipboard import. Delete the plaintext image after protected backup and device import.

## Acceptance checklist

### Server

- [ ] KiwiVM emergency console opens.
- [ ] Dedicated SSH key login succeeds.
- [ ] SSH password authentication is rejected after key verification.
- [ ] Xray configuration test passes.
- [ ] Xray is active and enabled.
- [ ] Expected port is owned by Xray.
- [ ] No unauthenticated SOCKS5 inbound is exposed.
- [ ] Reboot recovery passes.

### Network path

- [ ] Reality works before the US exit is added.
- [ ] Direct exit matches the Japan VPS.
- [ ] Standalone SOCKS5 test matches the purchased US IP.
- [ ] Final Reality path matches the same US IP on two checks.
- [ ] DNS behavior is consistent with the intended proxy mode.
- [ ] Required TCP applications work.
- [ ] Required UDP applications were tested, or the limitation is recorded.

### Clients

- [ ] Windows browser works.
- [ ] One required Windows desktop application works.
- [ ] iPhone on Wi-Fi works, when applicable.
- [ ] iPhone on cellular works, when applicable.
- [ ] Mac works, when applicable.

### Handoff

- [ ] Full credentials are in encrypted user-controlled storage.
- [ ] Public Git and chats contain no secrets.
- [ ] VPS, exit, and client renewal or purchase dates are recorded.
- [ ] Commit SHA, installer hash, Xray version, client versions, and backup path are recorded.
- [ ] Known region, bandwidth, device-count, and UDP limits are recorded.

