---
type: repository_policy
policy_id: agentvault-repository-policy-v0.2
date: 2026-06-17
owner_department: 总控办公室
status: active
risk_level: medium
current_mode: 坤-兑
chinese_title: AgentVault 仓库策略 v0.2
中文标题: AgentVault 仓库策略 v0.2
summary_zh: 定义 AgentVault 中哪些资料可以作为正式仓库资产、哪些资料默认本地保留，以及提交前的安全检查规则。
中文摘要: 定义 AgentVault 中哪些资料可以作为正式仓库资产、哪些资料默认本地保留，以及提交前的安全检查规则。
aliases:
  - 仓库策略
  - Git收纳边界
  - AgentVault版本控制规则
search_keywords:
  - 仓库策略
  - Git提交
  - 正式资产
  - 私有资料
  - 敏感信息
  - 提交前检查
  - 远端推送
检索元素:
  - 仓库策略
  - Git提交
  - 正式资产
  - 私有资料
  - 敏感信息
  - 提交前检查
  - 远端推送
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_17-14_总控办公室_implement-v0-2-repository-policy-workflow.md
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_19-02_总控办公室_redact-thread-id-registry-forward-fix.md
related_baseline:
  - AgentVault/00_System/Baselines/2026-06-17_Agent_OS_v0.1_Baseline.md
related_departments:
  - 总控办公室
  - 工程部
  - 记忆部
  - 安全部
---

# AgentVault Repository Policy v0.2

## 中文检索索引

- 中文标题：AgentVault 仓库策略 v0.2
- 中文摘要：定义 AgentVault 中哪些资料可以作为正式仓库资产、哪些资料默认本地保留，以及提交前的安全检查规则。
- 相关部门：总控办公室、工程部、记忆部、安全部。
- 中文关键词：仓库策略、Git 提交、正式资产、私有资料、敏感信息、提交前检查、远端推送。

本文件定义 esmee AI vault 中哪些资料属于正式仓库资产，哪些资料默认只保留在本地 Obsidian。目标是减少误提交、保护私人资料，并让 AgentVault 的版本历史保持可审计。

## 1. 核心原则

1. `AgentVault/` 是正式系统资产目录。
2. vault 顶层普通笔记默认视为私人资料。
3. `.obsidian/` 默认视为本机 UI 状态和个人设置。
4. 行动记忆必须优先写入 `AgentVault/50_Memory/Action_Logs/`。
5. 任何例外入库都要先写行动记忆，并在提交前检查 diff。

## 2. 默认纳入版本控制

以下路径默认可以纳入 Git：

- `AgentVault/00_System/`
- `AgentVault/20_Engineering/`
- `AgentVault/50_Memory/Action_Logs/`
- `AgentVault/50_Memory/Department_Handoffs/`
- `AgentVault/60_Skills/`
- `AgentVault/70_Safety/`
- `.gitignore`

纳入前仍需检查：

- 是否包含密钥、token、账号、隐私资料。
- 是否包含真实 Codex thread id、pending worktree id、connector session id 等内部调度元数据。
- 是否包含未经用户确认的外部资料。
- 是否为当前任务需要的最小文件集合。
- 是否已在行动记忆中记录原因和结果。

## 3. 默认不纳入版本控制

以下路径默认不纳入 Git：

- `.obsidian/`
- vault 顶层 `*.md`
- vault 顶层 `*.docx`
- `AgentVault/00_System/Private/`
- `行动记忆/`
- `.DS_Store`

说明：

- 顶层普通笔记可能包含私人想法、草稿或导入材料。
- `.obsidian/` 可能包含本机窗口状态、插件状态和个人偏好。
- `AgentVault/00_System/Private/` 用于本地运行时映射和内部调度元数据，例如真实 Codex thread id；不得提交或 push。
- `行动记忆/` 是旧式或非 AgentVault 结构的本地资料；正式行动记忆应写入 `AgentVault/50_Memory/Action_Logs/`。

## 4. 例外流程

如果确实需要把默认不纳入的文件提交到仓库，必须先完成：

1. 创建或更新行动记忆。
2. 说明文件用途、风险、是否含隐私资料。
3. 获得用户明确确认。
4. 只 stage 指定文件，不使用批量模糊 stage。
5. 提交前执行 `git diff --cached --stat` 和必要的内容检查。

## 5. 提交前检查清单

每次 Git 提交前检查：

- 是否只包含本次任务需要的文件。
- 是否没有 `.obsidian/`、顶层普通笔记、docx 或旧式 `行动记忆/`。
- 是否没有 `AgentVault/00_System/Private/` 或真实 Codex thread id 等内部调度元数据。
- 是否没有密钥、token、截图、音频、客户资料或敏感日志。
- 是否已更新行动记忆并记录实际结果。
- 是否需要同步到远端；若要 push，先确认远端目标和分支。

## 6. 当前 v0.2 决策

本次 v0.2 最小策略是：

- 保留并追踪 `AgentVault/` 下的正式系统资料。
- 忽略本机 Obsidian UI 状态和顶层私人资料。
- 不删除任何未跟踪文件。
- 不改变 vault 内容结构，只改变 Git 收纳边界。
