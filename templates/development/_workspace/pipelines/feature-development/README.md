# Feature Development Pipeline

General-purpose staged pipeline for feature work, bug fixes, refactors, migrations, and integrations.

Run one stage at a time. Store run state under `_workspace/runs/active/<run-slug>/`; archive completed runs under `_workspace/runs/archive/` after approval.
