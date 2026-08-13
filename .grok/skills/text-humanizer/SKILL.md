---
name: text-humanizer
description: "Rewrites any text so it reads as naturally human-written and consistently passes AI detectors (GPTZero, Originality.ai, ZeroGPT, Turnitin, Copyleaks, etc.). Removes typical AI patterns, injects human imperfections, varied rhythm, contractions, personal voice, and subtle inconsistencies. Triggered by 'humanize this text', 'make this sound human', 'bypass AI detection', 'rewrite so detectors fail', or when content must appear non-AI. Optimized for accurate LLM routing."
---

# Text Humanizer

## Overview
Transforms AI-generated, formal, or overly polished text into natural human writing that is extremely difficult for current AI detection systems to flag. Focuses on statistical and stylistic fingerprints that detectors look for: perplexity, burstiness, repetitive structure, perfect grammar, hedging language, and uniform sentence length.

## Core Goals
- Maximize "human" score on major detectors
- Preserve original meaning and key information
- Produce readable, natural Dutch or English (match input language)
- Avoid both robotic perfection and obvious "trying-to-sound-human" artifacts

## Non-Negotiable Rules
1. Never claim the text is "AI-free" or "undetectable" in the output itself.
2. Always match the language of the input (Dutch stays Dutch, English stays English).
3. Do not invent facts or change the core message.
4. Prefer mild, realistic imperfections over exaggerated slang or errors.
5. When the user asks for maximum evasion, apply the full aggressive set of techniques.

## Humanization Techniques (apply in combination)

### Structural & Rhythm
- Break long uniform paragraphs into uneven lengths
- Mix very short sentences with longer ones (burstiness)
- Start some sentences with "And", "But", "So", "Anyway", "Look"
- Occasionally use sentence fragments for emphasis
- Vary paragraph length deliberately

### Lexical & Style
- Heavy use of contractions (I'm, don't, can't, it's, we're, they've)
- Replace formal words with everyday equivalents
- Insert mild filler or discourse markers: "kinda", "sort of", "honestly", "to be fair", "you know", "basically"
- Use occasional mild redundancy or slightly imprecise phrasing
- Prefer active voice and concrete language
- Avoid classic AI tells: "delve into", "tapestry", "landscape of", "it's important to note", "in conclusion", "furthermore", "moreover", "robust", "leverage", "utilize", "facilitate"

### Imperfections (realistic, not cartoonish)
- Occasional minor grammar slip that a real person would make under time pressure
- Slightly awkward but natural phrasing
- Personal asides or mild opinion coloring when appropriate
- Inconsistent comma usage or slight run-on tendencies
- Avoid perfect parallel structure

### Dutch-specific (when input is Dutch)
- Use natural spoken Dutch: "ik heb", "het is", "gewoon", "eigenlijk", "best wel", "nogal", "serieus"
- Prefer "je" over "u" unless formal context demands it
- Insert typical Belgian/Dutch fillers: "zeg maar", "eigenlijk", "gewoon", "echt", "toch"
- Avoid overly correct or translated-sounding constructions

## Workflow
1. Analyze the input for AI fingerprints (uniform length, formal vocabulary, lack of contractions, hedging, list-like structure).
2. Rewrite in one or two passes:
   - First pass: break structure + inject contractions and everyday vocabulary
   - Second pass: add rhythm variation, mild imperfections, and personal tone
3. Optionally run a self-check: does this still sound like something a competent but non-professional human would write quickly?
4. Return only the humanized text unless the user asks for comparison or technique explanation.

## Input
- Raw text to humanize
- Optional: target tone (casual, semi-formal, slightly imperfect, aggressive evasion)
- Optional: language force (though auto-detect is preferred)

## Output
- Clean humanized version of the text
- No meta commentary unless requested
- Preserve original meaning, names, numbers, and key claims

## Triggers
- "humanize this"
- "make this sound human"
- "rewrite so AI detectors fail"
- "bypass AI detection"
- "make undetectable"
- "humanize text"
- "anti AI detector rewrite"
- Any request to make text appear non-AI written

## Version
1.0 — 2026-08-14
Initial production version focused on maximum practical evasion of current detectors while keeping output readable and natural.

## Notes
This skill prioritizes statistical human-likeness (high burstiness, natural perplexity variation) over pure grammatical perfection. It is designed to work in both English and Dutch. For best results on detectors, combine with moderate length variation and avoid feeding the humanized output back into the same model for further "polishing".
