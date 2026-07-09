# Architecture

This file is repository-specific and should be generated/updated during bootstrap.

The kit repo carries no root `AGENTS.md` or `CLAUDE.md`. It is a source of templates and docs, not a workspace. The reusable agent-in-workspace policy ships in `templates/*/AGENTS.md`; the system and methodology are documented in `docs/`. When you work on the kit itself, you do so inside a workspace you created from a template — that workspace's `AGENTS.md` provides the operating policy.

## Repository Map

- `docs/`: the whole system and methodology — grouped into `concepts/` (the model), `authoring/` (workflows, pipelines, template selection, run/safety rules), and `maintenance/` (kit upkeep and bootstrap).
- `templates/`: portable workspace templates, each with its own `AGENTS.md` (the shipped policy). Ships `minimal` and the reusable staged `pipeline` scaffold; extend `minimal` locally for larger domain-specific templates.
- `scripts/`: kit-level initialization and registry scripts.
- `.opencode/AGENTS.md`: global OpenCode shim linked by `setup.sh` — stays tiny and defers to the nearest project `AGENTS.md`.
- `.opencode/`: optional OpenCode runtime adapter, model-agnostic Manual/Auto/Plan prompts, skills, generated config sources, and scripts.
- `README.md`: what the kit is and how to use it. The kit repo carries no root `CLAUDE.md` either — Claude reads `README.md` and `docs/`, plus the enclosing workspace's `AGENTS.md`/`CLAUDE.md` when present.

## Boundaries

- Workflow state belongs in target project/vault `_workspace/` folders and Markdown files.
- Each template's `AGENTS.md` owns portable routing, context, run, process, lifecycle, and safety policy for the workspaces it creates.
- `docs/` owns the explanation of the system; templates carry the enforceable policy; neither restates the other beyond a pointer.
- OpenCode config owns only runtime permissions, model/provider settings, and control-mode prompts.
- In a target workspace, Claude compatibility is a pointer file (`CLAUDE.md`) that defers to that workspace's `AGENTS.md`. The kit repo itself has neither.
- Skills provide reusable task knowledge only when requested by a workflow or user request.
- Runbooks inside templates own known commands and validation procedures for target workspaces.
- Templates provide starting layouts and should stay smaller than the full kit.

## Documentation ownership

- `ARCHITECTURE.md`: this file — repository layout, ownership boundaries, key flows, contracts.
- `docs/concepts/`: the model, workspace shape, and methodology.
- `docs/authoring/`: how to write workflows and pipelines; run and safety rules.
- `docs/maintenance/`: how to maintain and bootstrap the kit.
- `templates/`: the reusable project/vault/artifact policy and layouts.
- `.opencode/skills/`: active skills and loading instructions.

When architecture, commands, or routing change, update the corresponding doc.

## Key Flows

1. User asks to work on the kit — templates, OpenCode config, skills, docs, or framework maintenance.
2. The runtime reads the enclosing workspace's `AGENTS.md`, then the routed kit docs, templates, scripts, configuration, and context.
3. It establishes a standalone task, workflow, or pipeline run in that workspace when required.
4. It follows the active runtime control mode while preserving safety and lifecycle gates.

## Critical Contracts

- OpenCode config lives in `.opencode/opencode.json` and is generated from `.opencode/config/base.json` plus permission fragments.
- OpenCode primary control modes are Manual, Auto, and Plan; all are model-agnostic and disable delegation.
- Bash permissions use explicit deny/ask guards, read-only allowlists, focused local validation allowlists, and ask gates for broad compound, pipe, and redirection forms.
- Run process types are standalone `task`, one-pass `workflow`, and staged `pipeline`.
- A run stays active through review; explicit finish creates its final and durable output, while archive remains separate.
