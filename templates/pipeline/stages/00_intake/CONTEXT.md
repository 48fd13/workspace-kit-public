# Stage 00: Intake

## Purpose

Clarify the input, scope, and intended pipeline output.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | User-provided source/input for this run |
| Layer 3 reference | `../../_config/` | Stable workspace rules, if relevant |

## Do NOT load

- `stages/01_process/` or later — do not read ahead
- `shared/` unless explicitly needed for intake

## Process

1. Read the run input.
2. Identify goal, constraints, missing information, and target output.
3. Do not perform downstream processing yet.
4. Produce a concise intake brief.

## Audit

Run these checks before saving stage output. If any fail, fix before writing output.

| Check | Pass condition |
|---|---|
| Goal captured | The brief states the goal and target output in one or two sentences |
| Open questions listed | Missing information is listed as explicit questions, not guessed |
| No downstream work | The brief contains no processing or drafting that belongs to later stages |

## Outputs

Write to `_workspace/runs/active/<run-slug>/stages/`:

- `00_intake.md`

Do not only respond in chat. The durable handoff for this stage is the file in the active run.

## Review gate

Stop after writing output. Wait for the user to review and edit the active run stage file before stage 01 runs.
