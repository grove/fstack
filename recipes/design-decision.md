# Resolve a design decision

Use this recipe when materially different viable approaches have different costs
or risks. Start with the decision to make, its scope, constraints, and when the
choice is needed. Avoid inventing alternatives solely to justify a predetermined
answer.

## Establish what could change the choice

Use [challenge assumptions](../skills/fstack-challenge-assumptions/SKILL.md) when
the proposal depends on uncertain premises. Identify which premise would change
the choice and what information could resolve it. Domain ambiguity may instead
need [model domain](../skills/fstack-model-domain/SKILL.md) before comparing
implementations of conflicting concepts.

Use [compare alternatives](../skills/fstack-compare-alternatives/SKILL.md) to
evaluate viable options against explicit criteria. Include the current approach
when retaining it is viable. Consider failure behavior and reversibility where
they affect the decision; do not manufacture precise scores from weak evidence.

## Resolve only consequential uncertainty

Use [research evidence](../skills/fstack-research-evidence/SKILL.md) when the
answer can be established from credible existing records. Use
[prototype uncertainty](../skills/fstack-prototype-uncertainty/SKILL.md) when a
bounded experiment can distinguish options more directly. Choose the least costly
method that can change the decision, then return its result and limitations to
the comparison.

For a consequential candidate, a bounded
[adversarial challenge](../skills/fstack-challenge-adversarially/SKILL.md) can seek
a plausible counterexample. Reopen the choice when new evidence changes a
decisive premise; disagreement alone does not justify an endless review loop.

## Preserve the decision

Use [record decisions](../skills/fstack-record-decisions/SKILL.md) for a choice
that future work will depend on. Record the scope, selected approach, meaningful
alternatives, decisive evidence, tradeoffs, and conditions for revisiting it.

Stop with a justified choice or a bounded unresolved decision naming the missing
evidence and its consequence. A design decision does not establish implementation
correctness or authorize applying the choice to unrelated parts of a system.
