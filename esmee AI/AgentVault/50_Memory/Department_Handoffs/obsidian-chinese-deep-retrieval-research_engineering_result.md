---
type: department_research_result
task_id: obsidian-chinese-deep-retrieval-research
department: 工程部
date: 2026-06-17
status: completed
current_mode: 坤-兑
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_23-02_记忆部_obsidian-chinese-deep-retrieval-research.md
---

# 工程部研究结果：Obsidian 中文深度检索优化

## 结论

推荐使用 Markdown、frontmatter 和索引页，不引入复杂 Obsidian 插件作为第一阶段依赖。

## 最小实现

- 保持原路径和文件名稳定。
- 每个新记忆写入中文 frontmatter 字段。
- 每个新记忆正文开头写固定中文检索入口。
- 新增中文索引页，链接到原文件。

## 脚本建议

- 新增中文索引生成脚本：只读扫描 Markdown，生成索引页。
- 新增中文检索审计脚本：检查必需中文字段是否缺失。
- 初期脚本只做 report-only 或只写索引页，不自动改历史文件。

## 测试建议

- 测试 frontmatter 中文字段。
- 测试正文中文检索入口。
- 测试 `set-status` 是否同步中文状态。
- 测试不改变历史链接。
- 用 fixture 或临时 vault 测试脚本，不直接写全库。

## Obsidian 原生能力

- Properties：承载中文结构化字段。
- Tags：承载稳定分类，如部门、状态、类型、风险。
- Aliases：承载中文别名和口语说法。
- Internal links：索引页链接原文件，保持反向链接可靠。

## 禁止事项

- 不批量迁移或重命名目录。
- 不把索引生成和 writer 强耦合成一个大系统。
- 不自动改历史正文。
- 不把私密路径、token、thread id、配置值写入索引。
