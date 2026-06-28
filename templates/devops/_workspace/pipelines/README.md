# Pipelines

This template includes all standard DevOps/cloud pipelines. None is the default; use the routing table to choose based on the task.

Pipelines:

- `onboarding-map/` — discover and map a new team/system/service/project scope
- `implementation-change/` — staged repo change for code, config, scripts, CI/CD, IaC, manifests, or automation
- `infrastructure-change/` — plan/review/validate shared infrastructure changes
- `incident-learning/` — turn incidents/alerts into durable learning and runbook improvements
- `service-readiness-review/` — assess operational readiness of a service/platform component

Execute one stage at a time. Store run state under `_workspace/runs/active/<run-slug>/`. After final approval, archive completed runs under `_workspace/runs/archive/`.
