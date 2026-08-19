Version: 2.1 - Added retry logic

## [0.4.0] - 2026-07-19
### Changed
- Fully rewrote `scripts/sync_engine.py` with argparse, typing, proper logging, and clean CLI.
- Added `--list`, `--backup`, `--cleanup`, `--import-zip` flags.
- Retention policy and hash-based inventory are now first-class.
### Fixed
- Main block was previously incomplete in some copies; now fully functional.

## [1.18] - 2026-08-15
### Changed
- Bumped to Version 1.18 with 2026-08-15 date awareness.
- Reinforced mandatory deferred-list reporting for packaging after 'every skill' requests.
### Note
- Limited batch evolution only.

## [1.22] - 2026-08-19
### Added
- Mandatory Auto-Push Contract (§0): every significant skill OR project update automatically packages, uploads to Drive, and pushes to the correct private GitHub repo (skills → Stijnman/grok-custom-skills; Pulverise → Stijnman/pulverise).
- Explicit Project Auto-Push Procedure (§11) with tar.gz + google_drive_upload_artifact + github___push_files steps.
- Canonical locations expanded for projects.
