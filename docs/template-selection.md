# Template Selection

Use the smallest template that adds value.

| Template | Use for | Avoid when |
|---|---|---|
| `minimal` | Small repos, experiments, docs folders, lightweight projects | Backend/cloud/infra complexity exists |
| `development` | Software, backend, cloud, DevOps, IaC, CI/CD, API, container, Kubernetes, security-aware engineering repos | The folder is mainly personal notes or learning material |
| `devops` | Advanced DevOps/cloud team/project work: implementation changes, onboarding, infra changes, incidents, readiness, platform operations | Simple app repos where `development` is enough; interview prep or personal learning |
| `pipeline` | Strict repeatable multi-stage workflows with human review between stages | One-off edits, normal Q&A, small bug fixes |

`pipeline` is a staged workflow pattern, not a standalone project instruction root. Pipelines live inside a workspace's `_workspace/pipelines/` folder. The `templates/pipeline/` is the canonical template to copy from when creating a new pipeline.

Initialize from the kit root:

```sh
python3 scripts/init-workspace.py --template minimal /path/to/folder
python3 scripts/init-workspace.py --template development /path/to/repo
python3 scripts/init-workspace.py --template devops /path/to/devops-workspace
```

The `pipeline` template is copied automatically into initialized workspaces as `_workspace/pipelines/pipeline-template/`. Copy and customize it when you need a strict staged workflow.

Verify afterward:

```sh
python3 scripts/verify-workspace.py /path/to/folder
```

Do not use `--overwrite` until local customizations have been reviewed.
