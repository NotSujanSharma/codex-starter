# Task Contract: <ID> — <Bounded Outcome>

Parent plan: <relative path>

Owner agent: <role>

Model and reasoning: <selection and short rationale>

Status: Ready | In progress | Blocked | Complete

## Objective and reason

Describe one verifiable outcome and why it exists in the parent plan.

## Authoritative inputs

- Approved requirements: <brief sections or acceptance IDs>
- Relevant files and symbols: <paths>
- Interface contracts: <links or exact description>
- Prior evidence: <exploration, reproduction, or decision references>

## Scope and ownership

- Read scope: <paths or systems>
- Exclusive write scope: <paths or read-only>
- Allowed generated or temporary artifacts: <paths or none>
- External systems allowed: <systems and actions or none>

The agent must not modify paths owned by another active writer.

## Dependencies and assumptions

- Required completed packages: <IDs or none>
- Assumptions the agent may rely on: <items>
- Blocking conditions: <conditions that require return to the main agent>

## Constraints and non-goals

- <constraint>
- Do not <adjacent or prohibited work>.

## Deliverable

Define the expected code, analysis, tests, documentation, or evidence. Name required files or output structure.

## Acceptance and validation

| Requirement | Check or command | Expected result |
| --- | --- | --- |
| <requirement> | <validation> | <observable result> |

## Authority and safety

State whether the task may add dependencies, modify data, use network access, change configuration, create commits, or interact externally. Omitted authority means the action is not allowed.

## Handoff

Return a concise handoff using `templates/HANDOFF.md`. Include exact files, commands, results, deviations, assumptions, risks, and blockers. Do not return raw command logs or claim completion without evidence.

