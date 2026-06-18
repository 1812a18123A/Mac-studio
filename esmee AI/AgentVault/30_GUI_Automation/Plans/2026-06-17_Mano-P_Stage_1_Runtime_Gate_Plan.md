---
type: gui_runtime_gate_plan
project_id: mano-p
date: 2026-06-17
owner_department: GUI 自动化部
status: completed
risk_level: high
current_mode: 坤-坎-艮-兑
related_python_source_review:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md
related_formula_review:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Formula_Dependency_Review.md
related_execution_checklist:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
related_install_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-55_gui-自动化部_mano-p-runtime-gate-plan.md
related_review_results:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-runtime-gate-review_safety_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-runtime-gate-review_engineering_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-runtime-gate-review_summary.md
related_help_only_candidate_package:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Help_Only_Runtime_Candidate_Package.md
related_help_only_candidate_review:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-help-only-candidate-review_summary.md
requires_user_confirmation_for_next_step: true
---

# Mano-P Stage 1 Runtime Gate Plan

## 1. Gate 结论

本文件是 runtime gate plan，不是 runtime 授权。

当前结论：

- `runtime_allowed`: no
- `mano_cua_help_allowed`: no
- `runtime_gate_review_completed`: yes
- `help_only_candidate_package_allowed`: yes_with_notes
- `help_only_candidate_package_prepared`: yes
- `help_only_candidate_review_completed`: yes
- `execution_confirmation_package_allowed`: yes_with_notes
- `mano_cua_check_allowed`: no
- `mano_cua_run_allowed`: no
- `cloud_mode_allowed`: no
- `local_mode_allowed`: no
- `screenshot_allowed`: no
- `gui_control_allowed`: no
- `bash_capability_allowed`: no
- `app_url_launch_allowed`: no
- `clipboard_mutation_allowed`: no
- `permission_grant_allowed`: no
- `config_value_read_allowed`: no

下一步只允许做：

```text
准备 help-only execution confirmation package；仍不得执行。
```

部门复审结果：

- 安全部：`approved_with_notes`
- 工程部：`approved_with_notes`
- 记忆部：`approved_with_notes`
- 汇总结论：允许准备 help-only execution confirmation package，不允许执行。
- 候选包状态：已复审完成，等待准备执行前确认包。

## 2. 必须解决的风险

Python source 审查已确认：

- 默认 `mano-cua run` 是 cloud mode。
- Cloud mode 会连接 `https://mano.mininglamp.com`。
- Cloud session body 可能包含 task、device id、platform、expected result 和 bash capability。
- Runtime 可以截图、打开 app/url、执行鼠标键盘动作、修改剪贴板、运行 shell command。
- Local mode 不等于低风险；它仍会截图、执行动作、保存 raw responses，并依赖模型/SDK。
- `$HOME/.mano/config.json` 已存在，本轮只读过键名，没有读取值。

因此，任何 runtime 前必须先通过本 gate。

## 3. Runtime 分层

### Layer 0: 文档与审查

允许：

- 继续写计划、审查报告和确认包。
- 读取已提交的审查文档。

禁止：

- 所有 `mano-cua` runtime command。
- 所有 Homebrew install/update/reinstall。
- 所有 GUI、截图、权限和外发行为。

当前状态：

- 已完成。

### Layer 1: 静态命令候选确认

候选命令：

```text
mano-cua --help
```

当前状态：

- 可准备候选包，但尚未授权执行。

进入条件：

- 用户明确确认只允许 `mano-cua --help`。
- 安全部确认该命令可以在 clean HOME 中执行。
- 工程部确认命令路径和环境变量。
- 记忆部确认行动记忆模板已创建。

明确禁止：

- `mano-cua run`
- `mano-cua check`
- `mano-cua config`
- `mano-cua stop`
- `mano-cua install-sdk`
- `mano-cua install-model`
- `mano-cua --local`

### Layer 2: Runtime help dry check

本层只是未来候选，不在本文件授权。

允许候选：

```bash
HOME=/private/tmp/esmee-mano-cua-clean-home \
MANO_RUNTIME_GATE=help-only \
mano-cua --help
```

预期副作用：

- 可能执行 Python entrypoint imports。
- 可能读取 process environment。
- 不应创建 session。
- 不应截图。
- 不应打开 app/url。
- 不应读取真实 `$HOME/.mano/config.json`。
- 不应写真实 `$HOME/.mano`。

停止条件：

- 出现网络请求迹象。
- 出现权限提示。
- 出现截图、GUI overlay、app/window/browser 打开。
- 产生真实 HOME 写入。
- 输出包含隐私路径、config value、token、账号信息。
- 命令超过预设时间。

### Layer 3: Sandbox GUI candidate

当前禁止。

进入条件：

- 单独创建本地静态测试窗口。
- 明确允许 Screen Recording 或替代观察方式。
- 明确禁止真实账号、Obsidian 设置、GitHub 设置、浏览器会话、付款、上传、消息。
- 明确动作白名单、最大步数和手动停止方式。

### Layer 4: Real GUI action

当前禁止。

必须另立项目，不属于 Stage 1。

## 4. Clean HOME 策略

未来任何 runtime command 都必须使用 clean HOME。

推荐路径：

```text
/private/tmp/esmee-mano-cua-clean-home
```

要求：

- 不读取真实 `$HOME/.mano/config.json`。
- 不写真实 `$HOME/.mano`。
- 不继承真实 model path、python path、sdk-installed、model-installed。
- 若命令必须创建 `.mano`，只能创建在 clean HOME 内。

禁止：

- 提交 clean HOME 内容。
- 保存 config value。
- 读取真实 config value，除非用户单独确认。

## 5. 环境变量策略

未来候选 runtime 必须最小化环境。

建议命令包装：

```bash
env -i \
  HOME=/private/tmp/esmee-mano-cua-clean-home \
  PATH=/opt/homebrew/bin:/usr/bin:/bin \
  LANG=en_US.UTF-8 \
  LC_ALL=en_US.UTF-8 \
  MANO_RUNTIME_GATE=help-only \
  mano-cua --help
```

说明：

- `env -i` 避免继承 token、API key、agent metadata。
- `HOME` 指向 clean HOME。
- `PATH` 只保留必要系统路径。
- 不设置 cloud API key。
- 不设置 agent shell。

仍需确认：

- 使用 `env -i` 是否会影响 Homebrew wrapper 中的 Python 路径。
- 是否需要显式调用 `/opt/homebrew/bin/mano-cua`。

## 6. 命令白名单

### 当前允许

无 runtime command。

### 未来候选

| 命令 | 当前状态 | 风险 | 进入条件 |
| --- | --- | --- | --- |
| `mano-cua --help` | not_allowed_yet | low-medium | 用户、安全部、工程部确认 runtime help gate |

### 禁止命令

| 命令 | 禁止原因 |
| --- | --- |
| `mano-cua run ...` | cloud/GUI/screenshot/action risk |
| `mano-cua check` | 可读写 config 并运行 subprocess dependency checks |
| `mano-cua config --list` | 会打印真实 config values |
| `mano-cua config --get/--set` | 会读取/写入 config，可能触发验证 subprocess |
| `mano-cua stop` | 会写 stop flag，并可能调用 cloud stop endpoint |
| `mano-cua install-sdk` | pip install、GitHub cider、写 config |
| `mano-cua install-model` | HuggingFace/modelscope 下载 |
| `brew reinstall mano-cua` | 重新触发 pip dependency resolution |
| `brew upgrade/update` | 修改 Homebrew 全局状态 |

## 7. 权限策略

当前不授予：

- Screen Recording
- Accessibility
- Automation
- Full Disk Access
- Files and Folders
- Browser automation

若未来出现任何权限提示：

1. 立即停止。
2. 不点击 Allow。
3. 记录权限名称、请求进程、上下文。
4. 等待用户和安全部确认。

## 8. 网络策略

当前不允许：

- cloud mode。
- session creation。
- model download。
- SDK download。
- telemetry。
- 外发截图、任务、窗口标题、路径、config。

对于 `mano-cua --help` 候选：

- 预期网络访问应为 none。
- 若出现网络访问迹象，立即停止。
- 不保存完整网络日志到仓库。

## 9. 数据和日志策略

禁止提交或外发：

- screenshots。
- trajectory。
- raw responses。
- full command output with private paths。
- `$HOME/.mano/config.json` values。
- device id。
- session id。
- token/key/password。

允许写入仓库：

- 脱敏摘要。
- 命令名称。
- 是否成功。
- 是否触发停止条件。
- 下一步建议。

## 10. Runtime Action Memory Template

未来若用户授权执行 `mano-cua --help`，先创建行动记忆并记录：

```text
command:
exact_binary:
environment:
clean_home:
allowed_network:
expected_network:
expected_writes:
expected_permissions:
expected_gui:
timeout:
stop_conditions:
actual_result_summary:
actual_writes:
actual_network_observed:
permission_prompt_observed:
gui_observed:
secret_scan_result:
next_step:
```

## 11. Go / No-Go

当前决定：

- `go_runtime`: no
- `go_prepare_help_only_candidate_package`: yes_with_notes
- `help_only_candidate_review_completed`: yes
- `go_prepare_execution_confirmation_package`: yes_with_notes
- `next_action`: 准备 help-only execution confirmation package

未来 `mano-cua --help` 的 go 条件：

- 用户明确确认。
- 安全部确认无 cloud、无截图、无权限、无 GUI。
- 工程部确认 clean HOME 和 exact binary。
- 记忆部确认行动记忆已建。
- 命令必须使用 timeout。
- 命令输出必须脱敏摘要，不保存完整敏感输出。

## 12. 给用户的确认包

若进入下一步，请用户选择：

### Option A: 继续只写文档

允许：

- 让安全部/工程部复审 runtime gate plan。
- 继续完善确认包和 stop condition。

禁止：

- 所有 runtime command。

### Option B: 准备 help-only runtime 候选包

允许：

- 写具体命令草案。
- 写 clean HOME 创建/验证草案。
- 写 timeout/输出脱敏/回退草案。

禁止：

- 实际执行 `mano-cua --help`。

### Option C: 执行 `mano-cua --help`

当前不建议直接进入。

若用户坚持，必须重新确认：

- exact command。
- clean HOME。
- timeout。
- no cloud。
- no screenshot。
- no permissions。
- no GUI。
- no config values。
- allowed outputs。
- stop conditions。
