---
type: department_discussion_summary
task_id: real-v0-3-thread-id-exposure
date: 2026-06-17
owner_department: 总控办公室
status: completed
risk_level: medium
current_mode: 坤-兑
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-32_总控办公室_department-discuss-thread-id-exposure.md
related_results:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_safety_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_memory_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_engineering_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_skillopt_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_gui_result.md
---

# 讨论汇总：真实 thread id 外发边界

## 1. 讨论问题

`Department_Thread_Registry.md` 已作为正式资产推送到远端，其中包含真实 Codex thread id。各部门需要判断这些 id 是否应继续作为远端正式资产保存，以及后续应如何处理。

## 2. 部门结论

| 部门 | 结论状态 | 核心建议 |
| --- | --- | --- |
| 安全部 | `recommend_redact` | thread id 不是密钥，但属于内部调度元数据；建议脱敏，不默认历史重写。 |
| 记忆部 | `recommend_private_registry` | 正式 registry 用别名；真实 id 迁入本地私有 registry；审计链路依靠 task id、handoff、result 和行动记忆。 |
| 工程部 | `recommend_redact_commit` | 默认采用普通提交脱敏；历史重写只在高敏或公开暴露确认后考虑。 |
| 技能优化部 | `recommend_update_skill` | 更新 `$obsidian-memory` 草稿/模板，加入内部调度元数据脱敏检查。 |
| GUI 自动化部 | `recommend_no_gui` | 第一轮不需要 GUI；如需确认仓库可见性，优先用只读 API/CLI，GUI 需单独授权。 |

## 3. 总控共识

多部门共识：

- 不建议继续把真实 Codex thread id 放在远端正式资产中。
- 建议用普通提交把正式 registry 改成公开别名。
- 建议新建本地私有 registry 保存真实 id 映射，并确保该路径被 `.gitignore` 忽略。
- 不建议默认执行 Git 历史重写、force push 或 tag 移动。
- 若仓库确认公开、外部协作者范围较大，或 thread id 被证明可以直接访问/控制会话，再升级到安全专项处理。
- 后续行动记忆、交接包、registry、baseline、release summary 中应避免写入真实 thread id，改用部门名、别名、交接包路径和 result 路径。

## 4. 推荐处理路径

第一步，低破坏前向修复：

1. 修改 `Department_Thread_Registry.md`，把真实 thread id 替换为稳定别名。
2. 新增本地私有 registry，例如 `AgentVault/00_System/Private/Department_Thread_Registry.private.md`。
3. 更新 `.gitignore`，确保私有 registry 不会被提交。
4. 更新仓库策略或 registry 说明：真实 thread id 属于内部调度元数据，默认不外发。
5. 更新 `$obsidian-memory` 草稿或模板：写入前检查内部调度元数据。

第二步，是否需要远端历史处理：

- 默认不做。
- 只有在用户确认高敏风险或公开暴露风险后，才设计单独的历史重写方案。

## 5. 需要用户确认

需要用户确认以下方向之一：

- `方案 A`: 接受低破坏前向修复：普通提交脱敏 + 本地私有 registry。
- `方案 B`: 先做 GitHub 仓库可见性只读检查，再决定是否脱敏。
- `方案 C`: 进入高风险历史处理评估，可能涉及历史重写、force push 或远端缓存处理。

总控办公室建议选择 `方案 A`，同时保留后续只读检查仓库可见性的选项。

## 6. 本轮未执行事项

- 未修改 registry。
- 未修改 `.gitignore`。
- 未创建私有 registry。
- 未改远端历史。
- 未 force push。
- 未移动 tag。
- 未提交、不 push。
- 未启动 GUI 自动化。
