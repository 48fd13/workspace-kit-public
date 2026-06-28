# Implementation Change Pipeline

Use this pipeline for staged repo changes that need human checkpoints but are broader than a quick one-shot workflow.

Examples:

- application code change
- script or automation change
- config change
- CI/CD pipeline update
- IaC or manifest edit that does not apply/mutate infrastructure directly
- operational tooling change
- runbook/doc update tied to implementation behavior

Run one stage at a time. Write stage artifacts under `_workspace/runs/active/<run-slug>/stages/`, then stop for review before the next stage.
