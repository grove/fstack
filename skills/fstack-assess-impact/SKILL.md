---
name: fstack-assess-impact
description: "Trace the consequences of a proposed change beyond its edited files. Use when assessing compatibility, consumers, lifecycle, persisted data, or rollout safety before implementation or release."
---

# Assess impact

## Starting point

Start with the exact change, the behavior or contract it alters, and the comparison baseline. Gather reachable consumers and operating context. Record the access available: a repository can reveal internal callers while leaving installed clients, stored data, scheduled work, or externally owned integrations unknown.

## Method

1. Describe the changed observable contract, including representation, timing, ordering, identity, errors, resource use, and persistence when relevant. Separate a purely internal substitution from a change that callers or previously written data can observe.
2. Trace direct producers and consumers, then cross boundaries that simple reference search misses. Consider serialized fields, generated clients, dynamic dispatch, scripts, queues, scheduled jobs, configuration, versioned protocols, caches, and separately deployed components.
3. Follow the change across time. Ask what happens to existing records, in-flight operations, old binaries, rolling deployments, delayed messages, and rollback. A current producer and current consumer agreeing does not prove mixed-version or replay compatibility.
4. Form a small set of consequential impact hypotheses. For each, identify the required condition, affected party, failure mechanism, and evidence that would confirm or clear it. Prioritize credible safety facts over an unranked inventory of everything the system contains.
5. Check the strongest available evidence. Inspect actual versions, formats, and call paths; execute a scoped compatibility or lifecycle experiment when authorized and useful. Distinguish a found caller from an exercised consumer and a plausible risk from an observed break.
6. State the remaining conditions for a safe change. Recommend the smallest justified compatibility bridge, rollout check, migration, or follow-up investigation. Stop when material claims are evidenced or explicitly bounded; do not interpret missing access or a search with no matches as proof of absence.

## What to return

Return the altered contracts, affected boundaries and versions, confirmed impacts, cleared hypotheses with evidence, and unresolved risks. Identify the one or two facts that determine whether the proposed rollout is safe. Include evidence locations and a concrete next observation for each important unknown, with ownership when it is known.

## Boundaries

This assessment does not authorize broad edits, data migration, rollout, or contacting external owners. Preserve user-defined scope and confidentiality. Avoid both false reassurance and invented catastrophe: each material risk needs a plausible mechanism and stated assumptions. A static assessment must not claim that unobserved production behavior was tested.

## Worked example

A catalog switches from byte ordering to case-insensitive ordering without changing its response fields. Trace cursors, page boundaries, cached result sets, and exports that assume the old order. A cursor issued before the change may resume at a different position afterward. Identify whether cursors encode ordering semantics, then choose evidence and a transition strategy appropriate to their lifetime rather than treating an unchanged response shape as compatibility proof.
