# Pipeline: Feature Development

A general-purpose software development pipeline. Language- and framework-agnostic. Apply to any coding task: feature, bug fix, refactor, migration, or integration.

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run `setup/questionnaire.md` to describe the task and project context |
| `status` | Scan `_workspace/runs/active/<run-slug>/stages/` — report COMPLETE (has files) or PENDING per stage |

## Routing

| Task | Go to |
|------|-------|
| Understand the task | `stages/00_understand/CONTEXT.md` |
| Design the solution | `stages/01_design/CONTEXT.md` |
| Implement | `stages/02_implement/CONTEXT.md` |
| Verify | `stages/03_verify/CONTEXT.md` |
| Finalize | `stages/04_finalize/CONTEXT.md` |

## Context loading by stage

| Stage | Load | Do NOT load |
|-------|------|-------------|
| 00_understand | active run `input/`, `_config/` | all `stages/` folders |
| 01_design | active run stage 00_understand output, `_config/`, `shared/` | active run `input/`, stages 02–04 |
| 02_implement | active run stage 01_design output, `_config/`, `shared/` | active run `input/`, stages 00, 03–04 |
| 03_verify | active run stage 02_implement output, active run stage 01_design output, `_config/` | active run `input/`, stages 00, 04 |
| 04_finalize | active run stage 03_verify output, active run stage 01_design output, `_config/` | active run `input/`, stages 00–02 references |

## Layers

| Layer | Purpose | Location |
|-------|---------|----------|
| Layer 0 | Identity and global rules | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing and shared context | this file |
| Layer 2 | Stage contract | `stages/*/CONTEXT.md` |
| Layer 3 | Reference material | `_config/`, `shared/`, `stages/*/references/` |
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

- Execute one stage at a time. Stop after writing output. Do not advance without explicit user instruction.
- Each stage output is the human edit surface. The next stage picks up whatever the human left there.
- Do not reply in chat only. The durable handoff is the file in `_workspace/runs/active/<run-slug>/stages/`.
- Load only what the current stage's Inputs table specifies. Do NOT load columns are hard constraints.
- If the task is simple enough to skip a stage, say so and ask the user before skipping.
- After final approval, ask before moving the active run to `_workspace/runs/archive/<run-slug>/`. Ask before moving, deleting, or clearing active run files.
