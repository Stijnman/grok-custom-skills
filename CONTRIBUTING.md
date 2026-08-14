# Contributing

Thank you for improving the Grok Custom Skills collection. Contributions should make agent behavior **clearer, safer, more reliable, or easier to discover**.

## Before you begin

Please search the [skills catalog](SKILLS_INDEX.md) before proposing a new package. Prefer improving an existing skill when the capability already exists. Do not submit private session logs, credentials, personal data, or copied content that you are not authorized to share.

## Creating or updating a skill

Each skill belongs in `.grok/skills/<skill-name>/` and must include `SKILL.md`. Keep the package self-contained and use `scripts/`, `references/`, or `templates/` only when they meaningfully reduce repeated work.

| Requirement | Expectation |
|---|---|
| **Name** | Lowercase, hyphen-separated, stable, and aligned with the directory name. |
| **Description** | State what the skill does and when to use it, with a small set of clear triggers. |
| **Workflow** | Use concrete, ordered steps and state the expected output. |
| **Boundaries** | Document access, privacy, approval, and safety limits where relevant. |
| **Error handling** | Explain how the skill responds to failed access, incomplete data, or ambiguity. |
| **Resources** | Do not include unreviewed binaries, secrets, telemetry, or auto-executing installers. |

Use [PUBLISHING.md](PUBLISHING.md) as the pre-submission checklist.

## Safety requirements

Skills must not instruct agents to bypass authentication, CAPTCHAs, paywalls, platform safeguards, or authorship requirements. Do not submit offensive security workflows, credential collection, hidden data transfer, spam automation, or actions that require a user’s approval without explicitly requesting it.

When a workflow may publish, purchase, delete, deploy, communicate externally, or change credentials, require explicit human approval before the action.

## Validation

Run the catalog generator and available repository checks before opening a pull request.

```bash
python3 scripts/generate_catalog.py
python3 scripts/check_no_private_data.py
python3 scripts/publish_safety_check.py
```

If the contribution includes executable helpers, test them with benign inputs and describe the test coverage in the pull request.

## Pull requests

Keep pull requests focused. Include the following in the description:

1. The problem or request the change addresses.
2. The skills and files changed.
3. Validation performed and the results.
4. Any capability, privacy, or safety considerations.
5. A note if a change affects installation or existing skill names.

Maintainers may request changes, split a submission into smaller reviews, or decline content that is unsafe, out of scope, unverifiable, or duplicative.

## Reporting concerns

Use [SECURITY.md](SECURITY.md) for security-sensitive reports. For ordinary questions or improvement ideas, open a GitHub issue or discussion with enough context to reproduce the concern.
