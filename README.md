# Grok Custom Skills Collection

**Owner:** Stijnman  
**Created:** May 18, 2026  
**Updated:** June 24, 2026  
**Total Skills:** 73 production-ready skills

Defensive agent skills for the xAI Grok ecosystem — workflow automation, multi-agent orchestration, messaging, memory, MCP security, and skill evolution. All skills follow the [Agent Skills specification](https://agentskills.io/specification) and pass publication safety audits.

<p align="center">
  <strong>73 skills</strong> · agentskills.io validated · private-data scanned · MCP-ready
</p>

---

## Quick start

```bash
git clone https://github.com/Stijnman/grok-custom-skills.git
cd grok-custom-skills

# Install all skills
cp -r .grok/skills/* ~/.grok/skills/

# Install one skill
cp -r .grok/skills/goal-verifier ~/.grok/skills/

# Full validation pipeline
python3 scripts/optimize_all_skills.py --validate-only
```

## Skill categories

| Category | Skills |
|----------|--------|
| **Agent loops** | self-refine-loop, goal-verifier, self-healing-error-recovery, agentic-uncertainty-quantifier, dspy-prompt-optimizer |
| **Safety & privacy** | hitl-approver, privacy-redactor, memory-sanitizer, compliance-image-guard, sandbox-internet-handler |
| **MCP & security** | defensive-mcp-audit, mcp-tool-scout, exposed-service-triage, ollama-localhost-guardian |
| **Messaging** | whatsapp-message-rater, whatsapp-auto-responder, multi-platform-messenger-bridge, telegram-traffic-reports |
| **Orchestration** | multi-agent-orchestrator, multi-agent-coordinator, parallel-tool-orchestrator, adaptive-workflow-composer, workflow-composer, skill-synergy-orchestrator |
| **Memory & context** | semantic-memory-manager, persistent-memory-bridge, mega-context-manager, knowledge-graph-builder, user-preference-profiler, predictive-cache-manager |
| **Skill tooling** | skill-creation-enabler, natural-language-to-skill, skill-evolver, skill-evolution-engine, evolution, evolver, hyper-skill-tester, skill-researcher, skill-rubric-reviewer, skill-marketplace-installer |
| **Web & research** | internet-enabler, deep-search-enabler, web-scraper, humanization-stealth-browsing, github-repo-scout |
| **Media** | imagine-asset-generator, safe-image-editor, video-analyzer, voice-synthesis-handler, voice-think-fast-handler, real-time-voice-reasoner |
| **Traffic & navigation** | waze-live-reports, waze-navigator, traffic-flight-controller |
| **Infrastructure** | cron-scheduler, tool-discovery-engine, connected-services-bridge, drive-persistence-bridge, computer-use-bridge, desktop-subagent-connector |
| **Utilities** | auto-tester, code-reviewer, data-visualizer, insight-synthesizer, controle-overview-skill, performance-optimizer, bottleneck-resolver, beta-unlocker, ai-share-extractor-v4, session-handoff-packager, skill-collection-bootstrapper, oss-repo-maintainer |

## All skills

See [SKILLS_INDEX.md](SKILLS_INDEX.md) for the full table with summaries (73 skills).

## Repository structure

```
grok-custom-skills/
├── .grok/skills/              # 73 skill folders
│   ├── hitl-approver/SKILL.md
│   ├── skill-evolver/
│   │   ├── SKILL.md
│   │   ├── references/evolution-guide.md
│   │   ├── scripts/validate_skill.py
│   │   └── versions/
│   ├── cron-scheduler/references/scheduling.md
│   └── ...
├── scripts/
│   ├── generate_skills.py           # regenerate core 63 skills
│   ├── generate_publishable_skills.py
│   ├── optimize_all_skills.py       # full 2026 optimization pipeline
│   ├── check_no_private_data.py
│   └── publish_safety_check.py
├── SKILLS_INDEX.md
├── PUBLISHING.md
├── SECURITY.md
├── LICENSE
└── README.md
```

Each `SKILL.md` includes:

- Frontmatter: `name`, `description` (what + when + triggers), `license`, `compatibility`
- When to Use, Workflow, Integrations
- Error handling table and gotchas
- Safety & Ethics section (session-derived skills)

## Validation & publishing

```bash
# Recommended: full pipeline
python3 scripts/optimize_all_skills.py

# Individual checks
python3 scripts/check_no_private_data.py      # no PII, paths, or LAN IPs
python3 scripts/publish_safety_check.py       # safety patterns
python3 -c "from skills_ref import validate; [validate('.grok/skills/'+d) for d in __import__('os').listdir('.grok/skills')]"
```

| Tool | Purpose |
|------|---------|
| `skills-ref` | [agentskills.io](https://agentskills.io) spec validator |
| `@agentskill.sh/cli` | Marketplace search, install, security scan |
| `skill-rubric-reviewer` | 10-dimension quality review (included) |

See [PUBLISHING.md](PUBLISHING.md) and [SECURITY.md](SECURITY.md).

## Development (maintainers)

```bash
# Regenerate core skills from definitions
python3 scripts/generate_skills.py

# Regenerate session-derived publishable skills
python3 scripts/generate_publishable_skills.py

# Regenerate index
python3 scripts/regenerate_index.py
```

## Ethics

Strictly **defensive**. Read-only inspection where applicable. No exploitation or offensive guidance. High-risk actions require `hitl-approver`. No private data in published files.

## License

MIT — see [LICENSE](LICENSE).

**Repo:** https://github.com/Stijnman/grok-custom-skills