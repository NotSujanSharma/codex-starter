# Adaptive Project Interview Guide

Use this guide to choose relevant questions, not as a script to recite. Begin with the product outcome, then follow uncertainty and risk. Skip lanes that repository evidence or prior answers already resolve.

## Round design

- Ask two to five related questions at a time.
- Start with broad product language and become more specific only where the answer changes the plan.
- Prefer examples over abstract requirement language: “Walk me through what the user does” is often better than “List functional requirements.”
- Offer a recommendation when the user lacks a preference.
- End each round with a compact decision summary and name the next topic.
- Do not ask low-value questions merely to complete every section.

## Lane 1: Product outcome and users

Establish why the product should exist.

Possible questions:

- What do you want to build, in your own words?
- Who is the primary user, and what are they trying to accomplish?
- What do they do today, and what is frustrating or expensive about it?
- What would make the first version genuinely useful rather than only demonstrable?
- How will you know the product is succeeding?

Do not force business metrics for a personal or exploratory project. An observable user outcome may be enough.

## Lane 2: Experience, workflow, and scope

Make the critical behavior concrete.

Possible questions:

- Walk through the main user journey from entry to a successful result.
- What inputs does the user provide, and what output do they expect?
- Which capabilities are essential for the first usable version?
- What should explicitly wait until later?
- Which error, empty, loading, offline, or recovery states matter?
- Are there different user roles or permission levels?

Use examples or Given/When/Then scenarios when words such as “simple,” “automatic,” “real time,” or “secure” hide ambiguity.

## Lane 3: Platform, technology, and integrations

Ask only choices that affect architecture or delivery.

Possible questions:

- Is this primarily web, mobile, desktop, CLI, API, library, or a combination?
- Do you have a required or preferred stack? If not, may the agent recommend one?
- Must it integrate with existing services, devices, data sources, or accounts?
- Where should it run or be hosted?
- Are there compatibility requirements for browsers, operating systems, API clients, or existing data?
- What budget, timeline, team skill, or maintenance constraints matter?

When recommending a stack, optimize for the stated users, delivery constraints, existing expertise, operations, and longevity—not novelty.

## Lane 4: Data, identity, security, and privacy

Use this lane whenever the product stores user data, has accounts, accepts untrusted input, moves money, communicates externally, or touches sensitive domains.

Possible questions:

- What data enters the system, where does it come from, and what must be stored?
- Is any data personal, confidential, regulated, financial, health-related, or otherwise sensitive?
- Does the product need accounts, organizations, roles, invitations, or anonymous access?
- Who may read, change, export, or delete each kind of data?
- How long should data be retained, and must users be able to remove it?
- Are there geographic, regulatory, audit, or consent requirements?
- Which external actions require confirmation or an audit trail?

Do not imply compliance merely because controls are planned. Record compliance as a requirement needing specific evidence.

## Lane 5: Quality and operations

Calibrate engineering effort to realistic risk.

Possible questions:

- What scale and traffic should the first version support?
- Which actions have latency expectations?
- What happens if a dependency is slow, unavailable, or returns partial results?
- What accessibility, localization, or usability requirements matter?
- What logging, analytics, monitoring, or support visibility is needed?
- How should releases, rollback, backups, and recovery work?
- Which environments are needed: local, test, staging, production?

Do not design enterprise operations for a disposable prototype unless the user needs them.

## Lane 6: Delivery, acceptance, and authority

Define what the agent may build and what proves it is done.

Possible questions:

- What should the first milestone demonstrate end to end?
- Which scenarios must pass before you would call the first version complete?
- Are there existing examples, competitors, designs, or APIs to follow or avoid?
- May the project add production dependencies, create accounts, or use paid services?
- Which decisions require the user's approval during implementation?
- Is there a deadline or preferred sequence of delivery?

Translate answers into observable acceptance criteria and explicit authority boundaries.

## Resolving “I don't know”

When the user is uncertain:

1. Explain why the decision matters now or why it can be deferred.
2. Offer one recommended default and at most two meaningful alternatives.
3. State the main cost, risk, or lock-in of the recommendation.
4. Ask the user to accept the default, choose an alternative, or defer with a named decision point.

Do not turn uncertainty into an unsupported fact.

## Readiness check

The interview is ready for the product-summary approval gate when these are sufficiently clear:

- primary user and desired outcome;
- main journey and first-version scope;
- non-goals;
- platform and material integrations;
- important data and permission boundaries;
- quality and delivery constraints proportional to risk;
- observable acceptance criteria;
- blocking decisions and authority.

Minor visual preferences, internal names, and reversible implementation details may remain open for the execution plan.
