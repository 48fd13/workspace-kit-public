# Stage 00: Timeline

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Incident source material |
| Layer 3 reference | `../../_config/` | Stable incident rules if present |

## Do NOT load

- later stage folders

## Process

1. Build a fact-only timeline with timestamps, symptoms, impact, mitigation, and unknowns.
2. Mark missing or uncertain timestamps.

## Outputs

Write `00_timeline.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for timeline review.
