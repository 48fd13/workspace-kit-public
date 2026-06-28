# Stage 04: Validation

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_review.md` | Reviewed risks |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_plan.md` | Plan to validate |
| Layer 3 reference | `references/` | Validation rules |

## Do NOT load

- later stage folders

## Process

1. Define pre-change, change-time, and post-change validation evidence.
2. Mark mutation-gated checks clearly.

## Outputs

Write `04_validation.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for validation review.
