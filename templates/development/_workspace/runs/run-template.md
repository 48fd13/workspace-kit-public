# Run: <title>

- Status: active
- Type: workflow | pipeline
- Workflow/pipeline: <path>
- Created: YYYY-MM-DD
- Owner: <person/team or unknown>

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

## Inputs

Run-specific source material belongs in `input/`.

## Working output

- Workflow runs write one-pass working output to `output/`.
- Pipeline runs write stage handoffs to `stages/`.

## Final / promotion

- Final durable artifacts -> `_workspace/outputs/`
- Open follow-ups -> `_workspace/backlog/items/`
- Reviewed stable facts -> `_workspace/context/project/`

## Notes

- Decisions, links, and validation notes.
