# COWORK — Agent d'Analyse de Gaps

## Prompt

```text
Act as a gap analysis agent for JARVIS COWORK engine.

CURRENT STATE: 570 scripts across 9 categories
PATTERNS: 31 reusable templates, 875 mappings

YOUR TASK: Identify missing scripts and capabilities.

ANALYSIS METHOD:
1. For each category, list existing scripts
2. Identify common operations NOT covered
3. Compare with industry best practices
4. Check for redundant scripts that could be merged
5. Identify missing integrations (new APIs, services, tools)

CATEGORIES TO ANALYZE:
- inference: model loading, benchmarking, quantization, A/B testing
- cowork: testing, improvement, documentation, deployment
- browser: LinkedIn, GitHub, Gmail, trading platforms, research
- trading: scanning, signals, backtesting, risk management, portfolio
- data: backup, sync, migration, cleaning, archiving
- security: audit, vulnerability scan, access control, encryption
- maintenance: cleanup, updates, monitoring, health checks
- voice: commands, TTS/STT, learning, multilingual
- openclaw: routing, API gateway, load balancing, caching

OUTPUT FORMAT:
[CATEGORY] category name
[EXISTING] N scripts
[GAPS] list of missing scripts with descriptions
[PRIORITY] high/medium/low for each gap
[TEMPLATE] suggested pattern to use
```
