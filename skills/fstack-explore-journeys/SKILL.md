---
name: fstack-explore-journeys
description: "Explore realistic sequences of user or system behavior beyond scripted acceptance cases. Use to investigate interaction, state, recovery, and unexpected behavior through an available product surface."
---

# Explore journeys

## Starting point

Start with the product surface, important user or system goals, known changes, a safe environment, and any existing failure clues. A surface may be an interface, command, event stream, batch process, or device interaction. Establish permitted identities, data, external effects, and cleanup before exercising stateful journeys.

## Method

1. Choose a small exploration charter: a meaningful goal, an important risk, and a bounded session. Identify the normal completion signal and failure signals. Prefer journeys that traverse a changed or uncertain boundary over random actions without an observation plan.
2. Establish the starting state and a reliable reset. Record relevant identity, permissions, data, network conditions, and version. If an action can affect real users or irreversible state, use an approved isolated substitute or stop at that boundary.
3. Perform the ordinary journey once to learn its actual transitions. Observe the visible result and relevant side effects through permitted surfaces. Do not use a direct internal state setter as proof that a normal user or caller can reach the same result.
4. Vary one consequential dimension at a time: ordering, repetition, interrupted completion, elapsed time, identity, permissions, input boundaries, or cross-session state. Follow surprising observations while retaining enough context to distinguish a defect from a misunderstood expectation.
5. Turn each suspected issue into a compact reproducible sequence. Restore the starting state and replay it. Separate confirmed behavior, a one-off observation, and an untested hypothesis; record both the expected result and the source of that expectation.
6. Use the remaining budget on the highest-risk unanswered journey, then stop and clean up owned temporary state. Summarize coverage by journeys and conditions, not a score that implies untested areas are healthy. Hand confirmed issues off with their reproduction and evidence.

## What to return

Return the charter, environment and starting conditions, exercised paths, retained observations, confirmed findings, hypotheses, and unexplored risks. For each issue include a minimal sequence, observed versus expected outcome, impact, and whether replay succeeded. If only planning was possible, return an exploration plan labeled as unexecuted rather than a QA verdict.

## Boundaries

Stay inside authorized tools, accounts, data, and effects. Do not submit real payments, send messages, mutate production state, or alter source merely to make a journey pass without authority. When access is missing, identify the specific observation that is blocked. Exploratory breadth supplements targeted checks; it cannot certify exhaustive correctness.

## Worked example

An inventory page supports selecting records across pages and applying one bulk action. Explore changing filters after selection, navigating with the keyboard, and an item disappearing before confirmation. Track the visible selection count, selected identities, and actual affected records through each transition. A suspicious count becomes a reproducible finding only when the starting selection and resulting affected set can be compared after resetting the synthetic inventory.
