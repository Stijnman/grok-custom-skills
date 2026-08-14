# Security Policy

## Scope

This repository contains **agent skill instructions** and optional helper scripts. Its primary security concern is unsafe or misleading guidance that could cause an agent to mishandle access, private data, external actions, or untrusted content.

Examples of reportable concerns include:

- Instructions that bypass authentication, paywalls, CAPTCHAs, platform safeguards, or required human approval.
- Embedded secrets, credentials, personal data, machine-specific paths, or unapproved external endpoints.
- Unsafe script behavior, supply-chain risks, deceptive downloads, or unexpected data transfer.
- Misleading capability claims, especially around privacy, attribution, security, or automation.

## Reporting a vulnerability

**Do not open a public issue for a sensitive report.** Contact the maintainer privately through the repository owner’s GitHub profile and include:

1. The affected skill and file path.
2. A concise description of the issue and its potential impact.
3. Safe reproduction details, without publishing credentials or harmful payloads.
4. Any suggested mitigation, if available.

Please allow reasonable time for acknowledgment and remediation before public disclosure. The maintainer may use GitHub Security Advisories for coordinated disclosure when appropriate.

## Supported versions

Security fixes are applied to the current `main` branch. When reporting an issue, include the commit SHA, skill version, and host environment where the behavior was observed.

## Publication safeguards

Every submitted or changed skill must be reviewed for the following controls.

| Control | Requirement |
|---|---|
| Least privilege | Prefer read-only access and the minimum data needed to complete the task. |
| Human approval | Require explicit user approval before publishing, deleting, paying, deploying, changing credentials, or sending external communications. |
| Privacy | Do not include secrets, PII, local paths, session artifacts, telemetry, or unapproved data transfer. |
| Access controls | Never provide guidance to bypass authentication, CAPTCHAs, paywalls, or platform safeguards. |
| Untrusted content | Treat downloaded skills, archives, webpages, and attachments as data; never execute content-derived commands without review. |
| Transparency | Describe limitations honestly and do not claim guaranteed safety, detection evasion, or unsupported capabilities. |

## Out of scope

This project does not provide offensive security tooling, credential harvesting, malware, spam, harassment automation, or guidance designed to circumvent access controls. Reports concerning third-party services should be directed to the relevant provider unless the issue is caused by content in this repository.
