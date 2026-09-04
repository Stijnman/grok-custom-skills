---
name: social-media-profile-finder
description: Find public Facebook and Instagram profiles from a photo plus a name and location using reverse image search, face search, and name-location dorks. Triggered by find Facebook Instagram from photo, OSINT social profiles, identify account from picture name city, reverse face search socials, or when the user supplies a social photo plus name plus location.
metadata:
  version: "1.0"
  type: workflow
  created: "2026-09-05"
---

# Social Media Profile Finder

## Overview

Identify the most likely public Facebook and Instagram profiles that belong to a person when the user supplies (1) a photo from social media, (2) a name, and (3) a location. Combines reverse-image search, face search, and name-location Google dorks. Public data only.

## Inputs

- Photo or photo URL / description of a face-forward image
- Full name or closest known name
- City, region, or country

If any of the three is missing, ask for it before running the full workflow. A name-only or photo-only search is allowed but must be labeled lower confidence.

## Workflow

Run these steps in order. Do not skip the photo step when a photo exists.

1. Prepare the image
   - Prefer the original file over a screenshot.
   - If multiple faces, crop mentally or describe the target face.
   - Note lighting, angle, distinctive features, clothing, background landmarks.

2. Reverse image and face search
   - Exact-file engines first — Google Lens / Google Images, Yandex Images, TinEye.
   - Face engines second — FaceCheck.ID, PimEyes, similar public face indexes.
   - Record every URL where the same face or same file appears (profile pics, tagged photos, news, forums).
   - Pixel match finds copies of a file. Face match finds the same person in different photos. You usually need both.

3. Name + location search
   Use web_search and open_page with queries such as
   - `"Full Name" "City"` site:facebook.com
   - `"Full Name" "City"` site:instagram.com
   - `"Full Name" instagram` City
   - `"Full Name" facebook` City
   - common username stems of the name plus city
   Also search the name without quotes and with middle initial / nickname variants.

4. Cross-check
   A candidate only counts if at least two of these align
   - Face match (same person, not a lookalike)
   - Name or close alias
   - Location consistency (current city, hometown, check-ins, language, friends from that area)
   - Photo reuse across platforms
   Rank High / Medium / Low. Common names without a face match stay Low.

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
- search_images only when you need additional public photos of a candidate
- x_keyword_search / x_user_search if an X handle surfaces as a pivot
- Do not claim access behind logins. Do not scrape private accounts.

## Limits

- Private Instagram and locked Facebook profiles will not resolve.
- Face tools have false positives. Require a second signal.
- Paid face engines (PimEyes, FaceCheck.ID) may only be describable, not callable from this sandbox. Tell the user to run those themselves if needed and then feed results back.
- This skill is for public OSINT, catfish checks, and self-audit. It is not a stalking kit.

## Version

1.0 — 2026-09-05. Initial skill from user prompt (photo + name + location → Facebook / Instagram).
