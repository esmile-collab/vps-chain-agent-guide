# 模块协作架构：依据与维护

核对日期：2026-11-07。代码 / 文档基线：`6cd3806a07f233c35a0dddae4fae7c34a7d430c2`。

## 图源与读法

`architecture.svg` 是可编辑图源，README 直接展示；英文版本存在时同步维护。图片无动画、脚本、外部字体或图片依赖。
图中只保留模块名与连线。实线表示模块协作，包含调用、读写与评测依赖；双向箭头包含结果返回。虚线表示人工迭代。模块职责、接口数据与实现边界见下表。
图按当前职责分组，保留实际依赖与直接访问路径。

## 模块与协作依据

| 模块 | 对应文件 | 接口与边界 |
| --- | --- | --- |
| 宿主 Agent 与部署 Skill | [.agents/skills/vps-chain-deployer/SKILL.md](../.agents/skills/vps-chain-deployer/SKILL.md) | Agent 读取规则、执行命令、调用检查脚本并判断结果；Skill 规定选型、执行、失败路由与授权边界。 |
| 选型校验 | [.agents/skills/vps-chain-deployer/scripts/research_gate.py](../.agents/skills/vps-chain-deployer/scripts/research_gate.py) | 读取私有研究记录并检查证据与推荐条件；输出 READY、UNVERIFIED 或格式错误。 |
| 操作手册 | [.agents/skills/vps-chain-deployer/references/troubleshooting.md](../.agents/skills/vps-chain-deployer/references/troubleshooting.md) | 提供部署、分层排障与回退依据；由 Agent 阅读后执行，不将文档画成独立自动修复服务。 |
| 检查脚本 | [.agents/skills/vps-chain-deployer/scripts/security_postcheck.sh](../.agents/skills/vps-chain-deployer/scripts/security_postcheck.sh) | 与 preflight、SOCKS5 测试等脚本分别完成确定性检查，在授权环境采集结果返回 Agent。 |
| 私有记录 | [templates/execution-record.md](../templates/execution-record.md) | 保存研究、验收与问题信息，供 Agent 回看与恢复；具体实例与凭据不进入公开 Git。 |
| 规则维护 | [docs/known-compatibility.md](../docs/known-compatibility.md) | 通用问题经复核后更新规则或兼容记录，图中以人工修订虚线表示。 |

## 随代码维护

模块职责、调用方、输入输出、共享校验、持久化或回流方式变化时，在同一提交中更新 SVG、README 和本文。不要将人工操作写成自动模块，也不要删除仍然存在的耦合关系。
图片仅显示简短模块名。使用细框线和充分间距，保持简洁图例；具体职责、接口、路径与限制维护在本文。
提交前检查 XML 解析、文字边界、连线与节点、README 引用以及静态资源大小。代码行为没有变化时无需为图增加运行依赖。
