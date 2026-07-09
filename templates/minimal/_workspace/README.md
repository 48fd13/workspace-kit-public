---
kind: workspace
template: minimal
kit_version: 0.1.0
initialized:
---

# Workspace

Minimal folder-workflow workspace.

Set `initialized` when creating the target workspace. Update `kit_version` only when intentionally aligning it with a kit release.

- `map/`: routing, naming, workspace map
- `workflows/`: task workflows and checklists
- `pipelines/`: multi-stage pipelines with review between stages
- `context/reference/`: template-provided reference context
- `context/reference/folder-workflow-system-primer.md`: local agent onboarding context, copied in by `init-workspace.py`
- `context/project/`: project-specific context discovered after initialization
- `backlog/`: deferred follow-ups and open action items
- `runs/`: active and archived run state/history
- `outputs/`: staged artifacts
