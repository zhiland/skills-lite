---
name: run-tickets
description: Implement a set of tickets with parallel subagents on one integration branch.
disable-model-invocation: true
argument-hint: "The spec and its tickets"
---

Implement every ticket of the spec on one integration branch. The tickets are a graph with "blocked by" edges, not a list of steps: any ticket whose blockers are all closed can be taken.

1. Read the spec and the tickets, and build the graph.
2. Create the integration branch.
3. For each ready ticket, start a separate background subagent with a fresh context, in its own worktree, on its own branch cut from the integration branch. Give it only links to the ticket and the spec, with no restatement.
4. Before reporting done, the subagent merges the current integration branch into its own branch and runs the tests.
5. Merge each finished branch into the integration branch. If that unblocks new tickets, start them.
6. When no tickets remain, a separate subagent with a fresh context checks the integration diff against the spec: what is missing or partial, what was not asked for, what is implemented wrongly. Each finding quotes the spec.
7. Fix the findings with one subagent, then run the full test suite.
8. Remove the subagents' worktrees. Report the branch and what is left undone. Do not push the branch or open a PR without my instruction.
