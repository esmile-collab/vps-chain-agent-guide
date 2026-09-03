# Agent 启动与能力检查

## 先确认运行环境

向用户确认：操作系统（macOS/Windows/Linux）、Agent 名称和版本、是否能读取本地仓库、是否能运行终端命令、是否能执行 SSH。只有能读取仓库并运行命令的本地 Agent 才能执行部署；网页聊天可用于计划和解释。

用户没有 Agent 时，给出 [docs/get-an-agent.md](../../../../docs/get-an-agent.md)，让用户从官方入口安装 Claude Code 或 Codex CLI。不要替用户选择账号、登录或接受服务条款。

## 启动验证

让用户在仓库目录运行：

```text
请先读取 README.md、AGENTS.md 和 .agents/skills/vps-chain-deployer/SKILL.md。
只回答：我的操作系统、你是否能读取本地文件、你是否能运行终端命令、你是否能通过 SSH 工作。不要连接服务器，也不要索取密码。
```

若任一项为否，停在计划阶段，并说明需要切换到具有本地终端权限的 Agent。若使用非官方模型网关，再执行 intake-and-gates.md 中的能力检查。
