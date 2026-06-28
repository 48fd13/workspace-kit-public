# Pipeline: Onboarding Map

## Routing

| Task | Go to |
|---|---|
| Clarify scope | `stages/00_intake/CONTEXT.md` |
| Inventory facts | `stages/01_inventory/CONTEXT.md` |
| Map relationships | `stages/02_relationships/CONTEXT.md` |
| Prepare questions | `stages/03_questions/CONTEXT.md` |
| Finalize map | `stages/04_finalize/CONTEXT.md` |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Identity and global rules | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing and shared context | this file |
| Layer 2 | Stage contract | `stages/*/CONTEXT.md` |
| Layer 3 | Reference material | `_config/`, `shared/`, `stages/*/references/`, selected provider/tool notes |
| Layer 4 | Working artifacts | active run `input/`, `_workspace/runs/active/<run-slug>/stages/` |
| Run archive | Completed approved runs | `_workspace/runs/archive/` |


## Run lifecycle

1. Use a user-provided run path/slug, or ask before creating a new run. Do not guess the active run.
2. Write or update the active run's `RUN.md` with the stage plan and expected output before doing the stage work.
3. Put run-specific source material under the active run's `input/` folder.
4. Write each stage handoff under the active run's `stages/` folder.
5. Promote final durable artifacts to `_workspace/outputs/`, open follow-ups to `_workspace/backlog/items/`, and reviewed stable facts to `_workspace/context/project/`.
6. After final approval, ask before moving the active run to `_workspace/runs/archive/<run-slug>/`.

## Operating rules

- Read-only discovery only.
- Execute one stage at a time and stop for review.
- Keep stage-local working files in `_workspace/runs/active/<run-slug>/stages/`.
- Promote deferred follow-ups, unresolved questions, risks, and next actions that should survive the pipeline into `_workspace/backlog/items/` during the final stage.
- Do not store unresolved risks/questions/TODOs in `_workspace/context/project/`; use project context only for durable facts and reviewed project-specific reference.
- Archive approved completed runs under `_workspace/runs/archive/` and ask before clearing active files.
