---
name: agent-reach-wrapper
description: Thin wrapper around Panniantong Agent-Reach so Grok can read YouTube, X, Reddit, Bilibili, Xiaohongshu, RSS, GitHub public pages, and Exa search without paying platform APIs. Triggered by Agent-Reach, agent reach, YouTube transcript, Reddit without API, Bilibili, Xiaohongshu, give the agent eyes, or live social read. Does not replace VintedListingAnalyzer, web-scraper, or humanization-stealth-browsing. Never stores cookies in the skill repo. Run doctor before any live call. Default install is check-only — never use --system unless the user explicitly allows machine writes.
metadata:
  type: integration
  version: "1.0"
  source: https://github.com/Panniantong/Agent-Reach
  owner: Stijnman
  created: "2026-08-28"
license: MIT
---

# Agent Reach Wrapper

## Overview

Route live-internet reads through Agent-Reach when Grok built-in tools are the wrong surface (YouTube transcripts, Bilibili, Xiaohongshu, Reddit after anonymous APIs died, X search that needs login-state, RSS). Keep Vinted work on Stijnman/VintedListingAnalyzer + humanization-stealth-browsing.

Upstream — https://github.com/Panniantong/Agent-Reach (MIT). This skill does not vendor their code.

## Hard rules

1. Run `agent-reach doctor` (or `doctor --json`) before the first live call in a session.
2. Never run `agent-reach install --system` unless the user explicitly authorizes writes to the machine.
3. Never commit cookies, tokens, or `~/.agent-reach/config.yaml` into skills, Drive dumps, or GitHub.
4. Login-state platforms (X, Reddit, Facebook, Instagram, Xiaohongshu) use throwaway accounts only.
5. Do not install the PyPI package named `agent-reach`. That is a different project. Install from the GitHub repo.
6. Do not use this skill for Vinted listing analysis. Use VintedListingAnalyzer.

## When to use vs when not to

Use this skill
- YouTube "what does this video say"
- Bilibili search or video detail
- Reddit / X / Xiaohongshu after built-in search is empty or blocked
- RSS ingest
- Exa-style semantic web search via their MCP path
- Public GitHub when `gh` is already the selected backend

Do not use this skill
- Vinted profiles, listings, stealth HTML download
- Anything already covered cleanly by Grok `web_search`, `x_keyword_search`, or connected GitHub tools
- Account creation, mass scraping, or multi-account farming

## Install posture (sandbox-aware)

Default, safe

```bash
# inspect only
agent-reach doctor
agent-reach install --env=auto --dry-run
```

If the binary is missing, tell the user the one-liner they can paste to their coding agent. Do not silently `--system` from this sandbox.

```
Install Agent Reach from https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
Do not use --system unless I say so.
```

OpenClaw note — exec must be enabled (`tools.profile = coding`) or the CLI never runs.

Retry failed doctor/install probes with exp backoff 10s / 30s / 60s ±25%. Report which backend `doctor` selected. Do not invent a healthy backend.

## Routing table

| Need | Preferred backend (current upstream default) | Fallback inside this ecosystem |
|---|---|---|
| Any public URL as readable text | Jina Reader via Agent-Reach web channel | `browse_page` / `web-scraper` |
| YouTube transcript + search | yt-dlp | `video-analyzer` if a local file exists |
| Bilibili | bili-cli | say blocked, do not resurrect yt-dlp for Bilibili |
| RSS / Atom | feedparser | `browse_page` on the feed URL |
| Semantic web search | Exa via mcporter | `web_search` + `deep-search-enabler` |
| Public GitHub | `gh` | connected `github___*` tools |
| X / Twitter beyond a single public post | twitter-cli then OpenCLI | `x_keyword_search` first |
| Reddit | OpenCLI then rdt-cli (login required) | `web_search` site-reddit.com |
| Xiaohongshu | OpenCLI then xiaohongshu-mcp | do not steal browser cookies |
| LinkedIn public page | Jina Reader | `web-scraper` + stealth skill |
| Vinted | OUT OF SCOPE | VintedListingAnalyzer + stealth downloader |

Exact commands live in `references/commands.md`.

## Execution pattern

1. Classify the request to a channel in the table.
2. If a first-party Grok tool already solves it cheaper, use that and stop.
3. If Agent-Reach is the right channel, check `command -v agent-reach`.
4. If missing — report install status, do not fake results.
5. If present — `agent-reach doctor --json` (or plain doctor). Record `active_backend`.
6. Call the upstream tool the doctor selected. Do not wrap output in extra fiction.
7. On 403 / 412 / empty — try the documented fallback backend once, then stop and say which path died.
8. Never persist credentials. Quote only public content.

## Output format

```
Channel: youtube
Backend: yt-dlp
Doctor: ok
Result: <transcript or structured extract>
Notes: <ban risk / missing login / next action>
```

## Security

Cookies belong only in `~/.agent-reach/config.yaml` mode 600 on the user's machine. This skill must not extract Chrome cookies, must not dump env tokens, and must not echo `TWITTER_AUTH_TOKEN` / `TWITTER_CT0`.

If the user asks to "just grab my logged-in session", refuse the grab and point them at Cookie-Editor export + throwaway account.

## Persistence

After any edit to this skill, push
- GitHub `Stijnman/grok-custom-skills` path `.grok/skills/agent-reach-wrapper/`
- Drive folder `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK` when a pack is built

Do not upload `~/.agent-reach/`.
