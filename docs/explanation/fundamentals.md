# Fundamentals, principles, and recipes

A fundamental skill teaches a repeatable engineering method with a useful result.
Its starting point can come from a person, a project, or another method. It remains
useful when the task, technology, agent, or tracker changes because its core judgment
does not depend on one particular implementation mechanism.

For example, causal diagnosis distinguishes competing explanations with controlled
observations. The observation might come from a small program, an event trace, a
device, or a service. The tools differ, but changing one factor and checking its
predicted consequence remains a meaningful engineering method.

## Three kinds of knowledge

| Kind | What it provides | Example |
| --- | --- | --- |
| Principle | A judgment that should influence relevant work. | Expected test results should have an independent basis. |
| Skill | A method for performing one engineering responsibility. | Develop one behavior through a discriminating failing case and a minimal correction. |
| Recipe | A possible composition for a broader task. | Diagnose a defect, correct it, verify behavior, and explain the result. |

These categories prevent two kinds of inflation. Turning every principle into a
skill creates commands with little work to do. Putting every activity in a single
skill makes it difficult to choose scope, preserve context, or assess completion.

Some methods apply a principle in enough detail to deserve their own entry point.
Making a small change, for instance, involves locating the behavior boundary,
preserving unrelated state, choosing a coherent delta, and checking consequences.
“Keep changes small” alone would not teach that method.

## Independence is about use

Independent skills can share ideas and terminology. Independence means a worker
can use a complete skill with supplied task context without needing to run another
skill first or recover an undocumented result format. A user can provide a clear
specification directly. A project can already have suitable tests. The method uses
what is adequate and identifies what is missing.

Composition is still valuable. A domain model can clarify a specification; a
specification can guide tests; executed observations can inform review. The handoff
should carry the relevant information and its limits. It does not need a universal
envelope to be useful.

## Boundaries keep methods distinct

The catalog deliberately separates questions that can otherwise become confused.
An intent discussion is different from a testable specification. Current behavior
does not establish why it was originally chosen. Requirement conformance and design
quality can produce different judgments about the same candidate. A fast feedback
signal may guide development while remaining insufficient for a final verification
claim.

The distinction is practical: a worker should know what it is trying to establish
and when the result is enough. Additional methods should answer a remaining question,
not merely lengthen the process.

## Recipes belong to the task

Feature development, refactoring, incident response, and release work can all use
fundamental methods. Their full processes also involve team policy, specialist
knowledge, environments, and authorized external actions. fstack's optional recipes
show where several methods can help while leaving those surrounding responsibilities
with the host and project.

This repository therefore remains a discipline library. It has no runtime dependency
on another project, no implicit orchestration layer, and no requirement to exercise
all 31 skills for a complete piece of work.
