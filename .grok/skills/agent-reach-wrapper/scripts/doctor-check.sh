#!/usr/bin/env bash
# Non-destructive Agent-Reach health probe for this wrapper skill.
set -euo pipefail

if ! command -v agent-reach >/dev/null 2>&1; then
  echo "STATUS=missing"
  echo "HINT=Install from https://github.com/Panniantong/Agent-Reach — not from PyPI."
  echo "HINT=Do not pass --system unless the user explicitly allows machine writes."
  exit 2
fi

if agent-reach doctor --json >/tmp/agent-reach-doctor.json 2>/tmp/agent-reach-doctor.err; then
  echo "STATUS=ok"
  echo "JSON=/tmp/agent-reach-doctor.json"
  exit 0
fi

echo "STATUS=doctor-failed"
echo "ERR=/tmp/agent-reach-doctor.err"
exit 1
