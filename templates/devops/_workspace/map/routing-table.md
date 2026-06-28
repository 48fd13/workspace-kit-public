# Routing Table

Use this file after reading `AGENTS.md`.

## First decision

- If the work needs human checkpoints between stages, use a pipeline.
- Before any pipeline stage, use a user-provided run path/slug, or ask before creating a new run. Do not guess the active run. The run lives under `_workspace/runs/active/YYYY-MM-DD-topic-slug/`. Put run input under `input/`, write stage output under `stages/`, and stop after one stage.
- If the work can be completed in one pass unless a safety gate triggers, use a workflow.
- Quick Q&A, status checks, and clarification questions can stay chat-only. For work/change/review/plan/validation/handoff tasks, use a run by default unless the user explicitly says to skip run state. Use a user-provided run path/slug, or ask before creating a new run. Do not guess the active run. For any run you create or use, write/update `_workspace/runs/active/YYYY-MM-DD-topic-slug/RUN.md` with request, assumptions, plan, current step, expected outputs, and open questions before doing the work. Workflow runs use `input/`, `output/`, and `final/`; pipeline runs use `input/`, `stages/`, and `final/`.
- If the task is unclear, ask one short clarifying question before loading more context.
- Load provider/tool notes only for providers or tools involved in the active task. Do not load AWS/GCP/Azure/tool notes all at once.

## Pipelines

### Onboarding map

Use when: understanding a new team, system, service, or project scope.

Go to: `_workspace/pipelines/onboarding-map/CONTEXT.md`

Context: onboarding notes plus relevant provider/tool notes.

### Implementation change

Use when: a repo change needs checkpoints between understanding, planning, implementation, validation, and handoff.

Examples: code, config, scripts, CI/CD, IaC, manifests, automation, or repo docs tied to behavior.

Go to: `_workspace/pipelines/implementation-change/CONTEXT.md`

Avoid when: the change is small, local, reversible, and safe enough for a one-pass workflow.

### Infrastructure change

Use when: planning, reviewing, or validating a cloud, infrastructure, platform, or shared-environment change.

Go to: `_workspace/pipelines/infrastructure-change/CONTEXT.md`

Context: infrastructure change principles, security rules, and relevant provider/tool notes.

Avoid when: it is only a small local config/script/repo edit with no shared infrastructure mutation.

### Incident learning

Use when: an incident, alert, outage, or operational issue needs structured analysis and durable learning.

Go to: `_workspace/pipelines/incident-learning/CONTEXT.md`

Context: incident/on-call and observability principles.

Avoid when: a quick incident note or postmortem draft is enough.

### Service readiness review

Use when: reviewing service, platform component, or environment operational readiness.

Go to: `_workspace/pipelines/service-readiness-review/CONTEXT.md`

Context: DevOps, observability, security, ownership, and supportability rules.

## Workflows

### Knowledge transfer

#### Repo/service review

Use when: reviewing a repo or service for first operational understanding.

Go to: `_workspace/workflows/knowledge-transfer/repo-service-review.md`

Context: DevOps, observability, and security rules.

#### Runbook draft

Use when: drafting or improving an operational runbook.

Go to: `_workspace/workflows/knowledge-transfer/runbook-draft.md`

Context: incident/on-call and observability principles.

#### Session handoff

Use when: creating a durable handoff for current task state.

Go to: `_workspace/workflows/knowledge-transfer/handoff.md`

Context: current task artifacts.

### Development

#### Small implementation

Use when: making a small code, config, script, automation, or documentation change.

Go to: `_workspace/workflows/development/small-implementation.md`

Context: local repo context and validation runbook.

Avoid when: the change needs staged review; use the implementation-change pipeline instead.

#### Bug fix

Use when: debugging or fixing a bug/regression.

Go to: `_workspace/workflows/development/bug-fix.md`

Context: local repo context, logs, test output, and failing behavior if supplied.

#### Script or config change

Use when: changing scripts, config, CI/CD glue, manifests, values files, or automation glue.

Go to: `_workspace/workflows/development/script-config-change.md`

Context: local repo context and relevant tool notes.

#### CI failure triage

Use when: triaging CI, test, build, lint, or typecheck failures.

Go to: `_workspace/workflows/development/ci-failure-triage.md`

Context: CI logs, test output, and build config.

#### PR / diff review

Use when: reviewing a PR or diff for implementation risk.

Go to: `_workspace/workflows/development/pr-review.md`

Context: diff, changed files, validation expectations, and operational risk surface.

#### Dependency update review

Use when: reviewing package, lockfile, base image, action, chart, module, or provider version changes.

Go to: `_workspace/workflows/development/dependency-update-review.md`

Context: changed dependency files, changelog/security notes when available, and validation expectations.

#### Database migration review

Use when: reviewing schema changes, data migrations, backfills, migration ordering, or database compatibility risks.

Go to: `_workspace/workflows/development/database-migration-review.md`

Context: migration files, application compatibility, deployment order, rollback/fix-forward expectations, and data-safety gates.

### Infrastructure

#### Cloud change plan

Use when: preparing a small cloud/DevOps change plan that does not need the full infrastructure-change pipeline.

Go to: `_workspace/workflows/infrastructure/cloud-change-plan.md`

Context: infrastructure change principles.

#### Terraform/OpenTofu review

Use when: reviewing Terraform or OpenTofu changes.

Go to: `_workspace/workflows/infrastructure/terraform-review.md`

Context: `_workspace/context/reference/tool-notes/terraform-opentofu.md`

#### Kubernetes/Helm/Kustomize review

Use when: reviewing Kubernetes, Helm, or Kustomize changes.

Go to: `_workspace/workflows/infrastructure/kubernetes-review.md`

Context: `_workspace/context/reference/tool-notes/kubernetes.md` and `_workspace/context/reference/tool-notes/helm-kustomize.md` as needed.

#### Container image review

Use when: reviewing Dockerfiles, image build config, base images, runtime users, layers, healthchecks, or registry behavior.

Go to: `_workspace/workflows/infrastructure/container-image-review.md`

Context: container/build files, deployment runtime, registry policy, and secrets rules.

#### Environment config review

Use when: reviewing environment variables, ConfigMaps, Secrets references, values files, per-environment overrides, or config drift.

Go to: `_workspace/workflows/infrastructure/environment-config-review.md`

Context: affected environments, config source, deployment mechanism, and rollback expectations.

#### Access change review

Use when: reviewing IAM, RBAC, security groups, permissions, service accounts, roles, credentials, or access-control changes.

Go to: `_workspace/workflows/infrastructure/access-change-review.md`

Context: security/secrets rules, identity/resource scope, auditability, and rollback path.

#### DNS/TLS review

Use when: reviewing DNS records, certificates, TLS settings, ingress/edge routing, load balancer listeners, or domain cutovers.

Go to: `_workspace/workflows/infrastructure/dns-tls-review.md`

Context: affected domains, environments, TTLs, certificate lifecycle, routing path, and rollback expectations.

#### Secrets rotation review

Use when: planning or reviewing secret, token, key, certificate, credential, or KMS/key-material rotation.

Go to: `_workspace/workflows/infrastructure/secrets-rotation-review.md`

Context: secret consumers, deployment/reload behavior, access scope, auditability, and rollback/revoke path.

#### Cost review

Use when: reviewing cloud/platform cost, resource sizing, usage changes, or billing-impacting infrastructure choices.

Go to: `_workspace/workflows/infrastructure/cost-review.md`

Context: affected resources, usage assumptions, environment scope, monitoring/budgets, and cost-risk gates.

### CI/CD

#### CI/CD review

Use when: reviewing CI/CD pipelines, build automation, release automation, or deployment workflow config.

Go to: `_workspace/workflows/ci-cd/ci-cd-review.md`

Context: `_workspace/context/reference/tool-notes/ci-cd.md` and secrets rules.

#### Release readiness review

Use when: checking whether a release/deployment is ready to proceed.

Go to: `_workspace/workflows/ci-cd/release-readiness-review.md`

Context: changelog, validation status, migration/rollback notes, observability, and deployment gates.

### Operations

#### Observability review

Use when: reviewing observability, alerts, dashboards, logs, metrics, traces, or SLO/support signals.

Go to: `_workspace/workflows/operations/observability-review.md`

Context: observability principles and relevant tool notes.

#### Incident review

Use when: drafting a quick incident review or postmortem note that does not need the full incident-learning pipeline.

Go to: `_workspace/workflows/operations/incident-review.md`

Context: incident/on-call principles.

#### Rollback plan review

Use when: reviewing or drafting a rollback/revert/fix-forward plan for a change.

Go to: `_workspace/workflows/operations/rollback-plan-review.md`

Context: changed components, data compatibility, deployment path, monitoring, and irreversible-operation risks.

#### Backup/restore review

Use when: reviewing backup coverage, restore readiness, retention, recovery testing, or disaster-recovery assumptions.

Go to: `_workspace/workflows/operations/backup-restore-review.md`

Context: data stores, RPO/RTO expectations, restore procedure, retention policy, and access controls.

#### SLO / error budget review

Use when: reviewing SLOs, SLIs, error budgets, reliability targets, burn-rate alerts, or release risk against reliability goals.

Go to: `_workspace/workflows/operations/slo-error-budget-review.md`

Context: service objectives, metrics, alerting, recent incidents, deployment/release risk, and ownership.

## Fallback

For general Q&A, no workflow is required. Read only the files needed to answer the question.
