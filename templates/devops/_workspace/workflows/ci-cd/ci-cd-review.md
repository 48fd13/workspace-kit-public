# CI/CD Review Workflow

## Required context

- `_workspace/context/reference/ci-cd-principles.md`
- `_workspace/context/reference/tool-notes/ci-cd.md`
- `_workspace/context/reference/security-and-secrets-rules.md`
- `_workspace/runbooks/ci-cd.md`

## Process

1. Identify trigger, permissions, secrets, artifacts, environments, and deploy gates.
2. Review build/test/deploy separation and production approval controls.
3. For infrastructure pipelines, verify plan/apply separation and protected apply.
4. Save review under `_workspace/outputs/reviews/`.
