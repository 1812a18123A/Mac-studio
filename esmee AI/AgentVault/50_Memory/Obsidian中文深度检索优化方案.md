---
type: memory_retrieval_optimization_plan
status: proposed
owner_department: 记忆部
date: 2026-06-17
current_mode: 巽-坤-兑
chinese_title: Obsidian 中文深度检索优化方案
中文标题: Obsidian 中文深度检索优化方案
summary_zh: 基于 Obsidian 原生 Properties、Tags、Aliases、Internal links 和三部门建议，提出中文索引层、中文属性层、中文标签层和渐进补齐路线。
中文摘要: 基于 Obsidian 原生 Properties、Tags、Aliases、Internal links 和三部门建议，提出中文索引层、中文属性层、中文标签层和渐进补齐路线。
aliases:
  - Obsidian中文检索优化
  - 记忆库中文深度检索
  - 中文资料库优化方案
search_keywords:
  - Obsidian
  - 中文检索
  - 中文索引
  - 属性
  - 标签
  - 别名
  - 行动记忆
  - 记忆库
检索元素:
  - Obsidian
  - 中文检索
  - 中文索引
  - 属性
  - 标签
  - 别名
  - 行动记忆
  - 记忆库
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_23-02_记忆部_obsidian-chinese-deep-retrieval-research.md
related_results:
  - AgentVault/50_Memory/Department_Handoffs/obsidian-chinese-deep-retrieval-research_memory_result.md
  - AgentVault/50_Memory/Department_Handoffs/obsidian-chinese-deep-retrieval-research_skillopt_result.md
  - AgentVault/50_Memory/Department_Handoffs/obsidian-chinese-deep-retrieval-research_engineering_result.md
official_references:
  - https://obsidian.md/help/properties
  - https://obsidian.md/help/tags
  - https://obsidian.md/help/links
---

# Obsidian 中文深度检索优化方案

## 1. 当前判断

本库目前有两层中文检索能力：

- 新版 writer 已能为新行动记忆写入中文标题、中文摘要、目录中文路径、文件时间中文、状态中文、风险中文和检索元素。
- 记忆库已有中文优先检索规范。

但历史资料尚未形成完整的中文索引层，当前约 174 个 Markdown 文件、记忆区约 149 个 Markdown 文件；大部分历史文件仍主要依赖英文路径、英文 task id 或正文自然语言检索。

## 2. Obsidian 原生能力

可优先使用 Obsidian 原生能力，不依赖复杂插件：

- Properties：用于结构化字段。Obsidian 官方说明 Properties 可以存储文本、链接、日期、复选框、数字等结构化数据，并支持用属性搜索语法配合其他搜索条件。
- Tags：用于稳定分类。官方说明 tags 是帮助快速查找笔记的关键词，也支持 nested tags。
- Aliases：用于中文别名。官方链接说明 aliases 适合为同一笔记设置不同叫法，便于输入别名找到同一文件。
- Internal links：用于索引页链接原文件，保留反向链接和原路径稳定性。

## 3. 推荐总体结构

采用四层结构：

```text
稳定路径层
中文属性层
中文标签层
中文索引层
```

### 3.1 稳定路径层

保留现有路径：

```text
AgentVault/50_Memory/Action_Logs/YYYY-MM-DD/...
```

不批量改名、不批量迁移。

通过 `目录中文路径` 解释目录含义，例如：

```text
记忆库 / 行动日志 / 2026年06月17日
```

### 3.2 中文属性层

新文件标准字段：

```yaml
中文标题:
中文摘要:
目录中文路径:
文件时间中文:
年份中文:
月份中文:
日期中文:
时段中文:
部门:
状态中文:
风险中文:
任务类型中文:
检索元素:
aliases:
tags:
```

### 3.3 中文标签层

建议标签少而稳定：

```text
#类型/行动记忆
#类型/部门交接
#类型/复审结果
#部门/记忆部
#部门/工程部
#部门/安全部
#部门/技能优化部
#部门/GUI自动化部
#状态/已完成
#状态/等待确认
#风险/低
#风险/中
#风险/高
#主题/Obsidian
#主题/中文检索
```

注意：标签不要包含空格；复杂描述放入 `检索元素` 或正文。

### 3.4 中文索引层

建议新增：

- `AgentVault/中文总索引.md`
- `AgentVault/50_Memory/记忆库索引.md`
- `AgentVault/50_Memory/Action_Logs/YYYY-MM-DD/今日行动索引.md`
- `AgentVault/50_Memory/Department_Handoffs/部门交接索引.md`
- `AgentVault/60_Skills/技能库索引.md`
- `AgentVault/30_GUI_Automation/GUI自动化索引.md`

索引页只放：

- 中文标题。
- 一句话摘要。
- 路径链接。
- 部门。
- 状态。
- 风险。
- 关键词。
- 下一步。

不复制全文。

## 4. Writer 下一步优化

建议最小增强，不做大系统：

1. 增加 `tags` 参数，由 writer 自动生成少量稳定中文标签。
2. 增加 `task_type_zh` 参数，例如行动记忆、交接包、复审结果、计划、研究。
3. 增加 `related_keywords_zh` 参数，补同义词和用户可能搜索的口语词。
4. 新增只读审计脚本：报告缺中文标题、缺中文摘要、缺检索元素、缺状态中文的文件。
5. 新增索引生成脚本：先只生成索引页，不自动改历史文件。

## 5. 历史资料补齐路线

### 阶段 1：索引不改文

- 新建中文总索引和记忆库索引。
- 索引页链接历史文件。
- 不改历史文件正文。

### 阶段 2：高频文件补字段

只补最近和高频文件：

- 最新 20 条行动记忆。
- 当前项目主文档。
- 常用规范。
- 部门交接汇总。

### 阶段 3：审计脚本 report-only

输出缺失清单，不自动修复：

- 缺中文标题。
- 缺中文摘要。
- 缺目录中文路径。
- 缺文件时间中文。
- 缺检索元素。
- 缺 tags。

### 阶段 4：按任务触达补齐

以后每次触达旧文件时，只补该文件的中文检索字段。

## 6. 不做事项

- 不批量重命名历史文件。
- 不批量移动目录。
- 不修改 `.obsidian` 设置。
- 不依赖复杂插件作为第一阶段。
- 不把真实内部 thread id、token、私密路径、配置值写进索引。
- 不把索引页做成正文副本。
- 不让标签无限发散。

## 7. 推荐下一步

下一小步建议：

```text
创建中文总索引和记忆库索引的第一版，只链接现有重要文件，不修改历史文件。
```

之后再做：

```text
实现只读中文检索审计脚本。
```
