# Stage 03: Verify

Check that the implementation is correct, complete, and does not introduce regressions. Use whatever validation tools exist in the project — this stage is tool-agnostic.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_implement.md` | What was implemented and what changed |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_design.md` | The approved design to verify against |
| Layer 3 reference | `../../_config/` | Project conventions, security rules |

## Do NOT load

- active run stage 00 output — already incorporated in design
- `stages/04_finalize/` — do not read ahead
- `_workspace/runs/active/<run-slug>/input/` — already consumed

## Process

1. Run the project's validation suite — tests, linter, type checker, build — whatever exists. Report results.
2. Verify the implementation against the design: does the code do what the design specified?
3. Check correctness: are edge cases handled? Are error paths safe? Are inputs validated at system boundaries?
4. Check for regressions: does anything that worked before now break?
5. Check security fundamentals: no hardcoded secrets, no injection surfaces, no unintended exposure of data or APIs.
6. Check that deviations flagged in stage 02 are acceptable or need design revision.
7. If verification fails on any point, describe the failure precisely — do not proceed to finalize with known issues.

## Audit

| Check | Pass condition |
|-------|----------------|
| Validation suite passes | No test, lint, or build failures (or failures are pre-existing and documented) |
| Implementation matches design | Every design requirement is satisfied |
| Edge cases handled | Boundary conditions and error paths are safe |
| No regressions | Existing behavior is preserved |
| No security issues | No secrets, injection surfaces, or unintended exposure introduced |

## Outputs

Write to `_workspace/runs/active/<run-slug>/stages/`:

- `03_verify.md` — validation results, correctness assessment, regression check, security notes, any issues found and their severity

Do not only respond in chat. The durable handoff is the file in `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop after writing `03_verify.md`. If issues are found, the user decides whether to fix them (loop back to stage 02) or accept them with documented rationale. Do not proceed to finalize with unresolved blocking issues.
