---
name: flip-pipeline-operator
description: Use when the user wants a Belgian-first resale arbitrage pipeline for underpriced scans, 2dehands deal scoring, Vinted/eBay margin checks, fee-aware comparisons, or sellflow drafts.
license: MIT
---

# Flip Pipeline Operator

**Version:** 1.1.1 (2026-09-22)

## When to use

Use this skill when the user wants underpriced second-hand deals in BE/NL/US scored after fees and shipping.

## Workflow

1. Confirm query, budget, region (`be` default), minimum ROI, and private vs business seller assumptions.
2. Prefer documented marketplace APIs or user-provided/exported listing data over brittle HTML scraping.
3. Score candidates with current fee and shipping tables; keep fee assumptions explicit and configurable rather than silently treating them as permanent constants.
4. Label comparable sales as proxies unless verified sold-market data is available.
5. Respect marketplace access controls and do not bypass authentication, anti-bot controls, or platform restrictions.
6. Persist structured results only to an approved workspace or repository path.

## Output

Return the source listing, acquisition cost, estimated resale range, fees, shipping, expected gross/net margin, ROI, confidence, and the assumptions that materially affect the score.
