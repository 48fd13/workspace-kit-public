# Workflows

One-shot checklists for day-to-day DevOps work.

Use a workflow when one pass is enough. Use a pipeline when you need review between stages.

Quick Q&A, status checks, and clarification questions can stay chat-only. For work/change/review/plan/validation/handoff tasks, use a run by default unless the user explicitly says to skip run state. Use a user-provided run path/slug, or ask before creating a new run. Do not guess the active run. For any run you create or use, write/update `_workspace/runs/active/YYYY-MM-DD-topic-slug/RUN.md` with request, assumptions, plan, current step, expected outputs, and open questions before doing the work. Put run input under `input/`, workflow working output under `output/`, and final run notes under `final/`.

Final durable artifacts still go to `_workspace/outputs/`, open follow-ups to `_workspace/backlog/items/`, and reviewed stable facts to `_workspace/context/project/`.

Workflow sets:

- `development/` — implementation, bugs, dependencies, migrations, scripts/config, CI failures, PRs
- `infrastructure/` — cloud, IaC, Kubernetes, containers, config, access, DNS/TLS, cost, secrets
- `ci-cd/` — CI/CD, release readiness, build and deployment workflows
- `operations/` — observability, incidents, backups, SLOs, rollback planning
- `knowledge-transfer/` — repo/service review, runbooks, handoffs
