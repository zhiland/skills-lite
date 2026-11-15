# Skills Lite

Compact versions of [Matt Pocock's skills v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2) for the frontier coding models available in **November 2026**.

OpenSpec adaptations are coming next. They will shorten the original workflows while preserving the CLI and specification format. **v0.5 contains only Matt Pocock adaptations.**

## Why this exists

Instructions accumulate as we work around older models' limitations. Newer models may already handle those tasks, while the old guidance remains: repeated advice, rigid recipes, and conflicting rules that consume context or get in the way.

[Addy Osmani recommends auditing agent files](https://addyosmani.com/blog/audit-your-agent-files/) as models improve.
[Anthropic describes simplifying context for Claude 5 models](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) to avoid unnecessary constraints.

[OpenAI recommends rethinking skills and prompts for GPT-6 Astra](https://learn.chatgpt.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), including shorter instructions and more precise skill selection.

This project applies that idea to popular coding skills:

- **Approach:** reviewed and edited with Claude Fable 5.2 and GPT-6 Astra to shorten general guidance, preserve useful workflow choices, and keep the original wording where it works.
- **Intended audience:** users of current frontier models, rather than models that need extensive procedural guidance.
- **Evidence:** reviewed adaptations, not benchmark-proven replacements for the upstream collections.
- **Sources:** exact source details are in [SOURCES.md](SOURCES.md).

## Skills

| Folder | Original name | Skill | Purpose |
| --- | --- | --- | --- |
| `matt-pocock-skills` | `grilling` | `lite-grilling` | Resolve blocking decisions |
| `matt-pocock-skills` | `to-spec` | `lite-to-spec` | Turn settled decisions into a spec |
| `matt-pocock-skills` | `to-tickets` | `lite-to-tickets` | Split a spec into verifiable tickets |
| `matt-pocock-skills` | `implement-spec` | `lite-implement-spec` | Implement, integrate, and verify tickets |
| `matt-pocock-skills` | `retro` | `lite-retro` | Review the agent's working environment |
| `matt-pocock-skills` | `to-questionnaire` | `lite-to-questionnaire` | Draft questions for someone whose knowledge you need |

Names follow the upstream skill name with a `lite-` prefix. Additional source details are in [SOURCES.md](SOURCES.md).

## What we kept and left out

| Source material | Decision and reason |
| --- | --- |
| Matt Pocock: `grilling`, `to-tickets`, `implement-spec`, `retro`, `to-questionnaire` | Keep their workflow core: decisions, handoffs, verification, and output formats. |
| Matt Pocock: `to-spec` | Keep a compact spec template; omit the exhaustive story list and tracker setup. |
| Matt Pocock: `tdd`, `code-review`, `diagnosing-bugs`, architecture guidance | Omit standalone tutorials on familiar engineering methods. Retain selected rules and verification within the workflows. |

These are scope choices informed by text review, not proof that the omitted skills are obsolete.
For OpenSpec, use the [upstream project](https://github.com/Fission-AI/OpenSpec) until the compatible adaptations are ready.

## Install

Ask your agent:

> Install the skills I select from https://github.com/zhiland/skills-lite into this project. Compare existing same-named skills before replacing them.

Or copy the selected directories from `matt-pocock-skills/skills/`:

- **Codex:** `<project>/.agents/skills/` or `~/.agents/skills/`.
- **Claude Code:** `<project>/.claude/skills/` or `~/.claude/skills/`.

Copy the whole skill directory, including its license and any supporting files. No Python, installer, or CLI dependency.
Codex can select skills automatically or via `$skill-name`. Claude Code uses explicit `/skill-name` invocation.
When updating, replace renamed skill folders rather than keeping both names. See the [rename map](docs/HISTORY.md#skill-names-on-main). Remove obsolete `agents/openai.yaml` files to enable automatic selection in Codex.

**Upgrading from v0.4 or earlier:** remove installed `lite-feature-plan` and `lite-adaptation-review` skill folders, preserving any local customizations. They were removed because they did not provide shortened upstream OpenSpec workflows. Updating this repository does not remove installed copies.

## Use

Start with `lite-grilling` → `lite-to-spec`.
Add tickets and implementation when needed; do not create duplicate plans.
[Optional project rules](matt-pocock-skills/OPTIONAL-RULES.md) are separate from installation.

[History and diffs](docs/HISTORY.md) · [Review](docs/REVIEW.md) · [Evaluation guide](docs/EVALUATION.md)

MIT. See [LICENSE](LICENSE) and [upstream notices](THIRD_PARTY_NOTICES.md).
