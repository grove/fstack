# Skill catalog

The catalog contains 31 independent methods. Groups help discovery; they do not
define an execution order. Each link opens the complete method. Use the
[selection guide](../how-to/choose-skills.md) when responsibilities look similar.

## Understanding

| Skill | Responsibility and useful result |
| --- | --- |
| [fstack-clarify-intent](../../skills/fstack-clarify-intent/SKILL.md) | Resolve consequential unknowns about the desired outcome, scope, and constraints; produce a usable outcome brief. |
| [fstack-trace-behavior](../../skills/fstack-trace-behavior/SKILL.md) | Follow current execution and data flow; explain the supported path and unresolved branches. |
| [fstack-recover-rationale](../../skills/fstack-recover-rationale/SKILL.md) | Reconstruct historical constraints and decisions from records; distinguish documented reasons from plausible interpretations. |
| [fstack-research-evidence](../../skills/fstack-research-evidence/SKILL.md) | Resolve a bounded question with credible evidence; explain conflicts, freshness, and remaining uncertainty. |
| [fstack-challenge-assumptions](../../skills/fstack-challenge-assumptions/SKILL.md) | Examine premises before committing to a solution; identify the assumptions that could change the decision. |

## Design

| Skill | Responsibility and useful result |
| --- | --- |
| [fstack-model-domain](../../skills/fstack-model-domain/SKILL.md) | Establish shared terms, identity, invariants, and state transitions; make ambiguous domain rules explicit. |
| [fstack-write-specification](../../skills/fstack-write-specification/SKILL.md) | Translate an agreed outcome into observable behavior, examples, boundaries, and acceptance conditions. |
| [fstack-design-interfaces](../../skills/fstack-design-interfaces/SKILL.md) | Define coherent boundaries and caller contracts that contain complexity and expose meaningful operations. |
| [fstack-compare-alternatives](../../skills/fstack-compare-alternatives/SKILL.md) | Compare materially different viable options against explicit criteria; justify a bounded choice. |
| [fstack-prototype-uncertainty](../../skills/fstack-prototype-uncertainty/SKILL.md) | Design the cheapest discriminating experiment for a named uncertainty; report what its result can establish. |
| [fstack-model-failures](../../skills/fstack-model-failures/SKILL.md) | Examine partial failure, ordering, retries, ownership, and recovery; identify controls and unresolved failure behavior. |
| [fstack-slice-vertically](../../skills/fstack-slice-vertically/SKILL.md) | Plan small demonstrable behavior increments and dependencies; use a bounded mechanical migration only when that exception is justified. |

## Implementation

| Skill | Responsibility and useful result |
| --- | --- |
| [fstack-create-feedback-loop](../../skills/fstack-create-feedback-loop/SKILL.md) | Establish a fast observation that distinguishes the relevant behavior, with a reliable reset and replay path. |
| [fstack-diagnose-root-cause](../../skills/fstack-diagnose-root-cause/SKILL.md) | Separate causal hypotheses with controlled observations; explain the supported cause and remaining alternatives. |
| [fstack-develop-test-first](../../skills/fstack-develop-test-first/SKILL.md) | Exercise one behavior through a meaningful failing check and passing implementation; keep any cleanup bounded. |
| [fstack-make-small-change](../../skills/fstack-make-small-change/SKILL.md) | Implement the smallest coherent behavioral change within scope; explain the delta and its actual checks. |
| [fstack-refactor-safely](../../skills/fstack-refactor-safely/SKILL.md) | Improve structure while preserving stated observable contracts; retain evidence of preservation. |

## Verification

| Skill | Responsibility and useful result |
| --- | --- |
| [fstack-verify-behavior](../../skills/fstack-verify-behavior/SKILL.md) | Connect requirements to current executed observations; separate demonstrated completion from unverified claims. |
| [fstack-explore-journeys](../../skills/fstack-explore-journeys/SKILL.md) | Investigate realistic stateful paths beyond scripted acceptance; report reproducible observations and coverage limits. |
| [fstack-assess-impact](../../skills/fstack-assess-impact/SKILL.md) | Trace affected consumers, data, compatibility, and lifecycle boundaries; identify change and rollout implications. |
| [fstack-review-conformance](../../skills/fstack-review-conformance/SKILL.md) | Compare a candidate with stated requirements; return evidence-backed deviations without substituting design preference. |
| [fstack-review-design](../../skills/fstack-review-design/SKILL.md) | Assess ownership, complexity, maintainability, and applicable engineering standards; explain consequential findings. |
| [fstack-challenge-adversarially](../../skills/fstack-challenge-adversarially/SKILL.md) | Seek plausible counterexamples to a candidate decision or change; produce a bounded challenge supported by evidence. |
| [fstack-measure-performance](../../skills/fstack-measure-performance/SKILL.md) | Make fair, reproducible measurements under stated conditions; report uncertainty and bounded performance claims. |

## Collaboration

| Skill | Responsibility and useful result |
| --- | --- |
| [fstack-record-decisions](../../skills/fstack-record-decisions/SKILL.md) | Preserve a consequential decision, alternatives, constraints, rationale, and reasons to revisit it. |
| [fstack-preserve-context](../../skills/fstack-preserve-context/SKILL.md) | Prepare a compact, verifiable handoff that a worker can use without the original conversation. |
| [fstack-coordinate-work](../../skills/fstack-coordinate-work/SKILL.md) | Define ownership, dependencies, isolation, and integration across workers; produce a coordination plan within available capabilities. |
| [fstack-reconcile-feedback](../../skills/fstack-reconcile-feedback/SKILL.md) | Evaluate feedback against evidence and scope; explain accepted, rejected, conflicting, or deferred findings. |
| [fstack-communicate-change](../../skills/fstack-communicate-change/SKILL.md) | Explain purpose, changed behavior, evidence, and remaining risk for a reader deciding what happens next. |

## Improvement

| Skill | Responsibility and useful result |
| --- | --- |
| [fstack-encode-lessons](../../skills/fstack-encode-lessons/SKILL.md) | Convert an observed recurring failure class into a structural safeguard whose value can be checked. |
| [fstack-evaluate-skills](../../skills/fstack-evaluate-skills/SKILL.md) | Compare skill effectiveness with a baseline on controlled, representative tasks; retain limitations and failures. |

Names and groups are also recorded in [`catalog.json`](../../catalog.json).
The [package reference](packages-and-tools.md) describes the machine-readable
metadata. [Recipes](../../recipes/README.md) illustrate a few optional combinations.
