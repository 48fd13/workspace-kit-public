# Authoring Workflows

How to write a workflow: a one-shot checklist for a task type.

## When to use a workflow

Use a workflow for:

- small or medium tasks
- reviews
- validations
- handoffs
- note processing
- code review
- documentation updates
- non-repeatable or lightly repeatable work

Use a pipeline instead when the task has natural stage boundaries where a human should review between stages, or the same multi-step process will run repeatedly with different input. See `authoring-pipelines.md`.

## Shape

A workflow is a short numbered list of steps an agent follows — not prose explaining why the system works the way it does.

```text
_workspace/workflows/<task-name>.md
```

Keep it to what changes agent behavior. If a step is "read `AGENTS.md`," it doesn't need to explain what `AGENTS.md` is — that's assumed context.

Minimal example (`minor-change.md`):

```markdown
# Minor Change Workflow

Use for small, obvious, local, reversible edits.

1. Read only relevant files.
2. Make the smallest useful change.
3. Validate if a safe validation command exists.
4. Summarize changes and validation.
```

Checklist-style example (`code-review.md`):

```markdown
# Code Review Checklist

Findings only unless the user asks for fixes.

Check correctness, edge cases, validation, tests, contracts, and convention drift.

For each finding include issue, why it matters, path/line, and smallest fix.
```

Both examples ship in `templates/minimal/_workspace/workflows/`.

## Run behavior

A workflow run is one persistent execution of a selected checklist. See `rules-and-safety.md` for the shared run lifecycle.

1. Read the selected workflow.
2. Load only the runbooks/context/skills it names.
3. Establish or continue `_workspace/runs/active/<run-slug>/` unless the user explicitly says to skip run state.
4. Set `process: workflow` in `RUN.md` frontmatter and record request, assumptions, plan, current step, expected outputs, route/context/process, and open questions.
5. Put supplied material under `input/` and working output under `output/`.
6. Keep the run `active` through review.
7. On explicit finish, write approved content under `final/`, create and record at least one durable workspace output, then set status to `finished`.
8. Stop for confirmation if a safety gate applies.

## How to add a new workflow to a workspace

1. Decide what recurring task this covers, and add a row for it in `_workspace/map/routing-table.md` pointing at the new file's path.
2. Create `_workspace/workflows/<name>.md` as a short numbered checklist.
3. If the workflow needs stable rules to follow, add them under `_workspace/context/reference/` and reference the file from the workflow or the routing-table row — don't inline long rules into the workflow itself.
4. Review that the routing row resolves to the workflow and every named context/runbook path exists.

The `workspace-setup` workflow and `workspace-bootstrap` pipeline (both in `templates/minimal/_workspace/`) automate this for a whole workspace at once — see `authoring-pipelines.md` for when to reach for the pipeline instead.
