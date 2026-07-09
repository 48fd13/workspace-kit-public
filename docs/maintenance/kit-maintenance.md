# Kit Maintenance

Use this doc when changing the framework kit itself.

## Common tasks

| Task | Where |
|---|---|
| Add a reusable project template | `templates/` |
| Add or update OpenCode skills | `.opencode/skills/` |
| Update OpenCode control-mode prompts | `.opencode/agents/manual.md`, `auto.md`, `plan.md` |
| Update global OpenCode instructions | `.opencode/AGENTS.md` — keep this file as a tiny fallback shim |
| Change runtime permissions | `.opencode/config/permissions/` then regenerate config |
| Update init or registry behavior | `scripts/` |
| Explain framework concepts | `docs/` |
| Author or edit a workflow | `docs/authoring/authoring-workflows.md` — read this first |
| Author or edit a pipeline | `docs/authoring/authoring-pipelines.md` — read this first |
| Decide where new context/rules go | `docs/concepts/context-model.md` |
| Run/safety rules that apply everywhere | `docs/authoring/rules-and-safety.md` |

## Skill routing

Load a skill proactively when a maintenance task matches it.

| Task type | Skill |
|---|---|
| Creating, rebuilding, renaming, or repairing this workspace kit | `workspace-kit-bootstrap` |
| Initializing this workflow in a new or existing repository | `repo-bootstrap` |
| Editing kit docs, templates, or other prose for clarity | `clear-writing` |
| Removing AI-tell phrasing from user-facing prose | `humanizer` |

If a task spans multiple skill areas, load all relevant skills.

## Validation

Run from the kit root to confirm the scripts still parse and the config regenerates cleanly:

```sh
python3 -m py_compile scripts/init-workspace.py scripts/workspaces.py scripts/export-public.py
python3 .opencode/scripts/build-config.py
```

Then review the `.opencode/opencode.json` diff for unintended permission changes.

`templates/pipeline/` is the canonical pipeline scaffold, copied by `init-workspace.py` into every initialized workspace's `_workspace/pipelines/pipeline-template/` — it is not a standalone workspace template and is not selectable with `--template`.

Additional local-only templates may exist outside version control, but never add them to `scripts/export-public.py`'s `DIRECTORIES` list — only `minimal` is published.

To rebuild the sibling public copy:

```sh
python3 scripts/export-public.py ../workspace-kit-public --force
```

## Maintenance rules

- Keep this repo as the reusable kit, applied per project — not a machine-wide router.
- Keep OpenCode mode prompts model-agnostic and limited to mode behavior; routing and lifecycle stay in workspace `AGENTS.md` files.
- Put copyable project state in `templates/`, not in a kit-local `_workspace/`.
- Put explanation in `docs/`. Durable-artifact shapes (plan, review, decision, etc.) are documented in `../authoring/rules-and-safety.md`, not shipped as separate skeleton files — agents generate them inline.
