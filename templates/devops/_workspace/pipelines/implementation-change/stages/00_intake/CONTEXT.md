# Stage 00: Intake

## Goal

Clarify the requested implementation change, boundaries, risks, and needed inputs before reading broadly or editing.

## Inputs

- User request
- Files or links in active run `input/`
- Nearest `AGENTS.md` and routing table
- Known safety gates

## Process

1. Restate the requested change in one paragraph.
2. Identify affected area type: code, config, script, CI/CD, IaC, manifest, docs/runbook, or mixed.
3. List explicit constraints, approvals needed, and out-of-scope actions.
4. Identify missing information that blocks safe discovery.
5. Decide whether the task should remain in this pipeline or switch to a more specific pipeline/workflow.

## Outputs

Write `00_intake.md` under `_workspace/runs/active/<run-slug>/stages/` containing:

- request summary
- affected area guess
- facts vs assumptions
- safety gates
- missing inputs/questions
- recommended next stage

## Review gate

Stop after writing the active run stage file. Ask for review if scope, risk, or required inputs are unclear.
