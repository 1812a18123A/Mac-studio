---
type: action_memory
date: 2026-06-17
time: "21:55"
department: GUI-自动化部
task_id: mano-p-runtime-gate-plan
status: completed
risk_level: high
current_mode: 坤-坎-兑
related_skills:
  - obsidian-memory
related_plugins:
  - none
related_files:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Formula_Dependency_Review.md
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
  - AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
notify_departments:
  - GUI 自动化部
  - 安全部
  - 工程部
  - 记忆部
requires_user_confirmation: false
---

# 行动记忆：Mano-P Stage 1 Runtime Gate Plan

## 1. 用户目标

用户想要什么：
- 继续推进 Mano-P Stage 1 下一步，但不直接运行 mano-cua，保持项目稳定和安全边界。

## 2. 本次行动目标

这一次只做什么：
- 本次只编写 runtime gate plan，定义未来运行任何 mano-cua 命令前的环境、权限、命令白名单、禁止事项和停止条件。

## 3. 当前上下文

已知信息：
- 用户确认继续下一步。
- Python source 审查发现默认 `mano-cua run` 使用 cloud mode。
- Runtime 可截图、打开 app/url、执行鼠标键盘动作、使用 bash capability，并受 `$HOME/.mano/config.json` 影响。
- 当前安全结论是不直接运行，先写 runtime gate plan。

未知信息：
- 未来是否允许先执行 `mano-cua --help`。
- 未来是否允许创建 clean HOME 临时目录。
- 未来是否允许任何截图或 GUI 权限。
- 是否需要真实多部门复审 runtime gate plan。

## 4. 涉及资料

需要读取或参考的资料：
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Formula_Dependency_Review.md
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md

禁止使用或不能外发的资料：
  - 本地隐私资料
  - 真实内部 thread id
  - token、SSH key、账号认证信息
  - `$HOME/.mano/config.json` 的配置值
  - 截图、窗口内容、浏览器会话、Obsidian 设置、GitHub 设置

## 5. 需要修改什么

计划修改的文件、配置、skill、插件、脚本：
  - 新增 Mano-P Stage 1 runtime gate plan 文档。
  - 更新 Stage 1 执行清单、安装计划、PoC checklist、Python source review 的状态和下一步。
  - 更新本行动记忆。

## 6. 不能做什么

本次明确禁止：
- 不删除文件，除非用户明确确认
- 不发送邮件、消息、付款、提交表单，除非用户明确确认
- 不上传截图、音频、记忆文件到外部服务，除非用户明确确认
- 不覆盖已有 skill，除非先备份
- 不跳过 Obsidian 行动记录
- 不运行 `mano-cua --help/check/run/config/stop/install-sdk/install-model`
- 不执行 `brew install/tap/update/upgrade/reinstall`
- 不下载 SDK、模型、binary、Python 包或 skill
- 不授权 Screen Recording、Accessibility、Automation、Full Disk Access 等权限
- 不截图、点击、输入、打开 app/url、读取当前 GUI 内容或启用 cloud mode

## 7. 需要调用的 skill

本次需要：
  - obsidian-memory：写入和更新可审计行动记忆。

## 8. 需要使用的 Codex App 插件功能

本次需要：
  - none

## 9. 行动步骤

- [x] Step 1: 记录行动记忆。
- [x] Step 2: 编写 runtime gate plan。
- [x] Step 3: 更新 Stage 1 关联文档。
- [x] Step 4: 扫描敏感信息、提交并推送文档。

## 10. 风险检查

风险：
- 高。计划对象涉及潜在 GUI 自动化、截图、cloud mode、shell capability、剪贴板、鼠标键盘和用户本地配置影响。

缓解措施：
- 本轮只写文档，不运行命令入口。
- 计划默认 `no cloud/no GUI/no screenshot/no bash/no app/url/no clipboard`。
- 提交前扫描 thread id、token、私钥模式。

## 11. 部门通知

需要通知哪个部门：
  - GUI 自动化部
  - 安全部
  - 工程部
  - 记忆部

通知原因：
- GUI 自动化部负责 runtime PoC 路线。
- 安全部负责运行边界、外发和权限控制。
- 工程部负责命令白名单、环境隔离和可回退性。
- 记忆部负责行动记忆和审计归档。

## 12. 执行结果

实际做了什么：
- 新增 Mano-P Stage 1 runtime gate plan。
- 更新 Stage 1 执行清单、安装计划、PoC checklist 和 Python source review 的状态。
- 明确当前 `runtime_allowed: no`，下一步只能部门复审 gate plan 或准备 help-only runtime 候选包。

成功：
- 成功。未运行 `mano-cua`，未安装、下载、授权、截图、点击、输入、打开 app/url 或启用 cloud mode。

失败：
- 无。

## 13. 产生的新资料

新增文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-55_gui-自动化部_mano-p-runtime-gate-plan.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Runtime_Gate_Plan.md

更新文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-55_gui-自动化部_mano-p-runtime-gate-plan.md

截图/日志/轨迹：
- 无截图。未产生 runtime 日志或轨迹。

## 14. 下一步

下一步建议：
- 让安全部/工程部复审 runtime gate plan，或在用户确认后准备 help-only runtime 候选包；仍不直接运行 `mano-cua`。

## 15. 给用户的简短汇报

用简短中文告诉用户：
- 已完成 runtime gate plan。当前仍不允许运行；下一步建议复审 gate plan 或准备 help-only 候选包。

## Log 2026-06-17 21:57

- 完成 runtime gate plan：当前 runtime_allowed=no；下一步仅允许部门复审 gate plan 或准备 help-only runtime 候选包，仍不直接执行 mano-cua。
