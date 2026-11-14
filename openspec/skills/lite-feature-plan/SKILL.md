---
name: lite-feature-plan
description: Plan a large feature with a proposal, behavior spec and verifiable tasks.
disable-model-invocation: true
---

## Large features

1. A large feature starts with a folder `changes/<feature-name>/` containing `proposal.md`, `spec.md` and `tasks.md`, based on the templates in [templates](templates/proposal.md) ([spec](templates/spec.md), [tasks](templates/tasks.md)).
2. Study the code first, then ask questions. Do not ask what you can verify in code, tests or docs.
3. Ask one question at a time and say which decision it unlocks. Resolve blocking decisions before the details that depend on them. No answer is not agreement.
4. Do not write code until a human has approved `proposal.md` and `spec.md`. Reuse approval for unchanged scope.
5. `proposal.md` answers "what and why"; `spec.md` answers "how the system behaves". Fill in the "Decisions" section of `proposal.md` only for a cross-cutting change, a new dependency or a migration.
6. `spec.md` holds observable behavior only. Every requirement has at least one WHEN/THEN scenario.
7. Resolve questions that would change `spec.md` or the task breakdown before approving the affected work.
8. Every task in `tasks.md` states how to verify it: a test, a command or an observable behavior.
9. Relevant tests and docs go in the same task group as the code. The final group is for cross-cutting checks only.
10. Every task must make sense to a new agent without this conversation: it names the files or area, the requirement and the check.
11. Mark a task done only after its check has passed.
12. If requirements change mid-work, update `proposal.md`, `spec.md` and `tasks.md` first, then the code.
13. Before merging, summarize the change in the PR description. Retain the feature folder unless project policy says otherwise.

If separate tickets are used, let them own task status; `tasks.md` links to them and tracks cross-cutting checks only.
