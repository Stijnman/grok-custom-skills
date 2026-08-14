---
name: skill-creation-enablerimage-processor
description: "Image processing helper for skill assets: resize, optimize, format convert. Use for: process skill image, optimize asset, skill icon, resize skill image."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [process skill image, optimize asset, skill icon, resize skill image]
    related_skills: [skill-creation-enabler, imagine-asset-generator, safe-image-editor]
compatibility: Grok agent; optional MCP and shell access
---
# Skill Creation Enablerimage Processor
## When to Use

- User says **process skill image** or task matches this capability
- User says **optimize asset** or task matches this capability
- User says **skill icon** or task matches this capability
- User says **resize skill image** or task matches this capability

## Workflow

1. Load image from skill assets/ or user path.
2. Resize to target dimensions (icons: 96px, banners: 720w).
3. Convert to PNG or SVG as appropriate.
4. Save alongside SKILL.md; update references.

## Integrations

- `skill-creation-enabler`
- `imagine-asset-generator`
- `safe-image-editor`

## Error Handling

| Failure | Response |
|---------|----------|
| Unsupported format | Convert via PNG intermediate. |

## Gotchas

- Companion to skill-creation-enabler for visual skills.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
