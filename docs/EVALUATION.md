# Runtime evaluation protocol

Use a disposable repository and synthetic data. Do not use private session history for a public benchmark.

Compare three conditions on the same tasks: plain request, upstream workflow, and this adaptation.
Use the same model version, harness, tools, permissions, initial commit, and context budget. Repeat runs to expose variance.
Record failures as well as successful outcomes.

Suggested tasks:

1. Draft a feature with one unresolved error behavior. Check draft status and question relevance.
2. Slice a feature with shared interfaces. Check coverage, dependency validity, and independently verifiable outcomes.
3. Implement two tickets whose changes interact. Check the combined integration commit, not only worker reports.
4. Repeat with an unavailable check and a dirty worker checkout. Check honest status and preservation of work.
5. Review a tool without usage history. Check that uncertainty is preserved and unrelated data is not read.
6. Draft a questionnaire with all intake facts supplied. Check that it avoids repeat questions and invented deadlines.

Record model and client versions, skill commit, input artifacts, final diff, passed checks, human interventions,
loaded prompt tokens when measurable, elapsed time, and cost when available.
Report whether the savings came from fewer installed skills, shorter invoked bodies, or different execution behavior.
Publish redacted artifacts and the evaluation method. Do not infer universal superiority from one run.

Before rollout, check that each installed skill appears in the selector, runs when explicitly invoked,
and stays inactive on an unrelated request. Validate manual-only behavior in each supported client version.
