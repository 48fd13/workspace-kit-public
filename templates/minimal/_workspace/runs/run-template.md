---
kind: run
status: active
process: task
started: YYYY-MM-DD
updated: YYYY-MM-DD
finished:
outputs: []
---

# Run: <title>

## Request

Original request or task summary.

## Assumptions

- Facts/assumptions that shape the plan.

## Plan

1. Planned step.

## Current step

- What is being worked on now.

## Expected outputs

- Run output, final artifact, backlog item, or context update expected from this run.

## Open questions

- Questions that block or may change the plan.

## Route and context

- Routing-table entry, selected context, and task/workflow/pipeline path.

## Inputs

Run-specific source material belongs in `input/`.

## Working output

- Standalone task and workflow runs write working output to `output/`.
- Pipeline runs write stage handoffs to `stages/`.

## Finish and promotion

- Keep status `active` through drafting and review.
- On explicit finish: write the approved artifact to `final/`, promote at least one durable artifact to `_workspace/outputs/`, record its path in frontmatter, then set status to `finished`.
- Archive only on separate explicit instruction.
- Open follow-ups -> `_workspace/backlog/items/`
- Reviewed stable facts -> `_workspace/context/project/`

## Notes

- Decisions, links, and validation notes.
