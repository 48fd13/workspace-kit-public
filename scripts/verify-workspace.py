#!/usr/bin/env python3
"""Verify a folder-workflow workspace in any project directory."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


STANDARD_REQUIRED_PATHS = [
    "AGENTS.md",
    "_workspace/README.md",
    "_workspace/map/workspace-map.md",
    "_workspace/map/routing-table.md",
    "_workspace/map/naming-conventions.md",
    "_workspace/context/reference/README.md",
    "_workspace/context/project/README.md",
    "_workspace/backlog/README.md",
    "_workspace/backlog/items/README.md",
    "_workspace/backlog/items/item-template.md",
    "_workspace/runs/README.md",
    "_workspace/runs/run-template.md",
    "_workspace/runs/active/README.md",
    "_workspace/runs/archive/README.md",
    "_workspace/outputs/README.md",
]

PIPELINE_REQUIRED_PATHS = [
    "CONTEXT.md",
    "README.md",
    "_config/README.md",
    "shared/README.md",
]

OLD_LAYOUT_DIRS = [
    "00-map",
    "10-workflows",
    "20-runbooks",
    "30-context",
    "40-outputs",
    "_map",
    "_workflows",
    "_runbooks",
    "_context",
    "_outputs",
]

OLD_PIPELINE_TEXT_PATTERNS = [
    r"stages/\*/output",
    r"`\.\./[0-9]{2}_[^`]+/output",
    r"`\.\./\.\./input/`",
    r"runs/YYYY-MM-DD",
    r"pipeline's `runs`",
]


def referenced_workspace_paths(routing_table: Path) -> list[str]:
    text = routing_table.read_text()
    # Capture backticked _workspace paths from the routing table.
    paths = set(re.findall(r"`(_workspace/[^`]+)`", text))
    return sorted(
        path for path in paths
        if "<" not in path and "YYYY" not in path
    )


def pipeline_stage_contexts(root: Path) -> list[Path]:
    stages_dir = root / "stages"
    if not stages_dir.exists():
        return []
    return sorted(stages_dir.glob("*/CONTEXT.md"))


def verify_pipeline_contracts(root: Path) -> list[str]:
    errors: list[str] = []
    contexts = pipeline_stage_contexts(root)
    if not contexts:
        errors.append("pipeline workspace must include at least one stages/*/CONTEXT.md")
        return errors
    for obsolete in ["input", "runs"]:
        if (root / obsolete).exists():
            errors.append(f"pipeline must not contain local {obsolete}/; use _workspace/runs/ at workspace root")

    for context in contexts:
        text = context.read_text()
        for heading in ["## Inputs", "## Process", "## Outputs", "## Review gate"]:
            if heading not in text:
                errors.append(f"pipeline stage missing {heading}: {context.relative_to(root)}")
        for pattern in OLD_PIPELINE_TEXT_PATTERNS:
            if re.search(pattern, text):
                errors.append(f"pipeline stage uses old run layout pattern {pattern!r}: {context.relative_to(root)}")
        stage_name = context.parent.name
        expected_stage_file = f"{stage_name}.md"
        if expected_stage_file not in text:
            errors.append(f"pipeline stage must name canonical handoff file {expected_stage_file}: {context.relative_to(root)}")
        if "_workspace/runs/active/<run-slug>/stages/" not in text:
            errors.append(f"pipeline stage must write/read active run stages path: {context.relative_to(root)}")
        if (context.parent / "output").exists():
            errors.append(f"pipeline stage must not contain output/: {context.parent.relative_to(root)}")
        if stage_name.endswith("finalize") or stage_name.endswith("handoff"):
            for required in ["_workspace/outputs/", "_workspace/backlog/items/", "_workspace/context/project/"]:
                if required not in text:
                    errors.append(f"final pipeline stage missing promotion target {required}: {context.relative_to(root)}")
        stage_dir = context.parent
        for child in ["references"]:
            if not (stage_dir / child).is_dir():
                errors.append(f"pipeline stage missing {child}/: {stage_dir.relative_to(root)}")
    return errors


def verify_nested_pipelines(root: Path) -> list[str]:
    errors: list[str] = []
    pipelines_dir = root / "_workspace" / "pipelines"
    if not pipelines_dir.is_dir():
        return errors
    for pipeline in sorted(path for path in pipelines_dir.iterdir() if path.is_dir()):
        if (pipeline / "CONTEXT.md").exists() and (pipeline / "stages").is_dir():
            for error in verify_pipeline_contracts(pipeline):
                errors.append(f"{pipeline.relative_to(root)}: {error}")
    return errors


def verify_run_template(root: Path) -> list[str]:
    errors: list[str] = []
    run_template = root / "_workspace" / "runs" / "run-template.md"
    if not run_template.exists():
        return errors
    text = run_template.read_text()
    for heading in required_run_headings():
        if heading not in text:
            errors.append(f"run-template.md missing required heading: {heading}")
    return errors


def required_run_headings() -> list[str]:
    return [
        "## Request",
        "## Assumptions",
        "## Plan",
        "## Current step",
        "## Expected outputs",
        "## Open questions",
    ]


def verify_active_runs(root: Path) -> list[str]:
    errors: list[str] = []
    active_runs_dir = root / "_workspace" / "runs" / "active"
    if not active_runs_dir.is_dir():
        return errors
    for run_dir in sorted(path for path in active_runs_dir.iterdir() if path.is_dir()):
        run_file = run_dir / "RUN.md"
        if not run_file.exists():
            errors.append(f"active run missing RUN.md: {run_dir.relative_to(root)}")
            continue
        text = run_file.read_text()
        for heading in required_run_headings():
            if heading not in text:
                errors.append(f"active run RUN.md missing required heading {heading}: {run_file.relative_to(root)}")
    return errors


def verify_skills(root: Path) -> list[str]:
    errors: list[str] = []
    skills_dir = root / ".opencode" / "skills"
    if not skills_dir.exists():
        return errors
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"missing skill file: {skill_file.relative_to(root)}")
            continue
        text = skill_file.read_text()
        if "name:" not in text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else True:
            errors.append(f"skill frontmatter missing name: {skill_file.relative_to(root)}")
        if "description:" not in text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else True:
            errors.append(f"skill frontmatter missing description: {skill_file.relative_to(root)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", default=".", help="Workspace root to verify.")
    args = parser.parse_args()

    root = Path(args.target).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        print(f"Target is not a directory: {root}", file=sys.stderr)
        return 1

    is_pipeline = (root / "CONTEXT.md").exists() and (root / "stages").is_dir()
    required_paths = PIPELINE_REQUIRED_PATHS if is_pipeline else STANDARD_REQUIRED_PATHS

    for relative in required_paths:
        if not (root / relative).exists():
            errors.append(f"missing required path: {relative}")

    if is_pipeline:
        errors.extend(verify_pipeline_contracts(root))
    else:
        routing_table = root / "_workspace" / "map" / "routing-table.md"
        if routing_table.exists():
            for relative in referenced_workspace_paths(routing_table):
                if not (root / relative).exists():
                    errors.append(f"routing table references missing path: {relative}")
        errors.extend(verify_nested_pipelines(root))
        errors.extend(verify_run_template(root))
        errors.extend(verify_active_runs(root))

    for relative in OLD_LAYOUT_DIRS:
        path = root / relative
        if path.exists():
            try:
                has_entries = any(path.iterdir()) if path.is_dir() else True
            except OSError:
                has_entries = True
            if has_entries:
                warnings.append(f"old layout path still exists: {relative}")

    errors.extend(verify_skills(root))

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
        print()

    if errors:
        print("Workspace verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Workspace verification passed: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
