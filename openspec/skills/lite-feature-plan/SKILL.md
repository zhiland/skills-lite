---
name: lite-feature-plan
description: "Plan a substantial feature with a proposal, behavior scenarios, and verifiable tasks."
disable-model-invocation: true
---

# Feature plan

Use this workflow for a feature that needs review or handoff. A small, clear edit does not need these artifacts.

1. Read the relevant code, tests, and project instructions. Reuse an existing plan and its approved decisions.
2. Resolve questions that change scope, observable behavior, or task dependencies. Ask only for missing decisions or inaccessible facts.
3. Use the project's planning location. Otherwise create `changes/<feature>/` with the [templates](templates/proposal.md): `proposal.md`, `spec.md`, and `tasks.md`.
4. Record confirmed decisions separately from assumptions. Include requirement IDs and WHEN/THEN scenarios with observable outcomes.
5. Put technical choices in the proposal's Decisions section. Use `design.md` only when those choices need substantial explanation.
6. Give each task an area, requirement IDs, dependencies, and a concrete check. Include relevant tests and docs with its code.
7. Present the artifacts for approval before implementation. Existing explicit approval covers unchanged scope. Silence does not approve a plan.

This invocation creates a plan, not feature code. A draft with blocking questions remains a draft. Do not mark it ready.

During later implementation, revise affected artifacts when requirements change. Obtain approval for material scope changes before implementing them.
Mark work verified only when its check passes. Record unavailable checks as unverified.
Keep the plan as a historical record after merge unless the project specifies another retention policy. Never delete it automatically.

These templates are independent Markdown. They are not OpenSpec CLI schemas or delta specs.

Template entry points: [proposal](templates/proposal.md), [behavior](templates/spec.md), [tasks](templates/tasks.md).
