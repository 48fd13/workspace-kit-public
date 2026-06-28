# Stage 02: Relationships

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_inventory.md` | Reviewed inventory |
| Layer 3 reference | `references/` | Mapping rules |

## Do NOT load

- later stage folders

## Process

1. Map service, environment, ownership, dependency, deploy, network, and observability relationships.
2. Flag unclear or risky relationships.

## Outputs

Write `02_relationships.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for review before question generation.
