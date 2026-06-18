---
type: action_memory
date: 2026-06-17
time: "22:08"
department: GUI-自动化部
task_id: mano-p-help-only-candidate-package
status: completed
risk_level: high
current_mode: 坤-坎-兑
related_skills:
  - obsidian-memory
related_plugins:
  - none
related_files:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-runtime-gate-review_summary.md
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Runtime_Gate_Plan.md
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
notify_departments:
  - GUI 自动化部
  - 安全部
  - 工程部
  - 记忆部
requires_user_confirmation: true
---

# 行动记忆：Mano-P Help-only Runtime 候选包准备

## 1. 用户目标

用户想要什么：
- 继续推进 Mano-P Stage 1 下一步，但仍不执行 mano-cua，先把 help-only runtime 候选包准备完整。

## 2. 本次行动目标

这一次只做什么：
- 本次只准备 help-only runtime 候选包，包含 exact binary、clean HOME、env-i、timeout、expected writes、verification checks、输出脱敏和停止条件。

## 3. 当前上下文

已知信息：
- 安全部和工程部已复审 runtime gate plan，均为 `approved_with_notes`。
- 共同允许准备 help-only runtime 候选包。
- 共同不允许执行 `mano-cua --help`。
- 候选包必须补 exact binary、clean HOME、`env -i`、timeout、expected writes、verification checks、输出脱敏和停止条件。

未知信息：
- 未来用户是否会确认执行 `mano-cua --help`。
- 未来是否需要记忆部复审行动记忆模板。
- 当前 wrapper 路径元数据是否能只读确认，不执行 wrapper。

## 4. 涉及资料

需要读取或参考的资料：
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-runtime-gate-review_summary.md
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Runtime_Gate_Plan.md
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md
  - `/opt/homebrew/bin/mano-cua` wrapper path metadata, read-only only.

禁止使用或不能外发的资料：
  - 本地隐私资料
  - 真实内部 thread id
  - token、SSH key、账号认证信息
  - `$HOME/.mano/config.json` 的配置值
  - 完整敏感 stdout/stderr、截图、窗口内容、设备标识

## 5. 需要修改什么

计划修改的文件、配置、skill、插件、脚本：
  - 新增 help-only runtime 候选包文档。
  - 更新 runtime gate plan、执行清单、安装计划和 PoC checklist 状态。
  - 更新本行动记忆。

## 6. 不能做什么

本次明确禁止：
- 不删除文件，除非用户明确确认
- 不发送邮件、消息、付款、提交表单，除非用户明确确认
- 不上传截图、音频、记忆文件到外部服务，除非用户明确确认
- 不覆盖已有 skill，除非先备份
- 不跳过 Obsidian 行动记录
- 不执行 `/opt/homebrew/bin/mano-cua` 或 `mano-cua --help`
- 不执行 `mano-cua run/check/config/stop/install-sdk/install-model/--local`
- 不执行 Homebrew install/tap/update/upgrade/reinstall
- 不创建 clean HOME、不运行候选命令、不授权权限
- 不截图、点击、输入、打开 app/url、读取 GUI、启用 cloud/local mode
- 不读取或记录真实 `$HOME/.mano/config.json` 配置值

## 7. 需要调用的 skill

本次需要：
  - obsidian-memory：写入行动记忆和候选包审计记录。

## 8. 需要使用的 Codex App 插件功能

本次需要：
  - none

## 9. 行动步骤

- [x] Step 1: 记录行动记忆。
- [x] Step 2: 只读验证 wrapper 路径元数据，不执行 wrapper。
- [x] Step 3: 编写 help-only runtime 候选包。
- [x] Step 4: 更新 Stage 1 状态文档。
- [x] Step 5: 扫描敏感信息、提交并推送。

## 10. 风险检查

风险：
- 高。候选包面向未来 runtime，涉及 cloud、GUI、截图、权限、shell、配置值和环境变量泄露风险。

缓解措施：
- 本轮只做只读元数据验证和文档写入。
- 候选包明确“不授权执行”。
- 提交前扫描 thread id、token、私钥模式。

## 11. 部门通知

需要通知哪个部门：
  - GUI 自动化部
  - 安全部
  - 工程部
  - 记忆部

通知原因：
- GUI 自动化部负责候选包路线。
- 安全部和工程部已批准准备候选包但禁止执行。
- 记忆部负责行动记忆模板和审计归档。

## 12. 执行结果

实际做了什么：
- 只读验证 `/opt/homebrew/bin/mano-cua` 是 Homebrew symlink，目标为 `../Cellar/mano-cua/1.1.4/bin/mano-cua`。
- 只读查看 wrapper 文本摘要，确认它会读取 `$HOME/.mano/config.json`，因此 clean HOME 必须保留为强制条件。
- 新增 help-only runtime 候选包文档。
- 更新 runtime gate plan、执行清单、安装计划和 PoC checklist 状态。

成功：
- 成功。未执行 `/opt/homebrew/bin/mano-cua`，未运行 `mano-cua --help`，未安装、下载、授权、截图、点击、输入、打开 app/url 或启用 cloud/local mode。

失败：
- 无。

## 13. 产生的新资料

新增文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_22-08_gui-自动化部_mano-p-help-only-candidate-package.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Help_Only_Runtime_Candidate_Package.md

更新文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Runtime_Gate_Plan.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_22-08_gui-自动化部_mano-p-help-only-candidate-package.md

截图/日志/轨迹：
- 无截图。未产生 runtime 日志或轨迹。

## 14. 下一步

下一步建议：
- 让安全部、工程部、记忆部复审 help-only runtime 候选包；仍不执行 `mano-cua --help`。

## 15. 给用户的简短汇报

用简短中文告诉用户：
- 已完成 help-only runtime 候选包。下一步建议三部门复审候选包；当前仍不允许运行。

## Log 2026-06-17 22:12

- 完成 help-only runtime 候选包：只读验证 wrapper 路径元数据并写入候选包；未执行 mano-cua；下一步建议三部门复审候选包。
