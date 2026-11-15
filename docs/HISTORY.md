# Versions

| Tag | Version |
| --- | --- |
| [v0.1](https://github.com/zhiland/skills-lite/tree/v0.1) | Original local drafts supplied for review |
| [v0.2](https://github.com/zhiland/skills-lite/tree/v0.2) | First rewrite and repository packaging |
| [v0.3](https://github.com/zhiland/skills-lite/tree/v0.3) | Conservative revision preserving the original wording |
| [v0.4](https://github.com/zhiland/skills-lite/tree/v0.4) | Skills Lite: automatic Codex discovery, no Python tooling or CI, shorter README, and documented rationale |
| [v0.5](https://github.com/zhiland/skills-lite/tree/v0.5) | Matt Pocock skills only; remove the two independent OpenSpec-related skills pending compatible upstream adaptations |

The original drafts were already local adaptations of the upstream projects. Their text is preserved at the later package paths for easy comparison.
Use v0.5 or the latest main branch for installation; v0.1 is a historical snapshot, not an installable package.

## Compare

- [v0.4 → v0.5](https://github.com/zhiland/skills-lite/compare/v0.4...v0.5)

- [v0.1 → v0.2](https://github.com/zhiland/skills-lite/compare/v0.1...v0.2)
- [v0.2 → v0.3](https://github.com/zhiland/skills-lite/compare/v0.2...v0.3)
- [v0.3 → v0.4](https://github.com/zhiland/skills-lite/compare/v0.3...v0.4)
- [v0.1 → v0.4](https://github.com/zhiland/skills-lite/compare/v0.1...v0.4)

The earlier descriptive tags remain as aliases: `original-drafts` = `v0.1`, `first-rewrite` = `v0.2`, and `conservative-revision` = `v0.3`.

## Skill names on main

Matt Pocock adaptations now use `lite-` followed by the upstream skill name. The v0.4 tag retains its original names.

| Earlier package name | Current name | Upstream name |
| --- | --- | --- |
| `lite-grill` | `lite-grilling` | `grilling` |
| `lite-feature-spec` | `lite-to-spec` | `to-spec` |
| `lite-run-tickets` | `lite-implement-spec` | `implement-spec` |
| `lite-ask-person`, then `lite-questionnaire` | `lite-to-questionnaire` | `to-questionnaire` |
| `lite-to-tickets` | unchanged | `to-tickets` |
| `lite-retro` | unchanged | `retro` |

Replace the old installation folder when adopting a renamed skill. Preserve any local customizations before replacement.
v0.5 removes `lite-feature-plan` and `lite-adaptation-review`. They were independent local workflows, not shortened upstream OpenSpec skills. Remove installed copies when upgrading, preserving any local customizations. Earlier tags retain the historical files. Compatible OpenSpec adaptations are planned separately.
