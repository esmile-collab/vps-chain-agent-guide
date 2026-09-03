# VPS Chain Agent Guide

这是一个给个人用户用的“从公共机场迁移到自建节点”工具箱。先按需求和预算选网络路径，再让 Agent 帮你购买后的服务器完成部署、测试和交付。

默认服务端协议是 `VLESS + Reality`，无需域名和 Cloudflare。你可以选择直连、两台 VPS，或加一个固定的 ISP/家宽出口。

## 先看方案

| 你的情况 | 建议路径 | 预算参考（美元/月） |
| --- | --- | --- |
| 想低成本试用，能接受机房 IP | 一台海外服务器直接使用 | 3–15 |
| 更在意亚洲入口的稳定性 | 一台日本或其他亚洲服务器 | 10–35 |
| 需要固定的美国出口 | 亚洲服务器 + 固定美国网络出口 | 服务器 + 3–20 |
| 不能接受一个节点坏掉就中断 | 主服务器 + 备用服务器 | 在上面方案上再加一台服务器 |

价格是购买页面上的常见参考，库存、地区、税费和续费价格会变化。让 Agent 在付款前重新读取页面。方案比较见 [`docs/choose-a-plan.md`](docs/choose-a-plan.md)。

## 你需要准备

- 一台 Mac 或 Windows 电脑。手机和平板只负责使用节点，部署仍在电脑上完成。
- 一个可以运行 Claude Code、Codex 等 Agent 的环境。
- 一个 VPS 账号和付款方式（可从 [`docs/providers.md`](docs/providers.md) 选择）。
- 如果选择链式方案：一个支持认证 SOCKS5 的固定出口账号和付款方式。
- 如果使用 iPhone/iPad 客户端：自己的 Apple ID。

## 开始使用

### Mac

打开“终端”，运行：

```bash
git clone https://github.com/esmile-collab/vps-chain-agent-guide.git
cd vps-chain-agent-guide
claude
```

### Windows

在 PowerShell 中运行：

```powershell
git clone https://github.com/esmile-collab/vps-chain-agent-guide.git
cd vps-chain-agent-guide
claude
```

然后把这段话发给 Agent：

```text
请按仓库里的 vps-chain-deployer Skill，先按价格、稳定性、速度/延迟和功能支持逐项问我，再根据调研结果推荐直连、链式或双服务器方案，最后带我完成个人自建节点。
我不懂服务器，每次只问我一个问题。购买、付款、输入密码、重装、改防火墙、关闭密码登录、重启和开启全局代理前，先告诉我影响并等我确认。密码只让我在网页或终端的隐藏输入框里输入。先验证已选入口直连；只有选择链式方案时才接入出口，全部测试通过后再说完成。
```

如果电脑还没有 Agent，先看 [`docs/get-an-agent.md`](docs/get-an-agent.md)。只从官方页面安装；部署需要 Agent 能读取本地仓库、运行终端命令并在关键步骤等待确认。

## 你亲自完成的事

1. 注册账号、收验证码、确认服务条款和付款。
2. 选择并付款购买 VPS；确认地区、账期、流量和续费方式。
3. 如果使用链式方案，确认出口是固定 IP、目标国家、支持 SOCKS5 和认证。
4. 在网页或终端提示中亲自输入密码。
5. 按设备安装客户端：Windows 和 Mac 使用 v2rayN；iPhone/iPad 使用 Shadowrocket 或其他官方来源客户端。
6. 最后亲自测试网页、电脑和手机。

其他步骤由 Agent 完成。

## 购买和验收

- 只从供应商官网进入购买页，不使用陌生代理转售链接。
- 付款前让 Agent 核对当天的产品、价格、有效期、续费、退款和地区限制。
- 部署后按 [`docs/testing.md`](docs/testing.md) 检查出口国家/ASN、DNS、IPv6、WebRTC、延迟、丢包和速度。
- Windows 和 Mac 客户端使用 [v2rayN 官方发布页](https://github.com/2dust/v2rayN/releases)；官方项目明确支持 Windows、Linux 和 macOS。
- Apple 客户端使用 [Shadowrocket 官方 App Store 页面](https://apps.apple.com/us/app/shadowrocket/id932747118)。

## 请保管好

密码、SSH 私钥、完整节点链接、Reality 私钥、美国代理账号和二维码都不要发到聊天、截图、公共网站或 GitHub。

详细技术步骤由 `.agents/skills/vps-chain-deployer/` 提供，Agent 会按需读取。用户要看的最短流程见 [`docs/human-steps.md`](docs/human-steps.md)。

## 许可证

本仓库自有代码、Skill 和文档采用 [MIT License](LICENSE)。引用的第三方项目、客户端和服务仍遵循各自许可证与服务条款。
