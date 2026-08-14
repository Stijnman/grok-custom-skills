---
name: imagine-asset-generator
description: "Generates visual assets via image generation tools. Use for: generate image, create asset, make icon, design mockup."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [generate image, create asset, make icon, design mockup]
    related_skills: [imagine, compliance-image-guard, safe-image-editor]
compatibility: Grok agent; optional MCP and shell access
---
# Imagine Asset Generator
## When to Use

- User says **generate image** or task matches this capability
- User says **create asset** or task matches this capability
- User says **make icon** or task matches this capability
- User says **design mockup** or task matches this capability

## Workflow

1. Clarify subject, style, dimensions, and constraints.
2. Run compliance-image-guard on prompt.
3. Generate via imagine skill or image API.
4. Deliver file path and usage notes.

## Integrations

- `imagine`
- `compliance-image-guard`
- `safe-image-editor`

## Error Handling

| Failure | Response |
|---------|----------|
| Policy block | Revise prompt; explain blocked element. |

## Gotchas

- Load imagine skill when image_gen tools are available.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
