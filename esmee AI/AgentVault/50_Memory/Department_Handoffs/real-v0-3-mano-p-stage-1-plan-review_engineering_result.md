---
type: department_handoff_result
task_id: real-v0-3-mano-p-stage-1-plan-review
department: 工程部
status: approved_with_notes
created_at: 2026-06-17
source_handoff: AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_engineering.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_19-56_工程部_real-v0-3-mano-p-stage-1-plan-review.md
related_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
related_checklist:
  - AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
---

# 工程部结果：Mano-P Stage 1 计划只读审查

## 结论

status: `approved_with_notes`

工程部认可当前 Stage 1 隔离安装计划可以作为进入用户确认前的工程计划。计划已经明确区分了只读检查、会修改系统状态的命令、会下载的命令、GUI/权限风险和 cloud mode 风险；也明确禁止克隆、安装、模型下载、权限授予和 GUI 执行，符合当前只读审查边界。

该结论不等于允许执行安装。进入任何真实执行前，仍必须补齐下列工程项，并获得用户和安全部确认。

## 已读取资料

- `AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-stage-1-plan-review_engineering.md`
- `AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md`
- `AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md`

## 必须补充项

- 补充 Homebrew tap / formula / package 的只读元数据检查清单：来源、license、版本、formula 内容、是否有 pre/post install、是否创建后台服务或 launch agent。
- 补充 `.external/` 隔离目录的 `.gitignore` 规则方案；若使用 `/private/tmp/`，说明哪些审计记录需要保存在 AgentVault 文档中。
- 补充 Stage 1 执行前命令分级表：只读命令、会写 Homebrew 状态的命令、会下载的命令、会请求权限的命令、会运行 GUI 的命令。
- 补充清理和回退的具体命令草案，但在用户确认前不得执行；清理范围必须是明确路径，不能使用模糊或破坏性删除。
- 补充 Homebrew 缓存、SDK 缓存、模型缓存、日志路径的预期位置和检查方式。
- 补充 PoC 证据记录格式：每一步记录命令类别、预期副作用、实际输出摘要、是否产生文件、是否触发网络或权限提示。
- 补充失败停止规则：任何命令出现安装、下载、权限弹窗、外发、GUI 控制、账号页面或隐私内容时立即停止并写行动记忆。

## 最低风险下一步

最低风险下一步不是安装，也不是 tap。

建议 GUI 自动化部、安全部和工程部先补一份 Stage 1 执行清单，只列候选命令、风险分类、预期副作用、用户确认项和回退路径。完成后再由用户确认是否允许进入“只读 Homebrew 元数据查询”。

在用户确认前，工程部建议最多继续做本地文档级准备：

- 完成命令分级表。
- 完成 `.gitignore` 方案草案。
- 完成清理和回退草案。
- 完成 Stage 1 执行记录模板。

## 禁止动作

- 不克隆 Mano-P。
- 不执行 `brew tap`。
- 不执行 `brew install`。
- 不运行 `mano-cua`、`mano-cua check`、`mano-cua install-sdk`、`mano-cua install-model` 或 `mano-cua run`。
- 不执行 `clawhub install`。
- 不下载 SDK、模型、依赖或二进制。
- 不授予 Screen Recording、Accessibility、Automation、Full Disk Access、Files and Folders 或浏览器自动化权限。
- 不启用 cloud mode。
- 不截图、不点击、不输入、不打开真实 App。
- 不读取 `.obsidian/`、浏览器密码、SSH key、token、GitHub 设置或隐私文档。
- 不提交、不 push。
- 不写真实 thread id。

## 工程维护判断

计划已经具备“可审计、可回退、可复现”的骨架，但执行前需要把供应链和回退细节从原则补成清单。只要按上述补充项推进，Stage 1 可以保持为低扩散、低耦合、可停止的隔离验证，不会把 Mano-P 引入 esmee AI 主仓库依赖树。
