---
name: obsidian-memory
description: Create, update, and audit Obsidian action memory files for local Agent OS workflows. Use when a task requires department routing, pre-action or post-action checklists, structured Markdown action logs, Obsidian vault memory writes, department handoffs, or appending execution results with the local action-memory writer.
---

# Obsidian Memory

## Purpose

Use this skill to make every meaningful action auditable in the local Obsidian vault. Prefer the existing local writer adapter over hand-written files.

Operational metadata:
- Department: 记忆部 / 技能优化部
- Version: draft-0.1
- Risk level: low
- Related tool: `/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py`
- Related plugin: none

## Workflow

1. Determine the primary department and collaborators.
2. Decide whether the task needs a new action memory or an update to an existing one.
3. Write the action memory before making substantive changes.
4. Execute one small step.
5. Append the result, success/failure state, new files, and next step.
6. When the task is done, use `set-status` to update frontmatter fields such as `status` and `current_mode`.
7. If the task crosses departments, create a department handoff note.

## Chinese-first Retrieval

Memory records must be searchable primarily in Chinese.

For every new or substantially updated memory, include Chinese-first retrieval content near the top:
- Chinese title.
- Chinese summary.
- Chinese aliases.
- Chinese search keywords.
- Chinese directory path.
- Chinese file elements.
- Chinese time elements.
- Chinese next step.
- Chinese department names.

Recommended frontmatter fields:

```yaml
chinese_title:
中文标题:
aliases:
  - 中文别名
search_keywords:
  - 中文关键词
检索元素:
  - 中文关键词
summary_zh:
中文摘要:
directory_zh:
目录中文路径:
file_time_zh:
文件时间中文:
年份中文:
月份中文:
日期中文:
时段中文:
status_zh:
状态中文:
risk_level_zh:
风险中文:
```

Directory meanings, file elements, time elements, status, risk, departments, and next steps should be searchable in Chinese. English task ids, command names, repository names, API names, and original source text may remain in English, but add nearby Chinese explanation for search. Do not mass-rename historical files; when an old memory is touched again, add Chinese aliases, keywords, directory notes, time notes, or summary instead.

Use current-mode labels:
- `乾`: planning
- `坤`: memory/archive
- `巽`: background context gathering
- `坎`: risk/permissions
- `离`: visual inspection
- `艮`: waiting for confirmation
- `兑`: report/communication

## Standard Paths

Action memory:
`AgentVault/50_Memory/Action_Logs/YYYY-MM-DD/YYYY-MM-DD_HH-mm_[department]_[task-id].md`

Skill draft:
`AgentVault/60_Skills/Drafts/[skill-name]/SKILL.md`

Published skill memory:
`AgentVault/60_Skills/Published/[skill-name]/best_skill.md`

Department handoff:
`AgentVault/50_Memory/Department_Handoffs/[task-id]_[department].md`

## Department Handoff

When a task must move to another department, create a handoff note with:
- initiating department
- receiving department
- task ID and priority
- related action memory files
- related skills and plugins
- current state
- background
- completed work
- requested next work
- prohibitions
- success standard
- destination for the result note

Keep handoff notes short and store them under:
`AgentVault/50_Memory/Department_Handoffs/`

## Failure And Handoff Examples

When handling failures, blocked states, user confirmations, cross-department handoffs, result writebacks, or safety-boundary references, read:
`AgentVault/60_Skills/Drafts/obsidian-memory/examples_failure_and_handoff.md`

Use those examples as draft guidance only. Prefer the writer commands below, keep `append-log` for already-created action memories, and keep high-risk confirmation states in `坎-艮` or `坎-艮-兑`.

## Writer Commands

Create an action memory:

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  create \
  --department '工程部' \
  --task-id 'example-task' \
  --title '示例任务' \
  --status 'planned' \
  --risk-level 'low' \
  --current-mode '乾-坤' \
  --user-goal '记录用户目标。' \
  --action-goal '本次只做一个小步行动。'
```

Use the path printed by `create` as the source of truth. For later `append-log`, `set-status`, or `uri` commands, pass that exact absolute path or the equivalent vault-relative `AgentVault/...md` path; do not invent or hand-type the timestamped filename.

Append a step result:

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  append-log \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/example.md' \
  --message '完成一个小步行动。'
```

After appending final results, update the action memory frontmatter:

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  set-status \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/example.md' \
  --status 'completed' \
  --current-mode '坤-兑'
```

Generate an Obsidian open URI:

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  uri \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/example.md'
```

## Required Content

Include these sections in every action memory:
- User goal
- Current one-step action goal
- Known and unknown context
- Materials read or needed
- Planned changes
- Explicit prohibitions
- Skills and plugins needed
- Action steps
- Risk check and mitigation
- Department notifications
- Execution result
- New or updated files
- Next step
- Short user-facing report
- Chinese title, Chinese aliases, Chinese search keywords, Chinese directory path, Chinese file elements, Chinese time elements, and Chinese summary for retrieval.

## Safety Boundaries

- Do not delete files unless the user explicitly confirms.
- Do not send messages, payments, forms, emails, or external uploads without explicit confirmation.
- Do not install Obsidian plugins by default.
- Do not modify `.obsidian` settings unless that is the specific confirmed task.
- Keep memory writes inside the vault.
- Record uncertainty as a pending confirmation item instead of guessing.

## Verification

After editing the writer or this skill, run:

```bash
python3 -m unittest discover -s '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools' -p 'test_*.py'
python3 '/Users/peipei/.codex/skills/.system/skill-creator/scripts/quick_validate.py' '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/60_Skills/Drafts/obsidian-memory'
```

If validation fails, fix the smallest issue and rerun.
