# Stage 05: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_plan.md` | Approved plan |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_review.md` | Risk review |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_validation.md` | Validation plan |
| Layer 3 reference | `references/` | Change packet rules |

## Do NOT load

- unrelated raw input unless needed for unresolved gaps

## Process

1. Produce final change packet for human/team approval.
2. Follow pipeline-level archive rule after approval.

## Outputs

Write `05_finalize.md` to `_workspace/runs/active/<run-slug>/stages/`.


## Promotion

After writing the stage handoff:

- Promote final reviewed artifacts to `_workspace/outputs/` when they should be used outside the run.
- Promote deferred follow-ups, unresolved questions, risks to revisit, TODOs, and next actions to `_workspace/backlog/items/`.
- Promote reviewed stable project facts to `_workspace/context/project/`.
- Keep full run history in `_workspace/runs/active/<run-slug>/` until the user approves archiving it to `_workspace/runs/archive/<run-slug>/`.

## Review gate

Stop for final approval.
