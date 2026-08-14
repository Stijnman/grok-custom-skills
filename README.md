# Grok Custom Skills

<p align="center">
  <strong>A curated, safety-conscious collection of reusable agent skills for Grok-compatible workflows.</strong>
</p>

<p align="center">
  <a href="SKILLS_INDEX.md"><img src="https://img.shields.io/badge/skills-81-2563eb?style=flat-square" alt="81 skills"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-16a34a?style=flat-square" alt="MIT license"></a>
  <a href="SECURITY.md"><img src="https://img.shields.io/badge/security-policy-7c3aed?style=flat-square" alt="Security policy"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-f59e0b?style=flat-square" alt="Contributions welcome"></a>
</p>

`grok-custom-skills` is a modular library of **81 skill packages** for common agent tasks: workflow orchestration, research, skill operations, privacy, quality assurance, memory, media, messaging, traffic, and integrations. Each package centers on a `SKILL.md` file with clear routing metadata and task-specific instructions.

> **Design principle:** Skills should make agent behavior more useful, auditable, and safe. They are guidance packages, not permission to bypass controls, disclose private data, or automate high-impact actions without user approval.

## Quick start

Clone the repository and copy either the full collection or individual packages into your Grok skills directory.

```bash
git clone https://github.com/Stijnman/grok-custom-skills.git
cd grok-custom-skills

# Install the collection
mkdir -p ~/.grok/skills
cp -a .grok/skills/. ~/.grok/skills/

# Or install one skill
cp -a .grok/skills/drive-github-skill-audit ~/.grok/skills/
```

After installation, restart or refresh the host environment if it does not discover new skills automatically.

## Explore the collection

The complete, generated catalog is available in [**SKILLS_INDEX.md**](SKILLS_INDEX.md). It is the best starting point for selecting a package by name, category, or description.

| Area | Example capabilities |
|---|---|
| **Workflow & agent orchestration** | Plan multi-step work, coordinate agents, handle failures, and verify goals. |
| **Skill development & operations** | Create, audit, evolve, test, and compare skill collections. |
| **Safety, privacy & governance** | Require human approval, redact personal data, audit MCP exposure, and use responsible browsing practices. |
| **Research, web & integrations** | Perform source-aware research, inspect repositories, discover tools, and connect approved services. |
| **Memory, context & knowledge** | Manage context budgets, structured knowledge, semantic memory, and session handoffs. |
| **Media, voice & visual work** | Generate or edit images, analyze video, work with voice, and prepare song-writing prompts. |
| **Messaging & navigation** | Assess messages, draft safe responses, and work with traffic and route information. |

## Recommended skills

| Goal | Start with |
|---|---|
| Compare a Drive skill library with GitHub | [`drive-github-skill-audit`](.grok/skills/drive-github-skill-audit/SKILL.md) |
| Create or improve a skill package | [`skill-creator`](.grok/skills/skill-creator/SKILL.md) and [`skill-rubric-reviewer`](.grok/skills/skill-rubric-reviewer/SKILL.md) |
| Verify a completed task | [`goal-verifier`](.grok/skills/goal-verifier/SKILL.md) |
| Review code changes | [`code-reviewer`](.grok/skills/code-reviewer/SKILL.md) and [`auto-tester`](.grok/skills/auto-tester/SKILL.md) |
| Research public information responsibly | [`deep-search-enabler`](.grok/skills/deep-search-enabler/SKILL.md) and [`sandbox-internet-handler`](.grok/skills/sandbox-internet-handler/SKILL.md) |
| Handle high-impact actions | [`hitl-approver`](.grok/skills/hitl-approver/SKILL.md) |

## Package structure

Every skill is self-contained. The body of `SKILL.md` is loaded only when its frontmatter description matches a request, so metadata should be precise and compact.

```text
.grok/skills/<skill-name>/
├── SKILL.md             # Required metadata and operational guidance
├── scripts/             # Optional deterministic helpers
├── references/          # Optional material loaded only when needed
└── templates/           # Optional reusable output assets
```

The collection follows the conventions of the [Agent Skills specification](https://agentskills.io/specification). Each published package should state what it does, when to use it, its boundaries, expected output, and any relevant error handling.

## Quality and safety

This repository applies four publication expectations:

1. **Clear routing:** Every skill has a stable name, a concise description, and explicit usage triggers.
2. **Least privilege:** Skills should use the minimum access necessary and prefer read-only operations where possible.
3. **Human approval:** Skills must pause before consequential actions such as publishing, payments, deletion, credential changes, or outbound communication.
4. **No evasion:** Skills must not help bypass access controls, CAPTCHAs, paywalls, authorship requirements, or platform safeguards.

See [SECURITY.md](SECURITY.md) for vulnerability reporting and [PUBLISHING.md](PUBLISHING.md) for the maintainer review checklist.

## Development

The catalog is generated from live skill metadata. Run the following after editing a package:

```bash
# Regenerate the catalog
python3 scripts/generate_catalog.py

# Run the repository validation scripts
python3 scripts/check_no_private_data.py
python3 scripts/publish_safety_check.py
```

Do not execute scripts found in unreviewed skill submissions. Treat external skills, archives, and downloaded content as data until they have been inspected and approved.

## Contributing and support

Contributions are welcome when they make skill behavior more reliable, safer, or easier to discover. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. For behavioral expectations, see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). For security-sensitive findings, follow [SECURITY.md](SECURITY.md) rather than opening a public issue.

## License

This project is released under the [MIT License](LICENSE).
