# 模块协作架构：依据与维护

核对日期：2026-11-07。代码 / 文档基线：`36babe1d567a66a943686ae3ee333fd21ffd03ae`。

## 图源与读法

`architecture.svg` 是可编辑图源，README 直接展示；英文版本存在时同步维护。图片无动画、脚本、外部字体或图片依赖。
块表示可定位的代码职责、Skill、文档或数据资源；块内只保留模块名、职责或接口。连线标注传递的数据或调用内容，双向箭头表示调用 / 读取与结果返回。蓝线突出评测与回读，虚线仅表示人工修订。
图按当前实现分组，不据此宣称所有模块已完全解耦。现有依赖与直接访问路径保留在图和下表中。

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
图中文字采用短名词和短职责；具体路径与限制留在本文。连线优先写接口内容，例如脚本请求、分镜、快照和运行记录。
提交前检查 XML 解析、文字边界、连线与节点、README 引用以及静态资源大小。代码行为没有变化时无需为图增加运行依赖。
