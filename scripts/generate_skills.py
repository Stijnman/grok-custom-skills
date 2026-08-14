#!/usr/bin/env python3
"""Generate production-ready SKILL.md files for the grok-custom-skills collection."""

from __future__ import annotations

import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / ".grok" / "skills"

# Each entry: description, triggers, workflow, errors, integrations, gotchas
SKILLS: dict[str, dict] = {
    # --- Existing 12 (optimized) ---
    "self-refine-loop": {
        "description": (
            "Runs a generator-critique-reviser loop to iteratively improve agent outputs. "
            "Use when the user asks to refine, critique, or improve a draft, or mentions "
            "self-refine, reflexion, or iterative revision. Stops at 5 iterations or "
            "confidence 8/10. Triggers: self refine, reflexion loop, critique and revise."
        ),
        "workflow": [
            "Capture the current output and the user's quality criteria.",
            "Generate a critique listing specific weaknesses (max 5 bullets).",
            "Revise the output addressing every critique point.",
            "Score confidence 0-10 on whether criteria are met.",
            "Repeat until confidence >= 8 or 5 iterations; return best version with changelog.",
        ],
        "triggers": ["self refine", "reflexion loop", "critique and revise", "improve output"],
        "integrations": ["goal-verifier", "agentic-uncertainty-quantifier", "dspy-prompt-optimizer"],
        "errors": {
            "No criteria given": "Ask user for 1-3 success criteria before looping.",
            "Confidence stuck below 5": "Stop early; report blocker and ask for guidance.",
            "Output grows unbounded": "Cap revisions to prior length + 20%.",
        },
        "gotchas": ["Do not loop on trivial typos; one-pass fix is enough."],
    },
    "goal-verifier": {
        "description": (
            "Verifies task completion against stated goals before marking work done. "
            "Use when the user asks to verify success, confirm completion, or says "
            "'did I achieve this'. Runs checks + optional self-refine pass. "
            "Triggers: verify goal, confirm success, did I achieve this."
        ),
        "workflow": [
            "Restate the original goal in one sentence.",
            "List acceptance criteria (explicit or inferred from conversation).",
            "Check each criterion: pass / fail / partial with evidence.",
            "If any fail, invoke self-refine-loop or report gaps.",
            "Only mark complete when all critical criteria pass.",
        ],
        "triggers": ["verify goal", "confirm success", "did I achieve this", "check if done"],
        "integrations": ["self-refine-loop", "auto-tester"],
        "errors": {
            "Goal undefined": "Ask user to confirm goal before verifying.",
            "False positive risk": "Require evidence (file path, command output, or test result).",
        },
        "gotchas": ["Verification is read-only; do not mutate artifacts during checks."],
    },
    "hitl-approver": {
        "description": (
            "Pauses high-risk actions for explicit human approval. Use before WhatsApp "
            "sends, deployments, deletions, credential changes, or financial actions. "
            "Triggers: approve this, hitl check, human review needed."
        ),
        "workflow": [
            "Classify action: message / deploy / delete / financial / credential.",
            "Present briefing: summary, risk (low/medium/high), rollback plan.",
            "Wait for explicit approval (yes / approve / go ahead).",
            "On approval, execute and confirm outcome. On denial, abort and suggest safer path.",
        ],
        "triggers": ["approve this", "hitl check", "human review needed", "confirm before send"],
        "integrations": ["whatsapp-auto-responder", "privacy-redactor", "multi-platform-messenger-bridge"],
        "errors": {
            "Ambiguous approval": "Re-ask; never infer consent from silence.",
            "Timeout in session": "Defer action; remind user once.",
            "User says no": "Abort; log reason; offer alternative.",
        },
        "gotchas": ["Medium+ risk always requires HITL even if user seems hurried."],
        "output_template": "HITL Required: {type}\nSummary: {summary}\nRisk: {level}\nRollback: {plan}\nApprove? (yes/no)",
    },
    "self-healing-error-recovery": {
        "description": (
            "Diagnoses failures and retries with alternate strategies. Use when commands "
            "fail, tools error, or the user says heal this error, self recover, fix "
            "failure automatically. Stores lessons for future tasks."
        ),
        "workflow": [
            "Capture error message, command, and environment context.",
            "Classify: transient / config / permission / logic / dependency.",
            "Try up to 3 recovery strategies (retry, alternate path, dependency fix).",
            "If recovered, summarize fix. If not, escalate with diagnosis.",
            "Record lesson: error pattern -> successful fix.",
        ],
        "triggers": ["heal this error", "self recover", "fix failure automatically", "retry smart"],
        "integrations": ["knowledge-graph-builder", "semantic-memory-manager", "bottleneck-resolver"],
        "errors": {
            "Destructive command failed": "Do not auto-retry deletes; require HITL.",
            "Same error 3x": "Stop retrying; report root cause.",
            "Permission denied": "Never escalate privileges; ask user.",
        },
        "gotchas": ["Read-only diagnosis first; mutate only after classification."],
    },
    "cron-scheduler": {
        "description": (
            "Schedules recurring or delayed agent tasks. Use when the user says schedule "
            "this, run daily, cron job, or set timer. Parses schedules from SKILL.md "
            "or cron-jobs.md. Triggers: schedule this, run daily, cron job, set timer."
        ),
        "workflow": [
            "Parse schedule expression (cron, interval, or natural language).",
            "Write entry to workspace cron-jobs.md (default) or document GitHub Action.",
            "Define task: skill to invoke, args, and notification channel.",
            "Confirm next 3 run times with user.",
            "On trigger, execute task and log via insight-synthesizer.",
        ],
        "triggers": ["schedule this", "run daily", "cron job", "set timer", "every morning"],
        "integrations": ["insight-synthesizer", "goal-verifier"],
        "references": "references/scheduling.md",
        "errors": {
            "Invalid cron": "Show valid example: 0 9 * * 1-5 (weekdays 9am).",
            "No workspace write access": "Output schedule as copy-paste block only.",
        },
        "gotchas": ["Read references/scheduling.md for backend options."],
    },
    "privacy-redactor": {
        "description": (
            "Detects and redacts PII in inputs and outputs before external actions. "
            "Use when the user says redact PII, privacy check, or sanitize this. "
            "Scans emails, phones, names, addresses. Routes high-risk to hitl-approver."
        ),
        "workflow": [
            "Scan text for PII patterns: email, phone, SSN, address, full names.",
            "Replace with tokens: [EMAIL], [PHONE], [NAME], [ADDRESS].",
            "List redactions in summary for user review.",
            "If external send requested, run hitl-approver after redaction.",
        ],
        "triggers": ["redact PII", "privacy check", "sanitize this", "remove personal data"],
        "integrations": ["hitl-approver", "whatsapp-auto-responder", "memory-sanitizer"],
        "errors": {
            "Over-redaction": "Preserve structure; only redact confirmed PII.",
            "Missed PII": "Run second pass on capitalized tokens and @ symbols.",
        },
        "gotchas": ["Never log raw PII to external services after redaction."],
    },
    "memory-sanitizer": {
        "description": (
            "Scores and filters retrieved memory against trust and poisoning risk. "
            "Use before citing prior context, or when user says sanitize memory, "
            "trust score retrieval, clean knowledge graph."
        ),
        "workflow": [
            "For each memory entry, score trust 0-10 (source, recency, user-confirmed).",
            "Discard entries below 4 unless user explicitly references them.",
            "Prefix 4-6 scores with [unverified memory] when citing.",
            "Flag contradictions between entries; prefer user-confirmed.",
        ],
        "triggers": ["sanitize memory", "trust score retrieval", "clean knowledge graph"],
        "integrations": ["semantic-memory-manager", "knowledge-graph-builder", "agentic-uncertainty-quantifier"],
        "errors": {
            "All entries low trust": "Ask user to confirm facts before proceeding.",
            "Contradictory memories": "Present both; ask user to resolve.",
        },
        "gotchas": ["Delegate retrieval to semantic-memory-manager when installed."],
    },
    "agentic-uncertainty-quantifier": {
        "description": (
            "Scores task uncertainty to calibrate memory depth and iteration count. "
            "Use when stakes are high, facts are sparse, or user says quantify "
            "uncertainty, fast slow think, uncertainty score."
        ),
        "workflow": [
            "Score epistemic uncertainty 0-10 (how much is unknown).",
            "Score procedural uncertainty 0-10 (how clear are the steps).",
            "High epistemic (>6): retrieve more context, run self-refine-loop.",
            "Low procedural (<4): ask clarifying questions before acting.",
            "Report scores and recommended depth to user.",
        ],
        "triggers": ["quantify uncertainty", "fast slow think", "uncertainty score", "how sure"],
        "integrations": ["self-refine-loop", "semantic-memory-manager", "deep-search-enabler"],
        "errors": {
            "False confidence": "Bias toward caution on destructive tasks.",
        },
        "gotchas": ["Uncertainty > 7 on financial/deploy actions triggers hitl-approver."],
    },
    "dspy-prompt-optimizer": {
        "description": (
            "Tunes prompts iteratively using reflection and success metrics. Use when "
            "the user says optimize this prompt, dspy tune, or improve prompt with "
            "reflection. Integrates self-refine-loop for critique cycles."
        ),
        "workflow": [
            "Capture baseline prompt and 2-3 example inputs with desired outputs.",
            "Run baseline; score outputs against criteria.",
            "Generate 3 prompt variants addressing failures.",
            "Test variants; pick best by score.",
            "Return optimized prompt with before/after metrics.",
        ],
        "triggers": ["optimize this prompt", "dspy tune", "improve prompt with reflection"],
        "integrations": ["self-refine-loop", "auto-tester", "hyper-skill-tester"],
        "errors": {
            "No examples": "Ask for 2 input/output pairs minimum.",
            "Overfitting one example": "Require 3+ diverse examples.",
        },
        "gotchas": ["Keep prompt under 2000 tokens unless user needs longer."],
    },
    "whatsapp-message-rater": {
        "description": (
            "Rates WhatsApp messages for sentiment, urgency, and spam likelihood. "
            "Use before auto-reply decisions or when user says rate this WhatsApp, "
            "analyze chat sentiment, score message urgency."
        ),
        "workflow": [
            "Parse message: sender, text, timestamp, attachments.",
            "Score sentiment (-1 to 1), urgency (0-10), spam (0-10).",
            "Output JSON summary plus one-line recommendation.",
            "Update per-contact profile if memory available.",
        ],
        "triggers": ["rate this WhatsApp", "analyze chat sentiment", "score message urgency"],
        "integrations": ["whatsapp-auto-responder", "privacy-redactor", "multi-platform-messenger-bridge"],
        "errors": {
            "Empty message": "Return neutral scores; flag as no-content.",
            "PII in message": "Run privacy-redactor before storing profile.",
        },
        "gotchas": ["Spam score > 7: never auto-reply; flag for user."],
        "output_template": '{"sentiment": 0.0, "urgency": 0, "spam": 0, "recommendation": ""}',
    },
    "whatsapp-auto-responder": {
        "description": (
            "Drafts and optionally sends WhatsApp replies with rater and HITL gates. "
            "Use when user says auto reply WhatsApp or enable WhatsApp assistant. "
            "Per-contact toggle; ethical guardrails and rate limits enforced."
        ),
        "workflow": [
            "Rate incoming message via whatsapp-message-rater.",
            "If spam > 7: ignore. If urgency > 8: notify user immediately.",
            "Draft reply; run privacy-redactor on draft.",
            "If contact auto-mode off or risk medium+: hitl-approver before send.",
            "Send and log; respect max 10 auto-replies/hour per contact.",
        ],
        "triggers": ["auto reply WhatsApp", "enable WhatsApp assistant", "reply on WhatsApp"],
        "integrations": ["whatsapp-message-rater", "hitl-approver", "privacy-redactor", "cron-scheduler"],
        "errors": {
            "Rate limit hit": "Queue for user review; do not send.",
            "Bridge unavailable": "Draft only; tell user to send manually.",
        },
        "gotchas": ["Never auto-reply to financial or legal content."],
    },
    "multi-platform-messenger-bridge": {
        "description": (
            "Unifies WhatsApp, Telegram, and future channels with shared memory and "
            "rating. Use when user says bridge messengers or unified chat memory. "
            "One rater, one auto-responder policy across platforms."
        ),
        "workflow": [
            "Normalize message format across platforms (sender, channel, body, meta).",
            "Route through whatsapp-message-rater (or platform equivalent).",
            "Apply shared contact profile from semantic-memory-manager.",
            "Dispatch reply via platform adapter; same HITL rules everywhere.",
        ],
        "triggers": ["bridge messengers", "unified chat memory", "cross-platform reply"],
        "integrations": ["whatsapp-auto-responder", "whatsapp-message-rater", "semantic-memory-manager", "hitl-approver"],
        "references": "references/messenger-setup.md",
        "errors": {
            "Platform not configured": "Read references/messenger-setup.md; guide setup.",
            "Channel policy mismatch": "Apply strictest policy across channels.",
        },
        "gotchas": ["Read references/messenger-setup.md before first use."],
    },
    # --- README original 51 ---
    "adaptive-workflow-composer": {
        "description": (
            "Composes multi-step agent workflows from goals and available skills. "
            "Use when tasks need orchestration or user says compose workflow, plan "
            "steps, adaptive pipeline. Triggers: compose workflow, plan steps."
        ),
        "workflow": [
            "Parse goal into subtasks with dependencies.",
            "Map subtasks to installed skills via tool-discovery-engine.",
            "Order steps; identify parallelizable segments.",
            "Output workflow DAG with skill assignments and fallbacks.",
        ],
        "triggers": ["compose workflow", "plan steps", "adaptive pipeline", "orchestrate task"],
        "integrations": ["workflow-composer", "multi-agent-orchestrator", "tool-discovery-engine"],
        "errors": {"No matching skill": "Suggest natural-language-to-skill or manual step."},
        "gotchas": ["Prefer fewer steps; merge trivial subtasks."],
    },
    "ai-share-extractor-v4": {
        "description": (
            "Extracts shareable insights from long agent sessions for export. "
            "Use when user wants a summary to share, export takeaways, or create "
            "share card. Triggers: extract shares, shareable summary, export insights."
        ),
        "workflow": [
            "Identify key decisions, outputs, and actionable items.",
            "Strip PII via privacy-redactor.",
            "Format as markdown share card with title and 5 bullet highlights.",
            "Offer copy-paste and optional image via imagine-asset-generator.",
        ],
        "triggers": ["extract shares", "shareable summary", "export insights"],
        "integrations": ["privacy-redactor", "insight-synthesizer", "imagine-asset-generator"],
        "errors": {"Session too short": "Report insufficient content; ask what to highlight."},
        "gotchas": ["Never include secrets, tokens, or raw credentials."],
    },
    "auto-tester": {
        "description": (
            "Runs validation tests on code, skills, or outputs after changes. "
            "Use after implementations or when user says run tests, auto test, "
            "validate changes. Triggers: run tests, auto test, validate changes."
        ),
        "workflow": [
            "Detect project type (Python, Node, skill-only).",
            "Run appropriate test command (pytest, npm test, or skill checklist).",
            "Parse results; classify pass/fail/flaky.",
            "On fail: invoke self-healing-error-recovery or report with fix hints.",
        ],
        "triggers": ["run tests", "auto test", "validate changes", "check tests"],
        "integrations": ["goal-verifier", "self-healing-error-recovery", "hyper-skill-tester"],
        "errors": {"No test suite": "Run smoke checks: import, lint, dry-run."},
        "gotchas": ["Never skip tests before marking goal-verifier complete."],
    },
    "beta-unlocker": {
        "description": (
            "Guides enabling beta or experimental Grok features safely. Use when user "
            "asks about beta features, early access, or unlock experimental tools."
        ),
        "workflow": [
            "Identify requested feature and current environment.",
            "Check prerequisites (account tier, settings path, risks).",
            "Provide step-by-step enable instructions.",
            "Warn about instability; suggest hitl-approver for risky betas.",
        ],
        "triggers": ["beta feature", "early access", "unlock experimental", "enable beta"],
        "integrations": ["hitl-approver", "help"],
        "errors": {"Feature unavailable": "State requirement; suggest alternatives."},
        "gotchas": ["Beta features may change without notice; avoid production deps."],
    },
    "bottleneck-resolver": {
        "description": (
            "Identifies and resolves performance bottlenecks in agent workflows. "
            "Use when tasks are slow, stuck, or user says find bottleneck, speed up."
        ),
        "workflow": [
            "Profile step durations (tool calls, waits, retries).",
            "Rank bottlenecks by impact.",
            "Propose fixes: parallelize, cache, simplify, batch.",
            "Implement highest-impact fix; re-measure.",
        ],
        "triggers": ["find bottleneck", "speed up", "why so slow", "optimize workflow"],
        "integrations": ["performance-optimizer", "parallel-tool-orchestrator", "predictive-cache-manager"],
        "errors": {"Cannot measure": "Add timing logs to next run."},
        "gotchas": ["Measure before optimizing; avoid premature parallelization."],
    },
    "code-reviewer": {
        "description": (
            "Reviews code changes for bugs, style, security, and maintainability. "
            "Use after writing code or when user says review code, code review, "
            "check my PR. Triggers: review code, code review, check my changes."
        ),
        "workflow": [
            "Read diff or changed files; understand intent.",
            "Check: correctness, edge cases, security, tests, style.",
            "Categorize findings: critical / major / minor / nit.",
            "Suggest concrete fixes with file:line references.",
        ],
        "triggers": ["review code", "code review", "check my PR", "review my changes"],
        "integrations": ["auto-tester", "goal-verifier", "self-refine-loop"],
        "errors": {"No diff available": "Ask user for files or git diff."},
        "gotchas": ["Critical security issues block merge recommendation."],
    },
    "compliance-image-guard": {
        "description": (
            "Checks images for policy compliance before generation or publish. "
            "Use before sharing images or when user says compliance check, safe image."
        ),
        "workflow": [
            "Review image prompt or asset for policy risks.",
            "Flag: real persons without consent, violence, IP infringement.",
            "Block or revise prompt; route edge cases to hitl-approver.",
            "Log decision rationale.",
        ],
        "triggers": ["compliance check", "safe image", "image policy", "can I publish this"],
        "integrations": ["safe-image-editor", "imagine-asset-generator", "hitl-approver"],
        "errors": {"Ambiguous policy": "Default deny; ask user to confirm."},
        "gotchas": ["Real-person likeness requires explicit user confirmation."],
    },
    "computer-use-bridge": {
        "description": (
            "Bridges desktop automation to agent tool calls. Use when tasks need GUI "
            "interaction, screen control, or user says computer use, desktop control."
        ),
        "workflow": [
            "Confirm desktop environment and permissions.",
            "Plan actions: click, type, navigate (minimal steps).",
            "Execute via desktop-subagent-connector with screenshots.",
            "Verify outcome visually; retry once on mismatch.",
        ],
        "triggers": ["computer use", "desktop control", "click on screen", "GUI automation"],
        "integrations": ["desktop-subagent-connector", "hitl-approver"],
        "errors": {"Permission denied": "Ask user to grant accessibility permissions."},
        "gotchas": ["Destructive GUI actions require hitl-approver."],
    },
    "connected-services-bridge": {
        "description": (
            "Connects external services (GitHub, Notion, Drive) to agent workflows. "
            "Use when integrating APIs or user says connect service, bridge API."
        ),
        "workflow": [
            "Identify service and required scopes.",
            "Check MCP or OAuth availability.",
            "Configure connection; test read-only call first.",
            "Document usage pattern for workflow-composer.",
        ],
        "triggers": ["connect service", "bridge API", "integrate GitHub", "hook up Notion"],
        "integrations": ["drive-persistence-bridge", "tool-discovery-engine", "internet-enabler"],
        "errors": {"Auth missing": "Guide user through auth; never store tokens in skill files."},
        "gotchas": ["Least-privilege scopes only."],
    },
    "control-overview": {
        "description": (
            "Provides control-panel overview of active skills, workflows, and status. "
            "Use when user says overview, status dashboard, what skills are active."
        ),
        "workflow": [
            "List installed skills from .grok/skills/.",
            "Summarize recent workflows and scheduled jobs.",
            "Highlight risks from defensive audits if available.",
            "Output status table: skill, last used, health.",
        ],
        "triggers": ["overview", "status dashboard", "what skills", "control panel"],
        "integrations": ["tool-discovery-engine", "cron-scheduler", "insight-synthesizer"],
        "errors": {"Skills dir missing": "Report path; suggest install steps."},
        "gotchas": ["Read-only inventory; do not modify skills during overview."],
    },
    "data-visualizer": {
        "description": (
            "Creates charts and visual summaries from tabular or numeric data. "
            "Use when user says visualize data, chart this, plot results."
        ),
        "workflow": [
            "Parse data source (CSV, JSON, spreadsheet).",
            "Choose chart type: bar, line, pie, scatter (default bar for categories).",
            "Generate visualization code or image.",
            "Include title, labels, and one-sentence insight.",
        ],
        "triggers": ["visualize data", "chart this", "plot results", "graph this"],
        "integrations": ["xlsx", "insight-synthesizer"],
        "errors": {"Malformed data": "Show first 5 rows; ask user to fix format."},
        "gotchas": ["Prefer code-generated charts over hand-drawn ASCII for accuracy."],
    },
    "deep-search-enabler": {
        "description": (
            "Enables thorough multi-source research beyond quick answers. Use for "
            "complex research or user says deep search, comprehensive research."
        ),
        "workflow": [
            "Decompose question into sub-queries.",
            "Search web, docs, and workspace in parallel.",
            "Synthesize with citations; flag conflicting sources.",
            "Score confidence via agentic-uncertainty-quantifier.",
        ],
        "triggers": ["deep search", "comprehensive research", "research thoroughly"],
        "integrations": ["internet-enabler", "web-scraper", "insight-synthesizer", "agentic-uncertainty-quantifier"],
        "errors": {"No sources found": "Broaden query; suggest alternate terms."},
        "gotchas": ["Cite URLs for factual claims."],
    },
    "desktop-subagent-connector": {
        "description": (
            "Spawns desktop subagents for isolated GUI or local tasks. Use when "
            "delegating screen work or user says desktop subagent, spawn local agent."
        ),
        "workflow": [
            "Define subagent scope and timeout.",
            "Launch with minimal tool set for task.",
            "Monitor progress; collect result artifact.",
            "Terminate subagent; merge results to parent context.",
        ],
        "triggers": ["desktop subagent", "spawn local agent", "delegate desktop"],
        "integrations": ["computer-use-bridge", "multi-agent-coordinator"],
        "errors": {"Subagent timeout": "Return partial result; report stuck step."},
        "gotchas": ["Subagents inherit safety rules including hitl-approver."],
    },
    "drive-persistence-bridge": {
        "description": (
            "Persists agent artifacts to cloud drive storage. Use when saving "
            "reports, backups, or user says save to drive, persist output."
        ),
        "workflow": [
            "Identify artifact and target folder.",
            "Run privacy-redactor on content if external.",
            "Upload via connected service; confirm link.",
            "Log path in semantic-memory-manager optional index.",
        ],
        "triggers": ["save to drive", "persist output", "upload report", "cloud backup"],
        "integrations": ["connected-services-bridge", "privacy-redactor", "persistent-memory-bridge"],
        "errors": {"Upload fail": "Retry once; offer local save fallback."},
        "gotchas": ["Large files: confirm with user before upload."],
    },
    "evolution": {
        "description": (
            "Tracks incremental improvements to skills and workflows over time. "
            "Use when iterating on skill quality or user says evolve skill, track evolution."
        ),
        "workflow": [
            "Capture baseline metrics (triggers, success rate, user feedback).",
            "Propose one improvement per cycle.",
            "Apply via skill-evolver; version backup.",
            "Compare before/after; keep or rollback.",
        ],
        "triggers": ["evolve skill", "track evolution", "improve over time"],
        "integrations": ["skill-evolver", "skill-evolution-engine", "evolver"],
        "errors": {"Regression detected": "Rollback from versions/ backup."},
        "gotchas": ["One change per evolution cycle for clear attribution."],
    },
    "evolver": {
        "description": (
            "Lightweight skill mutation helper for quick iterations. Use for small "
            "skill tweaks or user says quick evolve, mutate skill."
        ),
        "workflow": [
            "Load target SKILL.md.",
            "Apply single targeted edit (description, workflow step, error row).",
            "Validate frontmatter; save.",
            "Notify skill-evolution-engine of change.",
        ],
        "triggers": ["quick evolve", "mutate skill", "tweak skill"],
        "integrations": ["skill-evolver", "evolution", "hyper-skill-tester"],
        "errors": {"Invalid frontmatter": "Restore from git or versions/ backup."},
        "gotchas": ["Prefer skill-evolver for major rewrites."],
    },
    "humanization-stealth-browsing": {
        "description": (
            "Browses web with human-like patterns to reduce bot detection. Use for "
            "scraping fragile sites or user says stealth browse, human-like browsing."
        ),
        "workflow": [
            "Set realistic delays and headers.",
            "Navigate incrementally; avoid burst requests.",
            "Rotate user-agent only when site blocks.",
            "Respect robots.txt; stop on CAPTCHA and ask user.",
        ],
        "triggers": ["stealth browse", "human-like browsing", "avoid bot detection"],
        "integrations": ["web-scraper", "sandbox-internet-handler", "humanization-stealth-browsing"],
        "errors": {"CAPTCHA encountered": "Stop; ask user to solve manually."},
        "gotchas": ["Never bypass paywalls or auth without permission."],
    },
    "hyper-skill-tester": {
        "description": (
            "Stress-tests skills with edge-case prompts and scoring rubric. Use "
            "before publishing skills or user says test skill, hyper test."
        ),
        "workflow": [
            "Load skill; generate 10 trigger and 5 anti-trigger prompts.",
            "Simulate agent behavior against rubric.",
            "Score 10 dimensions; flag scores below 3.",
            "Output report with fix suggestions.",
        ],
        "triggers": ["test skill", "hyper test", "skill QA", "audit skill quality"],
        "integrations": ["auto-tester", "skill-researcher", "review-skill"],
        "errors": {"Skill not found": "Verify path under .grok/skills/."},
        "gotchas": ["Run after every skill-evolver change."],
    },
    "imagine-asset-generator": {
        "description": (
            "Generates visual assets via image generation tools. Use when user needs "
            "icons, mockups, illustrations, or says generate image, create asset."
        ),
        "workflow": [
            "Clarify subject, style, dimensions, and constraints.",
            "Run compliance-image-guard on prompt.",
            "Generate via imagine skill or image API.",
            "Deliver file path and usage notes.",
        ],
        "triggers": ["generate image", "create asset", "make icon", "design mockup"],
        "integrations": ["imagine", "compliance-image-guard", "safe-image-editor"],
        "errors": {"Policy block": "Revise prompt; explain blocked element."},
        "gotchas": ["Load imagine skill when image_gen tools are available."],
    },
    "insight-synthesizer": {
        "description": (
            "Synthesizes findings from multiple sources into actionable insights. "
            "Use after research or user says synthesize, key takeaways, summarize findings."
        ),
        "workflow": [
            "Collect inputs: search results, logs, conversation.",
            "Cluster themes; rank by impact and confidence.",
            "Output: 3-5 insights, each with evidence and action.",
            "Tag uncertainties for agentic-uncertainty-quantifier.",
        ],
        "triggers": ["synthesize", "key takeaways", "summarize findings", "insight report"],
        "integrations": ["deep-search-enabler", "knowledge-graph-builder", "ai-share-extractor-v4"],
        "errors": {"Contradictory sources": "Present both sides; do not merge blindly."},
        "gotchas": ["Insights must be actionable, not restatements."],
    },
    "internet-enabler": {
        "description": (
            "Ensures web access is used effectively for live information. Use when "
            "facts may be stale or user says search web, need internet, look up online."
        ),
        "workflow": [
            "Decide if web search is needed (current events, versions, prices).",
            "Formulate specific query; search with citations.",
            "Cross-check 2+ sources for critical facts.",
            "Summarize with URLs and retrieval date.",
        ],
        "triggers": ["search web", "need internet", "look up online", "current info"],
        "integrations": ["deep-search-enabler", "web-scraper", "sandbox-internet-handler"],
        "errors": {"Search blocked": "Use sandbox-internet-handler fallback."},
        "gotchas": ["Prefer WebSearch for facts not in training data."],
    },
    "knowledge-graph-builder": {
        "description": (
            "Builds structured knowledge graphs from text and sessions. Use when "
            "organizing entities and relations or user says knowledge graph, map entities."
        ),
        "workflow": [
            "Extract entities: people, tools, projects, concepts.",
            "Define relations: uses, depends_on, blocks, produces.",
            "Output JSON graph or mermaid diagram.",
            "Store index in semantic-memory-manager.",
        ],
        "triggers": ["knowledge graph", "map entities", "build graph", "entity map"],
        "integrations": ["semantic-memory-manager", "insight-synthesizer", "self-healing-error-recovery"],
        "errors": {"Too many entities": "Cluster; show top 20 with expand option."},
        "gotchas": ["Graphs are hypotheses; mark unverified edges."],
    },
    "mega-context-manager": {
        "description": (
            "Manages large context windows via chunking, summarization, and retrieval. "
            "Use for long documents or user says manage context, too much context."
        ),
        "workflow": [
            "Measure token estimate of inputs.",
            "If over budget: chunk, summarize chunks, index.",
            "Retrieve relevant chunks per subtask only.",
            "Drop stale chunks after task completion.",
        ],
        "triggers": ["manage context", "too much context", "chunk document", "context budget"],
        "integrations": ["semantic-memory-manager", "predictive-cache-manager", "persistent-memory-bridge"],
        "errors": {"Retrieval miss": "Expand query; include adjacent chunks."},
        "gotchas": ["Summaries lose detail; keep raw chunks for citation."],
    },
    "multi-agent-coordinator": {
        "description": (
            "Coordinates multiple agents with role assignment and handoffs. Use for "
            "parallel work or user says coordinate agents, multi agent team."
        ),
        "workflow": [
            "Define roles: planner, executor, reviewer (minimum).",
            "Assign subtasks per role.",
            "Establish handoff format between agents.",
            "Merge outputs; run goal-verifier on combined result.",
        ],
        "triggers": ["coordinate agents", "multi agent team", "agent roles", "delegate agents"],
        "integrations": ["multi-agent-orchestrator", "desktop-subagent-connector", "goal-verifier"],
        "errors": {"Agent conflict": "Reviewer role breaks tie."},
        "gotchas": ["Max 5 parallel agents to avoid context sprawl."],
    },
    "multi-agent-orchestrator": {
        "description": (
            "Orchestrates complex multi-agent pipelines with DAG execution. Use for "
            "large projects or user says orchestrate agents, agent pipeline."
        ),
        "workflow": [
            "Build task DAG via adaptive-workflow-composer.",
            "Spawn agents per node with scoped context.",
            "Execute topological order; parallelize independent nodes.",
            "Aggregate; run self-refine-loop on final output.",
        ],
        "triggers": ["orchestrate agents", "agent pipeline", "multi step agents"],
        "integrations": ["multi-agent-coordinator", "parallel-tool-orchestrator", "self-refine-loop"],
        "errors": {"DAG cycle": "Break cycle; serialize conflicting nodes."},
        "gotchas": ["Integrates self-refine-loop as skeptic reviewer agent."],
    },
    "natural-language-to-skill": {
        "description": (
            "Converts natural language descriptions into SKILL.md drafts. Use when "
            "user describes a new capability or says create skill from description."
        ),
        "workflow": [
            "Parse intent: triggers, workflow, integrations, errors.",
            "Generate SKILL.md following Agent Skills spec.",
            "Run hyper-skill-tester on draft.",
            "Save to .grok/skills/<name>/ via skill-creation-enabler.",
        ],
        "triggers": ["create skill from description", "NL to skill", "skill from prompt"],
        "integrations": ["skill-creation-enabler", "hyper-skill-tester", "skill-researcher"],
        "errors": {"Vague request": "Ask 3 clarifying questions before generating."},
        "gotchas": ["Name must be lowercase-hyphen, max 64 chars."],
    },
    "parallel-tool-orchestrator": {
        "description": (
            "Runs independent tool calls in parallel for latency reduction. Use when "
            "multiple reads/searches needed or user says parallel tools, run concurrently."
        ),
        "workflow": [
            "Identify independent tool calls in plan.",
            "Batch parallel execution (max 5 concurrent).",
            "Collect results; handle partial failures.",
            "Continue sequential steps that depend on results.",
        ],
        "triggers": ["parallel tools", "run concurrently", "batch requests", "parallelize"],
        "integrations": ["performance-optimizer", "bottleneck-resolver", "multi-agent-orchestrator"],
        "errors": {"Rate limited": "Backoff exponentially; reduce concurrency."},
        "gotchas": ["Never parallelize dependent or destructive operations."],
    },
    "performance-optimizer": {
        "description": (
            "Optimizes agent and code performance via profiling and tuning. Use when "
            "slow execution or user says optimize performance, make faster."
        ),
        "workflow": [
            "Profile hot paths: tools, loops, prompts.",
            "Apply: caching, shorter prompts, parallel tools, lazy load.",
            "Measure improvement.",
            "Document tradeoffs for user.",
        ],
        "triggers": ["optimize performance", "make faster", "performance tune"],
        "integrations": ["bottleneck-resolver", "parallel-tool-orchestrator", "predictive-cache-manager"],
        "errors": {"No baseline": "Record timing before changes."},
        "gotchas": ["Do not sacrifice correctness for speed."],
    },
    "persistent-memory-bridge": {
        "description": (
            "Bridges session memory to persistent storage across conversations. Use "
            "when continuity needed or user says remember this, persistent memory."
        ),
        "workflow": [
            "Extract durable facts: preferences, project state, decisions.",
            "Run memory-sanitizer before persist.",
            "Write to semantic-memory-manager store.",
            "Confirm what was saved; offer forget option.",
        ],
        "triggers": ["remember this", "persistent memory", "save to memory", "recall later"],
        "integrations": ["semantic-memory-manager", "memory-sanitizer", "user-preference-profiler"],
        "errors": {"Storage full": "Prune lowest-trust entries first."},
        "gotchas": ["Never persist secrets or credentials."],
    },
    "predictive-cache-manager": {
        "description": (
            "Caches frequent tool results and prefetches likely next requests. Use "
            "for repeated workflows or user says cache results, prefetch."
        ),
        "workflow": [
            "Identify repeat queries from session history.",
            "Cache with TTL based on data freshness needs.",
            "Invalidate on write operations to same resource.",
            "Prefetch only high-confidence next steps.",
        ],
        "triggers": ["cache results", "prefetch", "reuse cache", "avoid repeat fetch"],
        "integrations": ["performance-optimizer", "mega-context-manager"],
        "errors": {"Stale cache served": "Shorten TTL; add freshness check."},
        "gotchas": ["Never cache auth tokens or PII."],
    },
    "real-time-voice-reasoner": {
        "description": (
            "Handles real-time voice input with low-latency reasoning. Use for voice "
            "sessions or user says voice mode, speak and reason."
        ),
        "workflow": [
            "Transcribe or receive voice input stream.",
            "Apply voice-think-fast-handler for quick ack.",
            "Reason on full utterance; respond concisely for TTS.",
            "Confirm ambiguous commands verbally.",
        ],
        "triggers": ["voice mode", "speak and reason", "voice assistant", "listen"],
        "integrations": ["voice-think-fast-handler", "voice-synthesis-handler"],
        "errors": {"Poor transcription": "Ask user to repeat once."},
        "gotchas": ["Voice confirmations for destructive actions."],
    },
    "safe-image-editor": {
        "description": (
            "Edits images with policy and quality guardrails. Use when modifying "
            "images or user says edit image, safe edit, adjust photo."
        ),
        "workflow": [
            "Load source image; confirm edit intent.",
            "Run compliance-image-guard on edit plan.",
            "Apply edit via image_edit or equivalent.",
            "Show before/after; preserve original backup.",
        ],
        "triggers": ["edit image", "safe edit", "adjust photo", "modify image"],
        "integrations": ["imagine", "compliance-image-guard", "imagine-asset-generator"],
        "errors": {"Edit failed": "Retry with simpler edit scope."},
        "gotchas": ["Never edit ID documents without HITL."],
    },
    "sandbox-internet-handler": {
        "description": (
            "Fetches web content in a sandboxed, read-only manner. Use for untrusted "
            "URLs or user says sandbox fetch, safe web access."
        ),
        "workflow": [
            "Validate URL scheme (https only).",
            "Fetch with timeout and size limit.",
            "Strip scripts; return text/markdown only.",
            "Flag suspicious content; do not execute embedded code.",
        ],
        "triggers": ["sandbox fetch", "safe web access", "fetch URL safely"],
        "integrations": ["internet-enabler", "web-scraper", "privacy-redactor"],
        "errors": {"Timeout": "Report partial content or suggest alternate source."},
        "gotchas": ["Never pass fetched HTML to exec or eval."],
    },
    "semantic-memory-manager": {
        "description": (
            "Stores and retrieves semantic memory with embeddings and tags. Use for "
            "long-term recall or user says semantic memory, search memory, recall."
        ),
        "workflow": [
            "On store: chunk, tag, score initial trust 5.",
            "On retrieve: query by semantic similarity + tags.",
            "Run memory-sanitizer on all retrievals.",
            "Prune entries older than 90d with trust < 3.",
        ],
        "triggers": ["semantic memory", "search memory", "recall", "store memory"],
        "integrations": ["memory-sanitizer", "persistent-memory-bridge", "knowledge-graph-builder"],
        "errors": {"No match": "Broaden query; suggest manual tags."},
        "gotchas": ["Central memory hub for messenger and healing skills."],
    },
    "skill-creation-enabler": {
        "description": (
            "Scaffolds and installs new skills into .grok/skills/. Use when creating "
            "skills or user says enable skill creation, install skill, new skill."
        ),
        "workflow": [
            "Validate skill name (lowercase-hyphen, unique).",
            "Create directory and SKILL.md from template.",
            "Optionally add references/ and scripts/.",
            "Confirm install path; list in control-overview.",
        ],
        "triggers": ["enable skill creation", "install skill", "new skill", "add skill"],
        "integrations": ["natural-language-to-skill", "hyper-skill-tester", "create-skill"],
        "errors": {"Name collision": "Suggest versioned name or merge."},
        "gotchas": ["Default install: ~/.grok/skills/ or workspace .grok/skills/."],
    },
    "skill-asset-image-processor": {
        "description": (
            "Image processing helper for skill assets: resize, optimize, format convert. "
            "Use when preparing skill images or user says process skill image, optimize asset."
        ),
        "workflow": [
            "Load image from skill assets/ or user path.",
            "Resize to target dimensions (icons: 96px, banners: 720w).",
            "Convert to PNG or SVG as appropriate.",
            "Save alongside SKILL.md; update references.",
        ],
        "triggers": ["process skill image", "optimize asset", "skill icon", "resize skill image"],
        "integrations": ["skill-creation-enabler", "imagine-asset-generator", "safe-image-editor"],
        "errors": {"Unsupported format": "Convert via PNG intermediate."},
        "gotchas": ["Companion to skill-creation-enabler for visual skills."],
    },
    "skill-evolution-engine": {
        "description": (
            "Manages skill version history and automated improvement cycles. Use for "
            "skill maintenance or user says evolve skills, version skills."
        ),
        "workflow": [
            "Snapshot current SKILL.md to versions/.",
            "Run hyper-skill-tester baseline.",
            "Apply evolution proposal from evolution skill.",
            "Compare scores; commit or rollback.",
        ],
        "triggers": ["evolve skills", "version skills", "skill maintenance"],
        "integrations": ["skill-evolver", "evolution", "evolver", "hyper-skill-tester"],
        "errors": {"Score regression": "Auto-rollback to latest versions/ backup."},
        "gotchas": ["Keeps last 10 version backups per skill."],
    },
    "skill-evolver": {
        "description": (
            "Full skill rewrite and improvement with versioned backups and templates. "
            "Use for major skill upgrades or user says evolve skill, upgrade SKILL.md."
        ),
        "workflow": [
            "Backup to versions/<timestamp>/SKILL.md.",
            "Read references/evolution-guide.md for rubric.",
            "Rewrite weak sections per 10-dimension review.",
            "Validate; run hyper-skill-tester; save or rollback.",
        ],
        "triggers": ["evolve skill", "upgrade SKILL.md", "improve skill file"],
        "integrations": ["skill-evolution-engine", "hyper-skill-tester", "natural-language-to-skill"],
        "references": "references/evolution-guide.md",
        "errors": {"Broken frontmatter": "Restore from versions/ immediately."},
        "gotchas": ["Read references/evolution-guide.md before major rewrites."],
    },
    "skill-researcher": {
        "description": (
            "Researches existing skills and best practices before creating new ones. "
            "Use before skill authoring or user says research skills, find skill examples."
        ),
        "workflow": [
            "Search agentskill.sh and local .grok/skills/.",
            "Compare similar skills; note gaps.",
            "Summarize best patterns to adopt.",
            "Recommend install or custom authoring path.",
        ],
        "triggers": ["research skills", "find skill examples", "skill best practices"],
        "integrations": ["natural-language-to-skill", "skill-creation-enabler", "tool-discovery-engine"],
        "errors": {"No matches": "Propose greenfield skill spec."},
        "gotchas": ["Prefer extending existing skills over duplicates."],
    },
    "skill-synergy-orchestrator": {
        "description": (
            "Combines multiple skills into synergistic pipelines. Use when skills "
            "work better together or user says combine skills, skill pipeline."
        ),
        "workflow": [
            "Identify skill chain for goal (e.g. research -> synthesize -> verify).",
            "Define handoff data between skills.",
            "Run pipeline; catch failures at each stage.",
            "Tune order based on bottleneck-resolver feedback.",
        ],
        "triggers": ["combine skills", "skill pipeline", "chain skills", "skill synergy"],
        "integrations": ["adaptive-workflow-composer", "multi-agent-orchestrator", "tool-discovery-engine"],
        "errors": {"Skill missing": "Substitute or install via skill-creation-enabler."},
        "gotchas": ["privacy-redactor should run before any external-facing skill."],
    },
    "telegram-traffic-reports": {
        "description": (
            "Fetches and reports traffic conditions via Telegram bot format. Use for "
            "commute updates or user says telegram traffic, traffic report Telegram."
        ),
        "workflow": [
            "Get user location or route.",
            "Fetch traffic via waze-live-reports or traffic-flight-controller.",
            "Format concise Telegram message with delays and incidents.",
            "Optionally schedule via cron-scheduler.",
        ],
        "triggers": ["telegram traffic", "traffic report Telegram", "commute alert"],
        "integrations": ["waze-live-reports", "traffic-flight-controller", "cron-scheduler", "multi-platform-messenger-bridge"],
        "errors": {"Location missing": "Ask for origin/destination."},
        "gotchas": ["Rate limit Telegram sends to 1/min per chat."],
    },
    "tool-discovery-engine": {
        "description": (
            "Discovers available tools, MCP servers, and skills for a task. Use when "
            "planning work or user says what tools, discover capabilities."
        ),
        "workflow": [
            "Scan MCP tool descriptors and .grok/skills/.",
            "Match task keywords to tools/skills.",
            "Rank by relevance and availability.",
            "Output recommended tool/skill list with paths.",
        ],
        "triggers": ["what tools", "discover capabilities", "find tool for", "available skills"],
        "integrations": ["adaptive-workflow-composer", "control-overview", "skill-researcher"],
        "errors": {"MCP dir missing": "List skills only; note MCP unavailable."},
        "gotchas": ["Always read tool schema before calling MCP tools."],
    },
    "traffic-flight-controller": {
        "description": (
            "Coordinates traffic and navigation data sources for optimal routing info. "
            "Use for commute planning or user says traffic route, best route now."
        ),
        "workflow": [
            "Query waze-live-reports and waze-navigator.",
            "Merge incidents, ETA, alternate routes.",
            "Rank routes by time and reliability.",
            "Present recommendation with confidence.",
        ],
        "triggers": ["traffic route", "best route now", "commute plan", "drive time"],
        "integrations": ["waze-live-reports", "waze-navigator", "telegram-traffic-reports"],
        "errors": {"No route data": "Fallback to straight-line estimate; note limitation."},
        "gotchas": ["Traffic data may be stale; show retrieval time."],
    },
    "user-preference-profiler": {
        "description": (
            "Builds and applies user preference profiles across sessions. Use to "
            "personalize responses or user says my preferences, remember how I like."
        ),
        "workflow": [
            "Extract preferences from conversation (tone, format, tools).",
            "Merge with persistent-memory-bridge store.",
            "Apply profile to current task defaults.",
            "Confirm major preference changes with user.",
        ],
        "triggers": ["my preferences", "remember how I like", "user profile", "personalize"],
        "integrations": ["persistent-memory-bridge", "semantic-memory-manager"],
        "errors": {"Conflicting prefs": "Ask user to resolve."},
        "gotchas": ["Preferences are suggestions, not overrides for safety rules."],
    },
    "video-analyzer": {
        "description": (
            "Analyzes video content for scenes, text, and summaries. Use when user "
            "shares video or says analyze video, what's in this video."
        ),
        "workflow": [
            "Load video or URL; check size limits.",
            "Extract key frames or use video review tools.",
            "Summarize: scenes, spoken content, on-screen text.",
            "Output timestamped highlights.",
        ],
        "triggers": ["analyze video", "what's in this video", "video summary", "review video"],
        "integrations": ["insight-synthesizer", "compliance-image-guard"],
        "errors": {"File too large": "Analyze first 5 minutes only; ask to trim."},
        "gotchas": ["Run compliance check before publishing video-derived content."],
    },
    "voice-synthesis-handler": {
        "description": (
            "Converts agent responses to natural speech output. Use for voice UX or "
            "user says speak response, text to speech, voice output."
        ),
        "workflow": [
            "Format response for spoken delivery (short sentences).",
            "Strip markdown and code blocks for TTS.",
            "Invoke TTS; confirm audio output path or stream.",
            "Offer shorter summary if text exceeds 30 seconds speech.",
        ],
        "triggers": ["speak response", "text to speech", "voice output", "read aloud"],
        "integrations": ["real-time-voice-reasoner", "voice-think-fast-handler"],
        "errors": {"TTS unavailable": "Return text with speakable formatting note."},
        "gotchas": ["Never speak secrets or OTP codes aloud."],
    },
    "voice-think-fast-handler": {
        "description": (
            "Provides quick acknowledgment during voice latency gaps. Use in voice "
            "mode or user says quick ack, thinking aloud, fast think."
        ),
        "workflow": [
            "On voice input received, emit brief ack ('Got it, checking...').",
            "Continue full reasoning in background.",
            "Deliver complete response when ready.",
            "Avoid over-use; max one ack per 10 seconds.",
        ],
        "triggers": ["quick ack", "thinking aloud", "fast think", "voice ack"],
        "integrations": ["real-time-voice-reasoner", "voice-synthesis-handler"],
        "errors": {"Double ack": "Suppress duplicate acks in same turn."},
        "gotchas": ["Acks must not promise outcomes prematurely."],
    },
    "waze-live-reports": {
        "description": (
            "Fetches live Waze traffic incidents and jams for a location. Use for "
            "real-time traffic or user says waze report, live traffic, road incidents."
        ),
        "workflow": [
            "Resolve location to coordinates or area name.",
            "Fetch live incident data via web or API.",
            "Summarize: jams, accidents, road closures.",
            "Include severity and estimated delay.",
        ],
        "triggers": ["waze report", "live traffic", "road incidents", "traffic jams"],
        "integrations": ["waze-navigator", "traffic-flight-controller", "telegram-traffic-reports"],
        "errors": {"Location not found": "Ask user to clarify or share map link."},
        "gotchas": ["Data is third-party; cite source and time."],
    },
    "waze-navigator": {
        "description": (
            "Provides navigation guidance using Waze-style routing context. Use for "
            "turn-by-turn help or user says navigate, waze navigate, directions."
        ),
        "workflow": [
            "Get origin and destination.",
            "Fetch routes via waze-live-reports enrichment.",
            "Present primary route + one alternate.",
            "Update if user reports new incidents.",
        ],
        "triggers": ["navigate", "waze navigate", "directions", "how do I get to"],
        "integrations": ["waze-live-reports", "traffic-flight-controller"],
        "errors": {"Offline": "Provide static route; note no live traffic."},
        "gotchas": ["Do not distract driver; keep responses concise for voice."],
    },
    "web-scraper": {
        "description": (
            "Extracts structured data from web pages. Use when user needs page content "
            "or says scrape page, extract from website, get page data."
        ),
        "workflow": [
            "Fetch via sandbox-internet-handler or WebFetch.",
            "Parse HTML to text, tables, or JSON per user spec.",
            "Respect robots.txt and rate limits.",
            "Return data with source URL and timestamp.",
        ],
        "triggers": ["scrape page", "extract from website", "get page data", "web extract"],
        "integrations": ["sandbox-internet-handler", "humanization-stealth-browsing", "internet-enabler"],
        "errors": {"Blocked by site": "Try stealth mode or ask user for export."},
        "gotchas": ["Never scrape authenticated pages without user session."],
    },
    "workflow-composer": {
        "description": (
            "Composes linear and branching workflows from goals and constraints. Use "
            "when planning multi-step work or user says compose workflow, build plan."
        ),
        "workflow": [
            "Define goal, constraints, and success criteria.",
            "Break into steps with inputs/outputs per step.",
            "Assign skills or tools per step.",
            "Output markdown workflow doc with checklist.",
        ],
        "triggers": ["compose workflow", "build plan", "workflow plan", "step by step plan"],
        "integrations": ["adaptive-workflow-composer", "goal-verifier", "skill-synergy-orchestrator"],
        "errors": {"Scope creep": "Cap at 15 steps; split into phases if larger."},
        "gotchas": ["workflow-composer is linear; use adaptive-workflow-composer for DAGs."],
    },
}


def format_skill_md(name: str, spec: dict) -> str:
    desc = spec["description"]
    triggers = spec.get("triggers", [])
    workflow = spec["workflow"]
    errors = spec.get("errors", {})
    integrations = spec.get("integrations", [])
    gotchas = spec.get("gotchas", [])
    references = spec.get("references")
    output_template = spec.get("output_template")

    trigger_str = ", ".join(triggers[:6])
    related = ", ".join(integrations[:8])

    lines = [
        "---",
        f"name: {name}",
        "description: >",
    ]
    for para_line in textwrap.wrap(desc, width=78):
        lines.append(f"  {para_line}")
    lines.extend([
        "version: 1.1.0",
        "author: Stijnman",
        "license: MIT",
        "metadata:",
        "  grok:",
        f"    tags: [{trigger_str}]",
        f"    related_skills: [{related}]",
        "---",
        "",
        f"# {name.replace('-', ' ').title()}",
        "",
        "## When to Use",
        "",
    ])
    for t in triggers:
        lines.append(f"- User says **{t}** or task matches this capability")
    lines.extend(["", "## Workflow", ""])
    for i, step in enumerate(workflow, 1):
        lines.append(f"{i}. {step}")
    if output_template:
        lines.extend(["", "## Output Template", "", "```", output_template, "```"])
    if references:
        lines.extend([
            "",
            "## References",
            "",
            f"Read `{references}` when setup, backends, or rubric details are needed.",
        ])
    lines.extend(["", "## Integrations", ""])
    for skill in integrations:
        lines.append(f"- `{skill}`")
    lines.extend(["", "## Error Handling", "", "| Failure | Response |", "|---------|----------|"])
    for err, resp in errors.items():
        lines.append(f"| {err} | {resp} |")
    lines.extend(["", "## Gotchas", ""])
    for g in gotchas:
        lines.append(f"- {g}")
    lines.extend([
        "",
        "## Example",
        "",
        "**Input:** User request matching triggers above.",
        "**Output:** Structured result per workflow with integrations invoked as needed.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    count = 0
    for name, spec in sorted(SKILLS.items()):
        skill_dir = ROOT / name
        skill_dir.mkdir(parents=True, exist_ok=True)
        path = skill_dir / "SKILL.md"
        path.write_text(format_skill_md(name, spec), encoding="utf-8")
        count += 1
        print(f"  wrote {path.relative_to(ROOT.parent.parent)}")
    print(f"\nTotal: {count} skills")


if __name__ == "__main__":
    main()