---
name: fstack-model-domain
description: "Build a precise model of domain terms, identities, rules, and state transitions. Use when vocabulary is ambiguous, business rules are scattered, or a change depends on agreeing what the system represents."
---

# Model domain

## Starting point

Gather the requested behavior, concrete scenarios, relevant domain language, and existing rules. Read accessible examples and implementation evidence to discover ambiguity, but do not assume the current database or class structure defines the domain correctly. Identify the people or documents authoritative for unsettled business decisions.

## Method

1. Extract terms from real scenarios. Ask what each term refers to, who uses it, and whether different groups mean different things. Preserve established language where it is precise; split overloaded terms instead of forcing unrelated concepts into one definition.
2. Identify entities, values, and events through their behavior. Determine what retains identity across change, what is interchangeable by value, and what records something that happened. Specify identity scope and lifetime, including tenant or account boundaries when relevant.
3. State invariants in ordinary language. Distinguish unconditional invariants from conditions that hold only in named states or after reconciliation. Separate domain rules from current implementation limitations and convenient conventions.
4. Walk through state transitions using actual examples. Record the initiating actor or event, preconditions, resulting state, failure behavior, and ownership. Include cancellation, expiration, duplicate requests, and concurrent attempts where they can change domain meaning.
5. Separate concepts across contexts when their meanings or rules legitimately differ. Name the translation boundary rather than pretending one universal object serves every group. Describe relationships with their cardinality and relevant timing without prematurely choosing storage machinery.
6. Challenge the model with a counterexample. Trace an edge case that previously caused disagreement and check whether the terms and rules produce one coherent outcome. Surface a missing business decision instead of silently encoding a guessed answer.
7. Reconcile the model with existing software and documents. Mark contradictions as current behavior, intended rule, or unresolved migration work. Keep the result small enough to guide naming, interfaces, and acceptance criteria without becoming an inventory of every noun.

## What to return

Return a concise glossary, identity rules, important relationships, invariants, state transitions, representative examples, and unresolved domain decisions. Use a table or diagram only when it clarifies the model. Distinguish agreed rules from proposals and implementation observations. State which contradictions require resolution before dependent work proceeds.

## Boundaries

Do not turn this exercise directly into database tables, classes, services, or a framework-specific design. Model the domain before selecting its representation. Work within the supplied scope and authority; a discovered inconsistency does not authorize a data migration or policy change. This method needs no other skill or prescribed glossary file.

## Worked example

A document review system calls both comments and required sign-offs “feedback.” Separate a comment, which may discuss any draft, from an approval attached to an exact revision. Define who can approve and which approvals publication requires. If a new revision appears, establish whether old approvals remain valid before drawing the transition. A comment count cannot stand in for approval status merely because both appear on the same screen.
