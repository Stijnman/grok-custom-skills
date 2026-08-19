## Summary

Describe the user need or maintenance goal addressed by this change.

## Changes

- [ ] Skill metadata or routing
- [ ] Skill workflow or resources
- [ ] Generated catalog or README
- [ ] Community, security, or repository governance files
- [ ] Other: describe below

## Validation

List the checks performed and their results.

```text
- [ ] python3 scripts/optimize_all_skills.py
- [ ] python3 -m unittest discover -s tests -p "test_*.py"
- [ ] git diff --check
- [ ] git diff --exit-code -- SKILLS_INDEX.md
- [ ] Relevant helper-script test, if applicable
```

## Safety and privacy review

- [ ] No secrets, personal data, local paths, or session artifacts were added.
- [ ] No access-control bypass, CAPTCHA evasion, credential collection, or deceptive automation was introduced.
- [ ] Consequential external actions require explicit human approval.
- [ ] New or changed scripts were reviewed and tested only with safe inputs.

## Notes for reviewers

Call out any breaking changes, renamed skills, external dependencies, or follow-up work.
