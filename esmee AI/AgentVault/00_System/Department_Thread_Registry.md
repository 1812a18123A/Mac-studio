---
type: department_thread_registry
registry_id: department-thread-registry-v0.3-draft
date: 2026-06-17
owner_department: 总控办公室
status: active
risk_level: medium
current_mode: 坤-兑
related_baseline:
  - AgentVault/00_System/Baselines/2026-06-17_Agent_OS_v0.2_Release_Summary.md
related_workflow:
  - AgentVault/00_System/Department_Workflow_v0.2.md
related_policy:
  - AgentVault/00_System/Repository_Policy.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-13_总控办公室_create-department-thread-registry.md
---

# Department Thread Registry v0.3 Draft

本文件登记真实 Codex 部门会话，用于 v0.3 的最小多部门调度。它只记录调度入口和写回规则，不代表自动派发任务，也不要求每个小任务都启动多部门协作。

## 1. 使用原则

- 总控办公室先判断主责部门、风险等级和是否需要协作窗口。
- 低风险单文件文档或行动记忆任务，可以由总控直接完成。
- 涉及代码、测试、仓库结构、提交或 push 时，优先通知工程部。
- 涉及隐私、账号、token、外发、删除、GUI 自动化或权限时，必须通知安全部。
- 涉及行动记忆结构、部门交接、结果归档或未收口审计时，通知记忆部。
- 涉及重复流程、skill 草案、模板优化或失败复盘时，通知技能优化部。
- 涉及 Obsidian、浏览器、鼠标键盘、截图或桌面 App 操作时，通知 GUI 自动化部。

## 2. 部门线程登记

| 部门 | Codex thread id | 当前状态 | 负责范围 | 最近确认任务 | 结果写回约定 |
| --- | --- | --- | --- | --- | --- |
| 总控办公室 | `019ed788-3cd8-7b13-b705-51c89a33dea7` | idle | 任务判断、范围控制、跨部门派发、结果汇总、用户简报 | `real-v0-2-e2e` | 汇总写入 `AgentVault/50_Memory/Action_Logs/YYYY-MM-DD/` 或 `AgentVault/00_System/Baselines/` |
| 工程部 | `019ed788-4a85-7652-b143-b73791c170e7` | idle | 代码、工具、测试、Git、仓库结构、本地脚本 | `real-v0-2-e2e` | `AgentVault/50_Memory/Department_Handoffs/[task-id]_engineering_result.md` |
| 记忆部 | `019ed788-5664-7853-8a8b-63cfc6dc7837` | idle | 行动记忆、交接包、归档结构、未收口审计 | `real-v0-2-e2e` | `AgentVault/50_Memory/Department_Handoffs/[task-id]_memory_result.md` |
| 安全部 | `019ed793-7e74-7b72-8b13-7969d6c8b180` | idle | 权限、隐私、外发、删除、GUI 自动化、账号和密钥风险 | `real-v0-2-e2e` | `AgentVault/50_Memory/Department_Handoffs/[task-id]_safety_result.md` |
| 技能优化部 | `019ed793-7fb9-7ce2-b363-2c3371a2f017` | idle | skill、模板、复用流程、失败模式沉淀 | `real-v0-2-e2e` | `AgentVault/50_Memory/Department_Handoffs/[task-id]_skillopt_result.md` |
| GUI 自动化部 | `019ed793-810d-78c3-a68d-35e0fd60f24d` | idle | 桌面 UI、Obsidian/浏览器/本机 App 操作、截图和交互验证 | `real-v0-2-e2e` | `AgentVault/50_Memory/Department_Handoffs/[task-id]_gui_result.md` |

## 3. 任务状态定义

- `idle`: 当前没有已派发且未回收的任务。
- `active`: 已派发任务，等待部门执行或结果写回。
- `blocked`: 部门已报告阻断，需要用户确认、权限变更或上游资料。
- `archived`: 线程不再作为默认调度入口。

总控办公室更新状态时，应在本文件和当前行动记忆中同时记录原因。

## 4. 派发规则

每次真实多部门派发必须有唯一 `task_id`，建议格式：

```text
real-v0-3-[short-task-name]
```

派发前总控办公室必须创建或更新行动记忆，并列出：

- 主责部门。
- 协作部门。
- 交接包路径。
- 结果写回路径。
- 禁止事项。
- 成功标准。
- 是否需要用户确认。

## 5. 结果回收规则

每个部门完成后，必须写回一个 result 文件。result 文件至少包含：

- `task_id`
- `department`
- `status`: `passed` / `passed_with_notes` / `blocked` / `failed`
- 已读取资料
- 实际执行内容
- 风险或阻断
- 下一步建议

总控办公室只有在所有必需部门返回 result 后，才可以写最终汇总结论。若某部门 `blocked` 或 `failed`，总控不得把该任务标记为完成，除非用户明确接受降级范围。

## 6. 禁止事项

未经用户明确确认，不得：

- 删除、覆盖、批量移动或批量重命名文件。
- 修改 `.obsidian/`、Obsidian 插件、全局 skill 或系统配置。
- 操作 token、SSH 私钥、账号、付款、表单或隐私资料。
- 外发、上传、发送邮件、发送消息或提交表单。
- 使用 GUI 自动化控制鼠标、键盘、截图或桌面 App。
- 移动 `agent-os-v0.1` 或 `agent-os-v0.2` tag。
- 使用 `git add .` 暂存不确定文件。

## 7. v0.3 第一阶段成功标准

- 总控办公室可以从本文件找到所有部门会话入口。
- 每个部门都有明确职责和 result 写回路径。
- 每次派发都有唯一 task id。
- 部门状态可被更新为 `idle`、`active`、`blocked` 或 `archived`。
- 所有多部门结果都能回写到 Obsidian。
- Git 提交仍遵守 `Repository_Policy.md`。

## 8. 下一步建议

下一小步建议创建 `real-v0-3-dispatch-protocol` 交接包，让安全部、记忆部和工程部真实审查本注册表是否足够支撑 v0.3 调度。
