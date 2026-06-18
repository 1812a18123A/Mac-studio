---
type: department_discussion_summary
task_id: real-v0-3-mano-p-stage-1-plan-review
date: 2026-06-17
owner_department: 总控办公室
status: completed
risk_level: medium
current_mode: 坤-兑
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_19-55_总控办公室_mano-p-stage-1-plan-department-review.md
related_results:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_engineering_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_safety_result.md
related_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
---

# 讨论汇总：Mano-P Stage 1 计划部门审查

## 1. 审查问题

Mano-P Stage 1 隔离安装计划是否足够可审计、可回退、可复现，是否可以进入真实命令执行前的用户确认阶段。

本轮只审查计划和文档，不执行任何安装或 GUI 操作。

## 2. 部门结论

| 部门 | 结论 | 核心意见 |
| --- | --- | --- |
| 工程部 | `approved_with_notes` | 计划骨架可用，但执行前必须补 Homebrew/tap/formula/package 元数据清单、命令分级表、缓存路径、清理回退草案和执行记录模板。 |
| 安全部 | `approved_with_notes` | 计划可作为等待确认前的安全计划，但 Homebrew 元数据查询前仍需命令白名单、联网/缓存/auto-update 说明和再次安全复核。 |

## 3. 总控结论

Mano-P Stage 1 隔离安装计划通过部门只读审查，但不能进入安装、tap、run、model download、权限授权或 GUI 自动化。

当前允许继续的最低风险下一步：

```text
只做 Stage 1 执行清单和用户确认包。
```

当前仍禁止：

- `brew tap`
- `brew install`
- `mano-cua check`
- `mano-cua install-sdk`
- `mano-cua install-model`
- `mano-cua run`
- `clawhub install`
- SDK/model/binary/skill 下载
- Screen Recording / Accessibility / Automation 权限授权
- 截图、点击、输入、真实 GUI 操作
- cloud mode

## 4. 必须补充项

下一步文档需要补：

- Homebrew 元数据查询命令白名单。
- 每条候选命令的风险等级、是否联网、是否写缓存、是否触发 auto-update。
- `.external/` 隔离目录的 `.gitignore` 方案；未确认前优先使用 `/private/tmp/`。
- Homebrew tap、formula、package、Python 依赖、SDK、模型的来源和 license 检查项。
- pre/post install、PATH、后台服务、launch agent 检查项。
- 清理与回退草案，路径必须明确，不允许模糊删除。
- Stage 1 执行记录模板。
- 用户确认包：允许什么、禁止什么、遇到什么立即停止。

## 5. 下一步

创建以下文档：

```text
AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
```

该文档仍只做计划，不执行命令。
