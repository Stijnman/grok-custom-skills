---
name: product-requirements-document
description: "Write a clear product requirements document that defines the problem, scope, requirements, success measures, risks, and open questions. Use for: product requirements document, PRD, feature specification, engineering handoff."
license: Apache-2.0
metadata:
  version: 1.0.0
  author: Stijnman
  grok:
    tags: [product requirements document, PRD, feature specification, engineering handoff]
---

# Product Requirements Document

## Purpose

Create a decision-ready product specification that explains why work matters, what must be delivered, what is out of scope, and how success will be evaluated without inventing unavailable facts.

## Workflow

1. State the user or business problem, relevant context, and the intended outcome.
2. Define measurable success criteria and identify the evidence or baseline supporting each one.
3. Describe the proposed user-facing behavior and the functional requirements needed to support it.
4. Separate in-scope work, explicit exclusions, assumptions, dependencies, and unresolved questions.
5. Surface non-functional requirements such as accessibility, reliability, privacy, performance, or security only when relevant.
6. Identify risks, owners where known, and validation or rollout considerations.
7. Deliver the PRD as a reviewable draft; do not present it as approved unless the user confirms approval.

## Required sections

Include: **Problem**, **Goals and success measures**, **Users and use cases**, **Scope**, **Requirements**, **Non-functional considerations**, **Dependencies and risks**, **Open questions**, and **Acceptance criteria**.

## Quality boundaries

Do not fabricate customer evidence, market data, timelines, owners, technical commitments, or performance targets. Mark assumptions and placeholders visibly. Keep solution detail sufficient for alignment but leave implementation design to the relevant technical decision process.

## Error handling

| Situation | Response |
|---|---|
| Problem is not agreed | Produce a problem-framing draft and identify the missing decision. |
| Requirements conflict | Record the conflict, affected stakeholder, and trade-off rather than hiding it. |
| Metrics have no baseline | Propose a measurement plan and label the target provisional. |
| Scope is too broad | Split the document into a smallest viable release and deferred work. |
