# Pipeline: Implementation Change

## Routing

| Task | Go to |
|---|---|
| Clarify request and constraints | `stages/00_intake/CONTEXT.md` |
| Understand current behavior | `stages/01_understand/CONTEXT.md` |
| Plan implementation | `stages/02_plan/CONTEXT.md` |
| Implement scoped change | `stages/03_implement/CONTEXT.md` |
| Validate result | `stages/04_validate/CONTEXT.md` |
| Finalize handoff | `stages/05_handoff/CONTEXT.md` |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Identity and safety rules | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing and shared context | this file |
| Layer 2 | Stage contract | `stages/*/CONTEXT.md` |
| Layer 3 | Reference material | `_config/`, `shared/`, `stages/*/references/`, relevant tool/provider notes |
| Layer 4 | Working artifacts | active run `input/`, `_workspace/runs/active/<run-slug>/stages/` |
| Run archive | Completed approved runs | `_workspace/runs/archive/` |


## Run lifecycle

1. Use a user-provided run path/slug, or ask before creating a new run. Do not guess the active run.
2. Write or update the active run's `RUN.md` with the stage plan and expected output before doing the stage work.
3. Put run-specific source material under the active run's `input/` folder.
4. Write each stage handoff under the active run's `stages/` folder.
5. Promote final durable artifacts to `_workspace/outputs/`, open follow-ups to `_workspace/backlog/items/`, and reviewed stable facts to `_workspace/context/project/`.
6. After final approval, ask before moving the active run to `_workspace/runs/archive/<run-slug>/`.

## Operating rules

- Execute exactly one stage, write the output artifact, then stop for review.
- Prefer read-only discovery before editing.
- Keep scope tight; do not expand a small change into a redesign without approval.
- Do not install dependencies, push, publish, deploy, mutate infrastructure, or change secrets/auth/billing without explicit approval.
- Treat Terraform/OpenTofu apply/import/state changes, Kubernetes/Helm mutations, cloud mutations, and production/shared environment changes as out of scope unless the user explicitly approves a separate gated operation.
- Archive completed approved runs under `_workspace/runs/archive/` and ask before clearing active run files.
