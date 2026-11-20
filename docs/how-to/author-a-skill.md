# Add or improve a fundamental skill

Use this guide when an engineering task exposes a gap in an existing method or a
responsibility that deserves an independent method. For contribution requirements,
see [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Establish a distinct responsibility

Describe the starting information, repeatable reasoning or action, useful result,
and condition for stopping. Ask whether the result is meaningfully different from
an existing skill's result. If a combination of current methods already covers the
task, document a recipe. If the idea is a general preference such as reducing
unnecessary complexity, improve a principle or the relevant methods.

A useful new skill should work on more than one technology or team process. A
specific project can supply its own details without the method prescribing a
framework, model, tracker, directory layout, or production service.

## Write the entry point

Create `skills/fstack-<verb>-<object>/SKILL.md`. Use this frontmatter shape:

```yaml
---
name: fstack-example-method
description: "Describe what this method does and the concrete situations that should trigger it."
---
```

The description is a JSON-quoted scalar, which is also valid YAML. The repository
uses this narrow convention so its standard-library validator can parse metadata
without a YAML dependency. The name must match the directory and contain at most
64 characters.

Write the five sections in order:

1. **Starting point:** what the worker should know or inspect before proceeding.
2. **Method:** a compact repeatable procedure, including important decisions and
   observations that distinguish plausible explanations or outcomes.
3. **What to return:** a concrete useful result and the evidence or limitations that
   make it assessable by another person or worker.
4. **Boundaries:** when to stop, what cannot be concluded, and which actions are
   outside the responsibility or granted scope.
5. **Worked example:** a specific case illustrating the method's judgment, rather
   than merely repeating its name.

Use imperative instructions and familiar language. Explain the differences that
matter: a useful observation versus a misleading proxy, a historical fact versus
an inferred motive, or a behavior change versus a refactor. Keep the method under
500 lines and usually far shorter. Avoid padding every skill with the same generic
quality checklist.

## Preserve independent use

Put the complete method in its own `SKILL.md`. Optional complementary methods can
be named in ordinary text, but they must not become required calls. A skill should
accept information supplied directly by a user or project; it should not require a
particular predecessor to manufacture that information.

If a future change genuinely needs another local resource, keep it inside the
package and update validation and export to handle it before relying on it. The
initial library uses no such additional resources.

## Write a discriminating case

Add `evals/cases/<skill-name>.json` using the fields in the
[reference](../reference/packages-and-tools.md). Give the worker raw task data and
plausible ambiguity. Keep expected behavior and forbidden shortcuts in evaluator
fields, outside the worker's prompt. Include an observable condition that can fail.

For example, a historical-rationale case could provide a commit explanation and a
later operational constraint that contradicts the current narrative. The evaluator
can then inspect whether the result distinguishes documented facts from inference.
A task that simply asks “explain how to research history” does not test that ability.

## Integrate and check

Update `catalog.json`, the [catalog reference](../reference/catalog.md), and any
affected composition example. Run the validator and tests, export the package to a
fresh directory, and inspect it without relying on neighboring files. For a claimed
behavioral improvement, perform an appropriately bounded evaluation and preserve
the actual result, including failed or inconclusive dimensions.
