---
name: workspace-kit-bootstrap
description: Use when creating, rebuilding, installing, renaming, or repairing the `workspace-kit` repository or its optional runtime adapters.
---

# workspace-kit-bootstrap

Use the cross-tool runbook instead of treating this skill as the source of truth:

```text
docs/maintenance/workspace-kit-bootstrap.md
```

That file is canonical so OpenCode, Claude, and other Markdown-capable tools can follow the same workflow.

Do not use this skill for normal project setup. For target repos/folders, use `repo-bootstrap` and `scripts/init-workspace.py`.
