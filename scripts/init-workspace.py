#!/usr/bin/env python3
"""Initialize a folder-workflow workspace from a template.

Interactive mode (no arguments): prompts for target directory and template,
then copies the chosen workspace template and a local copy of the pipeline
template into _workspace/pipelines/pipeline-template/.

Non-interactive mode: pass target and --template to skip prompts.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


KIT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = KIT_ROOT / "templates"
PRIMER_PATH = KIT_ROOT / "docs" / "concepts" / "folder-workflow-system-primer.md"
REGISTRY_PATH = KIT_ROOT / "state" / "workspaces.json"

# "pipeline" is a staged-workflow scaffold copied into every workspace, not a
# standalone workspace template — exclude it from the selectable list.
NON_WORKSPACE_TEMPLATES = {"pipeline"}

TEMPLATE_DESCRIPTIONS = {
    "minimal": "lightweight folder — notes, small projects, simple routing",
    "development": "engineering/code/cloud repo — full dev workflows, runbooks, pipelines",
    "devops": "advanced all-in-one DevOps/cloud workspace — onboarding, infra changes, incidents, readiness",
}


def discover_templates() -> list[str]:
    if not TEMPLATES_DIR.is_dir():
        return []
    names = [
        p.name
        for p in sorted(TEMPLATES_DIR.iterdir())
        if p.is_dir() and p.name not in NON_WORKSPACE_TEMPLATES
    ]
    return names


AVAILABLE_TEMPLATES = discover_templates()


def copy_tree(src: Path, dst: Path, overwrite: bool) -> list[str]:
    written: list[str] = []
    for source in sorted(src.rglob("*")):
        relative = source.relative_to(src)
        destination = dst / relative
        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and not overwrite:
            continue
        shutil.copy2(source, destination)
        written.append(str(relative))
    return written


def copy_file(src: Path, dst: Path, overwrite: bool) -> str | None:
    if not src.is_file():
        return None
    if dst.exists() and not overwrite:
        return None
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return str(dst)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_registry() -> dict:
    if not REGISTRY_PATH.exists():
        return {"workspaces": []}
    with REGISTRY_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict) or not isinstance(data.get("workspaces"), list):
        raise ValueError(f"Invalid workspace registry: {REGISTRY_PATH}")
    return data


def save_registry(data: dict) -> None:
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with REGISTRY_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")


def register_workspace(path: Path, template: str) -> str:
    data = load_registry()
    now = utc_now()
    resolved = str(path.resolve())

    for workspace in data["workspaces"]:
        if workspace.get("path") == resolved:
            workspace["template"] = template
            workspace["status"] = "active"
            workspace["last_initialized_at"] = now
            save_registry(data)
            return "updated"

    data["workspaces"].append(
        {
            "path": resolved,
            "template": template,
            "created_at": now,
            "last_initialized_at": now,
            "status": "active",
        }
    )
    save_registry(data)
    return "added"


def prompt_target() -> Path:
    print("\nWhere should the workspace be created?")
    print("Enter a path to an existing directory (absolute or relative to current dir).")
    raw = input("Target directory: ").strip()
    if not raw:
        print("No path entered. Aborting.", file=sys.stderr)
        sys.exit(1)
    path = Path(raw).expanduser().resolve()
    if not path.exists():
        print(f"Directory does not exist: {path}", file=sys.stderr)
        sys.exit(1)
    if not path.is_dir():
        print(f"Not a directory: {path}", file=sys.stderr)
        sys.exit(1)
    return path


def prompt_template() -> str:
    print("\nChoose a workspace template:")
    for i, name in enumerate(AVAILABLE_TEMPLATES, 1):
        print(f"  {i}. {name} — {TEMPLATE_DESCRIPTIONS.get(name, 'workspace template')}")
    raw = input(f"Template [1-{len(AVAILABLE_TEMPLATES)}] or name: ").strip()
    if raw.isdigit():
        idx = int(raw) - 1
        if 0 <= idx < len(AVAILABLE_TEMPLATES):
            return AVAILABLE_TEMPLATES[idx]
        print(f"Invalid selection: {raw}", file=sys.stderr)
        sys.exit(1)
    if raw in AVAILABLE_TEMPLATES:
        return raw
    print(f"Unknown template: {raw}. Choose from: {', '.join(AVAILABLE_TEMPLATES)}", file=sys.stderr)
    sys.exit(1)


def prompt_overwrite() -> bool:
    raw = input("\nOverwrite existing files? [y/N]: ").strip().lower()
    return raw in ("y", "yes")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "target",
        nargs="?",
        help="Directory to initialize. Omit to use interactive mode.",
    )
    parser.add_argument(
        "--template",
        choices=AVAILABLE_TEMPLATES,
        help="Template to apply. Omit to choose interactively.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files.",
    )
    parser.add_argument(
        "--no-register",
        action="store_true",
        help="Do not record this workspace in state/workspaces.json.",
    )
    args = parser.parse_args()

    interactive = args.target is None and args.template is None

    if interactive:
        print("=" * 60)
        print("  Workspace Initializer")
        print("  workspace-kit/scripts/init-workspace.py")
        print("=" * 60)
        target_dir = prompt_target()
        template = prompt_template()
        overwrite = prompt_overwrite()
    else:
        if args.target is None:
            print("Error: target directory required in non-interactive mode.", file=sys.stderr)
            return 1
        target_dir = Path(args.target).expanduser().resolve()
        template = args.template or "minimal"
        overwrite = args.overwrite
        if not target_dir.exists() or not target_dir.is_dir():
            print(f"Target directory does not exist: {target_dir}", file=sys.stderr)
            return 1

    template_dir = TEMPLATES_DIR / template
    if not template_dir.is_dir():
        print(f"Template not found: {template_dir}", file=sys.stderr)
        return 1

    print(f"\nInitializing '{template}' workspace in: {target_dir}")

    # Copy workspace template
    written = copy_tree(template_dir, target_dir, overwrite)

    # Copy pipeline template into _workspace/pipelines/pipeline-template/
    pipeline_src = TEMPLATES_DIR / "pipeline"
    pipeline_dst = target_dir / "_workspace" / "pipelines" / "pipeline-template"
    pipeline_written = []
    if pipeline_src.is_dir():
        pipeline_written = copy_tree(pipeline_src, pipeline_dst, overwrite)
        if pipeline_written:
            written += [f"_workspace/pipelines/pipeline-template/{f}" for f in pipeline_written]

    # Copy the current system primer into each initialized workspace so it is self-contained.
    primer_dst = target_dir / "_workspace" / "context" / "reference" / "folder-workflow-system-primer.md"
    primer_written = copy_file(PRIMER_PATH, primer_dst, overwrite)
    if primer_written:
        written.append("_workspace/context/reference/folder-workflow-system-primer.md")

    registry_result = None
    if not args.no_register:
        try:
            registry_result = register_workspace(target_dir, template)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(f"\nWarning: workspace initialized, but registry update failed: {exc}", file=sys.stderr)

    if written:
        print("\nFiles written:")
        for path in written:
            print(f"  + {path}")
    else:
        print("\nNo files written — existing files were preserved (use --overwrite to force).")

    print(f"\nDone. Workspace '{template}' initialized at:")
    print(f"  {target_dir}")
    if registry_result:
        print(f"\nWorkspace registry: {registry_result} {target_dir}")

    print("\nNext steps:")
    print(f"  1. Review AGENTS.md — set the project role and safety gates.")
    print(f"  2. Edit _workspace/map/workspace-map.md — describe your project folders.")
    print(f"  3. Edit _workspace/map/routing-table.md — map tasks to workflows.")
    print(f"  4. Keep _workspace/context/reference/folder-workflow-system-primer.md for agent onboarding context.")
    has_workflows = bool((target_dir / "_workspace" / "workflows").glob("*"))
    step = 5
    if has_workflows:
        print(f"  {step}. Browse _workspace/workflows/ — pre-built workflows are ready to use.")
        step += 1
    print(f"  {step}. Create a pipeline: copy _workspace/pipelines/pipeline-template/ into")
    print(f"     _workspace/pipelines/<your-pipeline-name>/ and customize stage contracts.")
    print(f"\n  Registry: python3 {KIT_ROOT / 'scripts' / 'workspaces.py'} list")

    return 0


if __name__ == "__main__":
    sys.exit(main())
