---
name: drive-persistence-bridge
description: "Creates, verifies, restores, or synchronizes user-approved backups and artifacts with connected cloud storage or a repository. Use for: backing up files, preparing a restore, comparing versions, or uploading a specifically approved artifact."
license: MIT
---

# Drive Persistence Bridge

Use this skill to preserve named artifacts safely across local storage and an approved remote destination. It supports backup preparation, version comparison, restore planning, and approved uploads; it does **not** authorize autonomous synchronization or publication.

## Workflow

1. Confirm the source files, destination service and folder or repository, retention expectation, and whether the request is local-only, upload, restore, or comparison.
2. Inspect available connector capabilities and permissions. Use read-only discovery first; do not assume a destination, branch, folder, account, or tool schema.
3. Build a local, timestamped artifact with a clear name. Record its checksum, source scope, creation time, and a concise description. Exclude secrets, credentials, cache directories, and unnecessary personal data.
4. For a remote upload, repository commit or push, restoration that overwrites files, retention cleanup, or deletion, present a preview of the exact targets and changes. Obtain explicit user approval before proceeding.
5. Execute only the approved operation with least privilege. Verify the returned identifier, link, commit reference, or checksum.
6. Report what completed, where it was stored, how to restore it, and any failed steps. Keep local artifacts intact when a remote operation fails.

## Restore and Version Comparison

List available versions with dates, checksums, sizes, and source descriptions. Compare candidate versions before restoration and use a dry run where available. Require approval before overwriting local or remote data, and preserve a rollback copy before any approved overwrite.

## Reliability

Retry only idempotent, transiently failed operations a small bounded number of times. Stop for authentication, permission, conflict, or capability failures; explain the blocker and offer a local export or manual-upload alternative. Never claim a remote backup, sync, commit, or restore succeeded without verified evidence.

## Safety & Ethics

### Required approvals

Require explicit approval for all remote uploads, repository commits or pushes, background scheduling, bidirectional synchronization, retention changes, restoration that overwrites data, and every deletion. A request to create a backup does not itself authorize publishing it to a remote service.

### Prohibited actions

- Do not run automatic, event-driven, background, or recurring syncs without the user's specific approval.
- Do not infer a remote destination, repository, branch, storage folder, or retention policy from prior context.
- Do not delete duplicate files, prune backups, overwrite data, or resolve conflicts automatically.
- Do not expose or store access tokens, credentials, private paths, or personal data in artifacts or logs.
- Do not bypass authentication, service permissions, access controls, CAPTCHAs, or platform safeguards.
