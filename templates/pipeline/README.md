# Pipeline Template

Use this template when a task is sequential, reviewable, and repeatable.

Pipelines are process definitions. They do not store run state. All run input, stage output, and final run history lives in the parent workspace:

```text
_workspace/runs/
  active/
  archive/
```

## When to create a pipeline

Use a pipeline when:

- stage 2 depends on stage 1 output
- a human should review each stage before the next stage runs
- the same process will run more than once

Use a workflow for one-pass work.

## Folder structure

```text
pipeline-name/
├── CONTEXT.md
├── README.md
├── setup/
│   └── questionnaire.md
├── _config/
├── shared/
└── stages/
    ├── 00_intake/
    │   ├── CONTEXT.md
    │   └── references/
    ├── 01_process/
    │   ├── CONTEXT.md
    │   └── references/
    └── 02_finalize/
        ├── CONTEXT.md
        └── references/
```

Run files live outside the pipeline definition:

```text
_workspace/runs/active/YYYY-MM-DD-topic-slug/
├── RUN.md
├── input/
├── stages/
│   ├── 00_intake.md
│   ├── 01_process.md
│   └── 02_finalize.md
└── final/
```

After approval, move the active run to:

```text
_workspace/runs/archive/YYYY-MM-DD-topic-slug/
```

## Layer model

| Layer | What it is | Where it lives |
|---|---|---|
| Layer 0 | Identity and safety | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | `CONTEXT.md` |
| Layer 2 | Stage contracts | `stages/*/CONTEXT.md` |
| Layer 3 | Stable reference/config | `_config/`, `shared/`, `stages/*/references/` |
| Layer 4 | Per-run working artifacts | `_workspace/runs/active/<run-slug>/` |

## How to run a pipeline

1. Use a user-provided run path/slug, or ask before creating a new run under `_workspace/runs/active/YYYY-MM-DD-topic-slug/`. Do not guess the active run.
2. Write or update that run's `RUN.md` with the request, assumptions, plan, current stage, expected output, and open questions.
3. Put source material in that run's `input/` folder.
4. Run one stage.
5. Before stage work, update `RUN.md` with the stage plan and expected output.
6. The agent writes the stage artifact under the run's `stages/` folder and stops.
7. Review/edit the stage artifact.
8. Tell the agent to run the next stage.
9. After final approval, ask before moving the active run to `archive/`.

Never say "run the whole pipeline". Run one stage at a time.

## Promotion rules

At the end of a run:

- final plans/reviews/validations/handoffs go to `_workspace/outputs/`
- deferred follow-ups and unresolved actions go to `_workspace/backlog/items/`
- reviewed stable project facts go to `_workspace/context/project/`
- full run history goes to `_workspace/runs/archive/`
