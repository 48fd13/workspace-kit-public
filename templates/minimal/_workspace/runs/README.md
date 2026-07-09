# Runs

Persistent, human-editable work state and history for this workspace.

- A run may use `process: task`, `workflow`, or `pipeline`.
- Standalone task and workflow runs use `input/`, `output/`, and `final/`.
- Pipeline runs use `input/`, `stages/`, and `final/`.
- Runs remain `active` through drafting and review.
- Explicit finish creates run-final content and at least one durable `_workspace/outputs/` artifact, then sets status to `finished`.
- Explicit archive later sets status to `archived` and moves the run to `archive/`.

Folders:

- `active/`: active runs plus finished runs awaiting archive
- `archive/`: explicitly archived run history
- `run-template.md`: template for a run's `RUN.md`
