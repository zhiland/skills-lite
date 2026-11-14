# Independent review of the two local drafts

## Verdict

The compact workflow idea is useful. The original drafts needed correction before public distribution.
The claim that frontier models make all other workflow skills obsolete was unsupported. Capability does not establish reliable execution under context pressure.
The package now describes a selective workflow preference and preserves its evidence limits.

## Findings and corrections

| Area | Problem in the supplied drafts | Correction |
| --- | --- | --- |
| Model claims | Declared broad categories obsolete without runs | Removed model rankings and universal obsolescence claims |
| Context | Claude-specific flag treated as universal zero-context support | Added Codex policy files and client/version caveat |
| Naming | Common names could collide with installed upstream skills | Used consistent `lite-` names |
| OpenSpec rules | Always-on rules and templates required manual setup | Packaged the workflow and templates as one optional skill |
| Retention | Required deleting change artifacts before merge | Retain historical artifacts by default, follow project policy |
| Approvals | Repeated approval could be required for settled decisions | Reuse explicit approval within unchanged scope |
| Interview | Every possible decision had to close, with yes-biased questions | Close blockers for the next step, record deferrals, show alternatives |
| Spec | No interview, yet compulsory new agreement on test seams | Synthesize known decisions, ask only blocking questions, keep draft status |
| Navigation | Blanket prohibition of file paths | Allow current paths as navigation, preserve stable requirement references |
| Tickets | Lacked explicit graph validation, coverage and verification evidence | Added IDs, cycle checks, requirement coverage, checks and evidence |
| Runner | Worker tests could predate other integration merges | Serialize integration and check the resulting integration tip |
| Runner | Assumed worktree support and source access | Added sequential fallback and accessible planning artifacts |
| Runner | Unconditional worktree removal | Remove only integrated clean worktrees created by the run |
| Adoption review | Searched global/private history and inferred no need from no data | Limit evidence scope and support provisional trials |
| Retro | Could promote speculative no-op claims into permanent rules | Separate evidence and hypotheses, prefer narrow fixes |
| Questionnaire | Reasked known facts and could invent delivery details | Ask only missing essentials, omit unknown optional details |
| Debugging rule | Forbade hypotheses until a fast deterministic reproduction | Allow evidence-guided hypotheses for intermittent or inaccessible failures |
| Prototype rule | Forbade all error handling and tests | Preserve necessary safeguards, test only where useful to the experiment |
| Publication | Missing retained licenses, pinned provenance, client validation | Added MIT notices, source mapping, validation and publication guidance |

## Verification boundary

All seven original skill bodies, six optional rules, three templates, and the OpenSpec rules were read.
The new eighth skill packages those OpenSpec rules. Selected upstream source files and both MIT licenses were checked.
Original input files were hash-checked after packaging. No original was edited.

Static checks cover all eight skill folders, both invocation policies, and relative Markdown links.
The installed Codex quick validator rejects Claude's supported `disable-model-invocation` field.
The repository validator therefore checks the combined metadata explicitly with a YAML parser, including both client policies.
Installation tests use temporary directories and check preservation of existing content, refusal of symlinks, and path boundaries.
A manual scenario walkthrough checked the contracts below. It is not a model execution test:

| Scenario | Required outcome in the revised contract |
| --- | --- |
| Spec has an unresolved behavior choice | Draft, targeted question, no invented approved requirement |
| Tickets form a cycle | Graph error before dispatch |
| Two workers start from the same base | Serialized integration and checks after each merge |
| Harness cannot isolate workers | Sequential implementation |
| Worker has untracked files at cleanup | Preserve worktree and report it |
| Candidate has no usage history | Provisional verdict or trial, no claim of demonstrated redundancy |
| Questionnaire recipient and goal are supplied | No repeated intake questions |
| Check requires an unavailable environment | Work remains explicitly unverified |

Not tested: discovery in a live Claude Code or Codex session, actual prompt token usage, implementation reliability,
quality versus upstream, and execution across different frontier models. No performance or production-readiness claim follows from static validation.
