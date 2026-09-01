# Architecture Decision Records

Use an ADR for durable, cross-cutting decisions whose rationale will matter after the current feature task is complete.

Copy `templates/ADR.md` to a sequentially numbered file such as:

```text
docs/decisions/0001-use-postgresql-for-transactional-state.md
```

Create an ADR when choosing or changing:

- a system boundary or major technology;
- a public interface or compatibility strategy;
- a data ownership or migration model;
- a security or permission boundary;
- a reliability, deployment, or operational pattern;
- a dependency that meaningfully constrains future design.

Do not create ADRs for routine implementation details. Mark superseded records rather than rewriting history.

