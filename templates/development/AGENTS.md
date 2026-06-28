# Agent Guide

Use the local folder workflow system as the control plane.

## Workflow order

1. Read this file.
2. Read `_workspace/map/routing-table.md`.
3. Select the matching workflow.
4. Read only required workflow, runbook, context, and skill files.
5. Answer quick Q&A, status checks, and clarification questions directly; for work/change/review/plan/validation/handoff tasks, use a run by default unless the user explicitly says to skip run state.
6. For non-trivial, risky, or ambiguous work, explain the plan and ask before proceeding.
7. Save plans, validations, reviews, and handoffs under `_workspace/outputs/` when useful.
8. Put deferred follow-ups and open action items in `_workspace/backlog/items/`.

## Run rules

Quick Q&A, status checks, and clarification questions can stay chat-only. Work/change/review/plan/validation/handoff tasks use a run by default unless the user explicitly says to skip run state.

## Workflows

A workflow is a one-shot checklist for a task.

- Use a user-provided run path/slug, or ask before creating one.
- Do not guess the active run.
- Write/update `_workspace/runs/active/YYYY-MM-DD-topic-slug/RUN.md` before work.
- `RUN.md` must include request, assumptions, plan, current step, expected outputs, and open questions.
- Use `input/`, `output/`, and `final/` inside the run.

## Pipelines

A pipeline is a multi-stage folder workflow with review between stages.

- Use a user-provided run path/slug, or ask before creating one.
- Do not guess the active run.
- Write/update `RUN.md` before each stage with the stage plan and expected output.
- Write stage output under `_workspace/runs/active/<run-slug>/stages/`.
- Run one stage, then stop for review.
- Ask before archiving or clearing active run files.

## Durable artifact triggers

Treat plans, reviews, validations, and handoffs as workflow artifacts:

- `handoff`, `handoff this`, `save state`, `preserve this`, `continue later` → `_workspace/outputs/handoffs/`
- `plan`, `write a plan` → `_workspace/outputs/plans/`
- `review`, `audit`, `assess` → `_workspace/outputs/reviews/`
- `validation`, `verify`, `check result` → `_workspace/outputs/validations/`

Do not only reply in chat unless the user asks for chat-only. After writing the artifact, reply with the file path, one-line summary, and next action.

## Safety

Ask before destructive or irreversible operations, installs, push/publish/deploy, infrastructure mutations, secrets/auth changes, billing/funds-flow changes, external API contract changes, or irreversible data operations.

Do not commit unless explicitly asked.
