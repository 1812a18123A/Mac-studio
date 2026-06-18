---
type: department_research_result
task_id: obsidian-chinese-deep-retrieval-research
department: 技能优化部
date: 2026-06-17
status: completed
current_mode: 坤-兑
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_23-02_记忆部_obsidian-chinese-deep-retrieval-research.md
---

# 技能优化部研究结果：Obsidian 中文深度检索优化

## 结论

推荐把中文检索规则固化为三层：

1. 路径/文件名层：保留稳定路径，但用中文部门名和中文任务短名辅助。
2. 属性层：使用 Obsidian properties 放少量稳定中文字段。
3. 正文层：保留 `## 中文检索入口` 或 `## 中文检索索引`。

## Writer 下一步建议

- 支持 `aliases`。
- 支持 `summary_zh`。
- 支持 `search_terms_zh` 或 `检索元素`。
- 支持 `task_type_zh`。
- 支持 `time_zh`。
- 支持 `related_keywords_zh`。

## 降低复杂度

- 必填控制在中文标题、中文摘要、中文检索词。
- 检索词建议 5 到 8 个。
- 不要求所有字段中英双写。
- 新规则先用于新文件，不迁移旧文件。

## 验收标准

- 能用中文部门搜到。
- 能用中文任务对象搜到。
- 能用中文风险/状态搜到。
- 能用中文时间或日期搜到。
- 能通过中文别名找到英文 task id 文件。

## 禁止事项

- 不把中文检索做成复杂插件。
- 不无限扩展同义词。
- 不为了检索牺牲行动记忆可读性。
