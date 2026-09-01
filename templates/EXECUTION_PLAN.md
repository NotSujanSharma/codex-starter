# Execution Plan: <Outcome>

Status: Draft | Approved | In progress | Blocked | Complete | Superseded

Feature brief: <relative path>

Plan owner: Main agent

Created: <YYYY-MM-DD>

Last updated: <YYYY-MM-DD HH:MM timezone>

## Objective and definition of done

State the approved outcome and the exact conditions required for completion.

## Progress

- [ ] Brief and high-level plan approved.
- [ ] Interfaces and ownership boundaries stabilized.
- [ ] Work packages completed in dependency order.
- [ ] Acceptance criteria validated.
- [ ] Independent review completed.
- [ ] Findings resolved and revalidated.
- [ ] Documentation and plan closure completed.

## Current-state summary

Summarize the relevant architecture, behavior, constraints, and evidence. Link to authoritative repository files.

## High-level design

### System boundaries and data flow

Describe components, entry points, state transitions, external calls, and trust boundaries. Include a diagram only if it materially improves clarity.

### Interfaces and contracts

| Interface | Owner | Current or new behavior | Compatibility requirement |
| --- | --- | --- | --- |
| <interface> | <owner> | <behavior> | <requirement> |

### Failure and rollback behavior

Describe expected errors, partial failure, retries, idempotency, recovery, migration ordering, feature flags, and rollback.

## Milestones and critical path

| Milestone | Outcome | Dependencies | Exit evidence |
| --- | --- | --- | --- |
| M1 | <outcome> | <IDs or none> | <evidence> |

Identify the critical path and which milestones may run safely in parallel.

## Work-package graph

| ID | Outcome | Owner agent | Model and effort | Dependencies | Write scope | Validation | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WP-1 | <bounded outcome> | <role> | <choice and rationale> | <IDs or none> | <paths or read-only> | <checks> | Pending |

Create a task contract from `templates/TASK_CONTRACT.md` for every delegated package. Shared interfaces must be resolved before dependent packages run.

## Parallelization and file ownership

| Path or subsystem | Writer | Isolation | Active during | Notes |
| --- | --- | --- | --- | --- |
| <scope> | <agent> | <worktree, branch, or disjoint path> | <work package IDs> | <coordination rule> |

Serialize overlapping writes when isolation is unavailable.

## Acceptance matrix

| Acceptance ID | Implementation location | Test or evidence | Status |
| --- | --- | --- | --- |
| AC-1 | <file or component> | <command, test, or inspection> | Pending |

## Validation plan

List exact targeted tests, broader suites, lint, formatting, type checks, builds, integration or browser checks, security checks, and manual evidence. Identify the independent verifier.

## Review plan

Name the independent reviewer, distinct review concerns, required inputs, and blocking threshold. Use additional reviewers only for distinct high-risk questions.

## Security, privacy, and operational impact

Address permissions, secrets, untrusted inputs, data classification, retention, migrations, observability, deployment, and support implications. State when a category is not applicable and why.

## Risks and stop conditions

| Risk or stop condition | Signal | Response | Authority required |
| --- | --- | --- | --- |
| <risk> | <evidence> | <mitigation or stop> | <user, owner, or none> |

## Decision log

| Date | Decision | Evidence and rationale | Approved by | Affected packages |
| --- | --- | --- | --- | --- |
| <date> | <decision> | <basis> | <authority> | <IDs> |

## Deviations and blockers

Record what changed from the approved plan, why, impact, and any approval. Never silently rewrite history.

## Final evidence

Complete before closure:

- Acceptance matrix result: <summary>
- Validation commands and results: <summary or links>
- Independent review verdict: <verdict and report path>
- Documentation updated: <paths>
- Residual risk or limitations: <items or none>
- Rollback readiness: <status>

## Retrospective

- What went well?
- What caused rework, confusion, or delay?
- Did delegation improve speed or quality?
- Was model routing appropriate?
- Were there file conflicts, duplicated work, or missing context?
- Is any lesson durable enough to update `AGENTS.md`, a template, or a reusable workflow?

