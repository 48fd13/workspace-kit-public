# Workspace Kit Bootstrap and Repair

Use this runbook when creating, rebuilding, installing, renaming, or repairing the machine-level OpenCode/Claude `workspace-kit`, global OpenCode links, or root folder-workflow router.

This is the canonical cross-tool procedure. OpenCode skills may point here, but this file should remain usable by Claude and other tools that can read normal Markdown.

## Goal

Create a small, portable workspace kit that provides:

- one active OpenCode primary agent: `general`
- global OpenCode config and skills
- reusable templates for target folders
- root workspace routing docs
- validation scripts
- a tiny global `AGENTS.md` shim, with detailed behavior kept local to projects

## Workspace model

```text
~/workspace/                 daily machine-level router
~/workspace/workspace-kit/   reusable OpenCode/Claude workspace kit
target repo/folder/vault/    local AGENTS.md + _workspace/ only when useful
```

The kit is a control-plane asset, not an application repo template to copy wholesale into every project.

## Scope boundaries

This runbook is for the kit/control-plane layer:

- `~/workspace/workspace-kit/`
- `~/workspace/AGENTS.md`
- `~/workspace/_workspace/`
- `~/.config/opencode/` symlinks to the kit

Do not use it for application code changes or ordinary repo setup. For target repos/folders, use the project bootstrap flow and `scripts/init-workspace.py` templates instead.

## Required kit shape

```text
workspace-kit/
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── VERSION
├── .opencode/
│   ├── opencode.json
│   ├── AGENTS.md
│   ├── agents/
│   │   └── general.md
│   ├── skills/
│   ├── config/
│   └── scripts/
├── templates/
│   ├── minimal/
│   ├── development/
│   ├── devops/
│   └── pipeline/
├── scripts/
│   ├── init-workspace.py
│   ├── verify-workspace.py
│   ├── workspaces.py
│   └── export-public.py
├── docs/
└── archive/
```

## Root workspace shape

The machine-level router lives outside the kit:

```text
~/workspace/
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── _workspace/
│   ├── map/
│   ├── workflows/
│   ├── runbooks/
│   ├── context/
│   │   ├── reference/
│   │   └── project/
│   ├── backlog/
│   │   └── items/
│   ├── runs/
│   │   ├── active/
│   │   └── archive/
│   └── outputs/
└── workspace-kit/
```

Root workspace docs should route work to the right folder. They should not duplicate the full kit.

## Invariants

- Keep one active executable OpenCode agent: `general`.
- Keep `.opencode/agents/` to active `general.md` only.
- Keep workflow control in Markdown docs, runbooks, templates, checklists, and `_workspace/runs/` state.
- Keep global instructions minimal. Put detailed behavior in local `AGENTS.md`, `_workspace/`, docs, templates, runbooks, or skills.
- Skills are optional reusable knowledge. They are not the canonical cross-tool source for kit reconstruction.

## Global OpenCode shim

`.opencode/AGENTS.md` should stay short because it is loaded broadly.

Recommended shape:

```md
# Global OpenCode Instructions

Prefer the nearest project `AGENTS.md`.

If `_workspace/map/routing-table.md` exists, use it to find the relevant workflow.
Read only task-relevant workflow, runbook, context, and skill files.

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

1. Confirm the intended kit path, normally `~/workspace/workspace-kit`.
2. Check existing local instructions:
   - root `~/workspace/AGENTS.md`
   - root `_workspace/map/routing-table.md`
   - kit `AGENTS.md`
3. Create or repair the required kit shape.
4. Create or repair the root workspace router if the user asked for machine-level workflow setup.
5. Keep `.opencode/agents/` to active `general.md` only.
6. Keep `.opencode/AGENTS.md` as a tiny fallback shim.
7. Before changing `~/.config/opencode`, run setup in dry-run mode and ask for approval:

   ```sh
   ./setup.sh --dry-run
   ```

8. After approval, repair global symlinks:

   ```sh
   ./setup.sh
   ```

9. Validate with the smallest relevant checks.

## Validation

Run from the kit root:

```sh
python3 -m py_compile scripts/init-workspace.py scripts/verify-workspace.py scripts/workspaces.py scripts/export-public.py
python3 verify-opencode-setup.py
python3 scripts/verify-workspace.py templates/minimal
python3 scripts/verify-workspace.py templates/development
python3 scripts/verify-workspace.py templates/devops
python3 scripts/verify-workspace.py templates/pipeline
```

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
