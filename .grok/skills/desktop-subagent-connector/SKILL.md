---
name: desktop-subagent-connector
description: "Securely bridges the 4-agent ecosystem to the user's local desktop for controlled file access, local script execution, GUI automation, and sub-agent spawning. Maintains strict sandboxing and permission model. Triggered by 'connect to desktop', 'local file access', 'run locally', or 'access my files safely'. Enables heavy local computation without uploading sensitive data. Optimized for accurate LLM routing."
---

# Desktop Subagent Connector

## Overview

This skill establishes a secure, auditable bridge between the cloud-based 4-agent ecosystem and the user's local desktop. It allows safe reading/writing of local files, execution of user-approved scripts, limited GUI interaction, and spawning of lightweight local sub-agents while respecting privacy and security boundaries.

## Instructions

1. **Connection Establishment**
   - Request explicit user permission for each new session or sensitive operation.
   - Establish encrypted tunnel (via connected-services-bridge or secure protocol).
   - Negotiate permission scope: read-only, read-write specific folders, execute whitelist, GUI allowed.

2. **File Operations**
   - List, read, write, move, delete local files/folders within approved scope.
   - Sync selected files bidirectionally with artifacts/ or drive-persistence-bridge.
   - Handle large files via streaming/chunking to avoid memory issues.

3. **Local Execution**
   - Run user-approved bash/Python/scripts locally with timeout and output capture.
   - Support "local mode" for skills that benefit from native hardware (e.g., heavy video processing via ffmpeg local).
   - Return results + logs to main ecosystem.

4. **Sub-Agent Spawning**
   - Launch isolated local sub-agents for parallel work (e.g., background watcher, heavy computation).
   - Monitor sub-agent health and auto-restart on failure.
   - Aggregate outputs back to Master Agent.

4b. **Local Browser / GUI Control** (reinforced 2026-08-14)
   - When user is in Belgium (or has Belgian IP/proxy), use local browser for geo-restricted sites (e.g. RingTwice).
   - Support controlled navigation, form filling, screenshot capture, and limited interaction under explicit permission.
   - Prefer local browser when remote sandbox is blocked by geo-fences.

5. **Security & Audit**
   - All operations logged with timestamp, action, and result.
   - Automatic sandboxing: No access outside whitelisted paths.
   - Immediate disconnect on any suspicious activity or user command "disconnect desktop".
   - Never store or transmit local file contents without explicit user approval.

**When to Use**
- User requests processing of local files or "do this on my computer".
- When cloud tools are insufficient (special hardware, licensed local software).
- For privacy-sensitive workflows where data should not leave the device.
- During long-running local tasks that benefit from sub-agent delegation.
- For geo-restricted websites that the remote sandbox cannot access properly.

**Examples**
- "Connect to my desktop and process all PDFs in Downloads folder": Establishes bridge → lists files → runs local pdf skill on each → returns structured results + updated local copies.
- "Spawn local sub-agent to watch folder for new images and auto-analyze": Persistent local watcher running in background.
- "Use local browser for RingTwice": Opens Belgian browser session to bypass geo-modal.

**Error Handling**
- Permission denied or connection lost: Gracefully degrade to cloud-only mode and notify user.
- Local execution timeout or crash: Kill sub-process, log, offer retry with reduced scope.
- Always confirm destructive actions ("delete 47 files?") with user.

**Integration**
- Primary partners: connected-services-bridge, sandbox-internet-handler, computer-use-bridge, drive-persistence-bridge.
- Works with: pdf, ffmpeg, any local-heavy skill.
- Logs to: evolution_log.md + local audit file.

**Version:** 1.5 — 2026-08-14  
Prepared and reinforced for active use. Added explicit support for local browser control / GUI automation (useful for geo-restricted sites such as RingTwice) and aligned with current Persistence Contract.
