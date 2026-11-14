---
name: retro
description: Session review - what to change in the agent's environment so the next session goes better.
disable-model-invocation: true
argument-hint: "Which session (default: this one)"
---

Review the session and propose improvements to the agent's environment, not to the code. Change nothing; only propose. List the proposals most severe first, each with the place in the session where the problem showed.

What to look for:

- **Navigation.** A file or fact took long to find → a pointer in the rules next to the module.
- **Automated checks.** A check would have caught the mistake → first see which checks the repo already has and whether they are wired in. A mechanical mistake (a pattern, a banned call, a file location) → a lint rule or a CI step, not a new instruction.
- **Coding standards.** Something only judgement can check → a rule for review.
- **Instructions.** A line that does not change the agent's behaviour → delete it. A rule in the shared instructions that matters only at review → move it there.
- **Tools.** Expensive calls that could be simpler.
- **Access to data.** Logs, an environment, or read access were missing → name exactly what.
