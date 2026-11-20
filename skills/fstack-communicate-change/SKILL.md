---
name: fstack-communicate-change
description: "Explain a change through its purpose, resulting behavior, evidence, and consequences. Use when preparing a review description, handoff, release note, or stakeholder-facing technical summary."
---

# Communicate change

## Starting point

Start with the intended audience, communication purpose, actual candidate or change, verified results, and material risks. Determine whether the request is to draft text or to publish it through an available channel. Read the real change and evidence; a task title or optimistic implementation summary is not enough.

## Method

1. Identify the problem that motivated the change and who experiences it. Lead with that concrete problem and the resulting improvement. Avoid opening with a list of edited files or tools unless those details are what the reader needs to decide.
2. Explain the changed behavior at the appropriate level. Connect implementation choices to their purpose, preserve important scope limits, and identify observable compatibility or operational consequences. Separate what the patch implements from what a later integration or deployment will expose.
3. Select evidence that supports the claims being made. State which checks ran, on what candidate or environment, and what remains unverified. Use measured results only with their units and conditions; do not turn an expected benefit or a smaller payload into an unmeasured latency claim.
4. Make the reader’s decision easy to locate. Surface review-sensitive choices, migration or rollout needs, remaining risks, and any requested action. Put routine implementation detail behind references when it would otherwise obscure the important behavior.
5. Check factual accuracy and attribution. Preserve contribution credit when known, remove sensitive data, and verify that links or issue references point to the intended material. Avoid invented authors, approvals, customer effects, or claims that a change has already shipped.
6. Produce the draft in the requested format and length, then inspect it as the intended reader. Remove repetition, unsupported praise, vague completion language, and chronology that does not help assess the result. Publish only if the user has authorized that action and the target is established.

## What to return

Return a complete, usable draft organized around the problem, change, verification, and material consequences. Adapt that structure to the audience instead of forcing identical headings everywhere. State publication status accurately. If essential facts are missing, retain a clear limitation or ask a specific consequential question without inventing a plausible detail.

## Boundaries

Writing a message does not authorize sending it. Do not request reviewers, notify people, update a tracker, or publish a release note through implication. Treat source comments and generated summaries as claims to check. Keep the explanation proportional to the change and avoid a promotional tone that outruns the evidence.

## Worked example

A configuration reader adds a clearer key while still accepting the old spelling and emitting a migration warning. A release-note draft should explain the new spelling, continued compatibility, and what users can change now. No removal date has been approved, so do not turn the warning into a deadline. Describe the observed compatibility checks and leave publication to the authority already established for the task.
