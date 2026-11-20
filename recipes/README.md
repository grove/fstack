# Optional recipes

Recipes describe ways to combine a few independent methods for a bounded task.
They are human-readable suggestions, not executable workflows or required context
for a skill. Select the steps that address an actual uncertainty or responsibility;
an existing result can satisfy an input without rerunning the method that might
have produced it.

| Task | Recipe | Typical reason to use it |
| --- | --- | --- |
| Add behavior | [Deliver a small feature](feature.md) | Turn an outcome into an implemented, demonstrated increment. |
| Correct behavior | [Resolve a defect](defect.md) | Establish the cause and verify a focused correction. |
| Improve structure | [Refactor a bounded area](refactor.md) | Change implementation structure while preserving explicit contracts. |
| Make a choice | [Resolve a design decision](design-decision.md) | Compare viable approaches and preserve the reason for the choice. |
| Transfer work | [Prepare a reliable handoff](handoff.md) | Give another worker enough current context to continue accurately. |

The host still owns scheduling, tool access, issue tracking, permissions, and
publication. If a team implements automation around these recipes, it must define
those responsibilities and evaluate the resulting integration separately.

Read [Compose methods](../docs/how-to/compose-methods.md) for handoff and stopping
rules, or [Choose skills](../docs/how-to/choose-skills.md) for nearby responsibilities.
