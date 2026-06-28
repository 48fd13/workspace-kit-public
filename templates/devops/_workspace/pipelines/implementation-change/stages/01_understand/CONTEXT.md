# Stage 01: Understand

## Goal

Map the current behavior and relevant files using minimal read-only discovery.

## Inputs

- `_workspace/runs/active/<run-slug>/stages/00_intake.md`
- Files, logs, diffs, or notes in active run `input/`
- Relevant repo files and runbooks
- Relevant tool/provider notes only when needed

## Process

1. Inspect only the files needed to understand the change path.
2. Identify current behavior, ownership boundaries, and likely impact surface.
3. Find existing tests, validation commands, CI checks, runbooks, or examples.
4. Note dependencies, deployment/runtime coupling, and rollback considerations.
5. Avoid editing in this stage.

## Outputs

Write `01_understand.md` under `_workspace/runs/active/<run-slug>/stages/` containing:

- current behavior summary
- relevant files/components
- impact surface
- validation options
- risks/open questions
- recommendation for planning

## Review gate

Stop after writing the active run stage file. Ask for review if the behavior or ownership is unclear.
