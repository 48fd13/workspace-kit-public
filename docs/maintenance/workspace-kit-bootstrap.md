# Workspace Kit Bootstrap and Repair

Use this runbook when creating, rebuilding, installing, renaming, or repairing the `workspace-kit` repository or its optional runtime adapters.

This is the canonical cross-tool procedure. OpenCode skills may point here, but this file should remain usable by Claude and other tools that can read normal Markdown.

## Goal

Create a small, portable workspace kit that provides:

- model-agnostic OpenCode Manual, Auto, and Plan primary control modes
- global OpenCode config and skills
- reusable templates for target folders
- validation scripts
- a tiny global `AGENTS.md` shim, with detailed behavior kept local to projects

## What the kit is

The kit is a control-plane asset: the source you initialize per-project workspaces *from*. It is not applied to your work by itself, and it is not copied wholesale into every project.

```text
workspace-kit/                the reusable kit (this repo)
target project workspace/     local AGENTS.md + _workspace/ when useful
target project workspace/repo/ project code/repository files
```

## Scope boundaries

This runbook is for the kit itself and its OpenCode adapter:

- the `workspace-kit/` repository
- `~/.config/opencode/` symlinks to the kit

Do not use it for application code changes or ordinary repo setup. For target repos/folders, use the project bootstrap flow and `scripts/init-workspace.py` templates instead.

## Required kit shape

The kit repo has no root `AGENTS.md` or `CLAUDE.md` — it is a source of templates and docs, not a workspace.

```text
workspace-kit/
├── README.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── VERSION
├── .opencode/
│   ├── opencode.json
│   ├── AGENTS.md
│   ├── agents/
│   │   ├── manual.md
│   │   ├── auto.md
│   │   └── plan.md
│   ├── skills/
│   ├── config/
│   └── scripts/
├── templates/
│   ├── minimal/
│   ├── pipeline/
│   └── (optional local-only templates, e.g. development/, devops/ — not published)
├── scripts/
│   ├── init-workspace.py
│   ├── workspaces.py
│   └── export-public.py
├── docs/
└── archive/
```

## Invariants

- Keep Manual, Auto, and Plan as model-agnostic primary modes.
- Keep routing, context, run, process, lifecycle, and safety policy in the nearest workspace `AGENTS.md`, not mode prompts.
- Keep workflow control in Markdown docs, runbooks, templates, checklists, and `_workspace/runs/` state.
- Keep global instructions minimal. Put detailed behavior in local `AGENTS.md`, `_workspace/`, docs, templates, runbooks, or skills.
- Skills are optional reusable knowledge. They are not the canonical cross-tool source for kit reconstruction.

## Global OpenCode shim

`.opencode/AGENTS.md` should stay short because it is loaded broadly.

Recommended shape:

```md
# Runtime Bootstrap

Read and follow the nearest project `AGENTS.md`.

Do not create `_workspace/` or project workflow files unless the user asks.

Ask before destructive, machine-wide, deploy/publish, dependency,
infrastructure, secret/auth, billing/payment, or irreversible data operations.

Do not hardcode secrets. Do not commit unless explicitly asked.
```

## Global symlink policy

Global OpenCode files may point at the kit:

```text
~/.config/opencode/opencode.json -> ~/workspace/workspace-kit/.opencode/opencode.json
~/.config/opencode/agents       -> ~/workspace/workspace-kit/.opencode/agents
~/.config/opencode/skills       -> ~/workspace/workspace-kit/.opencode/skills
~/.config/opencode/config       -> ~/workspace/workspace-kit/.opencode/config
~/.config/opencode/scripts      -> ~/workspace/workspace-kit/.opencode/scripts
~/.config/opencode/AGENTS.md    -> ~/workspace/workspace-kit/.opencode/AGENTS.md
```

Always ask before applying machine-wide symlink changes.

## Bootstrap or repair workflow

1. Confirm the intended kit path.
2. Check the existing kit shape against the layout above.
3. Create or repair the required kit shape.
4. Keep `.opencode/agents/` to model-agnostic Manual, Auto, and Plan primary-mode prompts.
5. Keep `.opencode/AGENTS.md` as a tiny fallback shim.
6. Before changing `~/.config/opencode`, run setup in dry-run mode and ask for approval:

   ```sh
   ./setup.sh --dry-run
   ```

7. After approval, repair global symlinks:

   ```sh
   ./setup.sh
   ```

8. Validate with the smallest relevant checks.

## Validation

Run from the kit root:

```sh
python3 -m py_compile scripts/init-workspace.py scripts/workspaces.py scripts/export-public.py
python3 .opencode/scripts/build-config.py
```

Then review the `.opencode/opencode.json` diff for unintended permission changes, and keep `scripts/export-public.py`'s `DIRECTORIES` limited to `templates/minimal` and `templates/pipeline`.

If global links changed, verify their targets and tell the user to restart OpenCode.

## Guardrails

- Ask before machine-wide config changes, destructive cleanup, installs, commits, push/publish/deploy, or infrastructure mutation.
- Do not hardcode secrets or credentials.
- Do not create project-local `_workspace/` files unless the user asked for project initialization.
- Do not put large process docs in global `AGENTS.md`.

## Handoff

Return:

1. kit path
2. global symlink changes, if any
3. files added or changed
4. validation commands and results
5. restart reminder for OpenCode config changes
