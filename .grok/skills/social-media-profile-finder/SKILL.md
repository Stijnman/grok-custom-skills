---
name: social-media-profile-finder
description: Help a user audit their own public Facebook or Instagram presence using profile details and sources they provide. Use when the user asks to find, verify, or review their own public social-media profiles. Do not identify or track private people from photos, face search, or location clues.
metadata:
  version: "2.0"
  type: workflow
  created: "2026-09-05"
license: MIT
---

# Social Media Profile Finder

## Overview

Help the user audit their own public Facebook and Instagram presence using names, handles, or links they supply. Do not infer identity from a photo or search for another private person. Keep review limited to public pages and the stated self-audit purpose.

## Inputs

- Public profile links or handles the user controls
- Name or username the user supplies for their own account

Confirm that the user owns or is authorized to manage the account. If authorization is unclear, stop and offer general privacy/self-audit guidance rather than locating profiles.

## Workflow

Use only public sources and identifiers the user provided. Do not use a photo to identify a person.

1. Search identifiers supplied by the user
   - Search the user's stated handles, profile URLs, and name variants on the named public platforms.
   - Use exact-image matching only to locate copies of an image the user owns or is authorized to audit; do not use face-search engines to identify a person.
   - Record relevant public URLs and distinguish confirmed account ownership from name similarity.

2. Cross-check
   - Treat an account as belonging to the user only when they confirm it or it links from an account they control.
   - A matching name or image alone is not proof. Do not infer identity from location, friends, or biometric similarity.

5. Output (strict)
   - Highest-confidence Facebook URL + evidence
   - Highest-confidence Instagram URL + evidence
   - Other candidates ranked
   - Confidence per result
   - What could not be confirmed (private account, common name, no indexed photos)
   - Exact searches that were run

Do not invent profiles. If nothing solid appears, say so and list the searches.

## Tool use

- web_search and open_page for dorks and result pages
- search_images only to find an exact copy of an authorized user-owned image; never to identify a person
- x_keyword_search / x_user_search if an X handle surfaces as a pivot
- Do not claim access behind logins. Do not scrape private accounts.

## Limits

- Private Instagram and locked Facebook profiles will not resolve.
- Do not use face-search services to identify or track people.
- Do not direct the user to face-search services to identify another person.
- This skill is for a user’s own-account self-audit. Do not use it for stalking, doxxing, surveillance, or locating private individuals.

## Version

2.0 — 2026-10-21. Narrowed to authorized self-audits; removed identity inference from face and location searches.
