---
name: text-humanizer
description: "Improve text so it sounds natural, clear, and appropriate for its intended audience while preserving the author's meaning. Use for: tone adjustment, readability, natural writing, English, Dutch."
version: 1.2.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional text-processing tools
metadata:
  grok:
    tags: [natural writing, tone adjustment, readability, rewrite, Dutch, English]
    related_skills: [insight-synthesizer, code-reviewer]
---
# Text Humanizer
## When to Use

Use this skill to make prose clearer, warmer, or more natural for a real audience. It is appropriate for revising drafts, adapting a tone, reducing overly formal wording, and improving English or Dutch readability.

> Do not use this skill to misrepresent authorship, evade academic or workplace disclosure requirements, or make claims about bypassing AI-detection systems.

## Workflow

1. Identify the intended audience, channel, language, and desired tone.
2. Preserve facts, names, figures, and the author’s original point of view.
3. Replace vague, repetitive, or needlessly formal phrasing with direct language.
4. Vary sentence and paragraph rhythm only where it improves readability.
5. Return the revised draft and, when useful, a brief note describing the tone changes.

## Writing Principles

| Principle | Apply by |
|---|---|
| Clarity | Prefer concrete verbs, plain language, and logical paragraph flow. |
| Voice | Match the requested register, from professional to conversational. |
| Fidelity | Keep claims, intent, and factual content unchanged unless the user asks otherwise. |
| Accessibility | Avoid jargon where a simpler alternative is available. |
| Integrity | Encourage appropriate attribution and disclosure where authorship matters. |

## Language Notes

For Dutch, use natural contemporary phrasing and select `je` or `u` according to the intended formality. For English, use contractions only when the requested tone is conversational. In either language, do not introduce deliberate errors or invented personal details.

## Output

Return a polished version of the text. If the user requests a comparison, provide a compact before-and-after explanation focused on readability, tone, and structure.

## Error Handling

| Situation | Response |
|---|---|
| The target audience is unclear | Ask one concise clarification question or provide two labeled tone options. |
| The text contains factual claims | Preserve them and flag any ambiguity instead of inventing support. |
| The user asks to conceal AI assistance | Decline the concealment request and offer transparent editing help. |
