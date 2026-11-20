---
name: fstack-review-conformance
description: "Assess whether a fixed candidate satisfies its stated requirements. Use for an independent requirements review without mixing correctness findings with architectural or stylistic preferences."
---

# Review conformance

## Starting point

Start with the candidate and baseline, the accepted specification, relevant decisions, and available verification. Establish the actual reviewed content, including uncommitted changes when they are part of the request. If requirements conflict or are missing, state the ambiguity instead of silently selecting a convenient interpretation.

## Method

1. Extract the in-scope obligations into identifiable criteria. Include negative behavior, error handling, boundaries, and compatibility explicitly required by the agreement. Distinguish those obligations from suggestions, historical expectations, and new preferences introduced during review.
2. Trace each criterion to the relevant implementation path and evidence. Look for missing branches and conditions, not only the main success path. A test name or completion comment is a pointer to inspect, not proof that the promised observation occurred.
3. Construct a concrete counterexample for each suspected mismatch. State input or prior state, the requirement’s expected result, the candidate’s actual or logically implied result, and the consequence. Confirm with authorized execution when available; label static reasoning as such.
4. Challenge the finding before reporting it. Check surrounding guards, applicable input restrictions, earlier decisions, and the exact candidate. Remove findings that depend on an excluded scenario or a misread path. Keep genuine requirement ambiguity separate from a demonstrated defect.
5. Examine whether verification supports the same criterion and current content. Identify checks that miss the boundary, assert only a superficial result, or derive expectations from the implementation. Preserve gaps even when the overall test process reports success.
6. Report disposition by criterion: supported, contradicted, or unresolved. Prioritize violations by their real effect and retain stable finding identifiers for a subsequent review. Stop after the scoped coverage is assessed or a specific missing requirement or observation prevents a conclusion.

## What to return

Return the candidate identity, criterion coverage, supported findings, evidence, and unresolved questions. Each finding needs a criterion reference, concrete mechanism, affected behavior, and verification suggestion. Explain any accepted-risk decision only when it actually exists. Keep design improvements and optional polish out of the conformance verdict.

## Boundaries

Review is read-only unless edits are separately requested. Do not publish comments, resolve discussions, change requirements, or approve integration through inference. Preserve independence accurately: a fresh reading by the same worker is not a separately authenticated reviewer. Changed relevant content invalidates the affected conclusion, even if a previous review approved it.

## Worked example

A ranking contract requires equal-scoring results to retain their incoming order. The candidate sorts equal scores alphabetically. For incoming results Zeta then Alpha with equal scores, the specified order is Zeta then Alpha, while the implementation reverses them. Existing tests use distinct scores and cannot settle that criterion. Report the demonstrated tie-order mismatch and the missing regression observation without prescribing a different ranking architecture.
