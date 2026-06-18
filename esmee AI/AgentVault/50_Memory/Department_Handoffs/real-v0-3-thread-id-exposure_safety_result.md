---
type: department_handoff_result
task_id: real-v0-3-thread-id-exposure
department: 安全部
status: recommend_redact
created_at: 2026-06-17
related_handoff: AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_safety.md
related_action_memory: AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-34_安全部_real-v0-3-thread-id-exposure.md
current_mode: 坤-兑
---

# 交接结果：真实 Codex thread id 外发风险讨论

## status

`recommend_redact`

## 风险等级

`medium`

真实 Codex thread id 不等同于密码、token、SSH 私钥或账号凭据。仅凭 thread id 通常不应直接获得会话访问权，但它属于内部调度元数据，会暴露部门会话结构、协作入口命名、任务组织方式和部分运行节奏。若远端仓库是公开仓库，风险更高；若远端仓库是私有仓库且协作者可信，风险为中低。

## 已读取资料

- `AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_safety.md`
- `AgentVault/00_System/Department_Thread_Registry.md`
- `AgentVault/00_System/Repository_Policy.md`
- `AgentVault/70_Safety/Permission_Boundaries.md`
- `git status --short --branch`

## 是否建议保留 / 脱敏 / 移出远端

建议：脱敏后保留调度协议。

- 不建议继续在正式远端资产中保存真实 thread id。
- 建议把远端版 `Department_Thread_Registry.md` 中的真实 id 替换为稳定别名，例如 `ceo-window`、`engineering-window`、`memory-window`、`safety-window`。
- 真实 thread id 建议迁移到本地私有文件，例如 vault 顶层私有笔记、`.obsidian` 外的本地忽略文件，或一个被 `.gitignore` 明确忽略的 `AgentVault/00_System/Private/Department_Thread_IDs.local.md`。
- 若仍需在仓库中表达映射关系，可只保留“部门别名、职责、结果写回路径、状态”，不保留真实 id。

## 是否需要历史重写

默认不建议历史重写。

理由：

- thread id 不是密钥，不需要像泄露 token/私钥一样立即撤销或重写历史。
- 历史重写、force push、tag 移动都会带来协作和审计风险，且本任务明确禁止执行这些动作。
- 普通提交脱敏可以降低未来暴露面，同时保留可审计历史。

需要升级为“考虑历史重写”的条件：

- 用户确认远端仓库是公开仓库，并且不希望任何外部人看到真实 thread id。
- Codex thread id 被确认可被外部直接用于访问、恢复、控制或枚举会话。
- 远端仓库包含其它敏感资料，thread id 只是更大泄露的一部分。

若进入这些条件，历史重写、force push、tag 移动、远端设置变更都必须单独获得用户明确确认，并由总控办公室、工程部、安全部共同制定回滚方案。

## 需要用户确认的动作

- 是否允许工程部用普通提交把 `Department_Thread_Registry.md` 中真实 thread id 替换为别名。
- 是否允许新增一个本地私有、不入库的 thread id 映射文件。
- 是否确认远端仓库的可见性：public / private / 内部协作者范围。
- 是否允许将真实 thread id 从后续行动记忆、交接包或结果文件中同步脱敏。
- 是否需要进一步评估历史重写；默认不建议，除非用户明确确认高敏风险。

## 推荐处理方案

1. 先停止继续把真实 thread id 写入新的远端资产。
2. 由总控办公室确认脱敏策略：稳定别名优先。
3. 由工程部在普通提交中修改 `Department_Thread_Registry.md`，移除真实 id。
4. 由记忆部维护一个本地私有映射，确保调度仍可用。
5. 由安全部更新权限边界或仓库策略：真实 thread id 归类为“内部调度元数据”，默认不外发。

## 本次未执行事项

- 未删除文件。
- 未改远端历史。
- 未 force push。
- 未移动 tag。
- 未操作 token、SSH 私钥或 GitHub 设置。
- 未提交。
- 未 push。

## 下一步建议

总控办公室可以把本议题派给工程部和记忆部：工程部负责普通提交脱敏方案，记忆部负责本地私有映射方案。安全部建议在用户确认前不要继续向远端写入真实 thread id。
