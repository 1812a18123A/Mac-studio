---
type: department_handoff
task_id: real-v0-3-mano-p-integration
priority: medium
initiating_department: 总控办公室
receiving_department: 安全部
status: ready_for_discussion
created_at: 2026-06-17
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-46_总控办公室_discuss-mano-p-integration.md
reference_project:
  - https://github.com/Mininglamp-AI/Mano-P
result_path: AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_safety_result.md
---

# 交接包：real-v0-3-mano-p-integration - 安全部

## 背景

Mano-P 是公开开源 GUI-VLA 项目。若考虑接入，需要安全部评估许可证、供应链、模型/权重、下载、GUI 自动化和隐私风险。

## 请求安全部讨论

请判断：

- 是否允许把 Mano-P 作为正式参考项目。
- 是否允许后续克隆或引入依赖，前置条件是什么。
- Apache-2.0 是否存在明显阻断。
- GUI 自动化、截图、桌面控制、模型下载、第三方权重有哪些风险。
- 是否需要先做只读仓库可见性/许可证/Release 检查。

## 禁止事项

- 不克隆、不下载模型、不安装依赖。
- 不启动 GUI 自动化。
- 不操作账号、token、SSH key。
- 不提交、不 push。

## 成功标准

写回 result，包含：

- `status`: `allow_reference` / `allow_poc_with_conditions` / `blocked`
- 安全准入条件。
- 许可证和供应链判断。
- 用户确认项。

## 结果写回位置

```text
AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_safety_result.md
```
