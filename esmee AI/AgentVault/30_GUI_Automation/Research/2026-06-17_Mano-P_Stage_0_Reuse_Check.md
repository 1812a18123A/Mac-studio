---
type: gui_reuse_check
project_id: mano-p
date: 2026-06-17
owner_department: GUI 自动化部
status: completed
risk_level: medium
current_mode: 坤-兑
chinese_title: Mano-P Stage 0 复用检查
中文标题: Mano-P Stage 0 复用检查
summary_zh: 记录 Mano-P 作为 GUI 自动化参考项目和受控 PoC 候选的只读复用检查结论、许可证判断、供应链入口、local/cloud 模式和最小 adapter 候选边界。
中文摘要: 记录 Mano-P 作为 GUI 自动化参考项目和受控 PoC 候选的只读复用检查结论、许可证判断、供应链入口、local/cloud 模式和最小 adapter 候选边界。
aliases:
  - Mano-P复用检查
  - GUI自动化复用研究
  - Stage0只读研究
search_keywords:
  - Mano-P
  - Stage 0
  - 复用检查
  - GUI自动化
  - Local Mode
  - Cloud Mode
  - 供应链
  - adapter草案
检索元素:
  - Mano-P
  - Stage 0
  - 复用检查
  - GUI自动化
  - Local Mode
  - Cloud Mode
  - 供应链
  - adapter草案
source_project:
  - https://github.com/Mininglamp-AI/Mano-P
source_readme:
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/README.md
source_license:
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/LICENSE
source_issues:
  - https://github.com/Mininglamp-AI/Mano-P/issues/9
  - https://github.com/Mininglamp-AI/Mano-P/issues/15
  - https://github.com/Mininglamp-AI/Mano-P/issues/16
related_reference:
  - AgentVault/30_GUI_Automation/References/GUI_Reference_Mano-P.md
related_checklist:
  - AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_19-43_gui-自动化部_mano-p-stage-0-reuse-check.md
---

# Mano-P Stage 0 Reuse Check

## 中文检索索引

- 中文标题：Mano-P Stage 0 复用检查
- 中文摘要：记录 Mano-P 作为 GUI 自动化参考项目和受控 PoC 候选的只读复用检查结论、许可证判断、供应链入口、local/cloud 模式和最小 adapter 候选边界。
- 相关部门：GUI 自动化部、工程部、安全部、记忆部、技能优化部。
- 中文关键词：Mano-P、Stage 0、复用检查、GUI 自动化、Local Mode、Cloud Mode、供应链、adapter 草案。

## 1. 一句话结论

Mano-P 可以继续作为 esmee AI GUI 自动化路线的正式参考项目和受控 PoC 候选，但当前不应直接接入、不应作为主系统依赖、不应写生产 adapter。

当前决策：

- `reference_project`: yes
- `poc_candidate`: yes
- `direct_dependency`: no
- `adapter_implementation`: not_yet
- `clone_install_run`: requires_user_confirmation
- `cloud_mode`: disabled_by_default

## 2. 本轮只读范围

已读资料：

- 官方仓库首页和文件树。
- 官方 README。
- 官方 LICENSE。
- 本地 `GUI_Reference_Mano-P.md`。
- 本地 `Mano-P_PoC_Checklist.md`。
- 部分公开 issue，优先关注 local mode、内存、SDK、架构和运行入口风险。

未执行：

- 未克隆仓库。
- 未安装 Homebrew tap、SDK、模型、skill 或依赖。
- 未运行 Mano-P。
- 未启动截图、屏幕录制、Accessibility 或 GUI 自动化。
- 未访问账号页面、付款页面、GitHub 设置或 Obsidian 私有配置。

## 3. 官方项目表面

公开仓库当前主要包含：

- `README.md`
- `README_CN.md`
- `LICENSE`
- `pics/`

本轮未在主仓库根目录看到独立 `examples/` 目录，因此 Stage 0 不能声称已经存在可直接复用的 example suite。

README 公开信息显示，Mano-P 定位为 GUI-VLA agent，强调边缘设备、本地优先、长任务 GUI 自动化和 think-act-verify。README 同时区分 cloud mode 与 local mode；local mode 需要显式参数和额外本地组件。

## 4. 许可证判断

主仓库 LICENSE 为 Apache-2.0。

当前可以成立：

- 作为参考项目记录。
- 作为 PoC 候选记录。
- 在后续文档中引用来源链接。

当前不能直接成立：

- 复制源码进 AgentVault。
- 作为主仓库依赖。
- 作为可分发组件。
- 将其 README、图片、demo、模型或 skill 当成 esmee AI 原生资产。

原因：

- README、图片、视频、模型权重、SDK、Homebrew tap、Claude Code skill、OpenClaw skill、第三方依赖可能各自有单独条款。
- Apache-2.0 主许可证不足以覆盖所有外部分发和运行材料。

## 5. 供应链与运行入口

README 指向的潜在入口包括：

- Homebrew tap。
- OpenClaw。
- Claude Code skill。
- CLI 形式的 `mano run`。
- local mode 所需 SDK 与模型。

工程判断：

- 当前不应 vendor 或 submodule。
- 当前不应直接把 Mano-P 写进 esmee AI 依赖树。
- 若进入 Stage 1，只能克隆到隔离目录或临时目录。
- Stage 1 之前必须列出安装入口、下载内容、模型体积、hash、license、系统权限和卸载路径。

## 6. Local Mode / Cloud Mode 判断

README 显示 Mano-P 支持 cloud mode 和 local mode。

esmee AI 默认策略：

- 只优先评估 local mode。
- cloud mode 默认禁用。
- 若后续评估 cloud mode，必须单独列出会外发的截图、任务描述、窗口标题、路径、日志和服务方。

安全判断：

- 即使 README 声称 cloud mode 不访问本地文件、剪贴板或凭据，也不能自动等同于 esmee AI 安全部批准。
- 任何屏幕内容外发都需要用户确认和安全部审查。
- local mode 也不是零风险，因为仍可能涉及截图、鼠标键盘、系统权限和第三方模型/SDK。

## 7. 公开 issue 风险信号

本轮只读查看到的公开 issue 显示以下风险方向：

- local mode 可能出现图像 token 过多或上下文窗口相关问题。
- W8A8 模型部署可能有内存压力。
- SDK 检查或 torch/架构兼容可能失败。
- GUI 自动化场景中可能需要处理 Cursor、macOS 和模型运行细节。

这说明 Mano-P 仍适合 PoC，而不是立即纳入主系统。

## 8. 与 esmee AI 的可复用边界

可复用思想：

- observe / think / act / verify 循环。
- GUI-VLA provider 作为可替换执行层。
- 长任务拆分、一步一验证。
- 本地优先与失败即停。

不可复用为默认主链路：

- 不替代总控办公室的任务判断。
- 不替代安全部的权限和隐私闸门。
- 不替代记忆部的行动记忆写入。
- 不替代工程部的依赖审计。
- 不绕过用户确认执行真实桌面动作。

## 9. 最小 adapter 候选

当前只允许保留 adapter 草案，不写实现。

未来若 Stage 1 和 Stage 2 通过，最小 adapter 应只暴露：

- `observe_only`
- `propose_action`
- `execute_one_confirmed_action`

输入至少包括：

- `task_goal`
- `allowed_apps`
- `forbidden_actions`
- `stop_conditions`
- `action_memory_path`
- `mode`

输出至少包括：

- `observation`
- `proposed_action`
- `risk_check`
- `needs_confirmation`
- `execution_result`
- `verification_result`
- `failure_reason`

默认规则：

- 不确定就返回 `needs_confirmation`。
- 高风险动作不执行。
- 每一步都写行动记忆。
- 真实账号、付款、上传、删除、提交表单、发送消息、GitHub 设置、Obsidian 私有配置全部默认禁止。

## 10. Stage 0 通过标准

本轮 Stage 0 结论：

- 明确可运行入口：部分通过。README 提供入口，但未验证。
- 明确 local/cloud 差异：通过，但需安全部后续复核。
- 明确依赖和硬件要求：部分通过。已识别 SDK、模型、Homebrew tap、skills 等入口，但未形成完整依赖树。
- 明确 license 和 attribution 风险：部分通过。主仓库 Apache-2.0，外部材料需要二次审计。

综合结论：

```text
stage_0_result: passed_with_conditions
next_allowed_stage: stage_1_planning_only
blocked_actions: clone install run gui_execution cloud_mode direct_dependency
```

## 11. 下一步建议

下一步只建议做 Stage 1 计划，不直接执行 Stage 1：

1. 写 `Mano-P_Stage_1_Isolated_Install_Plan.md`。
2. 列出克隆目录、安装入口、依赖来源、模型来源、权限需求和清理方案。
3. 交安全部、工程部、GUI 自动化部复核。
4. 再由用户确认是否允许克隆或安装。

在用户确认前，不进入克隆、安装、下载、运行或 GUI 自动化。
