---
name: grill
description: Interview before a feature or decision - rounds of questions until no decision is left open.
disable-model-invocation: true
argument-hint: "What are we discussing?"
---

Interview me until we share the same understanding of the task. Do not implement anything or write a spec until I confirm.

- Explore the code first. Find facts yourself (what is in the code, configs, tracker), with a subagent if the search is large. Ask me only about decisions.
- Ask in rounds. A round holds every question that can be answered without knowing the answer to another open question. Leave dependent questions for the next round.
- Number the questions. Give a recommended answer for each. Word each question so that "yes" accepts the recommendation.
- If a term I use conflicts with the code, or I use it in two senses, say so at once and propose one term.
- If what I say contradicts the code, show the contradiction and ask which is right.
- Test boundaries with concrete edge-case scenarios.

The interview is done when no decision is left open and I have confirmed it. Finish with a list of the decisions made.
