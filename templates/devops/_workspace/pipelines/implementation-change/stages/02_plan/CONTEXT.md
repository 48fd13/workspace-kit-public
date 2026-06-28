# Stage 02: Plan

## Goal

Create a small, reviewable implementation plan with validation and rollback expectations.

## Inputs

- `_workspace/runs/active/<run-slug>/stages/00_intake.md`
- `_workspace/runs/active/<run-slug>/stages/01_understand.md`
- Relevant runbooks, tests, and tool notes

## Process

1. Define the smallest useful change.
2. List files expected to change.
3. Define validation commands/checks and expected outcomes.
4. Identify rollback/revert approach.
5. Call out approvals required before implementation or validation.

## Outputs

Write `02_plan.md` under `_workspace/runs/active/<run-slug>/stages/` containing:

- scope
- non-goals
- planned file changes
- implementation steps
- validation plan
- rollback/revert notes
- approval questions

## Review gate

Stop after writing the active run stage file. Wait for approval before implementation.
