---
name: fstack-create-feedback-loop
description: "Establish a fast, repeatable, discriminating observation for a specific behavior. Use before iterative implementation or debugging when existing checks are slow, flaky, misleading, or disconnected from the reported symptom."
---

# Create feedback loop

## Starting point

Identify the behavior or symptom, the relevant execution boundary, and the current means of observing it. Record available tools, permitted environments, representative inputs, and the time budget. The goal is a trustworthy loop that can guide changes, not a final claim that the whole system is correct.

## Method

1. Define the observation that separates acceptable from unacceptable behavior. Use an independently stated expected result or a precise symptom. A command that exits successfully without observing the behavior is not yet a useful signal.
2. Choose the narrowest boundary that retains the mechanism of interest. Reduce unrelated setup while preserving consequential state, timing, integration, and side effects. If a substitution removes the failure mechanism, use a more faithful boundary even if it is slower.
3. Establish a known starting state and reset procedure. Record inputs, fixtures, clocks, randomness, identities, and environment assumptions as relevant. Ensure one run does not contaminate the next through cached data, leftover work, or reused identifiers.
4. Run the baseline when execution is authorized and available. Confirm that the loop can reveal the current defect or missing behavior. If the current implementation is already correct, use a safe temporary perturbation or an independently known failing example only when within scope, then restore it.
5. Improve turnaround without weakening the signal. Select focused cases, reduce irrelevant data, or reuse safe setup. Retain checks for correct output and the actual path being exercised. A faster false green is a worse loop.
6. Assess repeatability. For intermittent behavior, record attempts and outcomes and isolate one variable at a time. Establish a useful reproduction rate or explain why the signal remains too noisy to guide causal conclusions. Keep a slower confirmation path for assumptions the fast loop omits.
7. Package the loop so another worker can reset, run, and interpret it. Include the expected observation, known blind spots, captured baseline, and a stopping rule for persistent environment or flakiness problems.

## What to return

Return the behavior under observation, setup and reset instructions, exact operation or test invocation where available, expected result, observed baseline, turnaround, repeatability, and limits. State whether the loop is usable, blocked, or inconclusive. A useful result may be a minimal executable reproduction or a concrete plan when execution is unavailable.

## Boundaries

Do not fix production code merely to make a reproduction easier unless that edit is explicitly part of the task. Do not turn a timeout, missing environment, skipped assertion, or unexecuted plan into success. Respect write scope and restore temporary perturbations. This method creates a signal; it does not by itself establish a root cause or complete verification.

## Worked example

A command-line tool contaminates machine-readable output with diagnostics. Use a small malformed input and capture standard output, standard error, and exit status separately in a local invocation. Compare each against its specified role and restore the fixture before repeating. Combining both streams into one capture would hide the relevant distinction. A successful isolated check does not replace later confirmation through the real consumer pipeline.
