# Resolve a defect

Use this recipe for a reported mismatch between expected and observed behavior.
Start with the symptom, expected behavior, affected state, and available records.
Separate a suggested cause from an established cause.

## Select the necessary methods

1. Use [create feedback loop](../skills/fstack-create-feedback-loop/SKILL.md) if
   there is no practical way to reproduce or distinguish the failure. Establish
   setup, observation, and reset before changing several things at once.
2. Use [diagnose root cause](../skills/fstack-diagnose-root-cause/SKILL.md) to
   compare causal explanations. Prefer an observation that separates hypotheses
   over collecting more instances of the same symptom.
3. Make the correction with
   [develop test first](../skills/fstack-develop-test-first/SKILL.md) when a
   regression check can demonstrate the specific failure before the fix. Use
   [make small change](../skills/fstack-make-small-change/SKILL.md) for the bounded
   implementation when another observation mechanism is needed.
4. Use [verify behavior](../skills/fstack-verify-behavior/SKILL.md) against the
   corrected candidate, including a nearby case that distinguishes the intended
   fix from an overbroad workaround.

Use [trace behavior](../skills/fstack-trace-behavior/SKILL.md) when the execution
path is unknown. Add [assess impact](../skills/fstack-assess-impact/SKILL.md) if
existing data, other consumers, or recovery work may remain affected after the
code correction.

## Keep the diagnosis testable

Carry the failed observation, tested hypotheses, causal evidence, candidate
change, and current verification into the next step. If the symptom disappears
without a discriminating observation, report that limit. Intermittent behavior
requires enough repetition or controlled conditions to support the claim made.

## Stop at a supported correction

Explain what failed, why the evidence supports the correction, and what remains
unverified or unrepaired. An incident may still require authorized data recovery
or operational work. Use [encode lessons](../skills/fstack-encode-lessons/SKILL.md)
when observed recurrence justifies a lasting safeguard beyond the local fix.
