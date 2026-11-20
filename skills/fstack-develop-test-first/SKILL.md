---
name: fstack-develop-test-first
description: "Implement a bounded behavior through a discriminating failing test followed by the smallest correct change. Use when test-first development is requested or when a focused regression provides a reliable guide to the intended behavior."
---

# Develop test first

## Starting point

Read the intended behavior, relevant public boundary, existing tests, and authorized change scope. Use already agreed criteria and test boundaries where available. Clarify only a missing decision that changes correctness; do not require a new approval ritual for ordinary tests within the task.

## Method

1. Choose one observable behavior increment. Identify the public operation and a concrete example whose expected result follows from the requirement, a worked calculation, or another independent source. Do not derive the expected answer by repeating the implementation’s own logic.
2. Write the smallest useful test for that increment. Prefer inputs and outcomes meaningful to a caller. Replace unstable external boundaries only when the substitute preserves the contract being tested; avoid asserting private call sequences merely because they are easy to mock.
3. Run the test against the unchanged production behavior and inspect the failure. Confirm that it fails for the intended missing or incorrect behavior. A syntax error, unavailable service, broken fixture, or test that never executes does not establish the red phase.
4. Make the smallest coherent implementation change that satisfies the behavior. Keep surrounding obligations intact. Do not hard-code the observed example, weaken the assertion, or introduce speculative cases and abstractions that the current increment does not require.
5. Run the focused test and relevant neighboring checks. Inspect the actual results. If the new test was already green before the change, it did not demonstrate the intended gap; revise the example or explain that the behavior already existed before claiming a test-first implementation.
6. Repeat one behavior increment at a time. Let each observation inform the next test and change. After green, perform only a small behavior-preserving cleanup justified by current duplication or clarity, and re-run affected checks. A larger restructuring deserves its own bounded task.
7. Verify the completed scope with the appropriate broader checks. Record the failing-before and passing-after evidence, final candidate, tests actually executed, and coverage limits. Stop when the accepted behavior is established or a missing prerequisite prevents trustworthy execution.

## What to return

Return the behavior implemented, public test boundary, independent expected results, observed red and green outcomes, source change summary, broader verification, and remaining limits. Make clear whether all required checks ran. Keep historical failures intact as evidence of discrimination; do not count them as current-candidate failures or silently discard them.

## Boundaries

Use this discipline where a meaningful test can guide the work; do not create brittle tests merely to follow a ritual. If execution is unavailable, report the work as unverified and do not claim red or green. Respect existing scope and preserve unrelated work. This method authorizes no external publication, integration, or deployment.

## Worked example

A display-name cleaner must remove surrounding whitespace while preserving spaces inside a name. Use “  Mira Chen  ” and the expected result “Mira Chen”. Observe the existing function fail that assertion before editing. Add a separate example protecting the interior space. An assertion that computes its expected result by invoking the cleaner again cannot detect mistakes.
