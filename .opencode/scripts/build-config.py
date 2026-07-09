#!/usr/bin/env python3
"""Build .opencode/opencode.json from organized source config files."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


OPENCODE_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = OPENCODE_DIR / "config"
PERMISSIONS_DIR = CONFIG_DIR / "permissions"
BASE_CONFIG_PATH = CONFIG_DIR / "base.json"
ASSIGNMENTS_PATH = PERMISSIONS_DIR / "agents.json"
OUTPUT_PATH = OPENCODE_DIR / "opencode.json"

PROFILE_FILES = {
    "bash-risky-ask": "bash-risky-ask.json",
    "bash-readonly": "bash-readonly.json",
    "bash-validation": "bash-validation.json",
    "bash-shell-risky-ask": "bash-shell-risky-ask.json",
    "bash-destructive-deny": "bash-destructive-deny.json",
}

READONLY_PROFILE = [
    "bash-risky-ask",
    "bash-readonly",
    "bash-shell-risky-ask",
    "bash-destructive-deny",
]

VALIDATION_PROFILE = [
    "bash-risky-ask",
    "bash-readonly",
    "bash-validation",
    "bash-shell-risky-ask",
    "bash-destructive-deny",
]

PROFILE_COMPOSITION = {
    "readonly": READONLY_PROFILE,
    "validation": VALIDATION_PROFILE,
}

VALIDATION_PATTERNS = {
    "npm test*",
    "npm run test*",
    "npm run lint*",
    "npm run typecheck*",
    "npm run check*",
    "npm run build*",
    "npm run format:check*",
    "pnpm test*",
    "pnpm run test*",
    "pnpm lint*",
    "pnpm run lint*",
    "pnpm typecheck*",
    "pnpm run typecheck*",
    "pnpm check*",
    "pnpm run check*",
    "pnpm build*",
    "pnpm run build*",
    "pnpm run format:check*",
    "yarn test*",
    "yarn lint*",
    "yarn typecheck*",
    "yarn check*",
    "yarn build*",
    "yarn format:check*",
    "bun test*",
    "bun run test*",
    "bun run lint*",
    "bun run typecheck*",
    "bun run check*",
    "bun run build*",
    "pytest*",
    "python -m pytest*",
    "python3 -m pytest*",
    "python -m unittest*",
    "python3 -m unittest*",
    "ruff check*",
    "python -m ruff check*",
    "python3 -m ruff check*",
    "mypy*",
    "pyright*",
    "python -m compileall*",
    "python3 -m compileall*",
    "go test*",
    "go vet*",
    "go list*",
    "cargo test*",
    "cargo check*",
    "cargo clippy*",
    "cargo build*",
    "cargo fmt --check*",
    "make test*",
    "make lint*",
    "make check*",
    "make verify*",
    "make build*",
    "mvn test*",
    "mvn verify*",
    "./mvnw test*",
    "./mvnw verify*",
    "gradle test*",
    "gradle check*",
    "./gradlew test*",
    "./gradlew check*",
}

SHELL_RISKY_PATTERNS = {
    "*>*",
    "*>>*",
    "*|*",
    "*`*",
    "*$(*",
    "* xargs *",
    "tee *",
    "*--output*",
    "*--pre*",
    "*--ext-diff*",
    "*<(*",
    "*&&*",
    "*;*",
    "git status* && git diff*",
    "git status* && git diff --stat*",
    "git status* && git log*",
    "pwd && ls*",
    "pwd; ls*",
    "git status*; git diff*",
    "git diff --ext-diff*",
    "git grep -O*",
    "git grep --open-files-in-pager*",
    "git grep* -O*",
    "git grep* --open-files-in-pager*",
}


def read_json(path: Path):
    return json.loads(path.read_text())


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent="\t") + "\n")


def load_rule_file(name: str) -> list[dict[str, str]]:
    data = read_json(PERMISSIONS_DIR / PROFILE_FILES[name])
    if not isinstance(data, list):
        raise ValueError(f"{PROFILE_FILES[name]} must contain a list of rule objects")
    return data


def compose_bash(profile_name: str) -> dict[str, str]:
    profile = PROFILE_COMPOSITION.get(profile_name)
    if profile is None:
        raise ValueError(f"unknown bash permission profile: {profile_name}")

    bash = {"*": "ask"}
    for rule_file_name in profile:
        for rule in load_rule_file(rule_file_name):
            pattern = rule.get("pattern")
            value = rule.get("permission")
            if not pattern or value not in {"allow", "ask", "deny"}:
                raise ValueError(f"invalid rule in {PROFILE_FILES[rule_file_name]}: {rule!r}")
            if pattern == "*":
                raise ValueError("the catch-all '*' rule is generated and must not be in source fragments")
            bash[pattern] = value
    return bash


def build_config() -> dict:
    config = read_json(BASE_CONFIG_PATH)
    assignments = read_json(ASSIGNMENTS_PATH)

    global_profile = assignments.get("global")
    if global_profile:
        config.setdefault("permission", {})["bash"] = compose_bash(global_profile)

    agent_profiles = assignments.get("agent", {})
    for agent_name, profile_name in agent_profiles.items():
        agent_config = config.get("agent", {}).get(agent_name)
        if agent_config is None:
            raise ValueError(f"bash profile assigned to unknown agent: {agent_name}")
        agent_config.setdefault("permission", {})["bash"] = compose_bash(profile_name)

    return config


def write_built_config() -> None:
    write_json(OUTPUT_PATH, build_config())


def init_source_from_runtime() -> None:
    runtime = read_json(OUTPUT_PATH)
    base = copy.deepcopy(runtime)
    assignments = {"global": "readonly", "agent": {}}

    global_bash = base.get("permission", {}).pop("bash", None)
    if not isinstance(global_bash, dict):
        raise ValueError("runtime config is missing global permission.bash")

    agents = base.get("agent", {})
    agent_bashes: dict[str, dict[str, str]] = {}
    for agent_name, agent_config in agents.items():
        permission = agent_config.get("permission", {})
        bash = permission.pop("bash", None)
        if isinstance(bash, dict):
            agent_bashes[agent_name] = bash
            if any(pattern in bash for pattern in VALIDATION_PATTERNS):
                assignments["agent"][agent_name] = "validation"
            else:
                assignments["agent"][agent_name] = "readonly"

    sample_validation = next(
        bash for bash in agent_bashes.values() if any(pattern in bash for pattern in VALIDATION_PATTERNS)
    )

    risky_ask = []
    readonly = []
    validation = []
    shell_risky = []
    destructive = []

    for pattern, value in global_bash.items():
        if pattern == "*":
            continue
        rule = {"pattern": pattern, "permission": value}
        if value == "deny":
            destructive.append(rule)
        elif pattern in SHELL_RISKY_PATTERNS:
            shell_risky.append(rule)
        elif value == "ask":
            risky_ask.append(rule)
        else:
            readonly.append(rule)

    for pattern, value in sample_validation.items():
        if pattern in VALIDATION_PATTERNS:
            validation.append({"pattern": pattern, "permission": value})

    write_json(BASE_CONFIG_PATH, base)
    write_json(ASSIGNMENTS_PATH, assignments)
    write_json(PERMISSIONS_DIR / PROFILE_FILES["bash-risky-ask"], risky_ask)
    write_json(PERMISSIONS_DIR / PROFILE_FILES["bash-readonly"], readonly)
    write_json(PERMISSIONS_DIR / PROFILE_FILES["bash-validation"], validation)
    write_json(PERMISSIONS_DIR / PROFILE_FILES["bash-shell-risky-ask"], shell_risky)
    write_json(PERMISSIONS_DIR / PROFILE_FILES["bash-destructive-deny"], destructive)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--init-source-from-runtime",
        action="store_true",
        help="initialize .opencode/config from the current generated opencode.json",
    )
    args = parser.parse_args()

    if args.init_source_from_runtime:
        init_source_from_runtime()
    write_built_config()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
