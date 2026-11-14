---
name: lite-to-tickets
description: Break a spec or plan into tickets - vertical slices with "blocked by" edges.
disable-model-invocation: true
argument-hint: "The spec (path or ticket) and where to publish"
---

Break the spec, plan, or this conversation into tickets.

Slicing rules:

- A ticket is a vertical slice: a narrow but complete behaviour, verifiable on its own.
- Size: one agent completes a ticket in one fresh context.
- Every ticket lists what blocks it. Check for missing blockers and cycles.
- For a wide mechanical change: add the new form beside the old → migrate callers in batches → delete the old form.
- A ticket is understandable without this conversation: it links to an accessible spec and states its own outcome and checks.

Process:

1. Draft the breakdown locally: title, blocked by, what it delivers. Cover every in-scope requirement.
2. Ask about size and dependencies unless I already approved this breakdown.
3. Use the place I named; otherwise `.scratch/<feature>/tickets/NN-<title>.md`, blockers first. Publish externally only when requested.

Ticket template:

    # <NN>: <title>
    Spec: <link and requirement IDs>
    What to build: the end-to-end behaviour from the user's point of view.
    Blocked by: <numbers> or "nothing".
    Acceptance criteria:
    - [ ] ...
    Check: <command or observable result>
