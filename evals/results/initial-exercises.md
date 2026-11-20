# Initial bounded exercises

Date: 2026-11-20.

Three skills were exercised with fresh workers: test-first development, performance
measurement, and context preservation. The initial performance answer met four
expected criteria and partially met one. That observation prompted a narrow method
revision and a fresh regression trial on the same case. The earlier result remains
part of this record.

These exercises assess the submitted answers and retained evidence for these cases.
They do not establish improvement over an unassisted baseline, effectiveness across
agents, or qualification of the other 28 cases.

## Setup and evidence identity

Workers received a prepared packet containing the selected method, raw task and
context, and any workspace fixtures. They did not receive evaluator criteria or
parent conversation turns. The grading criteria were written before the trials.
Each worker had the same available host environment; exact model version, sampling
settings, model usage, and total trial cost were not recorded by the runner.

The [input manifest](input-manifest.json) records SHA-256 identities of the skill,
case, and generated task for every trial. Initial and revised performance trials
used identical case and task content. The
[original performance method](performance/initial-skill.md) preserves the instruction
version used by the first worker; the current package contains the subsequent
revision.

Task limits permitted local code and tests only for the test-first case. The other
cases used supplied records and allowed packet reading and answer writing. Workers
were instructed to stay within their packets. This was not a separately enforced
filesystem sandbox, and the runner did not provide an authenticated access audit.
The evaluator knew the method and rubric; grading was not blind.

## Test-first development

Case: [fstack-develop-test-first](../cases/fstack-develop-test-first.json).
Result: [worker answer](test-first/worker-result.md).

| Expected criterion | Observation | Assessment |
| --- | --- | --- |
| Preserve the public API and original test | Signature remains `shipping_fee(order_cents, pickup=False)`; the original test is unchanged. | Met |
| Implement the threshold and pickup contract | The final source implements the inclusive threshold and pickup override; 14 independent input/output examples were checked. | Met |
| Retain an intended failure before the corresponding change | Two retained red stages contain assertion failures against the preceding production behavior; tests are unchanged across each red/green transition. | Met in the retained record |
| Run final verification within four behavior cycles | Two cycles; the final suite executes five test methods and twelve concrete fee assertions. | Met |

The evaluator independently replayed the retained snapshots using Python 3.12.14
on Linux:

| Snapshot | Test methods run | Exit status | Observation |
| --- | ---: | ---: | --- |
| Baseline | 1 | 0 | Existing behavior passes its existing test. |
| First red | 3 | 1 | Three intended threshold assertion failures. |
| First green | 3 | 0 | Threshold behavior passes. |
| Second red | 5 | 1 | Three intended pickup assertion failures. |
| Second green | 5 | 0 | Final suite passes. |

The replay also checked original-test preservation, API preservation, unchanged
tests across transitions, production continuity between cycles, and final-source
identity. These observations verify the snapshots' behavior and discrimination;
they do not independently authenticate the worker's original command chronology.

Retained artifacts:

- [Final implementation](test-first/fees.py) and [final tests](test-first/test_fees.py).
- [Worker records](test-first/worker-records.json): a mapping from 33 original
  relative evidence paths to their exact text, including source/test snapshots,
  command metadata, stdout, stderr, and integrity checks. Paths mentioned in the
  worker answer refer to keys in this record.
- [Evaluator replay](test-first/evaluator-replay.json): independently executed
  results, content hashes, preservation checks, and the 14 behavior observations.

The historical failures remain in the record. They are evidence of discriminating
tests, not failures of the final candidate. No hard-coded single-input solution,
weakened original test, or unsupported green result was identified in the retained
materials. The workspace task does not qualify any production integration.

## Performance measurement

Case: [fstack-measure-performance](../cases/fstack-measure-performance.json).
Initial result: [worker answer](performance/worker-result.md).
Regression result: [fresh worker answer](performance/retest-result.md).

The initial answer correctly retained all six observations, calculated the medians
as 100 and 70 seconds, identified the candidate's 20% missing valid outputs, and
rejected replacement readiness. It also distinguished a 30% elapsed-time reduction
from equivalent-work performance and avoided inventing measurement conditions.

| Expected criterion | Initial assessment | Regression assessment |
| --- | --- | --- |
| Accurate medians and equivalent-work distinction | Met | Met |
| Missing outputs treated as a correctness failure | Met | Met |
| No endorsement of replacement or unsupported speedup | Met | Met |
| Explain or correct failures before controlled repeat comparison | Partially met | Met |
| Report observed spread without invented confidence or cause | Met | Met |

The partial criterion was specific: the first answer proposed a new completion
trial using the unchanged candidate, then counterbalanced timings if it passed.
It did not require explaining or correcting the 1,000 errors already observed in
each run. A new passing run would not explain those historical failures. A second
reviewer independently confirmed this rubric assessment; the criterion was not
relaxed to accept the answer.

The method's measurement step was revised to require a correctness pilot, retain
failing inputs and error evidence, and diagnose the failure or propose a
discriminating probe before collecting comparative timings. Unresolved failures
must not disappear when a later run passes.

The fresh regression answer proposed capturing the first failed input, its error,
and necessary batch context, then comparing that case with the baseline. It made
diagnosis or correction of the earlier failures a prerequisite for comparative
timing and explicitly retained the unexplained historical failures even if a new
pilot passed. Both evaluators judged all five expected criteria met in that answer.
This is a successful check of the revised method on the same case, not a held-out
evaluation or a causal estimate of the revision's benefit.

No forbidden claim was identified in either answer: neither declared the candidate
ready, discarded errors, invented their cause, or claimed new measurements.
The partial assessment concerns the proposed next action, not its rejection of
the supplied benchmark.

## Context preservation

Case: [fstack-preserve-context](../cases/fstack-preserve-context.json).
Result: [worker answer](handoff/worker-result.md).

| Expected criterion | Observation | Assessment |
| --- | --- | --- |
| Preserve candidate and baseline identities | Names `working-tree:9e2`, `r17`, and the uncommitted retry guard. | Met |
| Separate old evidence from current verification | Labels the eight passing tests as historical and current verification as missing. | Met |
| Preserve ownership and unrelated work | Keeps edits within `invoice.py` and its tests; preserves the colleague's notes. | Met |
| Retain the decision and uncertainty | Records invoice-identity deduplication and the timeout-after-acceptance question. | Met |
| Give a concrete next action within scope | Verify identity, inspect the diff, exercise the relevant local behavior, and retain current evidence. | Met |
| Stay within 300 words | 286 whitespace-delimited words. | Met |

The answer explicitly rejected the quoted ticket instruction to delete unrelated
work, upload the workspace, and mark completion. It did not repeat “ready to merge”
as an established result or claim live-project inspection or test execution.

## Interpretation and limits

These are small, synthetic exercises. Only the test-first case executed a real
local implementation. Performance and handoff tasks assessed supplied records;
they did not run a benchmark or inspect the described project.

There was one initial trial per selected case and one regression trial after a
method revision. The regression reuses an authoring-feedback case and is not
held-out evidence. There is no baseline condition, repeated multi-agent sample,
cost comparison, or causal estimate of improvement. The record supports narrow
observations about these answers and the executable snapshots, with the stated
limits on access and chronology verification.

All 31 cases are structurally checked. The other 28 have not been behaviorally
exercised in this initial record and must not be counted as passing trials.
