# MWP Compatibility

This kit is inspired by **Model Workspace Protocol (MWP)** from Jake Van Clief and David McDermott, described in *Interpretable Context Methodology: Folder Structure as Agentic Architecture*.

Primary reference:

- Jake Van Clief and David McDermott, *Interpretable Context Methodology: Folder Structure as Agentic Architecture*, arXiv:2603.16021, 2026. <https://arxiv.org/abs/2603.16021>
- DOI: <https://doi.org/10.48550/arXiv.2603.16021>

Related MWP repository: <https://github.com/RinDig/Model-Workspace-Protocol-MWP>.

MWP uses folder structure, Markdown context files, stage contracts, and plain-text outputs as the control surface for sequential human-reviewed AI workflows.

This kit adapts those ideas for OpenCode/Claude and supports two operating modes.

## 1. General folder workflows

Used by the `minimal`, `development`, and `devops` templates.

These are best for day-to-day development, note work, reviews, and lightweight repeatable tasks.

## 2. Strict pipeline workflows

Used by `templates/pipeline`.

These follow the paper more directly:

```text
nearest AGENTS.md / tool instructions  Layer 0
CONTEXT.md                            Layer 1
stages/*/CONTEXT.md                   Layer 2
_config/, shared/, references/        Layer 3
_workspace/runs/active/<run-slug>/    Layer 4
_workspace/runs/archive/<run-slug>/   Completed run archive after review
```

## Name mapping

| MWP paper | This kit |
|---|---|
| `CLAUDE.md` | `AGENTS.md` canonical, `CLAUDE.md` compatibility pointer |
| `CONTEXT.md` | `CONTEXT.md` in pipeline template; `_workspace/map/routing-table.md` in general templates |
| `stages/NN_stage/CONTEXT.md` | strict pipeline stage contract |
| `references/`, `_config/`, `shared/` | Layer 3 reference material |
| `output/` | workflow output under `_workspace/runs/active/<run-slug>/output/`; pipeline stage artifacts under `_workspace/runs/active/<run-slug>/stages/` |
| `runs/` | top-level `_workspace/runs/active/` and `_workspace/runs/archive/` |

## When to use strict pipeline mode

Use it for workflows that are:

- repeated
- sequential
- human-reviewed between stages
- artifact-producing
- dependent on previous stage outputs

Do not use it for simple edits, one-off bug fixes, normal Q&A, or small note cleanup.
