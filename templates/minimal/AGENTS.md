# Agent Guide

## Delivery flow

1. Read `_workspace/map/routing-table.md`, then load and follow only the context and process files named by the matching route.
2. Keep quick Q&A, status checks, and clarification chat-only when the route permits.
3. For other routed work, establish or continue the run and update `RUN.md` before substantive work.
4. Follow the selected standalone task, workflow, or pipeline process.
5. Keep drafts in the active run and stop at safety gates and pipeline stage boundaries.
6. Finish, promote, and archive only on the corresponding explicit user instruction.

## Runs

Quick Q&A, status checks, and clarification questions may stay chat-only when the route permits. Work, changes, reviews, plans, validations, handoffs, and other routed tasks use a run by default unless the user explicitly says to skip run state.

A run is a persistent, human-editable work session. Set `process` in `RUN.md` frontmatter to:

- `task` for standalone work without a reusable process
- `workflow` for one-pass checklist work
- `pipeline` for staged work with human review

Use a user-provided run or a clearly continuing active run. If several active runs are plausible, ask which applies. If none applies, establish a new dated run under `_workspace/runs/active/`.

Write or update `RUN.md` before substantive work. It records request, assumptions, plan, current step or stage, expected outputs, route/context/process, and open questions.

Standalone task and workflow runs use `input/`, `output/`, and `final/`. Pipeline runs use `input/`, `stages/`, and `final/`.

## Processes

- A standalone task follows the request and routed context directly.
- A workflow follows one selected checklist.
- A pipeline loads the pipeline and current stage context, executes one stage, writes one stage handoff, and stops for review.

## Lifecycle and artifacts

- Keep `status: active` through drafting, review, and human editing.
- Requested plans, reviews, validations, handoffs, decisions, retrospectives, and other artifacts stay under the active run while work continues.
- Finish only when the user explicitly says the run is finished.
- Finishing writes the approved artifact under run `final/`, creates at least one durable artifact under `_workspace/outputs/`, records its path in `RUN.md` frontmatter, and changes frontmatter status to `finished`.
- When changed project files are the primary result, create a concise completion handoff as the durable output.
- Archive only on separate explicit instruction; set status to `archived` and move the run from `runs/active/` to `runs/archive/`.
- Put deferred follow-ups, risks, and open actions in `_workspace/backlog/items/`.

## Workspace layout

- `AGENTS.md`: local operating instructions
- `_workspace/`: routing, context, processes, runs, backlog, and outputs
- `repo/`: project code and application files
- `repos/<name>/`: multiple repositories when needed

## Safety

Ask before destructive or irreversible operations, installs, external mutations, push/publish/deploy, infrastructure changes, secrets/auth/security changes, billing or funds-flow changes, external contract breaks, or irreversible data operations.

Do not hardcode secrets. Do not commit unless explicitly asked.
