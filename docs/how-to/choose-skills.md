# Choose the smallest useful set of skills

Start with the uncertainty or engineering responsibility in front of you. Select a
skill because its result will resolve that need, rather than because a lifecycle
stage usually includes it.

## Identify the result you need

| Need | Start with |
| --- | --- |
| A clear outcome, scope, and consequential unanswered questions | `fstack-clarify-intent` |
| A map of current execution and data flow | `fstack-trace-behavior` |
| Evidence about historical constraints or decisions | `fstack-recover-rationale` |
| A testable statement of agreed behavior | `fstack-write-specification` |
| A reliable observation before changing code | `fstack-create-feedback-loop` |
| A causal explanation supported by discriminating observations | `fstack-diagnose-root-cause` |
| A bounded behavioral change | `fstack-make-small-change` |
| Evidence that the current result satisfies its requirements | `fstack-verify-behavior` |
| A useful context packet for another worker | `fstack-preserve-context` |

Use the [catalog](../reference/catalog.md) for responsibilities not listed here.
Give the selected method the available task information directly. You do not need
to run an earlier skill merely to manufacture an input format.

## Distinguish nearby responsibilities

| Pair | Choose by the question being answered |
| --- | --- |
| Clarify intent / Write specification | Clarification resolves what is wanted; specification makes agreed behavior and exclusions observable. |
| Trace behavior / Recover rationale | Tracing establishes how the current system works; rationale investigation explains supported historical reasons and labels unknown motives. |
| Research evidence / Prototype uncertainty | Research evaluates existing sources; a prototype creates a discriminating observation about an uncertainty. |
| Challenge assumptions / Challenge adversarially | Assumption work examines the problem's framing; adversarial work seeks realistic counterexamples to a candidate conclusion or change. |
| Model domain / Design interfaces | Domain modeling names concepts and rules; interface design decides what callers must know and who owns implementation complexity. |
| Compare alternatives / Review design | Alternatives support a decision among viable options; review assesses a particular design against concrete engineering concerns. |
| Create feedback loop / Verify behavior | A feedback loop enables fast, reliable learning during work; verification establishes a bounded completion claim for the current candidate. |
| Develop test-first / Refactor safely | Test-first development establishes new behavior through a failing case; refactoring preserves existing observable behavior while changing structure. |
| Review conformance / Review design | Conformance checks stated requirements; design review checks ownership, complexity, and maintainability. Report these judgments separately. |
| Record decisions / Preserve context | A decision record explains one consequential choice; a handoff packages current state, evidence, and the next bounded action. |

## Add a method only for a concrete reason

For a small correction with a clear specification and a dependable test, a bounded
change and verification may be enough. Add diagnosis when the cause is uncertain.
Add impact assessment when consumers, data, compatibility, or timing may be affected.
Add an alternative-design exercise when the choice has meaningful competing costs.

Use a test-first method when a discriminating test can guide the implementation.
Do not manufacture a fragile test for a claim that needs a different observation.
Use an independent reviewer when risk or policy requires one; a new role label in
the same conversation does not establish independence.

## Keep scope visible

State the question, supplied evidence, allowed actions, budget, and intended result.
If the method encounters a missing capability, let it return a useful partial result
with a specific limitation. Do not reinterpret an analytical result as proof that a
tool was run or a change was deployed.

For common combinations, see the [recipes](../../recipes/README.md).
