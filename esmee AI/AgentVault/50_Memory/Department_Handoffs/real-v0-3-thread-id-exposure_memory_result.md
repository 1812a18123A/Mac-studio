---
type: department_handoff_result
date: 2026-06-17
department: 记忆部
task_id: real-v0-3-thread-id-exposure
status: recommend_private_registry
related_handoff: AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_memory.md
related_action_memory: AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-34_记忆部_real-v0-3-thread-id-exposure.md
---

# 交接结果：real-v0-3-thread-id-exposure - 记忆部

## status

recommend_private_registry

## 已读取资料

- `AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_memory.md`
- `AgentVault/00_System/Department_Thread_Registry.md`
- `AgentVault/00_System/Department_Workflow_v0.2.md`
- `AgentVault/70_Safety/Permission_Boundaries.md`
- `/Users/peipei/.codex/skills/obsidian-memory/SKILL.md`

## 记忆结构建议

建议采用双轨结构：

- 正式 registry：保留在 `AgentVault/00_System/Department_Thread_Registry.md`，只记录部门名、职责、状态、最近任务、result 写回约定、内部别名，不记录真实 Codex thread id。
- 本地私有 registry：新建一个不提交、不 push 的本地文件，用于保存真实 thread id 到部门别名的映射。
- 正式行动记忆和交接包：记录“发给哪个部门”和“关联交接包/result 路径”，不记录真实 thread id。

建议本地私有 registry 的位置由工程部/安全部共同确认，候选为：

- `AgentVault/00_System/Private/Department_Thread_Registry.local.md`
- 或 vault 外部的本机私有路径。

如果放在 vault 内，必须加入忽略规则并明确不得进入远端。

## 对当前 registry 的建议

建议脱敏当前 `Department_Thread_Registry.md`：

- 将 `Codex thread id` 列替换为 `thread_alias` 或 `dispatch_alias`。
- 例：`dept-control`、`dept-engineering`、`dept-memory`、`dept-safety`、`dept-skillopt`、`dept-gui`。
- 正式 registry 中保留 result 写回路径和部门职责，因为这些是审计链路需要的公开结构信息。
- 不建议本轮改远端历史；既然已经推送，应通过后续正常提交进行前向修正，并在行动记忆中记录“已脱敏”和“真实 id 迁入私有 registry”。

## 是否需要脱敏

需要。

理由：

- 真实 Codex thread id 是内部调度入口元数据，不是业务审计事实。
- 远端正式资产应保留可审计结构，而不是暴露运行时会话入口。
- 审计链路需要知道“哪个部门处理了什么、写回了哪里”，不需要知道真实 thread id。

## 是否清理历史行动记忆或 result

不建议批量清理历史行动记忆或 result。

理由：

- 批量迁移/重命名/改写记忆会破坏审计连续性，也超出本轮权限。
- 已存在记录可保留为历史事实，但后续索引或新 registry 应使用脱敏别名。
- 若安全部判定 thread id 具备实际访问风险，再由总控办公室发起单独确认流程，决定是否做最小范围前向修正或历史处理。

## 是否需要更新 `$obsidian-memory`

建议更新，但不是本轮直接修改全局 skill。

建议后续由技能优化部提出最小规则：

- 内部调度元数据不得写入将被提交或推送的正式行动记忆、交接包、registry 或发布版 skill。
- 若必须引用部门会话，使用部门名、别名、交接包路径和 result 路径。
- 真实 thread id、窗口 id、会话 id、设备路径、账号标识等运行时入口信息，应写入本地私有 registry 或待确认记录。
- result 文件应通过 `related_handoff` 和 `related_action_memory` 保持审计链路，而不是通过 thread id 追踪。

## 如何保持审计链路

- 正式 registry 保留部门别名、职责、状态和 result 写回约定。
- 每次派发仍创建交接包，记录 `task_id`、发起部门、接收部门、禁止事项、成功标准和 result 路径。
- 每个部门仍创建自己的行动记忆，并在 result 中写 `related_handoff` 和 `related_action_memory`。
- 总控办公室通过 task id、部门名、交接包路径、result 路径汇总，而不是通过真实 thread id 汇总。
- 私有 registry 只负责“把部门别名映射到当前真实 Codex thread id”，不参与远端审计。

## 是否阻断

不建议继续把真实 thread id 作为正式资产推进。

v0.3 调度协议本身不必阻断，但进入下一步前应先完成前向脱敏方案：公开 registry 使用别名，本地私有 registry 保存真实 id。

## 禁止事项遵守

- 未删除文件。
- 未批量迁移或重命名行动记忆。
- 未修改全局 skill。
- 未修改远端历史。
- 未提交、未 push。
