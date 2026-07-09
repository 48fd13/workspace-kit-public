# Pipeline: {{Pipeline Name}}

<!-- Replace {{Pipeline Name}} with a real name and add one sentence describing what this pipeline produces. -->

## Triggers

| Keyword | Action |
|---|---|
| `setup` | Run `setup/questionnaire.md` to configure this pipeline definition |
| `status` | Inspect `_workspace/runs/active/<run-slug>/stages/` and report COMPLETE/PENDING for each stage |

## Routing

| Task | Go to |
|---|---|
| Run stage 00 | `stages/00_stagename/CONTEXT.md` |
| Run stage 01 | `stages/01_stagename/CONTEXT.md` |
| Run stage 02 | `stages/02_stagename/CONTEXT.md` |

## Context loading by stage

| Stage | Load | Do NOT load |
|---|---|---|
| 00_stagename | active run `input/`, `_config/` | later stage folders |
| 01_stagename | active run stage 00 output, `_config/`, `stages/01_stagename/references/` | unrelated run files, later stage folders |
| 02_stagename | active run stage 01 output, `_config/`, `stages/02_stagename/references/` | unrelated run files, earlier stage references unless needed |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Identity and global rules | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing and shared context | this file |
| Layer 2 | Stage contract | `stages/*/CONTEXT.md` |
| Layer 3 | Reference material | `_config/`, `shared/`, `stages/*/references/` |
| Layer 4 | Working artifacts | parent workspace `_workspace/runs/active/<run-slug>/` |
| Run archive | Explicitly archived finished runs | parent workspace `_workspace/runs/archive/` |

## Operating rules

- Execute one stage at a time. Stop after writing output. Do not advance to the next stage without explicit user instruction.
- Before running a stage, write or update `_workspace/runs/active/<run-slug>/RUN.md` with the request, assumptions, stage plan, current step, expected output, and open questions.
- Write stage output under `_workspace/runs/active/<run-slug>/stages/`.
- Each stage output is the human edit surface. The next stage reads whatever the human left there.
- Do not reply in chat only. The durable handoff is the stage file in the active run.
- Load only what the current stage's Inputs table specifies. The "Do NOT load" section is a hard constraint.
- If a stage seems skippable for the current task, say so and ask the user before skipping.
- Keep the run active through final review. Finish and archive according to the enclosing workspace `AGENTS.md`.
