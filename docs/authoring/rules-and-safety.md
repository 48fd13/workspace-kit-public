# Rules and Safety

Tool-agnostic operating rules for runs, artifact lifecycle, and safety gates.

## Run rules

A run is one persistent, human-editable work session. Its `process` is `task`, `workflow`, or `pipeline`.

Quick Q&A, status checks, and clarification questions can stay chat-only. Work/change/review/plan/validation/handoff tasks use a run by default unless the user explicitly says to skip run state.

- Use a user-provided run or a clearly continuing active run. Ask when several active runs are plausible; otherwise establish a new dated run.
- Write/update `_workspace/runs/active/YYYY-MM-DD-topic-slug/RUN.md` before substantive work.
- `RUN.md` frontmatter records lifecycle metadata. Its Markdown body records request, assumptions, plan, current step or stage, expected outputs, route/context/process, and open questions.
- Standalone task and workflow runs use `input/`, `output/`, and `final/`. Pipeline runs use `input/`, `stages/`, and `final/`.
- A standalone task run follows the request and routed context without inventing a workflow.

## Run lifecycle

- Keep `status: active` through drafting, review, and human editing.
- Finish only when the user explicitly says the run is finished.
- Finishing writes approved content under run `final/`, creates at least one durable `_workspace/outputs/` artifact, records its path in frontmatter, and then sets `status: finished`.
- When changed target files are the main result, create a concise completion handoff as the durable output.
- Keep finished runs in `runs/active/` until the user separately asks to archive them.
- Archiving sets `status: archived`, records the archive date, and moves the run to `runs/archive/`.

## Durable artifact triggers

When the user asks for one of these during an active run, write the draft under that run. The destination below is used when the run is explicitly finished:

| User asks for | Write to |
|---|---|
| handoff, save state, continue later | `_workspace/outputs/handoffs/` |
| plan, write a plan, change plan | `_workspace/outputs/plans/` |
| review, audit, assess | `_workspace/outputs/reviews/` |
| validation, verify, check result | `_workspace/outputs/validations/` |
| decision, decision record | `_workspace/outputs/decisions/` |
| retrospective, retro, post-mortem | `_workspace/outputs/retrospectives/` |
| deferred follow-up, risk, TODO, open action item | `_workspace/backlog/items/` |
| implementation or maintenance result | `_workspace/outputs/handoffs/` |
| pipeline stage output | remains in `_workspace/runs/active/<run-slug>/stages/` until finalization |

Artifact words select the artifact type; they do not finish or promote the run. After writing an active-run draft, reply with its path, one-line summary, and next action.

Name durable artifacts:

```text
YYYY-MM-DD-topic-handoff-vNN.md
YYYY-MM-DD-topic-plan-vNN.md
YYYY-MM-DD-topic-review-vNN.md
YYYY-MM-DD-topic-validation-vNN.md
YYYY-MM-DD-topic-decision-vNN.md
YYYY-MM-DD-topic-retrospective-vNN.md
```

### Artifact shapes

There's no skeleton file to copy — generate each artifact inline with these sections, adapted to the actual content:

| Type | Sections |
|---|---|
| Plan | Goal, Scope, Assumptions, Files/Areas, Steps, Validation, Risks/Stop Gates |
| Review | Scope, Findings (issue, why it matters, path/line, smallest fix), Summary |
| Validation | What was validated, Method, Result, Residual risk |
| Handoff | Current state, What's done, What's left, Next action, Relevant files/links |
| Decision record | Context, Options considered, Decision, Consequences |
| Retrospective | What happened, What went well, What didn't, Follow-ups (→ `_workspace/backlog/items/`) |

## Safety gates

Ask before:

- destructive or irreversible operations
- installs or dependency mutations
- push, publish, deploy, release, or external mutation
- Docker/Kubernetes/Helm/Terraform/shared infrastructure mutations
- secret/auth/security model changes
- billing, payments, or funds-flow changes
- external API contract breaks
- irreversible data operations
- machine-wide config changes
- editing/moving/deleting existing files unless explicitly approved

Do not hardcode secrets or credentials.

Do not commit unless explicitly asked.

## Anti-patterns

- Putting routing, context, run, or lifecycle rules in runtime-specific agent prompts instead of the nearest workspace `AGENTS.md`.
- Putting large process docs in global `AGENTS.md`.
- Keeping active instruction files inside pipeline templates where tools may accidentally load them.
- Copying stable rules into every stage instead of referencing Layer 3 material.
- Letting stage outputs exist only in chat.
- Running multiple pipeline stages without review gates.
- Finishing, promoting, archiving, or clearing run files without the corresponding explicit user instruction.
- Treating historical/archived source files as active policy.
