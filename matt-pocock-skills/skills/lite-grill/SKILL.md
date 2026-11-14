---
name: lite-grill
description: "Resolve decisions that block a feature or plan through a focused interview."
disable-model-invocation: true
---

# Grill

Read the relevant code and supplied artifacts before asking factual questions. Use the user's selected project scope.
Interview about unresolved decisions, not facts you can verify.

- Ask a small round of independent questions. Ask dependent questions after their prerequisites are settled.
- Give a recommendation when evidence supports one. State alternatives and tradeoffs without steering every answer toward yes.
- Resolve contradictions between the requested behavior and the current system. Distinguish current behavior from desired behavior.
- Use concrete boundary cases to test ambiguous requirements and overloaded terms.
- Keep confirmed decisions, proposed defaults, and unresolved questions separate. Silence is not acceptance.

Finish when scope, success criteria, and decisions needed for the next step are clear and the user confirms the summary.
List deferred questions with their impact. Do not expand the interview to unrelated branches.
This invocation produces a decision summary. Write a spec or implementation only if the user requests that next action.
