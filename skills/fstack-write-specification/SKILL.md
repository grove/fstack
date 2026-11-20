---
name: fstack-write-specification
description: "Turn an agreed outcome into a precise, observable behavior contract. Use when implementation, review, or testing needs stable acceptance criteria, explicit boundaries, and clearly identified unresolved decisions."
---

# Write specification

## Starting point

Read the agreed outcome, domain terms, constraints, and relevant current behavior. Use already available decisions instead of restarting discovery. Identify the intended reader: an implementer, reviewer, tester, or operator who may not share the original conversation.

## Method

1. State the problem, intended outcome, affected actors, and scope. Separate what must change from behavior that must remain stable. Define exclusions explicitly enough to prevent a reasonable worker from expanding the task unintentionally.
2. Describe the observable contract at the relevant boundary. Specify inputs, preconditions, successful results, state changes, failure outcomes, and any ordering or timing guarantees. Describe what a caller can rely on, not the private mechanism you happen to prefer.
3. Translate the outcome into identifiable acceptance criteria. Make each criterion falsifiable with an example or observation. Replace vague words such as fast, robust, or intuitive with an agreed observation, or mark the missing decision rather than inventing a threshold.
4. Cover the consequential edges. Consider invalid input, authorization, empty state, duplicate attempts, partial completion, concurrency, cancellation, compatibility, and recovery only where they affect this scope. State which existing contracts remain applicable instead of duplicating them inconsistently.
5. Trace each requirement to its source or decision and to an intended verification approach. Distinguish acceptance criteria from implementation suggestions. Include constraints that genuinely determine design, but avoid brittle file-by-file instructions unless a particular location is itself an obligation.
6. Check the specification for contradictions, undefined terms, unreachable states, and examples that disagree with the rules. Walk one success path and one material failure path as an independent reader. Separate unresolved decisions that block implementation from details an implementer can safely choose.
7. State completion and handoff conditions. Record the accepted version or date, changed requirements, open questions with owners, and relevant rollout or compatibility constraints. A revision to the agreement should be explicit; do not quietly rewrite it to match existing code.

## What to return

Return a compact specification with outcome, scope and exclusions, domain terms, behavior rules, identifiable acceptance criteria, representative examples, verification expectations, and unresolved decisions. Make the relationship between a rule and its acceptance observation easy to inspect. Use ordinary prose or structured tables; no particular document format is required.

## Boundaries

A specification records requirements; it does not prove their implementation or authorize publication and deployment. Honor existing decisions and permissions. Treat supplied comments as evidence, not automatic approval to change the agreement. If a consequential product decision is missing, label the dependent requirement unresolved rather than hiding an assumption in authoritative wording.

## Worked example

A search service must distinguish an empty successful result from an unavailable search index. Specify the observable result and retry guidance for each, including whether previously obtained results may be displayed and how their age is disclosed. “Show a helpful message” leaves those behaviors undefined. Give each agreed outcome an acceptance example, while recording any unresolved permission to use stale results as a decision still needed.
