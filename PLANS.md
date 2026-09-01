# Collaborative Planning Standard

Use this standard for new projects, substantial features, ambiguous changes, cross-cutting work, and high-risk fixes. `AGENTS.md` decides when the standard is required.

The plan is a shared source of truth, not a prediction that must remain unchanged. It should be understandable by a new agent with repository access and no hidden conversation context.

## Planning sequence

### 1. Inspect before interviewing

Map the relevant repository structure, existing behavior, tests, documentation, constraints, and recent user changes. Separate facts discoverable from the repository from product or risk decisions that require the user.

### 2. Conduct material discovery

Ask questions in one organized batch when possible. Cover only topics that can change the result:

- users, use cases, and desired outcome;
- in-scope and out-of-scope behavior;
- acceptance criteria and examples;
- architecture, technology, and compatibility constraints;
- data ownership, retention, privacy, and migration needs;
- security and permission boundaries;
- performance, reliability, and operational expectations;
- deployment, rollback, observability, and support needs.

Do not ask the user for facts that repository inspection can establish. When answers expose a genuinely new decision, ask a narrow follow-up instead of restarting discovery.

### 3. Approve the feature brief

Copy `templates/FEATURE_BRIEF.md` into `plans/active/<outcome>-brief.md`. Resolve or explicitly accept every material open question. Obtain user approval before implementing substantial work unless the user has requested autonomous execution.

### 4. Approve the high-level plan

Describe system boundaries, interfaces, data flow, milestones, risk, failure behavior, and rollback. Present alternatives only when they materially affect cost, behavior, maintainability, or risk. Record the decision and rationale.

### 5. Build the low-level task graph

Copy `templates/EXECUTION_PLAN.md` into `plans/active/<outcome>.md`. Split work by dependency and ownership, not by arbitrary file counts. Each work package must be independently understandable and verifiable.

For every package, record:

- dependency IDs;
- owner role;
- model and reasoning effort;
- read and write scope;
- interface contract;
- validation;
- completion evidence;
- whether independent review is required.

### 6. Execute and maintain

Update progress and decisions as work proceeds. If reality differs from the plan:

- record the evidence;
- assess which packages are affected;
- stop only the affected work;
- revise the plan;
- seek approval when behavior, authority, risk, or irreversible design changes.

### 7. Integrate and close

Integrate in dependency order. Complete the acceptance matrix, run validation, perform independent review, and record deviations and remaining risk. Move the plan to `plans/completed/` only after the requested outcome is genuinely complete.

## Planning quality rules

- Express work as observable outcomes, not vague activities.
- Include non-goals to prevent accidental expansion.
- Tie each acceptance criterion to implementation and evidence.
- Prefer a small number of coherent milestones over a long checklist of tiny edits.
- Identify the critical path and safe parallel work.
- Stabilize shared interfaces before parallel implementation.
- Assign a single writer to each file or subsystem at a time.
- Include failure, rollback, security, privacy, and operational behavior where relevant.
- Name exact commands when known; otherwise include a task to establish them.
- Keep decision history concise but never silently rewrite an approved decision.
- End with a definition of done and explicit stop conditions.

## When a plan may be skipped

A formal plan may be skipped for a small, reversible, well-understood change with known validation and no architectural or security impact. The agent must still state assumptions, validate the result, and inspect the diff.

