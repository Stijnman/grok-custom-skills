---
name: product-opportunity-tree
description: "Map a measurable product outcome to customer opportunities, solution options, and assumption tests. Use for: opportunity solution tree, product discovery map, customer opportunity mapping, outcome-to-solution planning."
license: Apache-2.0
metadata:
  version: 1.0.0
  author: Stijnman
  grok:
    tags: [opportunity solution tree, product discovery map, customer opportunity mapping, outcome-to-solution planning]
---

# Product Opportunity Tree

## Purpose

Create an evidence-aware opportunity tree that connects a desired outcome to customer needs, candidate solutions, and assumption tests. Use it to avoid treating a feature idea as the problem definition.

## Workflow

1. Define one measurable outcome that the team can influence, including its current baseline if known.
2. List customer opportunities as needs, barriers, or desired outcomes rather than proposed features.
3. Attach evidence to each opportunity and label it as observed, reported, inferred, or unknown.
4. Generate multiple solution options for promising opportunities; do not select a solution merely because it was proposed first.
5. Identify the riskiest assumption for each selected solution and define the smallest ethical test that could reduce uncertainty.
6. Prioritize the next branch using impact, confidence, effort, and evidence quality.
7. Deliver a tree, evidence notes, open questions, and the next experiment.

## Output format

Use a concise hierarchy: **Outcome → Opportunities → Solutions → Assumption tests**. Include a Mermaid diagram when it improves readability, but keep the textual hierarchy authoritative.

## Quality boundaries

Do not invent research evidence, customer quotes, baselines, or business impact. Distinguish a hypothesis from a validated opportunity. Do not present the tree as a commitment or roadmap without the relevant stakeholder approval.

## Error handling

| Situation | Response |
|---|---|
| Outcome is not measurable | Propose a measurable proxy and label it as a draft. |
| Evidence is sparse | Keep opportunities provisional and recommend discovery work before prioritization. |
| Solution list is already fixed | Record the constraint and identify the assumptions that still need testing. |
| Stakeholders disagree | Represent competing outcomes or assumptions rather than forcing a false consensus. |
