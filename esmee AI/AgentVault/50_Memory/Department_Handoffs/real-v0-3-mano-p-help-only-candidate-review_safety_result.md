---
type: department_review_result
task_id: real-v0-3-mano-p-help-only-candidate-review
department: 安全部
date: 2026-06-17
status: approved_with_notes
risk_level: high
current_mode: 坎-兑
related_candidate_package:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Help_Only_Runtime_Candidate_Package.md
---

# Safety Review Result: Help-only Runtime Candidate Package

## Verdict

`approved_with_notes`

安全部批准进入“执行前确认包准备阶段”，但不批准创建 runner 或执行 help-only runtime。

## Must Fix Before Execution Confirmation Package

- 增加“执行前确认包仍不是执行授权”的首行警示。
- 明确 runner 文件若要创建，也需先单独复审；当前只批准准备确认包，不批准创建或运行 runner。
- 补充 clean HOME 和 run cwd 的生命周期：谁创建、何时检查、何时清理；清理不得使用模糊删除。
- 补充“真实 HOME 路径不得出现在保存摘要中”，若出现只记录 `sensitive output intercepted`。
- 补充 preflight 禁止导入 `visual` 或调用任何 Python entrypoint，只能做文件元数据/文本只读检查。

## Recommended Additions

- 在确认包里加入三部门签核字段：安全部、工程部、记忆部。
- 加入用户确认原文摘要字段，明确只允许 help-only。
- 加入“repository status before/after unchanged”的摘要项。
- 加入“network observed: none/unknown/stop-hit”的摘要项，不保存完整网络日志。
- 加入“writes outside clean HOME: none/stop-hit”的摘要项。

## Prohibitions To Keep

- no cloud / no local mode
- no screenshot / no GUI / no permissions
- no config values / no real HOME config read
- no full stdout/stderr save
- no token/env inheritance
- no `run/check/config/stop/install-sdk/install-model/--local`
- no app/url launch
- no clipboard mutation
- no bash capability
- no download/install/tap/reinstall/update/upgrade

## Go / No-Go

- 准备“执行前确认包”：Go with notes。
- 创建 runner 文件：No-Go until separately reviewed.
- 执行 `/opt/homebrew/bin/mano-cua --help`：No-Go until user plus safety/engineering/memory confirmations.
- 任何 GUI、截图、权限、cloud、config、install、download：No-Go。

## Summary

候选包对 cloud、截图、权限、GUI、config values 和完整输出保存的禁止足够清楚；clean HOME、env allowlist、timeout、输出脱敏和停止条件总体到位。安全部批准进入“执行前确认包准备阶段”，但仍不批准创建 runner 或执行 help-only。
