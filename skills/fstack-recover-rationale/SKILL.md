---
name: fstack-recover-rationale
description: "Reconstruct the evidence behind an existing design or constraint without inventing motives. Use before changing surprising behavior, replacing an old abstraction, or revisiting a consequential historical decision."
---

# Recover rationale

## Starting point

Name the decision or unusual behavior whose rationale matters to the current task. Establish what the system does today from available evidence, then separate that fact from the historical question. Define how the answer could change the proposed work so the search remains bounded.

## Method

1. Identify a precise anchor: an interface, migration, condition, dependency choice, or behavior change. Locate when it appeared or materially changed. Broad repository history is less useful than the smallest history connected to the decision.
2. Build a short chronology from accessible changes, discussions, incident records, design notes, and tests. Preserve dates and versions. Distinguish contemporaneous explanations from later recollections or summaries.
3. Extract explicit reasons, considered alternatives, operating constraints, and rejected approaches. Attribute statements to their source. A comment saying “temporary” establishes an intention at that time, not proof that removal is safe today.
4. Seek counterevidence. Look for a later reversal, a changed dependency, a retired consumer, or a failed attempt at the proposed simplification. Absence of a reason in one channel is not evidence that no reason existed.
5. Classify conclusions by support. Separate documented intent, strong inference, plausible hypothesis, and unknown. Explain an inference’s connecting facts; do not fill missing discussion with a confident story about what an author must have wanted.
6. Test the present relevance of recovered constraints. Check whether the affected consumer, timing condition, compatibility promise, or failure mode still exists. Where permitted, use a focused observation to distinguish a live constraint from obsolete context.
7. Translate the history into current decision guidance: what to preserve, what may be reconsidered, what evidence would permit change, and what remains uncertain. Stop when the history sufficiently informs the current decision or when a named unavailable source prevents further progress.

## What to return

Return a compact chronology, the strongest evidence for the original rationale, later changes, confidence and gaps, and practical implications for the proposed change. Link precise records or supplied excerpts. State whether you recommend preserving, testing, or revisiting a constraint and why; keep that recommendation separate from historical fact.

## Boundaries

Use only authorized history and documents. Do not search unrelated personal records or treat a past author’s apparent preference as current authority. Preserve authorship when discussing prior work. This method investigates rationale; it does not grant permission to revert a decision or modify code.

## Worked example

A parser uses a hand-written scanner. Its original review cites an imminent delivery deadline and uncertainty about adopting a dependency. A benchmark published a year later shows that scanner performing well. Record the contemporary adoption constraints as supported rationale and the later benchmark as subsequent evidence. Do not turn an incidental later advantage into the original motive, or assume that the deadline explains every detail of the scanner.
