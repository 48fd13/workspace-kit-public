# Workspace Map

| Path | Purpose | Default behavior |
|---|---|---|
| `_workspace/map/` | Routing, naming, structure | Read first after `AGENTS.md` |
| `_workspace/context/reference/` | Template-provided principles and provider/tool notes | Load only files required by active workflow/pipeline |
| `_workspace/context/project/` | Reviewed stable project reference | Load when the task depends on reliable repo/service/environment details |
| `_workspace/backlog/` | Unresolved questions, deferred follow-ups, operational risks, and open action items | Add items when work is discovered but not completed |
| `_workspace/runs/` | Active and archived workflow/pipeline run state | Use for in-progress and historical run records |
| `_workspace/workflows/` | One-shot DevOps/cloud task checklists | Use for day-to-day work |
| `_workspace/runbooks/` | Command/review/validation procedures | Use when workflow calls for them |
| `_workspace/pipelines/` | Repeatable staged workflows | Execute one stage at a time |
| `_workspace/outputs/` | Durable artifacts and histories | Write plans/reviews/maps/change packets here |

Do not read every folder by default. Route first, then load the minimum needed context.
