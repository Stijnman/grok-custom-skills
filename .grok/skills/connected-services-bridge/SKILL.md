---
name: connected-services-bridge
description: "Connects approved external services such as Drive, GitHub, Notion, calendars, SharePoint, and Outlook through their available connectors. Use for: discovering connected-service capabilities, preparing a scoped integration, or completing a user-approved external action."
license: MIT
---

# Connected Services Bridge

Use this skill to discover available connected-service capabilities and perform **scoped, user-authorized** actions across approved services.

## Workflow

1. Identify the requested service, data scope, intended action, and expected output. Ask a focused question if any of these are ambiguous.
2. Discover the relevant connector and inspect its documented operation and parameter schema. Do not assume tool names, permissions, or data locations.
3. Use the least-privileged operation that can satisfy the request. Prefer a read-only check before any write.
4. For a consequential action, present the target service, destination, affected files or records, and rollback option. Obtain explicit approval before creating, updating, sending, deleting, committing, or sharing anything.
5. Perform the approved action. Verify the returned identifier, link, or status without exposing credentials, tokens, or private content.
6. Report the result, the exact scope completed, and any local fallback artifact if the service was unavailable.

## Reliability

Retry only transient, idempotent operations and stop after a small bounded number of attempts. For unavailable connectors, permission errors, or ambiguous results, preserve the local work and explain the blocker rather than guessing or escalating privileges.

## Safety & Ethics

### Required approvals

Require explicit user approval before remote writes, outbound communication, repository pushes, calendar changes, retention changes, or deletion. Treat a request to prepare an artifact as distinct from authorization to upload or publish it.

### Prohibited actions

- Do not collect, reveal, store, or transmit credentials, tokens, or private data unnecessarily.
- Do not enable background synchronization, recurring jobs, or automatic cross-service actions without the user's specific approval.
- Do not bypass service permissions, authentication, access controls, CAPTCHAs, or platform safeguards.
- Do not silently create, update, share, delete, commit, or push remote content.
