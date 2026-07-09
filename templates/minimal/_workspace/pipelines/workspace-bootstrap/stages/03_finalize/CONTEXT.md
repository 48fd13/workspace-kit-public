# Stage 03: Finalize

## Purpose

Write the reviewed map, routing table, workflows, and reference context into the live `_workspace/`, and hand off.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_structure.md` | Reviewed map and routing table draft |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_workflows.md` | Reviewed workflow and reference-context drafts |
| Target | live `_workspace/` | Where the reviewed drafts get written |

## Do NOT load

- unrelated active run input already consumed by earlier stages
- `stages/00_research/references/` or `stages/01_structure/references/` — prior stage rules
- Any stage output other than stages 01 and 02

## Process

1. Read the reviewed stage 01 and stage 02 output.
2. Write `_workspace/map/workspace-map.md` and `_workspace/map/routing-table.md` from the reviewed stage 01 draft.
3. Write each drafted workflow file under `_workspace/workflows/` and each drafted reference-context file under `_workspace/context/reference/` from the reviewed stage 02 draft.
4. Verify every routing-table row now points at a file that actually exists (workflow, pipeline, or reference context).
5. Verify alignment with stage 00's research and stage 01's decisions. Flag any deviation instead of silently resolving it.
6. Review the required control files, routing targets, and workspace boundaries for consistency.
7. Keep the run active and present the finalized workspace for review.

## Audit

Run these checks before saving stage output. If any fail, fix before writing output.

| Check | Pass condition |
|---|---|
| Live files written | `workspace-map.md`, `routing-table.md`, and every drafted workflow/context file exist in the live `_workspace/` |
| No dangling routes | Every routing-table row resolves to a file that exists |
| Aligned with prior stages | The final structure matches stage 00's research and stage 01/02 decisions, or deviations are flagged |
| Workspace coherent | Required control files exist and routing targets resolve |

## Outputs

Write to `_workspace/runs/active/<run-slug>/stages/`:

- `03_finalize.md` — summary of what was written, consistency review, and any flagged deviations

Only on explicit finish, follow `AGENTS.md` to promote approved output to `_workspace/outputs/`, deferred actions to `_workspace/backlog/items/`, and reviewed stable facts to `_workspace/context/project/`.

Do not only respond in chat. The durable handoff for this stage is the file in the active run.

## Review gate

Stop after writing output. The user reviews the finalized workspace before it's used for real work.
