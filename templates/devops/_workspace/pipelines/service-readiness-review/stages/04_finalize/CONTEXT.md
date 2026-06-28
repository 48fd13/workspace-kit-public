# Stage 04: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_operations.md` | Operations review |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_risk.md` | Risk review |
| Layer 3 reference | `references/` | Final report rules |

## Do NOT load

- unrelated raw input unless needed for unresolved gaps

## Process

1. Produce readiness report, prioritized gaps, and recommended next actions.
2. Follow pipeline-level archive rule after approval.

## Outputs

Write `04_finalize.md` to `_workspace/runs/active/<run-slug>/stages/`.


## Promotion

After writing the stage handoff:

- Promote final reviewed artifacts to `_workspace/outputs/` when they should be used outside the run.
- Promote deferred follow-ups, unresolved questions, risks to revisit, TODOs, and next actions to `_workspace/backlog/items/`.
- Promote reviewed stable project facts to `_workspace/context/project/`.
- Keep full run history in `_workspace/runs/active/<run-slug>/` until the user approves archiving it to `_workspace/runs/archive/<run-slug>/`.

## Review gate

Stop for final review.
