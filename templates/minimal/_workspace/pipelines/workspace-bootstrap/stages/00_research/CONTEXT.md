# Stage 00: Research

## Purpose

Understand the target well enough to describe it accurately, before writing any workspace files. Read-only.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | User-provided pointers: target path, URL, description, or existing docs |
| Layer 3 reference | `../../shared/` | Question checklist for unfamiliar targets, if present |
| Target | the target itself (repo, folder, vault, docs) | Actual structure, existing conventions, naming patterns |

## Do NOT load

- `stages/01_structure/` or later — do not draft the map yet
- `_config/` unless it holds house style relevant to research, not drafting

## Process

1. Identify what the target actually is: a code repo, a personal vault, a mixed folder, a domain with no existing structure.
2. Inventory the target's real top-level structure — list actual folders/areas, not assumed ones.
3. Identify existing conventions already in use (naming, tags, frontmatter, folder numbering, README files) — do not invent new ones yet.
4. Identify the recurring tasks a user would actually do here (the eventual routing-table rows).
5. List explicit open questions for anything ambiguous. Do not guess.
6. Do not write or propose `_workspace/map/` content yet — that's stage 01.

## Audit

Run these checks before saving stage output. If any fail, fix before writing output.

| Check | Pass condition |
|---|---|
| Real structure, not assumed | Every folder/area listed was actually observed in the target, not inferred from a template |
| Conventions distinguished from gaps | Existing conventions and missing/undecided conventions are in separate lists |
| No premature structure | The output contains no draft map or routing table — those belong in stage 01 |
| Open questions listed | Anything genuinely ambiguous is an explicit question, not a guess |

## Outputs

Write to `_workspace/runs/active/<run-slug>/stages/`:

- `00_research.md` — target inventory, existing conventions, recurring tasks, open questions

Do not only respond in chat. The durable handoff for this stage is the file in the active run.

## Review gate

Stop after writing output. Wait for the user to review and edit the active run stage file before stage 01 runs.
