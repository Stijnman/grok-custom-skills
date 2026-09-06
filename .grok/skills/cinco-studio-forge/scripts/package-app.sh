#!/usr/bin/env bash
# Package an exported Studio app tree for Drive upload.
set -euo pipefail
SLUG="${1:-}"
DATE="${2:-$(date +%Y%m%d)}"
if [[ -z "$SLUG" ]]; then
  echo "usage: package-app.sh <slug> [YYYYMMDD]" >&2
  exit 1
fi
SRC="/home/workdir/artifacts/${SLUG}"
OUT="/home/workdir/artifacts/${SLUG}-${DATE}.tar.gz"
if [[ ! -d "$SRC" ]]; then
  echo "missing tree: $SRC" >&2
  exit 2
fi
tar -czf "$OUT" -C /home/workdir/artifacts "$SLUG"
echo "$OUT"
