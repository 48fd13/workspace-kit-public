# Stage 03: Implement

## Goal

Apply the approved scoped change without performing external mutations or hidden broad refactors.

## Inputs

- Approved `_workspace/runs/active/<run-slug>/stages/02_plan.md`
- Relevant source/config/script/docs files
- User approval notes, if any

## Process

1. Re-check safety gates before editing.
2. Make only the planned local file changes.
3. Keep changes small and reviewable.
4. Update nearby docs/runbooks when behavior or operation changes.
5. Do not install dependencies, deploy, push, apply infrastructure, mutate clusters/cloud resources, or alter secrets/auth unless explicitly approved.

## Outputs

Write `03_implement.md` under `_workspace/runs/active/<run-slug>/stages/` containing:

- files changed
- implementation summary
- deviations from plan
- risks introduced or reduced
- validation still needed

## Review gate

Stop after writing the active run stage file. Ask for review before validation if implementation deviated from the plan.
