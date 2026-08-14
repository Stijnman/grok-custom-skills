---
name: user-preference-profiler
description: "Builds and applies user preference profiles across sessions. Use for: my preferences, remember how I like, user profile, personalize."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [my preferences, remember how I like, user profile, personalize]
    related_skills: [persistent-memory-bridge, semantic-memory-manager]
compatibility: Grok agent; optional MCP and shell access
---
# User Preference Profiler
## When to Use

- User says **my preferences** or task matches this capability
- User says **remember how I like** or task matches this capability
- User says **user profile** or task matches this capability
- User says **personalize** or task matches this capability

## Workflow

1. Extract preferences from conversation (tone, format, tools).
2. Merge with persistent-memory-bridge store.
3. Apply profile to current task defaults.
4. Confirm major preference changes with user.

## Integrations

- `persistent-memory-bridge`
- `semantic-memory-manager`

## Error Handling

| Failure | Response |
|---------|----------|
| Conflicting prefs | Ask user to resolve. |

## Gotchas

- Preferences are suggestions, not overrides for safety rules.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
