---
type: gui_python_source_review
project_id: mano-p
date: 2026-06-17
owner_department: GUI 自动化部
status: completed
risk_level: high
current_mode: 坤-坎-兑
related_formula_review:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Formula_Dependency_Review.md
related_execution_checklist:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
related_install_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
related_runtime_gate_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Runtime_Gate_Plan.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-46_gui-自动化部_mano-p-python-source-review.md
requires_user_confirmation_for_next_step: true
---

# Mano-P Stage 1 Python Source Review

## 1. 执行边界

用户已确认继续执行上一轮建议。本轮只读审查 Python requirements、entrypoint 和安全相关 source。

本轮执行了：

- 只读定位已安装 artifact 中的 `visual` source。
- 只读读取 Homebrew cache tarball 中的 `requirements.txt`。
- 只读读取 `visual/vla.py`、`visual/config/*`、`visual/agents/*`、`visual/computer/*`、`visual/model/task_model.py`。
- 只读取 `$HOME/.mano/config.json` 的顶层键名，不读取或记录配置值。
- 只读读取已安装 venv 的 package metadata 摘要。

本轮未执行：

- `mano-cua --help`
- `mano-cua check`
- `mano-cua run`
- `mano-cua install-sdk`
- `mano-cua install-model`
- `mano-cua config`
- `brew install/tap/update/upgrade/reinstall`
- Python package install
- SDK/model/binary/skill 下载
- 权限授权
- 截图、点击、输入或 GUI 自动化
- cloud mode

## 2. Requirements 结果

`requirements.txt` 未在 installed `visual` source 目录中保留，但存在于 Homebrew cache tarball。

文件内容：

```text
customtkinter
mss
pynput
requests
```

判断：

- 依赖未 pin 版本。
- 依赖未记录 hash。
- 未来 reinstall 可能解析到不同版本。
- 当前已安装 venv 的结果只能代表本机当前状态，不能代表可复现安装锁定。

当前 venv 中观察到的主要 installed packages：

| Package | Version | Observed license field |
| --- | --- | --- |
| `customtkinter` | 5.2.2 | Creative Commons Zero v1.0 Universal; classifier also says MIT |
| `mss` | 10.2.0 | MIT License |
| `pynput` | 1.8.2 | LGPLv3 |
| `requests` | 2.34.2 | Apache-2.0 |
| `pyobjc-core` | 12.2 | present as transitive dependency |
| `pyobjc-framework-ApplicationServices` | 12.2 | present as transitive dependency |
| `pyobjc-framework-Quartz` | 12.2 | present as transitive dependency |
| `pyobjc-framework-Cocoa` | 12.2 | present as transitive dependency |

Other observed transitive packages include `certifi`, `charset_normalizer`, `darkdetect`, `idna`, `packaging`, `six`, and `urllib3`.

License note:

- `pynput` is LGPLv3 and should be reviewed by engineering/legal before redistribution or vendoring.
- The `customtkinter` metadata has mixed license signals and needs confirmation from upstream before redistribution.

## 3. Entrypoint Findings

### 3.1 Default `run` path uses cloud mode

`mano-cua run` defaults to cloud mode unless `--local` is supplied.

Observed cloud behavior:

- Creates or reads a local device id.
- Sends task data to `https://mano.mininglamp.com`.
- Session creation body includes task text, device id, platform, optional expected result, and by default a `bash` capability unless `disable-bash` is set to `true`.
- Later step calls poll the cloud session endpoint for reasoning/actions.
- Close/stop/continue actions also call cloud endpoints.

Decision:

- Cloud mode remains prohibited.
- Running `mano-cua run` is not allowed.
- Even a sandbox task must wait for a separate explicit cloud/local decision.

### 3.2 `run` can open apps and URLs before automation starts

`run_task` supports `--app` and `--url`.

Observed behavior:

- On macOS, app launch uses `open -a`.
- URL launch uses the default browser.
- Windows/Linux have equivalent launch paths.

Decision:

- `--app` and `--url` must remain prohibited until GUI sandbox scope is approved.

### 3.3 `--local` avoids cloud inference but still takes screenshots and controls GUI

Local mode uses `LocalAgent`.

Observed behavior:

- Requires a local model path.
- Lazy-loads `mlx_vlm`, `vlm_service`, and optional `cider`.
- Takes screenshots via `mss`.
- Builds prompts containing screenshot images.
- Converts model output to actions such as click, type, hotkey, scroll, drag, open app, open URL, bash, finish, fail, and call user.
- Saves raw local model responses to `$HOME/.mano/raw_responses.jsonl`.

Decision:

- Local mode still requires Screen Recording and GUI-control risk review.
- Local mode is not authorized.

### 3.4 Runtime executor can perform high-impact actions

`ComputerActionExecutor` can:

- Capture screen data through `mss`.
- Move/click/scroll mouse through `pynput`.
- Type text and press hotkeys through `pynput`.
- Paste text through clipboard utilities such as `pbcopy` on macOS.
- Open apps and URLs.
- Move windows via `osascript` on macOS.
- Run shell commands through a `bash` tool path.

Decision:

- No runtime command should be allowed until a strict runtime gate disables or constrains bash, app/url launch, clipboard mutation, screenshots, and physical input.

### 3.5 Task loop captures screenshots after actions

`TaskModel` executes model actions and then captures a screenshot after the last action in each step.

Observed behavior:

- Initializes `ComputerActionExecutor`.
- Calls `agent.predict`.
- Executes actions.
- Captures screenshot bytes after actions.
- Optional `save-trajectory=true` stores screenshots, history, metadata, and final screenshots under `$HOME/.mano/trajectory/...`.

Decision:

- The `save-trajectory` config must remain `false` for any future test unless a separate local-only logging boundary is approved.
- Screenshot capture must remain prohibited until Screen Recording and test-window scope are approved.

## 4. Config Findings

`$HOME/.mano/config.json` exists on this machine.

Only top-level keys were read:

- `default-model-path`
- `model-installed`
- `python-path`
- `sdk-installed`

Values were not read or recorded.

Risk:

- Runtime may be influenced by local `python-path` and `default-model-path`.
- `check`, `config --set`, local mode, SDK install, and model install can read or write this config.

Decision:

- Any future runtime test should use a clean temporary `HOME` unless the user explicitly authorizes reading config values.
- Do not commit config values.

## 5. Subcommand Risk Table

| Command | Source-level risk | Current decision |
| --- | --- | --- |
| `mano-cua --help` | Likely low runtime surface, but still executes entrypoint imports | Not allowed yet; needs runtime gate confirmation |
| `mano-cua config --list` | Prints config values from `$HOME/.mano/config.json` | Prohibited |
| `mano-cua config --get/--set` | Reads/writes config; `--set` can run validation subprocesses | Prohibited |
| `mano-cua check` | Runs subprocess imports and can write config flags | Prohibited |
| `mano-cua install-sdk` | Creates venv, pip installs dependencies, installs `cider` from GitHub, writes config | Prohibited |
| `mano-cua install-model` | Probes network and downloads from HuggingFace or modelscope.cn | Prohibited |
| `mano-cua stop` | Writes `~/.mano/stop.flag` and calls cloud stop endpoint | Prohibited unless an active approved test session exists |
| `mano-cua run` | Cloud by default; can screenshot, open app/url, execute GUI actions, use bash | Prohibited |

## 6. Current Decision

Stage 1 should not proceed directly to runtime.

The next safe step was not to run `mano-cua`. The next safe step was to write a runtime gate plan, and that plan is now recorded.

Minimum runtime gate plan should define:

- Clean `HOME` directory.
- No cloud mode.
- No real app or URL target.
- No real account, browser session, Obsidian settings, GitHub settings, payments, uploads, or messages.
- Bash capability disabled or blocked.
- `save-trajectory=false`.
- No clipboard mutation.
- No mouse/keyboard action until sandbox GUI scope is approved.
- Exact command allowlist and stop conditions.

Potential first runtime candidate after a gate is approved:

```text
mano-cua --help
```

But this command is still not authorized by this report.
