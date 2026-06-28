# Routing Table

Quick Q&A, status checks, and clarification questions can stay chat-only. For work/change/review/plan/validation/handoff tasks, use a run by default unless the user explicitly says to skip run state. Use a user-provided run path/slug, or ask before creating a new run. Do not guess the active run. For any run you create or use, write/update `_workspace/runs/active/YYYY-MM-DD-topic-slug/RUN.md` with request, assumptions, plan, current step, expected outputs, and open questions before doing the work. Workflow runs use `input/`, `output/`, and `final/`; pipeline runs use `input/`, `stages/`, and `final/`.

For pipelines, create or select an active run first, then write stage handoffs under that run's `stages/` folder.

| User request | Workflow | Required files |
|---|---|---|
| Small local change | `_workspace/workflows/minor-change.md` | `AGENTS.md`, target files |
| General review | `_workspace/workflows/review/code-review.md` | target files or diff |
| Multi-step task needing review between steps | pipeline in `_workspace/pipelines/` | pipeline `CONTEXT.md`, stage `CONTEXT.md` |
| General Q&A | no workflow required | read only needed files |
