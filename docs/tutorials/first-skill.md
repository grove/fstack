# Use your first skill

In this tutorial, you will use one skill to clarify a small software request. You
need an agent that can read supplied text. No repository checkout, issue tracker, command
execution, or installation is needed for this exercise.

By the end, you will have a short outcome brief with a measurable success condition,
explicit scope, and a clear boundary for the next design task.

## 1. Read the skill

Open [fstack-clarify-intent](../../skills/fstack-clarify-intent/SKILL.md). Notice its
starting point, method, expected result, boundaries, and worked example. The whole
method is in this file.

If your agent can read repository files, give it that path. If it cannot, paste the
complete file into its context. Use the same content in either case.

## 2. Give the agent this request

Copy the following request after the skill:

```text
Use the supplied fstack-clarify-intent skill.

We maintain a scheduling application. Support says people frequently cannot find
meetings they cancelled last week. Someone suggested adding a global search bar.

For this exercise, the affected users are support staff looking up their own
organization's records. They need the meeting date, its title, and who cancelled it.
They do this a few times a day. We are willing to change the support interface but
not the customer interface in this increment. We have not decided how far back the
lookup must go. Existing access restrictions must remain in force.

Help me clarify the intended outcome. Ask only questions whose answers would
change scope or acceptance. Do not design or implement the solution, inspect an
external system, or publish anything. Use only the information supplied here.
```

The proposed search bar is a candidate solution. The task is to understand what
people need to accomplish and how completion could be recognized.

## 3. Answer the consequential question

The agent may ask about the lookup period or another material gap. Supply this
clarification when it is relevant:

```text
Support needs cancelled meetings from the previous 30 days. A support staff member
should find a known cancelled meeting within one minute using its approximate date
and title. Records from other organizations must remain inaccessible. A search bar
is optional; choose a solution later.
```

If the agent asks for information already supplied, point to it. If it asks about
visual styling, search infrastructure, or a particular framework, bring it back to
the intended outcome. Those decisions are outside this exercise.

## 4. Inspect the result

Ask for the skill's stated result in a concise form. Check that the brief:

- Names support staff and the lookup problem they are trying to solve.
- Specifies the 30-day period and the information needed from a meeting.
- Uses the one-minute lookup target as an acceptance condition.
- Preserves organization access restrictions and the customer-interface exclusion.
- Treats the search bar as an option, without claiming a design has been chosen.

These are properties to inspect, not a required JSON schema. A short structured
note is sufficient. The result should distinguish supplied facts from decisions
that still need later work.

## 5. Stop at the useful boundary

Save the brief wherever your team keeps task context. You have completed an intent
clarification exercise. You have not demonstrated the usability target, implemented
access controls, or verified a deployed application.

The brief can now be supplied to a designer, engineer, or another method such as
`fstack-write-specification`. That is a separate task choice. For guidance on
joining methods, see [Compose methods](../how-to/compose-methods.md).
