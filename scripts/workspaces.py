#!/usr/bin/env python3
"""Manage workspace-kit's local registry of created workspaces."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


KIT_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = KIT_ROOT / "state" / "workspaces.json"


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


def normalize_path(path: str) -> str:
    return str(Path(path).expanduser().resolve())


def add_workspace(args: argparse.Namespace) -> int:
    data = load_registry()
    path = normalize_path(args.path)
    now = utc_now()

    for workspace in data["workspaces"]:
        if workspace.get("path") == path:
            workspace["template"] = args.template
            workspace["status"] = args.status
            workspace["updated_at"] = now
            save_registry(data)
            print(f"Updated workspace: {path}")
            return 0

    data["workspaces"].append(
        {
            "path": path,
            "template": args.template,
            "created_at": now,
            "status": args.status,
        }
    )
    save_registry(data)
    print(f"Added workspace: {path}")
    return 0


def remove_workspace(args: argparse.Namespace) -> int:
    data = load_registry()
    path = normalize_path(args.path)
    before = len(data["workspaces"])
    data["workspaces"] = [w for w in data["workspaces"] if w.get("path") != path]
    if len(data["workspaces"]) == before:
        print(f"Workspace not registered: {path}", file=sys.stderr)
        return 1
    save_registry(data)
    print(f"Removed workspace: {path}")
    return 0


def list_workspaces(args: argparse.Namespace) -> int:
    data = load_registry()
    workspaces = data["workspaces"]
    if args.active:
        workspaces = [w for w in workspaces if w.get("status", "active") == "active"]

    if not workspaces:
        print("No workspaces registered.")
        return 0

    for workspace in sorted(workspaces, key=lambda w: w.get("path", "")):
        print(
            f"{workspace.get('path')}\t"
            f"template={workspace.get('template', 'unknown')}\t"
            f"status={workspace.get('status', 'active')}"
        )
    return 0


def check_workspaces(args: argparse.Namespace) -> int:
    data = load_registry()
    errors = 0
    for workspace in sorted(data["workspaces"], key=lambda w: w.get("path", "")):
        if args.active and workspace.get("status", "active") != "active":
            continue
        path = Path(workspace.get("path", ""))
        issues: list[str] = []
        if not path.exists():
            issues.append("missing path")
        elif not path.is_dir():
            issues.append("not a directory")
        else:
            if not (path / "AGENTS.md").exists():
                issues.append("missing AGENTS.md")
            if not (path / "_workspace" / "map" / "routing-table.md").exists():
                issues.append("missing _workspace/map/routing-table.md")

        if issues:
            errors += 1
            print(f"FAIL {path}: {', '.join(issues)}")
        else:
            print(f"OK   {path}")
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List registered workspaces.")
    list_parser.add_argument("--active", action="store_true", help="Show only active workspaces.")
    list_parser.set_defaults(func=list_workspaces)

    add_parser = subparsers.add_parser("add", help="Register a workspace path.")
    add_parser.add_argument("path", help="Workspace path to register.")
    add_parser.add_argument("--template", default="custom", help="Template name, e.g. minimal, pipeline, custom-vault.")
    add_parser.add_argument("--status", default="active", choices=["active", "inactive"], help="Registry status.")
    add_parser.set_defaults(func=add_workspace)

    remove_parser = subparsers.add_parser("remove", help="Remove a workspace from the registry.")
    remove_parser.add_argument("path", help="Workspace path to remove.")
    remove_parser.set_defaults(func=remove_workspace)

    check_parser = subparsers.add_parser("check", help="Check registered workspace paths and required files.")
    check_parser.add_argument("--active", action="store_true", help="Check only active workspaces.")
    check_parser.set_defaults(func=check_workspaces)

    args = parser.parse_args()
    try:
        return args.func(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
