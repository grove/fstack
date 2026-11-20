# Contributing to fstack

Improve an engineering method because an observed task exposes a gap. Start with
the raw task, relevant output, and the consequence of the failure. Explain which
part of the method needs to change and how a representative case would distinguish
the improved behavior.

## Preserve the product boundary

A skill must remain useful on its own. Keep its complete method in `SKILL.md` and
avoid requiring another skill, a controller, a repository-wide protocol, a result
schema, or a specific agent, model, language, tracker, or service. Host capabilities
may limit what can actually be performed; the skill must report that boundary
honestly.

Shared principles belong in [principles/engineering.md](principles/engineering.md).
Optional task compositions belong in [recipes/](recipes/README.md). Do not create
a new callable skill for every principle, file format, or sequence of existing
responsibilities.

## Change a skill

1. State the engineering responsibility and the actual failure being corrected.
2. Read the current skill and its evaluation case. Identify the smallest method
   change that addresses the failure without adding unrelated process.
3. Edit the skill in its existing directory. Use the repository's canonical
   frontmatter: `name` and a JSON-quoted, single-line `description`.
4. Keep the five sections: **Starting point**, **Method**, **What to return**,
   **Boundaries**, and **Worked example**. Teach concrete judgment and observations;
   do not substitute a long checklist of virtues.
5. Update the corresponding case under `evals/cases/` when the changed behavior
   affects its grading criteria. Keep task data separate from evaluator-only
   expectations. A case must challenge the method, not ask an agent to recite it.
6. Run the repository checks. Where a behavioral claim is at stake, run a bounded
   fresh-agent exercise and retain actual outputs and limitations.
7. Explain the problem, change, result, and validation in the pull request.

Use existing authorization without demanding repeated approval. Instructions must
not silently enlarge write scope, reinterpret external text as authority, invent
evidence, or treat an unavailable check as success. Analytical methods should
produce findings or drafts; external effects need applicable host authorization.

## Propose a new skill

Show why an existing skill or optional composition cannot cover the responsibility
without becoming ambiguous. Describe its starting information, repeatable method,
distinct useful result, stopping rule, and a realistic test case. Update
`catalog.json` and the [catalog documentation](docs/reference/catalog.md) together.

Names use `fstack-<verb>-<object>` with lowercase letters, digits, and separating
hyphens, up to 64 characters. Keep the `SKILL.md` under 500 lines; the usual method should be much
shorter. Additional resources are justified only when the method truly needs them,
must stay inside the skill package, and must be handled by validation and export.

## Validate

Run from the repository root:

```sh
python tools/validate.py
python -m unittest discover -s tests -v
python tools/export.py --output dist/contribution-check
```

Use a fresh export destination. Passing these checks establishes the properties
they inspect, not the truth of every engineering conclusion an agent might later
produce. Report the agent environment, task, permission scope, actual checks, and
failures for any behavioral exercise. Do not erase a failed trial after revising a
skill; record the revision and rerun as a separate observation.

## Write documentation for its purpose

- Tutorials guide a learner through one small, successful experience.
- How-to guides solve a stated practical problem for someone who knows the basics.
- Reference describes names, fields, commands, and boundaries precisely.
- Explanation develops the reasoning behind the design.

Keep instructions originally written and maintain applicable license notices.
Keep reusable methods independent of particular tools and services.
