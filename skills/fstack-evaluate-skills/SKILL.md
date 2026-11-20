---
name: fstack-evaluate-skills
description: "Evaluate whether a skill improves outcomes under controlled conditions. Use before adopting or changing engineering guidance when its benefit, cost, or failure modes need evidence."
---

# Evaluate skills

## Starting point

Start with a falsifiable claim about one skill or revision, the users and tasks it is meant to help, the current alternative, and a bounded evaluation budget. Define the decision the evaluation should support. Installation success, persuasive output, and agreement between reviewers do not establish that the skill improves engineering work.

## Method

1. Define success before running trials. Choose observable task outcomes and consequential constraints such as correctness, evidence integrity, scope, or authorization. Treat cost, time, and review effort as additional dimensions; do not average a serious failure away with attractive presentation or speed.
2. Select representative cases, including ordinary work, boundary conditions, misleading evidence, and unavailable prerequisites. Keep evaluation cases separate from examples used to author the skill. Give workers the raw task and necessary materials, withholding the grader’s expected answer and your suspected defect.
3. Choose an appropriate comparison: no skill, the current skill, or the best existing method. Hold the agent configuration, tools, environment, context, budget, and task distribution comparable. Use matched cases and randomized or balanced ordering where feasible; record unavoidable differences instead of attributing them to the skill.
4. Run fresh, bounded trials and preserve the actual artifacts, traces, failures, and resource use available. Do not quietly repair only one condition, discard inconvenient cases, reuse a solved conversation as a fresh trial, or invent model settings and costs that the host did not expose.
5. Grade against the predetermined criteria, ideally without revealing the condition to the grader. Report per-case outcomes and important failure modes before aggregates. Use repeated observations and uncertainty estimates only when the design supports them; a small demonstration remains a demonstration.
6. Decide whether to adopt, revise, narrow, or retire the skill. Separate evidence of usefulness in the tested setting from a universal claim. If the result is inconclusive or the cost exceeds the benefit, state that directly and propose the smallest additional test that could change the decision.

## What to return

Return the claim, case selection, comparison conditions, rubric, actual results, observed cost and time, uncertainty, failures, and recommendation. State which work was executed and which remains an evaluation plan. Preserve enough information for another evaluator to repeat the trial or understand why the comparison does not support a causal conclusion.

## Boundaries

Evaluation does not authorize expensive model calls, private-data transfer, live system mutation, or publication. Use supplied limits and approved materials. Do not describe structural linting as behavioral validation, report unavailable usage as zero, or claim improvement from incomparable tasks. Optimize for informative evidence rather than a larger pass count.

## Worked example

A verification skill scores well because its answers contain all required section headings, even when they claim success from failing logs. The rubric measures presentation without checking the intended judgment. Add cases whose raw evidence distinguishes passed, failed, and blocked work, and grade the conclusions and supporting observations. Repeat a controlled comparison with fresh cases; a more polished report is not evidence of more reliable verification.
