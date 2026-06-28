# Stage 01: Process

## Purpose

Transform the reviewed intake output into the main intermediate artifact.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_intake.md` | Reviewed intake from previous stage |
| Layer 3 reference | `../../_config/` | Stable workspace rules, if relevant |
| Layer 3 reference | `references/` | Stage-specific rules |

## Do NOT load

- unrelated active run input already consumed by stage 00
- `stages/02_finalize/` — do not read ahead
- Other stage references not listed above

## Process

1. Read the reviewed intake brief.
2. Apply the stage-specific transformation.
3. Preserve constraints and decisions from stage 00.
4. Produce the main intermediate output.

## Outputs

Write to `_workspace/runs/active/<run-slug>/stages/`:

- `01_process.md`

Do not only respond in chat. The durable handoff for this stage is the file in the active run.

## Review gate

Stop after writing output. Wait for the user to review and edit the active run stage file before stage 02 runs.
