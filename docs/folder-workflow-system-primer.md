# Folder Workflow System Primer

Use this primer to quickly load another AI assistant into the mental model behind this repository and the workspaces it creates.

This is context, not a command. Do not read it on every task. Load it when an agent is new to the system, when maintaining the kit, when designing a workspace, or when debugging workflow behavior.

## One-sentence model

The filesystem is the workflow control surface: folders route work, Markdown files define contracts, outputs are durable edit surfaces, and one agent loads only the context needed for the current task.

## Foundations

This system adapts ideas from **Model Workspace Protocol (MWP)** by Jake Van Clief and David McDermott, described in *Interpretable Context Methodology: Folder Structure as Agentic Architecture*: <https://arxiv.org/abs/2603.16021>.

Core sources of influence:

- Unix pipelines: one stage, one job; output of one step becomes input to the next.
- Plain text as interface: Markdown files are readable by humans and agents.
- Multi-pass compilation: each stage produces an intermediate artifact for the next pass.
- Literate programming: instruction files also document the workflow for humans.
- Human-centered AI: review gates, visible state, and editable intermediate outputs.
- Context engineering: select and isolate relevant context instead of loading everything.

## Core terms

| Term | Meaning |
|---|---|
| `workspace-kit` | Reusable kit containing templates, docs, scripts, OpenCode config, and shared workspace/workflow knowledge. |
| root workspace | Machine-level router, usually `~/workspace`. It routes to projects, vaults, and the kit. |
| target workspace | A project, repo, vault, or folder initialized with `AGENTS.md` and `_workspace/`. |
| workflow | One-shot checklist for a task. Read it, do the work, produce result/artifact. |
| pipeline | Repeatable multi-stage folder workflow with stage outputs and human review gates. |
| run | One execution of a pipeline with a specific input. |
| stage | One step inside a pipeline. It reads defined input, performs one job, writes output, then stops. |
| contract | A Markdown file defining what a stage reads, does, writes, and where it stops. |
| reference material | Stable rules and context that persist across runs. MWP Layer 3. |
| working artifact | Run-specific input/output that changes each run. MWP Layer 4. |
| edit surface | A file produced for human review/editing before downstream work continues. |
| durable artifact | A saved plan, review, validation, handoff, note, or stage output. |

## Repository roles

```text
~/workspace/                 daily router / coordination layer
~/workspace/workspace-kit/   reusable kit and OpenCode config source
<notes-vault>/           real Obsidian vault with local workflow rules
target project/repo/folder               complete local workspace when initialized
```

Important distinction:

- `workspace-kit/` is the kit source of truth.
- A target project workspace should be complete and usable locally after initialization.
- The kit may keep a local registry of created workspace paths for maintenance commands, but target workspaces should not depend on the kit at runtime unless explicitly designed to.

## Instruction hierarchy

Use the nearest relevant instruction file and do not load everything.

Typical order:

1. Runtime/platform instructions.
2. Nearest `AGENTS.md`.
3. Local `_workspace/map/routing-table.md`, if present.
4. Selected workflow or pipeline `CONTEXT.md`.
5. Required runbooks, context files, and skills only.
6. Working files needed for the current task.

`CLAUDE.md` is a compatibility pointer for Claude. `AGENTS.md` is canonical when both exist.

## MWP layer model

Strict pipelines follow the five-layer model most directly.

| Layer | Role | This kit |
|---|---|---|
| Layer 0 | Identity and global rules | nearest real workspace/project `AGENTS.md` or tool-level instructions |
| Layer 1 | Pipeline routing and shared context | pipeline `CONTEXT.md` |
| Layer 2 | Stage contract | `stages/*/CONTEXT.md` |
| Layer 3 | Stable reference material | `_config/`, `shared/`, `stages/*/references/`, relevant skills/context |
| Layer 4 | Working artifacts | `_workspace/runs/active/<run-slug>/` |

Adaptation from the paper:

- The paper commonly shows `CLAUDE.md` as Layer 0 inside a workspace.
- This kit avoids pipeline-local `AGENTS.md`/`CLAUDE.md` to prevent template files from acting as live instructions inside the kit repo.
- For pipelines, Layer 0 is inherited from the nearest real workspace root. Pipeline folders start at Layer 1.

## Layer 3 vs Layer 4

Layer 3 is the factory configuration.

Examples:

- style guide
- voice guide
- engineering conventions
- learning principles
- domain constraints
- stage-specific rules
- reusable skills when applicable

The model should internalize Layer 3 as constraints and patterns.

Layer 4 is the product or material being processed.

Examples:

- current run input
- previous stage output
- draft
- validation note
- final artifact
- user-provided source material

The model should process Layer 4 as input to transform.

Do not mix them casually. If stable rules and run-specific artifacts are dumped into one undifferentiated prompt, the model must infer which text is a constraint and which text is the object of work. The folder structure should make that separation explicit.

## Workflows

A workflow is a one-shot checklist for a task type.

Use workflows for:

- small or medium tasks
- reviews
- validations
- handoffs
- note processing
- code review
- documentation updates
- non-repeatable or lightly repeatable work

Typical structure:

```text
_workspace/workflows/<task>.md
_workspace/runbooks/<command-or-procedure>.md
_workspace/context/reference/<stable-rule>.md
_workspace/context/project/<project-specific-context>.md
_workspace/backlog/items/<backlog-item>.md
_workspace/outputs/<artifact-type>/
```

Keep critical behavior and safety rules in `AGENTS.md`, because agents read it first. Use `_workspace/context/reference/` for template-provided background facts, principles, provider/tool notes, and reusable reference material. Use `_workspace/context/project/` for context discovered or written after initializing a real project.

Use `_workspace/backlog/items/` for deferred work, open action items, risks to revisit, and follow-ups that should not be lost in chat.

Workflow behavior:

1. Read the selected workflow.
2. Load only listed runbooks/context/skills.
3. For work/change/review/plan/validation/handoff workflows, create/select `_workspace/runs/active/<run-slug>/` unless the user explicitly says to skip run state.
4. Write/update the active run's `RUN.md` with request, assumptions, plan, current step, expected outputs, and open questions.
5. Put supplied material under the run's `input/`, workflow working output under `output/`, and final run notes under `final/`.
6. Save durable artifacts when requested or useful.
7. Stop for confirmation if safety gates apply.

## Pipelines

A pipeline is a repeatable, sequential, human-reviewed workflow.

Use a pipeline when:

- the task has natural stage boundaries
- stage 2 depends on stage 1 output
- human review between stages improves quality
- the same process will run repeatedly with different input
- traceability of intermediate outputs matters

Do not use a pipeline for:

- one-off Q&A
- small edits
- ad hoc troubleshooting
- simple note cleanup
- tasks where a normal workflow checklist is enough

Canonical structure:

```text
pipeline-name/
├── CONTEXT.md              Layer 1 routing/shared rules
├── README.md               human-facing overview
├── setup/questionnaire.md  one-time setup questions
├── _config/                Layer 3 shared stable rules
├── shared/                 Layer 3 shared reference material
└── stages/
    ├── 00_intake/
    │   ├── CONTEXT.md      Layer 2 stage contract
    │   └── references/     Layer 3 stage-specific rules
    ├── 01_process/
    │   ├── CONTEXT.md
    │   └── references/
    └── 02_finalize/
        ├── CONTEXT.md
        └── references/
```

Pipeline run state lives in the enclosing workspace:

```text
_workspace/runs/active/YYYY-MM-DD-topic-slug/
├── RUN.md
├── input/
├── output/   # workflow runs
├── stages/
└── final/
```

Pipeline execution rule:

1. Read pipeline `CONTEXT.md`.
2. Read only the active stage `CONTEXT.md`.
3. Load only the inputs listed for that stage.
4. Write/update active run `RUN.md` with the stage plan and expected output.
5. Write output under `_workspace/runs/active/<run-slug>/stages/`.
6. Stop for human review.
7. Do not run the next stage until explicitly told.

After final approval:

1. Confirm the active run has original input, stage outputs, final output, and validation notes.
2. Ask before moving `_workspace/runs/active/<run-slug>/` to `_workspace/runs/archive/<run-slug>/`.
3. Treat `_workspace/runs/archive/` as completed-run history, not active stage state.

## Stage contracts

A stage contract lives in `stages/<NN_name>/CONTEXT.md`.

It should define:

- `Purpose`: one sentence, one job.
- `Inputs`: exact Layer 3 and Layer 4 files/folders to load.
- `Do NOT load`: future stages, unrelated references, already-consumed input.
- `Process`: concrete steps.
- `Checkpoints`: optional mid-stage review points.
- `Audit`: checks before writing to output.
- `Outputs`: exact file(s) written under `_workspace/runs/active/<run-slug>/stages/`.
- `Review gate`: stop instruction.
- `Verify`: optional consistency checks with prior outputs/source.

The stage output is the handoff. Chat should only summarize and point to the file.

## Durable artifacts

Durable artifacts are files created so humans or future agents can resume work without relying on chat memory.

Common artifact triggers:

| User asks for | Write to |
|---|---|
| handoff, save state, continue later | `_workspace/outputs/handoffs/` |
| plan | `_workspace/outputs/plans/` |
| review, audit, assess | `_workspace/outputs/reviews/` |
| validation, verify, check result | `_workspace/outputs/validations/` |
| pipeline stage output | `_workspace/runs/active/<run-slug>/stages/` |

Do not create chat-only handoffs unless the user explicitly asks for chat-only.

Recommended names:

```text
YYYY-MM-DD-topic-handoff-vNN.md
YYYY-MM-DD-topic-plan-vNN.md
YYYY-MM-DD-topic-review-vNN.md
YYYY-MM-DD-topic-validation-vNN.md
```

## Skills

Skills are on-demand reusable task knowledge.

They are not the workflow orchestrator and should not replace durable Markdown context when the context must be cross-tool.

Good skill uses:

- clear-writing
- humanizer
- repo-bootstrap
- workspace-kit-bootstrap pointer
- task-specific transformation knowledge

Bad skill uses:

- canonical project policy
- personal philosophy that belongs as vault context
- long system reconstruction docs that Claude and other tools cannot see

If a concept should be available to OpenCode, Claude, and other tools, make a Markdown doc or runbook canonical and let skills point to it.

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
- editing/moving/deleting vault notes unless explicitly approved

Do not hardcode secrets or credentials.

Do not commit unless explicitly asked.

## Context loading discipline

The agent should not read the whole workspace by default.

Good loading pattern:

1. Read nearest `AGENTS.md`.
2. Read routing table.
3. Read selected workflow or pipeline context.
4. Read only referenced context/runbook/skill files.
5. Read the working artifacts needed for the task.

Bad loading pattern:

- load every doc because it might be useful
- read future pipeline stages
- mix reference rules and run input without labeling them
- treat archived source files as active policy
- rely on chat history instead of durable artifacts

## Workspace templates

The kit provides standard templates:

| Template | Use when |
|---|---|
| `minimal` | Lightweight folders, small projects, simple routing. |
| `development` | Code/backend/cloud/devops repos with reviews, validation, runbooks, and pipelines. |
| `devops` | Advanced DevOps/cloud/platform work with onboarding, infra changes, incidents, and readiness reviews. |
| `pipeline` | Strict repeatable staged workflow pattern copied inside `_workspace/pipelines/`. |

Template workspaces are complete local workspaces after initialization. They should not require reading the kit for normal operation.

## Kit state and registry

The kit can keep a local registry of workspaces it created:

```text
workspace-kit/state/workspaces.json
```

This registry is machine-local and path-specific. It helps future maintenance commands find known workspaces without scanning the filesystem. It is not the runtime source of truth for a target workspace.

Commands:

```sh
python3 scripts/workspaces.py list
python3 scripts/workspaces.py add /path/to/workspace --template development
python3 scripts/workspaces.py check
python3 scripts/workspaces.py remove /path/to/workspace
```

## Anti-patterns

- Creating many agent prompts for routing when folders and workflows are enough.
- Putting large process docs in global `AGENTS.md`.
- Keeping active instruction files inside templates where tools may accidentally load them.
- Copying stable rules into every stage instead of referencing Layer 3 material.
- Letting stage outputs exist only in chat.
- Running multiple pipeline stages without review gates.
- Clearing active run files before the run is archived and approved.
- Turning personal learning philosophy or vault rules into OpenCode-only skills.
- Treating historical source notes as active policy.

## Quick onboarding script for another agent

If another assistant needs fast context, give it this sequence:

```text
Read nearest AGENTS.md.
Read _workspace/map/routing-table.md if present.
If maintaining the workspace system, read workspace-kit/docs/folder-workflow-system-primer.md.
For normal work, do not load the primer unless needed.
For workflows, read only the selected workflow file and referenced context/runbooks.
For pipelines, read pipeline CONTEXT.md, then the active stage CONTEXT.md, then only listed inputs.
Write durable outputs to the correct output folder; do not use chat as the only handoff.
Ask before destructive, external, infrastructure, secret/auth, billing, or irreversible operations.
```

## Current design decisions

- `AGENTS.md` is canonical; `CLAUDE.md` is a compatibility pointer.
- Global OpenCode instructions stay tiny to avoid token bloat.
- The kit uses one active OpenCode primary agent: `general`.
- Pipelines do not include local `AGENTS.md` or `CLAUDE.md`; Layer 0 comes from the enclosing workspace.
- `_workspace/runs/active/` is active run state; `_workspace/runs/archive/` is completed-run history.
- Handoffs, reviews, plans, validations, and stage outputs are durable files.
- Skills are optional reusable knowledge, not the primary workflow routing system.
- Target workspaces are complete local workspaces after initialization.
