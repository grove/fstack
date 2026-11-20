---
name: fstack-refactor-safely
description: "Improve internal structure while preserving observable contracts. Use when simplifying responsibility, removing duplication, or changing implementation shape without changing intended behavior."
---

# Refactor safely

## Starting point

Start with a concrete structural problem and the behavior that must remain stable. Establish the comparison baseline, permitted files, public interfaces, and existing verification. Include error behavior, ordering, persistence, resource lifetime, and timing guarantees when callers depend on them; a function signature alone is not the contract.

## Method

1. Name the maintenance difficulty and its consequence. Show the repeated knowledge, ownership ambiguity, or change dispersion that motivates the work. Avoid a refactor whose only argument is preference for another pattern or a smaller file.
2. Inventory observable obligations and representative callers. Separate intended behavior from accidental behavior only when an existing decision supports the distinction. If changing an observed behavior is desirable, propose that as a behavior change rather than silently calling it cleanup.
3. Establish a baseline using meaningful checks at the relevant boundaries. Where coverage is missing, add characterization or explicit contract examples with independent expectations. Record known failures so they cannot disappear into a misleading before-and-after comparison.
4. Choose a sequence of small, explainable transformations. Keep the public surface stable where possible. For broad changes, introduce a temporary compatibility path, migrate bounded groups, and remove that path only after all known consumers and obligations are accounted for.
5. After each meaningful transformation, exercise the behavior most likely to have changed. Inspect changed tests: a structural refactor should not need different expected business results. Test maintenance may be justified when removing coupling to internals, but the preserved observation must remain clear.
6. Compare the final behavior and structure with the baseline. Check for leftover migration scaffolding, duplicated policies, lost error handling, and unconverted consumers. Stop when the named maintenance difficulty has improved and the preservation evidence covers the claimed scope.

## What to return

Return the original structural problem, transformation sequence, preserved contracts, changed internal responsibilities, and before-and-after evidence. Identify any compatibility bridge and its removal condition. State unresolved coverage or observed behavior changes explicitly; if a change breaks an intended contract, report a failed refactor rather than redefining success.

## Boundaries

Stay inside authorized edits and execution, preserving unrelated work. Do not combine opportunistic features with preservation work. If the environment cannot establish equivalence for a consequential boundary, retain a smaller claim or stop for evidence. A green suite alone does not prove equivalence when its assertions were weakened or relevant cases are absent.

## Worked example

A parser combines character scanning with error reporting, making each grammar change difficult to locate. Extract a scanner while preserving token positions, the order of reported errors, and the existing accepted grammar. Compare valid input and malformed input at several positions before and after extraction. Accepting previously invalid syntax, even if convenient for the new scanner, would need a separate behavioral decision.
