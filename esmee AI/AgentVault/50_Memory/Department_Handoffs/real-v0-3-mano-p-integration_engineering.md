---
type: department_handoff
task_id: real-v0-3-mano-p-integration
priority: medium
initiating_department: 总控办公室
receiving_department: 工程部
status: ready_for_discussion
created_at: 2026-06-17
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-46_总控办公室_discuss-mano-p-integration.md
reference_project:
  - https://github.com/Mininglamp-AI/Mano-P
result_path: AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_engineering_result.md
---

# 交接包：real-v0-3-mano-p-integration - 工程部

## 背景

用户希望讨论是否把 Mano-P 直接加进项目。工程部需要评估最小接入策略，而不是默认从零实现 GUI agent 能力。

## 请求工程部讨论

请判断：

- 是否可直接复用 Mano-P，还是当前公开内容更适合参考。
- 接入方式：文档参考、Git submodule、adapter、PoC sandbox、或暂不接入。
- Apache-2.0 对集成的工程影响。
- 如果后续 PoC，最小工程步骤是什么。
- 是否需要先等待 Mano-P 后续开源模型/SDK。

## 禁止事项

- 不克隆 Mano-P。
- 不安装依赖。
- 不写代码。
- 不修改仓库结构。
- 不提交、不 push。
- 不操作 token 或 SSH key。

## 成功标准

写回 result，包含：

- `status`: `recommend_poc_first` / `recommend_reference_only` / `recommend_direct_dependency` / `blocked`
- 接入路线。
- 工程风险。
- 最小下一步。

## 结果写回位置

```text
AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_engineering_result.md
```
