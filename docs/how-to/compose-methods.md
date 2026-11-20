# Compose methods without hidden dependencies

Use composition when one method's result becomes useful input to another. Keep
the task's outcome and authority visible across the handoff. The optional
[recipes](../../recipes/README.md) illustrate common combinations; they are not
executed pipelines or mandatory sequences.

## 1. Name the responsibility at each step

Write down the result you need from each method. For a disputed defect, that might
be a replayable observation, a causal explanation, a bounded correction, and current
verification. Avoid a plan that says only “run diagnosis, implementation, and review”
without specifying what each result must establish.

Use supplied information when it is already adequate. A developer may provide a
clear specification directly; no clarification skill is then required. A useful
handoff may be a short note, a diagram, a source reference, or a recorded test result.

## 2. Pass the relevant result explicitly

A receiving worker needs the question, scope, candidate identity, relevant evidence,
material open issues, and its next responsibility. It should not need an entire
conversation or an undocumented predecessor's memory.

For example:

```text
Next responsibility: verify the correction against the accepted behavior.
Candidate: the current isolated change identified in the supplied diff.
Requirement: a repeated request must not create a second charge.
Diagnosis: the retained replay shows the duplicate after a response timeout.
Change: request identity is now checked at the ownership boundary.
Evidence: focused regression and its before/after results are attached.
Limits: the integrated retry path has not yet been exercised.
Scope: execute the approved local checks; do not publish or deploy.
```

The receiver must inspect whether the provided evidence still applies. A previous
worker's confidence is context, not independent proof.

## 3. Separate completion claims

Intent clarification completes when the material outcome is understood. A design
comparison completes when a defensible choice and its tradeoffs are recorded.
Implementation completes its bounded change; verification assesses behavior using
the actual candidate. A good design note does not prove the software is running.

When code, dependencies, configuration, or relevant inputs change, revisit affected
evidence before claiming the combined work is complete. Preserve the old result and
explain the new observation instead of silently relabeling stale proof.

## 4. Handle uncertainty and repair locally

Give an uncertain step a bounded budget and a condition for stopping. If an experiment
cannot distinguish alternatives, return the uncertainty and a better next observation.
If a reviewer identifies a concrete defect, evaluate the claim, make an authorized
correction, and refresh affected verification. Do not repeat broad reviews after a
format-only correction unless the remaining risk warrants them.

An unresolved blocker should remain visible at the handoff. A timeout or exhausted
budget is not acceptance. Conversely, do not activate extra methods merely because
they are available once the necessary evidence is sufficient.

## 5. Parallelize only independent ownership

Use `fstack-coordinate-work` when workers need shared planning. Define each worker's
inputs, output, write ownership, dependency assumptions, budget, and integrator.
Give workers isolated mutable state. Verify the combined result after integration;
separately passing branches do not establish that their combination behaves correctly.

The coordination method can produce a plan for a human or a host to execute. It
does not imply that an agent-dispatch API, tracker write capability, or scheduler
exists. External actions still use the host's normal authority and concurrency rules.
