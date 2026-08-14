---
name: hybrid-execution-bridge
description: Unified execution hub that routes work across sandbox computer-use, local desktop via cloudflared tunnel, connected services, stealth browsing, and controlled internet. Creates new skills on demand via natural-language-to-skill. Triggered by hybrid execution, tunnel bridge, unified bridge, local plus sandbox, stealth browse with persistence, or when a task needs mixed local remote and cloud capabilities. Optimized for accurate LLM routing.
---

# Hybrid Execution Bridge

## Overview

Single entry point that fuses:

| Component skill | Role in the fusion |
|-----------------|-------------------|
| **computer-use-bridge** | Sandbox shell, packages, files, code |
| **desktop-subagent-connector** | User machine via cloudflared tunnel + local daemon |
| **connected-services-bridge** | Drive, GitHub, Gmail, Calendar, Notion, etc. |
| **internet-enabler** / sandbox-internet-handler | Controlled external HTTP when sandbox is restricted |
| **humanization-stealth-browsing** | Anti-bot browsing patterns for hard sites |
| **natural-language-to-skill** | Spawn new skills when a gap appears mid-task |

Emergent capability: decide *where* each sub-step runs (sandbox vs local desktop vs pure API) and keep persistence + audit consistent.

## Routing Rules (decision order)

1. **Local desktop required?**  
   Login sessions, geo-fence (e.g. Belgium), licensed local software, heavy GUI, or user said "on my machine"  
   → `desktop-subagent-connector` (check `DESKTOP_BRIDGE_URL` + token; if missing, run easy setup instructions).

2. **Sandbox compute enough?**  
   Code, packages, artifacts, ffmpeg, pdf, etc.  
   → `computer-use-bridge`.

3. **External data / live web?**  
   - Soft sites → built-in browser tools + `internet-enabler`.  
   - Hard / anti-bot sites → `humanization-stealth-browsing` (optionally through local browser if tunnel is up).

4. **Persist or talk to SaaS?**  
   Always prefer `connected-services-bridge` for Drive/GitHub uploads, issues, calendar, mail.

5. **Capability gap mid-flight?**  
   → `natural-language-to-skill` + Persistence Contract (Local + Drive + GitHub).

Never claim local desktop access unless the tunnel health check succeeds.

## Tunnel path (desktop-subagent)

Easy setup the user runs once per session:

```bash
cd …/desktop-subagent-connector/scripts && bash setup.sh
```

Paste back:

```
DESKTOP_BRIDGE_URL=https://….trycloudflare.com
DESKTOP_BRIDGE_TOKEN=…
```

Then this skill:

```bash
curl -sS -H "Authorization: Bearer $DESKTOP_BRIDGE_TOKEN" "$DESKTOP_BRIDGE_URL/health"
```

Security notes (quick tunnels):
- URL is public; **token is the lock**.
- Short sessions only; kill tunnel when done.
- For longer/sensitive use: named Cloudflare Tunnel + Access in front of the daemon.

## Standard workflow

1. Parse goal → decompose into local / sandbox / cloud / web steps.
2. Health-check whatever bridges are needed (tunnel, connected tools, internet).
3. Execute in parallel where safe.
4. Aggregate results into artifacts/.
5. Persist important outputs via connected-services-bridge (Drive folder `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK`, GitHub `Stijnman/grok-custom-skills` when skills change).
6. If a reusable procedure appeared → natural-language-to-skill → full Persistence Contract.

## Error handling

- Tunnel down / 401 → fall back to sandbox-only; tell user how to re-run `setup.sh`.
- Internet blocked → internet-enabler / sandbox-internet-handler first; then retry.
- Stealth browse fails → escalate to local browser via tunnel if available.
- Exp backoff + jitter (10s / 30s / 60s ±25%) on transient failures.
- Log bridge choices and outcomes to evolution_log.md.

## When to activate

- "Use hybrid bridge", "tunnel + sandbox", "local and cloud together"
- Tasks that mix file access on user PC with sandbox processing and Drive upload
- Geo-restricted or login-walled browsing
- "Combine computer-use, desktop, connected services, stealth browse"
- Any request that previously would have required manually juggling those skills

## Anti-patterns

- Do not expose `/exec` on the local daemon without a strong token and user consent.
- Do not leave quick tunnels running unattended.
- Do not invent local results when the tunnel is down.
- Do not skip Persistence Contract when creating skills through this hub.

## Version
1.0.0 — 2026-08-14  
Initial fusion of connected-services-bridge + computer-use-bridge + desktop-subagent-connector (tunnel) + humanization-stealth-browsing + internet-enabler + natural-language-to-skill.
