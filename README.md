# Workspace Kit

A reusable OpenCode/Claude workspace kit based on folders, Markdown workflows, runbooks, centralized runs, staged outputs, and one active `general` agent.

The goal is simple: keep orchestration in files humans can read and edit.

## What it provides

- OpenCode guardrails and a single `general` agent
- reusable workspace templates
- one-shot workflows for common work
- staged pipelines for human-reviewed multi-step work
- centralized run state under `_workspace/runs/`
- scripts to initialize and verify workspaces
- compatible `AGENTS.md` and `CLAUDE.md` instructions

## Templates

| Template | Use for |
|---|---|
| `minimal` | small repos, notes, lightweight projects |
| `development` | software/backend/cloud repos with reviews and validation |
| `devops` | DevOps/cloud/platform work, infra reviews, incidents, readiness, CI/CD |
| `pipeline` | reusable staged workflow pattern copied into `_workspace/pipelines/` |

## Quick start

Initialize a workspace:

```sh
python3 scripts/init-workspace.py --template development /path/to/project
```

Verify it:

```sh
python3 scripts/verify-workspace.py /path/to/project
```

Install the OpenCode config globally:

```sh
./setup.sh
```

Then restart OpenCode.

## How the workflow works

1. Read the nearest `AGENTS.md`.
2. If present, read `_workspace/map/routing-table.md`.
3. Select the matching workflow or pipeline.
4. Read only the required context/runbooks.
5. For work/change/review/plan/validation/handoff tasks, use a run under `_workspace/runs/active/<run-slug>/` unless the user explicitly says to skip run state.
6. Save final durable plans, reviews, validations, or handoffs under `_workspace/outputs/`.

Quick Q&A, status checks, and clarification questions can stay chat-only. Work/change/review/plan/validation/handoff tasks use a run by default unless the user explicitly says to skip run state. The user must provide a run path/slug, or the agent must ask before creating one. Agents must not guess the active run.

## Runs

Every run has a `RUN.md` control file. It records:

- request
- assumptions
- plan
- current step
- expected outputs
- open questions

Workflow runs use:

```text
_workspace/runs/active/<run-slug>/
├── RUN.md
├── input/
├── output/
└── final/
```

Pipeline runs use:

```text
_workspace/runs/active/<run-slug>/
├── RUN.md
├── input/
├── stages/
└── final/
```

Use workflows for one-pass tasks. Use pipelines when each stage needs human review before the next stage runs. Pipeline definitions live under `_workspace/pipelines/`; run state lives under `_workspace/runs/`.

## Outputs, backlog, and context

- Final durable artifacts go to `_workspace/outputs/`.
- Deferred follow-ups, risks, TODOs, and unresolved questions go to `_workspace/backlog/items/`.
- Template-provided reference material goes to `_workspace/context/reference/`.
- Reviewed stable project facts go to `_workspace/context/project/`.

## OpenCode safety model

- one active agent: `general`
- explicit ask gates for risky commands
- stop before destructive, deploy, publish, infrastructure, auth/secrets, billing, or irreversible data operations
- review/security/performance work is handled by checklists and workflows, not separate agents

## Docs

- `docs/template-selection.md` — choose a template
- `docs/folder-workflow-system-primer.md` — system overview
- `docs/mwp-compatibility.md` — mapping to MWP concepts
- `docs/kit-maintenance.md` — maintenance commands

## Attribution

Inspired by **Model Workspace Protocol (MWP)** from Jake Van Clief and David McDermott, described in *Interpretable Context Methodology: Folder Structure as Agentic Architecture*:

- <https://arxiv.org/abs/2603.16021>
- <https://doi.org/10.48550/arXiv.2603.16021>

Related MWP repository: <https://github.com/RinDig/Model-Workspace-Protocol-MWP>
