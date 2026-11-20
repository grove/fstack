---
name: fstack-coordinate-work
description: "Define ownership and integration for work shared across people or agents. Use when tasks can overlap, depend on shared interfaces, or require reliable parallel handoffs."
---

# Coordinate work

## Starting point

Start with the intended outcome, bounded work items, dependencies, available workers or roles, and the shared resources they may affect. Determine whether coordination is worth its overhead. Two independent analyses may benefit from parallel work; two edits to the same mutable state require an explicit ownership and integration decision.

## Method

1. Separate unresolved decisions from executable tasks. A worker cannot independently implement an interface whose behavior is still being negotiated. Identify the prerequisite decision or contract and the evidence that will make dependent work ready.
2. Create a small dependency graph based on real prerequisites. For each task, specify scope, inputs, expected result, completion evidence, and exclusions. Distinguish an ordering preference from a requirement so coordination does not unnecessarily serialize independent work.
3. Assign one accountable owner to each mutable resource and one owner to integration. Use isolated workspaces or explicit serial ownership for overlapping edits. If isolation is unavailable, choose safe sequencing rather than assuming that cooperative workers cannot overwrite each other.
4. Prepare bounded work packets for ready tasks. Include durable context, agreed interface versions, write scope, budget, and a handoff format appropriate to the work. Give each worker enough information to succeed without relying on a hidden shared conversation or importing an entire project history.
5. Define how progress and conflicts are reconciled. Use stable task identities, ownership expiry or explicit transfer where needed, and a clear rule for uncertain completion. Re-read state before reassigning or retrying an action whose effects may already exist; do not create duplicate owners from a delayed response.
6. Plan integration as real engineering work. Check the combined candidate, resolve semantic overlap, and rerun evidence affected by shared changes. Stop or replan when a prerequisite, interface, or ownership assumption changes. Completion of individual tasks does not establish that the assembled result works.

## What to return

Return the dependency and ownership plan, ready work packets, shared-interface assumptions, integration responsibility, reconciliation rules, and evidence needed for overall completion. State which coordination actions were actually performed and which are recommendations. Keep the plan small enough that a worker can identify their next permitted action without guessing.

## Boundaries

This method does not provide a scheduler, distributed lock, or permission to dispatch agents, mutate trackers, or merge work. Use available authorized mechanisms, otherwise return the plan. Do not parallelize consequential writes without isolation or ownership controls. Avoid adding workers when coordination cost exceeds the benefit or when a required decision is still unresolved.

## Worked example

A latency investigation has one worker reproduce a slow request and another inspect lock-hold observations from the same build. Those read-only tasks can proceed together. Assign one worker ownership of any resulting patch, and wait for the observations before choosing a change. The integration owner then measures the patched build against the agreed workload; independent investigation reports alone do not establish that latency improved.
