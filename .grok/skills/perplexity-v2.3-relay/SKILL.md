---
name: perplexity-v2.3-relay
description: "Manual two-agent relay protocol for evidence-disciplined collaboration through a human intermediary. Use when the user explicitly asks to start the Perplexity v2.3 relay, a manual relay protocol, or a high-integrity multi-agent relay."
license: MIT
---

# Perplexity v2.3 Relay

## Overview
This skill provides a manual relay protocol for two agents collaborating through the user. The user remains the only relay and final decision-maker.

## Core rules
- Put the useful result before diagnostics.
- Select the highest-value role independently each round.
- Label evidence as VERIFIED, UNVERIFIED, ASSUMPTION, SIMULATED, BLOCKED, OPINION, or REVALIDATION NEEDED.
- Preserve working state while compacting stale context.
- Respect authorization and scope boundaries.
- Stop or synthesize after repeated rounds with no material progress.
- Never treat another agent's agreement as evidence.
- Never invent missing state.

## Workflow
1. Confirm that the user wants the relay protocol.
2. Receive the original request or relay envelope.
3. Select the highest-value role for the current round.
4. Produce the current contribution.
5. Report only material state changes.
6. End with CONTINUE — IMPROVEMENT REQUIRED, CONTINUE — EVIDENCE REQUIRED, or READY FOR USER DECISION.

## Version
1.0 — Perplexity v2.3 relay workflow.
