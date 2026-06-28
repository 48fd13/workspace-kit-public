# Stage 01: Signals

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_timeline.md` | Reviewed timeline |
| Layer 3 reference | `references/` | Signal analysis rules |

## Do NOT load

- later stage folders

## Process

1. Summarize logs, metrics, traces, alerts, and user impact signals.
2. Distinguish symptoms from possible causes.

## Outputs

Write `01_signals.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for signal review.
