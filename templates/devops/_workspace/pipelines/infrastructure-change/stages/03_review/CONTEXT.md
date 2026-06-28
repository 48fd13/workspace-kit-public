# Stage 03: Review

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_plan.md` | Reviewed plan |
| Layer 3 reference | `references/` | Risk review rules |

## Do NOT load

- later stage folders

## Process

1. Review security, reliability, cost, operational, dependency, and rollback risks.
2. Flag unresolved approvals or missing evidence.

## Outputs

Write `03_review.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for risk review.
