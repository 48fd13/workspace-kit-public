# Secrets Handling Runbook

Never store secret values in workspace files.

Use placeholders and record only:

- secret name or logical reference
- storage system
- consumer
- rotation/owner if known
- open questions

Treat secret/auth changes as gated.
