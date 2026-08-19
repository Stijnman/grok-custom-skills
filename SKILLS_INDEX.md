# Skills Catalog

This catalog is generated from the metadata in **89 skill definitions**. Run `python3 scripts/generate_catalog.py` after adding or changing a skill.

## Browse by category

| Category | Skills |
|---|---:|
| General Utilities | 14 |
| Media, Voice & Visuals | 6 |
| Memory, Context & Knowledge | 7 |
| Messaging & Communication | 5 |
| Quality, Code & Performance | 6 |
| Research, Web & Integrations | 13 |
| Safety, Privacy & Governance | 7 |
| Skill Development & Operations | 17 |
| Traffic & Navigation | 3 |
| Workflow & Agent Orchestration | 11 |

## Complete catalog

### General Utilities

| Skill | Description |
|---|---|
| [`accessible-color-review`](.grok/skills/accessible-color-review/SKILL.md) | Review color choices for contrast, semantic consistency, color-vision accessibility, and readable user-interface states. Use for: color accessibility review, contrast check, UI color audit, accessible palette. |
| [`architecture-decision-record`](.grok/skills/architecture-decision-record/SKILL.md) | Document a significant technical decision with its context, alternatives, consequences, and status. Use for: architecture decision record, ADR, technical decision log, technology choice. |
| [`beta-unlocker`](.grok/skills/beta-unlocker/SKILL.md) | Guides enabling beta or experimental Grok features safely. Use for: beta feature, early access, unlock experimental, enable beta. |
| [`contact-vcard-export`](.grok/skills/contact-vcard-export/SKILL.md) | Create a validated vCard contact-export file from contact details that the user has explicitly selected and confirmed. Use for: create VCF, export contacts, vCard file, contact import file. |
| [`control-overview`](.grok/skills/control-overview/SKILL.md) | Provides control-panel overview of active skills, workflows, and status. Use for: overview, status dashboard, what skills, control panel. |
| [`cron-scheduler`](.grok/skills/cron-scheduler/SKILL.md) | Schedules recurring or delayed agent tasks. Use for: schedule this, run daily, cron job, set timer. |
| [`dspy-prompt-optimizer`](.grok/skills/dspy-prompt-optimizer/SKILL.md) | Tunes prompts iteratively using reflection and success metrics. Use for: optimize this prompt, dspy tune, improve prompt with reflection, `self-refine-loop`. |
| [`experiment-results-analysis`](.grok/skills/experiment-results-analysis/SKILL.md) | Analyze completed experiment results with effect sizes, uncertainty, guardrails, limitations, and evidence-based next steps. Use for: experiment results, A/B test analysis, test readout, experiment decision. |
| [`exposed-service-triage`](.grok/skills/exposed-service-triage/SKILL.md) | Triages exposed TCP listeners found by security audits. Use for: exposed port, what is listening, fix exposed service, open port. |
| [`imagine-asset-generator`](.grok/skills/imagine-asset-generator/SKILL.md) | Generates visual assets via image generation tools. Use for: generate image, create asset, make icon, design mockup. |
| [`oss-repo-maintainer`](.grok/skills/oss-repo-maintainer/SKILL.md) | Maintain open-source repositories by checking README accuracy, version consistency, release readiness, and documentation drift. Use for: fix README, prepare release, repository maintenance, sync documentation. |
| [`product-opportunity-tree`](.grok/skills/product-opportunity-tree/SKILL.md) | Map a measurable product outcome to customer opportunities, solution options, and assumption tests. Use for: opportunity solution tree, product discovery map, customer opportunity mapping, outcome-to-solution planning. |
| [`product-requirements-document`](.grok/skills/product-requirements-document/SKILL.md) | Write a clear product requirements document that defines the problem, scope, requirements, success measures, risks, and open questions. Use for: product requirements document, PRD, feature specification, engineering handoff. |
| [`ringtwice-power-suite`](.grok/skills/ringtwice-power-suite/SKILL.md) | Support service providers with clear, platform-compliant RingTwice profile copy, job evaluation, customer communication, and service planning. Use for: RingTwice profile, job evaluation, service quote draft, customer message, review response. |

### Media, Voice & Visuals

| Skill | Description |
|---|---|
| [`real-time-voice-reasoner`](.grok/skills/real-time-voice-reasoner/SKILL.md) | Handles real-time voice input with low-latency reasoning. Use for: voice mode, speak and reason, voice assistant, listen. |
| [`safe-image-editor`](.grok/skills/safe-image-editor/SKILL.md) | Edits images with policy and quality guardrails. Use for: edit image, safe edit, adjust photo, modify image. |
| [`suno`](.grok/skills/suno/SKILL.md) | Turn a real-life story into structured, safety-filtered song lyrics and a Suno-ready style prompt. Use for: song lyrics, story to song, Suno prompt. |
| [`video-analyzer`](.grok/skills/video-analyzer/SKILL.md) | Analyzes video content for scenes, text, and summaries. Use for: analyze video, what's in this video, video summary, review video. |
| [`voice-synthesis-handler`](.grok/skills/voice-synthesis-handler/SKILL.md) | Converts agent responses to natural speech output. Use for: speak response, text to speech, voice output, read aloud. |
| [`voice-think-fast-handler`](.grok/skills/voice-think-fast-handler/SKILL.md) | Provides quick acknowledgment during voice latency gaps. Use for: quick ack, thinking aloud, fast think, voice ack. |

### Memory, Context & Knowledge

| Skill | Description |
|---|---|
| [`knowledge-graph-builder`](.grok/skills/knowledge-graph-builder/SKILL.md) | Builds structured knowledge graphs from text and sessions. Use for: knowledge graph, map entities, build graph, entity map. |
| [`mega-context-manager`](.grok/skills/mega-context-manager/SKILL.md) | Manages large context windows via chunking, summarization, and retrieval. Use for: manage context, too much context, chunk document, context budget. |
| [`memory-sanitizer`](.grok/skills/memory-sanitizer/SKILL.md) | Scores and filters retrieved memory against trust and poisoning risk. Use for: sanitize memory, trust score retrieval, clean knowledge graph, `semantic-memory-manager`. |
| [`predictive-cache-manager`](.grok/skills/predictive-cache-manager/SKILL.md) | Caches frequent tool results and prefetches likely next requests. Use for: cache results, prefetch, reuse cache, avoid repeat fetch. |
| [`semantic-memory-manager`](.grok/skills/semantic-memory-manager/SKILL.md) | Stores and retrieves semantic memory with embeddings and tags. Use for: semantic memory, search memory, recall, store memory. |
| [`session-handoff-packager`](.grok/skills/session-handoff-packager/SKILL.md) | Packages session work into a local handoff document for continuity. Use for: session summary, handoff, save what we did, continue next time. |
| [`user-preference-profiler`](.grok/skills/user-preference-profiler/SKILL.md) | Builds and applies user preference profiles across sessions. Use for: my preferences, remember how I like, user profile, personalize. |

### Messaging & Communication

| Skill | Description |
|---|---|
| [`ai-share-extractor-v4`](.grok/skills/ai-share-extractor-v4/SKILL.md) | Extracts shareable insights from long agent sessions for export. Use for: extract shares, shareable summary, export insights, `privacy-redactor`. |
| [`telegram-traffic-reports`](.grok/skills/telegram-traffic-reports/SKILL.md) | Fetches and reports traffic conditions via Telegram bot format. Use for: telegram traffic, traffic report Telegram, commute alert, `waze-live-reports`. |
| [`text-humanizer`](.grok/skills/text-humanizer/SKILL.md) | Improve text so it sounds natural, clear, and appropriate for its intended audience while preserving the author's meaning. Use for: tone adjustment, readability, natural writing, English, Dutch. |
| [`whatsapp-auto-responder`](.grok/skills/whatsapp-auto-responder/SKILL.md) | Drafts and optionally sends WhatsApp replies with rater and HITL gates. Use for: auto reply WhatsApp, enable WhatsApp assistant, reply on WhatsApp, `whatsapp-message-rater`. |
| [`whatsapp-message-rater`](.grok/skills/whatsapp-message-rater/SKILL.md) | Rates WhatsApp messages for sentiment, urgency, and spam likelihood. Use for: rate this WhatsApp, analyze chat sentiment, score message urgency, `whatsapp-auto-responder`. |

### Quality, Code & Performance

| Skill | Description |
|---|---|
| [`auto-tester`](.grok/skills/auto-tester/SKILL.md) | Runs validation tests on code, skills, or outputs after changes. Use for: run tests, auto test, validate changes, check tests. |
| [`code-reviewer`](.grok/skills/code-reviewer/SKILL.md) | Reviews code changes for bugs, style, security, and maintainability. Use for: review code, code review, check my PR, review my changes. |
| [`data-visualizer`](.grok/skills/data-visualizer/SKILL.md) | Creates charts and visual summaries from tabular or numeric data. Use for: visualize data, chart this, plot results, graph this. |
| [`goal-verifier`](.grok/skills/goal-verifier/SKILL.md) | Verifies task completion against stated goals before marking work done. Use for: verify goal, confirm success, did I achieve this, check if done. |
| [`insight-synthesizer`](.grok/skills/insight-synthesizer/SKILL.md) | Synthesizes findings from multiple sources into actionable insights. Use for: synthesize, key takeaways, summarize findings, insight report. |
| [`performance-optimizer`](.grok/skills/performance-optimizer/SKILL.md) | Optimizes agent and code performance via profiling and tuning. Use for: optimize performance, make faster, performance tune, `bottleneck-resolver`. |

### Research, Web & Integrations

| Skill | Description |
|---|---|
| [`computer-use-bridge`](.grok/skills/computer-use-bridge/SKILL.md) | Bridges desktop automation to agent tool calls. Use for: computer use, desktop control, click on screen, GUI automation. |
| [`connected-services-bridge`](.grok/skills/connected-services-bridge/SKILL.md) | Connects approved external services such as Drive, GitHub, Notion, calendars, SharePoint, and Outlook through their available connectors. Use for: discovering connected-service capabilities, preparing a scoped integration, or completing a user-approved external action. |
| [`deep-search-enabler`](.grok/skills/deep-search-enabler/SKILL.md) | Enables thorough multi-source research beyond quick answers. Use for: deep search, comprehensive research, research thoroughly, `internet-enabler`. |
| [`drive-persistence-bridge`](.grok/skills/drive-persistence-bridge/SKILL.md) | Creates, verifies, restores, or synchronizes user-approved backups and artifacts with connected cloud storage or a repository. Use for: backing up files, preparing a restore, comparing versions, or uploading a specifically approved artifact. |
| [`github-repo-scout`](.grok/skills/github-repo-scout/SKILL.md) | Investigate a GitHub repository from a URL by reviewing its README, file tree, local clone status, and recommended next steps. Use for: GitHub URL, check this repository, scout repository, understand this project. |
| [`hybrid-execution-bridge`](.grok/skills/hybrid-execution-bridge/SKILL.md) | Coordinate authorized work across sandbox tools, a user-approved local desktop, connected services, and public-web research. Use for: hybrid execution, local plus sandbox, connected services, scoped desktop access. |
| [`internet-enabler`](.grok/skills/internet-enabler/SKILL.md) | Ensures web access is used effectively for live information. Use for: search web, need internet, look up online, current info. |
| [`mcp-tool-scout`](.grok/skills/mcp-tool-scout/SKILL.md) | Discovers MCP servers and reads tool schemas before calling MCP tools. Use for: mcp tools, MCP schema, discover MCP, which MCP tool. |
| [`multi-platform-messenger-bridge`](.grok/skills/multi-platform-messenger-bridge/SKILL.md) | Unify WhatsApp, Telegram, and future channels with shared conversation context and message-quality assessment. Use for: bridge messengers, unified chat memory, cross-platform reply, WhatsApp responder. |
| [`persistent-memory-bridge`](.grok/skills/persistent-memory-bridge/SKILL.md) | Bridges session memory to persistent storage across conversations. Use for: remember this, persistent memory, save to memory, recall later. |
| [`research-interview-synthesis`](.grok/skills/research-interview-synthesis/SKILL.md) | Synthesize multiple user interviews into evidence-backed themes, insights, limitations, and next research actions. Use for: interview synthesis, customer research findings, usability study themes, discovery interview analysis. |
| [`tool-discovery-engine`](.grok/skills/tool-discovery-engine/SKILL.md) | Discovers available tools, MCP servers, and skills for a task. Use for: what tools, discover capabilities, find tool for, available skills. |
| [`web-scraper`](.grok/skills/web-scraper/SKILL.md) | Extracts structured data from web pages. Use for: scrape page, extract from website, get page data, web extract. |

### Safety, Privacy & Governance

| Skill | Description |
|---|---|
| [`compliance-image-guard`](.grok/skills/compliance-image-guard/SKILL.md) | Checks images for policy compliance before generation or publish. Use for: compliance check, safe image, image policy, can I publish this. |
| [`defensive-mcp-audit`](.grok/skills/defensive-mcp-audit/SKILL.md) | Run a defensive, read-only audit of local MCP and AI-agent exposure, including risky bindings, configuration issues, and confused-deputy risks. Use for: audit MCP, MCP security, localhost exposure, defensive MCP audit. |
| [`hitl-approver`](.grok/skills/hitl-approver/SKILL.md) | Pauses high-risk actions for explicit human approval. Use for: approve this, hitl check, human review needed, confirm before send. |
| [`humanization-stealth-browsing`](.grok/skills/humanization-stealth-browsing/SKILL.md) | Apply respectful, rate-limited browsing practices for public websites while honoring site rules and access controls. Use for: responsible web research, rate limiting, CAPTCHA stop, robots.txt. |
| [`ollama-localhost-guardian`](.grok/skills/ollama-localhost-guardian/SKILL.md) | Verify that local LLM services, including Ollama, are bound and configured safely before they are exposed or connected. Use for: Ollama security, check exposed Ollama, secure local LLM, Ollama localhost. |
| [`privacy-redactor`](.grok/skills/privacy-redactor/SKILL.md) | Detects and redacts PII in inputs and outputs before external actions. Use for: redact PII, privacy check, sanitize this, remove personal data. |
| [`sandbox-internet-handler`](.grok/skills/sandbox-internet-handler/SKILL.md) | Fetches web content in a sandboxed, read-only manner. Use for: sandbox fetch, safe web access, fetch URL safely, `internet-enabler`. |

### Skill Development & Operations

| Skill | Description |
|---|---|
| [`auto-skill-resolver`](.grok/skills/auto-skill-resolver/SKILL.md) | Plan and coordinate skill-library improvements by identifying gaps, overlaps, and the safest next action. Use for: skill gap analysis, resolve missing capability, skill-library cleanup, skill planning. |
| [`drive-github-skill-audit`](.grok/skills/drive-github-skill-audit/SKILL.md) | Compare Google Drive skill definitions with a GitHub skills repository and identify Drive skills not yet published. Use for: audit Drive skills, compare Drive and GitHub SKILL.md files, find unpublished skills, skill-library inventory. |
| [`evolution`](.grok/skills/evolution/SKILL.md) | Tracks incremental improvements to skills and workflows over time. Use for: evolve skill, track evolution, improve over time, `skill-evolver`. |
| [`evolver`](.grok/skills/evolver/SKILL.md) | Lightweight skill mutation helper for quick iterations. Use for: quick evolve, mutate skill, tweak skill, `skill-evolver`. |
| [`hyper-skill-tester`](.grok/skills/hyper-skill-tester/SKILL.md) | Stress-tests skills with edge-case prompts and scoring rubric. Use for: test skill, hyper test, skill QA, audit skill quality. |
| [`natural-language-to-skill`](.grok/skills/natural-language-to-skill/SKILL.md) | Converts natural language descriptions into SKILL.md drafts. Use for: create skill from description, NL to skill, skill from prompt, `skill-creation-enabler`. |
| [`skill-asset-image-processor`](.grok/skills/skill-asset-image-processor/SKILL.md) | Image processing helper for skill assets: resize, optimize, format convert. Use for: process skill image, optimize asset, skill icon, resize skill image. |
| [`skill-auditor`](.grok/skills/skill-auditor/SKILL.md) | Audit a SKILL.md definition for reliability, security, testability, workflow clarity, and production readiness, then prioritize concrete improvements. Use for: audit this skill, review SKILL.md, score skill quality, adversarial skill test. |
| [`skill-collection-bootstrapper`](.grok/skills/skill-collection-bootstrapper/SKILL.md) | Audit a skills repository, identify coverage gaps, validate SKILL.md files, and prepare an approval-gated installation plan. Use for: bootstrap skills, complete skill collection, install skill repository, validate skill library. |
| [`skill-creation-enabler`](.grok/skills/skill-creation-enabler/SKILL.md) | Identify coverage gaps and maintenance opportunities in a skill library, then prepare an approval-gated creation or improvement plan. Use for: skill gap analysis, missing capability, library health check, skill maintenance. |
| [`skill-creator`](.grok/skills/skill-creator/SKILL.md) | Create or improve reusable skill packages with clear metadata, focused workflows, and appropriate safety boundaries. Use for: create skill, update skill, skill package, new capability. |
| [`skill-evolution-engine`](.grok/skills/skill-evolution-engine/SKILL.md) | Manages skill version history and automated improvement cycles. Use for: evolve skills, version skills, skill maintenance, `skill-evolver`. |
| [`skill-evolver`](.grok/skills/skill-evolver/SKILL.md) | Full skill rewrite and improvement with versioned backups and templates. Use for: evolve skill, upgrade SKILL.md, improve skill file, `skill-evolution-engine`. |
| [`skill-marketplace-installer`](.grok/skills/skill-marketplace-installer/SKILL.md) | Safely search and install agent skills from public marketplaces with explicit user consent and security checks. Use for: find skill, install skill, skill marketplace, check skill safety. |
| [`skill-researcher`](.grok/skills/skill-researcher/SKILL.md) | Researches existing skills and best practices before creating new ones. Use for: research skills, find skill examples, skill best practices, `natural-language-to-skill`. |
| [`skill-rubric-reviewer`](.grok/skills/skill-rubric-reviewer/SKILL.md) | Reviews SKILL.md files against a 10-dimension quality rubric inspired by the Agent Skills specification. Use for: review skill, skill rubric, audit SKILL.md, score skill quality. |
| [`skill-synergy-orchestrator`](.grok/skills/skill-synergy-orchestrator/SKILL.md) | Combines multiple skills into synergistic pipelines. Use for: combine skills, skill pipeline, chain skills, skill synergy. |

### Traffic & Navigation

| Skill | Description |
|---|---|
| [`traffic-flight-controller`](.grok/skills/traffic-flight-controller/SKILL.md) | Coordinates traffic and navigation data sources for optimal routing info. Use for: traffic route, best route now, commute plan, drive time. |
| [`waze-live-reports`](.grok/skills/waze-live-reports/SKILL.md) | Fetches live Waze traffic incidents and jams for a location. Use for: waze report, live traffic, road incidents, traffic jams. |
| [`waze-navigator`](.grok/skills/waze-navigator/SKILL.md) | Provides navigation guidance using Waze-style routing context. Use for: navigate, waze navigate, directions, how do I get to. |

### Workflow & Agent Orchestration

| Skill | Description |
|---|---|
| [`adaptive-workflow-composer`](.grok/skills/adaptive-workflow-composer/SKILL.md) | Composes multi-step agent workflows from goals and available skills. Use for: compose workflow, plan steps, adaptive pipeline, orchestrate task. |
| [`agentic-uncertainty-quantifier`](.grok/skills/agentic-uncertainty-quantifier/SKILL.md) | Scores task uncertainty to calibrate memory depth and iteration count. Use for: quantify uncertainty, fast slow think, uncertainty score, how sure. |
| [`bottleneck-resolver`](.grok/skills/bottleneck-resolver/SKILL.md) | Identifies and resolves performance bottlenecks in agent workflows. Use for: find bottleneck, speed up, why so slow, optimize workflow. |
| [`desktop-subagent-connector`](.grok/skills/desktop-subagent-connector/SKILL.md) | Securely coordinate a remote sandbox with a user-approved local desktop through scoped file, shell, browser, and GUI access. Use for: remote sandbox, user-approved desktop, local desktop bridge, scoped desktop access. |
| [`multi-agent-coordinator`](.grok/skills/multi-agent-coordinator/SKILL.md) | Coordinates multiple agents with role assignment and handoffs. Use for: coordinate agents, multi agent team, agent roles, delegate agents. |
| [`multi-agent-orchestrator`](.grok/skills/multi-agent-orchestrator/SKILL.md) | Orchestrates complex multi-agent pipelines with DAG execution. Use for: orchestrate agents, agent pipeline, multi step agents, `multi-agent-coordinator`. |
| [`parallel-tool-orchestrator`](.grok/skills/parallel-tool-orchestrator/SKILL.md) | Runs independent tool calls in parallel for latency reduction. Use for: parallel tools, run concurrently, batch requests, parallelize. |
| [`self-healing-error-recovery`](.grok/skills/self-healing-error-recovery/SKILL.md) | Diagnoses failures and retries with alternate strategies. Use for: heal this error, self recover, fix failure automatically, retry smart. |
| [`self-refine-loop`](.grok/skills/self-refine-loop/SKILL.md) | Runs a generator-critique-reviser loop to iteratively improve agent outputs. Use for: self refine, reflexion loop, critique and revise, improve output. |
| [`voice-agent-design`](.grok/skills/voice-agent-design/SKILL.md) | Design a safe, vendor-neutral voice agent with conversation flows, consent notices, escalation paths, and approval-gated actions. Use for: voice agent design, phone assistant, call flow, conversational IVR. |
| [`workflow-composer`](.grok/skills/workflow-composer/SKILL.md) | Composes linear and branching workflows from goals and constraints. Use for: compose workflow, build plan, workflow plan, step by step plan. |
