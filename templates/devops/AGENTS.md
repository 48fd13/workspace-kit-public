# Cloud DevOps Workspace Guide

Use this workspace for day-to-day DevOps/cloud/platform work, recurring onboarding/discovery, infrastructure change planning, service readiness, incident learning, and operational runbook work.

## Workflow order

1. Read this file.
2. Read `_workspace/map/routing-table.md`.
3. Select the relevant workflow or pipeline.
4. Read only required context, runbook, skill, and working files.
5. Prefer read-only discovery before proposing changes.
6. Save run state under `_workspace/runs/active/`; save final durable artifacts under `_workspace/outputs/`.
7. Put deferred follow-ups, risks, and open action items in `_workspace/backlog/items/`.
8. Stop for human review at workflow safety gates and every pipeline stage boundary.

## Core principles

- Map before changing.
- Keep facts, assumptions, risks, and open questions separate.
- Treat shared infrastructure as approval-gated.
- Never store secrets or credentials in notes, prompts, artifacts, or examples.
- Keep provider/tool context stack-agnostic and load only what the active task needs.
- Do not include interview-prep or personal learning workflows in this workspace.

## Run rules

Quick Q&A, status checks, and clarification questions can stay chat-only. Work/change/review/plan/validation/handoff tasks use a run by default unless the user explicitly says to skip run state.

## Workflows

A workflow is a one-shot checklist for a task.

- Use a user-provided run path/slug, or ask before creating one.
- Do not guess the active run.
- Write/update `_workspace/runs/active/YYYY-MM-DD-topic-slug/RUN.md` before work.
- `RUN.md` must include request, assumptions, plan, current step, expected outputs, and open questions.
- Use `input/`, `output/`, and `final/` inside the run.

## Pipelines

A pipeline is a repeatable multi-stage folder workflow with review between stages.

- Use a user-provided run path/slug, or ask before creating one.
- Do not guess the active run.
- Write/update `RUN.md` before each stage with the stage plan and expected output.
- Write stage output under `_workspace/runs/active/<run-slug>/stages/`.
- Run one stage, then stop for review.
- Ask before archiving or clearing active run files.

## Durable artifact triggers

- `handoff`, `handoff this`, `save state`, `preserve this`, `continue later` → `_workspace/outputs/handoffs/`
- `plan`, `write a plan`, `change plan` → `_workspace/outputs/plans/`
- `review`, `audit`, `assess` → `_workspace/outputs/reviews/`
- `validation`, `verify`, `check result` → `_workspace/outputs/validations/`
- service/environment/dependency/ownership maps → `_workspace/outputs/maps/`
- change packets → `_workspace/outputs/change-packets/`
- incident notes/postmortems → `_workspace/outputs/incident-notes/`
- runbooks → `_workspace/outputs/runbooks/`
- deferred follow-ups, risks, TODOs, and open action items → `_workspace/backlog/items/`

Do not create a chat-only handoff unless the user explicitly asks for chat-only.

## Safety gates

Ask before destructive or irreversible operations, installs, push/publish/deploy, Terraform/OpenTofu apply/destroy/import/state changes, Kubernetes/Helm mutations, cloud resource mutations, IAM/auth/secrets changes, DNS/TLS/network changes, CI/CD deployment gate changes, production/shared environment changes, billing/cost-impacting changes, or irreversible data operations.

Do not commit unless explicitly asked.
