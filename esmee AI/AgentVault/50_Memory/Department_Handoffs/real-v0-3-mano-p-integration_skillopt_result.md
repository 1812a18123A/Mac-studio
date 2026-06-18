---
type: department_handoff_result
task_id: real-v0-3-mano-p-integration
department: 技能优化部
status: recommend_poc_checklist
created_at: 2026-06-17
risk_level: medium
current_mode: 坤-巽-坎-兑
related_handoff: AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_skillopt.md
related_action_memory: AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-48_技能优化部_real-v0-3-mano-p-integration-skillopt-discussion.md
reference_project: https://github.com/Mininglamp-AI/Mano-P
---

# 技能优化部结果：real-v0-3-mano-p-integration

## 1. 结论

建议状态：

`recommend_poc_checklist`

不建议现在直接把 Mano-P 接入 esmee AI，也不建议只把它当灵感放过。更稳的路线是：

1. 先创建 Mano-P 参考文档。
2. 再创建最小 PoC checklist。
3. 通过安全部和 GUI 自动化部审查后，才决定是否沉淀为 GUI 自动化 skill 或 adapter。

理由：Mano-P 的方向高度相关，但涉及 GUI 自动化、截图、鼠标键盘控制、外部服务模式、安装依赖、模型/SDK、系统权限和许可证保留义务。按 esmee AI 的安全边界，应先做评估清单，不直接集成。

## 2. 已核对的公开信息

参考项目：

- `https://github.com/Mininglamp-AI/Mano-P`

公开 README 显示的关键点：

- Mano-P 是面向边缘设备的 GUI-VLA agent 项目，目标是本地/边缘 GUI 自动化。
- 项目提到阶段式开源：先开放 Mano-CUA Skills，再开放本地模型和 SDK 组件，之后开放训练方法。
- 支持 Apple Silicon 本地推理路线，但 README 同时列出 Cloud Mode。
- 安装入口包括 `brew tap Mininglamp-AI/tap && brew install mano-cua`，以及 OpenClaw/Claude Code Skill。
- Cloud Mode 会发送截图和任务描述到外部服务；Local Mode 才符合“截图和任务数据留在设备上”的方向。
- 项目许可证标注 Apache-2.0；相关 skill 页面标注 MIT 时，需分别核对许可证和 attribution。

## 3. 是否应创建或更新 GUI 自动化相关 skill

建议：暂不直接更新正式 skill，先新增 reference doc 和 PoC checklist。

后续若 PoC 通过，再考虑创建或更新：

- `AgentVault/60_Skills/Drafts/gui-automation-mano-p/SKILL.md`
- 或更新既有 GUI 自动化 skill 的 `Existing solution check` / `Safety boundaries` / `Verification` 部分。

skill 草稿应覆盖：

- 什么时候可以评估 Mano-P。
- 什么时候禁止使用 Cloud Mode。
- 如何记录屏幕读取、截图用途、保存路径和敏感窗口排除。
- 如何确认 macOS Screen Recording / Accessibility 权限。
- 如何设置人工确认点、停止条件和失败回滚。
- 如何把 Mano-P 作为可替换后端，而不是写死到 esmee AI 主流程。

## 4. 是否新增 `GUI_Reference_Mano-P.md`

建议新增。

推荐路径：

`AgentVault/30_GUI_Automation/References/GUI_Reference_Mano-P.md`

建议包含：

- 项目定位：GUI-VLA、本地/边缘 GUI 自动化。
- 官方链接、README 摘要、许可证摘要。
- 本地模式与云模式差异。
- 安装入口和依赖类型。
- 需要的 macOS 权限。
- 安全风险和禁止事项。
- 适合 esmee AI 的复用方式：reference / PoC / adapter，而不是直接复制实现。
- 未验证事项：模型下载、硬件要求、离线可用性、日志格式、失败处理、是否可被 Codex/Obsidian 稳定调用。

## 5. Mano-P PoC checklist 建议

建议新增 checklist，而不是立即写 adapter。

推荐路径：

`AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md`

最小 checklist：

- [ ] 许可证：确认 Mano-P 主仓库 Apache-2.0；相关 skill / SDK / 模型另行确认。
- [ ] 安装边界：不安装前先获得用户确认；记录 Homebrew tap、模型下载、外部网络访问。
- [ ] 模式选择：默认禁止 Cloud Mode；只评估 Local Mode。
- [ ] 数据边界：确认截图、任务描述、窗口标题、剪贴板、文件路径不会外发。
- [ ] 权限边界：Screen Recording、Accessibility、GUI 控制必须由用户明确确认。
- [ ] 测试范围：只选一个低风险 App 和一个可回滚任务。
- [ ] 停止条件：出现外发、登录、支付、删除、上传、敏感窗口时立即停止。
- [ ] 日志：所有截图路径、命令、失败原因写入行动记忆。
- [ ] 可替换性：PoC 结果只定义 adapter 接口，不把 Mano-P 写成唯一实现。
- [ ] 复用判断：若 Mano-P 完成 70% 以上 GUI 任务能力，则优先封装；若依赖/权限/云模式风险过高，则只保留参考文档。

## 6. 如何落实“先找现成方案，不从零造轮子”

建议把 Mano-P 纳入 GUI 自动化现有方案候选池：

候选优先级：

1. macOS Accessibility / ScreenCaptureKit / Apple Vision OCR。
2. Mano-P / mano-cua。
3. Codex computer-use / browser/chrome 控制能力。
4. 其他开源 GUI automation / CUA 项目。
5. 自定义最小 adapter。

决策规则：

- 若现成工具可本地运行、许可证可接受、权限可控，优先封装 CLI/SDK。
- 若需要云模式或外发截图，默认不进入 esmee AI 自动化主链路。
- 若只能启发架构，但不能安全运行，则保留 reference doc，不接入。
- 若要写代码，只写 adapter / wrapper / config / test，不复制 Mano-P 大段实现。

## 7. 如何避免直接复制实现

建议写入模板规则：

- 不复制 Mano-P 源码进入 esmee AI，除非另行完成许可证审查和 attribution。
- 不把 README 示例改写成“我们的原创实现”。
- 可以引用项目链接、许可证、能力边界和公开接口。
- 可以通过 CLI/SDK 方式调用，前提是用户确认安装和权限。
- 可以学习流程结构：感知、规划、执行、验证、失败停止。
- 所有引用文档保留来源链接和许可证说明。

## 8. 安全边界

Mano-P 相关任务至少属于中风险，原因：

- GUI 自动化可能点击、输入、上传、提交或删除。
- 截图和任务描述可能包含隐私。
- Cloud Mode 涉及外部服务。
- 安装 CLI、模型或 SDK 涉及依赖和网络。
- macOS Screen Recording / Accessibility 是敏感权限。

因此后续任何 PoC 必须先通知：

- 安全部
- GUI 自动化部
- 工程部
- 总控办公室

并明确：

- 目标 App。
- 任务动作。
- 可接受失败范围。
- 截图和日志保存位置。
- 是否完全离线。
- 停止条件。

## 9. 最小下一步

建议总控办公室下一步只派一个小任务：

创建 `GUI_Reference_Mano-P.md` 草稿，不安装、不运行、不写 adapter。

推荐交接给 GUI 自动化部 + 安全部联合审查，成功标准：

- reference doc 能说明 Mano-P 是什么。
- 能区分 Local Mode / Cloud Mode。
- 能列出许可证与 attribution 风险。
- 能列出 PoC 前置确认项。
- 能给出是否进入 PoC 的判断。

## 10. 本次未执行事项

- 未修改全局 skill。
- 未发布 skill。
- 未写代码。
- 未安装 Mano-P。
- 未运行 Mano-P。
- 未提交、不 push。
- 未创建 reference doc 或 PoC checklist。
