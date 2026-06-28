# Stage 04: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_relationships.md` | Reviewed relationship map |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_questions.md` | Reviewed questions |
| Layer 3 reference | `references/` | Final output rules |

## Do NOT load

- unrelated raw input unless needed for unresolved gaps

## Process

1. Create final onboarding map, open questions, risks, and next actions.
2. Convert each deferred follow-up, unresolved question, risk to revisit, or next action that should survive the pipeline into a backlog item under `_workspace/backlog/items/`.
3. Keep durable facts/maps in `_workspace/context/project/` only after they are reviewed; do not store unresolved questions, risks, or TODOs there.
4. Follow pipeline-level archive rule after approval.

## Outputs

Write `04_finalize.md` to `_workspace/runs/active/<run-slug>/stages/` containing the final onboarding map, open questions, risks, and next actions.

Also write backlog items to `_workspace/backlog/items/YYYY-MM-DD-short-slug.md` for unresolved questions, risks, and deferred next actions that need tracking after the pipeline ends. Include a source link back to this pipeline/stage output in each backlog item.


## Promotion

After writing the stage handoff:

- Promote final reviewed artifacts to `_workspace/outputs/` when they should be used outside the run.
- Promote deferred follow-ups, unresolved questions, risks to revisit, TODOs, and next actions to `_workspace/backlog/items/`.
- Promote reviewed stable project facts to `_workspace/context/project/`.
- Keep full run history in `_workspace/runs/active/<run-slug>/` until the user approves archiving it to `_workspace/runs/archive/<run-slug>/`.

## Review gate

Stop for final review.
