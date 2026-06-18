---
type: action_memory
date: 2026-06-17
time: "19:50"
department: GUI 自动化部
task_id: mano-p-stage-1-install-plan
status: completed
risk_level: medium
current_mode: 坤-兑
related_skills:
  - obsidian-memory
related_plugins:
  - none
related_files:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
  - AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_0_Reuse_Check.md
notify_departments:
  - GUI 自动化部
  - 工程部
  - 安全部
  - 记忆部
requires_user_confirmation: false
---

# 行动记忆：Mano-P Stage 1 隔离安装计划

## 1. 用户目标

用户想要什么：
- 用户要求继续推进项目；基于 Stage 0 结论，写 Mano-P Stage 1 隔离安装计划。

## 2. 本次行动目标

这一次只做什么：
- 本次只写 Stage 1 计划和检查闸门：不克隆、不安装、不运行、不下载模型、不授予权限、不启动 GUI 自动化。

## 3. 当前上下文

已知信息：
- Stage 0 复用检查已完成并推送，结论为 `passed_with_conditions`。
- 官方 README 显示 `mano-cua` 可通过 Homebrew tap 安装；cloud mode 是默认模式；local mode 需要 `--local`、SDK 和模型安装。
- 官方 README 还说明 Screen Recording 和 Accessibility 是通用权限要求，并提到当前只支持主显示器。
- 本轮只写 Stage 1 计划，不执行任何安装或 GUI 操作。

未知信息：
- 用户是否允许进入真实 Stage 1：查询 tap、tap/install、运行 help、下载 SDK/model、授予权限都需要后续明确确认。
- Homebrew tap、SDK、模型、ClawHub skill 的完整依赖和许可证仍待工程/安全复核。

## 4. 涉及资料

需要读取或参考的资料：
  - https://github.com/Mininglamp-AI/Mano-P
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/README.md
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/LICENSE
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_0_Reuse_Check.md
  - AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md

禁止使用或不能外发的资料：
  - 屏幕截图、任务描述、账号页面、付款页面、私密 Obsidian 配置、GitHub 设置、token、SSH key、浏览器密码。

## 5. 需要修改什么

计划修改的文件、配置、skill、插件、脚本：
  - 新增 Mano-P Stage 1 隔离安装计划。
  - 更新 Mano-P PoC checklist，挂接 Stage 1 计划并保持执行需确认。

## 6. 不能做什么

本次明确禁止：
- 不删除文件，除非用户明确确认
- 不发送邮件、消息、付款、提交表单，除非用户明确确认
- 不上传截图、音频、记忆文件到外部服务，除非用户明确确认
- 不覆盖已有 skill，除非先备份
- 不跳过 Obsidian 行动记录
- 不克隆 Mano-P
- 不执行 `brew tap` 或 `brew install`
- 不运行 `mano-cua`
- 不运行 `clawhub install`
- 不下载 SDK 或模型
- 不授予 Screen Recording / Accessibility 权限
- 不启用 cloud mode
- 不启动 GUI 自动化

## 7. 需要调用的 skill

本次需要：
  - obsidian-memory：记录 Stage 1 计划、确认闸门和执行边界。

## 8. 需要使用的 Codex App 插件功能

本次需要：
  - none

## 9. 行动步骤

- [x] Step 1: 记录行动记忆。
- [x] Step 2: 只读核对官方 README 当前安装和权限说明。
- [x] Step 3: 新增 Stage 1 隔离安装计划。
- [x] Step 4: 更新 PoC checklist 的 Stage 1 计划状态。
- [x] Step 5: 验证并准备选择性提交本轮文档。

## 10. 风险检查

风险：
- 中：Stage 1 涉及未来可能执行的安装、模型下载、系统权限、cloud/local mode 和 GUI 自动化入口。

缓解措施：
- 本轮只写计划，不执行安装。
- 把所有真实执行动作列为 requires confirmation。
- 明确 cloud mode 默认禁止，权限默认不授予。
- 提交前检查 thread id、密钥模式和未完成状态。

## 11. 部门通知

需要通知哪个部门：
  - GUI 自动化部
  - 工程部
  - 安全部
  - 记忆部

通知原因：
- GUI 自动化部：维护 Stage 1 计划和 GUI 测试边界。
- 工程部：后续审查 Homebrew、SDK、模型和依赖链。
- 安全部：后续审查 cloud mode、截图、系统权限和数据外发。
- 记忆部：归档计划和后续确认包。

## 12. 执行结果

实际做了什么：
- 已创建行动记忆。
- 已只读核对官方 README 当前安装入口、local/cloud mode、权限要求和模型/SDK入口。
- 已新增 Stage 1 隔离安装计划。
- 已更新 PoC checklist，标注 Stage 1 计划完成但执行仍需用户确认。

成功：
- Stage 1 计划已明确不允许直接克隆、安装、运行、下载模型、授予权限或 GUI 自动化。

失败：
- 未发现本轮文档写入阻断项。

## 13. 产生的新资料

新增文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_19-50_gui-自动化部_mano-p-stage-1-install-plan.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md

更新文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_19-50_gui-自动化部_mano-p-stage-1-install-plan.md

截图/日志/轨迹：
- 只读 web 核对官方 GitHub/README/LICENSE。
- 本地读取 Stage 0 报告和 PoC checklist。

## 14. 下一步

下一步建议：
- 选择性提交并推送本轮计划；下一步可选择让工程部/安全部审查计划，或等待用户确认是否允许真实 Stage 1 元数据查询。

## 15. 给用户的简短汇报

用简短中文告诉用户：
- 已完成 Mano-P Stage 1 隔离安装计划；现在仍不允许克隆、安装、运行或 GUI 自动化，下一步需要用户确认执行边界。

## Log 2026-06-17 19:52

- Stage 1 隔离安装计划已完成：新增计划文档，更新 PoC checklist；本轮未克隆、未安装、未运行、未下载模型、未授予权限、未启动 GUI 自动化。提交前检查未发现真实 thread id 或严格密钥/token 模式。
