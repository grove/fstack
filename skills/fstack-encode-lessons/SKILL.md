---
name: fstack-encode-lessons
description: "Turn recurring observed mistakes into proportionate structural safeguards. Use after repeated defects or review corrections when a durable constraint could prevent the same failure class."
---

# Encode lessons

## Starting point

Start with concrete examples of a recurring failure, their causes and consequences, and the current system boundaries. Separate repeated evidence from a memorable one-off incident. The aim is to make correct behavior easier or invalid behavior harder, without accumulating broad rules that create noise or freeze legitimate design choices.

## Method

1. Describe the failure class using at least the actual examples available. Identify what repeats: missing context, ambiguous ownership, an invalid state, an unenforced contract, or a misleading tool boundary. Do not group unrelated mistakes merely because they share a symptom or appeared in the same review.
2. Trace how the current structure permits that failure. Identify the earliest boundary with enough information to prevent or detect it reliably. Prefer removing duplicate knowledge or invalid states over adding a reminder to every place where the mistake could occur.
3. Compare enforcement options appropriate to the project: a narrower interface, explicit ownership, a type or representation, a validation boundary, a build check, or a behavioral regression. Use documentation for judgment that cannot be reliably automated; do not pretend a keyword rule captures semantics it cannot observe.
4. Design both a failing example and a legitimate counterexample for the safeguard. The known mistake should be rejected or exposed, while valid behavior should remain possible. State the intended scope, false-positive risks, and any bypass that would undermine the protection.
5. Implement and exercise the safeguard only when authorized. Show it detecting a real historical failure or faithful reproduction, then show a valid case still works. If only a proposal is possible, describe the proof required rather than claiming the rule already prevents recurrence.
6. Record the changed invariant, its owner, where it is enforced, and how to revise or retire it if assumptions change. Remove redundant reminders when a reliable structural protection replaces them. Stop when the selected failure class is addressed at a useful boundary; do not use one lesson to justify a broad rewrite.

## What to return

Return the observed failure class, supporting examples, proposed or implemented safeguard, enforcement location, rejection and legitimate-use evidence, and remaining limits. Distinguish prevention from detection and a checked property from a general quality claim. Include a concrete follow-up measure for whether recurrence and review noise actually decline.

## Boundaries

Respect the user’s change authority and the project’s exceptions. Do not silently change global policy, weaken legitimate interfaces, or create tests that merely repeat the implementation. A single example may justify a regression check but does not establish a recurring class. New prose instructions alone are insufficient when the same preventable error remains structurally easy.

## Worked example

Twice, a changed test filter produced a green report after running no relevant tests. Improve the check at the reporting boundary: require evidence that the intended suite was collected and exercised before declaring it verified. Prove the guard rejects an empty collection and accepts a legitimate targeted run. Documentation-only jobs need a distinct outcome, not a universal minimum test count that misclassifies valid work.
