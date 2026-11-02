# Agentic Programming Template

This is a public, stack-agnostic template for building software with Codex. It turns the main task into an orchestrator, begins new projects with a conversational interview, makes planning and validation explicit, and uses specialized subagents only when delegation improves speed or quality.

The defaults are intentionally conservative:

- substantial work is planned with the user before implementation;
- a new project starts with an adaptive chat interview rather than asking the user to complete forms;
- the main agent owns requirements, decisions, task routing, integration, and the final result;
- subagents receive bounded task contracts and do not redefine project scope;
- read-heavy work is parallelized before write-heavy work;
- parallel writers require isolated worktrees or non-overlapping ownership;
- important changes receive independent review and validation;
- model choice follows ambiguity and risk, not file type alone;
- destructive, security-sensitive, production, and external actions require explicit authority.

## Start a new project

1. Create a repository from this template, or copy it including the hidden `.agents/` and `.codex/` directories.
2. Start a new Codex task from the repository root so the project instructions, kickoff skill, and custom agents load.
3. Describe your idea naturally, for example: `I want to build a simple platform for local sports clubs.`
4. Answer the kickoff questions in chat. You may say `I don't know`, ask for a recommendation, or skip a nonessential question.
5. Correct or approve the resulting product summary and high-level plan.
6. Codex writes the product definition, architecture, project commands, and low-level execution plan for you. You do not need to fill in the Markdown templates manually.
7. Review the model and permission defaults in [.codex/config.toml](.codex/config.toml) before implementation begins.

The kickoff skill should activate automatically for a new project. You can also invoke it explicitly:

```text
Use $project-kickoff to interview me and turn my idea into an approved product brief, architecture, and execution plan.
```

The interview asks two to five related questions per round, waits for your answers, summarizes decisions, and adapts the next questions. It does not send a giant questionnaire or begin coding before the approval gates.

## Workflow

```text
request
  -> inspect and classify
  -> conversational kickoff interview
  -> confirm product summary
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
| `.agents/skills/project-kickoff/` | Adaptive interview workflow for new projects |
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

## Publish as a GitHub template

The repository includes an MIT license, contribution guide, code of conduct, issue forms, pull-request template, and GitHub Actions validation workflow.

Before publishing:

1. Run `make validate-template`.
2. Review the default models and permissions for the audience you expect.
3. Replace generic repository descriptions or community links if desired.
4. Create the public GitHub repository and push the files.
5. In **Settings > General**, enable **Template repository**.
6. Enable private vulnerability reporting and appropriate branch protection for the default branch.

Publishing, pushing, changing GitHub settings, or creating remote resources is intentionally not automated by this template.

## Contributing

Public contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Security vulnerabilities should follow the private reporting guidance in [SECURITY.md](SECURITY.md).

## Codex behavior notes

- Project `.codex/` configuration is loaded only for a trusted repository.
- `AGENTS.md` is discovered when a Codex session starts; begin a new task after changing foundational instructions.
- Explicit user instructions and applicable nested `AGENTS.md` files override broader defaults.
- Organization-managed policies can override project permission or model settings.
- Subagents improve context isolation and wall-clock time for suitable tasks, but usually consume more total tokens than a comparable single-agent run.

The design follows the current official OpenAI guidance for [Codex best practices](https://learn.chatgpt.com/guides/best-practices), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [skills](https://learn.chatgpt.com/docs/build-skills), [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [models](https://learn.chatgpt.com/docs/models), and [worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees).
