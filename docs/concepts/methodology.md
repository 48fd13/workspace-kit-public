# Methodology

The complete model behind this kit: what the system is, why it is shaped this way, and how work flows through it end to end.

This is the long-form reference. It is context, not a per-task command — read it when you are new to the system, designing or maintaining a workspace, or debugging why a workflow behaved the way it did. For a fast orientation read `folder-workflow-system-primer.md`; for the specific procedures this doc points to, read the focused docs named inline.

---

## 1. The core idea

The filesystem is the control surface. Instead of encoding orchestration in agent prompts or bespoke tooling, the system keeps it in plain files a human can read, edit, and diff:

- **`AGENTS.md`** defines local policy — how an agent should behave in this folder.
- **the routing table** selects which context and which process a request maps to.
- **runs** hold the editable state of one work session while it is in progress.
- **outputs** are the durable artifacts a finished run leaves behind.

Everything else is elaboration on those four. The design goal is that orchestration stays legible: if you want to know what an agent will do, you read Markdown, not code.

### Why files instead of agents

The system deliberately does *not* build a graph of specialized sub-agents that route to each other. A folder tree plus checklists is easier to inspect, survives tool changes, and can be edited mid-task by a human. Routing, run lifecycle, and safety rules live in the nearest `AGENTS.md` — never in a runtime-specific agent prompt — so the same policy holds whether the work is driven by OpenCode, Claude, or any other tool that can read Markdown.

### Foundations

The approach adapts **Model Workspace Protocol (MWP)** by Jake Van Clief and David McDermott (*Interpretable Context Methodology: Folder Structure as Agentic Architecture*, <https://arxiv.org/abs/2603.16021>). The influences it draws on:

- **Unix pipelines** — one stage, one job; each stage's output is the next stage's input.
- **Plain text as interface** — Markdown is readable by humans and agents alike.
- **Multi-pass compilation** — each stage emits an intermediate artifact for the next pass.
- **Literate programming** — instruction files double as human documentation.
- **Human-centered AI** — review gates, visible state, editable intermediate outputs.
- **Context engineering** — select and isolate relevant context instead of loading everything.

See `mwp-compatibility.md` for the concept-by-concept mapping.

---

## 2. Kit and target workspace

There are two parts, and keeping them separate is what stops the system from collapsing into one undifferentiated pile.

| Part | What it is | Role |
|---|---|---|
| **Framework kit** | this repo | Provides portable policy, templates, docs, optional runtime adapters, and maintenance utilities. Not applied to anything by itself. |
| **Target workspace** | any initialized repo, vault, or folder | Owns local context for one project. Gets `AGENTS.md` + `_workspace/` when a durable, routed workflow is useful. |

**Rule of thumb: the kit provides; each target owns its own local context.**

The kit is a control-plane asset, not something to copy wholesale into every project. A target workspace is initialized *from* a kit template and then becomes a complete, self-contained local workspace that depends on nothing above it. See `concepts.md` for the short version of this split.

---

## 3. Core vocabulary

| Term | Meaning |
|---|---|
| **workspace** | A folder with `AGENTS.md` and `_workspace/`, capable of holding runs and outputs. |
| **run** | One persistent, human-editable work session. Its `process` is `task`, `workflow`, or `pipeline`. |
| **process** | *How* a run is carried out: standalone task, one-pass workflow, or staged pipeline. |
| **task** | A run that follows the request and routed context directly, with no reusable checklist. |
| **workflow** | A one-shot checklist for a task. Read it, do the work, produce the result. |
| **pipeline** | A repeatable multi-stage workflow with human review gates between stages. |
| **stage** | One step inside a pipeline. Reads defined input, does one job, writes output, then stops. |
| **contract** | The `CONTEXT.md` defining what a stage reads, does, writes, and where it stops. |
| **reference material** | Stable rules that persist across runs (MWP Layer 3). |
| **working artifact** | Run-specific input/output that changes each run (MWP Layer 4). |
| **durable artifact** | A saved plan, review, validation, handoff, decision, retro, or promoted output. |

---

## 4. The workspace shape

Every target workspace follows this layout. The exact folder names below are the current concrete reference shape — templates ship it, and agents can rely on it — but they express the *model*, not a contract enforced by tooling. If the shape evolves, this doc and the templates move together.

```text
target/
├── AGENTS.md          local policy: routing, runs, lifecycle, safety
├── CLAUDE.md          compatibility pointer to AGENTS.md
└── _workspace/
    ├── map/           routing table, workspace map, naming conventions
    ├── context/
    │   ├── reference/ stable rules known up front (Layer 3)
    │   └── project/   facts discovered during real work, after review (Layer 3)
    ├── workflows/     one-pass checklists
    ├── pipelines/     multi-stage definitions with review gates
    ├── runs/
    │   ├── active/    in-progress and finished-but-unarchived runs
    │   └── archive/   explicitly archived run history
    ├── outputs/       durable artifacts: plans, reviews, handoffs, etc.
    └── backlog/items/ deferred follow-ups, risks, TODOs, open questions
```

Two boundaries carry most of the weight:

- **`context/` (stable) vs `runs/` (in-flight) vs `outputs/` (finished).** Reference and project context shape *how* work is done; runs hold *what* is being done right now; outputs are what survives. Mixing them is the primary anti-pattern the structure exists to prevent.
- **`reference/` vs `project/` inside context.** Both are stable Layer 3, but `reference/` is authored up front (true on day one) and `project/` accumulates one reviewed fact at a time from real work. `context-model.md` covers this decision in full.

---

## 5. Runs: the unit of work

A run is one persistent work session. It is the single most important construct in the system, because it is where in-progress state lives *durably* instead of only in chat.

### When a run is required

Quick Q&A, status checks, and clarification questions can stay chat-only. Work, changes, reviews, plans, validations, and handoffs use a run by default — unless the user explicitly says to skip run state.

### Choosing the run

Use a user-provided run, or a clearly continuing active run. Ask only when several active runs are plausibly the target; otherwise establish a new dated run under `_workspace/runs/active/YYYY-MM-DD-topic-slug/`.

> **Design note.** This rule was deliberately loosened from an earlier "never create a run without asking." The default is now *establish a new run and proceed*, which removes friction from routine work. The tradeoff is a risk of **run sprawl** — near-duplicate runs for what the user meant as one continuing thread. There is no tool that polices this; the mitigation is judgment (prefer continuing an obviously-related active run) plus periodic cleanup. If sprawl becomes a real problem, the fix is a lightweight check for same-topic active runs, not a return to asking every time.

### RUN.md

Every run has a `RUN.md` control file. Its frontmatter carries lifecycle metadata; its body records the plan. Write or update it *before* substantive work — the plan must not live only in chat.

```text
---
kind: run
status: active          # active → finished → archived
process: task           # task | workflow | pipeline
started: YYYY-MM-DD
updated: YYYY-MM-DD
finished:
outputs: []
---
```

The body records: request, assumptions, plan, current step or stage, expected outputs, the route/context/process chosen, and open questions.

### Run folders by process

```text
task / workflow run          pipeline run
├── RUN.md                   ├── RUN.md
├── input/                   ├── input/
├── output/                  ├── stages/
└── final/                   └── final/
```

Task and workflow runs write one-pass working output to `output/`. Pipeline runs write one stage handoff per stage to `stages/`. Both write approved, promoted content to `final/` only at finish.

---

## 6. Lifecycle: active → finished → archived

The lifecycle is intentionally three explicit states, each advanced only by a corresponding user instruction. Nothing auto-promotes.

1. **Active.** The default. The run stays `active` through all drafting, review, and human editing. Requested artifacts (plans, reviews, handoffs, …) are drafted *under the active run* while work continues — asking for a "plan" selects an artifact type, it does **not** finish or promote the run.
2. **Finished.** Only on an explicit "this run is finished." Finishing:
   - writes the approved artifact under the run's `final/`,
   - creates **at least one** durable artifact under `_workspace/outputs/` (when changed project files are the main result, that durable artifact is a concise completion handoff),
   - records the output path in `RUN.md` frontmatter,
   - sets `status: finished`.
   Finished runs stay in `runs/active/` — finishing and archiving are separate steps.
3. **Archived.** Only on a separate explicit instruction. Archiving sets `status: archived`, records the archive date, and moves the run to `runs/archive/`.

This is what "keep drafts in the active run until the user explicitly finishes it" means in practice: the human, not the agent, decides when work is done and when history is closed. `../authoring/rules-and-safety.md` holds the authoritative rule text and the artifact-naming conventions.

---

## 7. The three processes

A run's `process` field selects one of three ways to do the work. They differ in how much structure and review the work needs.

### Task — direct work

The lightest process. Follow the request and the routed context directly, without inventing a checklist. Use it for in-scope work that has no matching reusable workflow or pipeline. Working output goes to the run's `output/`.

### Workflow — one-pass checklist

A single selected checklist executed in one pass. Use it for recurring, well-understood work where the steps are known but a review gate between steps is unnecessary. See `../authoring/authoring-workflows.md` to write one.

### Pipeline — staged, with review gates

A multi-stage process where each stage is reviewed before the next runs. Use it when work genuinely needs human checkpoints — bootstrapping an unfamiliar target, or any task where an early wrong turn is expensive to unwind.

Mechanics: read the pipeline `CONTEXT.md`, then only the **current** stage's `CONTEXT.md`; load only that stage's listed inputs; write the stage handoff under `runs/active/<run-slug>/stages/`; then **stop** and wait for the user. Never "run the whole pipeline" — one stage at a time, always. Stage outputs stay under the run until the run is finalized. See `../authoring/authoring-pipelines.md` for stage contracts and the full lifecycle.

Pipelines do not carry their own `AGENTS.md` or `CLAUDE.md`; their base policy comes from the enclosing workspace.

---

## 8. End-to-end flow

The canonical path a request takes, from arrival to durable result:

```text
1. Read the nearest AGENTS.md.
2. Read _workspace/map/routing-table.md.
3. Classify: quick Q&A → answer chat-only and stop.
             otherwise → continue.
4. The route names a task, workflow, or pipeline, plus the context to load.
5. Establish or continue the run; write/update RUN.md before substantive work.
6. Load ONLY the routed context, runbooks, and working files.
7. Do the work under the run:
     task/workflow → output/
     pipeline      → one stage to stages/, then stop for review.
8. Keep everything active. Stop at every safety gate and stage boundary.
9. On explicit finish: write final/, promote ≥1 durable output, record it, set finished.
10. On separate explicit instruction: archive.
```

### Loading discipline

Step 6 is load-bearing. The agent must **not** read the whole workspace by default. Read the nearest `AGENTS.md`, then the routing table, then only what the route names, then only the working files the current task needs. Do not read future pipeline stages ahead of time, do not mix reference rules with run input, and do not treat archived files as active policy. `context-model.md` details the good and bad loading patterns.

### Instruction hierarchy

When instructions overlap, precedence is:

1. Runtime/platform instructions.
2. Nearest `AGENTS.md` (canonical).
3. Local `_workspace/map/routing-table.md`.
4. The selected workflow or pipeline `CONTEXT.md`.
5. Referenced runbooks, context files, and skills — only those named.
6. Working files for the current task.

`CLAUDE.md` is a compatibility pointer for Claude; `AGENTS.md` wins when both exist.

---

## 9. Context, outputs, and backlog

Where a piece of information belongs is a function of *what kind of thing it is*, not where it happened to be produced.

| You're about to write… | It goes in |
|---|---|
| A rule true for every task here | `_workspace/context/reference/<topic>.md` |
| A durable fact a run just taught you (after review) | `_workspace/context/project/<topic>.md` |
| A finished plan, review, validation, handoff, decision, retro | `_workspace/outputs/<type>/` |
| A deferred follow-up, risk, TODO, or open question | `_workspace/backlog/items/` |
| Something specific to the current run only | the run's own `input/`, `output/`, or `stages/` |

The discriminating question for context: *would this have been true on day one (→ `reference/`), or did doing the work reveal it (→ `project/`)?* Durable artifacts are named `YYYY-MM-DD-topic-<type>-vNN.md`; the full trigger table and artifact section-shapes live in `../authoring/rules-and-safety.md`.

---

## 10. Safety gates

Some operations are never done autonomously. Stop and confirm before:

- security/auth model changes or secret handling,
- billing, payment, or funds-flow changes,
- destructive or irreversible operations (data loss),
- external API contract breaks,
- shared infrastructure changes outside local/dev scope,
- deploy, publish, push, cluster, or terraform mutations,
- installs and dependency changes.

Proceed autonomously only for minor, obvious, local, reversible, scoped work that does not change agreed behavior or force a user-facing design choice. Never hardcode secrets; never commit unless explicitly asked. These gates hold across **all** runtimes and control modes — an autonomous mode may skip *confirmation for routine local work*, but it does not skip a safety gate.

---

## 11. Runtime adapters

The methodology is tool-agnostic. A runtime adapter (OpenCode today) may add convenience but never redefines the model.

- `AGENTS.md` owns routing, context, runs, process, lifecycle, and safety.
- OpenCode contributes model-agnostic **Manual**, **Auto**, and **Plan** primary control modes, plus permission configuration. All three read the nearest `AGENTS.md`.
  - **Manual** — explain the plan and wait for confirmation before non-trivial work.
  - **Auto** — treat a clear request as authorization for reversible local work in scope; still stops at every safety gate and stage boundary.
  - **Plan** — inspect and plan without modifying target or policy files; may write planning artifacts into the active run only.
- Runtime config controls permissions and autonomy; it does not own routing or lifecycle.

Skills are optional on-demand task knowledge, not the orchestrator. If a concept must be available across tools, make a canonical Markdown doc and let skills point to it — never bury cross-tool policy inside a single tool's skill.

---

## 12. Design decisions, summarized

- `AGENTS.md` is canonical; `CLAUDE.md` is a thin compatibility pointer; runtime bootstrap files stay tiny and defer to it.
- Policy lives in workspace files, not agent prompts. Runtime modes carry behavior, never routing or lifecycle.
- Runs default to being created and proceeding; the human owns the finish and archive transitions.
- Everything stays under the active run until explicit finish; every finished run leaves at least one durable output.
- Context is split by stability (reference vs project) and separated from in-flight run state.
- Safety gates are absolute and cross-runtime.
- The concrete folder shape is a reference the templates keep in sync — the model is the contract, the exact names are the current expression of it.

---

## Where to go next

| You want to… | Read |
|---|---|
| Get oriented fast | `folder-workflow-system-primer.md` |
| Understand root vs kit vs target | `concepts.md` |
| Decide where context/rules belong | `context-model.md` |
| Write a workflow | `../authoring/authoring-workflows.md` |
| Write a pipeline | `../authoring/authoring-pipelines.md` |
| Get the authoritative run/safety rules | `../authoring/rules-and-safety.md` |
| Pick a template | `../authoring/template-selection.md` |
| Maintain this kit | `../maintenance/kit-maintenance.md` |
| Map to MWP | `mwp-compatibility.md` |
