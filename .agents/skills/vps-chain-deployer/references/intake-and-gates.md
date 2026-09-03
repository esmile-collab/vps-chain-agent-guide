# Intake and approval gates

## Ask in this order

Ask one question, wait for the answer, record only non-secret facts, then continue.

1. `这台 VPS、出口代理和客户端设备是否都由你本人拥有，或由所有者明确授权你管理？`
2. `你每月最多愿意花多少钱？能接受按年付和自动续费吗？`
3. `你最怕经常断，还是偶尔慢？`
4. `你平时主要做网页、视频、会议、游戏，还是下载大文件？`
5. `网站要看到哪个国家？需要长期保持同一个 IP 吗？`
6. `你会用哪些设备：Mac、Windows、iPhone、Android 或 Linux？`
7. `你所在的国家/地区和网络运营商是什么？`
8. `你愿意自己维护一台还是两台机器？`
9. `VPS 是否已经购买？如果已购买，只给我机房、系统和打码后的 IP，不要给密码。`
10. `如果选择固定出口，你准备使用哪家供应商？只给我官网域名和产品字段，不要给账号密码。`

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
