# Global OpenCode Instructions

Prefer the nearest project `AGENTS.md`.

If `_workspace/map/routing-table.md` exists, use it to find the relevant workflow or pipeline.
Read only task-relevant workflow, runbook, context, and skill files.

Quick Q&A, status checks, and clarification questions can stay chat-only. For work/change/review/plan/validation/handoff tasks, use a run under `_workspace/runs/active/<run-slug>/` by default unless the user explicitly says to skip run state. Use a user-provided run path/slug, or ask before creating a new run. Do not guess the active run. For any run you create or use, write or update `RUN.md` before doing the work. `RUN.md` must include the request, assumptions, plan, current step, expected outputs, and open questions. Workflow runs use `input/`, `output/`, and `final/`; pipeline runs use `input/`, `stages/`, and `final/`. Do not leave the plan only in chat/model context.

When the routing table points to a pipeline: use a user-provided active run path/slug, or ask before creating a new run. Do not guess the active run. Read the pipeline `CONTEXT.md`, then the current stage `CONTEXT.md`. Before running the stage, write/update `RUN.md` with the stage plan and expected output. Execute one stage, write stage output under the active run's `stages/` folder, then stop and wait for the user before proceeding to the next stage. After final approval, ask before moving the active run to `_workspace/runs/archive/`.

Do not create `_workspace/` or project workflow files unless the user asks.

Ask before destructive, machine-wide, deploy/publish, dependency,
infrastructure, secret/auth, billing/payment, or irreversible data operations.

Do not hardcode secrets. Do not commit unless explicitly asked.
