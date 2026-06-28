# Stage 01: Inventory

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_intake.md` | Reviewed scope |
| Layer 3 reference | `../../shared/` | Shared reference if present |
| Layer 3 reference | `references/` | Inventory rules |

## Do NOT load

- later stage folders
- raw active run input unless intake is insufficient

## Process

1. Inventory services, environments, repos, cloud accounts/projects, IaC, CI/CD, observability, owners, and open questions.
2. Separate known facts from assumptions.

## Outputs

Write `01_inventory.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for review before relationships.
