# Packages and maintainer tools

## Skill package

The initial package layout is:

```text
fstack-example-method/
  SKILL.md
```

The complete method is in `SKILL.md`. Exported packages also contain `LICENSE`.
No neighboring skill, root documentation file, runtime contract, or result schema
is required to use a method.

The file follows the [Agent Skills format](https://agentskills.io/specification):
YAML frontmatter followed by Markdown instructions. fstack uses a deliberately
narrow metadata convention:

| Field | fstack convention |
| --- | --- |
| `name` | `fstack-<verb>-<object>`; matches its directory; lowercase letters, digits, and single separating hyphens; at most 64 characters. |
| `description` | A nonempty, JSON-quoted, single-line scalar describing the responsibility and triggering situations; at most 1,024 characters. |

The required sections are **Starting point**, **Method**, **What to return**,
**Boundaries**, and **Worked example**. The repository keeps each entry point below
500 lines. Standard format compatibility concerns the package shape; host behavior
and available capabilities still require integration testing.

## Catalog

[`catalog.json`](../../catalog.json) contains a repository version and a `skills`
array. Each entry has `name`, `group`, and `purpose`. The name determines the package
location under `skills/`. Groups are `understanding`, `design`, `implementation`,
`verification`, `collaboration`, and `improvement`.

The catalog is an index for maintainers and discovery. It is not a controller, tool
permission manifest, result contract, or execution order.

## Evaluation case

One case under `evals/cases/` corresponds to each catalog skill. Case content uses:

| Field | Meaning |
| --- | --- |
| `id` | Case identity, matching the skill name for the initial corpus. |
| `skill` | The method exercised by the case. |
| `task` | The bounded request given to a fresh worker. |
| `context` | Raw observations, snippets, constraints, and access limitations needed for the task. |
| `expected` | Observable result or behavior properties for the evaluator. |
| `forbidden` | Incorrect claims, shortcuts, or side effects for the evaluator to detect. |
| `evidence` | What the evaluator should inspect to decide the result. |
| `mode` | `reasoning` for supplied-record tasks or `workspace` for tasks using materialized files. |
| `fixtures` | Optional workspace files, each with a relative `path` and text `content`. |

The grader fields `expected`, `forbidden`, and `evidence` must remain outside the
worker prompt. A case's presence does not mean that any agent has run or passed it.

## Tool requirements

The optional tools require Python 3.11 or newer and its standard library. Run the
commands from the repository root. No dependency installation is needed for these
utilities, and Python is not required by the engineering methods themselves.

Successful commands exit with status `0`. Validation and handled file or content
errors exit nonzero, normally `1`; command-line argument errors use `2`. Commands
print readable results or diagnostics, not a shared execution-status schema.

### Validate the repository

```sh
python tools/validate.py
```

Checks the properties implemented by the validator, including package metadata,
naming, catalog and case coverage, resource containment, documentation links, and
unfinished templates. A failure should be corrected at its cause. Do not weaken a
check solely to accept inconsistent content.

Validation is structural. It cannot establish that an arbitrary engineering
conclusion is true or that a skill improves performance across agents.

### Export independent packages

```sh
python tools/export.py --output dist/all-skills
python tools/export.py --output dist/one-skill \
  --skill fstack-model-domain
```

Omit `--skill` to export the catalog, or repeat it to select several distinct
skills. The destination must be absent or empty. Source and metadata destinations,
symbolic links, and unsafe resource paths are rejected. Each exported package
contains its complete instruction file, any local package resources, and a copy
of the repository license. The command does not install packages or invoke an
agent.

### Render an explicit invocation

```sh
python tools/render.py --skill fstack-clarify-intent \
  --task-file examples/change-request.txt
```

Prints the complete selected method and supplied task to standard output. The
included example asks for clarification of a display-name confirmation feature.
Replace the task-file path with your own text for other work. Rendering does not
write files, execute the task, contact a model, or establish authorization. The
agent must still distinguish task data from instructions that legitimately govern
its work.

### Prepare an evaluation task

```sh
python tools/prepare_eval.py --case fstack-model-domain --output dist/domain-trial
```

Creates a packet in an absent or empty destination:

| Path | Contents |
| --- | --- |
| `TASK.md` | Worker instructions, raw task, supplied context, and workspace guidance. |
| `skill/SKILL.md` | The complete selected method. |
| `skill/LICENSE` | The repository license. |
| `workspace/` | Declared fixture files, or an empty-workspace marker when there are no fixtures. |

Any additional package resources are copied under `skill/`. The packet excludes
the evaluator's `expected`, `forbidden`, and `evidence` fields. Its instructions
ask a worker with file-writing access to place its result in `workspace/result.md`;
the preparation command does not create that result. This is an evaluation
convenience, not a required skill-output format.

The command does not run an agent, test candidate code, or calculate a quality
score. Use a fresh destination for each trial and inspect the prepared files
before assigning it. Preparation is not an access-control sandbox: the evaluator
must separately prevent a worker from reading grader material if that separation
is required by the trial.

### Run tooling regression tests

```sh
python -m unittest discover -s tests -v
```

The tests cover the implemented tooling and packaging boundaries. Behavioral skill
evaluation is separate; see [Evaluate skills](../how-to/evaluate-skills.md).
