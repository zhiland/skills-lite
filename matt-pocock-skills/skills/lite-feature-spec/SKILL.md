---
name: feature-spec
description: Write a feature spec from what this conversation has already settled, with no new interview.
disable-model-invocation: true
argument-hint: "Where to save it (path or ticket)"
---

Write a feature spec from what is already decided in this conversation. Do not run a new interview. The spec is single-use: nobody maintains it after merge.

1. Explore the code if you have not already.
2. Propose the test seams and agree them with me: existing ones where possible, as high as possible, as few as possible.
3. Write the spec with the template below to the place I named. If I named none, ask once.

Template:

    ## Problem                   (from the user's point of view)
    ## Solution                  (from the user's point of view)
    ## Scenarios                 (only those discussed or directly implied by the decisions)
    ## Implementation decisions  (modules, interfaces, schemas, contracts)
    ## Testing decisions         (seams, similar tests already in the code)
    ## Out of scope

No file paths or code snippets: they go stale. Exception: a snippet from a prototype that states a decision more precisely than prose (a schema, a type, a state machine).
