---
type: gui_help_only_runtime_candidate_package
project_id: mano-p
date: 2026-06-17
owner_department: GUI 自动化部
status: completed
risk_level: high
current_mode: 坤-坎-艮-兑
related_runtime_gate_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Runtime_Gate_Plan.md
related_runtime_gate_review:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-runtime-gate-review_summary.md
related_python_source_review:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_22-08_gui-自动化部_mano-p-help-only-candidate-package.md
requires_user_confirmation_for_next_step: true
---

# Mano-P Stage 1 Help-only Runtime Candidate Package

## 1. Candidate 结论

本文件是 help-only runtime 候选包，不是执行授权。

当前结论：

- `candidate_package_completed`: yes
- `runtime_allowed`: no
- `mano_cua_help_allowed`: no
- `candidate_execution_allowed`: no
- `cloud_mode_allowed`: no
- `local_mode_allowed`: no
- `screenshot_allowed`: no
- `gui_control_allowed`: no
- `permission_grant_allowed`: no
- `config_value_read_allowed`: no
- `full_output_save_allowed`: no

下一步只允许：

```text
让安全部、工程部、记忆部复核 help-only runtime 候选包。
```

仍然禁止：

```text
执行 /opt/homebrew/bin/mano-cua --help
```

## 2. Scope

Candidate class:

```text
help-only
```

唯一未来候选 runtime command：

```text
/opt/homebrew/bin/mano-cua --help
```

本候选包不允许：

- `mano-cua run`
- `mano-cua check`
- `mano-cua config`
- `mano-cua stop`
- `mano-cua install-sdk`
- `mano-cua install-model`
- `mano-cua --local`
- any app/url launch
- any screenshot
- any permission grant
- any cloud session
- any model or SDK download

## 3. Wrapper Path Read-only Verification

本轮只读验证结果：

- exact binary candidate: `/opt/homebrew/bin/mano-cua`
- file type: symbolic link
- symlink target: `../Cellar/mano-cua/1.1.4/bin/mano-cua`
- resolved Homebrew wrapper: `/opt/homebrew/Cellar/mano-cua/1.1.4/bin/mano-cua`

Wrapper content summary:

- It sets `PYTHONPATH` to the installed `visual` source directory.
- It reads `$HOME/.mano/config.json` if the file exists.
- It uses `python-path` from that config if present and valid.
- Otherwise it uses the Homebrew-managed Python venv.

Decision:

- clean HOME is mandatory.
- The future command must not read the real user HOME.
- Wrapper path was read but not executed.

## 4. Clean HOME

Placeholder:

```text
<CLEAN_HOME>
```

Recommended value for future execution:

```text
/private/tmp/esmee-mano-cua-clean-home
```

Future preflight requirements:

- `<CLEAN_HOME>` must be a temporary directory outside the repository.
- `<CLEAN_HOME>` must not be the real user HOME.
- `<CLEAN_HOME>/.mano` should not exist before execution unless explicitly created by the test setup.
- No files from `<CLEAN_HOME>` may be committed.

Expected writes:

- Ideally none.
- If the wrapper or Python entrypoint writes, it must be limited to `<CLEAN_HOME>`.
- Any write outside `<CLEAN_HOME>` is a stop condition.

## 5. Working Directory

Future candidate execution should not run from the repository root.

Recommended placeholder:

```text
<RUN_CWD>
```

Recommended value:

```text
/private/tmp/esmee-mano-cua-help-run
```

Reason:

- Prevent accidental repository writes.
- Keep transient stdout/stderr handling outside the vault.
- Make post-run cleanup review simpler.

## 6. Environment Allowlist

Future execution must use an empty environment with an explicit allowlist.

Allowed environment variables:

```text
HOME=<CLEAN_HOME>
PATH=/opt/homebrew/bin:/usr/bin:/bin
LANG=en_US.UTF-8
LC_ALL=en_US.UTF-8
MANO_RUNTIME_GATE=help-only
```

Disallowed inherited environment:

- token variables
- API keys
- SSH agent variables
- GitHub auth variables
- browser automation variables
- agent shell variables
- real HOME
- model path variables
- SDK path variables

## 7. Timeout Strategy

Do not rely on GNU `timeout`; macOS may not have it.

Future candidate execution must use a timeout wrapper based on a confirmed available runtime.

Preferred timeout wrapper specification:

```text
Use Python standard library subprocess with timeout=10 seconds.
```

Runner behavior, to be implemented only after separate confirmation:

- Start command with the environment allowlist above.
- Set cwd to `<RUN_CWD>`.
- Run exact argv: `["/opt/homebrew/bin/mano-cua", "--help"]`.
- Kill process on timeout.
- Capture stdout/stderr in memory.
- Emit only a redacted summary.
- Exit with the child exit code unless a stop condition is hit.

This package does not create the runner file and does not execute the runner.

## 8. Candidate Command Template

Not authorized for execution.

```text
<PYTHON_TIMEOUT_RUNNER> \
  --timeout 10 \
  --cwd <RUN_CWD> \
  --clean-home <CLEAN_HOME> \
  -- /opt/homebrew/bin/mano-cua --help
```

Runner environment:

```text
HOME=<CLEAN_HOME>
PATH=/opt/homebrew/bin:/usr/bin:/bin
LANG=en_US.UTF-8
LC_ALL=en_US.UTF-8
MANO_RUNTIME_GATE=help-only
```

The candidate package intentionally avoids a copy-paste executable command until the runner itself is reviewed.

## 9. Expected Results

Expected network:

```text
none
```

Expected permissions:

```text
none
```

Expected GUI:

```text
none
```

Expected writes:

```text
none outside <CLEAN_HOME>
```

Expected output:

```text
help/usage text only
```

Expected exit behavior:

```text
exit 0 or nonzero help-related exit only; no session, no cloud, no GUI.
```

## 10. Preflight Checks

Before any future execution, record:

- exact binary exists and is a symlink to the expected Homebrew wrapper.
- wrapper file is readable.
- `<CLEAN_HOME>` path is outside the repository.
- `<RUN_CWD>` path is outside the repository.
- real user HOME config values are not read.
- repository working tree is clean.
- no runtime command has been executed yet.

Allowed preflight command types:

- file metadata read
- symlink target read
- wrapper text read
- repository status read

Forbidden preflight command types:

- executing `/opt/homebrew/bin/mano-cua`
- importing `visual.vla`
- calling Python entrypoint
- creating cloud session
- opening app/url
- creating screenshots
- writing config

## 11. Post-run Verification Checks

If a future separately approved run occurs, immediately verify:

- repository status unchanged.
- no real HOME `.mano` write.
- `<CLEAN_HOME>` writes summarized only by relative path and count.
- no GUI/window/app/browser opened.
- no permission prompt appeared.
- no download/install/model/SDK occurred.
- no cloud/session/network text appeared in output.
- stdout/stderr saved only as redacted summary.
- secret scan found no token-like output.

## 12. Output Redaction

Do not commit full stdout/stderr.

Allowed summary fields:

```text
exit_code:
duration_ms:
stdout_line_count:
stderr_line_count:
contains_usage_text:
contains_network_terms:
contains_permission_terms:
contains_gui_terms:
contains_config_value_like_text:
secret_scan_result:
stop_condition_hit:
```

Forbidden output storage:

- full stdout
- full stderr
- real HOME path
- config values
- device id
- session id
- token-like strings
- stack traces containing private paths

If sensitive output appears:

```text
Record only: sensitive output intercepted.
```

## 13. Stop Conditions

Immediately stop and escalate if any of the following occur:

- timeout.
- network/session/cloud text appears.
- permission prompt appears.
- GUI overlay/window/browser/app appears.
- screenshot-related text appears.
- config value appears.
- write outside `<CLEAN_HOME>` appears.
- real HOME path appears.
- token-like text appears.
- download/install/model/SDK text appears.
- non-help subcommand text appears.
- command attempts fallback to `check`, `config`, `run`, `stop`, `install-sdk`, or `install-model`.

## 14. Action Memory Template

Before future execution, create a new action memory with:

```text
command_class: help-only
exact_binary:
wrapper_target_summary:
clean_home:
run_cwd:
environment_allowlist:
timeout_seconds:
expected_network:
expected_permissions:
expected_gui:
expected_writes:
preflight_result:
user_confirmation:
safety_confirmation:
engineering_confirmation:
memory_confirmation:
actual_exit_code:
actual_duration_ms:
actual_output_summary:
post_run_verification:
secret_scan_result:
stop_condition_hit:
next_step:
```

## 15. Approval Required Before Execution

Required before execution:

- User explicit confirmation.
- 安全部 confirmation.
- 工程部 confirmation.
- 记忆部 confirmation that action memory template is ready.

Until those confirmations exist:

```text
candidate_execution_allowed: no
```
