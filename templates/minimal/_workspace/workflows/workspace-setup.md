# Workspace Setup Workflow

Use for extending this workspace after `init-workspace.py`: describing the actual project, adding a workflow, or adding reference context. One pass, no stage review.

Use the `workspace-bootstrap` pipeline instead when the target is unfamiliar and needs research before any of this can be written accurately (new repo, new domain, new vault).

1. Read `AGENTS.md`, `_workspace/README.md`, and the current `_workspace/map/workspace-map.md`.
2. Set `_workspace/README.md` frontmatter `initialized` to the workspace creation date and confirm its `template` and `kit_version` values.
3. Update `_workspace/map/workspace-map.md`: replace the generic `repo/`/`repos/<name>/` rows with the project's real top-level folders and what each one is for.
4. Update `_workspace/map/routing-table.md`: add one row per recurring task the user actually does here. Point each row at a standalone task context, workflow, or pipeline as appropriate.
5. To add a new workflow: create `_workspace/workflows/<name>.md` as a short numbered checklist (see `minor-change.md` for the shape). Keep it to the steps an agent needs, not prose explaining why.
6. To add reference context: create the file under `_workspace/context/reference/` (stable, project-wide rules) or `_workspace/context/project/` (facts discovered/reviewed during work, not written up front). Link it from the routing table row that needs it.
7. Review the changed control files and summarize what was added or changed.
