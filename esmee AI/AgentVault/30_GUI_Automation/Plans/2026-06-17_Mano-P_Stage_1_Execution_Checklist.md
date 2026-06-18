---
type: gui_execution_checklist
project_id: mano-p
date: 2026-06-17
owner_department: GUI 自动化部
status: waiting_user_confirmation
risk_level: medium
current_mode: 乾-坎-艮
chinese_title: Mano-P Stage 1 执行清单
中文标题: Mano-P Stage 1 执行清单
summary_zh: 记录 Mano-P Stage 1 从隔离安装计划到 help-only execution confirmation package 的执行前清单、当前状态、禁止事项和用户确认要求。
中文摘要: 记录 Mano-P Stage 1 从隔离安装计划到 help-only execution confirmation package 的执行前清单、当前状态、禁止事项和用户确认要求。
aliases:
  - Mano-P执行清单
  - Stage1执行前清单
  - help-only确认链路
search_keywords:
  - Mano-P
  - Stage 1
  - 执行清单
  - help-only
  - 用户确认
  - 运行门禁
  - 禁止执行
检索元素:
  - Mano-P
  - Stage 1
  - 执行清单
  - help-only
  - 用户确认
  - 运行门禁
  - 禁止执行
source_project:
  - https://github.com/Mininglamp-AI/Mano-P
source_readme:
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/README.md
source_license:
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/LICENSE
related_install_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
related_plan_review:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_summary.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_engineering_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_safety_result.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-03_gui-自动化部_mano-p-stage-1-execution-checklist.md
related_metadata_result:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Metadata_Query_Result.md
related_formula_review:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Formula_Dependency_Review.md
related_python_source_review:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md
related_runtime_gate_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Runtime_Gate_Plan.md
related_runtime_gate_review:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-runtime-gate-review_summary.md
related_help_only_candidate_package:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Help_Only_Runtime_Candidate_Package.md
related_help_only_candidate_review:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-help-only-candidate-review_summary.md
related_execution_confirmation_package:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Help_Only_Execution_Confirmation_Package.md
requires_user_confirmation: true
---

# Mano-P Stage 1 Execution Checklist

## 中文检索索引

- 中文标题：Mano-P Stage 1 执行清单
- 中文摘要：记录 Mano-P Stage 1 从隔离安装计划到 help-only execution confirmation package 的执行前清单、当前状态、禁止事项和用户确认要求。
- 相关部门：GUI 自动化部、工程部、安全部、记忆部。
- 中文关键词：Mano-P、Stage 1、执行清单、help-only、用户确认、运行门禁、禁止执行。

## 1. 当前结论

本文件是执行前清单和用户确认包，不是执行授权。

当前状态：

- `homebrew_metadata_query_completed`: yes
- `formula_dependency_review_completed`: yes
- `python_source_review_completed`: yes
- `runtime_gate_plan_completed`: yes
- `runtime_gate_review_completed`: yes
- `help_only_candidate_package_allowed`: yes_with_notes
- `help_only_candidate_package_prepared`: yes
- `help_only_candidate_review_completed`: yes
- `execution_confirmation_package_allowed`: yes_with_notes
- `execution_confirmation_package_prepared`: yes
- `brew_tap_allowed`: no
- `brew_install_allowed`: no
- `mano_cua_run_allowed`: no
- `sdk_download_allowed`: no
- `model_download_allowed`: no
- `permission_grant_allowed`: no
- `gui_execution_allowed`: no
- `cloud_mode_allowed`: no

工程部和安全部均已批准 Stage 1 计划作为文档计划，结论为 `approved_with_notes`。两部门共同要求先补命令白名单、风险分级、网络/缓存说明、执行记录模板和用户确认包。

用户已确认并完成 Option B 元数据查询。结果显示 `mano-cua` 与 `Mininglamp-AI/tap` 已经在本机 Homebrew 中安装/存在；本轮未安装、未运行。

用户随后确认继续执行，只读完成 formula 内容和依赖树审查。审查发现 formula 会在安装阶段执行 `pip install -r requirements.txt`，因此 Homebrew dependency tree 不能覆盖真实 Python runtime dependency surface。下一步只能等待用户确认是否只读审查 `requirements.txt`、`visual/vla.py` 和相关 source entrypoint。

用户再次确认继续执行后，已只读完成 Python requirements、entrypoint 和安全相关 source 审查。审查发现默认 `run` 使用 cloud mode，runtime 可截图、打开 app/url、执行鼠标键盘动作、使用 bash capability，并可能读取 `$HOME/.mano/config.json`。下一步不能直接运行；只能先写 runtime gate plan。

用户继续确认下一步后，已完成 runtime gate plan。结论仍是 `runtime_allowed: no`；下一步只允许部门复审 gate plan，或在用户再次确认后准备 help-only runtime 候选包，不能直接执行。

安全部和工程部已真实线程复审 runtime gate plan，结论均为 `approved_with_notes`。共同批准进入“准备 help-only runtime 候选包”，但仍不批准执行 `mano-cua --help`。

Help-only runtime 候选包已准备完成。它定义了 exact binary、clean HOME、`env -i`、Python timeout runner 规范、expected writes、pre/post verification、输出脱敏和停止条件；当前仍不授权执行。

安全部、工程部和记忆部已真实线程复审 help-only runtime 候选包，结论均为 `approved_with_notes`。共同允许准备 help-only execution confirmation package；仍不允许执行 `mano-cua --help`、创建 runner 文件、截图、GUI、cloud/local、install/download/tap 或读取配置值。

Help-only execution confirmation package 已准备完成。它明确声明“确认包仍不是执行授权”，只包含伪代码 runner 规范、clean HOME/RUN_CWD 生命周期、输出大小上限、脱敏策略、preflight/post-run checklist、四方确认字段和 stop conditions；当前仍不授权执行。

## 2. 官方信息摘要

当前官方 README 显示：

- Mano-P 面向 GUI-VLA 和边缘设备。
- 公开入口包括 `mano-cua`、`mano-skill`、Homebrew tap、local mode、cloud mode、SDK/model。
- cloud mode 是默认形态之一，会涉及屏幕截图和任务描述外发到云端视觉模型服务。
- local mode 需要本地模型/SDK，并对 Apple Silicon、内存、系统权限有要求。
- GUI 操作涉及 Screen Recording、Accessibility、点击、输入、截图等高风险权限与动作。

esmee AI 当前只考虑未来评估 `mano-cua` 的最小隔离路径；不评估 `mano-skill` 自动接入，不启用 cloud mode。

## 3. 命令风险分级

### 3.1 允许写入计划、但未授权执行

以下命令只作为候选清单出现，尚未授权执行。

| 命令 | 风险级别 | 预期用途 | 可能副作用 | 当前状态 |
| --- | --- | --- | --- | --- |
| `sw_vers` | low | 读取 macOS 版本 | 无明显写入 | not_allowed_yet |
| `uname -m` | low | 读取 CPU 架构 | 无明显写入 | not_allowed_yet |
| `sysctl -n machdep.cpu.brand_string` | low | 读取 CPU 信息 | 无明显写入 | not_allowed_yet |
| `system_profiler SPHardwareDataType` | medium | 读取硬件概况 | 可能输出本机序列号等设备信息 | not_allowed_yet |
| `brew --version` | low | 读取 Homebrew 版本 | 无明显写入 | not_allowed_yet |
| `brew info mano-cua` | medium | 查询 formula/package 元数据 | 可能联网、可能触发 auto-update、可能写 Homebrew 缓存 | not_allowed_yet |
| `brew search mano-cua` | medium | 搜索 package 名称 | 可能联网、可能写缓存 | not_allowed_yet |
| `brew tap-info Mininglamp-AI/tap` | medium | 查询 tap 元数据 | 可能联网、可能写缓存 | not_allowed_yet |

### 3.2 默认禁止

| 命令 | 风险级别 | 禁止原因 |
| --- | --- | --- |
| `brew tap Mininglamp-AI/tap` | high | 修改 Homebrew tap 状态，可能拉取外部仓库。 |
| `brew install mano-cua` | high | 安装软件、依赖和可能的脚本。 |
| `mano-cua check` | high | 可能触发环境探测、权限提示或安装建议。 |
| `mano-cua install-sdk` | high | 下载和安装 SDK。 |
| `mano-cua install-model` | high | 下载模型，涉及体积、license、缓存路径。 |
| `mano-cua run ...` | critical | 可能截图、外发、推理、点击、输入或控制 GUI。 |
| `clawhub install mano-cua` | high | 修改 agent skill 环境。 |

## 4. Homebrew 元数据查询闸门

在用户明确确认前，不执行任何 Homebrew 命令。

若用户确认“只查 Homebrew 元数据”，执行前必须逐项确认：

- 精确命令列表。
- 是否允许联网。
- 是否允许 Homebrew auto-update。
- 是否允许写入 Homebrew 缓存。
- 是否允许读取 tap/formula/package 元数据。
- 输出是否允许写入行动记忆摘要。
- 禁止安装、tap、下载、运行、权限弹窗、GUI 操作。

建议最低风险命令白名单：

```text
brew --version
brew info mano-cua
brew search mano-cua
brew tap-info Mininglamp-AI/tap
```

仍需安全部复核：

- 是否需要设置 Homebrew 环境变量避免 auto-update。
- 是否需要把输出只做摘要，不保存完整日志。
- 是否可能暴露本机路径。

## 5. 隔离路径和 `.gitignore`

若后续需要隔离目录，优先方案：

```text
/private/tmp/esmee-mano-p-stage1/
```

原因：

- 临时目录不进入仓库。
- 适合只读或短时验证。
- 减少把外部内容误提交的风险。

若必须保留工作目录，备选：

```text
/Users/peipei/Documents/esmee AI/.external/mano-p-stage1/
```

进入该路径前必须先确认 `.gitignore` 包含：

```gitignore
.external/
```

禁止提交：

- clone 内容。
- Homebrew metadata dump。
- SDK。
- model。
- screenshots。
- logs。
- caches。
- virtualenv。
- binary。
- generated skill。

## 6. 执行记录模板

若未来用户确认执行某个低风险命令，每一步必须写入行动记忆：

```text
command:
risk_level:
user_confirmation:
expected_side_effects:
network_expected:
cache_write_expected:
permission_prompt_expected:
actual_result_summary:
new_files_or_cache:
stop_condition_hit:
next_step:
```

不得把完整敏感输出、完整路径列表、账号信息、设备序列号、截图、token、SSH key、隐私文档内容写入远端提交。

## 7. 立即停止条件

出现以下任一情况，立即停止并写行动记忆：

- 命令尝试安装、下载、tap、运行 GUI、请求权限或打开应用。
- 出现 Screen Recording、Accessibility、Automation、Full Disk Access、Files and Folders、Browser automation 权限提示。
- 出现 cloud mode、截图上传、任务描述外发、窗口标题外发、路径外发。
- 出现真实账号、付款、上传、删除、提交表单、发送消息、系统设置修改。
- 出现 `.obsidian/`、浏览器密码、SSH key、token、GitHub 设置、隐私文档。
- 任何命令输出无法判断是否安全。

## 8. 清理和回退草案

本节只是草案，不授权执行清理命令。

若未来仅查询元数据：

- 记录是否写入 Homebrew 缓存。
- 记录是否触发 auto-update。
- 不删除 Homebrew 全局缓存，除非用户单独确认。

若未来允许 `brew tap`：

- 需要记录 tap 名称和 tap 路径。
- 清理候选必须单独确认，例如 `brew untap Mininglamp-AI/tap`。

若未来允许安装：

- 需要记录 formula 名称、版本、依赖列表、安装路径。
- 清理候选必须单独确认，例如 `brew uninstall mano-cua`。
- 需要检查是否有 launch agent、PATH 改动、后台服务或权限授权。

若未来允许模型或 SDK：

- 需要记录下载源、大小、hash、license、缓存路径。
- 删除模型/SDK 前必须明确路径，不允许模糊删除。

## 9. 用户确认包

进入任何命令层前，请用户确认以下最小范围之一。

### Option A: 继续只写文档

允许：

- 继续完善计划、清单、模板和安全边界。

禁止：

- 所有命令执行。

### Option B: 只查本机和 Homebrew 元数据

允许候选：

- `sw_vers`
- `uname -m`
- `sysctl -n machdep.cpu.brand_string`
- `brew --version`
- `brew info mano-cua`
- `brew search mano-cua`
- `brew tap-info Mininglamp-AI/tap`

仍禁止：

- `system_profiler SPHardwareDataType`，除非用户接受可能出现设备标识。
- `brew tap`
- `brew install`
- `mano-cua check`
- `mano-cua install-sdk`
- `mano-cua install-model`
- `mano-cua run`
- `clawhub install`
- SDK/model/binary/skill 下载。
- 权限授权。
- GUI 自动化。

### Option C: 进入安装专项评估

当前不建议。若用户坚持，必须先让工程部和安全部再审一次完整命令列表、依赖清单、日志路径和回退方案。

## 10. 当前推荐

推荐下一步：

```text
复审 help-only execution confirmation package。
```

在用户确认前，继续保持：

```text
no tap
no install
no run
no model
no permissions
no GUI automation
no cloud mode
```
