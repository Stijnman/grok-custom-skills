---
name: drive-persistence-bridge
description: "Persists agent artifacts to cloud drive storage. Use for: save to drive, persist output, upload report, cloud backup."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [save to drive, persist output, upload report, cloud backup]
    related_skills: [connected-services-bridge, privacy-redactor, persistent-memory-bridge]
compatibility: Grok agent; optional MCP and shell access
---
# Drive Persistence Bridge
## When to Use

- User says **save to drive** or task matches this capability
- User says **persist output** or task matches this capability
- User says **upload report** or task matches this capability
- User says **cloud backup** or task matches this capability

## Workflow

1. Identify artifact and target folder.
2. Run privacy-redactor on content if external.
3. Upload via connected service; confirm link.
4. Log path in semantic-memory-manager optional index.

## Integrations

- `connected-services-bridge`
- `privacy-redactor`
- `persistent-memory-bridge`

## Error Handling

| Failure | Response |
|---------|----------|
| Upload fail | Retry once; offer local save fallback. |

## Gotchas

- Large files: confirm with user before upload.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
