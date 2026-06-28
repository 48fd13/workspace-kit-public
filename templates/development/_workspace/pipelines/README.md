# Pipelines

Add pipelines here as named subfolders, one per pipeline.

A pipeline is a multi-stage folder where the agent executes one stage, writes output under `_workspace/runs/active/<run-slug>/stages/`, and stops for your review before the next stage runs. After final approval, completed runs are archived under `_workspace/runs/archive/`.

## Structure

Each pipeline folder follows the canonical template at `workspace-kit/templates/pipeline/`:

```
pipelines/
  my-pipeline/
    CONTEXT.md          ← routing, triggers, load/don't-load table
    input/              ← run-specific source material (Layer 4)
    runs/               ← completed run archives after final approval
    _config/            ← stable rules shared across stages (Layer 3)
    shared/             ← shared reference material (Layer 3)
    setup/
      questionnaire.md  ← onboarding, run once with "setup"
    stages/
      00_intake/
        CONTEXT.md
        references/
        output/
      01_process/
        CONTEXT.md
        references/
        output/
      02_finalize/
        CONTEXT.md
        references/
        output/
```

## Triggers

Each pipeline's `CONTEXT.md` should define at minimum:

- `setup` — run onboarding questionnaire
- `status` — show stage completion across all stages

## After final approval

`_workspace/runs/active/<run-slug>/` is the active working area for the current run. Archive completed approved runs under `_workspace/runs/archive/<run-slug>/`. Ask before moving, deleting, or clearing active run files.

## How to create a new pipeline

Copy `workspace-kit/templates/pipeline/` into this folder, rename it, and customize the stage contracts.
