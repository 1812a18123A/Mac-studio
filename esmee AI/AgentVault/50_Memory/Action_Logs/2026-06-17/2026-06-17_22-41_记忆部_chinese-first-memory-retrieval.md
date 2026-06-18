---
type: action_memory
date: 2026-06-17
time: "22:41"
department: 记忆部
task_id: chinese-first-memory-retrieval
chinese_title: 记忆库中文优先检索规则
aliases:
  - 中文优先记忆检索
  - 记忆库中文索引
  - 行动记忆中文关键词
search_keywords:
  - 中文检索
  - 中文优先
  - 记忆库
  - 行动记忆
  - Obsidian
  - 检索规范
summary_zh: 建立记忆库中文优先检索规范，后续记忆默认补中文标题、摘要、别名和关键词。
status: completed
risk_level: low
current_mode: 坤-兑
related_skills:
  - obsidian-memory
related_plugins:
  - none
related_files:
  - AgentVault/50_Memory/中文优先检索规范.md
  - AgentVault/60_Skills/Drafts/obsidian-memory/SKILL.md
  - AgentVault/60_Skills/Published/obsidian-memory/best_skill.md
notify_departments:
  - 记忆部
  - 技能优化部
requires_user_confirmation: false
---

# 行动记忆：记忆库中文优先检索规则

## 1. 用户目标

用户想要什么：
- 让 Obsidian 记忆库里的记忆以中文为主，方便中文检索。

## 2. 本次行动目标

这一次只做什么：
- 本次只建立中文优先检索规范，并同步到记忆技能说明；不批量改名历史文件。

## 3. 当前上下文

已知信息：
- 用户明确希望记忆库里的记忆以中文为主来检索。
- 当前行动记忆正文大多是中文，但文件名、task id、部分技能说明和部分复审结果仍偏英文。
- 批量改名历史文件会破坏链接和 Git 历史，不适合作为第一步。

未知信息：
- 后续是否要改造 writer，让它自动生成中文检索字段。
- 是否要分批给历史高频记忆补中文别名和关键词。

## 4. 涉及资料

需要读取或参考的资料：
  - AgentVault/60_Skills/Drafts/obsidian-memory/SKILL.md
  - AgentVault/60_Skills/Published/obsidian-memory/best_skill.md
  - AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py

禁止使用或不能外发的资料：
  - 本地隐私资料
  - 真实内部 thread id
  - token、SSH key、账号认证信息

## 5. 需要修改什么

计划修改的文件、配置、skill、插件、脚本：
  - 新增中文优先检索规范。
  - 更新库内 obsidian-memory 草稿技能说明。
  - 更新库内 obsidian-memory 发布版技能说明。
  - 更新本行动记忆。

## 6. 不能做什么

本次明确禁止：
- 不删除文件，除非用户明确确认
- 不发送邮件、消息、付款、提交表单，除非用户明确确认
- 不上传截图、音频、记忆文件到外部服务，除非用户明确确认
- 不覆盖已有 skill，除非先备份
- 不跳过 Obsidian 行动记录
- 不批量改名历史记忆文件。
- 不删除或移动既有记忆。
- 不改动 `.obsidian` 设置。
- 不修改 writer 程序逻辑，除非后续单独确认。

## 7. 需要调用的 skill

本次需要：
  - obsidian-memory：记录行动记忆，并同步记忆库检索规范。

## 8. 需要使用的 Codex App 插件功能

本次需要：
  - none

## 9. 行动步骤

- [x] Step 1: 记录行动记忆。
- [x] Step 2: 新增中文优先检索规范。
- [x] Step 3: 更新 obsidian-memory 草稿和发布版技能说明。
- [x] Step 4: 同步全局 obsidian-memory skill 并验证。
- [x] Step 5: 扫描并准备提交推送。

## 10. 风险检查

风险：
- 低。主要风险是批量改名破坏链接，或只写英文导致用户后续检索不到。

缓解措施：
- 本轮只新增规范和更新技能说明，不批量改名历史文件。
- 英文 task id 保留为稳定技术 ID，但要求附近补中文标题、摘要、别名和关键词。
- 后续触达历史文件时再逐步补中文检索字段。

## 11. 部门通知

需要通知哪个部门：
  - 记忆部
  - 技能优化部

通知原因：
- 记忆部负责记忆结构和检索体验。
- 技能优化部负责把规则同步到 obsidian-memory 技能说明。

## 12. 执行结果

实际做了什么：
- 已新增中文优先检索规范。
- 已更新 obsidian-memory 草稿和发布版技能说明，要求新记忆默认包含中文标题、中文摘要、中文别名、中文关键词和中文下一步。
- 已明确历史文件不批量改名，后续触达时逐步补中文检索字段。
- 已同步已安装的全局 obsidian-memory skill，使后续触发该 skill 时也会读取中文优先检索规则。
- 已运行 writer 单元测试、库内 skill 校验和全局 skill 校验，均通过。
- 已扫描内部 thread id、常见密钥格式和中文检索字段，未发现问题。

成功：
- 成功。中文优先检索规则已作为记忆库规范落地。

失败：
- 无。

## 13. 产生的新资料

新增文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_22-41_记忆部_chinese-first-memory-retrieval.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/中文优先检索规范.md

更新文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/60_Skills/Drafts/obsidian-memory/SKILL.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/60_Skills/Published/obsidian-memory/best_skill.md

截图/日志/轨迹：
- 无截图。未改名历史文件。
- 全局 skill 文件已同步，但它位于 Git 仓库外，不作为本仓库提交对象。

## 14. 下一步

下一步建议：
- 提交并推送库内中文优先检索规范；后续触达历史记忆时逐步补中文别名和关键词。

## 15. 给用户的简短汇报

用简短中文告诉用户：
- 已把“中文优先检索”固化为记忆库规则，后续记忆默认补中文标题、摘要、别名和关键词。

## Log 2026-06-17 22:44

- 已完成中文优先检索规则落地：新增规范、更新库内草稿/发布版 skill、同步全局 obsidian-memory skill，并通过验证。
