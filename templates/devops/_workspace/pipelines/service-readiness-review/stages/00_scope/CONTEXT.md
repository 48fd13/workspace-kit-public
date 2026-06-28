# Stage 00: Scope

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Service/readiness source material |
| Layer 3 reference | `../../_config/` | Stable review rules if present |

## Do NOT load

- later stage folders

## Process

1. Identify service/component, environment, criticality, owner, scope, and non-goals.

## Outputs

Write `00_scope.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for scope review.
