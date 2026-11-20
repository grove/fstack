---
name: fstack-slice-vertically
description: "Decompose work into small, demonstrable behavior increments with clear dependencies and verification. Use when a feature is too broad for one worker or when a delivery plan consists mainly of technical layers."
---

# Slice vertically

## Starting point

Read the outcome, acceptance criteria, constraints, and known design decisions. Identify what a user or consumer must be able to do after delivery. Separate unresolved decisions from implementation tasks so uncertainty does not masquerade as a ready work item.

## Method

1. Map the smallest complete path from a real input to an observable useful result. Include the necessary persistence, interface, and error behavior across layers. A slice may be narrow in supported cases while remaining complete for the case it claims to support.
2. Choose an initial increment that can be demonstrated and verified without waiting for unrelated layers. Prefer reducing actors, variations, or optional features over leaving the core behavior disconnected. Name any temporary constraint that users or downstream workers must understand.
3. Define each subsequent increment by the new behavior or obligation it adds. Give it a purpose, explicit in-scope criteria, inputs, resulting behavior, verification, and exclusions. Keep implementation suggestions subordinate to the outcome.
4. Record real dependencies and the reason for each. Distinguish a prerequisite decision, shared contract, required data state, and mere preferred ordering. Remove artificial edges and check that the graph has a usable ready frontier without cycles.
5. Plan ownership and integration. Identify overlapping write areas, stable interfaces for parallel work, the integration owner, and the checks needed on the combined result. Independent branch success does not prove the integrated behavior works.
6. Handle wide mechanical changes explicitly. For a migration or coordinated contract replacement, preparation, bounded conversions, and later cleanup may be safer than artificial user-facing slices. Preserve compatibility during the transition and define the evidence required before removing the old path.
7. Check completeness against the original scope. Every required criterion needs an accountable path to delivery; every proposed task needs a reason to exist. Stop splitting when further division would create coordination work without useful independence or clearer verification.

## What to return

Return the ordered or dependency-linked work units, each with its demonstrable result, criteria, verification, ownership boundary, prerequisites, and stopping conditions. Identify the ready frontier, unresolved decision tasks, integration checkpoints, and deliberately deferred work. State which increment is selected next; do not confuse completion of one item with completion of the entire outcome.

## Boundaries

Do not create or update external tickets without authorization. A plan is not evidence of implementation, and a layer diagram is not automatically a delivery plan. Avoid unsupported estimates or parallelism that requires workers to share mutable state without coordination. The method works with ordinary text; no tracker, scheduler, or sibling skill is required.

## Worked example

A persisted status rename cannot naturally be divided into independent user journeys. Prepare readers that accept both old and new values, convert a bounded set of records with count and validity checks, then remove the old representation after proving conversion coverage. Each increment must work with its neighbors during transition. Treat this as a compatibility-driven migration exception, with an explicit completion condition, rather than pretending a column rename alone delivers user value.
