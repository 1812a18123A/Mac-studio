---
type: gui_formula_dependency_review
project_id: mano-p
date: 2026-06-17
owner_department: GUI 自动化部
status: completed
risk_level: medium
current_mode: 坤-坎-兑
related_execution_checklist:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
related_install_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
related_metadata_result:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Metadata_Query_Result.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-33_gui-自动化部_mano-p-formula-review.md
requires_user_confirmation_for_next_step: true
---

# Mano-P Stage 1 Formula Dependency Review

## 1. 执行边界

用户已确认继续执行上一轮建议。本轮只读审查 Homebrew formula 内容和 dependency metadata。

本轮执行了：

- 读取 `/opt/homebrew/Library/Taps/mininglamp-ai/homebrew-tap/Formula/mano-cua.rb`
- `HOMEBREW_NO_AUTO_UPDATE=1 HOMEBREW_NO_ANALYTICS=1 brew deps --tree mininglamp-ai/tap/mano-cua`
- `HOMEBREW_NO_AUTO_UPDATE=1 HOMEBREW_NO_ANALYTICS=1 brew deps mininglamp-ai/tap/mano-cua`

本轮未执行：

- `brew tap`
- `brew install`
- `brew update`
- `brew upgrade`
- `mano-cua check`
- `mano-cua --help`
- `mano-cua run`
- `mano-cua install-sdk`
- `mano-cua install-model`
- `clawhub install`
- SDK/model/binary/skill 下载
- 权限授权
- 截图、点击、输入或 GUI 自动化
- cloud mode

## 2. Formula 摘要

本地 tap formula 显示：

- Formula class: `ManoCua`
- Description: VLA Desktop Automation Client
- Homepage: `https://github.com/Mininglamp-AI/mano-skill`
- Source archive: `https://github.com/Mininglamp-AI/mano-skill/archive/refs/tags/v1.1.4.tar.gz`
- Version: `1.1.4`
- SHA256: `965ab9f2d9151cf89923214d28f3aad6262af8f00a310b76706deba3fd36f78b`
- Declared Homebrew dependencies: `python@3.13`, `python-tk@3.13`

Formula install behavior:

- Creates a Homebrew-managed Python virtual environment under `libexec/venv`.
- Runs `python3.13 -m venv`.
- Runs `pip install -r requirements.txt`.
- Installs the source `visual` directory into `venv/src`.
- Writes a `mano-cua` shell wrapper into Homebrew `bin`.

Formula runtime wrapper behavior:

- Sets `PYTHONPATH` to the installed `venv/src`.
- Reads `$HOME/.mano/config.json` if it exists.
- Looks for a `python-path` value in that config.
- If `python-path` points to an existing file, it executes that custom Python binary/path against `visual/vla.py`.
- Otherwise it executes the Homebrew venv Python against `visual/vla.py`.

Formula test behavior:

- The Homebrew test invokes `mano-cua --help` and checks for `usage`.
- This test was not run in this review.

## 3. Dependency Metadata

Direct Homebrew dependencies:

- `python@3.13`
- `python-tk@3.13`

Recursive dependency tree summary:

- `python@3.13`
  - `mpdecimal`
  - `openssl@3`
  - `ca-certificates`
  - `sqlite`
  - `readline`
  - `xz`
- `python-tk@3.13`
  - `python@3.13`
  - `tcl-tk`
  - `libtommath`
  - `openssl@3`
  - `ca-certificates`

Flat dependency list:

- `ca-certificates`
- `libtommath`
- `mpdecimal`
- `openssl@3`
- `python-tk@3.13`
- `python@3.13`
- `readline`
- `sqlite`
- `tcl-tk`
- `xz`

Important caveat:

- `brew deps` does not enumerate the Python packages installed by `pip install -r requirements.txt`.
- The true runtime dependency surface is therefore larger than Homebrew's dependency tree.

## 4. Risk Findings

### 4.1 Install-time Python dependencies are not fully audited

The formula uses `pip install -r requirements.txt`. The reviewed formula does not vendor Homebrew `resource` blocks for these Python packages.

Risk:

- Python packages may have been downloaded during the original install.
- Their versions and licenses are not visible from `brew deps`.
- Their hashes are not visible in the formula.
- A future reinstall could perform network access and package resolution unless separately pinned and audited.

Required before any reinstall or distribution decision:

- Read `requirements.txt` from the tagged source or installed artifact if available.
- Record Python package names, versions, licenses, and hashes where possible.
- Decide whether package resolution should be mirrored, pinned, or avoided.

### 4.2 Runtime can be redirected by `$HOME/.mano/config.json`

The wrapper reads `$HOME/.mano/config.json` and honors `python-path` if it points to an existing file.

Risk:

- Future runtime behavior may depend on user-local config outside the Homebrew formula.
- A custom Python path could change the interpreter and execution environment.
- Before running `mano-cua`, this config path must be inspected or explicitly ignored through a controlled environment.

Required before any runtime command:

- Check whether `$HOME/.mano/config.json` exists.
- If it exists, summarize only safe keys and do not commit private values.
- Decide whether to run with a clean temporary `HOME` to avoid user-local config influence.

### 4.3 Formula does not expose cloud/local boundaries

The formula only installs and wraps `visual/vla.py`. It does not by itself state whether a command will use cloud mode, local mode, screenshots, or GUI permissions.

Risk:

- Running even low-looking CLI commands may import or initialize code paths not visible from the formula.
- `mano-cua --help` is still a runtime action and should remain gated until source review.

Required before runtime:

- Read the relevant source entrypoint `visual/vla.py`.
- Identify whether `--help`, `check`, or other commands initialize screenshot, permission, cloud, SDK, or model code.

### 4.4 No formula-level background service found

The formula text reviewed in this step did not show:

- `post_install`
- `caveats`
- `service do`
- launch agent creation
- shell profile modification
- automatic permission request

Interpretation:

- Formula-level risk appears concentrated in the install-time pip dependency resolution and runtime wrapper.
- This does not prove the Python source is safe to run; source review is still required.

## 5. Current Decision

Stage 1 should not proceed to runtime yet.

Recommended next step:

```text
Only inspect Python requirements and source entrypoints.
```

Minimum next read-only scope:

- Tagged source `requirements.txt` or installed equivalent if available.
- `visual/vla.py` entrypoint.
- Any config loading, cloud mode, screenshot, permission, SDK, model, or GUI control modules referenced by the entrypoint.

Still forbidden:

- `mano-cua --help`
- `mano-cua check`
- `mano-cua run`
- `mano-cua install-sdk`
- `mano-cua install-model`
- permission grants
- screenshots
- GUI automation
- cloud mode
- reinstall or cleanup
