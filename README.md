# Skills Lite

Compact versions of OpenSpec-inspired workflows and Matt Pocock's skills for the frontier coding models available in **November 2026**.

## Why this exists

Instructions accumulate as we work around older models' limitations. Newer models may already handle those tasks, while the old guidance remains: repeated advice, rigid recipes, and conflicting rules that consume context or get in the way.

[Addy Osmani recommends auditing agent files](https://addyosmani.com/blog/audit-your-agent-files/) as models improve.
[Anthropic describes simplifying context for Claude 5 models](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) to avoid unnecessary constraints.

This project applies that idea to two skill collections: shorten general guidance, preserve useful workflow choices, and keep the original wording where it works.
The initial review used Claude Fable 5.2; subsequent review and editing took place in Codex.
The intended audience uses current frontier models, not models that need extensive procedural guidance.
These are reviewed adaptations, not benchmark-proven replacements for the upstream collections.

## Based on

- [Matt Pocock Skills v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2)
- [OpenSpec v2.0.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.0.0)

Latest upstream releases checked on 14 November 2026. Exact source details are in [SOURCES.md](SOURCES.md).
OpenSpec-inspired templates are plain Markdown, not CLI schemas.

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
