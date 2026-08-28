#!/usr/bin/env python3
"""Minimal zip create/list/extract helper for zip-enabler."""
from __future__ import annotations

import argparse
import hashlib
import sys
import zipfile
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def cmd_create(out: Path, sources: list[Path]) -> int:
    out.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for src in sources:
            src = src.resolve()
            if src.is_dir():
                for p in src.rglob("*"):
                    if p.is_file():
                        zf.write(p, p.relative_to(src.parent))
                        count += 1
            elif src.is_file():
                zf.write(src, src.name)
                count += 1
            else:
                print(f"skip missing: {src}", file=sys.stderr)
    print(f"created {out} members={count} bytes={out.stat().st_size} sha256={sha256(out)}")
    return 0


def cmd_list(archive: Path) -> int:
    with zipfile.ZipFile(archive) as zf:
        for info in zf.infolist():
            print(f"{info.file_size:10d}  {info.filename}")
        print(f"members={len(zf.infolist())}")
    return 0


def cmd_extract(archive: Path, dest: Path) -> int:
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as zf:
        zf.extractall(dest)
        print(f"extracted {len(zf.infolist())} members to {dest}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("create")
    c.add_argument("out")
    c.add_argument("sources", nargs="+")

    l = sub.add_parser("list")
    l.add_argument("archive")

    e = sub.add_parser("extract")
    e.add_argument("archive")
    e.add_argument("dest")

    args = p.parse_args()
    if args.cmd == "create":
        return cmd_create(Path(args.out), [Path(s) for s in args.sources])
    if args.cmd == "list":
        return cmd_list(Path(args.archive))
    if args.cmd == "extract":
        return cmd_extract(Path(args.archive), Path(args.dest))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
