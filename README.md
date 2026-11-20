# fstack

**Fundamental engineering skills for any coding agent.**

fstack contains 31 focused methods for understanding, designing, changing,
verifying, and explaining software. Each skill teaches one engineering discipline:
how to investigate a cause, define an interface, write a testable specification,
challenge a design, preserve a useful handoff, or perform another bounded task well.

Use one skill when it resolves the problem. Combine a few when the work needs
several disciplines. Each `SKILL.md` is self-contained; it does not require a
controller, another skill, a particular programming language, or an issue tracker.
Results can be ordinary engineering notes, code, tests, diagrams, or review findings.
There is no mandatory result envelope or shared execution runtime.

## Start here

- [Try one skill](docs/tutorials/first-skill.md): clarify a small feature request.
- [Choose a method](docs/how-to/choose-skills.md): distinguish nearby skills and select a useful scope.
- [Browse all 31 skills](docs/reference/catalog.md): responsibilities, groups, and package links.
- [Use your coding agent](docs/how-to/use-with-an-agent.md): native discovery or explicit instructions.
- [Compose a few methods](docs/how-to/compose-methods.md): use an optional recipe without turning every task into a full process.

The [documentation index](docs/README.md) separates tutorials, how-to guides,
reference, and explanation using [Diátaxis](https://diataxis.fr/).

## The library

| Area | Skills | Main concern |
| --- | ---: | --- |
| Understanding | 5 | Intent, current behavior, historical rationale, evidence, and assumptions. |
| Design | 7 | Domain models, specifications, interfaces, alternatives, experiments, failure modes, and increments. |
| Implementation | 5 | Feedback, diagnosis, test-first development, small changes, and safe refactoring. |
| Verification | 7 | Executed behavior, exploration, impact, conformance, design review, counterexamples, and performance. |
| Collaboration | 5 | Decisions, handoffs, ownership, feedback, and change communication. |
| Improvement | 2 | Structural lessons and measured skill effectiveness. |

Every skill states its starting point, method, useful result, boundaries, and a
worked example. Names use `fstack-<verb>-<object>` so responsibilities remain visible
when several skill libraries are installed together.

The [engineering principles](principles/engineering.md) explain common judgments.
The [recipes](recipes/README.md) show possible combinations. Both are background
material; a worker can use a skill without loading them.

## Use a skill

Give your agent the complete file and a bounded task:

```text
Use skills/fstack-trace-behavior/SKILL.md.
Explain how an incoming cancellation reaches stored order state in this project.
Read the relevant implementation and tests. Do not change source files.
Show the actual path, the evidence for it, and any unresolved branches.
```

If the agent supports the [Agent Skills format](https://agentskills.io/specification),
register the complete skill directory using that host's documented mechanism.
Otherwise, load the file explicitly. The host supplies access, tools, scope, and
authority. A skill supplies a method; it does not create unavailable capabilities
or permission to publish, integrate, or deploy work.

## Maintain and export

The optional maintainer tools use Python 3.11 or newer and its standard library.
They do not constrain the technology used by a target project.

```sh
python tools/validate.py
python -m unittest discover -s tests -v
python tools/export.py --output dist/skills
```

An export contains each selected `SKILL.md` and the repository license. The
exporter does not install skills or call a coding agent. See the
[package and tooling reference](docs/reference/packages-and-tools.md).

The [evaluation guidance](docs/how-to/evaluate-skills.md) distinguishes package
checks from observed engineering performance. The included cases provide a basis
for evaluation; qualification applies only to the tasks and environments actually
exercised. See [evaluation material](evals/README.md) for recorded scope and results.

## Contribute

Use the [contribution guide](CONTRIBUTING.md) to improve an existing method or
propose a distinct responsibility with a discriminating evaluation case.

## License

[Apache License 2.0](LICENSE).
