---
name: lite-run-tickets
description: "Implement approved tickets, integrate their changes, and verify the result against the spec."
disable-model-invocation: true
---

# Run tickets

Read the approved spec, tickets, and repository instructions. Verify the base branch, working-tree state, and required checks.
If approval or source artifacts are missing, resolve that blocker before implementation.
Reuse an existing integration branch when appropriate. Otherwise create a new branch from the agreed base without disturbing user changes.

1. Validate unique ticket IDs, existing blockers, and an acyclic dependency graph. A dependency is ready only after integration and verification.
2. Use parallel workers only when the harness supports isolated worktrees and delegation is authorized. Otherwise execute sequentially.
   Do not simulate isolation by allowing concurrent writers in one checkout. Sequence tickets with conflicting ownership or interfaces.
3. Start each worker from the current integration commit. Supply the ticket, accessible spec revision, applicable instructions, and verification commands.
   Ensure uncommitted planning files are available in that worktree without staging unrelated user files.
4. Each worker reports its commit, changed files, checks, and unresolved issues. A worker report is evidence to inspect, not acceptance.
5. Integrate one result at a time. Inspect the diff and resolve conflicts deliberately. Run relevant checks on the new integration tip.
   If the tip changes during a worker's run, recheck its result against that tip. Mark the ticket verified only after integration checks pass.
6. Review the complete diff against each requirement and acceptance scenario. Use a fresh reviewer if available and authorized.
   Otherwise perform a separate review pass and disclose the lack of independent review. Fix concrete findings and rerun affected checks.
7. Run the project's required final checks. Report the integration commit, requirement coverage, passed checks, and remaining limits.

A failed or unavailable required check keeps affected work unverified. Preserve work when blocked.
If no ticket is ready while unfinished work remains, report the dependency or approval blocker instead of looping.
Remove only worktrees created by this run after their commits are integrated and their working trees contain no uncommitted or untracked work.
Preserve uncertain worktrees and report their paths. Never force cleanup or reset user changes.
Push, PR creation, and tracker updates require explicit instructions for those actions.
