---
type: department_handoff_result
date: 2026-06-17
department: GUI 自动化部
task_id: real-v0-3-mano-p-integration
status: recommend_poc_first
related_handoff: AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_gui.md
related_action_memory: AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-48_gui-自动化部_real-v0-3-mano-p-integration-gui.md
current_mode: 坎-兑
requires_user_confirmation_for_poc: true
---

# 交接结果：Mano-P 接入方式讨论

## 实际做了什么

- 读取 GUI 自动化部交接包。
- 读取 `$obsidian-memory` 规则、handoff 示例和 `Permission_Boundaries.md`。
- 查看公开参考项目：<https://github.com/Mininglamp-AI/Mano-P>。
- 未启动 GUI 自动化、未截图、未克隆 Mano-P、未安装依赖、未写代码、未提交、未 push。

## 结论

建议状态：

```text
recommend_poc_first
```

GUI 自动化部不建议现在直接把 Mano-P 并入 esmee AI 主系统，也不建议只停留在灵感层。最合适路线是先做受控 PoC：把 Mano-P 当作候选 GUI-VLA 执行引擎，先验证安装、许可证、硬件、隐私、本地执行、可回退性和最小任务成功率，再决定是否直接接入。

## 为什么不是直接接入

- Mano-P 与 esmee AI 的目标高度相关：视觉驱动 GUI 操作、长任务执行、本地推理、think-act-verify、浏览器/桌面 App 自动化都与 GUI 自动化部职责匹配。
- 但直接接入风险过高：GUI 控制、截图/屏幕读取、鼠标键盘输入都属于 `Permission_Boundaries.md` 中需要用户确认的动作。
- 公开 README 显示 Mano-P 是分阶段开源：先开放 Mano-CUA Skills，之后再开放本地模型和 SDK 组件，再开放训练方法。这意味着当前可直接接入的稳定接口、SDK 完整度和本地部署路径需要先核验。
- 项目宣称支持 Apple Silicon 本地运行，但硬件门槛、依赖复杂度、模型下载、运行权限和 macOS 辅助功能权限都需要工程部/安全部共同验证。
- esmee AI 已经有 Obsidian 记忆、部门路由、行动审计和安全边界；Mano-P 更适合先作为“GUI 执行后端候选”，不应替代现有调度与记忆系统。

## GUI 适配判断

适合吸收或验证的能力：

- 纯视觉 GUI grounding：识别屏幕元素、按钮、输入区、状态变化。
- think-act-verify 循环：先观察，再提出动作，再验证结果，适合 esmee AI 的“先阴后阳”工作方式。
- 长任务拆解与执行：可作为 GUI 自动化部未来执行复杂桌面流程的候选能力。
- 本地优先路线：如果本地模型和 SDK 可用，符合 esmee AI 的隐私目标。
- Mano-CUA Skills 思路：适合沉淀为 GUI 操作画像、App skill、失败回退策略。

暂不适合直接吸收的部分：

- 自动无人工介入的长任务 GUI 执行。esmee AI 目前必须保留用户确认、行动记忆、安全部审查和停止点。
- 真实账号、外部网站、GitHub 设置、付款、上传、提交表单等高风险 GUI 动作。
- 直接把 Mano-P 作为总控 Agent。Mano-P 应作为 GUI 执行/感知层候选，不应覆盖总控办公室、记忆部和安全部。

## 当前 GUI 自动化部与 Mano-P 的差距

- GUI 自动化部已有：部门边界、行动记忆、安全停止规则、Codex App 会话协作、Obsidian 文件写回。
- GUI 自动化部缺口：统一的视觉 grounding 引擎、可重复的屏幕状态验证、长任务 GUI 执行器、App 操作画像库、失败恢复策略。
- Mano-P 可能补齐：视觉定位、GUI-VLA 推理、think-act-verify、跨 App 自动化经验。
- 仍需自建或保留：Obsidian 审计、权限确认、部门交接、任务降级、回退到 Markdown 文件写入。

## 最小 PoC 建议

PoC 目标：验证 Mano-P 是否能作为 esmee AI 的 GUI 执行后端，而不是验证它能否替代整个系统。

建议最小 PoC 分三步，每一步都需要用户明确授权后才执行：

1. 只读研究 PoC
   - 工程部读取 Mano-P README、LICENSE、安装说明、examples。
   - 不克隆、不安装；先输出复用检查和许可证判断。
   - 成功标准：明确可运行入口、依赖、硬件要求、是否支持纯本地模式。

2. 隔离安装 PoC
   - 在独立目录或临时环境安装，不写入主仓库。
   - 不接入真实账号、不操作 Obsidian、不操作 GitHub。
   - 成功标准：能启动最小 demo 或命令行帮助，能确认本地/云端调用边界。

3. 安全 GUI 验证 PoC
   - 只允许操作低风险本地窗口或静态测试页面。
   - 第一轮只观察和生成“拟执行动作”，不点击。
   - 第二轮如用户确认，允许执行一个可回退的点击或输入。
   - 成功标准：能识别目标、提出动作、执行后验证状态，并把全过程写入行动记忆。

## PoC 推荐场景

首选场景：本地静态 HTML 测试页或沙盒窗口。

- 任务：识别一个按钮或输入框，输出拟点击位置和理由。
- 禁止：访问真实账号页面、提交表单、上传文件、截图外发。
- 回退：如果 GUI 识别失败，停止并写入失败记忆，不继续点击。

第二场景：Obsidian 只读定位。

- 任务：打开已知笔记或观察当前窗口标题，判断是否在目标页面。
- 禁止：编辑笔记、删除内容、改 `.obsidian` 设置。
- 回退：优先使用 Markdown 文件写入器和 Obsidian URI，不依赖 GUI 完成记忆写入。

## 前置条件

- 安全部确认 GUI 自动化、屏幕读取、模型下载、外部网络、账号权限边界。
- 工程部完成现有方案搜索与复用检查，包括 Mano-P 许可证、安装复杂度、维护活跃度和可运行 demo。
- 总控办公室明确 Mano-P 在 esmee AI 中的定位：GUI 后端候选，而不是总控替代。
- 记忆部提供 PoC 行动记忆模板，记录每次观察、动作、验证和失败。
- 用户确认是否允许后续克隆、安装依赖、下载模型、启用辅助功能权限或执行 GUI 动作。

## 风险

- GUI 自动化风险：误点击、误输入、误提交、误操作真实 App。
- 隐私风险：屏幕内容、截图、账号页面、任务数据可能被模型或外部服务处理。
- 依赖风险：模型、SDK、加速库、硬件要求可能复杂。
- 许可证风险：仓库显示 Apache-2.0 许可证，适合复用，但仍需工程部在实际接入前核对 LICENSE、模型权重许可和第三方依赖许可。
- 架构风险：若直接接入为主执行层，可能绕过 esmee AI 的部门审计和安全确认。

## 最小集成边界

如果 PoC 通过，建议只写最小 adapter：

- 输入：任务目标、允许 App、禁止动作、停止条件、当前行动记忆路径。
- 输出：观察结果、拟执行动作、实际动作、验证结果、失败原因。
- 回退：任何不确定或高风险状态都返回 `needs_confirmation`，不继续执行。
- 记忆：每一步写入 Obsidian 行动记忆。

不建议：

- 直接把 Mano-P 放进总控办公室。
- 直接允许无确认的真实桌面长任务。
- 让 Mano-P 写入 Obsidian 记忆或修改仓库。
- 在没有安全部审查前启用截图、鼠标键盘控制或真实账号页面操作。

## 下一步建议

- 总控办公室：创建 `real-v0-3-mano-p-poc-plan`，明确是否进入 PoC。
- 安全部：先审查 Mano-P PoC 的权限边界、隐私边界、外部网络和模型下载风险。
- 工程部：做只读复用检查，不克隆不安装，先确认 README、LICENSE、examples、硬件要求。
- GUI 自动化部：等待授权后设计最小沙盒 GUI 任务。
- 技能优化部：若 PoC 成立，把 GUI 自动化 think-act-verify 流程沉淀为 skill 草案。
