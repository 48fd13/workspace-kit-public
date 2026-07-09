# Concepts

The system has two parts: the reusable kit, and the workspaces it creates in projects.

## 1. Framework kit

This repository.

It provides portable folder-workspace policy, templates, docs, optional runtime adapters, and maintenance utilities. It is not applied to anything by itself — it is the source you initialize a workspace *from*.

The kit should be maintainable as a normal repo.

## 2. Target workspace

The kit is applied per project. Any repo, folder, or vault gets its own local workspace when a durable, routed workflow is useful:

```text
target/
├── AGENTS.md      local policy
├── CLAUDE.md      compatibility pointer
└── _workspace/    routing, context, runs, outputs
```

Each target workspace is self-contained: after initialization it owns its own routing, context, runs, and outputs, and does not depend on anything above it.

Examples:

- Obsidian vault → a customized personal-notes workspace
- small project → `templates/minimal`
- infrastructure repo → a workspace extended from `minimal`

## Rule of thumb

The kit provides; each target owns its own local context. There is no required layer above a project — a workspace is complete on its own.
