# Stage 03: Questions

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_relationships.md` | Reviewed relationships |
| Layer 3 reference | `references/` | Question grouping rules |

## Do NOT load

- later stage folders

## Process

1. Produce targeted questions grouped by owner/team/system/environment/risk.
2. Prioritize questions that unblock safe operations.
3. Mark which questions are backlog candidates if they remain unresolved after finalization.

## Outputs

Write `03_questions.md` to `_workspace/runs/active/<run-slug>/stages/`.

Do not write questions to `_workspace/context/project/`. Final-stage unresolved questions or deferred follow-ups must be promoted to `_workspace/backlog/items/` by Stage 04.

## Review gate

Stop for review before final map.
