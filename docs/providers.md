# VPS 和固定出口怎么选

这个项目不保存长期价格表。价格、库存、续费和线路都会变化，Agent 要在你提出需求的当天重新查，并留下可复查的研究记录。

## Agent 从哪里开始查

仓库里的 [供应商来源注册表](../.agents/skills/vps-chain-deployer/references/provider-matrix.md) 保存官网产品页、结账入口、条款、状态页和线路测试入口。当前候选包括 BandwagonHost、DMIT、RackNerd、Hetzner Cloud，以及 ClipProxy、IPRoyal、Decodo 和 Bright Data。

[DigVPS 服务器测评总表](https://digvps.com/review) 可用于发现其他商户和查看历史测评。它不能代替供应商官网的实时账单、条款、库存和用户本地线路测试。

## 每次都要重新核验什么

VPS 至少核验：

- 结账页这次实际付款、币种、税费和账期；
- 续费金额、周期、自动续费和取消方式；
- 购买地区和当前库存；
- IPv4、流量/FUP、退款、迁移和可接受用途；
- 从用户实际网络到目标机房的延迟、丢包和晚高峰表现。

固定 ISP/SOCKS5 出口还要核验：

- IP 是否长期静态、是否独享、目标国家和 ASN 类型；
- SOCKS5、认证、并发、流量和 UDP 支持；
- 到期/续费、退款、KYC、用途和地区限制；
- 从入口 VPS 到出口的实际连接与性能。

## 什么情况下可以推荐

Agent 使用 [即时研究与推荐门槛](../.agents/skills/vps-chain-deployer/references/research-and-decision-gates.md) 留下来源、核验时间、短原文、测试结果和未确认项。

结账金额、续费规则、库存、关键限制或线路测试缺失时，结果必须显示 `未验证`。此时 Agent 只能告诉你候选和最小补证动作，不能让你直接购买。

门槛通过后，Agent 最多给一个推荐和一个备选，并写清：

```text
状态：可推荐
本次实际付款：
续费和自动续费规则：
折算月均：
线路测试：
流量、IPv4、退款和用途限制：
官网来源与核验时间：
仍可能遇到的问题：
需要你亲自完成：
```

注册、验证码、实名、条款确认和付款始终由你本人完成。
