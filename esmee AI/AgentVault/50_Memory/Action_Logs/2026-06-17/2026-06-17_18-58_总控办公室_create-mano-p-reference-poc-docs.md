---
type: action_memory
date: 2026-06-17
time: "18:58"
department: 总控办公室
task_id: create-mano-p-reference-poc-docs
status: completed
risk_level: medium
current_mode: 坤-兑
related_skills:
  - obsidian-memory
related_plugins:
  - none
related_files:
  - AgentVault/30_GUI_Automation/References/GUI_Reference_Mano-P.md
  - AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_summary.md
notify_departments:
  - GUI 自动化部
  - 工程部
  - 安全部
  - 技能优化部
  - 记忆部
requires_user_confirmation: false
---

# 行动记忆：创建 Mano-P 参考文档和 PoC 清单

## 1. 用户目标

用户想要什么：
- 用户确认执行建议：创建 GUI_Reference_Mano-P.md 和 Mano-P_PoC_Checklist.md。

## 2. 本次行动目标

这一次只做什么：
- 本次只固化 Mano-P 参考文档和 PoC checklist；不克隆、不安装、不下载模型、不启用 GUI 自动化、不提交不 push。

## 3. 当前上下文

已知信息：
- 五部门已讨论 Mano-P 接入方式，结论是：进入 GUI 路线，先参考文档和受控 PoC checklist，不直接并入主系统。
- Mano-P 官方仓库标注 Apache-2.0，README 描述 GUI-VLA、本地/边缘推理、长任务 GUI 自动化、Local/Cloud 模式等方向。
- 本轮只创建文档，不执行任何安装或 GUI 操作。

未知信息：
- Mano-P 的可运行入口、模型权重、SDK、Homebrew tap、skill 和第三方依赖仍需后续 PoC 前置检查。

## 4. 涉及资料

需要读取或参考的资料：
  - https://github.com/Mininglamp-AI/Mano-P
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/README.md
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/LICENSE
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_summary.md

禁止使用或不能外发的资料：
  - 本地隐私资料

## 5. 需要修改什么

计划修改的文件、配置、skill、插件、脚本：
  - 新增 AgentVault/30_GUI_Automation/References/GUI_Reference_Mano-P.md
  - 新增 AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
  - 更新本行动记忆

## 6. 不能做什么

本次明确禁止：
- 不删除文件，除非用户明确确认
- 不发送邮件、消息、付款、提交表单，除非用户明确确认
- 不上传截图、音频、记忆文件到外部服务，除非用户明确确认
- 不覆盖已有 skill，除非先备份
- 不跳过 Obsidian 行动记录

## 7. 需要调用的 skill

本次需要：
  - obsidian-memory

## 8. 需要使用的 Codex App 插件功能

本次需要：
  - none

## 9. 行动步骤

- [x] Step 1: 记录行动记忆。
- [x] Step 2: 创建 GUI 自动化参考目录和 PoC checklist 目录。
- [x] Step 3: 创建 GUI_Reference_Mano-P.md。
- [x] Step 4: 创建 Mano-P_PoC_Checklist.md。
- [x] Step 5: 检查关键章节、来源链接和敏感模式。

## 10. 风险检查

风险：
- 中。文档涉及第三方开源项目、GUI 自动化、模型/SDK、cloud/local 数据边界和后续可能的安装授权。

缓解措施：
- 本轮只写文档；不克隆、不安装、不下载模型、不启用 GUI 自动化、不提交不 push。

## 11. 部门通知

需要通知哪个部门：
  - GUI 自动化部
  - 工程部
  - 安全部
  - 技能优化部
  - 记忆部

通知原因：
- 这些部门已在上一轮讨论中给出路线意见，本轮把共识固化成文档。

## 12. 执行结果

实际做了什么：
- 创建 Mano-P GUI 参考文档和 PoC checklist，明确其是参考项目与 PoC 候选，暂不是主系统依赖。

成功：
- 成功。两个文档已创建；关键章节存在；未发现 token/private-key 或精确 thread id 模式。

失败：
- 无。

## 13. 产生的新资料

新增文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-58_总控办公室_create-mano-p-reference-poc-docs.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/References/GUI_Reference_Mano-P.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md

更新文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-58_总控办公室_create-mano-p-reference-poc-docs.md

截图/日志/轨迹：
- 未截图，未启动 GUI 自动化。

## 14. 下一步

下一步建议：
- 下一步可先处理 thread id 脱敏修复；之后再提交本轮 Mano-P 文档，或继续进入 Mano-P Stage 0 只读研究。

## 15. 给用户的简短汇报

用简短中文告诉用户：
- 已创建 Mano-P GUI 参考文档和 PoC checklist；本轮没有克隆、安装、运行或提交。

## Log 2026-06-17 18:59

- 完成文档固化：新增 GUI_Reference_Mano-P.md 和 Mano-P_PoC_Checklist.md；检查关键章节和来源链接通过；敏感模式扫描无命中；未克隆、未安装、未运行、未提交、未 push。
