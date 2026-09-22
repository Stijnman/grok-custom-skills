---
name: social-media-profile-finder
description: "Find likely public social-media profiles from user-provided identity clues using public web search and evidence cross-checking. Use for authorized self-audits, catfish checks, or locating a public account when the user supplies sufficient non-sensitive clues."
license: MIT
metadata:
  version: "1.1"
  type: workflow
---

# Social Media Profile Finder

## Scope
Use public information only. Do not bypass logins, access private accounts, or use this workflow for stalking, harassment, sensitive-trait inference, or invasive tracking.

## Inputs
- A name or public alias.
- A broad location when relevant.
- A public photo only when the user is authorized to use it.

A partial search is allowed, but confidence must reflect missing signals.

## Workflow
1. Search public web results for the supplied name/alias and location.
2. Compare public profile details that the user already supplied or that are openly visible.
3. Require multiple independent matching signals before calling a candidate high confidence.
4. Clearly separate confirmed facts, likely matches, and unresolved candidates.
5. Return public URLs only; do not attempt to reveal private account content.

## Confidence
- High: multiple independent public signals align.
- Medium: some corroboration exists but identity is not conclusive.
- Low: common-name or weak-signal candidate.

## Output
Return the strongest public candidates, supporting evidence, confidence, and what could not be verified. Never invent a profile.

## Version
1.1 — tightened public-data and authorization boundaries.
