# Publish as a new GitHub project

The local repository is prepared on `main`. Review its README, license, and initial commit before publication.
No remote is configured and no GitHub repository was created by the packaging task.

From this repository root, after authenticating GitHub CLI:

```sh
gh repo create frontier-skills-lite --public --source=. --remote=origin --push
```

This command creates a public project under the authenticated account and pushes the current branch.
For an organization, specify `ORG/frontier-skills-lite`. Choose visibility deliberately before running it.

Suggested description:

> Compact, opt-in coding-agent workflows adapted from OpenSpec and Matt Pocock's skills, with explicit verification and minimal context overhead.

Suggested topics: `agent-skills`, `claude-code`, `codex`, `spec-driven-development`, `developer-tools`.

The CI workflow validates packaging and runs installation tests. GitHub execution is not verified until the first push completes.
