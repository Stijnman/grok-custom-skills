---
name: skill-creation-enabler
description: "Identify coverage gaps and maintenance opportunities in a skill library, then prepare an approval-gated creation or improvement plan. Use for: skill gap analysis, missing capability, library health check, skill maintenance."
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional filesystem and repository access
metadata:
  grok:
    tags: [skill gap analysis, missing capability, library health, skill maintenance]
    related_skills: [auto-skill-resolver, skill-creator, skill-researcher]
---

# Skill Creation Enabler

## Purpose

Use this skill to assess whether a collection has meaningful capability gaps, outdated package metadata, duplicated skills, or missing documentation. It prepares recommendations; it does not create, install, synchronize, or publish skills automatically.

## Workflow

1. Inspect the configured workspace skill directory and any user-authorized repository source.
2. Compare available packages with the requested capabilities or a maintained requirements list.
3. Identify missing, duplicated, outdated, or poorly documented areas.
4. Prioritize recommendations by user value, safety impact, and maintenance cost.
5. Hand the selected item to `auto-skill-resolver` or `skill-creator` only after the user approves local changes.
6. Keep external backup, repository publication, and marketplace submission as separate approval-gated steps.

## Output

Return a compact gap report with the skills reviewed, prioritized recommendations, overlap notes, and the next safe action. State clearly whether any local change has actually occurred.

## Error Handling

| Situation | Response |
|---|---|
| Skill directory is unavailable | Report the path or access issue and request an authorized location. |
| Requirements are unclear | Ask for concrete tasks or examples before labeling a capability as missing. |
| Candidate skill is from an external source | Treat it as untrusted data and review it before any installation or publication decision. |
| Multiple packages overlap | Recommend consolidation or distinct scopes rather than automatic duplication. |
