---
name: lite-to-tickets
description: "Split an approved spec into independently verifiable tickets with explicit dependencies."
disable-model-invocation: true
---

# To tickets

Read the spec and relevant code. If decisions remain open, identify the blockers before marking tickets ready.
Prefer vertical slices that deliver a narrow behavior through the layers it actually needs.
Use preparatory refactoring only when it enables the feature. For wide migrations, use expand, migrate, and contract stages.

1. Draft one ticket per bounded outcome. Include its requirement IDs, dependency IDs, and verification method.
2. Check that IDs are unique, blockers exist, and the graph has no cycles. Check that all in-scope requirements are covered.
3. Present the breakdown for approval. Reuse approval already given for an unchanged breakdown.
4. Write approved tickets to the requested location. Default to `changes/<feature>/tickets/NN-title.md`.
   External publication requires a request that identifies the tracker and scope. Approval of content alone is not publication permission.

Each ticket contains:

    # T01: <title>
    Spec: <relative link or stable URL, and revision>
    Requirements: <IDs>
    Outcome: <observable behavior>
    Area: <modules or current file paths for navigation>
    Blocked by: <ticket IDs or none>
    Acceptance criteria: <observable checks>
    Verification: <commands or manual procedure, and expected results>
    Status: pending | running | blocked | verified
    Evidence: <filled after execution>

Tickets must make sense without this conversation. Include task-specific constraints and link shared decisions rather than copying the whole spec.
Ensure a worker can access the linked spec. Local artifacts must reach its worktree before dispatch.
Document overlapping files or shared interfaces that require sequencing.
A closed tracker issue does not prove a dependency was integrated and verified.
