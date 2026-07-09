# Workspace Bootstrap Pipeline

Use this pipeline when a workspace needs to describe a target the agent doesn't understand yet: a new repo, a new domain, or a personal vault with its own conventions.

It produces:

- a `_workspace/map/workspace-map.md` and `_workspace/map/routing-table.md` that reflect the real target, not the generic placeholders
- one or more starter workflows under `_workspace/workflows/`
- initial reference context under `_workspace/context/reference/`

Use `_workspace/workflows/workspace-setup.md` instead when the target is already familiar and this can be done in one pass without research.

## Stages

1. `00_research` — read-only discovery of the target: what it is, what it's for, how it's organized
2. `01_structure` — draft the workspace map and routing table from the research
3. `02_workflows` — draft the first workflow(s) and any reference context the routing table now points to
4. `03_finalize` — review everything together, write it into the live `_workspace/`, and hand off

Run one stage at a time. Write stage artifacts under `_workspace/runs/active/<run-slug>/stages/`, then stop for review before the next stage.
