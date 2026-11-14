# Optional project rules

Adopt only rules that match the project. Do not paste this entire file into global instructions by default.

- When TDD is requested or required, use one failing behavior test at a time, then minimal code and refactoring. Use independent expected results.
- For a hard bug, seek a representative reproduction. Form explicit hypotheses to guide evidence collection when reproduction is unavailable or intermittent.
  Record uncertainty and distinguish a diagnostic observation from a verified fix.
- Remove temporary instrumentation introduced by the task, unless the project needs it retained. Preserve existing observability.
- A prototype answers one bounded question. Keep safeguards needed for real data and external effects. Add tests only where they support that question.
  Move prototype code into production only through an explicit implementation decision and normal checks.
- Resolve ambiguous domain terms when they affect behavior or interfaces.
- Record consequential design choices with rationale and alternatives. Use an ADR when the project needs a durable decision record.
