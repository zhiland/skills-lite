# Skills Lite

Compact versions of [OpenSpec v2.0.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.0.0)-inspired workflows and [Matt Pocock's skills v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2) for the frontier coding models available in **November 2026**.

## Why this exists

Instructions accumulate as we work around older models' limitations. Newer models may already handle those tasks, while the old guidance remains: repeated advice, rigid recipes, and conflicting rules that consume context or get in the way.

[Addy Osmani recommends auditing agent files](https://addyosmani.com/blog/audit-your-agent-files/) as models improve.
[Anthropic describes simplifying context for Claude 5 models](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) to avoid unnecessary constraints.

This project applies that idea to two skill collections:

- **Approach:** reviewed and edited with Claude Fable 5.2 and GPT-6 Astra to shorten general guidance, preserve useful workflow choices, and keep the original wording where it works.
- **Intended audience:** users of current frontier models, rather than models that need extensive procedural guidance.
- **Evidence:** reviewed adaptations, not benchmark-proven replacements for the upstream collections.
- **Sources:** exact source details are in [SOURCES.md](SOURCES.md).

## Skills

| Folder | Skill | Purpose |
| --- | --- | --- |
| `openspec` | `lite-feature-plan` | Proposal, behavior spec, and tasks |
| `openspec` | `lite-adaptation-review` | Evaluate a skill or tool for your project¹ |
| `matt-pocock-skills` | `lite-grill` | Resolve blocking decisions |
| `matt-pocock-skills` | `lite-feature-spec` | Turn settled decisions into a spec |
| `matt-pocock-skills` | `lite-to-tickets` | Split a spec into verifiable tickets |
| `matt-pocock-skills` | `lite-run-tickets` | Implement, integrate, and verify tickets |
| `matt-pocock-skills` | `lite-retro` | Review the agent's working environment |
| `matt-pocock-skills` | `lite-ask-person` | Draft a questionnaire |

¹ An original companion skill, not an upstream OpenSpec skill.

## What we kept and left out

| Source material | Decision and reason |
| --- | --- |
| Matt Pocock: `grilling`, `to-tickets`, `implement-spec`, `retro`, `to-questionnaire` | Keep their workflow core: decisions, handoffs, verification, and output formats. |
| Matt Pocock: `to-spec` | Keep a compact spec template; omit the exhaustive story list and tracker setup. |
| Matt Pocock: `tdd`, `code-review`, `diagnosing-bugs`, architecture guidance | Omit standalone tutorials on familiar engineering methods. Retain selected rules and verification within the workflows. |
| OpenSpec: `explore`, `new`, `continue`, `ff`, `propose`, `apply`, `update`, `verify`, `onboard` | Replace separate commands, CLI instructions, and onboarding with one planning skill and three templates. |
| OpenSpec: `sync`, `archive`, `bulk-archive` | Omit living-spec synchronization and delta merging; this collection uses change-specific plans. |

**Preserved from OpenSpec:** proposal/spec/tasks, human approval before code, WHEN/THEN scenarios, and a check for every task, with relevant tests and docs alongside the code.

These are scope choices informed by text review, not proof that the omitted skills are obsolete.
Use upstream OpenSpec when you need living specs, delta validation, or its shared CLI workflow.

## Install

Ask your agent:

> Install the skills I select from https://github.com/zhiland/skills-lite into this project. Compare existing same-named skills before replacing them.

Or copy the selected directories from either collection's `skills/` folder:

- **Codex:** `<project>/.agents/skills/` or `~/.agents/skills/`.
- **Claude Code:** `<project>/.claude/skills/` or `~/.claude/skills/`.

Copy the whole skill directory, including templates and license. No Python, installer, or CLI dependency.
Codex can select skills automatically or via `$skill-name`. Claude Code uses explicit `/skill-name` invocation.
When replacing an older copy, remove its obsolete `agents/openai.yaml` to enable automatic selection in Codex.

## Use

Choose `lite-feature-plan`, or start with `lite-grill` → `lite-feature-spec`.
Add tickets and implementation when needed; do not create duplicate plans.
[Optional project rules](matt-pocock-skills/OPTIONAL-RULES.md) are separate from installation.

[History and diffs](docs/HISTORY.md) · [Review](docs/REVIEW.md) · [Evaluation guide](docs/EVALUATION.md)

MIT. See [LICENSE](LICENSE) and [upstream notices](THIRD_PARTY_NOTICES.md).
