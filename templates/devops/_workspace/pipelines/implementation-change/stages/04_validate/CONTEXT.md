# Stage 04: Validate

## Goal

Run the approved local validation checks and record results clearly.

## Inputs

- `_workspace/runs/active/<run-slug>/stages/02_plan.md`
- `_workspace/runs/active/<run-slug>/stages/03_implement.md`
- Available test/build/lint/check commands
- Changed files

## Process

1. Run only approved/local validation commands.
2. Record exact commands and results.
3. If validation fails, summarize failure and likely next step; do not expand scope silently.
4. If validation cannot run, explain why and list manual checks.
5. Do not deploy, publish, push, or mutate external systems.

## Outputs

Write `04_validate.md` under `_workspace/runs/active/<run-slug>/stages/` containing:

- validation commands run
- pass/fail/not-run status
- key output or error summary
- remaining risk
- recommended next action

## Review gate

Stop after writing the active run stage file. Ask before fixing failed validation if the fix is outside the approved plan.
