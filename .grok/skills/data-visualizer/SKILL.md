---
name: data-visualizer
description: >
  Creates charts and visual summaries from tabular or numeric data. Use when u
  ser says visualize data, chart this, plot results. Triggers: visualize data,
   chart this, plot results, graph this.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [visualize data, chart this, plot results, graph this]
    related_skills: [xlsx, insight-synthesizer]
compatibility: Grok agent; optional MCP and shell access
---

# Data Visualizer

## When to Use

- User says **visualize data** or task matches this capability
- User says **chart this** or task matches this capability
- User says **plot results** or task matches this capability
- User says **graph this** or task matches this capability

## Workflow

1. Parse data source (CSV, JSON, spreadsheet).
2. Choose chart type: bar, line, pie, scatter (default bar for categories).
3. Generate visualization code or image.
4. Include title, labels, and one-sentence insight.

## Integrations

- `xlsx`
- `insight-synthesizer`

## Error Handling

| Failure | Response |
|---------|----------|
| Malformed data | Show first 5 rows; ask user to fix format. |

## Gotchas

- Prefer code-generated charts over hand-drawn ASCII for accuracy.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
