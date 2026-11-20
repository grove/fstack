# Assessment of the proposed performance claim

## Decision now

**The supplied results do not support replacing the baseline.** The required operation produces one valid output for each of 5,000 inputs, with no dropped outputs. Every candidate run produced only 4,000 valid outputs and 1,000 errors. It therefore failed the required operation in all three observations.

The defensible timing statement is: **“For 5,000 attempts, the candidate's observed mean elapsed time was 70 seconds versus 100 seconds for the baseline, a 30% reduction, while its observed valid-output completion rate was 80% versus 100%.”** This is a comparison of the recorded attempted batches, not a demonstrated reduction in the time needed to complete the required batch correctly. The candidate's time to deliver all 5,000 valid outputs is unmeasured.

No additional measurement is needed to reject the current claim of readiness. A next experiment is useful only to determine whether the candidate can complete equivalent correct work and, if it can, what that completion costs.

## Question, workload, and evidence

The proposal is: “The candidate is 30% faster and ready to replace the baseline.” For this task, the decision metric should be **elapsed seconds to make all 5,000 required valid outputs available**, under equivalent operating conditions. Correctness is a prerequisite: each input must have its corresponding valid output. Attempt throughput and the rate of producing a partial set of valid outputs cannot substitute for that requirement.

The implementations are identified only as “baseline” and “candidate.” The available environment is one machine. All three baseline runs preceded all three candidate runs; background load was unrecorded. The timed intervals include all attempts and exclude setup. No versions, input contents or distributions, concurrency settings, resource budgets, warmup policy, cache state, recovery policy, or detailed timing endpoints are supplied. No runtime is provided, and this assessment uses only the supplied records.

### Individual observations

| Recorded order | Implementation | Elapsed seconds | Attempts | Valid outputs | Errors | Valid outputs / inputs |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Baseline | 99 | 5,000 | 5,000 | 0 | 100% |
| 2 | Baseline | 100 | 5,000 | 5,000 | 0 | 100% |
| 3 | Baseline | 101 | 5,000 | 5,000 | 0 | 100% |
| 4 | Candidate | 69 | 5,000 | 4,000 | 1,000 | 80% |
| 5 | Candidate | 70 | 5,000 | 4,000 | 1,000 | 80% |
| 6 | Candidate | 71 | 5,000 | 4,000 | 1,000 | 80% |

### Summary of the recorded batches

| Quantity | Baseline | Candidate |
|---|---:|---:|
| Number of runs | 3 | 3 |
| Mean elapsed seconds | 100 | 70 |
| Median elapsed seconds | 100 | 70 |
| Observed time range, seconds | 99–101 | 69–71 |
| Sample standard deviation, seconds | 1 | 1 |
| Total timed seconds | 300 | 210 |
| Total attempts | 15,000 | 15,000 |
| Total valid outputs | 15,000 | 12,000 |
| Total errors | 0 | 3,000 |
| Observed error fraction | 0% | 20% |
| Pooled attempts per timed second | 50.0 | 71.4 |
| Pooled valid outputs per timed second | 50.0 | 57.1 |
| Runs satisfying the required output count and validity | 3 of 3 | 0 of 3 |

The sample means differ by 30 seconds. The relative reduction is `(100 − 70) / 100 = 30%`. If “faster” means attempted throughput, its reciprocal calculation is `100 / 70 − 1 ≈ 42.9%`; these are different metrics, so the claim should name its metric explicitly.

The pooled valid-output rates are `15,000 / 300 = 50.0` and `12,000 / 210 ≈ 57.1` outputs per second. Their approximately 14.3% difference is a descriptive rate for the observed mixture of successes and failures. It does **not** establish a 14.3% speedup for the required operation. The missing outputs may have different costs, and failures may terminate work early. Neither possibility is established by these records. Extrapolating from 4,000 successes to the cost of completing 5,000, or assuming retries will repair the batch at the same rate, would be unsupported.

## Limits of the conclusion

1. **The candidate does not perform equivalent correct work.** Equal attempt counts do not establish equivalence when 20% of its required outputs are absent. The record contains no successful full candidate batch or measured recovery cost.
2. **Implementation and run order are confounded.** The observed timing difference could include changes in background load, machine state, warmup, or caches. These are possible explanations, not observed causes. The records do not isolate the effect of the candidate implementation.
3. **The workload and harness are incompletely specified.** The records do not establish that both implementations received identical inputs or configuration. Including all attempts is useful, but does not establish whether all output consumption, validation, or recovery needed for the promised endpoint was included. Setup exclusion also limits any claim about startup-inclusive latency.
4. **There are only three observations per implementation on one machine.** The narrow observed ranges describe these samples. They do not establish stable performance in other conditions, independence of observations, a trustworthy confidence interval, or general reliability. Zero observed baseline errors is not proof that the baseline can never fail.
5. **No other performance dimension was measured.** There is no evidence about memory, cost, saturation, capacity, other workloads, or a causal bottleneck.

## Smallest decisive next experiment — proposed, not executed

### Define the claim and correctness gate first

Predeclare the local question as: **“With the same 5,000 inputs and resource budget, can the candidate deliver every required valid output, and does its time to that endpoint meet a specified elapsed-time target?”** If the intended target is a 30% time reduction, the target ratio is `candidate completion time / baseline completion time ≤ 0.70`.

Use the unchanged candidate and baseline. If an existing production recovery policy is part of the claimed operation, document it and include its retries or fallback work in the timed endpoint. No such policy is present in the supplied evidence; do not assume one exists or add unmeasured recovery to the claim. If the unchanged candidate cannot complete the workload, further performance measurements do not rescue its readiness.

### Minimal first stage: one candidate completion trial

Run one fixed, representative batch of 5,000 inputs through the candidate under documented conditions. Prefer the exact supplied workload if it can be recovered; otherwise identify the new input set explicitly and limit the conclusion to that set. Retain input identities and independently validate that every input has one corresponding valid final output. Reject missing, duplicate-substituted, or invalid outputs.

Start timing at a documented boundary after the agreed setup and finish only when the complete required output set is available, including any existing required recovery. Record failures as failures, with their elapsed time and missing-output counts. Predeclare the operational timeout or resource ceiling; do not run indefinitely to obtain a success or discard a failed run.

**If any required output is still missing or invalid, stop.** That single failed completion trial is decisive against readiness on that workload. Because failure is the current decisive issue, no baseline timing run or larger timing study is needed in this branch. Passing this gate would be evidence of one complete candidate batch, not proof of general reliability or of a 30% reduction.

### Conditional timing stage, only after correctness passes

Use a small, predeclared pilot of **two matched pairs**, one baseline-then-candidate pair and one candidate-then-baseline pair. Randomize which pair occurs first. This is a minimal counterbalanced repeated comparison; it is a pilot, not a claim that four timings establish general performance.

For each run, replay the same immutable input batch with the same concurrency, resource limits, and relevant configuration. Give both implementations comparable setup and warmup. Define and reset cache and output state consistently, or explicitly study an equal warmed state. Isolate background work where practical and record machine load and relevant conditions. Use the same complete-output timing endpoint and validation gate for both implementations. Retain every individual time, output count, error count, recovery count, and timeout; stop the readiness assessment on a correctness failure.

For valid completed pairs, report the completion times, paired time ratios, and their spread. A ratio above 0.70 misses the stated 30% target in that pair; a ratio at or above 1.00 fails to improve completion time in that pair. Passing the target in both pairs supports a narrow statement about those observed conditions. It does not by itself justify replacement or a precise general speed claim.

If the pilot leaves uncertainty that could change the decision, use its variability to design a bounded follow-up with a predeclared sample size and analysis criterion, or a valid predeclared sequential stopping rule. Do not stop simply when a favorable result appears. The supplied failed candidate runs cannot determine how many successful full-batch observations would be sufficient: their endpoint is different, and variance for correct completion is unknown.

This staged design spends the minimum new work on the decisive correctness uncertainty, then measures equivalent completed work only if that uncertainty is resolved. It does not promise that any fixed tiny sample can establish broad replacement readiness.

## Execution status and sources

This report is an analysis and experiment design only. No new measurements were run, no implementation was edited, and no external information was used. All observations come from the supplied records in `TASK.md`; the method follows `skill/SKILL.md`. Arithmetic is derived from those records. The exact original benchmark cannot be reproduced from the packet alone because the executable implementations, input data, detailed configuration, and runtime are not supplied.
