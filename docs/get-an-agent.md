# 电脑还没装 Agent？从这里开始

这个项目需要一个能在你电脑上读文件、运行命令的 AI Agent。普通网页聊天可以回答问题，但通常不能直接替你配置服务器。

你只要安装 Claude Code 或 Codex 其中一个。拿不准就选自己已经有账号、能够正常登录的那个，不用两个都装。

## 开始前

准备一台 Mac 或 Windows 电脑，并确认：

- 你能安装软件；
- 你有稳定网络；
- 电脑里没有公司禁止 Agent 读取的资料，或者你会把项目放在单独文件夹；
- 你愿意在 Agent 执行命令前看清它要做什么。

Agent 可能看到当前项目文件和终端输出。不要让它读取密码管理器、私人文档或与本项目无关的文件夹。

## 选择一：Claude Code

官方安装说明：[Claude Code Quickstart](https://code.claude.com/docs/en/quickstart)

### Mac

1. 按 `Command + 空格`，搜索并打开“终端”。
2. 复制下面一行，粘贴后按回车：

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

3. 安装结束后输入：

```bash
claude
```

4. 按屏幕提示登录。

### Windows

1. 打开开始菜单，搜索 `PowerShell` 并打开。
2. 复制下面一行，粘贴后按回车：

```powershell
irm https://claude.ai/install.ps1 | iex
```

3. 安装结束后关闭 PowerShell，再重新打开，输入：

```powershell
claude
```

4. 按屏幕提示登录。

如果提示缺少 Git，先从 [Git for Windows 官网](https://git-scm.com/download/win) 安装，再重新打开 PowerShell。

## 选择二：Codex

官方说明：[OpenAI Codex CLI](https://learn.chatgpt.com/docs/codex/cli)，官方源码：[openai/codex](https://github.com/openai/codex)。

### Mac

1. 打开“终端”。
2. 运行：

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

3. 安装结束后运行：

```bash
codex
```

4. 按屏幕提示登录。

### Windows

1. 打开 PowerShell。
2. 运行：

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

3. 安装结束后关闭 PowerShell，再重新打开，输入：

```powershell
codex
```

4. 按屏幕提示登录。

安装方式可能随版本变化。如果命令失效，回到上面的官方说明核对当天推荐方法。

## 检查是否装好了

Claude Code 用户运行：

```bash
claude --version
```

Codex 用户运行：

```bash
codex --version
```

能看到版本号，说明 Agent 已能启动。看到“找不到命令”时，把完整报错发给普通聊天窗口，让它按你的 Mac 或 Windows 继续排查；不要反复安装很多来源不明的版本。

## 下载这个项目

还需要 Git。先运行：

```bash
git --version
```

能看到版本号后，运行：

```bash
git clone https://github.com/esmile-collab/vps-chain-agent-guide.git
cd vps-chain-agent-guide
```

然后输入 `claude` 或 `codex`。启动成功后，复制 README 里的整段启动提示。

## 先让 Agent 自检

第一次对话可以补一句：

```text
开始前先检查你能否读取当前仓库、运行本机终端命令，以及在需要时连接我有权管理的服务器。只报告检查结果，先不要修改电脑或服务器。
```

如果它只能聊天，或者明确说没有文件、终端和服务器连接能力，它仍能帮你比较购买方案，但不能完成自动部署。换到有这些能力的本地 Agent 后再继续。

## 三条安全提醒

- 只从上面的官方页面安装，不使用群文件、网盘包或陌生人提供的一键脚本。
- 支付密码、验证码、服务器临时密码和连接二维码不要粘贴进聊天。
- Agent 要重装、删除、修改防火墙或改变登录方式时，先让它解释影响和恢复方法，再决定是否同意。
