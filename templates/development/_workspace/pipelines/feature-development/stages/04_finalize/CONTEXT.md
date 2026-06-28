# Stage 04: Finalize

Produce the commit message, PR description, documentation updates, and follow-up list. Close the loop on the task.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_verify.md` | Verification results |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_design.md` | What was intended |
| Layer 3 reference | `../../_config/` | Project conventions for commits, PRs, docs |

## Do NOT load

- active run stage 00 output — already incorporated
- active run stage 02 output — verification report covers what matters
- `_workspace/runs/active/<run-slug>/input/` — already consumed

## Process

1. Write a commit message: one subject line (what changed and why, under 72 characters), optional body for non-obvious context. Do not describe what the code does — describe why the change was made.
2. Write a PR description: summary of the change, what was done and why, how to test it, any follow-ups or known limitations.
3. Identify documentation that needs updating: README, API docs, architecture notes, changelogs, runbooks — anything affected by this change.
4. List follow-ups: known limitations accepted during this task, refactors noted but deferred, open questions not resolved.
5. Flag any safety gates before merging: migrations to run, feature flags to set, dependent services to update, config changes to deploy.

## Audit

| Check | Pass condition |
|-------|----------------|
| Commit message explains why | Subject line is under 72 chars and states the reason, not just the action |
| PR description is complete | Covers what, why, and how to verify |
| Docs identified | Any affected documentation is named |
| Follow-ups captured | Nothing is silently dropped |
| Pre-merge gates listed | Any deployment or config steps are explicit |

## Outputs

Write to `_workspace/runs/active/<run-slug>/stages/`:

- `04_finalize.md` — commit message, PR description, docs to update, follow-up list, pre-merge gates

Do not only respond in chat. The durable handoff is the file in `_workspace/runs/active/<run-slug>/stages/`.


## Promotion

After writing the stage handoff:

- Promote final reviewed artifacts to `_workspace/outputs/` when they should be used outside the run.
- Promote deferred follow-ups, unresolved questions, risks to revisit, TODOs, and next actions to `_workspace/backlog/items/`.
- Promote reviewed stable project facts to `_workspace/context/project/`.
- Keep full run history in `_workspace/runs/active/<run-slug>/` until the user approves archiving it to `_workspace/runs/archive/<run-slug>/`.

## Review gate

Stop after writing `04_finalize.md`. The user reviews and commits. Pipeline complete.
