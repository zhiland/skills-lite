# Sources and provenance

Source review: 2026-11-13. Conservative revision: 2026-11-14. Local drafts were the input to this review. Upstream files were consulted to check attribution and omitted behavior.
This was not a new exhaustive audit of every upstream skill.

| Source | Pinned revision | Material used |
| --- | --- | --- |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec/tree/d12c2817776779e06891d68230773b3bb673b106) | `d12c2817776779e06891d68230773b3bb673b106` | `schemas/spec-driven/schema.yaml`, its templates, and the planning guidance in `src/core/templates/workflows/explore.ts` |
| [mattpocock/skills](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa) | `5863806dd4e15c63174bee4e7515a4256792ecfa` | `skills/productivity/grilling`, `to-questionnaire`, and `skills/engineering/to-spec`, `to-tickets`, `implement-spec`, `retro` |

The Matt Pocock revision matches the supplied handoff. The OpenSpec handoff did not pin one source commit.
The OpenSpec revision above identifies this review's snapshot, not a reconstructed revision of the earlier review.

The current skill text is edited directly from the supplied local drafts. Original templates are preserved unchanged.
The earlier broad rewrite remains in Git history. It is not the textual base of the current revision.

## Release versions

Verified against GitHub releases and source manifests on 2026-11-14:

| Project | Latest release | Relationship to our pinned source |
| --- | --- | --- |
| Matt Pocock Skills | [v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2), published 2026-10-29 | `5863806` is five commits after the tag; `.claude-plugin/plugin.json` still declares 1.3.2. Those changes include `implement-spec`. |
| OpenSpec | [v2.0.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.0.0), published 2026-11-11 | `d12c281` is the release commit; `package.json` declares 2.0.0. |

These are source versions, not a version or compatibility guarantee for this independent collection.
The original OpenSpec handoff also consulted CLI 1.16.1; its unpinned earlier materials are not retroactively relabeled as 2.0.0.

## Adaptation map

| Local deliverable | Origin and changes |
| --- | --- |
| `lite-feature-plan` and templates | OpenSpec-inspired local rules/templates, repackaged as an optional skill. No CLI or delta-format compatibility. |
| `lite-adaptation-review` | Original companion from the local OpenSpec review. Scope and uncertainty handling revised here. |
| `lite-grilling` | `grilling`, with domain-term clarification from the local draft. Bounded completion and neutral questions. |
| `lite-to-spec` | `to-spec`. No tracker setup, exhaustive story list, or compulsory new test-seam approval. |
| `lite-to-tickets` | `to-tickets`. Retained the original structure with accessible spec references, checks, coverage, and graph checks. |
| `lite-implement-spec` | `implement-spec` and spec-review ideas from the local `code-review` adaptation. Added integration acceptance and safe cleanup. |
| `lite-retro` | `retro`. Evidence scope and confidence made explicit. |
| `lite-to-questionnaire` | `to-questionnaire`. Reuses supplied context and avoids invented deadlines. |
| Optional rules | Local distillation of `tdd`, `diagnosing-bugs`, `prototype`, and `domain-modeling`. Unsafe universal constraints removed. |

Earlier handoffs contained model-specific obsolescence judgments and size estimates. They were not benchmarks and are not adopted as findings here.
Private handoffs, transcript paths, and project history are intentionally excluded from this public package.

Client documentation consulted: [Claude Code skills](https://code.claude.com/docs/en/skills) and [Codex skills](https://developers.openai.com/codex/skills).
Codex now uses default automatic invocation; the earlier manual-only policy files were removed. Client behavior still needs a live smoke test.

## Motivation and review method

- [Addy Osmani: Audit your Agent files](https://addyosmani.com/blog/audit-your-agent-files/) recommends revisiting accumulated instructions and testing whether removals help.
- [Anthropic: The new rules of context engineering for Claude 5 generation models](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) describes reducing constraints and retaining task-specific context.
- [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://learn.chatgpt.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) recommends auditing skills as model behavior changes. Its Astra observations are not automatically evidence about Sol, Terra, or Luna.

The initial local review used Claude Fable 5.2; subsequent review and editing used GPT-6 Astra in Codex, as confirmed by the author.
This was a text review, not a cross-model benchmark.
November 2026 describes the target model generation, not a guarantee that every instruction is redundant for every current model.
