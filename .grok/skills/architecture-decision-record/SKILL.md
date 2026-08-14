---
name: architecture-decision-record
description: "Document a significant technical decision with its context, alternatives, consequences, and status. Use for: architecture decision record, ADR, technical decision log, technology choice."
license: Apache-2.0
metadata:
  version: 1.0.0
  author: Stijnman
  grok:
    tags: [architecture decision record, ADR, technical decision log, technology choice]
---

# Architecture Decision Record

## Purpose

Write a concise, durable record of a material technical decision so future contributors can understand the context, trade-offs, and consequences without reconstructing the discussion.

## Workflow

1. Confirm that a real architecture or technology decision is being made; do not create an ADR for routine implementation detail.
2. Assign a stable identifier and a short active-voice title.
3. Describe the context, constraints, decision drivers, and relevant stakeholders.
4. Record the chosen decision precisely, including the intended scope and status: proposed, accepted, deprecated, or superseded.
5. Compare meaningful alternatives and explain the evidence or trade-offs behind the choice.
6. State positive, negative, and neutral consequences, including migration or operational effects.
7. Link related decisions or supporting evidence when available, then deliver the ADR for review.

## Output template

Use these headings: **Status**, **Context**, **Decision**, **Alternatives considered**, **Consequences**, and **References**. Keep the record self-contained and concise.

## Quality boundaries

Do not fabricate consensus, benchmarks, approvals, or cost estimates. Preserve uncertainty where it remains. An ADR documents a decision; it does not replace a design review, security review, or implementation plan.

## Error handling

| Situation | Response |
|---|---|
| Decision is still exploratory | Recommend a time-boxed spike or options analysis before creating an ADR. |
| No clear decision owner | Mark ownership as unresolved and request the needed governance context. |
| Prior decision exists | Cross-reference it and use the correct supersession status. |
| Alternatives lack evidence | State the limitation and identify the next validation step. |
