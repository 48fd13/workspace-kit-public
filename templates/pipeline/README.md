# Pipeline Template

A blank, ready-to-copy pipeline scaffold. For what a pipeline is, the layer model, stage contracts, and the run lifecycle, see `docs/authoring/authoring-pipelines.md` in the kit root — this file only covers copying this specific scaffold.

## How to use this template

1. Copy this folder into `_workspace/pipelines/<pipeline-name>/`.
2. Fill in `CONTEXT.md` — replace `{{Pipeline Name}}`, name the real stages.
3. Rename `stages/00_intake/`, `01_process/`, `02_finalize/` to real stage names (add or remove stages as needed).
4. Fill in each stage's `CONTEXT.md` from `stage-contract-template.md`.
5. Delete `setup/questionnaire.md` if the pipeline needs no one-time configuration.
