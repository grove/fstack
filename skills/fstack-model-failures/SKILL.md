---
name: fstack-model-failures
description: "Analyze how a bounded operation behaves under partial failure, retries, concurrency, and recovery. Use when correctness depends on state crossing process, storage, ownership, or time boundaries."
---

# Model failures

## Starting point

Identify the operation, actors, state owners, external effects, and guarantees that matter to callers. Read the success path and actual dependency guarantees. Start with one consequential operation rather than attempting an exhaustive threat or reliability audit of the entire system.

## Method

1. Draw or describe the operation’s meaningful steps and state transitions. Mark where information or authority crosses a boundary and where an effect becomes durable or irreversible. Separate initiation, acknowledgement, and observed completion.
2. Interrupt the operation at each consequential boundary. Consider a failure before an effect, after the effect but before acknowledgement, and during recovery. Ask what each participant knows at that moment; uncertainty about an outcome is different from confirmed failure.
3. Examine retries and duplicates. Define the logical operation identity, its scope and lifetime, where duplicate detection is durable, and what happens when an identity is reused with different meaning. A retry is safe only if repeated effects are prevented or acceptably compensated.
4. Examine overlapping operations and delayed messages. Identify the owner of each invariant, the expected version or ordering condition, and what stale work can still change. Include cancellation, timeout, and resource cleanup where they can race with completion.
5. Choose a response for each material failure: reject safely, retry within a bound, reconcile by observation, compensate, or escalate. State the conditions under which the response itself is safe. Compensation may be a new fallible operation, not a perfect reversal.
6. Connect detection to recovery. Specify how an operator or automated worker can distinguish pending, completed, failed, and unknown outcomes using durable evidence. Identify alerts, reconciliation records, and tests that exercise the critical interruption points.
7. Prioritize the failures by consequence and plausibility. Report guarantees that are unsupported by the dependencies. Recommend the smallest change or experiment needed to close the important gaps, with remaining risks explicit.

## What to return

Return the success-path model, state owners, important failure windows, knowledge at each boundary, retry or reconciliation rules, and recovery verification. A failure table is often useful: interruption, possible state, observable evidence, safe next action, and unresolved question. Link each important invariant to its enforcement and test location when known.

## Boundaries

Modeling does not authorize fault injection in a live system, data restoration, or changes to operational policy. Do not promise exactly-once effects merely because messages are retried or a lock exists. Distinguish dependency guarantees from assumptions. Stop when the selected operation’s material risks are explained; use a separate scoped assessment for unrelated security or capacity concerns.

## Worked example

Two editors load revision four and independently save replacements. A later save can silently erase the earlier editor’s work. Model the interval between reading and writing, then require the save to apply only if the stored revision still matches. Checking the revision in a separate earlier operation leaves the race open. Define the conflict response and preserve the rejected draft so recovery does not require reconstructing someone’s work.
