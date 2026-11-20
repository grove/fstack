---
name: fstack-compare-alternatives
description: "Compare materially different viable approaches against explicit constraints and decision criteria. Use when a consequential design choice has real tradeoffs or when an attractive proposal has not been tested against alternatives."
---

# Compare alternatives

## Starting point

State the decision, desired outcome, hard constraints, and who owns preference tradeoffs. Gather known workload and operating evidence. Determine which parts of the decision are reversible and which create costly commitments.

## Method

1. Define the decision criteria before evaluating favorites. Separate nonnegotiable constraints from preferences and identify the evidence behind each. A latency ceiling or compatibility promise is a gate; a preference for familiarity is a tradeoff to explain.
2. Develop at least two materially different feasible approaches when the problem genuinely permits them. Vary responsibility placement, data flow, state ownership, or operational mechanism rather than renaming the same structure. Include extending the current solution or doing less when credible.
3. Describe each alternative at a comparable level of detail. Show how a representative caller or scenario works, where complexity lives, how it fails, and what is required to operate and change it. Do not compare a polished favorite with deliberately weak sketches.
4. Eliminate options that violate hard constraints, using calculations or evidence where available. Mark unsupported estimates as estimates. If feasibility depends on an unknown, identify the smallest measurement or prototype that can decide it.
5. Compare the remaining tradeoffs directly. Discuss correctness, simplicity, migration, ownership, reliability, performance, and cost only as relevant. Avoid arbitrary weighted scores that disguise a value judgment or combine incomparable quantities into false precision.
6. Check sensitivity: would the recommendation change with a plausible workload shift, changed constraint, or failed assumption? Identify the conditions under which another option would become preferable. This separates a robust choice from a narrow bet.
7. Recommend an option with reasons, accepted disadvantages, and a reconsideration trigger. If the evidence cannot distinguish the candidates, propose the next discriminating experiment or ask the decision owner to resolve the actual preference tradeoff.

## What to return

Return the decision and criteria, comparable alternative sketches, feasibility exclusions, a concise tradeoff comparison, key unknowns, and a reasoned recommendation. Include the evidence supporting quantitative claims and distinguish calculations from observations. State what would change the recommendation and which commitments need explicit acceptance.

## Boundaries

Do not create a design competition for a trivial settled choice. If only one approach satisfies a genuine constraint, explain that result without inventing a second. Do not implement alternatives, spend money, or delegate costly work without existing authority. This method selects among approaches; it does not establish production correctness by argument alone.

## Worked example

A nightly reconciliation finishes by 04:30 against a 06:00 deadline, but malformed inputs occasionally require manual repair. Compare strengthening the current batch with replacing it by continuous processing. Earlier completion has little value unless someone needs fresher results; both options must address malformed data. Prefer the change that meets the real reliability need with acceptable operating cost, and name any volume growth or freshness requirement that would change the decision.
