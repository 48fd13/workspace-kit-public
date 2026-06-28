# Repo / Service Review Workflow

Use when reviewing a repository or service for operational understanding.

## Required context

- `_workspace/context/reference/devops-principles.md`
- `_workspace/context/reference/security-and-secrets-rules.md`
- `_workspace/context/reference/observability-principles.md` when runtime/alerts/logs are in scope

## Process

1. Identify service purpose, runtime, owners, environments, dependencies, and deploy path.
2. Note config, secrets, CI/CD, IaC, observability, and runbooks.
3. Separate facts, assumptions, risks, and open questions.
4. Write a service review to `_workspace/outputs/maps/` or `_workspace/outputs/reviews/`.
5. Do not propose mutations unless asked.
