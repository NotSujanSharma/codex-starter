# Contributing

Thank you for helping improve this public agentic-programming template.

## Good contributions

Changes should improve a reusable workflow for a broad range of software projects. Strong contributions usually:

- remove ambiguity or duplicated instructions;
- improve interview, planning, delegation, validation, review, or safety behavior;
- fix invalid or outdated Codex configuration;
- add realistic validation without imposing a specific application stack;
- improve public-template usability or documentation.

Avoid adding personal workflow preferences as universal rules, stack-specific application code, real credentials, paid-service dependencies, or process that costs more than the failure it prevents.

## Propose a change

1. Search existing issues and pull requests.
2. For a substantial behavioral change, open a feature request describing the user problem and expected agent behavior.
3. Create a focused branch or worktree.
4. Update the smallest relevant instruction, template, skill, agent, or validator.
5. Run `make validate-template`.
6. Open a pull request using the repository template.

## Instruction changes

When changing `AGENTS.md`, `PLANS.md`, a custom agent, or the kickoff skill:

- explain which real request should behave differently;
- keep the instruction outcome-oriented;
- preserve explicit user authority and safe stopping conditions;
- avoid repeating rules already defined in another authoritative file;
- update validation when a structural invariant changes;
- consider both requests that should and should not trigger the behavior.

## Model and configuration changes

Model availability and recommended defaults change over time. Support configuration changes with current official OpenAI documentation, explain the cost, latency, and quality tradeoff, and keep the template usable when organization-managed policy overrides project settings.

## Pull-request expectations

A pull request should be narrowly scoped, explain observable behavior changes, list validation performed, disclose unresolved risks, and avoid unrelated formatting churn. Review follows `CODE_REVIEW.md` and participation follows `CODE_OF_CONDUCT.md`.

Security vulnerabilities must be reported privately according to `SECURITY.md`.

