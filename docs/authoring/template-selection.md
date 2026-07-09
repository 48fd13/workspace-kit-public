# Template Selection

Use the smallest template that adds value.

| Template | Use for | Avoid when |
|---|---|---|
| `minimal` | Small repos, experiments, docs folders, lightweight projects | Backend/cloud/infra complexity exists |
| `pipeline` | Strict repeatable multi-stage workflows with human review between stages | One-off edits, normal Q&A, small bug fixes |

`pipeline` is a staged workflow pattern, not a standalone project instruction root. Pipelines live inside a workspace's `_workspace/pipelines/` folder. The `templates/pipeline/` is the canonical template to copy from when creating a new pipeline.

`minimal` is a deliberately small starting point. For a larger domain-specific workspace (e.g. software/DevOps), extend `minimal` locally: add workflows, pipelines, and reference context under `_workspace/` following the same conventions.

Initialize from the kit root:

```sh
python3 scripts/init-workspace.py --template minimal /path/to/folder
```

The `pipeline` template is copied automatically into initialized workspaces as `_workspace/pipelines/pipeline-template/`. Copy and customize it when you need a strict staged workflow.

Do not use `--overwrite` until local customizations have been reviewed.
