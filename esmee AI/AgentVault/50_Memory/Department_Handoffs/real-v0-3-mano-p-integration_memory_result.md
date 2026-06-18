---
type: department_handoff_result
date: 2026-06-17
department: 记忆部
task_id: real-v0-3-mano-p-integration
status: recommend_route_doc
related_handoff: AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_memory.md
related_action_memory: AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-48_记忆部_real-v0-3-mano-p-integration.md
reference_project:
  - https://github.com/Mininglamp-AI/Mano-P
---

# 交接结果：real-v0-3-mano-p-integration - 记忆部

## status

recommend_route_doc

## 已读取资料

- `AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_memory.md`
- `AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-42_总控办公室_clarify-gui-reference-mano-p.md`
- `AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_memory_result.md`
- `AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_engineering.md`
- `https://github.com/Mininglamp-AI/Mano-P`
- `https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/README.md`
- `https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/LICENSE`

## 记忆判断

Mano-P 不应只停留在聊天上下文或单条行动记忆中。它与 esmee AI 的 GUI 自动化路线高度相关，应该进入正式路线记录，但当前不建议直接作为代码依赖接入。

建议定位为：

- `参考项目`：立即成立。记录 Mano-P 的 GUI-VLA、Private AI、本地推理、长任务 GUI 自动化、think-act-verify、视觉驱动操作等方向。
- `PoC 候选`：成立，但需工程部、安全部、GUI 自动化部结果回写后再定最小 PoC 范围。
- `可复用依赖`：暂不成立。公开资料显示 Mano-P 采用分阶段开源路线，模型和 SDK 并非当前即可无条件接入；直接接入前需要确认可用组件、许可证、模型/权重、运行环境和隐私边界。

## 记忆固化路径

建议下一步新建或更新正式路线文档，而不是只创建参考碎片：

- 首选：`AgentVault/00_System/GUI_Automation_Route.md`
- 备选：`AgentVault/00_System/Mano-P_Integration_Route.md`

建议路线文档至少包含：

- 来源和链接。
- 当前定位：参考项目 / PoC 候选 / 可复用依赖。
- 许可证：Apache-2.0，仍需安全部复核第三方依赖、模型权重和数据许可。
- 可借鉴能力：本地优先、视觉 GUI 操作、长任务规划执行、think-act-verify、跨 App/浏览器自动化。
- 禁止事项：不克隆、不安装、不写 adapter、不接入模型/SDK，除非工程部和安全部先给出 PoC 许可。
- 下一步：等待 GUI、工程、安全、技能优化部 result 汇总后，由总控办公室决定是否立 PoC。

## 与 thread-id 未提交讨论文件的关系

Mano-P 路线记录和 thread-id 脱敏是两个独立议题，但都处在当前未提交的 v0.3 讨论资产批次中。

建议处理顺序：

1. 先处理 thread-id 暴露议题：正式 registry 脱敏、真实 thread id 迁入本地私有 registry。
2. 再提交或固化 Mano-P 路线文档，确保新路线文档不引用真实 thread id、窗口 id 或内部会话入口。
3. 两个议题的审计链路用 `task_id`、`related_handoff`、`related_action_memory` 和 result 路径连接，不用真实 thread id 连接。

不建议把 Mano-P 路线内容写进 thread-id 脱敏文件；也不建议把 thread-id 私有 registry 设计写进 Mano-P 路线文档。

## 是否阻断

不阻断继续讨论 Mano-P。

阻断直接接入：在工程部、安全部和 GUI 自动化部完成 result 前，不应 clone、安装、改仓库结构或把 Mano-P 作为正式依赖。

## 下一步建议

- 等五部门 result 回收后，由总控办公室决定是否创建 `GUI_Automation_Route.md` 或 `Mano-P_Integration_Route.md`。
- 若进入 PoC，应先写 PoC checklist，明确“不复制实现、不外发数据、不启动 GUI 自动化、不下载模型/权重，除非用户确认”。
- 技能优化部可后续把“参考项目 / PoC 候选 / 可复用依赖”的分级写成通用评估模板。

## 禁止事项遵守

- 未修改已有正式路线文档。
- 未删除文件。
- 未提交、未 push。
- 未 clone Mano-P。
- 未安装依赖。
