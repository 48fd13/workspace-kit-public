# Pipeline: Service Readiness Review

## Routing

| Task | Go to |
|---|---|
| Scope review | `stages/00_scope/CONTEXT.md` |
| Map architecture | `stages/01_architecture/CONTEXT.md` |
| Review operations | `stages/02_operations/CONTEXT.md` |
| Review risk | `stages/03_risk/CONTEXT.md` |
| Finalize readiness | `stages/04_finalize/CONTEXT.md` |

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

- Assess readiness; do not mutate systems.
- Execute one stage at a time and stop for review.
