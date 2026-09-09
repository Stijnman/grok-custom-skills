---
name: flip-pipeline-operator
description: Runs the Belgian-first resale arbitrage pipeline (2dehands/Marktplaats Adevinta JSON, Vinted scrape, eBay proxy comps, 2026 fee math, sellflow drafts). Triggered by flip pipeline, underpriced scan, 2dehands deal score, Vinted vs eBay margin.
---

# Flip Pipeline Operator

**Version:** 1.1.0 (2026-09-09)

## When to use
User wants underpriced second-hand deals in BE/NL/US scored after fees and shipping.

## Do this
1. Confirm query, budget, region (`be` default), min ROI, private vs business eBay seller.
2. Source first from Adevinta JSON — GET https://www.2dehands.be/lrp/api/search — not HTML scrape.
3. Score with scorer.py using 2026 tables (US 13.6%+$0.40, EEA private 0%, EEA business ~11%+1.9%+€0.35, bpost pickup €5.40/0-2kg).
4. Label comps as proxy unless Marketplace Insights / Terapeak sold data is present. Finding API died 2025-02-04.
5. Never scrape Facebook Marketplace or OfferUp.
6. Persist CSV + push Stijnman/flip-pipeline.
