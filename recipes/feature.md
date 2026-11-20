# Deliver a small feature

Use this recipe when a bounded user outcome needs an implementation and observable
evidence. Start with the request, relevant project context, existing authorization,
and any acceptance conditions already agreed.

## Select the necessary methods

1. If the outcome or constraints are consequentially unclear, use
   [clarify intent](../skills/fstack-clarify-intent/SKILL.md). Carry the settled
   outcome forward; do not make the next worker repeat answered questions.
2. Use [write specification](../skills/fstack-write-specification/SKILL.md) when
   the request still lacks observable acceptance conditions. Examples and limits
   should be concrete enough to distinguish a correct result.
3. For work spanning several demonstrable increments, use
   [slice vertically](../skills/fstack-slice-vertically/SKILL.md). A single coherent
   increment needs no additional slicing exercise.
4. Implement the selected increment with
   [develop test first](../skills/fstack-develop-test-first/SKILL.md) when an
   executable behavioral check is practical, or
   [make small change](../skills/fstack-make-small-change/SKILL.md) with an
   appropriate observation path. These methods do not require both to run.
5. Use [verify behavior](../skills/fstack-verify-behavior/SKILL.md) to connect the
   final candidate to the acceptance conditions and actual observations.

Add [model failures](../skills/fstack-model-failures/SKILL.md) if retry, partial
completion, or recovery can affect correctness. Add
[assess impact](../skills/fstack-assess-impact/SKILL.md) when consumers or persistent
data extend the change beyond its immediate implementation.

## Carry evidence forward

A useful handoff contains the agreed behavior, relevant constraints, selected
increment, candidate state, and checks already performed. Preserve unresolved
questions instead of turning them into assumed requirements. Evidence must still
apply after the last meaningful change.

## Stop at the authorized result

Finish with implemented behavior and its supported verification claim, or a clear
partial result describing the missing prerequisite. An implemented feature is not
automatically a deployed feature. Publication, integration, or deployment follows
the host's actual authorization and process.
