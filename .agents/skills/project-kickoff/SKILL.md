---
name: project-kickoff
description: Interview the user to turn a new or incomplete software-product idea into an approved product brief, initial architecture, and execution plan before implementation. Use when starting this template, bootstrapping a new project, or being asked to build a new product from a vague idea. Do not use for routine feature work in an established project.
---

# Project Kickoff Interview

Turn the user's idea into enough shared understanding to plan responsibly without asking them to fill repository forms.

## Start the interview

1. Inspect `README.md`, `AGENTS.md`, `docs/PRODUCT.md`, `docs/ARCHITECTURE.md`, and any existing code or plans.
2. Decide whether this is an untouched starter, a partially initialized project, or an established project. Use this skill only for the first two cases.
3. Tell the user you will conduct a short adaptive interview and that they can answer informally, say “I don't know,” ask for a recommendation, or skip a nonessential question.
4. Read [the interview guide](references/interview-guide.md) and select only the lanes that can materially change this project.

## Conduct the conversation

- Ask one round of two to five related questions, then wait for the user's answers.
- Use plain language. Explain technical choices only when the user needs to decide between meaningful tradeoffs.
- Do not send a giant questionnaire and do not ask the user to edit template files.
- Do not ask for facts already available in the repository.
- When the user is unsure, recommend a default, explain its main tradeoff, and ask them to accept or change it.
- After each round, briefly summarize confirmed decisions, assumptions, and remaining uncertainty before choosing the next questions.
- Challenge contradictions, risky assumptions, and accidental scope expansion with concrete consequences.
- Ask follow-ups only when the answer can change behavior, architecture, authority, acceptance, or risk.
- During the interview, use only read-only exploration needed to understand existing work. Do not start implementation agents.

## Approval gates

When enough information is available, present a concise kickoff summary containing:

- product problem and desired outcome;
- primary users and critical journeys;
- MVP scope and non-goals;
- platform, stack preferences, and integrations;
- data, security, privacy, and permission boundaries;
- quality, operational, delivery, and compatibility constraints;
- measurable acceptance criteria;
- recommended defaults, assumptions, risks, and unresolved decisions.

Ask the user to correct or approve this summary. Do not treat silence or partial answers as approval.

After the summary is approved:

1. Draft the high-level architecture and milestone plan with alternatives only where the tradeoff is material.
2. Ask the user to approve or revise the high-level plan.
3. Only after that approval, write the durable project artifacts and low-level task graph.

If the user explicitly requests autonomous decisions, select reversible defaults and label them. Still stop for missing authority, destructive or production actions, sensitive data, credentials, external side effects, or irreversible architecture decisions.

## Write the project artifacts

After both approval gates:

- replace the starter content in `docs/PRODUCT.md` with the approved product definition;
- replace the starter content in `docs/ARCHITECTURE.md` with the approved initial architecture;
- create the project bootstrap brief and execution plan in `plans/active/` from the repository templates;
- update the repository map and exact executable commands in `AGENTS.md` when the chosen stack makes them known;
- create ADRs only for durable cross-cutting decisions;
- preserve open but non-blocking decisions with an owner and decision point.

Do not begin implementation in the same step as writing an unapproved plan. Once the user approves the plan, return control to the normal orchestration, delegation, implementation, validation, and review rules in `AGENTS.md`.

## Completion

The kickoff is complete when the user has approved the product summary and high-level plan, the durable files reflect those decisions, the low-level execution plan is traceable to acceptance criteria, and no material blocking question is hidden.

End with a short report listing the files created or updated, approved decisions, remaining non-blocking questions, and the exact next implementation milestone.
