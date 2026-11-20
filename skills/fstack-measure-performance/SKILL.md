---
name: fstack-measure-performance
description: "Design fair measurements and make claims proportional to the observed data. Use for performance comparisons, regressions, capacity questions, or evaluating an optimization."
---

# Measure performance

## Starting point

Start with the performance question, the user-relevant outcome, the candidate and baseline, and the workload. Name the unit being measured and the correctness conditions that make work count. Establish the available environment and budget; a benchmark is an experiment with limitations, not permission to tune every part of the system.

## Method

1. Write the claim before measuring. Specify workload, data distribution, concurrency, success criteria, resource limits, and the metric that would change a decision. Distinguish latency, throughput, capacity, memory, and cost rather than calling every favorable number “faster.”
2. Inspect what the harness actually includes. Check setup, warmup, caching, deferred work, batching, retries, errors, and output consumption. Ensure the timed region contains the claimed operation and that a shortcut cannot reduce measured work by omitting required results.
3. Make the comparison fair. Use equivalent inputs, outputs, resource budgets, and relevant configuration. Control or record background load and environmental differences. Give both implementations comparable preparation and justified tuning; avoid handicapping the baseline to favor the candidate.
4. Start with a bounded correctness pilot. If required outputs fail, preserve the failing inputs and error evidence, and diagnose the failure or propose a discriminating probe before collecting comparative timings. Correct or explain the failure before resuming; a later passing run does not erase unresolved failures. Once comparable correct work is established, repeat measurements with alternating or randomized order where practical. Retain individual results and errors, and stop according to a decision-relevant budget rather than a favorable result.
5. Analyze correctness and variability before summarizing speed. Account for successful work separately from attempted or failed work. Report appropriate central values and spread, distinguish absolute from relative changes, and avoid precision or confidence claims unsupported by the experimental design.
6. Check whether the measured result supports the original user-level claim. Identify bottlenecks, saturation, measurement overhead, and operating conditions that limit generalization. Stop with a supported conclusion or an explicit inconclusive result and the smallest follow-up experiment that addresses the decisive uncertainty.

## What to return

Return the claim, workload, candidate/baseline identities, environment and configuration, harness scope, per-run observations, correctness and failure counts, summary statistics, and limitations. Include enough detail to repeat the comparison. Separate an observed difference from a causal explanation; showing a time reduction does not by itself explain which change produced it.

## Boundaries

Do not compare different amounts of correct work as equivalent performance, hide failed runs, cherry-pick a fastest sample, or change the claim after seeing results. Use authorized isolated resources and stop at cost or load limits. When only supplied records are available, analyze those records honestly and label proposed measurements as unexecuted.

## Worked example

A document renderer returns a lazy stream immediately, while its predecessor returns a fully materialized document. Timing only the call favors the stream before rendering or storage has finished. Define the user-visible endpoint as a complete, validated document available to read, then time both implementations through that endpoint. Record peak memory separately: a streaming design may reduce memory even when end-to-end latency changes little.
