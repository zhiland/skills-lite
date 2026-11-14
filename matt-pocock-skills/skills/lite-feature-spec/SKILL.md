---
name: lite-feature-spec
description: Write a feature spec from what this conversation has already settled, with no new interview.
disable-model-invocation: true
argument-hint: "Where to save it (path or ticket)"
---

Write a feature spec from what is already decided in this conversation. Do not run a new interview. The spec is single-use: no ongoing maintenance after merge.

1. Explore the code if you have not already.
2. Record the agreed test seams; prefer existing ones. Mark unresolved behavior as draft and ask only blocking questions.
3. Write the spec with the template below to the place I named. If I named none, ask once.

Template:

    ## Problem                   (from the user's point of view)
    ## Solution                  (from the user's point of view)
    ## Scenarios                 (requirement IDs and WHEN/THEN cases from the decisions)
    ## Implementation decisions  (modules, interfaces, schemas, contracts)
    ## Testing decisions         (seams, similar tests already in the code)
    ## Out of scope

Use file paths as navigation aids, not requirements. Include code only when it states a decision more precisely than prose.
