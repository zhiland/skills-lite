# Tasks: <feature name>

<!-- Groups are ordered by dependency. Tests and docs go in the same group as the code.
     Every task makes sense without the conversation: area, requirement, check.
     Tick a box only after its check has passed. -->

## 1. <Group name>

- [ ] 1.1 <What to do>
  - Where: <files or module>
  - Blocked by: <task IDs or none>
  - Requirement: R1
  - Check: <test, command or observable behavior>
- [ ] 1.2 <What to do>
  - Where:
  - Blocked by: <task IDs or none>
  - Requirement:
  - Check:

## 2. <Group name>

<!-- If a group depends on another, say so: "After: 1". Independent groups can go to different agents. -->

- [ ] 2.1 <What to do>
  - Where:
  - Blocked by: <task IDs or none>
  - Requirement:
  - Check:

## 3. Cross-cutting check

<!-- After all implementation groups. Record evidence and unavailable checks. -->

- [ ] 3.1 <A check that spans several groups>
  - Where: <integration boundary>
  - Requirement: <covered IDs>
  - Blocked by: <all implementation task IDs>
  - Check:
