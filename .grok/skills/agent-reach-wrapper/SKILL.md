---
name: agent-reach-wrapper
description: Thin wrapper around Panniantong/Agent-Reach for live web, YouTube transcripts, RSS, GitHub, Bilibili, Exa search, and optional login-state platforms (X, Reddit, Facebook, Instagram, Xiaohongshu, LinkedIn). Triggered by agent-reach, reach this URL, YouTube transcript, Reddit thread, Bilibili, Xiaohongshu, RSS feed, or give the agent eyes. Does not replace VintedListingAnalyzer or humanization-stealth-browsing. Doctor-first. Never run install --system unless the user explicitly allows machine changes. Cookies stay local and never go in the skill repo.
license: MIT
metadata:
  version: "1.0"
  type: integration
  upstream: https://github.com/Panniantong/Agent-Reach
  owner: Stijnman
  created: "2026-08-28"
---

# Agent Reach Wrapper

Capability layer over [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach). Routes a request to the current working backend. You do not scrape those platforms yourself when the CLI is healthy.

## Do not

- Do not treat this as a Vinted tool. Vinted stays `VintedListingAnalyzer` + `humanization-stealth-browsing`.
- Do not run `agent-reach install --system` unless the user explicitly says to modify the machine.
- Do not put cookies, tokens, or `~/.agent-reach/config.yaml` into git, Drive, or this skill directory.
- Do not use a main personal account for X / Reddit / IG / Xiaohongshu cookie backends. Throwaways only.
- Do not `pip install agent-reach` from PyPI. That package is not this project. Install from the GitHub repo only.

## Routing

| Need | Platform key | Default path | Fallback if CLI missing |
|---|---|---|---|
| Read a page | web | Jina Reader via Reach | `browse_page` or `https://r.jina.ai/URL` |
| YouTube talk track | youtube | yt-dlp via Reach | `browse_page` on the watch page; no fake transcript |
| RSS / Atom | rss | feedparser via Reach | fetch + parse if available |
| Public GitHub | github | `gh` via Reach | connected GitHub tools |
| Bilibili | bilibili | bili-cli | say blocked; do not invent |
| Semantic web search | search | Exa via mcporter | `web_search` |
| X / Twitter | twitter | twitter-cli / OpenCLI | built-in `x_keyword_search` / `x_semantic_search` first |
| Reddit | reddit | OpenCLI / rdt-cli | `browse_page` / search; anonymous API is dead |
| Facebook / Instagram / Xiaohongshu / LinkedIn deep | facebook / instagram / xhs / linkedin | OpenCLI or MCP after user login | public page via Jina / browse only |

## Workflow

1. Decide platform from the user request. If mixed (e.g. "summarize this YT and search X"), split into parallel calls.
2. Probe CLI
   ```bash
   command -v agent-reach && agent-reach doctor
   ```
   If `doctor` fails or the binary is missing, use the fallback column. Do not pretend Reach is installed.
3. If doctor shows the channel red, report the active/failed backend and the repair hint. Do not silently switch to a banned-account cookie flow.
4. Execute the smallest Reach command that answers the question. Prefer read/search over "configure".
5. Return clean structured output
   - source URL
   - platform + backend used (or fallback name)
   - extracted text / items
   - what failed
6. Retry with exp backoff + jitter on transient failures — 10s / 30s / 60s ±25%. After 3 failures, stop and report.

## Install plan (local machine, user must allow)

Safe check only

```bash
pip install "git+https://github.com/Panniantong/Agent-Reach.git"
agent-reach install --env=auto --dry-run
agent-reach doctor
```

System writes (skills dir, MCP, packages) only after explicit user OK

```bash
agent-reach install --env=auto --system
agent-reach doctor
```

Update

```
帮我更新 Agent Reach：https://raw.githubusercontent.com/Panniantong/Agent-Reach/main/docs/update.md
```

OpenClaw users need `tools.profile = coding` or the CLI cannot exec.

## Cookie / login channels

When the user asks to "configure Twitter/Reddit/XHS"

1. Warn about ban risk. Demand a dedicated account.
2. Let the user export cookies via Cookie-Editor themselves. Do not steal browser cookies.
3. Store only in `~/.agent-reach/config.yaml` (mode 600) on their machine.
4. Re-run `agent-reach doctor` and show which backend became active.

This sandbox usually cannot complete those login steps. Say so and fall back.

## Output contract

```
platform: youtube
backend: yt-dlp | fallback-browse
url: ...
status: ok | degraded | failed
notes: ...
content:
  ...
```

## Sibling skills

- Vinted listings / seller scoring → VintedListingAnalyzer + humanization-stealth-browsing
- Generic page scrape / image download → web-scraper
- Live X posts already in Grok tools → use those before Reach Twitter
- Connected GitHub → use `search_connected_tools` / `call_connected_tool` for Stijnman repos
