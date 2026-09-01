# Plans

`plans/active/` contains the current source of truth for substantial work. `plans/completed/` preserves completed plans, decisions, validation evidence, and retrospectives.

Use the process in `PLANS.md` and copy from `templates/` rather than inventing a new format for each feature.

Naming convention:

```text
plans/active/<short-outcome>-brief.md
plans/active/<short-outcome>.md
```

When an outcome is genuinely complete, update final evidence and the retrospective, then move both files to `plans/completed/` without discarding decision history.

Do not put secrets, raw production data, or large command logs in plans.

