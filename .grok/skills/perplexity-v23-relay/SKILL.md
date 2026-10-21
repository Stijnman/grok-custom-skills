---
name: perplexity-v23-relay
description: Coordinate evidence-focused collaboration between AI agents through the user as the manual relay, with result-first reporting, explicit evidence states, scoped authorization, and loop prevention. Use when the user asks to start the Perplexity v2.3 relay, use a manual relay protocol, or coordinate a high-integrity multi-agent handoff.
license: MIT
metadata:
  version: "2.0"
  aliases:
    - perplexity-v2.3-relay
---

# Perplexity v2.3 Relay

## Overview
This skill activates the full Perplexity v2.3 manual relay protocol. Two agents (or the same model in successive turns) collaborate exclusively through the user. The user is the only relay and the final decision-maker. The skill enforces rigorous evidence tracking, state integrity, independent role selection, and result-first output.

## Core Rules (Non-Negotiable)
- Result-first: The useful artifact always comes before diagnostic sections
- Independent role selection every round
- Strict evidence states: VERIFIED | UNVERIFIED | ASSUMPTION | SIMULATED | BLOCKED | OPINION | REVALIDATION NEEDED
- Persistent working state with active/archived compaction
- Authorization Class 0–3 + scope integrity
- Anti-loop: track NO_MATERIAL_PROGRESS_STREAK; force synthesis or stop after 2 empty rounds
- Never treat another agent’s agreement as evidence
- Never invent missing state

## Instructions
1. Confirm adoption of Perplexity v2.3
2. Wait for original user request or full relay envelope
3. Choose the single highest-value role independently
4. Produce the best current contribution first
5. Report only material state deltas
6. End with one of: [CONTINUE — IMPROVEMENT REQUIRED] | [CONTINUE — EVIDENCE REQUIRED] | [READY FOR USER DECISION]

## Trigger Phrases
- start perplexity relay
- use perplexity v2.3
- activate manual relay
- perplexity protocol
- high-integrity relay

## Output Format
Prefer the Compact Intermediate Format unless full diagnostic reporting is justified.

## Version
2.0 — 2026-10-21. Renamed the invalid dotted identifier; clarified external persistence approval.
