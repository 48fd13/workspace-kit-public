# Routing Table

Use this table after reading `AGENTS.md`.

| User request | Workflow | Required files |
|---|---|---|
| Small local change | `_workspace/workflows/minor-change.md` | `AGENTS.md`, target files |
| General review | `_workspace/workflows/review/code-review.md` | target files or diff |
| Extend this workspace: add a workflow, update the map, add reference context | `_workspace/workflows/workspace-setup.md` | `AGENTS.md`, `_workspace/map/workspace-map.md` |
| Bootstrap a workspace for an unfamiliar target (new repo, domain, or vault) | pipeline: `_workspace/pipelines/workspace-bootstrap/CONTEXT.md` | pipeline `CONTEXT.md`, stage `CONTEXT.md` |
| Multi-step task needing review between steps | pipeline in `_workspace/pipelines/` | pipeline `CONTEXT.md`, stage `CONTEXT.md` |
| Other in-scope work without a matching process | standalone task run | relevant target and workspace context |
| General Q&A | no workflow required | read only needed files |
