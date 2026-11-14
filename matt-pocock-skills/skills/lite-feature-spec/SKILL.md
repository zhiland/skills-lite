---
name: lite-feature-spec
description: "Turn settled decisions into a compact feature spec with acceptance scenarios."
disable-model-invocation: true
---

# Feature spec

Synthesize the conversation and supplied artifacts. Read the relevant code if needed. Do not restart the interview.

Write to the requested location or the existing project convention. Otherwise use `changes/<feature>/spec.md` and report the path.
Preserve existing content. If the target is an OpenSpec-inspired behavior spec, keep technical decisions in its proposal or design document.

Include:
- Problem and intended outcome.
- Requirements with stable IDs and observable WHEN/THEN scenarios.
- Relevant failure and boundary cases supported by the agreed scope.
- Confirmed implementation constraints, separate from observable requirements.
- Verification approach and relevant existing tests or file paths as navigation aids.
- Out of scope, assumptions, unresolved decisions, and approval status.

Prefer existing test boundaries. Select test levels for useful coverage and feedback speed, not a fixed minimum number of boundaries.
A proposed test approach is a proposal until approved when approval is required by the project.
If a missing decision changes behavior or scope, mark the spec as draft and ask only the blocking question.
Do not invent an answer or mark the spec ready for implementation.

The spec records this change. Preserve it after merge according to project policy. It need not become a continuously maintained system specification.
Local drafting does not authorize tracker publication.
