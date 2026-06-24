# Publishing Checklist

Use before publishing this repo or individual skills to GitHub, agentskill.sh, or PyPI.

## No private data

```bash
python3 scripts/check_no_private_data.py   # 0 failures required
```

Must not appear in any tracked file:

- Personal emails (use GitHub `users.noreply.github.com` for git commits)
- Machine hostnames, usernames, or `/home/<user>/` paths
- Private LAN IPs (`192.168.x.x`, `10.x.x.x`)
- Session-specific audit results (your ports, processes, machine model)
- API keys, tokens, phone numbers, chat IDs

Use `~/.grok/skills/`, `workspace .grok/skills/`, or generic examples only.

**Git history:** if you cloned locally, logs may contain your hostname/email.
Before first public push, set:

```bash
git config user.email "YOUR_ID+YOUR_USER@users.noreply.github.com"
```

Rewrite history if a personal email was already pushed.

## Repository

- [ ] `check_no_private_data.py` passes
- [ ] `README.md` skill count matches `find .grok/skills -name SKILL.md | wc -l`
- [ ] `SKILLS_INDEX.md` generated and linked
- [ ] `SECURITY.md` present
- [ ] `LICENSE` is MIT (or compatible)
- [ ] No `.env`, tokens, or credentials in git history

## Per-skill (`SKILL.md`)

- [ ] Valid frontmatter: `name`, `description`, `license: MIT`
- [ ] `name` matches directory name (lowercase-hyphen)
- [ ] Description includes **what** + **when** + trigger keywords
- [ ] Numbered workflow with clear steps
- [ ] Error handling table
- [ ] **Safety & Ethics** section (publishable/session-derived skills)
- [ ] No silent POST/telemetry to external APIs
- [ ] No hardcoded `/home/<user>/` paths — use `~/.grok/skills/` or workspace-relative
- [ ] Destructive ops reference `hitl-approver`
- [ ] Third-party tools attributed (e.g. defensive-mcp-audit, agentskill.sh CLI)

## Automated validation (2026 toolchain)

```bash
# Full pipeline (recommended)
python3 scripts/optimize_all_skills.py

# Validate only (no description patches)
python3 scripts/optimize_all_skills.py --validate-only

# Individual checks
python3 scripts/check_no_private_data.py      # no PII/paths/IPs
python3 scripts/publish_safety_check.py       # safety patterns
python3 -c "from skills_ref import validate; validate('.grok/skills/hitl-approver')"  # agentskills.io spec
```

### External tools

| Tool | Purpose | Install |
|------|---------|---------|
| [skills-ref](https://agentskills.io/specification) | Official Agent Skills spec validator | `pip install skills-ref` |
| [@agentskill.sh/cli](https://agentskill.sh) v2.0.2 | Search, install, security-scan marketplace skills | `npx @agentskill.sh/cli` |
| `skill-rubric-reviewer` | 10-dimension local quality review | included in repo |
| [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Description trigger eval loop (Anthropic) | marketplace / clone |

Regenerate session skills: `python3 scripts/generate_publishable_skills.py`

## agentskill.sh submission

1. Run `skill-rubric-reviewer` — target 40+/50
2. Run `skill-marketplace-installer` security scan if available
3. Confirm MIT license in frontmatter
4. Do **not** include auto-feedback POST blocks from third-party skill templates

## Red flags (block publish)

- Instructions to exploit, scan, or attack remote systems
- Credential harvesting or token logging
- Auto-install without user consent
- Real-person image generation without compliance guard
- Claims of "100% security" or offensive capabilities