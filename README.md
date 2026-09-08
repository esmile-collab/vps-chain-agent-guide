# VPS Chain Agent Guide

一套面向个人自建网络节点的 Agent 工作流。

项目把需求判断、产品调研、VPS 部署、客户端配置、安全检查、网络测试和故障交接整理成可执行的 Skill、操作手册与检查脚本。没有网络或服务器经验的用户可以由 Agent 一步步带着完成；开发者可以直接检查和复用其中的决策规则、执行流程与安全边界。

## 直接交给 Agent

把下面这段复制给 Claude Code、Codex 或其他能读取仓库并操作本机终端的 Agent：

```text
请读取并按照这个项目接手我的个人网络节点搭建：
https://github.com/esmile-collab/vps-chain-agent-guide

我可能完全不懂网络，也可能不知道自己需要什么。请先检查你是否具备仓库读取、网页查询、本机终端和服务器连接能力，然后一次只问我一个日常问题。先了解设备、用途、预算和当前困扰，再按仓库要求留下即时研究记录并运行推荐门槛；关键证据缺失时标记“未验证”。门槛通过后最多给我两个方案，并按安全规则带我完成购买、部署、客户端配置、测试和交接。
```

完整启动指令见 [`docs/start-with-agent.md`](docs/start-with-agent.md)。电脑还没有 Agent，先看 [`docs/get-an-agent.md`](docs/get-an-agent.md)。

## 这个项目解决什么

公共节点通常省事，但线路、出口和维护都由第三方控制。希望提高稳定性、独占使用、固定出口地区或掌握网络配置时，用户需要同时处理产品选购、服务器部署、客户端适配和长期维护。

本项目让 Agent 负责以下工作：

| 阶段 | Agent 交付 |
| --- | --- |
| 了解需求 | 用日常问题确认预算、设备、用途、稳定性和地区要求 |
| 选择方案 | 调查当天可购买产品，留下来源、原文和核验时间；硬门槛通过后才给推荐 |
| 部署服务器 | 完成只读预检、备份、安装、配置和服务验证 |
| 配置设备 | 指导 Windows、macOS、Linux、Android、iPhone、iPad 和电视使用 |
| 安全与验收 | 检查密钥、端口、IP、DNS、延迟、丢包、速度和必要的 UDP 能力 |
| 长期维护 | 记录版本、续费日期、恢复入口、回退点和已知限制 |

需要注册、验证身份、付款、输入密码或批准高风险改动时，Agent 会停下来让用户处理。详细的人机分工见 [`docs/human-steps.md`](docs/human-steps.md)。

## 适合谁

### 想自己搭节点的普通用户

- 正在从公共“机场”迁移，希望获得一套自己管理的节点。
- 更关心价格、稳定性、速度和实际能否使用，不想先学习网络术语。
- 需要覆盖电脑、手机或电视，希望 Agent 负责技术判断和排障。
- 需要固定国家出口、备用节点或更可控的网络路径。

### 想了解或复用项目的开发者

- 希望查看一套 Agent 如何完成需求采集、方案选择和高风险操作确认。
- 需要可审计的服务器部署 Runbook、安全门、验收标准和交付模板。
- 想把本项目的 Skill 复制到 Claude Code、Codex 或兼容 Agents 的工作环境。
- 计划扩展供应商、客户端、检测项或新的网络路径。

## 当前支持的方案

默认服务端入口采用 `VLESS + Reality + Vision`，无需用户准备域名或配置 Cloudflare。

```text
单服务器：设备 → VLESS + Reality → VPS → 目标网站

固定出口：设备 → VLESS + Reality → 入口 VPS
                         → 带认证的固定 SOCKS5 / ISP 出口
                         → 目标网站
```

Agent 会先判断单服务器能否满足需求。只有用户确实需要固定地区出口，并接受额外费用和故障点时，才增加链式出口。也可以增加第二台 VPS 作为出口或备用节点。

主要客户端：

- Windows、macOS、Linux：v2rayN 或 Hiddify
- Android：v2rayNG 或 Hiddify
- iPhone、iPad：Shadowrocket 或 Hiddify
- 电视：根据电视系统和共享网络方式单独判断

电视代理等特殊场景的已知版本差异记录在 [`docs/known-compatibility.md`](docs/known-compatibility.md)。当前记录包含 `v2rayN 7.23.2` 的实测线索与旧版本安全风险，不能直接当成所有设备的默认版本。

## Agent 原生设计

这个仓库既是说明文档，也是 Agent 可以直接执行的工作区：

- [`AGENTS.md`](AGENTS.md)：规定对话方式、人工确认、凭据处理和禁止范围。
- [`.agents/skills/vps-chain-deployer/SKILL.md`](.agents/skills/vps-chain-deployer/SKILL.md)：完整的选购、部署、组链、客户端和验收流程。
- [`.agents/skills/vps-chain-deployer/references/`](.agents/skills/vps-chain-deployer/references/)：按执行阶段提供供应商、部署、安全、测试和排障上下文。
- [`.agents/skills/vps-chain-deployer/scripts/`](.agents/skills/vps-chain-deployer/scripts/)：服务器预检、安全复查、出口测试等确定性检查。
- [`templates/research-record.json`](templates/research-record.json)：单次选购研究的非密钥记录结构。
- [`templates/execution-record.md`](templates/execution-record.md)：不含密钥的执行和交付记录。

Agent 先读取当前阶段需要的上下文，再执行对应检查。结账价格、续费、关键限制或线路实测缺失时，研究门槛会返回“未验证”，Agent 不能直接推荐。购买、重装、第三方脚本、防火墙、SSH、重启和设备全局网络等操作都设有人工确认门。

## 文档入口

面向使用者：

- [`docs/start-with-agent.md`](docs/start-with-agent.md)：复制给 Agent 的完整启动指令
- [`docs/choose-a-plan.md`](docs/choose-a-plan.md)：Agent 如何从日常问题判断用户需要什么
- [`docs/providers.md`](docs/providers.md)：供应商来源、即时核验项和推荐门槛
- [`docs/get-an-agent.md`](docs/get-an-agent.md)：Mac、Windows 从零安装 Agent
- [`docs/human-steps.md`](docs/human-steps.md)：必须由用户完成的动作
- [`docs/clients.md`](docs/clients.md)：电脑、手机和平板客户端
- [`docs/testing.md`](docs/testing.md)：网络质量和隐私泄漏检查
- [`docs/security.md`](docs/security.md)：凭据、第三方安装和故障恢复

面向 Agent 与开发者：

- [`deployment-runbook.md`](.agents/skills/vps-chain-deployer/references/deployment-runbook.md)：服务器部署步骤
- [`plan-selector.md`](.agents/skills/vps-chain-deployer/references/plan-selector.md)：方案决策规则
- [`provider-matrix.md`](.agents/skills/vps-chain-deployer/references/provider-matrix.md)：供应商官网入口和必查项目注册表
- [`research-and-decision-gates.md`](.agents/skills/vps-chain-deployer/references/research-and-decision-gates.md)：即时研究记录和推荐硬门槛
- [`client-and-acceptance.md`](.agents/skills/vps-chain-deployer/references/client-and-acceptance.md)：客户端和验收门
- [`security-playbook.md`](.agents/skills/vps-chain-deployer/references/security-playbook.md)：高风险操作与恢复流程
- [`troubleshooting.md`](.agents/skills/vps-chain-deployer/references/troubleshooting.md)：分层排障路径

## 安全与边界

项目只用于用户本人拥有或明确获授权的服务器、代理账号和设备。它不支持公开代理、共享售卖、扫描、攻击、流量劫持、凭据收集或绕过平台风控。

密码、验证码、SSH 私钥、完整节点链接、Reality 私钥、固定出口密码和二维码不能进入聊天、Git、截图或公共网站。Agent 在可能中断服务或改变安全状态前，必须说明影响、回退方式并获得确认。

## 验证与开发

在仓库根目录运行：

```bash
bash scripts/validate.sh
```

校验包含 Skill 元数据、本地文档链接、Shell 语法、敏感信息扫描和仓库风格检查。任何部署仍需在用户真实服务器、网络和设备上完成验收。

## 许可证

本仓库自有代码、Skill 和文档采用 [MIT License](LICENSE)。第三方软件与服务遵循各自许可证和服务条款。
