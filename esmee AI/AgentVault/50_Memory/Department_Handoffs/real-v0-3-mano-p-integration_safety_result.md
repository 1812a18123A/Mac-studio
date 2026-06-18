---
type: department_handoff_result
task_id: real-v0-3-mano-p-integration
department: 安全部
status: allow_poc_with_conditions
created_at: 2026-06-17
related_handoff: AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_safety.md
related_action_memory: AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-48_安全部_real-v0-3-mano-p-integration.md
current_mode: 坤-兑
---

# 交接结果：Mano-P 接入安全准入讨论

## status

`allow_poc_with_conditions`

## 结论

安全部允许把 Mininglamp-AI/Mano-P 作为正式参考项目；允许后续做受控 PoC；不建议直接接入生产或直接加入 esmee AI 主流程。

PoC 前必须完成许可证、供应链、模型权重、GUI 权限、云/本地模式、截图隐私、安装范围和回滚方案确认。

## 已读取资料

- `AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_safety.md`
- `AgentVault/70_Safety/Permission_Boundaries.md`
- `AgentVault/00_System/Repository_Policy.md`
- GitHub: `https://github.com/Mininglamp-AI/Mano-P`
- GitHub LICENSE: `https://github.com/Mininglamp-AI/Mano-P/blob/main/LICENSE`
- GitHub README: `https://github.com/Mininglamp-AI/Mano-P/blob/main/README.md`

## 许可证判断

- 仓库页面显示许可证为 Apache-2.0。
- Apache-2.0 通常允许使用、修改和分发，但需要保留 license、notice、版权声明，并标明修改。
- 许可证本身不是明显阻断项。
- 仍需单独确认：模型权重、SDK、Homebrew tap、ClawHub skill、视频/图片素材、论文或数据集是否有不同许可或使用条款。

## 供应链判断

- Mano-P 是公开 GitHub 仓库，适合作为只读研究对象。
- 不应在未审查前执行安装脚本、Homebrew tap、SDK 安装、模型下载或第三方 skill 安装。
- 本地模式需要模型/SDK，属于下载和执行第三方二进制或权重，必须先由工程部做依赖清单、hash/来源、版本锁定和隔离环境方案。
- 云模式会把截图和任务描述发往外部服务，默认不允许用于 esmee AI 的隐私或本地优先任务。
- GUI 自动化能力包含截图、点击、输入、拖拽、应用启动、URL 导航等高风险动作，必须受安全部审批和用户确认约束。

## 安全准入条件

PoC 必须满足：

1. 仅在隔离目录或独立测试用户环境中运行，不接触真实账号、支付、私密文档、聊天记录、密钥或生产资料。
2. 默认禁用 cloud mode；若要用 cloud mode，必须单独确认截图和任务描述外发范围。
3. GUI 自动化默认关闭；启用前必须记录目标 App、动作范围、停止条件、截图保存位置和失败回滚方式。
4. 禁止自动发消息、提交表单、付款、删除、移动文件、修改系统设置或操作账号。
5. 禁止让 Mano-P 读取或操作 `.obsidian/`、密钥目录、浏览器密码、钥匙串、SSH key、token、GitHub 设置。
6. 依赖安装前必须由工程部输出 SBOM/依赖清单和最小安装路线。
7. 模型权重下载前必须确认来源、许可证、体积、hash、存放位置、是否会联网。
8. PoC 日志和截图不得进入远端仓库，除非用户另行确认并脱敏。
9. 所有执行动作必须写入 Obsidian 行动记忆。

## 用户确认项

- 是否允许后续只读克隆仓库。
- 是否允许安装 Homebrew tap、SDK、Python 环境或 ClawHub skill。
- 是否允许下载模型权重或连接计算棒。
- 是否允许启用 GUI 自动化。
- 是否允许 cloud mode，以及哪些截图/任务描述可以外发。
- 是否允许在测试环境中控制浏览器、Obsidian、Finder、Terminal 或其它 App。
- 是否允许把 Mano-P 相关文件加入 esmee AI 仓库，还是仅保留本地研究目录。

## 推荐路径

1. 当前阶段：`allow_reference`，只做公开资料研究和架构比较。
2. 下一阶段：在用户确认后进入 `allow_poc_with_conditions`，只做隔离 PoC。
3. 生产接入：必须等待 PoC 安全报告、依赖清单、权限最小化方案、GUI 失败保护和隐私评估完成。

## 本次未执行事项

- 未克隆仓库。
- 未下载模型。
- 未安装依赖。
- 未启动 GUI 自动化。
- 未操作账号、token、SSH key。
- 未提交。
- 未 push。
