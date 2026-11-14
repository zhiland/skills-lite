---
name: lite-retro
description: "Review a session and propose evidence-backed improvements to the agent environment."
disable-model-invocation: true
---

# Retro

Review the specified session, or this conversation by default. Propose changes without applying them.
Use only relevant records within the authorized scope. State missing evidence instead of searching unrelated private history.

Look for:
- Repeated navigation failures that a precise pointer could prevent.
- Mechanical errors that an existing or new automated check could catch. Inspect current checks before proposing another.
- Judgment failures that need review guidance.
- Conflicting or redundant instructions. Treat a suspected no-op as a hypothesis unless behavior supports it.
- Unnecessary tool calls or unavailable information that affected the outcome.

Order findings by impact. For each, give the observed event, proposed location and change, expected benefit, and a way to check it.
Prefer a narrow correction over a global rule based on one incident. Report no findings when the evidence supports none.
