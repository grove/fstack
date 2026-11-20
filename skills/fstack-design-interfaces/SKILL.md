---
name: fstack-design-interfaces
description: "Design coherent boundaries that keep caller obligations small while containing implementation complexity. Use when responsibilities leak across callers, a module is difficult to test, or an interface is being created or changed."
---

# Design interfaces

## Starting point

Read the required behavior, actual callers, constraints, and existing ownership boundaries. Treat an interface as everything a caller must know: inputs, outputs, errors, ordering, resource lifetime, configuration, and meaningful performance obligations. Type signatures alone do not describe that contract.

## Method

1. Write a short caller example before designing internal structure. Include the normal use and an important failure or cancellation path. Notice how much knowledge the caller must supply and which details repeat across callers.
2. Group behavior around one coherent responsibility and an accountable owner. Identify state and resources that must change together. Keep invariants near the code that can enforce them instead of asking every caller to reconstruct the same safety rules.
3. Reduce the exposed coordination burden. Prefer an operation that expresses the caller’s intent over a sequence of low-level steps whose ordering is easy to misuse. Preserve information the caller genuinely needs; a small surface is not useful if it hides important uncertainty or failure.
4. Specify the full contract. Decide how invalid input, partial failure, cancellation, retries, ownership transfer, and cleanup are represented when relevant. Make defaults and required configuration visible. Avoid APIs that look safe only because callers rely on undocumented global state.
5. Test the boundary conceptually with two distinct caller scenarios and an independent behavioral observation. Ask whether the proposed interface concentrates knowledge or merely moves complexity into another layer. Introduce variation points for demonstrated needs rather than imagined future implementations.
6. Compare the proposed boundary with the existing design or a credible alternative. Consider caller simplicity, locality of change, enforceable invariants, compatibility, and operational costs. Do not use line-count ratios or number of methods as a substitute for those judgments.
7. Describe an incremental transition when consumers already exist. Identify adapters or compatibility periods that are actually necessary, and name the evidence needed before removing the old interface. Stop before implementing unless the request includes that work.

## What to return

Return the responsibility and owner, representative caller examples, full behavior contract, hidden implementation concerns, error and lifetime semantics, and important tradeoffs. Explain the proposed verification boundary and migration implications. Keep the design usable without prescribing a language, framework, inheritance pattern, or dependency mechanism.

## Boundaries

Respect project vocabulary and conventions rather than imposing one universal terminology. Do not invent extension points for unsupported future cases. A design exercise does not authorize source changes or consumer migration. If a required guarantee is impossible with the available dependency, expose that conflict instead of concealing it behind a tidy signature.

## Worked example

A search interface exposes storage offsets, leaving callers to combine pagination and ordering. Concurrent inserts then produce repeated or missing rows. Consider a query boundary that owns stable ordering and continuation, returning items and an opaque continuation value with an explicit expiry contract. Walk through an initial query and a resumed one. State whether results belong to a fixed snapshot; a short signature cannot silently promise both consistency and unrestricted live updates.
