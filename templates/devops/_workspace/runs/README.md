# Runs

Run state and run history for this workspace.

- `active/`: current in-progress workflow or pipeline runs
- `archive/`: completed runs kept for history
- `run-template.md`: template for a run's `RUN.md`

Use runs for non-trivial workflows, anything resumable/auditable, and all pipelines. Every run must have `RUN.md`.

`RUN.md` is the plan/control surface for every run. Use a user-provided run path/slug, or ask before creating a new run. Do not guess the active run. If a run exists, write or update `RUN.md` before work with the request, assumptions, plan, current step, expected outputs, and open questions. Do not leave the plan only in chat/model context.

Workflow runs use `input/`, `output/`, and `final/`.
Pipeline runs use `input/`, `stages/`, and `final/`.

Promotion rules:

- final durable artifacts -> `_workspace/outputs/`
- open follow-ups, unresolved questions, risks, TODOs -> `_workspace/backlog/items/`
- reviewed stable facts -> `_workspace/context/project/`

Do not store run state inside `_workspace/pipelines/`.
