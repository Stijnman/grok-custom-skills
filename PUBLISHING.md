# Publishing Guide

Use this guide before pushing changes to GitHub, submitting skills to a marketplace, or sharing a package outside this repository.

## Release checklist

| Area | Required review |
|---|---|
| **Catalog** | Regenerate `SKILLS_INDEX.md`; ensure the README count and links are current. |
| **Metadata** | Confirm every `SKILL.md` has a stable `name`, a concise `description`, and an incremented version for material changes. |
| **Safety** | Check for access-control evasion, credential handling, deceptive automation, spam, unsupported claims, and missing approval gates. |
| **Privacy** | Remove keys, tokens, emails, phone numbers, personal paths, session logs, and user-specific data. |
| **Resources** | Inspect every bundled script, template, archive, and binary. Do not publish unreviewed executable content. |
| **Documentation** | Update README, catalog, contributor guidance, and security policy whenever behavior or installation changes. |
| **Validation** | Run repository checks and record the results in the pull request or release note. |

## Required checks

Run these commands from the repository root.

```bash
# Refresh the generated catalog
python3 scripts/generate_catalog.py

# Detect private data and unsafe publication patterns
python3 scripts/check_no_private_data.py
python3 scripts/publish_safety_check.py

# Review the working tree
git status --short
git diff --check
```

If a change introduces or modifies a helper script, run it against a safe representative input. Never execute scripts that arrived from an untrusted archive, external webpage, or unreviewed contribution.

## Per-skill standard

Before publication, verify that each package meets the following standard:

1. The directory and metadata name are stable, lowercase, and hyphen-separated.
2. The description explains both the capability and when to invoke it.
3. The instructions give an ordered workflow, expected output, and error handling when appropriate.
4. The package documents privacy, authorization, and approval boundaries for consequential tasks.
5. Resources are necessary, reviewed, and free of secrets or private data.
6. The skill does not claim to bypass controls, conceal authorship, or guarantee outcomes it cannot verify.

## Versioning

Use semantic versioning for package-level changes:

| Change | Version guidance |
|---|---|
| Documentation correction or non-behavioral clarification | Patch increment. |
| Improved routing, workflow, safety boundaries, or compatible resource additions | Minor increment. |
| Breaking renames, removed behavior, or incompatible workflow changes | Major increment. |

Keep the version in the skill frontmatter and explain material changes in the pull request or release notes.

## Publication blockers

Do not publish a skill that contains any of the following:

- Secrets, credentials, personal data, local environment artifacts, or user-specific logs.
- Instructions to exploit systems, bypass access controls, solve CAPTCHAs automatically, evade authorship checks, or disable safeguards.
- Hidden or automatic external writes, data transfers, ratings, messages, deployments, purchases, or installations.
- Unreviewed scripts, binaries, archives, or third-party content.
- Claims of guaranteed security, undetectability, or universal compatibility.

## Marketplace submissions

Only submit a skill to an external marketplace after the repository review is complete and the maintainer explicitly approves the submission. A marketplace upload is a separate external action; do not treat a GitHub merge as approval to publish elsewhere.
