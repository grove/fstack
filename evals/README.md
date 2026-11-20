# Behavioral evaluations

Each skill has one task case in `cases/`. Cases are evaluator material: they
contain a realistic request, supplied records or workspace fixtures, expected
observable behavior, prohibited behavior, and the evidence needed to judge the
result. They are kept outside skill packages so installing a method does not
load its grading criteria.

## Run a case

Prepare a fresh packet from the repository root:

```sh
python tools/prepare_eval.py \
  --case fstack-measure-performance \
  --output dist/performance-trial
```

The packet contains `TASK.md`, the selected skill and license under `skill/`, and
a `workspace/` for supplied files and the result. The preparer deliberately
omits `expected`, `forbidden`, and `evidence` grading fields. It neither invokes
an agent nor executes candidate code.

Give a fresh worker only the packet, its normal host instructions, and the
capabilities explicitly allowed for the task. Keep previous answers and grader
material out of the worker context. The worker should read `TASK.md` and use
`skill/SKILL.md`, then return its observations, decisions, and limitations. Run
workspace tasks in an isolated environment appropriate for their code; packet
preparation itself is not a sandbox.

After completion, inspect the original case's criteria against the actual
response, source changes, tool trace, and retained evidence. For each criterion,
record **met**, **partially met**, **not met**, or **unresolved** and explain the
observation. A partial result must identify the unmet part and must not be counted
as a pass. Lack of evidence cannot be scored as success. Correct output alone does not establish
permission compliance, genuine execution, or a sound reasoning method.

## Compare a skill with a baseline

Use equivalent task instances, capabilities, models, budgets, and scoring. Compare
the skill against the same worker without it and, when useful, the current best
alternative. Randomize task/order effects, preserve failures, and repeat enough
trials to describe variability. Keep held-out cases separate from examples used
while editing the skill. A single successful run demonstrates a capability in
that setting; it does not establish a general improvement or universal portability.

Record skill content identity, task identity, agent/model when exposed, available
tools, scope, runtime, elapsed time/cost when observed, results, and limits. Do not
invent unavailable metadata. Never average away a violated authorization boundary
or a failed correctness requirement into an overall quality score.

## Coverage and results

`python tools/validate.py` checks that every catalog skill has a well-formed case.
`python -m unittest discover -s tests -v` checks the maintainer tools and packaging
boundaries. Neither command runs these behavioral tasks or establishes that a
skill improves outcomes.

The [initial exercises](results/initial-exercises.md) record three methods, a
retained partial result, and a subsequent regression check. Unrun cases remain
unqualified; no result should be inferred from the presence of a case file.
