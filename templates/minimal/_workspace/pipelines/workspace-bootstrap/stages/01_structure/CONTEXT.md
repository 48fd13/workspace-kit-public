# Stage 01: Structure

## Purpose

Turn the reviewed research into a draft `_workspace/map/workspace-map.md` and `_workspace/map/routing-table.md`.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_research.md` | Reviewed target inventory, conventions, recurring tasks |
| Layer 3 reference | `../../_config/map-conventions.md` | House style for map/routing-table rows, if present |

## Do NOT load

- unrelated active run input already consumed by stage 00
- `stages/02_workflows/` or later — do not draft workflow content yet
- Other stage references not listed above

## Process

1. Read the reviewed research output.
2. Draft `workspace-map.md`: one row per real top-level folder/area from the research, each with its actual purpose — replace generic placeholder rows entirely, don't append to them.
3. Draft `routing-table.md`: one row per recurring task identified in research, each pointing at a workflow or pipeline (existing or to be created in stage 02).
4. Route unmatched in-scope work to a standalone task context; flag only recurring work that needs a missing workflow.
5. Do not write workflow or context files yet — only the two map files.

## Audit

Run these checks before saving stage output. If any fail, fix before writing output.

| Check | Pass condition |
|---|---|
| Reflects research, not template | Every row traces back to something in stage 00's output, not a copied generic template row |
| Routing table is actionable | Every row points to standalone task context, an existing process, or a clearly flagged process still needed |
| No orphan structure | No map row exists that stage 00 didn't identify as real |
| No workflow content | The output is limited to the two map files; workflow/context content belongs in stage 02 |

## Outputs

Write to `_workspace/runs/active/<run-slug>/stages/`:

- `01_structure.md` — draft `workspace-map.md` content, draft `routing-table.md` content, and the list of workflows still needed

Do not only respond in chat. The durable handoff for this stage is the file in the active run.

## Review gate

Stop after writing output. Wait for the user to review and edit the active run stage file before stage 02 runs.
