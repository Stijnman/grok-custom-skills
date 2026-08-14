---
name: accessible-color-review
description: "Review color choices for contrast, semantic consistency, color-vision accessibility, and readable user-interface states. Use for: color accessibility review, contrast check, UI color audit, accessible palette."
license: MIT
metadata:
  version: 1.0.0
  author: Stijnman
  grok:
    tags: [color accessibility review, contrast check, UI color audit, accessible palette]
---

# Accessible Color Review

## Purpose

Review a palette, design, screenshot, or interface implementation for readability and robust semantic color use. Treat automated checks as evidence to review, not as a substitute for visual or user testing.

## Workflow

1. Identify foreground-background pairs, interactive states, data visualizations, and color-only signals.
2. Calculate or verify contrast for text and essential UI elements using the applicable accessibility target.
3. Check whether color communicates meaning consistently and whether another cue supports status, errors, and links.
4. Review color-vision risks, especially charts and success/error pairings.
5. Propose the smallest changes that improve readability while preserving the visual system.
6. Return findings with observed evidence, confidence, severity, and suggested replacements.

## Quality boundaries

Do not claim compliance from a palette alone. Contrast depends on rendered size, weight, background, opacity, and state. Flag uncertainty when an image or code sample cannot establish those conditions.

## Error handling

| Situation | Response |
|---|---|
| Screenshot is incomplete | Limit findings to visible evidence and request the missing state. |
| Pair cannot be measured | Explain the required colors and rendering context. |
| Brand color fails contrast | Offer accessible pairings or non-color cues instead of changing it without context. |
| Chart uses similar categories | Recommend labels, patterns, markers, or direct annotation. |
