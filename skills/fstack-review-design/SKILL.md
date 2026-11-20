---
name: fstack-review-design
description: "Assess a candidate\u2019s structural quality using concrete maintenance and failure consequences. Use to review responsibility, interfaces, ownership, complexity, and project engineering standards."
---

# Review design

## Starting point

Start with the fixed candidate, intended change, relevant project conventions, and enough surrounding code or design material to understand its callers. Establish the scale and risk of the work. A local correction should not automatically trigger a redesign of the entire system or a new set of universal style rules.

## Method

1. Identify the responsibilities and knowledge boundaries introduced or changed. Determine who owns state, lifecycle, validation, error translation, and recovery. Ask whether callers must coordinate internal details that should belong to one accountable boundary.
2. Inspect the complete caller contract: inputs, outputs, failure modes, ordering requirements, configuration, performance promises, and side effects. Compare the complexity callers must understand with the useful behavior the interface provides; implementation length alone says little about interface quality.
3. Trace a likely future change and a plausible failure through the design. Look for duplicated decisions, scattered invariants, temporal coupling, hidden global state, unnecessary variants, and unclear cleanup. Connect each concern to a specific maintenance burden or failure mechanism.
4. Evaluate testability at observable boundaries. Check whether the design permits independent expectations and realistic substitutes where behavior genuinely varies. Avoid demanding indirection for hypothetical future implementations or calling every internal helper a public contract.
5. Consider a smaller structural correction for each material concern. Preserve coherent existing conventions and explain the tradeoff. Separate defects that threaten current behavior, justified maintainability improvements, and optional preferences; do not inflate severity to win an argument about taste.
6. Check proposed findings against the actual scope and evidence. Remove duplicates and claims already prevented by another part of the design. Stop when the relevant boundaries have a defensible assessment; retain uncertainty when missing callers or operational facts prevent one.

## What to return

Return a concise structural assessment and prioritized findings. For each, name the boundary, the problematic dependency or obligation, a realistic consequence, supporting evidence, and the smallest useful response. Identify preserved strengths and explicit tradeoffs where they help a decision, without assigning an unsupported aggregate quality score.

## Boundaries

This skill evaluates structure, not a substitute set of product requirements. Keep requirement conformance and business decisions separate. Do not edit or publish unless requested, and do not create a mandatory rewrite from an optional improvement. A finding needs more than resemblance to a named pattern or violation of personal preference.

## Worked example

A report formatter reads the process timezone internally, although two callers now require different timezone settings. The concern is hidden configuration ownership: callers cannot express their requirement, and tests must alter process state. Passing the timezone through the existing formatting boundary makes that dependency explicit. Preserve the current default and output contract; a general dependency container or new formatting framework has no demonstrated benefit here.
