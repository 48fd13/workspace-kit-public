# Stage NN: Stage Name

<!-- One sentence describing this stage's single job. -->

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_previous.md` | Output from the previous stage |
| Layer 3 reference | `_config/conventions.md` | Stable pipeline rules |
| Layer 3 reference | `references/stage-specific.md` | Reference material for this stage only |

## Do NOT load

- later stage folders
- unrelated active run files
- `shared/` unless explicitly needed for this stage

## Process

1. Step one.
2. Step two.
3. Step three.

## Checkpoints (optional)

| After step | Agent presents | Human decides |
|---|---|---|
| 2 | Draft of X | Approve or redirect before step 3 |

## Audit

Run these checks before saving stage output under `_workspace/runs/active/<run-slug>/stages/`. If any fail, fix before writing output.

| Check | Pass condition |
|---|---|
| [Check name] | [What passing looks like] |

## Outputs

Write to `_workspace/runs/active/<run-slug>/stages/`:

- `NN_stage-name.md` — one-line description of what this file contains

Do not only respond in chat. The durable handoff is the stage file in the active run.

## Review gate

Stop after writing output. Wait for the user to review/edit the active run stage file before the next stage runs.

## Final-stage archive note

For final-stage contracts, follow the pipeline-level run archive rule in `../../CONTEXT.md`.
