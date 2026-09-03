# 还没装 Agent？按这个顺序

部署需要一个能在本机读取仓库、运行终端命令、通过 SSH 操作 VPS 的 Agent。普通网页聊天可以帮你理解步骤，但没有本地终端权限时，无法替你完成服务器部署。

## 选一个入口

### Claude Code

官方安装说明：[Claude Code Quickstart](https://code.claude.com/docs/en/quickstart)

打开电脑终端：

```bash
# Mac / Linux
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell：

```powershell
irm https://claude.ai/install.ps1 | iex
```

安装后运行 `claude`，按提示登录。Windows 若遇到终端兼容问题，先安装 [Git for Windows](https://git-scm.com/download/win)，再重新打开 PowerShell 或 Git Bash。

### Codex CLI

官方说明：[OpenAI Codex CLI](https://help.openai.com/en/articles/11096431)，源码和发布页：[openai/codex](https://github.com/openai/codex)。

先确认电脑有 Node.js；没有就从 [Node.js 官网](https://nodejs.org/en/download) 安装 LTS 版本。然后在终端运行：

```bash
npm install -g @openai/codex
codex
```

按提示登录。Codex CLI 在本机终端运行，能读取仓库和执行命令后，才能承担本项目的部署工作。

## 安装后先做三件事

1. 运行 `git --version` 和 `claude --version` 或 `codex --version`，确认命令存在。Mac 若没有 Git，按系统提示安装 Command Line Tools；Windows 从 [Git for Windows](https://git-scm.com/download/win) 安装。
2. `git clone` 本仓库并进入目录。
3. 启动 Agent 后粘贴 README 里的启动提示，让它先识别你的系统、设备和网络需求。

如果 Agent 只能聊天、无法读取本地文件或运行 SSH，先让它生成购买清单和操作计划；服务器变更等有本地终端能力的 Agent 再执行。

## 不要这样做

- 不从网盘、群聊或不明脚本安装 Agent。
- 不把 VPS 密码、SSH 私钥、完整节点链接粘贴给网页聊天。
- 不让 Agent 在你不知情时付款、重装系统、改防火墙或开启全局代理。
