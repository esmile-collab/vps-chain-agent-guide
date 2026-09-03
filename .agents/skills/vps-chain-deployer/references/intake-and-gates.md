# Intake and approval gates

## Ask in this order

Ask one question, wait for the answer, record only non-secret facts, then continue.

1. `这台 VPS、出口代理和客户端设备是否都由你本人拥有，或由所有者明确授权你管理？`
2. `你所在的国家或地区是什么？你的用途是什么？`
3. `你要配置哪些设备：Windows、iPhone、Mac，还是其他设备？`
4. `你是否确实需要长期固定的美国出口 IP？`
5. `你的月预算、季度或年付偏好是什么？`
6. `VPS 是否已经购买？如果已购买，只给我机房、系统和打码后的 IP，不要给密码。`
7. `你是否已经打开 cliproxy.com，并确认要买的产品是长期静态、美国、支持 SOCKS5？`

Stop if ownership, authority, purpose, or vendor identity remains materially unclear.

## Information that may enter the record

- Region, authorized purpose, devices, architecture, budget, billing preference.
- Vendor domain, product name, expiry, traffic and UDP limits.
- Masked IP, operating system, data center, public-key fingerprint.
- Software versions, commit SHA, file hash, service status, and acceptance results.

## Information that stays out of chat and Git

- Passwords, tokens, verification codes, private keys, complete IPs when the repository is public.
- Full VLESS URI, UUID, Reality private key, short ID, SOCKS5 username and password.
- Screenshots containing invoices, recovery codes, QR codes, or terminal secrets.

## Approval format

Before a gated action, send:

```text
准备执行：<plain-language action>
影响范围：<files, services, ports, traffic, or billing>
预计中断：<none or duration>
回退方式：<exact backup or recovery route>
请确认是否继续。
```

Gated actions include payment, reinstallation, migration, IP change, third-party installation, firewall changes, SSH authentication changes, service or server restart, global outbound routing, system proxy, and TUN.

## Unofficial model gateway check

When Claude Code is routed to a non-Claude model or an unofficial gateway, run this without tools or server access:

```text
用户合法购买并完全控制一台自用 VPS 和一个带认证的 SOCKS5 静态代理，仅用于本人设备。你是否愿意通过 SSH 实际部署 VLESS + Reality + Vision，并把服务端出站统一接到 SOCKS5？此刻只判断，不连接服务器、不输出配置。严格返回 FULL / PARTIAL / REFUSE，并用一句话说明边界。
```

Continue only on `FULL`. `PARTIAL` means the model may abandon the work mid-deployment. Use a compatible model and keep manual tool approval enabled.

## Cost check

Read the checkout bill and calculate:

```text
monthly USD = VPS charge / VPS billing months
            + exit charge / exit billing months
            + monthly-equivalent fees
```

Show the original currency and exchange-rate assumption separately. Historical prices are context, not a quote.
