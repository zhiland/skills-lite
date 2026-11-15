# Review and conservative revision

**Current scope:** six Matt Pocock adaptations. This review describes their conservative revision and optional project rules.

Source review: 2026-11-13. Historical conservative revision: 2026-11-14.

## Editorial decision

The first packaged version rewrote too much of the supplied drafts. This revision starts again from those drafts.
It preserves headings, steps, templates, and wording wherever a concrete correction does not require an edit.
Names keep the `lite-` prefix for installation, Claude retains manual invocation, and Codex uses automatic selection by default.

## Targeted changes

| Input | Changes retained |
| --- | --- |
| `grill` | Small independent rounds, evidence-based recommendations, completion when next-step decisions are settled. No compulsory delegation or yes-biased questions. |
| `feature-spec` | Record agreed test boundaries rather than reopen approval. Mark unresolved behavior as draft. Allow file paths as navigation. |
| `to-tickets` | Shorten slicing advice. Draft before approval. Reuse approval. Check coverage and dependency validity. Add requirement references and a check to the existing template. |
| `run-tickets` | Preserve the eight steps. Check integrated dependencies, use sequential fallback, verify the integration tip, preserve dirty worktrees, and limit unnecessary testing. |
| `retro` | Keep the original categories. Shorten one example list. Require evidence before proposing removal of instructions. |
| `ask-person` | Keep the original questionnaire structure. Ask only missing intake questions, avoid invented deadlines, and keep delivery separate. |
| Optional coding rules | Keep the six bullets. Make TDD conditional, permit hypotheses without a deterministic reproduction, and retain useful prototype safeguards. |

## Models and scope

This collection is intended for capable coding models, including GPT-6.1 Sol, GPT-6.1 Terra, and GPT-6 Luna.
It does not claim that the source skills are obsolete or that these revisions improve a benchmark score.
Generic engineering knowledge can be shortened, but output contracts and acceptance conditions remain explicit.

Sources informing this approach:
- [Rethinking skills and prompts for GPT-6 Astra](https://learn.chatgpt.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). Its observations concern Astra and do not establish that Sol or Luna need identical instructions.
- [GPT-6 guidance](https://developers.openai.com/api/docs/guides/latest-model). Evaluate prompting changes on the model and workload used.
- [Model selection](https://learn.chatgpt.com/docs/model-selection). Prefer concrete inputs and verification, and compare representative tasks.

## Verification boundary

The local drafts remain untouched. Earlier revisions passed metadata/link checks and five installation tests.
The installer, Python validator, development dependency, tests, and CI workflow were subsequently removed to keep this a Markdown-only collection.
Those earlier test results describe the historical tooling, not a current automated validation service.

Manual contract review covers unresolved decisions, invalid ticket dependencies, concurrent results, unavailable checks, dirty worker checkouts. This is text inspection, not independent behavioral testing.
Live discovery, actual prompt tokens, and implementation quality across models remain untested. See [EVALUATION.md](EVALUATION.md).
