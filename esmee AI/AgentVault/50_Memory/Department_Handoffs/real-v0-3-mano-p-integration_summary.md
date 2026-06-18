---
type: department_discussion_summary
task_id: real-v0-3-mano-p-integration
date: 2026-06-17
owner_department: 总控办公室
status: completed
risk_level: medium
current_mode: 坤-兑
chinese_title: Mano-P 接入讨论汇总
中文标题: Mano-P 接入讨论汇总
summary_zh: 汇总多部门对 Mininglamp-AI/Mano-P 是否直接接入 esmee AI 的判断，结论是作为 GUI 自动化参考项目和受控 PoC 候选，不直接成为主系统依赖。
中文摘要: 汇总多部门对 Mininglamp-AI/Mano-P 是否直接接入 esmee AI 的判断，结论是作为 GUI 自动化参考项目和受控 PoC 候选，不直接成为主系统依赖。
aliases:
  - Mano-P接入讨论
  - GUI自动化参考项目
  - Mano-P受控PoC
search_keywords:
  - Mano-P
  - GUI自动化
  - 受控PoC
  - 参考项目
  - 本地优先
  - cloud mode
  - 安全边界
检索元素:
  - Mano-P
  - GUI自动化
  - 受控PoC
  - 参考项目
  - 本地优先
  - cloud mode
  - 安全边界
reference_project:
  - https://github.com/Mininglamp-AI/Mano-P
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-46_总控办公室_discuss-mano-p-integration.md
related_results:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_gui_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_engineering_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_safety_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_memory_result.md
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_skillopt_result.md
---

# 讨论汇总：Mano-P 是否直接接入 esmee AI

## 中文检索索引

- 中文标题：Mano-P 接入讨论汇总
- 中文摘要：汇总多部门对 Mininglamp-AI/Mano-P 是否直接接入 esmee AI 的判断，结论是作为 GUI 自动化参考项目和受控 PoC 候选，不直接成为主系统依赖。
- 相关部门：GUI 自动化部、工程部、安全部、记忆部、技能优化部、总控办公室。
- 中文关键词：Mano-P、GUI 自动化、受控 PoC、参考项目、本地优先、cloud mode、安全边界。

## 1. 讨论问题

用户希望相关部门讨论：既然 GUI 自动化路线要参考 Mininglamp-AI/Mano-P，是否应直接接入或加入该开源项目，而不是只停留在灵感层。

## 2. 部门结论

| 部门 | 结论状态 | 核心建议 |
| --- | --- | --- |
| GUI 自动化部 | `recommend_poc_first` | Mano-P 方向高度匹配，但应先做受控 PoC，不直接并入主系统。 |
| 工程部 | `recommend_poc_first` | 不建议 submodule、vendor 或直接依赖；先做隔离 PoC 和最小 adapter 评估。 |
| 安全部 | `allow_poc_with_conditions` | 允许正式参考和受控 PoC；禁止未经确认克隆、安装、下载模型、启用 GUI 或 cloud mode。 |
| 记忆部 | `recommend_route_doc` | 应写入正式 GUI 路线文档，定位为参考项目和 PoC 候选，暂不是可复用依赖。 |
| 技能优化部 | `recommend_poc_checklist` | 建议先创建参考文档和 PoC checklist，再决定是否沉淀为 GUI skill 或 adapter。 |

## 3. 总控结论

Mano-P 应进入 esmee AI GUI 自动化路线，但当前不应直接接入主系统。

推荐分级：

- `参考项目`: 立即成立。
- `PoC 候选`: 立即成立，但必须受控。
- `可复用依赖`: 暂不成立，需 PoC 通过后再定。
- `主系统依赖`: 当前不成立。

## 4. 推荐路线

第一小步：

```text
AgentVault/30_GUI_Automation/References/GUI_Reference_Mano-P.md
```

记录 Mano-P 的官方链接、许可证、GUI-VLA、本地优先、think-act-verify、长任务 GUI 自动化、Local Mode / Cloud Mode 差异、风险边界和 PoC 前置条件。

第二小步：

```text
AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
```

只做 checklist，不安装、不运行、不克隆。

第三小步：

在用户确认后进入隔离 PoC：

- 只读克隆或下载前先确认。
- 不进入主仓库依赖树。
- 默认禁用 cloud mode。
- 不操作真实账号、付款、上传、删除、GitHub 设置或 Obsidian 私有配置。
- GUI 自动化和截图必须由用户明确确认。

## 5. 不建议的做法

- 不建议现在把 Mano-P 作为 Git submodule。
- 不建议复制 Mano-P 源码进 AgentVault。
- 不建议直接安装 Homebrew tap、SDK、模型或第三方 skill。
- 不建议让 Mano-P 替代总控办公室、记忆部或安全部。
- 不建议在未确认前启用 cloud mode 或真实桌面 GUI 控制。

## 6. 需要用户确认

进入下一步前，需要用户确认是否执行：

- 创建 `GUI_Reference_Mano-P.md`。
- 创建 `Mano-P_PoC_Checklist.md`。

这两步仍不涉及克隆、安装、运行或 GUI 自动化。

## 7. 本轮未执行事项

- 未克隆 Mano-P。
- 未安装依赖。
- 未下载模型或 SDK。
- 未启动 GUI 自动化。
- 未写代码或 adapter。
- 未修改主仓库依赖。
- 未提交、不 push。
