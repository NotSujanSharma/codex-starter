# Review Report: <Outcome>

Reviewer: <agent or person>

Reviewed revision or diff: <reference>

Brief and plan: <relative paths>

Verdict: Pass | Pass with non-blocking findings | Changes required | Incomplete evidence

## Findings

List findings in severity order. If there are no material findings, say `No material findings` and continue with coverage and limitations.

### <Severity>: <Short finding title>

- Location: <file and tight symbol or line reference>
- Acceptance or invariant affected: <ID or rule>
- Impact: <user or system consequence>
- Evidence: <reproduction, trace, or concrete reasoning>
- Recommended correction: <smallest safe direction, not an implementation>

## Acceptance coverage

| Acceptance ID | Evidence reviewed | Result | Notes |
| --- | --- | --- | --- |
| AC-1 | <test, code path, or artifact> | Satisfied, Unsatisfied, or Unclear | <notes> |

## Areas inspected

- Runtime paths: <scope>
- Security and permissions: <scope or not applicable>
- Data and migrations: <scope or not applicable>
- Concurrency and failure behavior: <scope or not applicable>
- Compatibility: <scope or not applicable>
- Tests and validation: <scope>

## Validation gaps and residual risk

List checks not run, inaccessible evidence, environment limitations, or remaining uncertainty. A clean review does not convert missing validation into a pass.

## Required follow-up

| Finding or gap | Owner | Required evidence for closure |
| --- | --- | --- |
| <item> | <role> | <evidence> |

