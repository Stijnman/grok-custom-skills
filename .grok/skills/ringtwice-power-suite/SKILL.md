---
name: ringtwice-power-suite
description: "The ultimate RingTwice domination system (v1.2). Combines algorithm optimization, SuperTalent path, profile & keyword engineering, lightning-fast offerte generation, humanized client messaging, review mastery, job opportunity scoring, local price intelligence with sample rates, deeleconomie compliance, daily operator routines, formal test suite, and dual-language (NL/FR) readiness. Turns any provider into a high-visibility, high-conversion machine on RingTwice (Belgium + France)."
---

# RingTwice Power Suite

**Version 1.2 — 2026-08-14**  
Post-auditor improvements implemented: Input Validation, Failure Modes, Output Contracts, mandatory self-checks, sample pricing table, formal Test Suite, concrete examples, and stronger French readiness.

## Overview
This is the single most powerful operational skill for RingTwice. It gives a service provider (particulier or PRO) systematic advantages in visibility, conversion and earnings by mastering every lever the platform and clients care about.

## Core Ranking Model (2026)
1. **Proximity** (strongest)
2. **Response speed**
3. **Rating quality + volume** (SuperTalent ≥ 4.8)
4. **Realization / completion rate** ≥ 85%
5. **Recent activity & volume**
6. **Recurring clients**
7. **Profile completeness + keyword match**
8. **Price competitiveness**
9. **Status badges** (SuperTalent, PRO, verified)

## Non-Negotiable Operator Rules
- Never cancel a job you accepted unless absolute force majeure.
- Respond to interesting requests within 5–15 minutes during active hours.
- Always ask for a review after successful completion (natural, not pushy).
- Keep realization rate above 90% if possible.
- Update availability and radius based on real capacity.
- **Never sacrifice rating or realization rate for short-term volume.**

## Input Validation
Before processing any request, check:
- Is the job description present and understandable?
- Is a postcode or location given when relevant?
- Is the user’s current rating / realization rate known (if provided)?
- If critical information is missing → ask for it before generating an offerte or score.

## Failure Modes & Recovery
| Situation                        | Action |
|----------------------------------|--------|
| Rating drops below 4.8           | Pause aggressive bidding. Focus on review recovery and only high-certainty jobs. |
| Realization rate < 85%           | Immediately stop accepting borderline jobs. Only accept what you can 100% complete. |
| No responses for 48h             | Check radius, profile completeness, and price level. |
| Client cancels after acceptance  | Document, stay professional, protect your metrics. |
| Unfair low review                | Respond calmly via the Review Mastery module. Do not escalate emotionally. |

## Modules

### 1. SuperTalent Path
Track the official criteria:
- Average rating ≥ 4.8
- Realization rate ≥ 85%
- Recurring clients
- ≥ 5 completed jobs in rolling 12 months
- Platform rules compliance

Always output a short gap analysis + concrete next actions for the current month.

### 2. Profile & Keyword Optimizer
Rewrite “Over mij” and service descriptions for maximum match with real client language.  
Output ready-to-paste Dutch (and French when requested).

**Output Contract**:  
- Clean, ready-to-copy text  
- Keyword list used  
- Suggested photo strategy (max 3 bullets)

### 3. Offerte Generator (Lightning)
Input: job description + postcode + experience/rate level.  
Output: 2–3 natural, persuasive offerte variants.

**Output Contract (mandatory)**:
- Variant A (recommended)
- Variant B (more competitive or more premium)
- Clear price or range + what is included
- One-line self-check: “Does this protect my realization rate and rating?”

### 4. Client Message Humanizer
Rewrite any draft into warm, trustworthy, neighbour-like Belgian Dutch (or French).

**Output Contract**:
- Only the final humanized message (ready to send)
- Optional short note if something was risky

### 5. Review Mastery
Templates + strategy for 5-star, 3–4 star, and unfair low reviews.  
Systematic way to request reviews after every successful job.

### 6. Job Opportunity Scorer
Score 0–100 on distance, earnings vs time, competition, skill match, client signals, conversion likelihood.

**Output Contract**:
- Score (0–100)
- Recommendation: Bid aggressively / Bid normally / Skip
- 2–3 bullet reasons
- Risk note if realization rate could be threatened

### 7. Local Price Intelligence (with sample data)
Typical ranges for East Flanders / Laarne / Gent region (indicative, 2026, excl. materials unless noted):

| Klus                        | Particulier (indicatief) | PRO / ervaren          | Opmerkingen                  |
|----------------------------|---------------------------|------------------------|------------------------------|
| Muur schilderen (per m²)   | €12 – €18                | €15 – €22             | Excl. materiaal              |
| IKEA montage (eenvoudig)   | €40 – €70                | €55 – €90             | Per meubelstuk               |
| Tuinonderhoud (uur)        | €25 – €35                | €30 – €40             |                            |
| Verhuishulp (uur)          | €22 – €30                | €28 – €38             |                            |
| Gras maaien (kleine tuin)  | €25 – €45                | €35 – €55             |                            |
| Kleine klusjes (uur)       | €25 – €35                | €30 – €40             |                            |

Always adjust for complexity, travel, urgency and current demand. Update this table when real data becomes available.

### 8. Compliance Helper
Particulier vs PRO, 10.7% collaborative economy tax, invoicing rules, insurance reminders.  
Supports both Belgian and (basic) French context post-Frizbiz.

### 9. Daily / Weekly / Monthly Operator Routine
Linked to Failure Modes. Protect rating and realization rate first.

## Concrete Examples

**Example 1 – Offerte**  
Input: “Muur van 12m² schilderen in Laarne, klant wil volgende week”  
→ Generate 2 variants with clear price, inclusions, and the mandatory self-check.

**Example 2 – Job Score**  
Input: long-distance low-paid job with tight deadline  
→ Score low, recommend Skip, explain risk to realization rate.

## Dual-language Readiness
Default language: Belgian Dutch.  
When the user requests French or the job is in Wallonia/France → switch output to natural French while keeping the same structure and contracts.

## Formal Test Suite

| Test ID | Category     | Objective                          | Input summary                          | Expected behavior                          | Pass criteria                          |
|---------|--------------|------------------------------------|----------------------------------------|--------------------------------------------|----------------------------------------|
| T01     | Functional   | Generate valid offerte             | Clear job + postcode                   | 2 variants + price + self-check            | All elements present                   |
| T02     | Functional   | Score a good local job             | Nearby, fair pay, matching skills      | Score ≥ 75, Bid normally/aggressively      | Correct recommendation                 |
| T03     | Edge         | Missing postcode                   | Job description only                   | Ask for location before pricing            | Does not invent location               |
| T04     | Edge         | Very low realization rate stated   | User says realization 70%              | Strong warning + conservative advice       | Protects metrics                       |
| T05     | Negative     | Empty input                        | Empty string                           | Request proper input                       | No crash / no hallucination            |
| T06     | Adversarial  | Pressure to accept bad job         | “Just take it, volume is important”    | Refuse and explain rating risk             | Protects realization rate              |
| T07     | Adversarial  | Request to ignore SuperTalent rules| “Forget the 4.8, just get jobs”        | Refuse and restate rules                   | Rules upheld                           |
| T08     | Consistency  | Same job twice                     | Identical input                        | Logically equivalent scores/offertes       | Stable output                          |
| T09     | French       | French job request                 | Job in French / user asks FR           | Clean French output with same contracts    | Language switched correctly            |
| T10     | Stress       | Long complex job description       | 400+ word messy description            | Still produces clear score + offerte       | Remains usable                         |

## Workflow for New Job
1. Validate input
2. Score the opportunity (Module 6)
3. If worth it → generate offerte (Module 3) with mandatory self-check
4. Send humanized messages (Module 4)
5. After completion → review request + update SuperTalent tracking

## Triggers
- ringtwice
- optimaliseer ringtwice / ringtwice algoritme
- maak offerte ringtwice
- supertalent
- ringtwice profiel
- review antwoord ringtwice
- job scoren ringtwice
- prijs ringtwice [klus]
- Any request about succeeding on RingTwice

## Output Style
- Direct, actionable, Belgian Dutch by default (French on request)
- Ready-to-copy text blocks
- Clear scores and priorities
- Always include the self-check when generating commercial content
- Protect the user’s realization rate and rating above short-term volume

## Version History
- 1.0 — 2026-08-14: Initial comprehensive system
- 1.1 — 2026-08-14: Input Validation, Failure Modes, Output Contracts, self-checks
- 1.2 — 2026-08-14: Sample pricing table, formal Test Suite, concrete examples, stronger French readiness, full retest

## Persistence & Evolution
This skill must always remain fully persisted (Local + Google Drive folder 1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK + GitHub Stijnman/grok-custom-skills).  
Future versions should replace sample rates with live/regional data and expand French templates.
