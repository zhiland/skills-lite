# Frontier Skills Lite

Eight compact skills for Codex and Claude Code, adapted from OpenSpec and Matt Pocock's skills.
They keep useful workflow rules and templates while cutting repeated guidance. Independent project; no model-performance claims.

## Sources

Latest releases checked on **14 November 2026**:

- [Matt Pocock Skills 1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2). Our source snapshot is `5863806`, five commits after that tag, still versioned 1.3.2.
- [OpenSpec 2.0.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.0.0). Our review snapshot `d12c281` matches this release.

The skills were shortened from local adaptations of these projects. See [SOURCES.md](SOURCES.md) for exact revisions and attribution.
The OpenSpec-inspired templates are plain Markdown, not OpenSpec CLI schemas.

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

> Install the skills I select from https://github.com/zhiland/frontier-skills-lite into this project. Compare existing same-named skills before replacing them.

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
