---
name: desktop-subagent-connector
description: "Securely bridges the remote Grok sandbox to the user's local desktop for scoped file access, approved shell execution, GUI/browser automation, and local sub-agent work. Use for: remote sandbox, user's real machine, List, Read."
version: 1.0.0
author: Stijnman
license: MIT
---
# Desktop Subagent Connector
## Overview

Bridges the **remote sandbox** to the **user's real machine**. The sandbox never gets raw network access to the user's LAN. Instead the user runs a small local daemon and exposes it via an outbound tunnel (cloudflared recommended). All calls are authenticated with a shared token and confined to allowed directory roots.

This is the concrete path for:
- Reading/writing files on the user's desktop
- Running approved local commands (ffmpeg, licensed tools, etc.)
- Optional browser control on the user's machine (Playwright or alongside Kimi WebBridge)
- Geo-restricted or login-session work that the remote sandbox cannot do alone

## Prerequisites (user side)

- Python 3.9+
- Optional but strongly recommended: `cloudflared` (makes the public URL automatic)
- Optional for browser control: `pip install playwright && playwright install chromium`

## Easy setup (recommended)

### macOS / Linux

1. Get the skill scripts folder (or at least `local-daemon.py` + `setup.sh`) onto your machine.
2. Run:

```bash
cd /path/to/desktop-subagent-connector/scripts
bash setup.sh
```

That single command:
- creates `~/desktop-subagent`
- generates a strong token
- starts the local daemon
- starts `cloudflared` if installed
- prints a ready-to-paste block:

```
DESKTOP_BRIDGE_URL=https://xxxx.trycloudflare.com
DESKTOP_BRIDGE_TOKEN=...
```

Paste that block back to the agent. Leave the terminal open (Ctrl+C stops everything).

If `cloudflared` is missing:
```bash
# macOS
brew install cloudflared
# then re-run setup.sh
```

### Windows (PowerShell)

```powershell
cd path\to\desktop-subagent-connector\scripts
powershell -ExecutionPolicy Bypass -File setup.ps1
```

Install cloudflared if needed: `winget install --id Cloudflare.cloudflared`

### Manual (no setup script)

```bash
python3 local-daemon.py          # auto-generates token if none given
cloudflared tunnel --url http://127.0.0.1:8765
```

Then paste URL + token to the agent.

Full protocol and security model: `references/local-component-spec.md`.

## Agent-side instructions (this skill)

### 1. Connection check
When the user supplies `DESKTOP_BRIDGE_URL` + `DESKTOP_BRIDGE_TOKEN` (or they are present in env / memory):

```bash
curl -sS -H "Authorization: Bearer $DESKTOP_BRIDGE_TOKEN" "$DESKTOP_BRIDGE_URL/health"
```

Expect JSON with `"status":"ok"` and a `capabilities` list. If this fails → tell the user the tunnel/daemon is down and stop.

### 2. File operations
- **List**: `GET /file/list?path=<abs-or-home-relative>`
- **Read**: `POST /file/read` body `{"path":"..."}` → utf-8 text or base64
- **Write**: `POST /file/write` body `{"path","content","encoding?":"utf-8|base64"}`

Always confirm destructive or large writes with the user first. Respect the daemon's path confinement (default = `$HOME` + any `--allow-root` the user set).

### 3. Local execution
`POST /exec` body `{"command":"...","timeout?":30,"cwd?"}`.  
Dangerous patterns are blocked by the daemon unless the user set `DESKTOP_BRIDGE_UNSAFE=1`. Still prefer explicit, minimal commands. Capture stdout/stderr and returncode.

### 4. Browser / GUI (optional)
If Playwright is installed on the user machine the daemon exposes:
- `POST /browser/navigate` → title + body text
- `POST /browser/screenshot` → base64 PNG
- `POST /browser/evaluate` → JS result

Use this when the remote sandbox browser is blocked (geo, login walls, CAPTCHA that needs a real profile). Prefer local browser for Belgian geo-restricted sites when the user is in Belgium.

If the user also runs Kimi WebBridge, treat the two as complementary: WebBridge drives their everyday Chrome profile via CDP; this daemon gives the *remote* agent a simple HTTP path without requiring WebBridge's agent pairing.

### 5. Permission & audit
- Ask for explicit permission the first time in a session (and again for broader scopes).
- Never exfiltrate whole home directories or secrets without a clear user request.
- Daemon writes `~/.desktop-subagent/audit.log` on the user machine — mention this if they ask for auditability.
- On "disconnect desktop" or token revoke → stop calling the URL immediately.

### 6. Error handling
- 401 → token wrong / missing
- 403 → path outside allowed roots or blocked command
- 501 → Playwright not installed (browser endpoints)
- Connection refused / tunnel dead → fall back to pure sandbox tools and tell the user

Retry transient network errors with exp backoff (10s / 30s / 60s ±25%).

### 7. Persistence of connection info
When the user successfully pairs, optionally store `DESKTOP_BRIDGE_URL` + token hint (not the raw token if possible) via persistent-memory-bridge for the session, and remind them that cloudflared quick tunnels are temporary.

## Integration
- Partners: computer-use-bridge (sandbox side), connected-services-bridge, drive-persistence-bridge, persistent-memory-bridge
- Browser alternatives: sandbox `browser_tab` tool first; escalate to this local bridge only when local identity / geo is required
- Logs: evolution_log.md + user-side audit.log

## Version
1.7.0 — 2026-08-14  
Easy setup: `scripts/setup.sh` (macOS/Linux) and `scripts/setup.ps1` (Windows) start daemon + cloudflared and print a ready-to-paste block. Daemon auto-generates token if none provided. Manual path still works.
