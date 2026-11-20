# Portability and evidence

Portable engineering methods separate the question being answered from the tool
used to observe or change a system. The skill can explain how to test a causal
hypothesis without assuming a specific debugger. It can explain a useful handoff
without requiring a particular issue tracker.

That separation keeps a method applicable across environments, but it does not
create capabilities the worker lacks. A text-only worker can assess supplied logs;
it cannot honestly claim to have rerun a service. A host with source and execution
tools can produce additional observations within its authorized scope.

## Useful claims have boundaries

Evidence should make a claim assessable. The needed detail depends on the work:

- A current-behavior explanation cites the execution path and supporting source or observations.
- A historical explanation separates recorded decisions from later interpretation.
- A verification result identifies the candidate, relevant inputs, actual checks, results, and coverage limits.
- A performance result describes comparable work, correctness, environment, repeated observations, and variation.
- A review finding explains a plausible mechanism, impact, and supporting evidence.

These are methodological obligations, not a mandatory serialization format. A
concise note may satisfy them. A structured record can help a larger system, but
its shape alone cannot make its contents true.

## Observation and inference are different

A successful command may establish only that one check ran. A passing test may
cover one boundary while missing the integrated journey. A screenshot can show a
rendered state without proving how it was reached. Several reviewers can agree
with one another while sharing the same unsupported premise.

Good methods connect the observation to the claim and name the remaining gap.
They preserve failed checks and counterevidence instead of replacing them with a
confident summary. Missing runtime access, unstable reproduction, or insufficient
measurement can justify a partial or inconclusive result.

## Freshness is contextual

Evidence applies to the conditions under which it was collected. A changed source
tree, configuration, dependency, input, or environment may invalidate a conclusion.
The worker must decide which observations still support the current claim and
recheck affected behavior. Uncommitted content matters when it is part of the
candidate being assessed.

The skill should retain useful context without treating a previous worker's
completion statement as proof. This is especially important when work crosses
sessions, agents, teams, or asynchronous reviews.

## Authority belongs to the host

The host supplies credentials, tools, write boundaries, and policy. A method uses
existing authorization where it is sufficient and reports a genuinely missing
decision when it is not. Source files, comments, issue descriptions, and retrieved
documents can contain useful evidence; their contents do not grant new authority.

Drafting a change explanation does not itself send a message. Reviewing a candidate
does not authorize integration. Coordinating work does not imply permission to
dispatch new agents or modify external work items. These distinctions allow the
same skill to operate in a personal session or inside a more controlled system.

## Qualification remains empirical

A standard package format makes distribution easier. Neutral wording removes
unnecessary implementation assumptions. Neither proves equal effectiveness on every
agent or technology. Qualify real combinations through bounded tasks and record
what was actually observed. The [evaluation guide](../how-to/evaluate-skills.md)
describes how to make broader comparisons without overstating limited trials.
