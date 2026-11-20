# Evaluate whether a skill helps

Use evaluations to decide whether a method produces better engineering outcomes
under stated conditions. Package validation and a convincing example are useful,
but they do not establish that the skill improves a worker's behavior.

## State the claim

Define the contribution you expect. Examples include finding a known causal defect
without changing unrelated behavior, preserving a critical constraint in a cold
handoff, or rejecting an unfair performance comparison. Name the comparison:
unassisted execution, the current skill, or another method applied under comparable
conditions.

Choose a success measure and unacceptable failures before running the case. Keep
correctness, evidence quality, scope compliance, and cost visible separately. A
faster result that invents execution is not a successful tradeoff.

## Select representative cases

Use the cases in [evals/](../../evals/README.md) as seeds. Each case separates worker
task/context from expected properties, forbidden behavior, and evidence for grading.
Include easy controls, difficult discriminating cases, missing capabilities, and
misleading evidence. Extend coverage across relevant technologies and task types.

Avoid tuning only to the cases used while writing a skill. Reserve separate cases
for a later check. If comparing alternatives, keep inputs, tools, time budgets,
permissions, and grader criteria comparable; randomize order where learning or
environment drift could affect the result.

## Prepare a fresh worker

Prepare a selected case in a new destination:

```sh
python tools/prepare_eval.py --case fstack-recover-rationale \
  --output dist/rationale-trial
```

Use the generated worker material and the complete selected skill. The preparation
tool does not run an agent or evaluate its answer. Do not give the worker the case's
`expected`, `forbidden`, or `evidence` grading fields. Restrict access to evaluator
material when the host supports it. Reusing an author's conversation or showing the
intended answer defeats the purpose of the exercise.

Provide tools only when the case actually calls for them and the isolated environment
can safely support them. A reasoning case may be fully assessable from supplied
records. A workspace case needs the stated fixtures and actual execution observations
for claims that depend on running the software.

## Grade the result and the behavior

Retain the task, skill revision, worker output, tool observations, and environment.
Inspect both the final deliverable and how it was obtained. Look for missing checks,
scope expansion, invented source access, fabricated identities, stale evidence, and
unjustified confidence. If a result is not assessable, record why rather than
interpreting it as a pass.

For each criterion, record an observed pass, failure, blocker, or inconclusive result.
Keep critical failures distinct rather than averaging them away in a single score.
Report actual time, operation counts, or cost only when those measurements are
available. Do not estimate unobserved model usage and present it as measured.

## Compare and act

One trial can reveal a concrete defect. It cannot establish a reliable advantage
across tasks. Broader claims need repeated trials, an appropriate baseline, and a
description of variation and uncertainty. Record the sample and avoid choosing only
favorable cases after seeing the result.

When an evaluation finds a problem, revise the smallest responsible part of the
method and repeat the relevant check with preserved history. Keep the failed trial
as evidence. Decide whether to keep, narrow, revise, or remove the method based on
its actual contribution. Use `fstack-evaluate-skills` for a bounded evaluation
design; its presence does not itself perform the experiment.
