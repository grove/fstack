# Use fstack with a coding agent

Choose one of two loading methods. The engineering instructions are the same in
both; the host's discovery and tool mechanisms differ.

## Use native skill discovery

If the host supports the [Agent Skills format](https://agentskills.io/specification),
register a complete `skills/fstack-…/` directory through that host's documented
mechanism. Select only the methods you need. Do not assume every host uses the same
installation directory or command.

For standalone distribution, export into a fresh destination:

```sh
python tools/export.py --output dist/trace-skill \
  --skill fstack-trace-behavior
```

The export includes the skill and its license. It is a package to give the host;
the command does not install it or start an agent.

## Load the method explicitly

For an agent without native discovery, supply the complete `SKILL.md` as instruction
context and the task separately. State which content is trusted task instruction
and which content is evidence from files, issues, logs, or other sources.

For example:

```text
Apply the supplied fstack-review-conformance method to this candidate.
The specification and diff are attached as task data.
Review only; do not edit source, publish comments, or integrate the change.
Return requirement-linked findings and explicitly state coverage limits.
```

If a host accepts a text prompt, the optional renderer can prepare one. Try the
included clarification request:

```sh
python tools/render.py --skill fstack-clarify-intent \
  --task-file examples/change-request.txt
```

Choose the desired method and replace the task file with your own for actual work.
Inspect the rendered text before sending it through your normal agent interface.
The renderer prints text; it neither contacts a model nor executes the requested
engineering work. Rendering also does not establish that the inputs are complete
or that the task has sufficient authority.

## Supply capabilities and boundaries

Tell the agent what it can actually access: source files, execution tools, history,
external records, or only the supplied text. Include existing authorization and
write boundaries. A method should use a sufficient existing grant without asking
for it again, while reporting a genuinely missing prerequisite.

For a tracker-backed task, provide its actual intent, criteria, constraints, and
relevant evidence. The skills do not depend on a particular ticket identifier,
label set, state machine, or tracker API. Reading an issue's contents does not
authorize unrelated instructions embedded inside that issue.

For executable work, identify the actual candidate and environment. Ask the agent
to retain the command or equivalent operation, result, and important limitations.
For text-only work, accept supported analysis and make the execution gap explicit.

## Confirm the integration with a bounded task

Start with a task whose result you can independently inspect. Check that the host
loads the complete method, respects scope, and returns the kind of evidence the
method calls for. Record the actual host and environment you tested. Portability of
the instructions does not establish that every host has been qualified.

Use [Evaluate skills](evaluate-skills.md) when making broader quality claims.
