---
name: fstack-verify-behavior
description: "Establish whether required behavior is supported by current observations. Use before claiming completion, after a change, or when existing test and runtime evidence needs examination."
---

# Verify behavior

## Starting point

Start with the claimed outcome, acceptance criteria, current candidate, relevant inputs and environment, and the evidence already available. Decide what the claim actually covers: source behavior, an integration, an installed release, or a live operation. A successful result in one scope does not establish another.

## Method

1. Translate each consequential criterion into an observable result, including a failure or boundary case where needed. State what would falsify the claim. Distinguish product expectations from internal implementation details and use an independent source for expected results.
2. Match existing evidence to the candidate and conditions. Check source revision or effective content, configuration, dependency state, data, and environment. Preserve older evidence as history, but do not relabel it current after a relevant change.
3. Choose the smallest adequate set of checks across affected boundaries. Use project-supported mechanisms and realistic inputs. Explain material omissions; a convenient unit test cannot substitute for an integration observation when the claim depends on that integration.
4. Run the required observations when authorized tools are available. Retain the invocation or equivalent operation, actual outcome, counts, timing, and identity of the observed candidate. Distinguish a completed test from collection, setup, a dry run, or a process that exited before exercising behavior.
5. Examine failure and ambiguity honestly. Separate a demonstrated defect from unavailable infrastructure and an insufficient observation. Zero executed checks, suppressed failures, skipped requirements, stale reports, and missing runtime access do not establish success.
6. Reconcile the observations against the original criteria. If repairs occur, identify and rerun the checks whose evidence changed. Finish with a bounded verdict supported by the retained observations, and list exactly what additional evidence would resolve any remaining uncertainty.

## What to return

Return a criterion-to-evidence account, candidate and environment identity, actual executed counts, failures and skips, and a clear conclusion. Use ordinary language to distinguish established behavior, observed failure, blocked execution, and inconclusive evidence. Include reproducible references where available and avoid an undifferentiated “all good” when only part of the requested scope was exercised.

## Boundaries

Verification does not authorize source edits, production probes, publication, or deployment. Use existing grants without repeatedly asking; report a specific missing capability when it prevents the required observation. Never create a passing expected value from the implementation’s own answer or weaken a criterion to accommodate an observed defect.

## Worked example

A backup feature uploads a file and verifies its checksum. Its acceptance criterion also requires recovery onto an empty instance. A permitted restore attempt stops because the required decryption key is unavailable. Report storage and integrity as observed, and recovery as blocked at that prerequisite. A successful upload is not evidence that the user can recover their data; identify the isolated restore check still needed.
