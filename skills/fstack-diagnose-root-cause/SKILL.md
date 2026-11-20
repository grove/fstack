---
name: fstack-diagnose-root-cause
description: "Establish a causal explanation for a specific defect through reproduction and controlled observations. Use when a symptom has several plausible explanations or when a proposed fix is based mainly on correlation."
---

# Diagnose root cause

## Starting point

State the exact symptom, expected behavior, affected scope, and known reproduction conditions. Read available code and observations without treating an early explanation as established fact. Identify the permitted experiments, environment, and budget; preserve useful evidence before changing state.

## Method

1. Reproduce or precisely characterize the symptom at its observable boundary. Record the candidate, inputs, environment, actual result, and expected result. If reproduction is unavailable, distinguish supplied observations from what you have personally executed.
2. Reduce the scenario while checking that the same failure remains. Remove irrelevant data and operations one at a time. Preserve timing, ownership, dependencies, or state that may be part of the mechanism; the smallest example is useful only if it is faithful.
3. Form a small set of plausible causal hypotheses. For each, name an observation that would support it and one that would weaken it. Include an alternative to the first attractive explanation, but do not spend effort enumerating implausible possibilities.
4. Choose the next probe for its ability to distinguish hypotheses. Hold other meaningful variables constant, inspect the relevant boundary, and record the prediction before the observation. Use instrumentation that does not accidentally eliminate a timing or performance problem.
5. Update the explanation after each result. Follow the causal chain from triggering condition through incorrect state or decision to the observed symptom. Reject explanations that account for a nearby event but do not explain why the expected behavior failed.
6. Check the proposed cause against a contrasting case or controlled intervention. A successful repair can support the mechanism, but an unrelated broad rewrite is weak evidence. If a repair is authorized, choose the smallest correction and a regression that distinguishes the faulty behavior from the intended behavior.
7. Stop when the causal explanation is supported well enough to guide the bounded correction, or when the budget or missing access prevents a defensible conclusion. Preserve unresolved alternatives and the next useful probe rather than forcing certainty.

## What to return

Return the symptom and scope, reproduction, hypotheses tested, discriminating observations, causal explanation, confidence, and repair direction. Include the smallest useful regression or verification plan and limitations. Clearly distinguish confirmed observations, source-based inference, and remaining hypotheses; an experiment plan is not an executed experiment.

## Boundaries

Do not change several variables and claim the result proves which one caused the defect. Do not erase the original evidence, weaken requirements, or silently expand the repair. Respect authorized environments and data. If the user requested diagnosis only, provide the correction proposal without editing source. A symptom disappearing once is insufficient proof for an intermittent failure.

## Worked example

A parser loses the final record only when a file lacks a trailing newline. Compare otherwise identical inputs with and without that delimiter. If the reader emits records only on delimiters and discards the remaining buffer at end-of-input, explain that mechanism and its predicted result. Changing encoding at the same time would weaken the comparison. Source inspection supports the hypothesis; an executed controlled replay can test it.
