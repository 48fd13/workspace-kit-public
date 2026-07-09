# Workspace Kit

A reusable folder-workspace kit based on portable `AGENTS.md` policy, Markdown routing, persistent runs, one-pass workflows, and human-reviewed pipelines.

The goal is simple: keep orchestration in files humans can read and edit.

## What it provides

- tool-agnostic workspace policy in `AGENTS.md`
- optional OpenCode Manual, Auto, and Plan primary control modes
- reusable workspace templates
- one-shot workflows for common work
- staged pipelines for human-reviewed multi-step work
- centralized run state under `_workspace/runs/`
- scripts to initialize workspaces
- compatible `AGENTS.md` and `CLAUDE.md` instructions

## Templates

| Template | Use for |
|---|---|
| `minimal` | small repos, notes, lightweight projects |
| `pipeline` | reusable staged workflow pattern copied into `_workspace/pipelines/` |

This public kit ships a small, generic starting point. Larger domain-specific templates (e.g. a full software/DevOps workspace) are easy to build on top by extending `minimal` — see `docs/authoring/template-selection.md`.

## Quick start

Initialize a workspace:

```sh
python3 scripts/init-workspace.py --template minimal /path/to/project
```

Install the OpenCode config globally:

```sh
./setup.sh
```

Then restart OpenCode.

## How the workflow works

1. Read the nearest `AGENTS.md`.
2. Read `_workspace/map/routing-table.md`.
3. Load the context and standalone task, workflow, or pipeline selected by the route.
4. Establish or continue the required run.
5. Read only the required context, runbooks, and working files.
6. Keep drafts in the active run until the user explicitly finishes it.
7. On finish, create run-final content plus at least one durable `_workspace/outputs/` artifact.

Quick Q&A, status checks, and clarification questions can stay chat-only. Work/change/review/plan/validation/handoff tasks use a run by default unless the user explicitly says to skip run state. Use a user-provided or clearly continuing run; ask only when several active runs are plausible, otherwise establish a new run.

## Runs

A run is one persistent, human-editable work session. Its process is:

- `task`: standalone work without a reusable process
- `workflow`: one-pass checklist work
- `pipeline`: staged work with human review

Every run has a `RUN.md` control file. It records:

- request
- assumptions
- plan
- current step
- expected outputs
- open questions

Standalone task and workflow runs use:

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

Runs remain `active` through drafting and review. Explicit finish creates approved content under run `final/`, promotes at least one durable workspace output, records its path in `RUN.md` frontmatter, and sets status to `finished`. Archive is a separate explicit transition.

## Workspace layout

Use the workspace root for workflow control files.

- `AGENTS.md`: local agent instructions
- `_workspace/`: workflows, pipelines, runs, outputs, backlog, and context
- `repo/`: project code, repositories, infrastructure manifests, and application files
- `repos/<name>/`: multiple repositories when needed

## Outputs, backlog, and context

- Active drafts stay under the run; finished durable artifacts go to `_workspace/outputs/`.
- Deferred follow-ups, risks, TODOs, and unresolved questions go to `_workspace/backlog/items/`.
- Template-provided reference material goes to `_workspace/context/reference/`.
- Reviewed stable project facts go to `_workspace/context/project/`.

## Runtime adapters

- `AGENTS.md` owns routing, context, run, process, lifecycle, and safety policy.
- OpenCode provides model-agnostic Manual, Auto, and Plan primary modes that all follow the nearest `AGENTS.md`.
- Runtime-specific configuration may control permissions and autonomy but does not redefine the folder methodology.
- All adapters preserve explicit gates for destructive, external, infrastructure, auth/secrets, billing, and irreversible operations.

## Docs

- `docs/concepts/folder-workflow-system-primer.md` — system overview
- `docs/concepts/methodology.md` — the complete model and end-to-end flows
- `docs/authoring/template-selection.md` — choose a template
- `docs/concepts/mwp-compatibility.md` — mapping to MWP concepts
- `docs/maintenance/kit-maintenance.md` — maintenance commands

## Attribution

Inspired by **Model Workspace Protocol (MWP)** from Jake Van Clief and David McDermott, described in *Interpretable Context Methodology: Folder Structure as Agentic Architecture*:

- <https://arxiv.org/abs/2603.16021>
- <https://doi.org/10.48550/arXiv.2603.16021>
