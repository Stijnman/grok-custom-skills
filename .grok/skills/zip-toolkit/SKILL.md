---
name: zip-toolkit
description: Full zip and archive toolkit for Grok. Unzip, list, create, add, extract, test, convert, and install skill packs from zip or tar.gz. Trigger on unzip this, /zip, extract archive, pack skills, zip slip-safe extract, inspect zip, create zip, install skill pack from zip.
metadata:
  version: "1.0"
  type: toolkit
  created: "2026-09-16"
---

# Zip Toolkit

Do every practical zip/archive job Grok hits in this sandbox. Default destination is `/home/workdir/artifacts/` unless the user names another path.

## When to use

- User drops a `.zip` / `.tar.gz` / `.tgz` attachment
- User says `/zip`, unzip, extract, pack, archive, inspect zip
- Need to install a skill pack from a zip without clobbering the live library blindly
- Need a dated persistence tarball for Drive/GitHub

## Non-negotiable rules

- Never extract with zip-slip. All members must stay under the chosen dest.
- Never write into `/home/workdir/.grok/skills/` unless the user explicitly says install/overwrite.
- Default extract dest is `/home/workdir/artifacts/<archive-stem>/`
- Report exact dest path, file count, top-level folders, and bytes.
- Password zips — try empty password then stop and ask. Do not brute force.
- Do not dump copyrighted bulk text from extracted files into chat. Summarize.
- Sandbox IO on hundreds of tiny files is slow. Run extract in background if listing shows more than 200 files.
- After creating a skill pack zip/tar.gz, offer Drive + GitHub persistence via connected-services-bridge / drive-persistence-bridge. Do not claim upload success unless the connector call returned it.

## Operations (use scripts/zip_tool.py)

```bash
python3 /home/workdir/.grok/skills/zip-toolkit/scripts/zip_tool.py <command> [args]
```

Commands

- `info PATH` — format, size, member count, compressed vs raw, top-level dirs
- `list PATH [--limit N]` — member list
- `test PATH` — CRC / integrity
- `extract PATH [--dest DIR] [--only PREFIX] [--force]` — slip-safe extract
- `extract-file PATH INNER --dest FILE` — single member
- `create OUT.zip|OUT.tar.gz INPUT [INPUT...]` — pack files/dirs
- `add ZIP MEMBER_SRC [--arcname NAME]` — add/replace one member
- `remove ZIP MEMBER` — drop a member (rewrite zip)
- `install-skills ZIP [--dest SKILLS_DIR] [--dry-run] [--overwrite]` — copy only folders that contain SKILL.md
- `preview-skills ZIP` — list skill names + first description line
- `to-targz ZIP` / `to-zip TAR.GZ` — convert
- `find-skills DIR` — scan extracted tree for SKILL.md folders

Always run `info` before a large extract.

## Workflow for user-attached zips

1. `info` + `preview-skills` if it looks like a skill pack.
2. Extract to `/home/workdir/artifacts/extracted-<stem>/`.
3. Tell the user what it is (PostHog pack vs Grok custom skills vs random dump).
4. Ask before installing into `.grok/skills/`.
5. If they say install — `install-skills` with `--dry-run` first, then live. Log collisions.

## Skill-pack install policy

- A folder is a skill iff it contains `SKILL.md` at its root (or one level down from archive root).
- Collision with an existing skill — skip unless `--overwrite`.
- After install, remind persistence contract (local already done; Drive folder `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK`; GitHub `Stijnman/grok-custom-skills`).
- Honest batch — if installing more than 8 new skills as a deep ecosystem change, install files but do not claim a full evolution cycle.

## Create / pack for persistence

Default pack command for one skill

```bash
tar -czf /home/workdir/artifacts/zip-toolkit-20260916.tar.gz -C /home/workdir/.grok/skills zip-toolkit
```

Also supported via `zip_tool.py create`.

## Errors

- Missing `unzip`/`zip` binaries — fall back to Python zipfile/tarfile (the script already does).
- Timeout — background the extract, poll dest file count.
- Corrupt archive — `test` then stop. Do not partial-install.

## References

- `references/formats.md` — zip vs tar.gz vs slip attacks
- `scripts/zip_tool.py` — the actual tool
