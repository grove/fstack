---
name: fstack-challenge-adversarially
description: "Seek plausible counterexamples to a consequential proposal or change. Use when ordinary review may share assumptions and you need a bounded, evidence-based challenge to a specific claim."
---

# Challenge adversarially

## Starting point

Start with the claim under challenge, the candidate or proposal, relevant constraints, available evidence, and a review budget. Name what would count as a material failure. The goal is to discover a defensible counterexample or strengthen a bounded conclusion, not to manufacture disagreement or collect a predetermined number of objections.

## Method

1. Restate the strongest defensible version of the claim, including its scope and assumptions. Identify the system boundary and which guarantees come from another component. Distinguish a desired property from an established guarantee before trying to break it.
2. Select a few consequential challenge directions: boundary inputs, hostile or mistaken callers, interrupted operations, stale state, concurrency, cross-version behavior, or evidence integrity. Choose directions from the actual mechanism and stakes rather than a universal attack checklist.
3. Construct the smallest plausible counterexample for each direction. Specify initial state, sequence, timing or ordering, and the resulting violation. Label an executable reproduction, a source-supported inference, and an unsupported possibility differently.
4. Attempt to falsify your own objection. Inspect guards, ownership, external guarantees, and scope exclusions that might prevent it. Drop or narrow objections that do not survive this check. Record the observation that would resolve uncertainty instead of presenting possibility as fact.
5. Use independent review when it is available, justified, and authorized. Supply the same bounded materials without leading the reviewer toward an intended answer. Treat findings as claims to verify, not votes; different role labels or unanimous models do not establish independent evidence.
6. Synthesize the surviving challenges and the assumptions that held. Use at most the agreed follow-up rounds, focusing later passes on changed evidence and unresolved material claims. Stop when the budget is exhausted or only unsupported objections remain; silence and exhaustion are not approval.

## What to return

Return the challenged claim, supported counterexamples, cleared objections, unresolved assumptions, and a proportionate recommendation. Each material finding needs a failure mechanism, consequence, evidence, and a minimal confirming experiment or correction. State whether another reviewer actually participated and what independence could be established; do not invent review identities or consensus.

## Boundaries

Perform analysis without changing the candidate or publishing findings unless authorized. Do not transmit private materials to another service merely to obtain diversity. Keep review effort proportional to risk, and allow an honest conclusion that no supported counterexample was found within the examined scope. That conclusion remains bounded by evidence and coverage.

## Worked example

A priority queue always takes the highest-priority waiting job. Its design claims every submitted job eventually runs, while allowing high-priority arrivals indefinitely. Construct an arrival sequence that always places another high-priority job ahead of one low-priority job. The sequence refutes the unconditional fairness claim without demonstrating a production incident. A bounded arrival assumption, aging rule, or reserved capacity would need its own analysis before restoring that guarantee.
