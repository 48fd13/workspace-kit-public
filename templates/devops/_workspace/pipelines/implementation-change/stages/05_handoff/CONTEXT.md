# Stage 05: Handoff

## Goal

Produce the final implementation handoff for human review, follow-up, or PR preparation.

## Inputs

- All previous stage outputs
- Final changed files and validation results
- Any unresolved questions or risks

## Process

1. Summarize what changed and why.
2. List validation status and any skipped checks.
3. Capture risks, follow-ups, and rollback notes.
4. Recommend next human action: review, commit, PR, rerun validation, or revise plan.
5. Ask before archiving run outputs under `_workspace/runs/archive/` or clearing active folders.

## Outputs

Write `05_handoff.md` under `_workspace/runs/active/<run-slug>/stages/` containing:

- change summary
- files changed
- validation summary
- known risks/follow-ups
- rollback/revert notes
- next action


## Promotion

After writing the stage handoff:

- Promote final reviewed artifacts to `_workspace/outputs/` when they should be used outside the run.
- Promote deferred follow-ups, unresolved questions, risks to revisit, TODOs, and next actions to `_workspace/backlog/items/`.
- Promote reviewed stable project facts to `_workspace/context/project/`.
- Keep full run history in `_workspace/runs/active/<run-slug>/` until the user approves archiving it to `_workspace/runs/archive/<run-slug>/`.

## Review gate

Stop after writing the active run stage file. Do not commit, push, deploy, archive, or clear active outputs without explicit approval.
