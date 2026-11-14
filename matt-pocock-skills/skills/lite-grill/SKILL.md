---
name: lite-grill
description: Interview before a feature or decision - rounds of questions until blocking decisions are settled.
disable-model-invocation: true
argument-hint: "What are we discussing?"
---

Interview me until we share the same understanding of the task. Do not implement anything or write a spec unless I ask.

- Explore the code first. Find facts yourself (what is in the code, configs, tracker). Ask me only about decisions.
- Ask in rounds. Keep each round small and its questions independent. Leave dependent questions for the next round.
- Number the questions. Give a recommended answer where the evidence supports one.
- If a term I use conflicts with the code, or I use it in two senses, say so at once and propose one term.
- If what I say contradicts the code, show the contradiction and ask which is right.
- Test boundaries with concrete edge-case scenarios.

The interview is done when decisions needed for the next step are settled. Finish with a list of the decisions made and deferred questions.
