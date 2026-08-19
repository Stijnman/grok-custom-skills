---
name: connected-services-bridge
description: "Discovers, orchestrates, and executes actions across Grok's connected services (Google Drive, Notion, Linear, Google Calendar, GitHub, SharePoint, Outlook) using search_connected_tools and call_connected_tool. Enables seamless file sync, data automation, calendar management, and cross-platform workflows. Triggered by 'save to Google Drive', 'update Notion', 'create GitHub issue', 'sync calendar', or any external service task. Mandatory first step for persistent storage or external actions. Produces versioned, auditable outputs. Optimized for accurate LLM routing. Enhanced with exp backoff+jitter (10/30/60s ±25%) and sandbox awareness. Version 1.18 (MINOR) 2026-08-19: auto-push contract for project updates (Pulverise → Stijnman/pulverise private + Drive) in addition to skills; pairs with drive-persistence-bridge §0 Auto-Push Contract."
---

# Connected Services Bridge

## Overview

Provides unified access to Grok's 2026 connected services ecosystem (Google Drive for file persistence, Notion/Linear for project tracking, Google Calendar/Outlook for scheduling, GitHub for code repos, SharePoint for enterprise docs). Uses search_connected_tools to discover exact tool schemas (e.g., google_drive_write_file, google_drive_upload_artifact, google_drive_search) then executes via call_connected_tool. Ensures all skill outputs (documents, images, logs) are auto-persisted and versioned.

## Instructions

- Always start external tasks with: Call search_connected_tools with query describing needed action (e.g., 'search pages', 'create issue', 'list files', 'read email', 'calendar events', 'query database') to get precise tool_name and argument schema.
- For Google Drive (priority per ecosystem protocol): Use discovered tools to upload artifacts (e.g., generated images, SKILL.md updates, reports), create folders, search files, read/write content; maintain Grok_Ecosystem_Skills/ directory for all new modules.
- Workflow: 1) Discover tool, 2) Validate args against schema, 3) Execute call_connected_tool, 4) Log result + link in shared memory, 5) Notify Master on success/failure.
- Cross-service automation: Sync research findings (deep-search-enabler) to Notion pages; schedule follow-ups in Calendar via connected events; push code outputs to GitHub repos; update Linear issues from Execution Agent results.
- Error handling: If tool unavailable, fallback to local artifacts/ + manual upload instructions; escalate to multi-agent-orchestrator for alternative strategies.
- Security: Enforce least-privilege (read-only unless write explicitly requested); audit all calls in evolution_log.md; never expose credentials.
- Integration: Auto-trigger on skill creation (e.g., new SKILL.md -> upload to Drive); combine with imagine-asset-generator to store visuals; use with voice-synthesis-handler for audio asset management.
- **Skill + Project Persistence Support (Mandatory when relevant)**: After any new skill creation, significant evolution, **or project version bump** (e.g. Pulverise), execute or assist with: (1) dated tar.gz packaging, (2) `google_drive_upload_artifact` (skills → folder ID `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK`; projects → same or project subfolder), (3) GitHub push via `github___push_files` / `github___create_or_update_file` — skills → `Stijnman/grok-custom-skills` path `.grok/skills/<name>/…`; projects → `Stijnman/pulverise` (or the known private repo). Use current date in filenames and relative artifact paths only. Log results to evolution_log.md. Driven by drive-persistence-bridge §0 Auto-Push Contract — no extra user command required.
- Optimization: Cache service schemas in tool_registry.json; predictive pre-fetch for frequent actions (e.g., daily Drive sync); batch operations for efficiency.


## Evolution Update (2026-05-27)
- Added structured error handling and retry logic.
- Enhanced integration with parallel-tool-orchestrator.
- Improved meta-reflection for better ROI tracking.
- Version bumped to 1.3


## Auto-Evolution Patch (2026-05-31): Added general robustness note and version tracking.

## Autonomous Evolution Cycle (2026-06-07)
- Added jittered backoff retry logic to connected services discovery, tool calls (Drive, Notion, Calendar, GitHub), and orchestration.
- Included sandbox-aware connection handling and fallback modes.
- Version bumped to 1.4.
- Key: Enables reliable external integrations during full skill library evolution and uploads.
  - 2026-07-20 Library Evolution: Added/strengthened exp backoff+jitter error handling, sandbox awareness, transparent reporting. Version MINOR bump.
