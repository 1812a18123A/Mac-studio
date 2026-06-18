---
type: department_handoff_result
task_id: real-v0-3-thread-id-exposure
department: 技能优化部
status: recommend_update_skill
created_at: 2026-06-17
risk_level: medium
current_mode: 坤-坎-兑
related_handoff: AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_skillopt.md
related_action_memory: AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-34_技能优化部_real-v0-3-thread-id-exposure-skillopt-discussion.md
related_registry: AgentVault/00_System/Department_Thread_Registry.md
---

# 技能优化部结果：real-v0-3-thread-id-exposure

## 1. 讨论结论

建议更新 `$obsidian-memory`，并同步新增 registry 模板与交接包脱敏检查。

本次问题的核心不是单个 Markdown 字段写错，而是“内部调度元数据”和“可公开协作资产”没有分层。真实 Codex thread id 可以用于本地调度，但不应进入会被提交、push、发布或共享的正式资产。

建议总状态：

- `status`: `recommend_update_skill`
- 同时建议：`recommend_template_change`
- 不建议：仅靠人工记忆避免复发。

## 2. 是否更新 `$obsidian-memory`

建议更新，但先只改草稿或 examples，不直接改全局 skill。

建议新增一条规则：

> 行动记忆、交接包、registry、baseline、release summary、README 等可能提交或共享的文件，在写入前必须检查是否包含内部调度元数据。真实 Codex thread id、pending worktree id、connector 会话 id、审批会话 id、临时 UI/session 标识应默认视为内部元数据；除非用户明确要求并确认保留，否则公开资产只写部门名、职责、别名、结果路径和本地私有 registry 引用。

建议放入 `$obsidian-memory` 的位置：

- `Safety Boundaries`：加入“内部调度元数据外发前确认”。
- `Department Handoff`：加入“不得在可公开交接包中粘贴真实 thread id”。
- `Required Content`：加入“内部元数据检查结果”。
- `Failure And Handoff Examples`：追加一个“公开/私有 registry 分层示例”。

## 3. 是否新增公开 / 私有 registry 模板

建议新增两个模板，而不是继续维护一个混合 registry。

### 3.1 公开版 registry

建议路径：

`AgentVault/00_System/Templates/Department_Registry_Public_Template.md`

公开版只包含：

- 部门名称。
- 部门别名，例如 `ceo-window`、`engineering-window`。
- 职责范围。
- 状态：`idle` / `active` / `blocked` / `archived`。
- 结果写回路径模板。
- 相关行动记忆路径。
- 私有 registry 的本地引用说明，但不写真实 id。

公开版禁止包含：

- 真实 Codex thread id。
- pending worktree id。
- session id、connector id、审批 id。
- 任何可直接定位内部会话入口的标识。

### 3.2 本地私有 registry

建议路径：

`AgentVault/00_System/Private/Department_Thread_Registry.private.md`

私有版可包含真实调度入口，但应默认不提交。若仓库需要长期维护，应由工程部检查 `.gitignore` 或仓库策略是否覆盖 `AgentVault/00_System/Private/`。

私有版字段建议：

- 部门名称。
- 本地别名。
- 真实 Codex thread id。
- 当前状态。
- 最近确认任务。
- 结果写回路径。
- 最后校验时间。
- 维护人或主责部门。

## 4. 交接包模板是否加入内部元数据脱敏检查

建议加入，而且应作为交接包模板的必填检查项。

建议在交接包模板新增：

```markdown
## 内部元数据脱敏检查

- [ ] 是否包含真实 Codex thread id？
- [ ] 是否包含 pending worktree id、session id、connector id 或审批 id？
- [ ] 是否包含 token、密钥、账号、隐私资料或本地敏感路径？
- [ ] 是否会被提交、push、分享或发布？
- [ ] 如需保留内部调度入口，是否改写到本地私有 registry？

结论：
- public_safe: true | false
- private_registry_required: true | false
- requires_user_confirmation: true | false
```

建议规则：

- 发给部门窗口的临时 prompt 可以使用真实 thread id，因为它属于当前 Codex 调度上下文。
- 写入正式 Obsidian 资产时，应优先写部门别名和结果路径。
- 如果必须保留真实 id，只能写入私有 registry，并明确标记“不提交/不外发”。

## 5. 流程防复发建议

建议采用“三层闸门”：

1. 写入前：总控办公室判断文件是否可能被提交或共享。
2. 写入中：模板强制填写“内部元数据脱敏检查”。
3. 提交前：工程部或安全部执行一次检索审查。

建议检索模式：

```text
Codex thread id
thread id
pendingWorktreeId
source_thread_id
019e
```

注意：`019e` 这类前缀只能作为粗筛，不能作为唯一判断依据。最终应由人工确认上下文。

## 6. 如何保持可审计但不泄露 thread id

建议以“稳定别名 + 行动记忆 + 结果路径”替代真实 id：

- `总控办公室` -> `ceo-window`
- `工程部` -> `engineering-window`
- `记忆部` -> `memory-window`
- `安全部` -> `safety-window`
- `技能优化部` -> `skillopt-window`
- `GUI 自动化部` -> `gui-window`

可审计链路应依靠：

- `task_id`
- 交接包路径
- result 文件路径
- 行动记忆路径
- 部门别名
- 本地私有 registry 引用

不依靠：

- 真实 Codex thread id。
- 临时会话 id。
- 远端不可复现的内部调度标识。

## 7. 需要总控或用户确认的事项

需要总控办公室决定：

- 是否把当前正式资产中的真实 thread id 改为公开版 registry。
- 是否创建本地私有 registry 路径。
- 是否要求工程部补 `.gitignore` 或仓库策略。
- 是否创建一次“已推送资产脱敏修复”任务。

需要用户确认：

- 若要重写 git 历史、撤回远端提交、删除远端敏感记录，属于高风险操作，必须单独确认。
- 若只新增公开模板、私有模板草稿、或后续普通提交修复当前文件，通常可按低到中风险处理，但仍应由总控明确任务边界。

## 8. 本次未执行事项

- 未修改全局 `$obsidian-memory`。
- 未发布 skill。
- 未删除任何文件。
- 未提交、不 push。
- 未修改当前 registry。
- 未创建公开/私有 registry 模板。

## 9. 下一步建议

建议总控办公室派发三个小任务：

1. 安全部：判断当前已推送 thread id 的风险等级，以及是否需要远端历史处理。
2. 记忆部：起草公开/私有 registry 模板和交接包脱敏检查模板。
3. 工程部：检查仓库策略或 `.gitignore` 是否能保护私有 registry。

技能优化部后续可接收任务：把本次规则沉淀进 `$obsidian-memory` draft 和 examples，但需在总控确认后执行。
