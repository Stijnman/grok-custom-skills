---
name: flip-pipeline-operator
description: Analyze potentially underpriced second-hand listings in Belgium, the Netherlands, and the US, comparing fees, shipping, and resale comps. Use when the user asks for a flip-pipeline scan, deal score, or resale margin estimate. Ask before saving or sharing results, contacting sellers, or taking a marketplace action.
license: MIT
metadata:
  version: "1.2.0"
---

# Flip Pipeline Operator

**Version:** 1.2.0 (2026-10-21)

## When to use
User wants underpriced second-hand deals in BE/NL/US scored after fees and shipping.

## Do this
1. Confirm query, budget, region (`be` default), min ROI, private vs business eBay seller.
2. Source first from Adevinta JSON — GET https://www.2dehands.be/lrp/api/search — not HTML scrape.
3. Score with scorer.py using 2026 tables (US 13.6%+$0.40, EEA private 0%, EEA business ~11%+1.9%+€0.35, bpost pickup €5.40/0-2kg).
4. Label comps as proxy unless Marketplace Insights / Terapeak sold data is present. Finding API died 2025-02-04.
5. Never scrape Facebook Marketplace or OfferUp.
6. Save a local CSV only when requested. Before a repository push, seller contact, purchase, or listing action, state the target and proposed content/action and obtain explicit user approval.


## Version

1.2.0 — 2026-10-21. Added approval before remote writes or marketplace actions.
