---
type: gui_metadata_query_result
project_id: mano-p
date: 2026-06-17
owner_department: GUI 自动化部
status: completed
risk_level: medium
current_mode: 坤-兑
related_execution_checklist:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
related_install_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-16_gui-自动化部_mano-p-stage-1-metadata-query.md
requires_user_confirmation_for_next_step: true
---

# Mano-P Stage 1 Metadata Query Result

## 1. 执行边界

用户已确认进入 Option B：只查本机和 Homebrew 元数据。

本轮执行了：

- `sw_vers`
- `uname -m`
- `sysctl -n machdep.cpu.brand_string`
- `brew --version`
- `brew info mano-cua`
- `brew search mano-cua`
- `brew tap-info Mininglamp-AI/tap`

本轮未执行：

- `system_profiler SPHardwareDataType`
- `brew tap`
- `brew install`
- `mano-cua check`
- `mano-cua install-sdk`
- `mano-cua install-model`
- `mano-cua run`
- `clawhub install`
- SDK/model/binary/skill 下载
- 权限授权
- 截图、点击、输入或 GUI 自动化
- cloud mode

## 2. 本机基础信息

| 项目 | 结果 |
| --- | --- |
| macOS | 26.5.1 |
| Build | 25F80 |
| 架构 | arm64 |
| CPU | Apple M3 Ultra |
| Homebrew | 6.0.2 |

备注：

- `system_profiler SPHardwareDataType` 未执行，因为它可能输出设备标识。
- `sysctl -n machdep.cpu.brand_string` 首次被沙箱拦截，随后按用户确认范围只读重试成功。

## 3. Homebrew 元数据结果

### 3.1 `brew info mano-cua`

结果摘要：

- Formula: `mininglamp-ai/tap/mano-cua`
- Stable version: `1.1.4`
- Description: VLA Desktop Automation Client
- Upstream: `https://github.com/Mininglamp-AI/mano-skill`
- Formula source: `https://github.com/Mininglamp-AI/homebrew-tap/blob/HEAD/Formula/mano-cua.rb`
- Tap: `mininglamp-ai/tap`
- Installed: yes
- Installed version: `1.1.4`
- Installed files: 2,158
- Installed size: 50.2MB
- Linked: yes
- Direct dependencies: `python@3.13`, `python-tk@3.13`
- Recursive runtime dependencies: installed

重要判断：

- `mano-cua` 已经在本机 Homebrew 中处于 installed/linked 状态。
- 本轮没有执行安装；该状态是查询前已存在的本机状态。
- 由于它已安装，后续风险重点从“是否安装”扩展为“是否允许运行、检查、下载 SDK/model、授权权限或清理”。

### 3.2 `brew search mano-cua`

结果摘要：

- `mininglamp-ai/tap/mano-cua`
- `mininglamp-ai/tap/mano-asr`
- `manus`

判断：

- `mano-cua` 来自 `mininglamp-ai/tap`。
- `mano-asr` 同 tap 存在，但本轮不评估。

### 3.3 `brew tap-info Mininglamp-AI/tap`

结果摘要：

- Tap installed: yes
- Trusted: yes
- Formulae: 3
- Local tap path: `/opt/homebrew/Library/Taps/mininglamp-ai/homebrew-tap`
- Repository: `https://github.com/Mininglamp-AI/homebrew-tap`
- HEAD: `e03152d9737c59ec3f3458f5682cfa12edd0f2d7`
- Last commit: 5 days ago
- Formulae: `mano-afk`, `mano-asr`, `mano-cua`

重要判断：

- `Mininglamp-AI/tap` 已经在本机 Homebrew 中处于 installed/trusted 状态。
- 本轮没有执行 `brew tap`；该状态是查询前已存在的本机状态。
- 后续如果继续，应先审查 tap formula 内容和依赖树，而不是直接运行 `mano-cua`。

## 4. 副作用检查

本轮采取的限制：

- Homebrew 查询使用 `HOMEBREW_NO_AUTO_UPDATE=1`。
- Homebrew 查询使用 `HOMEBREW_NO_ANALYTICS=1`。
- 未执行 tap/install/run/check/download 权限相关命令。

已知副作用：

- Homebrew 元数据查询可能读取已有 tap/formula 缓存。
- 未观察到安装、下载模型、权限弹窗或 GUI 启动。
- 本仓库工作树变化只来自本报告和行动记忆文档。

未知或待复核：

- Homebrew 是否更新了内部查询缓存，未做全局 Homebrew 缓存审计。
- `mano-cua` 何时被安装，非本轮动作，未追溯安装历史。

## 5. 下一步建议

下一步不应运行 `mano-cua`。

推荐最低风险下一步：

```text
审查 Homebrew formula 内容和依赖树，只读读取 formula 文本。
```

进入下一步前需要用户确认：

- 是否允许只读查看 formula 文件内容。
- 是否允许读取 `/opt/homebrew/Library/Taps/mininglamp-ai/homebrew-tap/Formula/mano-cua.rb`。
- 是否允许读取 Homebrew dependency 元数据。

仍然禁止：

- `mano-cua check`
- `mano-cua run`
- `mano-cua install-sdk`
- `mano-cua install-model`
- 权限授权
- GUI 自动化
- cloud mode
- 卸载或清理
