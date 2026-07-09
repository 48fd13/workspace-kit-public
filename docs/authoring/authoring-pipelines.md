# Authoring Pipelines

How to write a pipeline: a repeatable, sequential, human-reviewed workflow. Applies to `templates/pipeline/` and any pipeline created in a workspace's `_workspace/pipelines/`.

## When to use a pipeline

Use a pipeline when:

- the task has natural stage boundaries
- stage 2 depends on stage 1 output
- human review between stages improves quality
- the same process will run repeatedly with different input
- traceability of intermediate outputs matters

Do not use a pipeline for one-off Q&A, small edits, ad hoc troubleshooting, simple note cleanup, or anything a workflow checklist already covers. See `authoring-workflows.md`.

## Layer model

| Layer | Role | Where it lives |
|---|---|---|
| Layer 0 | Identity and global rules | nearest real workspace/project `AGENTS.md` |
| Layer 1 | Pipeline routing and shared context | pipeline `CONTEXT.md` |
| Layer 2 | Stage contract | `stages/*/CONTEXT.md` |
| Layer 3 | Stable reference material | `_config/`, `shared/`, `stages/*/references/` |
| Layer 4 | Working artifacts | `_workspace/runs/active/<run-slug>/` |

Pipelines do not get a local `AGENTS.md`/`CLAUDE.md` — that would let a template file act as a live instruction file inside the kit repo. Layer 0 is always inherited from the nearest real workspace root; pipeline folders start at Layer 1.

Layer 3 vs Layer 4 is explained in `../concepts/context-model.md` — the same distinction applies inside a pipeline: `_config/`/`shared/`/`references/` are the stable rules, `_workspace/runs/active/<run-slug>/` is the material being processed.

## Folder structure

```text
pipeline-name/
├── CONTEXT.md              Layer 1 routing/shared rules
├── README.md               human-facing overview
├── setup/questionnaire.md  one-time setup questions
├── _config/                Layer 3 shared stable rules
├── shared/                 Layer 3 shared reference material
└── stages/
    ├── 00_intake/
    │   ├── CONTEXT.md      Layer 2 stage contract
    │   └── references/     Layer 3 stage-specific rules
    ├── 01_process/
    │   ├── CONTEXT.md
    │   └── references/
    └── 02_finalize/
        ├── CONTEXT.md
        └── references/
```

A pipeline folder is a process definition only — it holds no run state. All run input, stage output, and final run history live in the enclosing workspace:

```text
_workspace/runs/active/YYYY-MM-DD-topic-slug/
├── RUN.md
├── input/
├── stages/
└── final/
```

Stage names are pipeline-specific — rename `00_intake`/`01_process`/`02_finalize` to whatever the pipeline's real stages are, and add or remove stages as needed. A blank pipeline having 3 stages named `intake`/`process`/`finalize` is a starting scaffold, not a convention every pipeline must follow.

## File roles

| File | Role | Size target |
|---|---|---|
| `CONTEXT.md` | Router — triggers, routing table, load/don't-load table | 25–80 lines |
| `stages/*/CONTEXT.md` | Stage contract — inputs, process, audit, outputs, review gate | 30–100 lines |
| `_config/`, `shared/`, `references/` | Reference material (Layer 3) — stable rules, guidelines, constraints | any |
| `_workspace/runs/active/<run-slug>/` | Working artifacts (Layer 4) — per-run content, changes each run | any |
| `_workspace/runs/archive/<run-slug>/` | Archive for completed approved runs after final review | any |

**`CONTEXT.md` files are routers, not content.** If you find yourself writing actual rules or guidelines in a `CONTEXT.md`, move them to a reference file and add a pointer.

## Stage contracts

A stage contract lives in `stages/<NN_name>/CONTEXT.md` and should define:

- `Purpose` — one sentence, one job.
- `Inputs` — exact Layer 3 and Layer 4 files/folders to load.
- `Do NOT load` — future stages, unrelated references, already-consumed input.
- `Process` — concrete steps.
- `Checkpoints` (optional) — mid-stage review points.
- `Audit` — checks before writing to output.
- `Outputs` — exact file(s) written under `_workspace/runs/active/<run-slug>/stages/`.
- `Review gate` — stop instruction.

The stage output is the handoff. Chat should only summarize and point to the file.

### One-way references

References between stages flow forward only. If stage 03 reads from stage 02 output, stage 02 must not read from stage 03.

```text
Stage 00 → Stage 01 → Stage 02   ✓
Stage 02 → Stage 01               ✗
```

This prevents circular dependencies and keeps each stage independently re-runnable.

### Canonical sources

Every piece of information lives in exactly one file. If the same content appears in two places, one of them should become a pointer to the other.

- Voice rules live in `_config/voice.md` — stages reference it, they do not copy it.
- Stage output is the single source of truth for downstream stages — do not paraphrase it in a later stage's contract.

### Selective section loading

The Inputs table should specify which *section* of a file to load, not just the file:

```markdown
| Layer 3 reference | `_config/voice.md` | "Hard Constraints" section only |
```

Only specify the full file when every section is needed.

### Do NOT load is a hard constraint

The "Do NOT load" section in a stage contract is not a suggestion. It enforces the context window boundary for that stage. An agent that loads future stage folders or already-consumed inputs will degrade in quality.

### Audit before output

Every stage contract should have an Audit table. It runs before writing stage output — the stage's quality gate. If any check fails, fix before saving.

### Checkpoints for creative stages

Use checkpoints inside stages where human direction is valuable mid-stage — before a full draft is written, not after. A checkpoint presents options or a brief for the human to steer, then continues only after confirmation.

### Specs define WHAT, not HOW

When a stage produces a specification for the next stage (an animation spec, a design brief, a technical plan), it defines what the output should be and when things happen — not how to implement it. Leave implementation decisions to the stage that builds.

## Triggers

Every pipeline's `CONTEXT.md` should define at minimum:

- `setup` — run `setup/questionnaire.md` if the pipeline needs one-time configuration; delete the file if it doesn't.
- `status` — inspect `_workspace/runs/active/<run-slug>/stages/`. A stage is COMPLETE if its stage artifact exists, otherwise PENDING. Render a simple diagram. Treat `_workspace/runs/archive/` as completed-run history, not current status.

`setup/questionnaire.md`, when present, asks only system-level questions — things that configure the pipeline permanently, not per-run questions (those are asked conversationally at stage 00). After setup, answers are written into the relevant reference files and never asked again.

## Run lifecycle

1. Establish or continue a run under `_workspace/runs/active/YYYY-MM-DD-topic-slug/`.
2. Set `process: pipeline` in frontmatter and record request, assumptions, plan, current stage, expected output, route/context/process, and open questions.
3. Put source material in the run's `input/` folder.
4. Read pipeline `CONTEXT.md`, then only the active stage's `CONTEXT.md`.
5. Load only the inputs listed for that stage.
6. Write output under `_workspace/runs/active/<run-slug>/stages/`, then stop.
7. The user reviews/edits the stage artifact, then tells the agent to run the next stage.
8. Never say "run the whole pipeline" — one stage at a time, always.
9. Keep the run `active` through all stages and final review.

## Promotion rules

When the user explicitly finishes the run:

- approved content goes under run `final/`
- at least one durable artifact goes to `_workspace/outputs/` and its path is recorded in `RUN.md` frontmatter
- deferred follow-ups and unresolved actions go to `_workspace/backlog/items/`
- reviewed stable facts go to `_workspace/context/project/` (see `../concepts/context-model.md`)
- run status changes to `finished`

Archive is a separate explicit transition: set status to `archived` and move the finished run to `_workspace/runs/archive/` only when the user asks.

## How to create a new pipeline

1. Copy `templates/pipeline/` from the kit root (or `pipeline-template/` inside an initialized workspace's `_workspace/pipelines/`) into `_workspace/pipelines/<pipeline-name>/`.
2. Fill in `CONTEXT.md` — replace `{{Pipeline Name}}`, name the real stages, fill in the routing and context-loading tables.
3. Rename `stages/00_intake/`, `01_process/`, `02_finalize/` to real stage names — add or remove stages as needed.
4. Fill in each stage's `CONTEXT.md` from `stage-contract-template.md`.
5. Delete `setup/questionnaire.md` if the pipeline needs no one-time configuration.
6. Review that every pipeline route, stage folder, input, and handoff path is internally consistent.

`templates/minimal/_workspace/pipelines/workspace-bootstrap/` is a complete worked example — a real 4-stage pipeline, not a blank scaffold. Read it to see every convention above applied.
