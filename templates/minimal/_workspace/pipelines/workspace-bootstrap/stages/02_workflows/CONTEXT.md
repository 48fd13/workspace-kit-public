# Stage 02: Workflows

## Purpose

Draft the workflows the reviewed routing table points to, and any reference context they need.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_structure.md` | Reviewed map, routing table, and list of workflows still needed |
| Layer 3 reference | `../../_config/workflow-conventions.md` | House style for workflow checklists, if present |
| Layer 3 reference | `references/` | Examples of good short workflows |

## Do NOT load

- unrelated active run input already consumed by earlier stages
- `stages/03_finalize/` — do not read ahead
- Other stage references not listed above

## Process

1. Read the reviewed routing table and the list of workflows still needed.
2. For each missing workflow, draft `_workspace/workflows/<name>.md` as a short numbered checklist — steps an agent follows, not prose explaining the system.
3. For each workflow that needs stable reference material (rules, conventions, style) to do its job, draft the file under `_workspace/context/reference/` and note which routing-table row should link it.
4. Do not draft `_workspace/context/project/` content — that's discovered later during real work, not written up front.
5. If a routing-table row turns out to need a pipeline instead of a workflow (multi-step, needs review between steps), flag it — don't build the pipeline in this stage.

## Audit

Run these checks before saving stage output. If any fail, fix before writing output.

| Check | Pass condition |
|---|---|
| Every gap filled or flagged | Every workflow stage 01 flagged as missing is either drafted here or explicitly deferred with a reason |
| Workflows are checklists | Each drafted workflow is a short numbered list of steps, not an essay |
| Context is linked, not orphaned | Every drafted reference-context file is referenced from a specific routing-table row |
| No project context invented | No `_workspace/context/project/` content was written from assumption |

## Outputs

Write to `_workspace/runs/active/<run-slug>/stages/`:

- `02_workflows.md` — drafted workflow files (or their content, to be written out in stage 03), drafted reference-context files, and any deferred pipeline flags

Do not only respond in chat. The durable handoff for this stage is the file in the active run.

## Review gate

Stop after writing output. Wait for the user to review and edit the active run stage file before stage 03 runs.
