---
name: to-tickets
description: Break a spec or plan into tickets - vertical slices with "blocked by" edges.
disable-model-invocation: true
argument-hint: "The spec (path or ticket) and where to publish"
---

Break the spec, plan, or this conversation into tickets.

Slicing rules:

- A ticket is a vertical slice: a narrow but complete path through every layer, verifiable on its own. Not a slice of one layer.
- Size: one agent completes a ticket in one fresh context.
- Every ticket lists what blocks it. Preparatory refactoring goes first.
- Do not slice a wide mechanical change (a rename or retype across the codebase) vertically. Sequence it: add the new form beside the old → migrate callers in batches, one ticket per batch → delete the old form in the last ticket.
- A ticket is understandable without this conversation: it links to the spec and does not restate it. No file paths.

Process:

1. Show the breakdown as a list: title, blocked by, what it delivers.
2. Ask: is the size right? are the edges correct? what should be merged or split? Revise until I approve.
3. After approval, publish to the place I named. If I named none, write one file per ticket to `.scratch/<feature>/tickets/NN-<title>.md`, blockers first.

Ticket template:

    # <NN>: <title>
    Spec: <link>
    What to build: the end-to-end behaviour from the user's point of view, not a list of layers.
    Blocked by: <numbers> or "nothing".
    Acceptance criteria:
    - [ ] ...
