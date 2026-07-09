# Workspace Kit Docs

This repository is the reusable folder-workspace kit. It is the source you initialize a per-project workspace *from* — it is not itself applied to your work.

This repo owns:

- portable workspace policy in `AGENTS.md`
- reusable templates
- initialization and registry scripts
- optional runtime adapters, including OpenCode config and skills
- guidance for maintaining the kit

## Key docs

Docs are grouped into three folders: `concepts/` (the model), `authoring/` (how to build workflows and pipelines), and `maintenance/` (keeping the kit healthy).

### `concepts/` — the model

- `concepts/folder-workflow-system-primer.md`: start here — one-sentence model, terminology, and an index into the docs below
- `concepts/methodology.md`: the complete model — concepts, workspace shape, runs, lifecycle, processes, and end-to-end flows in one place
- `concepts/concepts.md`: the kit vs a per-project target workspace
- `concepts/context-model.md`: Layer 3 vs Layer 4, `context/reference/` vs `context/project/`, where new context goes
- `concepts/mwp-compatibility.md`: how this kit maps to MWP concepts

### `authoring/` — building work

- `authoring/authoring-workflows.md`: how to write a workflow
- `authoring/authoring-pipelines.md`: how to write a pipeline, stage contracts, run lifecycle
- `authoring/rules-and-safety.md`: run rules, run lifecycle, durable artifact triggers, safety gates
- `authoring/template-selection.md`: when to use `minimal` vs `pipeline`

### `maintenance/` — keeping the kit healthy

- `maintenance/kit-maintenance.md`: how to maintain this repository
- `maintenance/workspace-kit-bootstrap.md`: cross-tool procedure for creating or repairing the kit
