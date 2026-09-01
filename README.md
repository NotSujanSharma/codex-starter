# Agentic Programming Starter

This repository is a stack-agnostic starting point for building software with Codex. It turns the main task into an orchestrator, makes planning and validation explicit, and uses specialized subagents only when delegation improves speed or quality.

The defaults are intentionally conservative:

- substantial work is planned with the user before implementation;
- the main agent owns requirements, decisions, task routing, integration, and the final result;
- subagents receive bounded task contracts and do not redefine project scope;
- read-heavy work is parallelized before write-heavy work;
- parallel writers require isolated worktrees or non-overlapping ownership;
- important changes receive independent review and validation;
- model choice follows ambiguity and risk, not file type alone;
- destructive, security-sensitive, production, and external actions require explicit authority.

## Start a new project

1. Copy this repository, including hidden `.codex/` files, into the new project.
2. Fill in [the product brief](docs/PRODUCT.md) and [architecture overview](docs/ARCHITECTURE.md). It is fine to ask Codex to interview you and draft them.
3. Update the project commands and repository map in [AGENTS.md](AGENTS.md) after the initial stack is selected.
4. Review the model and permission defaults in [.codex/config.toml](.codex/config.toml).
5. Start a new Codex task from the repository root so the project instructions and custom agents are loaded.
6. Ask for a coherent outcome, for example: `Build the account invitation feature.` The main agent will choose the fast path or the planned workflow defined in [AGENTS.md](AGENTS.md).

For a brand-new or ambiguous product, a useful opening request is:

```text
Interview me to turn this idea into an approved feature brief. Inspect the repository first, ask only material questions, challenge risky assumptions, and do not implement until we agree on the brief and high-level plan.
```

## Workflow

```text
request
  -> inspect and classify
  -> discover requirements
  -> approve feature brief
  -> approve high-level plan
  -> create low-level task graph
  -> explore in parallel
  -> implement isolated work packages
  -> integrate and validate
  -> independent review
  -> final evidence and retrospective
```

Small, reversible, well-scoped changes use a fast path and do not require ceremonial planning or delegation.

## Repository map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Durable operating agreement automatically supplied to Codex |
| `PLANS.md` | Standard for collaborative briefs and execution plans |
| `.codex/config.toml` | Safe project defaults and multi-agent concurrency limits |
| `.codex/agents/` | Narrow custom agent definitions and model assignments |
| `templates/` | Feature brief, execution plan, work contract, handoff, review, and ADR templates |
| `plans/active/` | Source-of-truth plans for work in progress |
| `plans/completed/` | Completed plans retained for decisions and retrospectives |
| `docs/` | Product, architecture, and durable decision context |
| `CODE_REVIEW.md` | Independent review standard |
| `SECURITY.md` | Safety, secrets, dependency, data, and external-action rules |
| `scripts/validate_template.py` | Structural and TOML validation for this starter |

## Built-in agent roles

| Agent | Default model | Role |
| --- | --- | --- |
| `explorer` | Luna, medium | Read-only codebase and evidence mapping |
| `implementer` | Terra, medium | Scoped routine implementation |
| `debugger` | Sol, high | Ambiguous failures and difficult logic |
| `verifier` | Terra, medium | Independent command execution and evidence collection |
| `reviewer` | Sol, high | Read-only correctness, security, and regression review |
| `documenter` | Luna, low | Source-grounded documentation updates |

These are starting points. Measure quality, elapsed time, retries, token use, merge conflicts, and escaped defects, then adjust routing based on evidence.

## Validate the starter

Run:

```bash
python3 scripts/validate_template.py
```

This checks the required structure, parses all TOML configuration, verifies agent fields and model routing, checks instruction size, and reports broken relative Markdown links.

## Codex behavior notes

- Project `.codex/` configuration is loaded only for a trusted repository.
- `AGENTS.md` is discovered when a Codex session starts; begin a new task after changing foundational instructions.
- Explicit user instructions and applicable nested `AGENTS.md` files override broader defaults.
- Organization-managed policies can override project permission or model settings.
- Subagents improve context isolation and wall-clock time for suitable tasks, but usually consume more total tokens than a comparable single-agent run.

The design follows the current official OpenAI guidance for [Codex best practices](https://learn.chatgpt.com/guides/best-practices), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [models](https://learn.chatgpt.com/docs/models), and [worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees).

