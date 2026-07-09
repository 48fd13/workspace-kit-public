# Context Model

How to decide what a workspace should load, and where new context belongs.

## Layer 3 vs Layer 4

Layer 3 is the factory configuration: stable rules that shape how the agent works, regardless of what it's currently working on.

Examples: style guide, voice guide, engineering conventions, learning principles, domain constraints, stage-specific rules, reusable skills.

Layer 4 is the product or material being processed: the thing currently being worked on, which changes every run.

Examples: current run input, previous stage output, a draft, a validation note, a final artifact, user-provided source material.

The agent should internalize Layer 3 as constraints and patterns, and treat Layer 4 as input to transform. Do not mix them casually — if stable rules and run-specific artifacts are dumped into one undifferentiated prompt, the agent has to infer which text is a constraint and which text is the object of work. The folder structure should make that separation explicit.

## `context/reference/` vs `context/project/`

Both live under `_workspace/context/` and are Layer 3, but differ in when they're written and how stable they are.

`context/reference/` is template-provided or authored up front: rules that are true before any real work has happened here — style, tagging rules, domain principles, tool notes. Write these during workspace setup, not mid-task.

`context/project/` is discovered: facts learned about this specific project/vault/repo while doing real work, then reviewed and promoted because they'll stay true. Don't write to `context/project/` speculatively or in bulk up front — it accumulates from runs, one reviewed fact at a time. An empty `context/project/` is normal for a new workspace.

Rule of thumb: if you're writing it before you've done any work, it's `reference/`. If you're writing it because a run just taught you something durable, it's `project/`.

## Loading discipline

The agent should not read the whole workspace by default.

Good loading pattern:

1. Read the nearest `AGENTS.md`.
2. Read `_workspace/map/routing-table.md`.
3. Read the standalone-task context, selected workflow, or pipeline `CONTEXT.md` named by the route.
4. Read only the context/runbook/skill files that route explicitly points to.
5. Read the working artifacts needed for the current task.

Bad loading pattern:

- loading every doc because it might be useful
- reading future pipeline stages ahead of the current one
- mixing reference rules and run input without labeling them
- treating archived source files as active policy
- relying on chat history instead of durable artifacts

## Where new context goes

| You're about to write... | Goes in |
|---|---|
| A rule that should hold for every task in this workspace | `_workspace/context/reference/<topic>.md` |
| A fact you just learned while doing real work, worth remembering | `_workspace/context/project/<topic>.md`, after review |
| A one-time decision or deferred question | `_workspace/backlog/items/` |
| Something specific to the current run only | the run's own `input/`, `output/`, or `stages/` — not stable context |

If you're unsure whether something belongs in `reference/` or `project/`, ask: would this have been true on day one, or did it take doing the work to find out? Day-one truths are `reference/`; discoveries are `project/`.
