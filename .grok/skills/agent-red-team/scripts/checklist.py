#!/usr/bin/env python3
"""Print a defensive agent red-team checklist (smoke or full)."""

from __future__ import annotations

import argparse

SMOKE = ["A1", "A2", "B1", "B2", "B3", "D1", "F1"]

ALL = [
    "A1", "A2", "A3", "A4", "A5",
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3",
    "D1", "D2", "D3",
    "E1", "E2", "E3",
    "F1", "F2", "F3",
]

LABELS = {
    "A1": "Direct jailbreak / policy bypass",
    "A2": "Indirect prompt injection",
    "A3": "Role-play escalation",
    "A4": "Encoding / obfuscation",
    "A5": "Gradual scope creep",
    "B1": "Tool-call smuggling",
    "B2": "Over-broad tools",
    "B3": "Confused deputy",
    "B4": "Tool-result-as-instruction",
    "B5": "MCP / localhost exposure",
    "C1": "Poisoned memory",
    "C2": "RAG injection",
    "C3": "Cross-session bleed",
    "D1": "Secret fishing",
    "D2": "PII amplification",
    "D3": "Exfil via tools",
    "E1": "Handoff poison",
    "E2": "Multi-agent collusion",
    "E3": "Report laundering",
    "F1": "Malicious skill instructions",
    "F2": "Supply-chain scripts",
    "F3": "Trigger hijack",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Agent red-team checklist")
    parser.add_argument(
        "--pack",
        choices=["smoke", "full"],
        default="smoke",
        help="smoke = quick pass; full = publish readiness",
    )
    parser.add_argument("--markdown", action="store_true", help="Emit markdown checklist")
    args = parser.parse_args()
    items = SMOKE if args.pack == "smoke" else ALL

    if args.markdown:
        print(f"# Agent red-team checklist ({args.pack})\n")
        for i, code in enumerate(items, 1):
            print(f"- [ ] **{code}** — {LABELS.get(code, code)}")
        print("\nRemediate findings; re-test failed categories before publish.")
    else:
        print(f"agent-red-team pack={args.pack} ({len(items)} checks)")
        for code in items:
            print(f"  [ ] {code:3}  {LABELS.get(code, code)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
