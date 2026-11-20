---
name: fstack-prototype-uncertainty
description: "Design and perform the smallest experiment that can resolve a named engineering uncertainty. Use when an important feasibility, interaction, or design claim cannot be settled reliably by discussion alone."
---

# Prototype uncertainty

## Starting point

Name the uncertainty and the decision it blocks. State the competing explanations or outcomes, available evidence, permitted tools and data, and experiment budget. A prototype is useful because of the question it can answer, not because it resembles a finished product.

## Method

1. Express the claim so an observation could contradict it. Specify the relevant workload, users, environment, and boundary. “This approach scales” is too broad; identify the capacity, latency, memory, or interaction behavior that matters to the decision.
2. Choose the cheapest observation that separates the plausible outcomes. Consider a calculation, disposable script, fake dependency, paper interaction, or small integration before building a large slice. Preserve the mechanism being tested even when unrelated details are simplified.
3. Define the success threshold, failure threshold, controls, and stopping rule before running. State which conclusions the experiment cannot support. Select representative inputs and at least one limiting case; do not choose only the example most favorable to the proposal.
4. Keep the experiment isolated and reversible. Use approved synthetic or appropriately protected data. Identify files, resources, and external effects it may create, and plan cleanup. Label shortcuts that would be unacceptable in production so they cannot be mistaken for completed engineering.
5. Run within the budget and capture actual inputs, environment, observations, and errors. Vary one relevant factor at a time when testing causality. When execution is unavailable, return the executable experiment plan and call the result untested.
6. Compare observations with the predefined decision rule. Check whether a control failed, a shortcut invalidated the mechanism, or measurement noise obscures the result. Treat an invalid experiment as inconclusive rather than as evidence for either design.
7. Explain what changed in the decision. Recommend adopt, reject, narrow, or investigate further only within the experiment’s supported scope. Retain useful evidence and remove disposable resources as authorized. Decide explicitly whether any prototype code is worth reworking for production.

## What to return

Return the question, hypothesis or alternatives, experiment setup, controls, decision thresholds, observed results, limitations, and next decision. Include reproduction instructions or a compact experiment artifact when appropriate. Distinguish a viable mechanism from a production-ready implementation and a successful demonstration from representative evidence.

## Boundaries

Do not expand a prototype into a product implementation without a scope decision. Existing permission to investigate does not authorize spending money, publishing services, or using sensitive external data. Do not conceal missing controls or promote unverified assumptions merely because the demonstration looks convincing. Stop at the stated budget or once the decisive uncertainty is resolved.

## Worked example

A proposed settings layout may make account cancellation hard to find. Build a clickable navigation mock and give representative participants an unprompted cancellation task. Predeclare a discovery criterion, compare against the existing layout, and record wrong turns as well as completion. Keep payment and account backends simulated because they do not answer this question. Successful navigation would support discoverability, without establishing production correctness or accessibility across untested interaction modes.
