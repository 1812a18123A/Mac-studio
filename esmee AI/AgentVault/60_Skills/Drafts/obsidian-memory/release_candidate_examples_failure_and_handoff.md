---
type: skill_release_candidate
skill: obsidian-memory
candidate: examples_failure_and_handoff
status: ready_for_user_confirmation
date: 2026-06-17
owner_department: 技能优化部
not_active_rule: true
requires_user_confirmation: true
---

# obsidian-memory 示例草稿发布候选包

## 候选内容

候选文件：
- `AgentVault/60_Skills/Drafts/obsidian-memory/examples_failure_and_handoff.md`

候选范围：
- 失败时追加行动日志。
- 失败时设置 `status` 和 `current_mode`。
- 需要用户确认时记录待确认事项。
- 跨部门交接包最小模板。
- 接收部门完成后的结果回写样例。
- 不确定或高风险时引用安全边界文档。

## 当前结论

状态：可进入用户确认，不自动发布。

理由：
- 记忆部审核完成，结论为需小修，小修已完成。
- 安全部审核完成，结论为需小修，小修已完成。
- 工程部校验完成，writer 命令接口与真实工具一致。
- 最新补充已明确 `append-log` 应用于已经创建好的行动记忆。

## 已完成审核

记忆部：
- 行动记忆：`AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-17_记忆部_review-obsidian-memory-examples.md`
- 原结论：需小修。
- 修复状态：已应用。

安全部：
- 行动记忆：`AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-17_安全部_review-obsidian-memory-examples.md`
- 原结论：需小修。
- 修复状态：已应用。

工程部：
- 行动记忆：`AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-36_工程部_verify-obsidian-memory-example-commands.md`
- 结论：命令接口层面通过。
- 修复状态：已补充 `append-log` 使用边界。

## 已完成修正

- 增加原始错误、原始命令、日志路径字段。
- 补充 `failed` 与 `blocked` 选择标准。
- 高风险待确认状态使用 `坎-艮-兑`。
- 交接包模板增加 `current_state`、`completed_work`、`related_skills`、`related_plugins`。
- 结果回写样例增加 `related_action_memory`。
- 补充 `append-log` 应用于已存在行动记忆；本轮没有行动记忆时先使用 `create`。

## 验证记录

- `python3 -m unittest discover -s '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools' -p 'test_*.py'`
  - 结果：4 项通过。
- `python3 '/Users/peipei/.codex/skills/.system/skill-creator/scripts/quick_validate.py' '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/60_Skills/Drafts/obsidian-memory'`
  - 结果：`Skill is valid!`

## 禁止事项

发布前仍禁止：
- 不修改 `/Users/peipei/.codex/skills/obsidian-memory/SKILL.md`。
- 不修改 `AgentVault/60_Skills/Published/obsidian-memory/best_skill.md`。
- 不修改现有 draft `SKILL.md`。
- 不修改 `.obsidian`。
- 不安装依赖。
- 不把本候选文件当成已生效规则。

## 用户确认选项

下一步需要用户明确确认其一：

1. 只保留为 draft 参考，不合并。
2. 合并进 vault 内 draft `SKILL.md`，仍不影响全局 skill。
3. 合并进 published `best_skill.md`，作为 vault 内发布版本。
4. 安装/同步到全局 `$obsidian-memory`，这会写入 `/Users/peipei/.codex/skills/obsidian-memory/SKILL.md`，需要单独确认。

## 建议

建议下一步先选择选项 2：合并进 vault 内 draft `SKILL.md`。这样可以继续验证结构，不直接影响全局运行时。
