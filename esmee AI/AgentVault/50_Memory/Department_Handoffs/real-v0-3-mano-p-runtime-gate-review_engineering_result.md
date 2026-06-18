---
type: department_review_result
task_id: real-v0-3-mano-p-runtime-gate-review
department: 工程部
date: 2026-06-17
status: approved_with_notes
risk_level: high
current_mode: 巽-坎-兑
related_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Runtime_Gate_Plan.md
related_source_review:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md
---

# Engineering Review Result: Mano-P Runtime Gate

## Verdict

`approved_with_notes`

工程部批准进入“准备 help-only runtime 候选包”，但不批准执行 `mano-cua --help`。

## Must Fix Before Candidate Package

- 明确 timeout 机制；macOS 默认不一定有 `timeout`，候选包必须指定可用的超时包装方式。
- 使用 `<CLEAN_HOME>` 占位符定义 clean HOME，不把真实 HOME、配置值或私密路径写入共享结果。
- 明确 exact binary：需要先验证 `/opt/homebrew/bin/mano-cua` 是存在的 wrapper 路径，但只做文件元数据/路径验证，不执行它。
- 列出 expected writes：只允许 `<CLEAN_HOME>` 内可能生成 `.mano/` 或缓存；真实 HOME、仓库、Homebrew 全局状态均应为 no-write。
- 定义 verification checks：执行前后检查真实 HOME 未写入、仓库未变更、无权限弹窗、无 GUI、无网络迹象、无敏感输出入库。
- 输出策略需更精确：不保存完整 stdout/stderr，只保存脱敏摘要、退出码、是否命中停止条件。

## Recommended Additions

- 将 `mano-cua --help` 候选拆成两步：先 wrapper 路径只读验证，再 help-only runtime 候选包确认。
- 说明为什么需要 `/opt/homebrew/bin`，并禁止继承 shell、agent、API、token 相关环境。
- 补充 `PWD` / 工作目录策略，建议使用非仓库临时工作目录。
- 停止条件增加：任何非 help 文案之外的初始化、session、config、network、permission、GUI、download 字样都停止并升级复审。
- 输出中如出现 token-like 字符串、真实 HOME、设备标识、配置值，只记录“敏感输出已拦截”。

## Exact Candidate Package Requirements

- Purpose: only prepare candidate package, not execute.
- Command class: help-only.
- Exact binary: `/opt/homebrew/bin/mano-cua`
- Command template: `env -i HOME=<CLEAN_HOME> PATH=/opt/homebrew/bin:/usr/bin:/bin LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 MANO_RUNTIME_GATE=help-only <TIMEOUT_WRAPPER> /opt/homebrew/bin/mano-cua --help`
- Expected network: none.
- Expected permissions: none.
- Expected GUI: none.
- Expected writes: none outside `<CLEAN_HOME>`; ideally none at all.
- Verification checks: pre/post true HOME config untouched, repo unchanged, no GUI/window open, no permission prompt, no download/install, no cloud/session text, output summarized only.
- Required approvals before execution: user, 安全部, 工程部, 记忆部行动记忆模板。

## Go / No-Go

- 准备 help-only runtime 候选包：Go with notes。
- 执行 `mano-cua --help`：No-Go。
- `mano-cua check/config/stop/install-sdk/install-model/run`、cloud mode、local mode、GUI、screenshot、permissions、download、install、tap、wrapper execution before explicit confirmation：No-Go。

## Summary

Runtime gate 的方向工程上成立：clean HOME、`env -i`、最小 PATH、exact binary、timeout、输出脱敏是正确组合。但候选包还需要把 timeout、expected writes、pre/post verification 和 wrapper 路径只读验证写到可执行级别。
