# Pipeline: Workspace Bootstrap

Researches an unfamiliar target (new repo, domain, or vault) and produces a working `_workspace/map/` and initial workflows/reference context for it, with review between each step.

## Triggers

| Keyword | Action |
|---|---|
| `status` | Inspect `_workspace/runs/active/<run-slug>/stages/` and report COMPLETE/PENDING for each stage |

## Routing

| Task | Go to |
|---|---|
| Research the target before writing anything | `stages/00_research/CONTEXT.md` |
| Draft the workspace map and routing table | `stages/01_structure/CONTEXT.md` |
| Draft the first workflows and reference context | `stages/02_workflows/CONTEXT.md` |
| Finalize and hand off | `stages/03_finalize/CONTEXT.md` |

## Context loading by stage

| Stage | Load | Do NOT load |
|---|---|---|
| 00_research | active run `input/`, current `_workspace/map/workspace-map.md`, `AGENTS.md` | later stage folders |
| 01_structure | active run stage 00 output, `_config/` | unrelated run files, later stage folders |
| 02_workflows | active run stage 01 output, `_config/`, `stages/02_workflows/references/` | unrelated run files, later stage folders |
| 03_finalize | active run stage 02 output, all prior stage outputs | earlier stage references unless needed |

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
- Prefer read-only discovery (stage 00) before proposing any structural change.
- If the target is already well understood (small repo, already-familiar domain), skip this pipeline and use `_workspace/workflows/workspace-setup.md` instead — say so and ask before skipping.
- Keep the run active through final review. Finish and archive according to the enclosing workspace `AGENTS.md`.
