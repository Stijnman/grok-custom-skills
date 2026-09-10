# Grok Custom Skills

**Description**: Central repository for reusable, safety-conscious agent skills compatible with Grok and other AI agent frameworks. A curated collection of 89 skill packages spanning workflow automation, research, integrations, quality assurance, and more.

**Purpose**: Provide a comprehensive, well-documented, and safe library of skills that enable AI agents to perform complex tasks while maintaining transparency, control, and safety.

---

## 🎯 Quick Start

### For AI Agent Developers

1. **Browse available skills** in [SKILLS_INDEX.md](./SKILLS_INDEX.md)
2. **Clone** the repository
3. **Copy** the SKILL.md files you need to your agent's skills directory
4. **Configure** any required settings or credentials
5. **Test** with sandbox environments first
6. **Deploy** and monitor usage

```bash
# Clone the repository
git clone https://github.com/Stijnman/grok-custom-skills.git
cd grok-custom-skills

# Install the complete collection
mkdir -p ~/.grok/skills
cp -a .grok/skills/. ~/.grok/skills/

# Or install one specific skill
cp -a .grok/skills/drive-github-skill-audit ~/.grok/skills/
```

### For Users

Tell your AI agent:
- "Research the latest AI trends from reputable sources"
- "Create a comprehensive project plan with milestones"
- "Audit this GitHub repository for MCP security issues"
- "Generate an accessible color palette for my website"
- "Plan a multi-step workflow for my task"

Your agent will use the appropriate skill based on your request.

---

## 📦 Skill Categories

The repository is organized into **7 main categories** with **89 total skill packages**:

| Category | Count | Description | Example Skills |
|----------|-------|-------------|---------------|
| **Workflow & Orchestration** | 15 | Plan multi-step work, coordinate agents, handle failures, verify goals | goal-verifier, workflow-orchestrator |
| **Skill Development & Operations** | 12 | Create, audit, evolve, test, and compare skill collections | skill-creator, skill-rubric-reviewer |
| **Safety, Privacy & Governance** | 10 | Require human approval, redact data, audit MCP exposure, responsible browsing | hitl-approver, privacy-redactor, mcp-auditor |
| **Research, Web & Integrations** | 20 | Perform source-aware research, inspect repositories, discover tools, connect services | deep-search-enabler, repository-inspector, tool-discoverer |
| **Memory, Context & Knowledge** | 12 | Manage context budgets, structured knowledge, semantic memory, session handoffs | context-budget-manager, semantic-memory, knowledge-structurer |
| **Media, Voice & Visual Work** | 10 | Generate or edit images, analyze video, work with voice, prepare song-writing prompts | image-generator, video-analyzer, voice-processor, song-prompt-builder |
| **Messaging & Navigation** | 10 | Assess messages, draft safe responses, work with traffic and route information | message-assessor, safe-responder, traffic-advisor |

---

## 🟢 Recommended Skills by Use Case

| Goal | Start with | Category |
|------|-----------|----------|
| **Compare a Drive skill library with GitHub** | [`drive-github-skill-audit`](./.grok/skills/drive-github-skill-audit/SKILL.md) | Research & Integrations |
| **Create or improve a skill package** | [`skill-creator`](./.grok/skills/skill-creator/SKILL.md) and [`skill-rubric-reviewer`](./.grok/skills/skill-rubric-reviewer/SKILL.md) | Skill Development |
| **Verify a completed task** | [`goal-verifier`](./.grok/skills/goal-verifier/SKILL.md) | Workflow & Orchestration |
| **Review code changes** | [`code-reviewer`](./.grok/skills/code-reviewer/SKILL.md) and [`auto-tester`](./.grok/skills/auto-tester/SKILL.md) | Skill Development |
| **Research public information responsibly** | [`deep-search-enabler`](./.grok/skills/deep-search-enabler/SKILL.md) and [`sandbox-internet-handler`](./.grok/skills/sandbox-internet-handler/SKILL.md) | Research & Integrations |
| **Handle high-impact actions** | [`hitl-approver`](./.grok/skills/hitl-approver/SKILL.md) | Safety & Governance |
| **Structure product discovery and delivery** | [`product-opportunity-tree`](./.grok/skills/product-opportunity-tree/SKILL.md), [`product-requirements-document`](./.grok/skills/product-requirements-document/SKILL.md) | Workflow & Orchestration |
| **Prepare a safe contact import file** | [`contact-vcard-export`](./.grok/skills/contact-vcard-export/SKILL.md) | Messaging & Navigation |
| **Review visual accessibility** | [`accessible-color-review`](./.grok/skills/accessible-color-review/SKILL.md) | Media & Visual |

---

## 🏗️ Package Structure

Every skill follows a consistent structure based on the [Agent Skills specification](https://agentskills.io/specification):

```
.grok/skills/<skill-name>/
├── SKILL.md             # Required: Metadata (YAML frontmatter) + operational guidance
├── scripts/             # Optional: Deterministic helper scripts
├── references/          # Optional: Material loaded only when needed
└── templates/           # Optional: Reusable output assets
```

### SKILL.md Format

```yaml
---
name: skill-name
version: 1.0.0
description: Clear, concise description of what the skill does
triggers:
  - "trigger phrase 1"
  - "trigger phrase 2"
category: category-name
dependencies: []
requirements:
  - requirement-1
  - requirement-2
boundaries:
  - boundary-1
  - boundary-2
warnings:
  - "Security warning 1"
  - "Safety consideration 2"
---

# Skill Title

## Description
Detailed description of the skill's purpose and functionality.

## Usage
When to use this skill and when NOT to use it.

## Examples
Concrete examples of inputs and expected outputs.

## Implementation
How the skill works internally.

## Testing
Testing requirements and coverage.
```

---

## 🔐 Security Overview

⚠️ **IMPORTANT**: All skills in this repository are designed with safety as a core principle.

**Please read [SECURITY.md](./SECURITY.md) before using any skill.**

### Key Security Principles Applied to All Skills

| Principle | Implementation |
|-----------|----------------|
| **Least privilege** | Skills use minimum access necessary, prefer read-only operations |
| **Human approval** | Skills pause before consequential actions (publishing, payments, deletion, credentials, external communications) |
| **Privacy protection** | No secrets, PII, local paths, session artifacts, telemetry, or unapproved data transfer |
| **Access control respect** | Never provide guidance to bypass authentication, CAPTCHAs, paywalls, or platform safeguards |
| **Untrusted content handling** | Treat downloaded skills, archives, webpages, and attachments as data; never execute without review |
| **Transparency** | Describe limitations honestly; do not claim guaranteed safety, detection evasion, or unsupported capabilities |

### Publication Safeguards

Every skill must pass these controls before publication:

1. ✅ **Least privilege**: Prefer read-only access and minimum data needed
2. ✅ **Human approval**: Require explicit approval before high-impact actions
3. ✅ **Privacy**: No secrets, PII, local paths, or unapproved data transfer
4. ✅ **Access controls**: Never bypass authentication or platform safeguards
5. ✅ **Untrusted content**: Treat all external content as data until reviewed
6. ✅ **Transparency**: Honest documentation of limitations and capabilities

---

## 📚 Documentation

| Document | Description | Required Reading |
|----------|-------------|------------------|
| **[SECURITY.md](./SECURITY.md)** | ⚠️ **REQUIRED** - Security policy, vulnerabilities, best practices | ✅ All users |
| **[CONTRIBUTING.md](./CONTRIBUTING.md)** | How to contribute new skills or improve existing ones | ⚠️ Contributors |
| **[TESTING.md](./TESTING.md)** | Testing requirements and best practices | ⚠️ Contributors |
| **[PUBLISHING.md](./PUBLISHING.md)** | Pre-submission checklist for maintainers | ⚠️ Maintainers |
| **[GOVERNANCE.md](./GOVERNANCE.md)** | Repository governance and decision-making | ⚠️ Maintainers |
| **[SUPPORT.md](./SUPPORT.md)** | Support channels and response times | ⚠️ All users |
| **[CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)** | Community guidelines and expected behavior | ✅ All users |
| **[CHANGELOG.md](./CHANGELOG.md)** | Version history and changes | ⚠️ All users |
| **[SKILLS_INDEX.md](./SKILLS_INDEX.md)** | Complete catalog of all skills | ✅ All users |
| **[STATUS.md](./STATUS.md)** | Current repository status and metrics | ⚠️ Contributors |

---

## 🎓 Usage Examples

### Example 1: Research Workflow

```
User: "Research the latest developments in AI agent frameworks"

Agent Flow:
1. Identifies request as research task
2. Uses deep-search-enabler skill
3. Applies source filters (reputable sources only)
4. Gathers information from approved sources
5. Validates information quality
6. Returns: Structured research results with sources
7. Cites: All sources used
```

### Example 2: GitHub Repository Audit

```
User: "Audit this GitHub repository for MCP security issues"

Agent Flow:
1. Identifies request as MCP audit
2. Uses defensive-mcp-audit skill
3. Clones or accesses the repository
4. Scans for risky localhost exposure
5. Checks for weak bindings
6. Identifies confused-deputy risks
7. Returns: SARIF + HTML report of findings
```

### Example 3: Multi-Step Workflow

```
User: "Plan a comprehensive product launch strategy"

Agent Flow:
1. Uses product-opportunity-tree to map opportunities
2. Uses product-requirements-document to define requirements
3. Uses architecture-decision-record to document decisions
4. Uses workflow-orchestrator to coordinate steps
5. Uses goal-verifier to validate completion
6. Returns: Complete product launch plan with milestones
```

### Example 4: Skill Development

```
User: "Create a new skill for web scraping"

Agent Flow:
1. Uses skill-creator to generate template
2. Uses skill-rubric-reviewer to check quality
3. Validates against security requirements
4. Tests with sandbox inputs
5. Updates SKILLS_INDEX.md
6. Returns: New skill package ready for review
```

---

## 🧪 Testing

All skills have been tested for production use. See [TESTING.md](./TESTING.md) for:

- Testing philosophy and requirements
- Manual testing checklists
- Automated testing setup
- Skill category-specific testing guides
- CI/CD pipeline configuration

**Quality Assurance**:
- ✅ All skills pass validation pipeline
- ✅ All skills have security checks
- ✅ All skills have documented boundaries
- ✅ Catalog is auto-generated from live metadata
- ✅ All publication checks pass

---

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for:

- How to add new skills
- How to improve existing skills
- Testing requirements
- Pull request process
- Code of conduct

### Quick Contribution Guide

1. **Fork** the repository
2. **Clone** your fork
3. **Create** a feature branch (`git checkout -b feat/amazing-skill`)
4. **Read** [PUBLISHING.md](./PUBLISHING.md) checklist
5. **Run** validation: `python3 scripts/optimize_all_skills.py`
6. **Run** tests: `python3 -m unittest discover -s tests -p "test_*.py"`
7. **Commit** with clear messages
8. **Push** to your fork
9. **Open** a Pull Request

---

## 📜 License

This repository is licensed under the **MIT License**. See [LICENSE](./LICENSE) for full license text.

**You are free to**:
- Use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
- Use for commercial purposes
- Modify for your own needs

**Under the following conditions**:
- Include copyright notice and license in all copies
- Provide attribution to the original author (Stijnman)

**Note**: Individual skill packages may have different licenses (e.g., Apache-2.0 for product-management workflows with required attribution in THIRD_PARTY_NOTICES.md).

---

## 📞 Support & Contact

| Issue Type | How to Get Help | Response Time | Notes |
|-----------|-----------------|---------------|-------|
| 🐛 **Bug Report** | [Open a GitHub Issue](https://github.com/Stijnman/grok-custom-skills/issues/new?template=bug_report.yml) | 24-48 hours | Use bug_report.yml template |
| 🔒 **Security Issue** | Private message via GitHub profile | Immediate | See [SECURITY.md](./SECURITY.md) |
| ❓ **General Question** | [Open a GitHub Discussion](https://github.com/Stijnman/grok-custom-skills/discussions) | 24 hours | For non-sensitive questions |
| 💡 **Feature Request** | [Open a GitHub Issue](https://github.com/Stijnman/grok-custom-skills/issues/new?template=feature_request.yml) | 1 week | Use feature_request.yml template |

---

## 🏷️ Repository Metadata

| Attribute | Value |
|-----------|-------|
| **Repository** | [grok-custom-skills](https://github.com/Stijnman/grok-custom-skills) |
| **Owner** | [Stijnman](https://github.com/Stijnman) |
| **License** | MIT |
| **Total Skills** | 89 |
| **Categories** | 7 |
| **Language** | English |
| **Created** | July 2026 |
| **Last Updated** | September 2026 |
| **Stars** | 9 |
| **Forks** | 1 |

### Categories Breakdown

| Category | Skills | Percentage |
|----------|--------|------------|
| Research & Integrations | 20 | 22.5% |
| Workflow & Orchestration | 15 | 16.9% |
| Skill Development | 12 | 13.5% |
| Memory & Knowledge | 12 | 13.5% |
| Media & Visual | 10 | 11.2% |
| Messaging & Navigation | 10 | 11.2% |
| Safety & Governance | 10 | 11.2% |

---

## 🔗 Related Resources

### Specifications & Standards
- [Agent Skills specification](https://agentskills.io/specification) - Skill package conventions
- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) - Integration standards
- [AI Agent Best Practices](https://github.com/ai-safety-standards) - Safety guidelines

### Tools & Frameworks
- [Grok Agent Framework](https://grok.com) - Primary target platform
- [Mistral Vibe](https://github.com/mistralai) - AI agent CLI
- [Agent Skills Ecosystem](https://agentskills.io) - Skill discovery and sharing

### Documentation
- [Agent Skills Documentation](https://agentskills.io/docs) - Official documentation
- [MCP Documentation](https://github.com/modelcontextprotocol/specification) - MCP standards

---

## 🎯 Key Differentiators

| Feature | This Repository | Other Skill Repositories |
|---------|----------------|--------------------------|
| **Safety Focus** | ✅ Core principle - all skills have safety checks | ❌ Varies by contributor |
| **Consistent Structure** | ✅ All skills follow same format | ❌ Inconsistent formats |
| **Comprehensive Testing** | ✅ Testing guide and requirements | ❌ Minimal testing |
| **Publication Safeguards** | ✅ 6 mandatory controls | ❌ No controls |
| **Auto-Generated Catalog** | ✅ SKILLS_INDEX.md from live metadata | ❌ Manual catalog |
| **Validation Pipeline** | ✅ Automated checks | ❌ No validation |
| **Documentation Quality** | ✅ 10/10 standard | ❌ Varies widely |

---

## 📌 Important Notes

### Design Principle
> **Skills should make agent behavior more useful, auditable, and safe.** They are guidance packages, not permission to bypass controls, disclose private data, or automate high-impact actions without human approval.

### Usage Warning
> **Always read and understand a skill before using it.** Check the triggers, boundaries, and warnings in each SKILL.md file. Follow all security requirements in [SECURITY.md](./SECURITY.md).

### Contribution Warning
> **Do not submit skills that**: bypass authentication, evade CAPTCHAs, circumvent paywalls, harvest credentials, automate spam, violate platform terms, or claim unsafe capabilities.

---

## 🏆 Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-09-11 | 2.0.0 | Added comprehensive documentation (SKILL.md, TESTING.md, STATUS.md, CONTRIBUTORS.md), pre-commit hooks, markdown lint config, secrets baseline |
| 2026-09-10 | 1.2.0 | Enhanced documentation (SECURITY.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, CHANGELOG.md, GOVERNANCE.md, PUBLISHING.md, SUPPORT.md), added .github workflows and templates |
| 2026-07-30 | 1.0.0 | Initial repository with 89 skill packages, catalog system, validation pipeline |

---

*Last updated: September 11, 2026*
*Maintainer: Stijnman*
*Repository: [grok-custom-skills](https://github.com/Stijnman/grok-custom-skills)*

---

**Need help?** See [SUPPORT.md](./SUPPORT.md) or open a GitHub issue.
