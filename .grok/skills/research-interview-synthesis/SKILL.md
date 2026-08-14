---
name: research-interview-synthesis
description: "Synthesize multiple user interviews into evidence-backed themes, insights, limitations, and next research actions. Use for: interview synthesis, customer research findings, usability study themes, discovery interview analysis."
license: Apache-2.0
metadata:
  version: 1.0.0
  author: Stijnman
  grok:
    tags: [interview synthesis, customer research findings, usability study themes, discovery interview analysis]
---

# Research Interview Synthesis

## Purpose

Turn multiple user-research conversations into a traceable synthesis that distinguishes what participants said from the team’s interpretation and recommendations.

## Workflow

1. Confirm the research question, participant count, recruitment context, and available materials.
2. Remove or replace direct identifiers unless they are essential and authorized for the requested audience.
3. Code observations by topic while preserving participant IDs and source references.
4. Identify recurring patterns, notable exceptions, and areas of disagreement; do not treat frequency as proof of importance.
5. Draft insights that state the evidence, interpretation, confidence, and limitations separately.
6. Propose research or product actions that tie back to specific findings.
7. Deliver a research overview, themes, representative attributed excerpts, insights, recommendations, and limitations.

## Evidence rules

Use verbatim quotations only when they are present in the source and safe to share. Do not fabricate quotes, merge comments into a false quotation, or infer prevalence from a small convenience sample. Label tentative findings clearly.

## Output format

For each theme, include: **evidence**, **interpretation**, **confidence**, **representative participant IDs**, and **implication**. End with open questions and the recommended next research step.

## Error handling

| Situation | Response |
|---|---|
| Fewer than three research conversations | Produce an exploratory summary, not a pattern claim. |
| Notes are incomplete | Separate direct evidence from inference and list the missing data. |
| Sensitive personal data is present | Redact or generalize it before preparing a shareable report. |
| Stakeholders request certainty not supported by data | State the limitation and propose a validation method. |
