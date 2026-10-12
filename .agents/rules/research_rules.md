---
description: Rules defining general research behaviors and constraints. Must remain active during all research tasks.
trigger: always_on
---

# General Research Behaviors and Operational Limits (Research Rules)

When executing research in this workspace, you must follow these operational rules:

## 1. Unrestricted Multilingual Scanning
* Unless the user specifies a specific language constraint, execute web searches and queries across multiple languages (prioritizing English).
* Prioritize sources where the highest quality technical data exists.

## 2. Deterministic Depth and Rigor
* When a task specifies a deterministic depth limit (e.g., "verify 100 sources"), continue research until you reach that count or verify that no further sources exist. Do not stop early.
* When reading sources with web extraction tools, evaluate source quality and factual validity, and persist each record into the local SQLite database.

## 3. Context Memory Protection
* Never load voluminous raw text or full HTML dumps into your context memory window or Markdown reports.
* Stream extracted text directly to SQLite with minimal summaries; retain only the final synthesized analysis in context.

## 4. Operational Autonomy
* During research execution, do not ask the user iterative approval questions. Boundary parameters are established during scoping; make independent decisions within those boundaries and present final results.

## 5. Zero Simulation and Real Data Invariant (Anti-Mock Invariant)
* **Never Generate Synthetic or Mock Data:** You must never populate the database or analysis pool with algorithmically fabricated, mock, or simulated records.
* **Every Source Must Be Real and Verifiable:** Every entry must originate from a live HTTP/API request; save authentic URLs, live metrics, and real raw content (e.g., README or technical specs) into the SQLite database.
* **Strict Evaluation Invariant:** Simulating document parsing with local heuristics to save tokens or time is strictly prohibited. You must actually fetch and parse each candidate source.
* **Authentic Multi-Agent Execution:** When a multi-agent workflow is requested, stages must execute as authentic subagent invocations (`invoke_subagent`) or discrete API analysis pipelines, never mocked labels.

## 6. Master Registry and Metrics Commitment (Master DB Registry)
* **Permanent Auditing:** When research completes, in addition to local `data.db` and `report.md` files, record the scanned source count (`sources_scanned_count`), analyzed source count (`sources_analyzed_count`), methodological approach, data volume, and efficiency scores in the central database (`research_master.db`).
* **Completion Gate:** A research track cannot be marked `COMPLETED` without a registered entry in `research_master.db` via `scripts/master_db_manager.py`.
