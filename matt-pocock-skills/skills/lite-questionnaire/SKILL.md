---
name: lite-questionnaire
description: Write a questionnaire for a person who holds knowledge a decision needs.
disable-model-invocation: true
argument-hint: "Who it is for and about what"
---

Write a questionnaire for one person who knows what I do not.

Ask only for missing information:

1. Who it goes to: their role, what they know, how they relate to me.
2. What I need back: which decisions or facts.

Then write the questionnaire to `ask-<topic>.md` and report the path.

Structure:

    # <title>
    Purpose: why this exists and which decision depends on it.
    From, to, and how the answers will be used.
    ## Context           (one paragraph for someone outside the topic)
    ## How to answer     (known deadline; "I don't know" is a valid answer)
    ## <theme>           (questions from most to least important)
    ## What did we not ask?

One question, one idea. Leave space for the answer under each. Do not send the questionnaire.
