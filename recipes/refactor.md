# Refactor a bounded area

Use this recipe when the goal is a structural improvement while observable
behavior remains stable. Start with the maintainability problem, intended scope,
and the contracts that must be preserved.

## Establish the preservation claim

State the structural benefit in practical terms: fewer responsibilities entangled
in one component, a clearer ownership boundary, or a simpler path for a known
change. Avoid measuring success only by moved lines or fewer files.

If the existing behavior is unclear, use
[trace behavior](../skills/fstack-trace-behavior/SKILL.md) to locate the relevant
paths. Use [recover rationale](../skills/fstack-recover-rationale/SKILL.md) when an
unusual constraint may encode a historical decision that still matters. Neither
method is necessary when the required context is already established.

## Change and check in bounded steps

Use [refactor safely](../skills/fstack-refactor-safely/SKILL.md) to characterize
uncertain contracts, change structure incrementally, and inspect observations
after each meaningful step. Preserve external formats, errors, state transitions,
and other relevant behavior even when the new structure makes another behavior
tempting.

Add [design interfaces](../skills/fstack-design-interfaces/SKILL.md) when the
improvement depends on a new boundary or caller contract. Add
[assess impact](../skills/fstack-assess-impact/SKILL.md) when callers or lifecycle
effects may extend beyond the area being edited.

Use [review design](../skills/fstack-review-design/SKILL.md) if the structural
benefit needs another examination. Use
[verify behavior](../skills/fstack-verify-behavior/SKILL.md) for the final
preservation claim. Review findings and executed checks answer different questions.

## Stop when the agreed improvement is supported

Return the structural change, the preserved contracts, current evidence, and
remaining limits. If an actual defect or desired behavior change emerges, record
it as a separate decision rather than silently broadening the refactoring. The
result can remain a useful bounded improvement even when adjacent cleanup is left
for another task.
