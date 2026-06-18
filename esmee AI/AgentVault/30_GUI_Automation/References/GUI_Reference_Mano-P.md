---
type: gui_reference_project
project_id: mano-p
date: 2026-06-17
owner_department: GUI 自动化部
status: reference_active
risk_level: medium
current_mode: 坤-兑
chinese_title: Mano-P GUI 自动化参考
中文标题: Mano-P GUI 自动化参考
summary_zh: 记录 Mano-P 作为 esmee AI GUI 自动化路线参考项目和 PoC 候选的定位、来源、可借鉴能力、边界、安全风险和 PoC 前置条件。
中文摘要: 记录 Mano-P 作为 esmee AI GUI 自动化路线参考项目和 PoC 候选的定位、来源、可借鉴能力、边界、安全风险和 PoC 前置条件。
aliases:
  - GUI参考Mano-P
  - Mano-P参考项目
  - GUI自动化PoC候选
search_keywords:
  - Mano-P
  - GUI自动化
  - GUI-VLA
  - think-act-verify
  - Local Mode
  - Cloud Mode
  - PoC前置条件
检索元素:
  - Mano-P
  - GUI自动化
  - GUI-VLA
  - think-act-verify
  - Local Mode
  - Cloud Mode
  - PoC前置条件
source_project:
  - https://github.com/Mininglamp-AI/Mano-P
source_readme:
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/README.md
source_license:
  - https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/LICENSE
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-46_总控办公室_discuss-mano-p-integration.md
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-58_总控办公室_create-mano-p-reference-poc-docs.md
related_discussion_summary:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-integration_summary.md
---

# GUI Reference: Mano-P

## 中文检索索引

- 中文标题：Mano-P GUI 自动化参考
- 中文摘要：记录 Mano-P 作为 esmee AI GUI 自动化路线参考项目和 PoC 候选的定位、来源、可借鉴能力、边界、安全风险和 PoC 前置条件。
- 相关部门：GUI 自动化部、工程部、安全部、记忆部、技能优化部。
- 中文关键词：Mano-P、GUI 自动化、GUI-VLA、think-act-verify、Local Mode、Cloud Mode、PoC 前置条件。

## 1. 定位

Mano-P 是 esmee AI GUI 自动化路线的正式参考项目和 PoC 候选。

当前定位：

- `reference_project`: yes
- `poc_candidate`: yes
- `direct_dependency`: no
- `main_system_replacement`: no

本文件只记录参考路线，不表示已经接入、安装、克隆、运行或授权 GUI 自动化。

## 2. 来源

项目：

```text
https://github.com/Mininglamp-AI/Mano-P
```

README：

```text
https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/README.md
```

LICENSE：

```text
https://raw.githubusercontent.com/Mininglamp-AI/Mano-P/main/LICENSE
```

公开 README 显示，Mano-P 是面向边缘设备的 GUI-VLA agent 项目，强调 Private AI、本地/边缘推理、GUI 自动化、长任务规划执行和 think-act-verify。仓库标注 license 为 Apache-2.0。

## 3. 可借鉴能力

适合 esmee AI 借鉴的方向：

- 视觉驱动 GUI 操作：通过屏幕视觉理解定位按钮、输入框、状态变化和操作结果。
- think-act-verify 循环：先观察，再规划动作，再验证执行结果。
- 长任务 GUI 自动化：将复杂流程拆成可验证步骤，而不是一次性盲目点击。
- 本地优先与隐私优先：优先让截图、任务数据和 GUI 操作留在本机。
- GUI-VLA 作为执行后端：可作为 GUI 自动化部未来的可替换 provider。
- 失败回退：任何不确定、高风险或不可验证状态都应停止，并回写行动记忆。

## 4. 与 esmee AI 的边界

Mano-P 不应替代：

- 总控办公室的任务判断和范围控制。
- 记忆部的行动记忆、交接包和结果归档。
- 安全部的权限确认、隐私判断和停止规则。
- 工程部的依赖审计、最小 adapter 和测试边界。
- 用户对高风险 GUI 动作的最终确认。

Mano-P 若后续 PoC 成功，只能作为 GUI 执行或视觉理解候选层，而不是 esmee AI 的总控大脑。

## 5. Local Mode / Cloud Mode

必须区分：

- Local Mode：优先方向。目标是截图、任务描述和 GUI 操作留在本机。
- Cloud Mode：默认禁止进入 esmee AI 主链路；若要评估，必须单独确认外发内容、服务方、日志和隐私边界。

任何涉及截图、屏幕内容、窗口标题、剪贴板、账号页面、私密文档或任务描述外发的模式，都必须先由安全部审查并获得用户确认。

## 6. 许可证与归属

当前主仓库标注 Apache-2.0。

可初步认为：

- 作为参考项目记录：允许。
- 作为 PoC 候选：允许，但需保留来源链接和许可证说明。
- 作为直接依赖或分发组件：必须再次核对 license、notice、第三方依赖、模型权重、SDK、Homebrew tap、skills、数据集和素材许可证。

禁止：

- 将 Mano-P README、代码或示例改写成 esmee AI 原创实现。
- 复制源码进 AgentVault，除非完成许可证审查和 attribution。
- 忽略模型权重、SDK、外部 skill 或安装包可能具有不同许可的事实。

## 7. 安全边界

Mano-P 相关 PoC 至少属于中风险，因为可能涉及：

- 截图和屏幕读取。
- 鼠标、键盘、窗口、浏览器或桌面 App 控制。
- macOS Screen Recording / Accessibility 权限。
- Homebrew tap、SDK、模型权重或第三方 skill 安装。
- 外部网络或 cloud mode。
- 真实账号、隐私资料、GitHub 设置、Obsidian vault 或本地文件系统。

默认禁止：

- 未确认就克隆、安装、下载模型或运行脚本。
- 未确认就启用 GUI 自动化、截图、点击或输入。
- 操作真实账号、付款、上传、删除、提交表单、发送消息或修改设置。
- 让 Mano-P 读取 `.obsidian/`、密钥目录、浏览器密码、SSH key、token 或 GitHub 设置。
- 将 PoC 截图、日志、模型输出或敏感路径提交到远端仓库。

## 8. PoC 前置条件

进入 PoC 前必须完成：

- 安全部确认权限、隐私、外发和安装边界。
- 工程部完成只读复用检查和依赖清单。
- GUI 自动化部定义低风险测试场景和停止条件。
- 记忆部提供 PoC 行动记忆模板。
- 技能优化部维护 PoC checklist 和后续 skill 草案入口。
- 用户确认是否允许克隆、安装、下载模型、启用 GUI 权限或执行桌面动作。

## 9. 推荐 PoC 形态

第一阶段：只读研究

- 读取 README、LICENSE、安装说明、examples 和 issues。
- 不克隆、不安装、不运行。
- 产出复用检查和风险边界。

第二阶段：隔离安装验证

- 仅在独立目录、临时环境或独立测试用户中进行。
- 不接触真实账号、私密文档、Obsidian 配置或 GitHub 设置。
- 默认禁止 cloud mode。

第三阶段：沙盒 GUI 验证

- 只操作本地静态 HTML 页面或低风险沙盒窗口。
- 第一轮只观察和生成拟执行动作，不点击。
- 第二轮必须由用户确认后，才允许一次可回退动作。

## 10. 下一步

本参考文档对应的下一步是：

```text
AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
```

在 checklist 通过前，不应把 Mano-P 加入主仓库依赖、submodule、adapter 或自动执行链路。
