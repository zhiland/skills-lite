# Frontier Skills Lite

Compact, opt-in workflows for capable coding agents. Keep the decisions, acceptance criteria, and handoff contracts. Load them when needed.

This project adapts ideas from [OpenSpec](https://github.com/Fission-AI/OpenSpec) and [Matt Pocock's skills](https://github.com/mattpocock/skills).
It is an independent adaptation, not an official distribution or a drop-in replacement for either project.

## Why this exists

Strong models still need the team's decisions and workflow constraints. They do not need a general engineering tutorial in every task.
This collection keeps focused interviews, behavior specs, ticket dependencies, verification evidence, and retrospective feedback.
It shortens the supplied local adaptations while preserving their wording and structure.
Changes target concrete problems, including unnecessary approval stops and unsafe cleanup.

The design targets current frontier coding models. This is a design premise, not proof that a model makes the original skills obsolete.
There is no measured claim of better quality, lower cost, or a particular token saving. See [review and limitations](docs/REVIEW.md).

## Two independent collections

| Collection | Skill | Use it for |
| --- | --- | --- |
| `openspec` | `lite-feature-plan` | Proposal, behavior spec, and verifiable tasks for a substantial feature |
| `openspec` | `lite-adaptation-review` | Evidence-based adoption review within an agreed project scope |
| `matt-pocock-skills` | `lite-grill` | Decisions that block a feature or plan |
| `matt-pocock-skills` | `lite-feature-spec` | A compact spec from settled decisions |
| `matt-pocock-skills` | `lite-to-tickets` | Verifiable slices and dependency edges |
| `matt-pocock-skills` | `lite-run-tickets` | Implementation, controlled integration, and final verification |
| `matt-pocock-skills` | `lite-retro` | Evidence-backed environment improvements |
| `matt-pocock-skills` | `lite-ask-person` | A questionnaire, saved locally |

Each skill is self-contained. No skill requires another installed skill, MCP server, API key, or external CLI.
The planning skill includes its own templates. Parallel execution requires a harness with isolated worktrees and authorized delegation.
The runner also supports sequential execution.

`lite-adaptation-review` is a locally originated companion. It is grouped with the OpenSpec review materials, not attributed to OpenSpec's authors.
[Optional project rules](matt-pocock-skills/OPTIONAL-RULES.md) are available separately. They are not installed automatically.

## Choose one planning path

- **Artifact-based:** `lite-feature-plan` produces proposal, spec, and tasks. Add tickets only when separate handoffs are useful.
- **Conversation-based:** `lite-grill` → `lite-feature-spec` → `lite-to-tickets` → `lite-run-tickets`.

These are suggested sequences, not automatic chains. Invoke each skill when needed. Reuse existing artifacts instead of creating competing specs.
The OpenSpec-inspired templates are plain Markdown. They omit live-spec delta merging, archive commands, and OpenSpec validation.
Use upstream OpenSpec when those capabilities are part of your team's process.

## Install selected skills

Clone this repository, then run these commands **from its root**. Copy only the skills you intend to use.
The examples install one skill. Repeat with another source folder as needed. A pre-existing destination causes the copy to stop.

### Claude Code

```sh
python3 scripts/install.py openspec/skills/lite-feature-plan --dest "$HOME/.claude/skills"
```

For a project, pass `/path/to/project/.claude/skills` instead.
Invoke `/lite-feature-plan Describe the feature here`.

### Codex

```sh
python3 scripts/install.py openspec/skills/lite-feature-plan --dest "$HOME/.agents/skills"
```

For a project, pass `/path/to/project/.agents/skills` instead.
Invoke `$lite-feature-plan` with the feature request.

Codex can select installed skills automatically when they match the task. Explicit `$skill-name` invocation also works.
No `agents/openai.yaml` is needed: automatic invocation is Codex's default.
Claude Code remains manual-only through `disable-model-invocation: true` in each `SKILL.md`.

Codex can use skill names and descriptions for discovery; the full instructions load when a skill is selected.
Keep installed skills relevant and descriptions concise. Actual context use depends on the client and version.
Verify discovery and invocation in your installed client before wider rollout.
If updating an earlier copy, remove its old `agents/openai.yaml` or replace that skill folder deliberately.

References: [Claude skills](https://code.claude.com/docs/en/skills), [Codex skills](https://developers.openai.com/codex/skills).
No setup command edits your global instructions. To update an existing installation, review the diff and replace that selected folder deliberately.

## Review and validation

Requires Python 3.10+ and PyYAML for validation. The installer uses only the Python standard library.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests
```

Validation checks metadata, invocation policy, local links, and packaging. Tests check installation boundaries and collision behavior.
These checks do not prove agent behavior. The review includes a manual scenario walkthrough, not a live multi-agent implementation benchmark.
The current revision returns to the local source drafts after an earlier rewrite changed too much of their wording.

Read [REVIEW.md](docs/REVIEW.md) for corrections, [EVALUATION.md](docs/EVALUATION.md) for the runtime trial protocol,
and [SOURCES.md](SOURCES.md) for pinned upstream provenance.

## Revision history

The first three commits preserve the original local drafts, the first rewrite, and the final conservative revision.
[Browse the history and compare versions](docs/HISTORY.md).

## Publish or contribute

This is a standalone Git repository. No account, remote URL, or private project data is required.
[Publication notes](docs/PUBLISHING.md) explain the repository setup and how to publish a separate fork.
Changes should address a demonstrated failure or a concrete workflow need. Keep each skill independently installable.
Run validation, describe the behavioral change, and state whether it was tested in a real client.
Do not add model superiority claims without reproducible evidence.

## License

MIT. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
Upstream notices are retained, including inside installable skill folders. The respective authors do not endorse this adaptation.
