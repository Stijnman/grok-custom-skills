---
name: desktop-subagent-connector
description: Securely bridges the remote Grok sandbox to the user's local desktop for scoped file access, approved shell execution, GUI/browser automation, and local sub-agent work. Requires a local daemon the user runs on their machine plus an outbound tunnel. Triggered by connect to desktop, local file access, run locally, access my files safely, or when geo-restricted / login-required browser control is needed. Optimized for accurate LLM routing.
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

1. Python 3.9+
2. The daemon script from this skill: `scripts/local-daemon.py`
3. Optional but recommended: `cloudflared`
4. Optional for browser: `pip install playwright && playwright install chromium`

## One-time setup (user runs on their machine)

```bash
mkdir -p ~/desktop-subagent && cd ~/desktop-subagent
# obtain local-daemon.py (from skill scripts/ or artifacts)
export DESKTOP_BRIDGE_TOKEN=$(openssl rand -hex 24)
echo "TOKEN=$DESKTOP_BRIDGE_TOKEN"   # keep this secret

python3 local-daemon.py --token "$DESKTOP_BRIDGE_TOKEN" --port 8765
# other terminal:
cloudflared tunnel --url http://localhost:8765
```

Copy the printed `https://….trycloudflare.com` URL and the token. Tell the agent:

```
DESKTOP_BRIDGE_URL=https://xxxx.trycloudflare.com
DESKTOP_BRIDGE_TOKEN=...
```

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
1.6.0 — 2026-08-14  
Concrete local daemon + protocol + cloudflared pairing path. Replaces pure aspirational docs with a working user-side component.
