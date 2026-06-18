---
type: department_review_result
task_id: real-v0-3-mano-p-help-only-candidate-review
department: 工程部
date: 2026-06-17
status: approved_with_notes
risk_level: high
current_mode: 巽-坎-兑
related_candidate_package:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Help_Only_Runtime_Candidate_Package.md
---

# Engineering Review Result: Help-only Runtime Candidate Package

## Verdict

`approved_with_notes`

工程部批准进入“执行前确认包准备阶段”，但不批准执行。

## Must Fix Before Execution Confirmation Package

- 补一个 Python timeout runner 草案，但只写草案/伪代码，不创建可执行文件、不运行。
- Runner 需明确：不用 shell、只用 argv list、固定 cwd、固定 env allowlist、stdout/stderr 只进内存、10 秒超时、超时后强制终止。
- 增加输出大小上限，例如 stdout/stderr 最大字节数和最大行数，防止意外长输出。
- Preflight/post-run verification 需要写成逐项清单，区分“可在确认包中描述”和“执行后才检查”。
- Output redaction 需列出具体拦截类别：真实 HOME、配置值、设备标识、session、token-like、stack trace 私密路径。

## Recommended Additions

- Execution confirmation package 里保留 exact binary，但不提供一键复制执行命令。
- Wrapper path verification 只允许文件元数据、symlink target、wrapper 文本摘要；不得执行 wrapper。
- Clean HOME 和 RUN_CWD 使用占位符；确认包只描述路径规则，不预创建目录。
- Post-run 检查增加：真实 HOME 配置未被读取/写入、仓库状态未变、无 GUI/权限/网络/下载/安装迹象。
- Stop condition 增加：出现 cloud/session/config/check/run/install/model/sdk 等非 help 语义时立即停止。

## Execution Confirmation Package Requirements

- `command_class`: `help-only`
- `exact_binary`: Homebrew wrapper absolute path
- `argv`: exact binary + `--help`
- `cwd`: `<RUN_CWD>`，必须在仓库外
- `env`: only `HOME`, `PATH`, `LANG`, `LC_ALL`, `MANO_RUNTIME_GATE`
- `timeout`: Python stdlib `subprocess` timeout, no GNU timeout assumption
- `expected_network`: none
- `expected_permissions`: none
- `expected_gui`: none
- `expected_writes`: none outside `<CLEAN_HOME>`
- `output_storage`: redacted summary only, no full stdout/stderr
- `approvals`: 用户、安全部、工程部、记忆部全部确认后才可执行

## Go / No-Go

- Go: 可以进入“执行前确认包”准备阶段。
- No-go: 不能执行候选包，不能运行 Mano-P 入口，不能安装、下载、授权、截图、点击、输入或打开 GUI。
- No-go: 不能进入 `check/config/run/stop/install-sdk/install-model/local/cloud` 任何路径。

## Summary

候选包工程方向成立：exact binary、clean HOME、RUN_CWD、env allowlist、Python timeout、pre/post verification 和脱敏策略都覆盖了核心风险。进入下一步前要把 runner 草案和验证清单写到可审查级别；批准准备确认包，不批准执行。
