---
type: department_handoff_result
task_id: real-v0-3-mano-p-integration
department: 工程部
status: recommend_poc_first
created_at: 2026-06-17
source_handoff: AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_engineering.md
reference_project:
  - https://github.com/Mininglamp-AI/Mano-P
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-48_工程部_real-v0-3-mano-p-integration.md
---

# 工程部结果：real-v0-3-mano-p-integration

## status

`recommend_poc_first`

## 已读取资料

- `AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_engineering.md`
- `https://github.com/Mininglamp-AI/Mano-P`

只读观察：

- Mano-P 是 GUI-VLA / Computer Use Agent 方向项目，强调本地边缘设备执行和隐私。
- 仓库显示 Apache-2.0 license，允许商业使用、修改和分发，但需要保留版权声明并标注修改。
- 仓库当前有 README、中文 README、LICENSE、pics，显示无正式 GitHub release。
- README 描述当前分阶段开源：先开放 Mano-CUA Skills，后续再开放本地模型和 SDK 组件。
- 安装入口展示为 Homebrew CLI 和 OpenClaw/Claude Code Skill，而不是一个稳定可直接嵌入 esmee AI 的库 API。
- 硬件门槛明确：本地模式面向 Apple M4 芯片、32GB RAM，或外接算力棒；也存在 cloud mode，会发送截图和任务描述到外部服务。

## 工程判断

不建议现在把 Mano-P 作为直接依赖加入 esmee AI 主仓库，也不建议 clone 或 vendor 进来。当前更合适的路线是先做隔离 PoC：把 Mano-P 当作外部可选能力，在独立沙箱中验证安装、权限、数据流、任务成功率和与现有部门流程的边界。

原因：

- 公开仓库当前更像产品/研究入口和 CLI/skill 分发说明，不像稳定 SDK。
- GUI 自动化会触碰截图、桌面控制、隐私和外发边界，必须先由安全部确认。
- 本地硬件要求较高，不能假设所有 esmee AI 环境可运行。
- cloud mode 与 esmee AI 的本地优先原则存在潜在冲突。
- 直接引入会把模型、GUI 权限、运行时依赖、Homebrew 分发、外部服务策略一起带进维护面。

## 接入路线

推荐路线：

1. `reference_only` 阶段：先把 Mano-P 作为可研对象，记录能力、许可证、硬件要求和安全边界。
2. `poc_sandbox` 阶段：在独立目录或独立机器上验证，不进入主仓库依赖树；只记录步骤和结果。
3. `adapter_design` 阶段：如果 PoC 成功，只设计最小 adapter，输入是任务描述和允许范围，输出是行动日志和结果；不要让 Mano-P 直接控制 esmee AI 的核心记忆/仓库流程。
4. `optional_integration` 阶段：将其作为可选 GUI 自动化 provider，而不是基础依赖。

不推荐路线：

- 不建议 Git submodule：会把外部项目生命周期和主仓库绑定，维护成本高。
- 不建议直接依赖 Homebrew CLI：版本、权限和机器状态不稳定，且不适合无确认自动执行。
- 不建议把 Mano-P 代码复制进 AgentVault：会引入许可证标注、更新同步和供应链审计成本。

## 工程风险

- 许可证风险低到中：Apache-2.0 友好，但一旦分发修改版，必须保留声明和记录修改。
- 供应链风险中：安装入口、外部模型/SDK、Homebrew tap、skill 分发都需要安全审查。
- 权限风险高：GUI 自动化、截图、桌面控制、跨 App 操作都需要明确用户确认。
- 隐私风险中到高：本地模式较友好，但 cloud mode 会外发截图和任务描述，不应默认启用。
- 维护风险中：无正式 release，阶段性开源，SDK/模型尚可能变化。
- 架构风险中：如果直接接入主流程，会让 esmee AI 的可审计行动记忆和权限边界变复杂。

## 最小下一步

1. 请安全部先出一页风险边界：是否允许 GUI 自动化、截图、cloud mode、Homebrew 安装、外部模型下载。
2. 请技能优化部整理 Mano-P 能力映射：哪些能力可转成 esmee AI skill，哪些只保留参考。
3. 工程部后续只在用户确认后创建 PoC 交接包，范围限定为“只读安装方案评估 + sandbox runbook”，仍不进入主仓库依赖。
4. PoC 通过后再决定是否写最小 adapter；adapter 默认读取本地配置，默认禁用外发和自动桌面控制。

## 当前禁止事项执行情况

- 未 clone Mano-P。
- 未安装依赖。
- 未写代码。
- 未修改仓库结构。
- 未提交、未 push。
- 未操作 token 或 SSH key。
