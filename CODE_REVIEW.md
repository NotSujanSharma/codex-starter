# Code Review Standard

Independent review exists to find consequential problems before completion. It is not a second implementation pass and not a style contest.

## Reviewer contract

The reviewer must:

- remain read-only;
- inspect the approved brief, execution plan, final diff, relevant code paths, and tests;
- independently trace behavior rather than relying on the implementer's summary;
- prioritize correctness, security, data integrity, concurrency, compatibility, reliability, and missing tests;
- distinguish verified defects from questions or speculative risks;
- include the smallest useful file and symbol reference;
- explain user or system impact;
- provide reproduction steps, a failing scenario, or concrete reasoning when possible;
- avoid fixing findings unless the main agent creates a separate task contract.

## Severity

- **Blocking:** likely security exposure, data loss, broken core behavior, unsafe migration, or a release-stopping regression.
- **High:** significant incorrect behavior or reliability risk in a realistic path.
- **Medium:** bounded defect, missing edge-case handling, or meaningful test gap.
- **Low:** legitimate maintainability issue with a concrete future cost.

Do not report formatting preferences or hypothetical concerns without an actionable failure mode. Mechanical formatting and lint issues belong to automated checks.

## Review order

1. Map acceptance criteria to the actual diff.
2. Trace changed runtime paths and state transitions.
3. Check trust boundaries, authorization, input validation, secrets, and unsafe external effects.
4. Check data invariants, migrations, retries, idempotency, failure behavior, and rollback.
5. Check concurrency, ordering, caching, and time-dependent behavior when applicable.
6. Check compatibility with public APIs, persisted data, configuration, and callers.
7. Assess whether tests would fail for the important incorrect behaviors.
8. Review scope, complexity, and documentation.

## Output

Use `templates/REVIEW_REPORT.md`. Lead with findings ordered by severity. If no material finding exists, say so and list the areas inspected and any residual validation gap.

A review is not approval when required tests were not run, evidence is unavailable, or the change differs materially from the approved brief.

