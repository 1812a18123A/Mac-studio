---
type: gui_install_plan
project_id: mano-p
date: 2026-06-17
owner_department: GUI 自动化部
status: waiting_user_confirmation
risk_level: medium
current_mode: 乾-坎-艮
source_project:
  - https://github.com/Mininglamp-AI/Mano-P
source_readme:
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/README.md
source_license:
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/LICENSE
related_reuse_check:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_0_Reuse_Check.md
related_checklist:
  - AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
related_plan_review:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_summary.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_engineering_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_safety_result.md
related_execution_checklist:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
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
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_19-50_gui-自动化部_mano-p-stage-1-install-plan.md
notify_departments:
  - GUI 自动化部
  - 工程部
  - 安全部
  - 记忆部
requires_user_confirmation: true
---

# Mano-P Stage 1 Isolated Install Plan

## 1. 计划结论

本文件只是 Stage 1 隔离安装计划，不是执行授权。

部门审查结果：

- 工程部：`approved_with_notes`
- 安全部：`approved_with_notes`
- 总控结论：Stage 1 执行清单和用户确认包已补；Option B 元数据查询、formula/dependency 审查、Python source 审查、runtime gate plan 和部门复审均已完成。安全部与工程部均为 `approved_with_notes`，允许准备 help-only runtime 候选包，但仍不允许执行。

当前状态：

- `stage_1_status`: runtime_gate_review_completed_waiting_help_only_candidate_package_confirmation
- `clone_allowed`: no
- `install_allowed`: no
- `model_download_allowed`: no
- `permission_grant_allowed`: no
- `gui_execution_allowed`: no
- `cloud_mode_allowed`: no

进入任何真实执行前，必须由用户明确确认，并由安全部、工程部、GUI 自动化部复核边界。

## 2. 官方入口摘要

官方 README 显示 Mano-P 相关使用形态主要包括：

- `mano-cua` CLI：面向人类用户和脚本调用。
- `mano-skill`：面向 Claude Code、OpenClaw 等 agent 的 skill 形态。
- Homebrew tap：`Mininglamp-AI/tap`。
- local mode：需要 `--local`，并需要环境检查、SDK 安装和模型安装。
- cloud mode：默认模式，会把截图和任务描述发往云端视觉模型服务。
- common permissions：Screen Recording 和 Accessibility。

esmee AI 当前只计划评估 `mano-cua` CLI 的隔离安装路径，不评估 `mano-skill` 的自动 agent 接入。

## 3. Stage 1 目标

Stage 1 只验证隔离安装是否可审计、可回退、可复现。

允许目标：

- 明确安装入口和依赖来源。
- 明确安装目录和缓存目录。
- 明确是否会触发网络访问。
- 明确是否需要系统权限。
- 明确如何卸载或清理。
- 只查看 `help`、`version` 或 dry-run 类低风险输出。

不允许目标：

- 不运行 GUI 任务。
- 不截图。
- 不点击、不输入、不打开真实 App。
- 不下载模型，除非用户单独确认。
- 不授予 Screen Recording 或 Accessibility 权限，除非用户单独确认。
- 不启用 cloud mode。
- 不把 Mano-P 写入 esmee AI 主仓库依赖树。

## 4. 隔离位置

建议隔离目录：

```text
/Users/peipei/Documents/esmee AI/.external/mano-p-stage1/
```

该目录应加入 `.gitignore`，并且不得提交任何下载内容、日志、截图、缓存、模型或虚拟环境。

备选临时目录：

```text
/private/tmp/esmee-mano-p-stage1/
```

优先级：

1. 若只读检查和命令 help 可完成，优先用临时目录。
2. 若需要保留审计清单，使用 `.external/mano-p-stage1/`，但只提交计划文档，不提交外部内容。

## 5. 可能命令清单

以下命令是计划候选，不代表已经允许执行。

只读环境检查候选：

```bash
sw_vers
uname -m
sysctl -n machdep.cpu.brand_string
system_profiler SPHardwareDataType
```

Homebrew 信息候选：

```bash
brew info mano-cua
brew search mano-cua
brew tap-info Mininglamp-AI/tap
```

禁止在未确认前执行：

```bash
brew tap Mininglamp-AI/tap
brew install mano-cua
mano-cua check
mano-cua install-sdk
mano-cua install-model
mano-cua run ...
clawhub install mano-cua
```

原因：

- `brew tap` 和 `brew install` 会修改本机 Homebrew 状态。
- `mano-cua check` 可能触发环境探测或安装建议。
- `install-sdk` / `install-model` 会下载外部组件。
- `mano-cua run` 会触发截图、推理和 GUI 控制风险。
- `clawhub install` 会修改 agent skill 环境。

## 6. 权限边界

Stage 1 默认不授予：

- Screen Recording
- Accessibility
- Automation
- Full Disk Access
- Files and Folders
- Browser automation permissions

若未来需要权限，必须先写清楚：

- 权限名称。
- 哪个可执行文件请求权限。
- 为什么需要。
- 可否只在沙盒窗口测试。
- 如何撤销权限。
- 权限截图或日志是否保存，以及是否脱敏。

## 7. 网络和数据边界

默认禁止：

- cloud mode。
- 上传截图、任务描述、窗口标题、文件路径或日志。
- 访问真实账号页面、付款页面、聊天窗口或隐私文档。
- 读取 `.obsidian/`、浏览器密码、SSH key、token、GitHub 设置。

如果后续只做 Homebrew 元数据查询，必须记录：

- 请求目标。
- 是否下载 formula。
- 是否写入 tap。
- 是否安装二进制或 Python 虚拟环境。

如果后续下载模型，必须单独确认：

- 下载平台。
- 模型名称。
- 预计大小。
- license。
- hash 或校验方式。
- 存放路径。
- 清理方式。

## 8. 供应链检查清单

进入安装前，工程部需要补全：

- Homebrew formula 来源。
- tap 仓库 license。
- `mano-cua` 包 license。
- Python 依赖清单。
- Tkinter 或 GUI 库依赖。
- SDK 来源与 license。
- 模型来源与 license。
- 是否有 pre/post install 脚本。
- 是否写入 PATH。
- 是否启动后台服务。
- 是否创建 launch agent。

当前判断：

- 主 Mano-P 仓库 Apache-2.0 不能自动覆盖 Homebrew tap、SDK、模型、ClawHub skill 或外部服务。
- 任何 vendor、submodule 或生产依赖都必须另做许可证审计。

## 9. 安全部确认点

安全部需要确认：

- cloud mode 是否保持禁用。
- 是否允许任何截图。
- 是否允许任何 GUI 权限申请。
- 是否允许读取当前屏幕。
- 是否允许工具控制鼠标键盘。
- 是否允许访问浏览器窗口。
- 是否允许写入本地日志。
- 日志、缓存和模型输出是否需要脱敏。

默认答案全部为 no，直到用户确认。

## 10. GUI 自动化部测试边界

即便 Stage 1 安装成功，也不能直接进入真实 GUI 操作。

Stage 2 之前只能规划：

- 本地静态 HTML 测试页。
- 无账号、无网络、无隐私内容。
- 第一轮 observe-only。
- 第二轮 propose-action。
- 只有用户再次确认后才允许一次可回退动作。

禁止场景：

- WeChat、邮件、GitHub 设置、Obsidian 私有配置、付款、上传、删除、提交表单、发送消息。
- 系统设置修改。
- 浏览器登录态页面。
- 多显示器场景。

## 11. 清理和回退

若后续用户允许进入 Stage 1，必须在执行前写清理方案：

- 卸载 Homebrew 包。
- 移除 tap。
- 删除隔离目录。
- 删除模型缓存。
- 删除 SDK 缓存。
- 撤销 Screen Recording / Accessibility 权限。
- 确认没有 launch agent、后台服务或 PATH 残留。

禁止使用破坏性清理命令，除非用户明确确认路径和范围。

## 12. 阶段出口

Stage 1 计划完成后的出口只能是：

- `wait_user_confirmation`: 等待用户确认是否允许克隆或安装。
- `needs_engineering_review`: 工程部补依赖和供应链清单。
- `needs_safety_review`: 安全部补权限和外发边界。
- `blocked`: 许可证、供应链、权限或外发风险不可接受。

当前出口：

```text
wait_user_confirmation
```

## 13. 给用户的确认包

若用户要进入真实 Stage 1，必须确认以下事项：

1. 是否允许查询 Homebrew tap 元数据。
2. 是否允许 `brew tap Mininglamp-AI/tap`。
3. 是否允许 `brew install mano-cua`。
4. 是否允许运行 `mano-cua --help` 或等价只读命令。
5. 是否禁止 cloud mode。
6. 是否禁止模型下载，直到单独确认。
7. 是否禁止 Screen Recording / Accessibility 授权，直到单独确认。

推荐默认确认范围：

```text
只允许查询元数据和写 Stage 1 执行计划；暂不允许 tap/install/run/model/permissions/gui。
```

## 14. 部门审查后新增前置项

在进入任何命令层之前，必须先新增：

```text
AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
```

该清单至少包含：

- Homebrew 元数据查询命令白名单。
- 每条命令是否联网、是否写缓存、是否触发 auto-update。
- 命令风险分级：只读、会写状态、会下载、会请求权限、会 GUI 执行。
- `.external/` 隔离目录的 `.gitignore` 方案。
- Homebrew/tap/formula/package/Python/SDK/model/license 检查项。
- 缓存、日志、模型输出和截图的默认不提交规则。
- 清理与回退草案，且不得使用模糊或破坏性删除命令。
- 用户确认包和立即停止条件。

当前状态：

- 执行清单已创建。
- Option B 元数据查询已完成。
- 未执行 `brew tap`、`brew install`、`mano-cua`、`clawhub`、下载、权限授权或 GUI 自动化。
- 未授权任何安装、下载、权限或 GUI 自动化。
- 下一步等待用户确认是否允许只读审查 Homebrew formula 内容和依赖树。
