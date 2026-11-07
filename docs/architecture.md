# VPS 搭建 Agent：架构图依据与维护

核对日期：2026-11-07。代码 / 文档基线：`28203c6a266e1e4b71075e4f14eb57e43716108d`。

## 图源

`architecture.svg` 是可编辑图源，README 直接展示。图中没有脚本、动画、外部字体或图片依赖。
实线表示已有代码关系或仓库规定的 Skill 流程；虚线表示人工处理、人工维护或下一次发起。蓝色突出评测问题和反馈回路。

## 模块与证据

| 图中关系 | 对应文件 | 已核对的范围 |
| --- | --- | --- |
| 总体执行与失败路由 | [.agents/skills/vps-chain-deployer/SKILL.md](../.agents/skills/vps-chain-deployer/SKILL.md) | 已有 Skill 流程，按阶段验收；失败后分层排障并恢复已验证层。 |
| 方案证据门槛 | [.agents/skills/vps-chain-deployer/scripts/research_gate.py](../.agents/skills/vps-chain-deployer/scripts/research_gate.py) | 证据缺失返回未验证；不凭历史价格或未核对线路直接给推荐。 |
| 纠错与回退 | [.agents/skills/vps-chain-deployer/references/troubleshooting.md](../.agents/skills/vps-chain-deployer/references/troubleshooting.md) | 收集证据、恢复上个已验证层、一次改一个变量；高风险操作按授权规则执行。 |
| 问题沉淀与交付 | [templates/execution-record.md](../templates/execution-record.md) | 记录验收、版本、回退与仍待处理项；具体实例与凭据留在私有目录。 |
| 可复用兼容性经验 | [docs/known-compatibility.md](../docs/known-compatibility.md) | 通用问题经复核后由维护者更新，不能将个别版本表现扩展为全部版本结论。 |

## 当前边界

- Skill 规定流程；Agent 执行检查，高风险修改由用户确认。
- 出现失败先恢复已验证层；凭据和具体实例记录保留在仓库外。
- 本次只核对仓库流程，没有连接或修改任何服务器。
- 通用经验经复核后维护到文档；具体实例记录不进入公开 Git。

## 随代码维护

输入输出、模块调用、评测门槛、记录位置或反馈路径变化时，在同一提交内更新 SVG、对应 README 与本文件。人工环节保留虚线；只有代码已经实现自动执行后才改为实线。
直接编辑 SVG 中的文字、节点与路径，保持全部信息默认可见。英文图存在时同步更新。提交前检查 XML 能解析、文字与箭头不重叠、README 图片路径有效，且图中每条回流都有代码或现有流程依据。
