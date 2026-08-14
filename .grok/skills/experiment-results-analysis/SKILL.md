---
name: experiment-results-analysis
description: "Analyze completed experiment results with effect sizes, uncertainty, guardrails, limitations, and evidence-based next steps. Use for: experiment results, A/B test analysis, test readout, experiment decision."
license: Apache-2.0
metadata:
  version: 1.0.0
  author: Stijnman
  grok:
    tags: [experiment results, A/B test analysis, test readout, experiment decision]
---

# Experiment Results Analysis

## Purpose

Create an honest experiment readout that separates measured outcomes from interpretation and avoids treating inconclusive data as a decision.

## Workflow

1. Record the hypothesis, variants, primary metric, guardrails, sample sizes, time window, and pre-defined stopping rule when available.
2. Check data quality, assignment integrity, missing values, and material deviations from the experiment plan.
3. Report primary and guardrail metrics with effect estimates, uncertainty, and the method used.
4. Review relevant segments cautiously; label exploratory segment findings and avoid overinterpreting small samples.
5. State whether the evidence supports shipping, iterating, stopping, or gathering more data.
6. Capture learnings, limitations, and next steps.

## Evidence boundaries

Do not invent baselines, statistical significance, causal conclusions, or business impact. A decision recommendation must state the evidence strength and any remaining risk.

## Error handling

| Situation | Response |
|---|---|
| Required metrics are missing | Describe the gap and recommend a measurement plan. |
| Results are inconclusive | State that clearly and propose the smallest useful follow-up. |
| Guardrail degrades | Flag the trade-off even if the primary metric improves. |
| Segments are underpowered | Treat them as exploratory rather than decisive. |
