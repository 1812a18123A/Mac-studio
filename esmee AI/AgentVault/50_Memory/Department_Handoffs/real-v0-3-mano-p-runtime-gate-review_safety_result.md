---
type: department_review_result
task_id: real-v0-3-mano-p-runtime-gate-review
department: 安全部
date: 2026-06-17
status: approved_with_notes
risk_level: high
current_mode: 坎-兑
related_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Runtime_Gate_Plan.md
related_source_review:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md
---

# Safety Review Result: Mano-P Runtime Gate

## Verdict

`approved_with_notes`

安全部批准进入“准备 help-only runtime 候选包”，但不批准执行 `mano-cua --help`。

## Must Fix Before Candidate Package

- 把 `mano-cua --help` 候选包写成“准备包”，明确仍不授权执行。
- 补充 exact binary 解析方式，只允许记录脱敏路径摘要，不写完整私密路径。
- 补充 clean HOME 预创建和验证步骤：只能使用临时空目录，执行后检查是否产生 `.mano`，不得读取真实 HOME 配置。
- 补充 timeout 和输出处理：必须限时，只保存脱敏摘要，不保存完整 stdout/stderr。
- 补充停止条件：只要出现网络、权限提示、GUI 窗口、截图迹象、真实 HOME 写入、config value、token/env 泄露，立即停止。

## Recommended Additions

- 显式列出允许环境变量白名单。
- 声明 `PATH` 只保留必要系统路径与确认后的 binary 路径。
- 加入“执行前后不读取、不打印、不提交 config values”的检查项。
- 加入“help-only 不允许 `check/config/run/stop/local/install-*` fallback”的硬规则。
- 候选包由安全部、工程部、记忆部复核后，再请求用户确认是否执行。

## Prohibitions To Keep

- no cloud
- no screenshot
- no permissions
- no GUI
- no config values
- no real HOME config read
- no token/env inheritance
- no `mano-cua run/check/config/stop/install-sdk/install-model/--local`
- no app/url launch
- no clipboard mutation
- no bash capability
- no full command output with sensitive paths

## Go / No-Go

- 准备 help-only runtime 候选包：Go with notes。
- 执行 `mano-cua --help`：No-Go。
- 任何 GUI、截图、cloud、权限、config、install、download：No-Go。

## Summary

Runtime Gate Plan 对 no cloud、no screenshot、no permissions、no GUI、no config values 的边界已经足够清楚。clean HOME 加 `env -i` 能显著降低真实配置和 token/env 泄露风险，但候选包还需要补 exact binary、timeout、脱敏输出、真实 HOME 写入检测和停止条件。
