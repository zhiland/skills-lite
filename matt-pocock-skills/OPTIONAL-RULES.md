## Rules for working with code

- Write tests one at a time: test → minimal code → next test. A test checks behaviour through the public interface. Take the expected value from an independent source; do not compute it the way the code does.
- Hard bug: do not form hypotheses until there is one command that you have already run, that fails on the exact reported symptom, gives a stable result, and runs in seconds. If there is no such command, say what you tried and ask for access or an artifact.
- Tag debug logs with a unique prefix and remove them before you finish.
- A prototype is throwaway code for one question: no tests, no error handling, no abstractions, and a name that says "prototype". Only the decision goes to the main branch.
- When a term conflicts with the code or is used in two senses, name it at once and propose one term.
- Propose an ADR only if the decision is hard to reverse, would surprise a reader without context, and was chosen from real alternatives.
