# Folder Workflow System Primer

Use this primer to quickly load another AI assistant into the mental model behind this repository and the workspaces it creates.

This is context, not a command. Do not read it on every task. Load it when an agent is new to the system, when maintaining the kit, when designing a workspace, or when debugging workflow behavior.

## One-sentence model

The filesystem is the workflow control surface: `AGENTS.md` defines local policy, the routing table selects context and process, runs preserve editable work state, and finished outputs become durable artifacts.

## Where to read next

| Question | Read |
|---|---|
| The full model in one doc — concepts, shape, runs, lifecycle, flows | `methodology.md` |
| How do the kit and a target workspace relate? | `concepts.md` |
| What's the difference between stable reference rules and per-run material? | `context-model.md` |
| How do I write a workflow? | `../authoring/authoring-workflows.md` |
| How do I write a pipeline? | `../authoring/authoring-pipelines.md` |
| When is a run required, when do I write a durable artifact, what do I always ask before doing? | `../authoring/rules-and-safety.md` |
| Which template should I start from? | `../authoring/template-selection.md` |
| How do I maintain this kit itself? | `../maintenance/kit-maintenance.md` |
| How does this map to Model Workspace Protocol (MWP)? | `mwp-compatibility.md` |

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
| target workspace | A project, repo, vault, or folder initialized with `AGENTS.md` and `_workspace/`. |
| workflow | One-shot checklist for a task. Read it, do the work, produce result/artifact. |
| pipeline | Repeatable multi-stage folder workflow with stage outputs and human review gates. |
| run | One persistent work session using a standalone task, workflow, or pipeline process. |
| stage | One step inside a pipeline. It reads defined input, performs one job, writes output, then stops. |
| contract | A Markdown file defining what a stage reads, does, writes, and where it stops. |
| reference material | Stable rules and context that persist across runs. MWP Layer 3. |
| working artifact | Run-specific input/output that changes each run. MWP Layer 4. |
| edit surface | A file produced for human review/editing before downstream work continues. |
| durable artifact | A saved plan, review, validation, handoff, note, or stage output. |

## Instruction hierarchy

Use the nearest relevant instruction file and do not load everything. Typical order:

1. Runtime/platform instructions.
2. Nearest `AGENTS.md`.
3. Local `_workspace/map/routing-table.md`.
4. Selected workflow or pipeline `CONTEXT.md`.
5. Required runbooks, context files, and skills only.
6. Working files needed for the current task.

`CLAUDE.md` is a compatibility pointer for Claude. `AGENTS.md` is canonical when both exist.

## Skills

Skills are on-demand reusable task knowledge. They are not the workflow orchestrator and should not replace durable Markdown context when the context must be cross-tool.

Good skill uses: clear-writing, humanizer, repo-bootstrap, workspace-kit-bootstrap pointer, task-specific transformation knowledge.

Bad skill uses: canonical project policy, personal philosophy that belongs as workspace context, long system-reconstruction docs that other tools can't see.

If a concept should be available to OpenCode, Claude, and other tools, make a Markdown doc or runbook canonical and let skills point to it.

## Quick onboarding script for another agent

If another assistant needs fast context, give it this sequence:

```text
Read nearest AGENTS.md.
Read _workspace/map/routing-table.md.
If maintaining the workspace system, read workspace-kit/docs/concepts/folder-workflow-system-primer.md.
For normal work, do not load the primer unless needed.
For workflows, read only the selected workflow file and referenced context/runbooks.
For pipelines, read pipeline CONTEXT.md, then the active stage CONTEXT.md, then only listed inputs.
Keep drafts in the active run. On explicit finish, write run-final content and promote at least one durable output.
Ask before destructive, external, infrastructure, secret/auth, billing, or irreversible operations.
```

## Current design decisions

- `AGENTS.md` is canonical; `CLAUDE.md` is a compatibility pointer.
- Runtime-specific bootstrap instructions stay tiny and defer to the nearest `AGENTS.md`.
- OpenCode may provide model-agnostic Manual, Auto, and Plan primary modes; those modes do not own routing or workspace lifecycle.
- Pipelines do not include local `AGENTS.md` or `CLAUDE.md`; Layer 0 comes from the enclosing workspace.
- `_workspace/runs/active/` contains active runs plus finished runs awaiting archive; `_workspace/runs/archive/` is explicitly archived history.
- Runs remain active through review. Explicit finish creates run-final content and at least one durable workspace output.
- Skills are optional reusable knowledge, not the primary workflow routing system.
- Target workspaces are complete local workspaces after initialization.
