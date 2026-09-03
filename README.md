# VPS Chain Agent Guide

这是一个让 AI Agent 帮你搭建个人链式代理的项目。

网络路径：

```text
电脑或手机 → 日本 VPS → 美国固定 SOCKS5 出口 → 网站
```

服务端只部署 `VLESS + Reality`，不需要域名，也不需要 Cloudflare。

## 你需要准备

- 一台 Windows 电脑。
- 一个可以运行 Claude Code、Codex 等 Agent 的环境。
- 搬瓦工账号和付款方式。
- 一个美国长期静态 SOCKS5 出口账号和付款方式。
- 如果使用 iPhone 或 Mac：自己的 Apple ID。

## 开始使用

在 PowerShell 中运行：

```powershell
git clone https://github.com/esmile-collab/vps-chain-agent-guide.git
cd vps-chain-agent-guide
claude
```

然后把这段话发给 Agent：

```text
请按仓库里的 vps-chain-deployer Skill，带我从零完成个人 VPS 链式代理。
我不懂服务器，每次只问我一个问题。购买、付款、输入密码、重装、改防火墙、关闭密码登录、重启和开启全局代理前，先告诉我影响并等我确认。密码只让我在网页或终端的隐藏输入框里输入。先验证日本直连，再接美国 SOCKS5，全部测试通过后再说完成。
```

如果电脑还没有 Agent，先安装官方 Claude Code 或 Codex；不要从陌生网盘下载客户端。

## 你亲自完成的事

1. 注册账号、收验证码、确认服务条款和付款。
2. 确认搬瓦工买的是日本 VPS。
3. 确认美国出口买的是长期静态、支持 SOCKS5 的产品。
4. 在网页或终端提示中亲自输入密码。
5. 安装 Windows 客户端；Apple 设备从官方 App Store 安装客户端。
6. 最后亲自测试网页、电脑和手机。

其他步骤由 Agent 完成。

## 购买时记住

- VPS 只从 [搬瓦工官网](https://bandwagonhost.com/)进入。
- 美国出口供应商是 `cliproxy.com`。付款前让 Agent 核对当天的产品、价格、有效期和地区限制。
- 美国出口要确认 `static`、`United States`、`SOCKS5`、认证方式和到期日。
- Windows 客户端使用 [v2rayN 官方发布页](https://github.com/2dust/v2rayN/releases)。
- Apple 客户端使用 [Shadowrocket 官方 App Store 页面](https://apps.apple.com/us/app/shadowrocket/id932747118)。

## 请保管好

密码、SSH 私钥、完整节点链接、Reality 私钥、美国代理账号和二维码都不要发到聊天、截图、公共网站或 GitHub。

详细技术步骤由 `.agents/skills/vps-chain-deployer/` 提供，Agent 会按需读取。
