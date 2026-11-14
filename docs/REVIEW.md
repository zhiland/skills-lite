# Review and conservative revision

Source review: 2026-11-13. Current revision: 2026-11-14.

## Editorial decision

The first packaged version rewrote too much of the supplied drafts. This revision starts again from those drafts.
It preserves headings, steps, templates, and wording wherever a concrete correction does not require an edit.
The three OpenSpec-inspired templates are unchanged from the local originals.
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
| `adaptation-review` | Keep the original headings and verdicts. Shorten repeated prose. Limit private-history access to the selected project and qualify claims about tokens and model ability. |
| OpenSpec rules | Keep all 13 numbered rules. Correct template links, preserve prior approval, allow drafting around unresolved decisions, and replace automatic deletion with project retention policy. |
| Optional coding rules | Keep the six bullets. Make TDD conditional, permit hypotheses without a deterministic reproduction, and retain useful prototype safeguards. |

If planning uses separate tickets, they own ticket status. `tasks.md` becomes their index and the cross-cutting checklist.
This prevents competing records of the same work.

## Size comparison

Across the seven original skill bodies, the OpenSpec rules, and optional coding rules, text decreased from 2,130 to 1,915 whitespace-delimited words (about 10%).
This excludes frontmatter and unchanged templates. It is not a token measurement.
The runner grew by 21 words and OpenSpec rules by seven words to retain concrete integration and status safeguards.

## Models and scope

This collection is intended for capable coding models, including GPT-6.1 Sol, GPT-6.1 Terra, and GPT-6 Luna.
It does not claim that the source skills are obsolete or that these revisions improve a benchmark score.
Generic engineering knowledge can be shortened, but output contracts and acceptance conditions remain explicit.

Sources informing this approach:
- [Rethinking skills and prompts for GPT-6 Astra](https://learn.chatgpt.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). Its observations concern Astra and do not establish that Sol or Luna need identical instructions.
- [GPT-6 guidance](https://developers.openai.com/api/docs/guides/latest-model). Evaluate prompting changes on the model and workload used.
- [Model selection](https://learn.chatgpt.com/docs/model-selection). Prefer concrete inputs and verification, and compare representative tasks.

## Verification boundary

The local drafts remain untouched. All eight skill packages are checked for metadata, client invocation policy, and local links.
Installation tests check preservation of existing content, refusal of source symlinks, and source boundaries.
The installed Codex quick validator rejects Claude's supported invocation fields, so this repository validates the combined metadata explicitly with a YAML parser.

Manual contract review covers unresolved decisions, invalid ticket dependencies, concurrent results, unavailable checks, dirty worker checkouts,
and adoption reviews without usage evidence. This is text inspection, not independent behavioral testing.
Live discovery, actual prompt tokens, and implementation quality across models remain untested. See [EVALUATION.md](EVALUATION.md).
