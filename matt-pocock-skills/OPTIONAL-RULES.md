## Rules for working with code

Optional: adopt only rules your project needs.

- When TDD is required, write tests one at a time: test → minimal code → next test. Take the expected value from an independent source; do not compute it the way the code does.
- Hard bug: seek a reproducible failure. If none is available, state hypotheses and missing evidence; do not claim a verified fix.
- Tag debug logs with a unique prefix and remove them before you finish.
- A prototype is throwaway code for one question: keep only tests and safeguards needed for that question, and a name that says "prototype". Only the decision goes to the main branch.
- When a term conflicts with the code or is used in two senses, name it at once and propose one term.
- Propose an ADR only if the decision is hard to reverse, would surprise a reader without context, and was chosen from real alternatives.
