# Agent-Reach command cheat sheet

Upstream docs
- Install — https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
- Update — https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
- Repo — https://github.com/Panniantong/Agent-Reach

## Doctor

```bash
agent-reach doctor
agent-reach doctor --json
```

Treat doctor JSON `active_backend` as source of truth. Do not assume yt-dlp still works for Bilibili.

## Safe install / uninstall

```bash
agent-reach install --env=auto
agent-reach install --env=auto --dry-run
agent-reach install --env=auto --safe
# only with explicit user permission
agent-reach install --env=auto --system

agent-reach uninstall --dry-run
agent-reach uninstall --keep-config
```

## Typical upstream calls (agent invokes these after doctor)

Web
```bash
curl -fsSL "https://r.jina.ai/https://example.com"
```

YouTube
```bash
yt-dlp --skip-download --write-auto-sub --sub-lang en,nl,fr --print title URL
```

GitHub
```bash
gh repo view owner/repo
gh search repos "query"
```

RSS
```bash
python -c "import feedparser,sys; d=feedparser.parse(sys.argv[1]); print(d.feed.get('title'), len(d.entries))" FEED_URL
```

Bilibili — use bili-cli, not yt-dlp.

X / Reddit / Xiaohongshu — only after the user configured a throwaway login path. Prefer `agent-reach configure <channel>` guided by the user, never silent cookie injection.
