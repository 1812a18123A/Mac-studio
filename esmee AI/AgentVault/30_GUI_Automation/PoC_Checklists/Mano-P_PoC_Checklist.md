---
type: gui_poc_checklist
project_id: mano-p
date: 2026-06-17
owner_department: GUI 自动化部
status: draft
risk_level: medium
current_mode: 乾-坤-坎
source_project:
  - https://github.com/Mininglamp-AI/Mano-P
related_reference:
  - AgentVault/30_GUI_Automation/References/GUI_Reference_Mano-P.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-46_总控办公室_discuss-mano-p-integration.md
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-58_总控办公室_create-mano-p-reference-poc-docs.md
related_reuse_check:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_0_Reuse_Check.md
related_install_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
related_plan_review:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_summary.md
related_execution_checklist:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
---

# Mano-P PoC Checklist

## 1. PoC 目标

验证 Mano-P 是否适合作为 esmee AI 的可选 GUI 自动化后端。

PoC 不验证：

- Mano-P 是否能替代总控办公室。
- Mano-P 是否能绕过安全部和记忆部。
- Mano-P 是否可直接接入生产流程。
- Mano-P 是否可无确认操作真实桌面、账号或外部网站。

## 2. 当前准入状态

- `reference_project`: allowed
- `poc_candidate`: allowed_with_conditions
- `direct_dependency`: not_allowed_yet
- `gui_execution`: requires_user_confirmation
- `cloud_mode`: disabled_by_default

## 3. 必须先完成的检查

### 3.1 许可证

- [ ] 确认主仓库 license 为 Apache-2.0。
- [ ] 确认 README、图片、视频、paper、dataset 是否另有条款。
- [ ] 确认模型权重、SDK、Homebrew tap、OpenClaw/Claude Code skill 是否另有 license。
- [ ] 如后续分发或修改，记录 attribution、notice 和修改说明。

### 3.2 供应链

- [ ] 列出安装入口：Homebrew、SDK、Python 包、binary、model weights、skills。
- [ ] 不执行安装脚本，直到用户确认。
- [ ] 不下载模型或权重，直到用户确认来源、大小、license、hash 和存放路径。
- [ ] 记录所有外部网络访问。
- [ ] 若有 binary 或加速库，记录来源和版本。

### 3.3 硬件与系统

- [ ] 确认本机芯片、内存和 macOS 版本是否满足官方说明。
- [ ] 确认是否需要计算棒或额外硬件。
- [ ] 确认是否需要 macOS Screen Recording 权限。
- [ ] 确认是否需要 macOS Accessibility 权限。
- [ ] 不授予权限，直到用户确认。

### 3.4 数据和隐私

- [ ] 默认禁止 cloud mode。
- [ ] 确认截图、任务描述、窗口标题、剪贴板、文件路径是否会外发。
- [ ] 禁止读取真实账号页面、付款页面、隐私文档、聊天记录、密钥和浏览器密码。
- [ ] PoC 日志和截图默认保存在本地，不提交、不 push。
- [ ] 如需保留截图，先确认保存路径和脱敏方式。

## 4. 允许的 PoC 阶段

### Stage 0: 只读研究

允许：

- [x] 读取 README、LICENSE、安装说明、examples、issues。
- [x] 写复用检查报告。
- [ ] 写风险边界和最小 adapter 草案。

禁止：

- [ ] 克隆仓库。
- [ ] 安装依赖。
- [ ] 运行命令。
- [ ] 下载模型或 SDK。
- [ ] 启动 GUI 自动化。

通过标准：

- [x] 明确可运行入口。
- [x] 明确 local/cloud 模式差异。
- [ ] 明确依赖和硬件要求。
- [ ] 明确 license 和 attribution 风险。

Stage 0 结果：

- `passed_with_conditions`
- 复用检查报告：`AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_0_Reuse_Check.md`
- 下一步只允许写 Stage 1 计划；不允许直接克隆、安装、运行或 GUI 自动化。

### Stage 1: 隔离安装验证

当前状态：

- `waiting_user_confirmation_for_metadata_query`
- 计划文件：`AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md`
- 执行清单：`AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md`
- 已完成安装计划和执行清单；未克隆、未安装、未运行、未下载模型、未授予权限。
- 工程部和安全部均已只读审查，结论为 `approved_with_notes`。
- 进入命令层前必须由用户明确确认是否允许 Option B：只查本机和 Homebrew 元数据。

进入条件：

- [ ] 用户明确确认允许克隆或下载。
- [ ] 用户明确确认允许安装哪些依赖。
- [ ] 安全部批准安装边界。
- [ ] 工程部指定隔离目录或临时环境。

允许：

- [ ] 克隆到隔离目录。
- [ ] 安装最小依赖。
- [ ] 查看 CLI help 或 dry-run。

禁止：

- [ ] 写入主仓库依赖树。
- [ ] 操作真实账号或私密资料。
- [ ] 启动自动点击或输入。
- [ ] 默认启用 cloud mode。

通过标准：

- [ ] 安装步骤可复现。
- [ ] 依赖清单可记录。
- [ ] 无未确认外发。
- [ ] 可卸载或清理。

### Stage 2: 沙盒 GUI 观察

进入条件：

- [ ] 用户确认允许屏幕观察。
- [ ] 安全部确认截图和日志边界。
- [ ] GUI 自动化部指定目标测试窗口。

允许：

- [ ] 使用本地静态 HTML 测试页或沙盒窗口。
- [ ] 观察界面并生成拟执行动作。
- [ ] 将观察、计划、风险写入行动记忆。

禁止：

- [ ] 自动点击。
- [ ] 输入真实信息。
- [ ] 访问账号页面。
- [ ] 操作 Obsidian `.obsidian/`、GitHub 设置、付款、上传或删除。

通过标准：

- [ ] 能识别目标元素。
- [ ] 能输出动作理由和停止条件。
- [ ] 能在不点击的情况下完成 verify 计划。

### Stage 3: 一次可回退动作

进入条件：

- [ ] 用户再次确认允许一个动作。
- [ ] 动作为低风险、可回退、可验证。
- [ ] 已写行动记忆。

允许：

- [ ] 点击本地测试按钮。
- [ ] 在沙盒输入框输入无敏感测试文本。

禁止：

- [ ] 发送消息。
- [ ] 提交表单。
- [ ] 上传文件。
- [ ] 删除、移动、覆盖文件。
- [ ] 修改系统、浏览器、GitHub 或 Obsidian 设置。

通过标准：

- [ ] 动作执行后状态变化可验证。
- [ ] 结果写回行动记忆。
- [ ] 失败时停止，不连续点击。

## 5. 停止条件

发现以下任一情况，立即停止：

- 需要登录、付款、上传、提交表单或发送消息。
- 出现隐私文档、聊天记录、密钥、token、浏览器密码或账号设置。
- 模式会外发截图、任务描述或本地路径，且未获确认。
- GUI 坐标、目标元素或动作意图不确定。
- 任务请求删除、覆盖、批量移动或修改系统设置。
- 工具要求高权限、辅助功能、屏幕录制或网络访问，且未获确认。

## 6. 最小 adapter 候选接口

如果 PoC 通过，后续 adapter 只应暴露最小接口：

输入：

- `task_goal`
- `allowed_apps`
- `forbidden_actions`
- `stop_conditions`
- `action_memory_path`
- `mode`: `observe_only` / `propose_action` / `execute_one_confirmed_action`

输出：

- `observation`
- `proposed_action`
- `risk_check`
- `execution_result`
- `verification_result`
- `needs_confirmation`
- `failure_reason`

默认行为：

- 不确定就返回 `needs_confirmation`。
- 高风险动作不执行。
- 每一步都写行动记忆。

## 7. 成功标准

PoC 成功需要同时满足：

- [ ] local mode 可控，或 cloud mode 被明确禁用。
- [ ] 权限边界清晰。
- [ ] 依赖和许可证可审计。
- [ ] 能完成低风险沙盒任务。
- [ ] 能记录 observe / act / verify。
- [ ] 失败时能停止。
- [ ] 可作为可替换 provider，不绑定主系统。

## 8. 决策出口

PoC 完成后只能进入以下之一：

- `reference_only`: 保留参考文档，不接入。
- `adapter_candidate`: 写最小 adapter 设计，不运行真实桌面。
- `sandbox_provider`: 仅允许沙盒 GUI 自动化。
- `blocked`: 因许可证、供应链、隐私、权限或稳定性阻断。

禁止直接进入：

- `production_dependency`
- `unattended_desktop_control`
- `cloud_mode_default`
