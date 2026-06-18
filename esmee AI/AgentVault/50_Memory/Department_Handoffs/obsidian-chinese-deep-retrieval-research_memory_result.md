---
type: department_research_result
task_id: obsidian-chinese-deep-retrieval-research
department: 记忆部
date: 2026-06-17
status: completed
current_mode: 坤-兑
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_23-02_记忆部_obsidian-chinese-deep-retrieval-research.md
---

# 记忆部研究结果：Obsidian 中文深度检索优化

## 结论

推荐采用：

```text
稳定英文路径 + 中文索引层 + 中文 frontmatter + 渐进补齐
```

## 建议结构

- 总索引：`AgentVault/中文总索引.md`
- 记忆库索引：`AgentVault/50_Memory/记忆库索引.md`
- 日期索引：`AgentVault/50_Memory/Action_Logs/YYYY-MM-DD/今日行动索引.md`
- 部门索引：按部门汇总行动记忆、交接包、决策、禁区、失败复盘和待确认事项。

## 标准字段建议

- `中文标题`
- `中文摘要`
- `检索元素`
- `目录中文路径`
- `文件时间中文`
- `部门`
- `状态`
- `风险`
- `相关行动记忆`
- `相关交接包`
- `结果路径`

## 历史文件策略

- 不批量重命名历史文件。
- 不移动历史目录。
- 只在再次触达时追加中文摘要、中文关键词和中文索引链接。
- 高频文件优先补齐。

## 禁止事项

- 不把真实内部调度元数据写入公开索引。
- 不把完整命令输出、私密路径、token、配置值放进检索字段。
- 不让索引页复制正文全文；索引只保留摘要、路径和检索入口。
