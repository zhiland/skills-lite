---
name: lite-run-tickets
description: Implement a set of tickets with parallel subagents on one integration branch.
disable-model-invocation: true
argument-hint: "The spec and its tickets"
---

Implement every ticket of the spec on one integration branch. The tickets are a graph with "blocked by" edges, not a list of steps: any ticket whose blockers are integrated and verified can be taken.

1. Read the approved spec and tickets. Check the graph for missing blockers and cycles.
2. Create or reuse the integration branch without disturbing user changes.
3. For each ready ticket, start a separate background subagent with a fresh context, in its own worktree, on its own branch cut from the integration branch. Give it the ticket, accessible spec and repository instructions. If isolated delegation is unavailable or unauthorized, work sequentially.
4. Before reporting done, the subagent merges the current integration branch into its own branch and runs the tests.
5. Inspect and merge each finished branch one at a time. Run relevant checks on the integration tip before unblocking dependent tickets.
6. When no tickets remain, review the integration diff against the spec with a fresh subagent if available and authorized; otherwise disclose self-review. Each finding quotes the spec.
7. Fix the findings, then run required and change-relevant checks. Broaden testing only for failures or unresolved risks.
8. Remove only this run's clean, fully integrated worktrees. Report the branch, checks and what remains unverified. Do not push the branch or open a PR without my instruction.
