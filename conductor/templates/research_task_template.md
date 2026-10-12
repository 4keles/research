# Research Task Template

This template defines the standard configuration and operational boundaries for an autonomous research engagement.

## 1. Core Parameters

* **Topic:** [Primary research subject or domain, e.g., Embedded Memory Architectures]
* **Depth Limit (Verifiable Sources):** [Minimum verified source count, e.g., 100 sources]
* **Contextual Constraints:** [Deterministic boundary conditions, e.g., "Published after 2024", "Permissive open-source licenses only"]
* **Languages:** [Search languages: All, English, or specific ISO language codes]
* **Reasoning Method:** [Selected reasoning framework: Macro-to-Micro Deductive Sequential Thinking]
* **Methodological Approach:** [e.g., Multi-Agent Funnel Optimization, Protocol Benchmarking]
* **Agent Architecture:** [e.g., Single Lead Researcher, Multi-Agent Swarm]
* **Creation Date:** [YYYY-MM-DD]

## 2. Directory and Data Management

* **Output Directory:** `[ID]-[Date]-[Research_Name]` (e.g., `RES010-20261015-memory-architectures`)
* **Persistence Rules:**
  * Raw extraction dumps, candidate matrices, and full-text copies must reside in the local **SQLite Database (`data.db`)**.
  * The synthesized executive summary must reside in the root of the task folder as **Markdown (`report.md`)**.
  * Upon task completion, research metadata and metrics must be registered in the central audit database (`research_master.db`).

## 3. Dynamic Execution Steps

*(Populated dynamically during the pre-flight requirements interview.)*

### Scoping Interview Questions:
1. **[Scope]:** What exact sub-domains and technical boundaries define this investigation?
2. **[Constraints]:** What deterministic filtering criteria (dates, licenses, architecture types) apply?
3. **[Output Format]:** What level of technical depth, benchmark tables, and code samples are required?

### Synthesized Execution Steps:
1. [Step 1: Primary Data Collection & Scanning]
2. [Step 2: Deep Extraction & Multi-Criteria Filtering]
3. [Step 3: Synthesis Report (`report.md`) & SQLite Database (`data.db`) Finalization]
4. **[Mandatory Checkpoint]:** Commit research metadata and metrics to `research_master.db` via `scripts/master_db_manager.py`.

## 4. Master Registry Metrics Checkpoint

Upon completion, record these parameters in `research_master.db`:
- **Scanned Source Count (`sources_scanned_count`):** Total URLs or candidates scanned.
- **Analyzed Source Count (`sources_analyzed_count`):** Candidates subjected to full-text technical extraction.
- **Analyzed Volume (`total_volume_analyzed`):** e.g., "1.8M words", "240 repositories".
- **Agent Count (`agent_count`):** Number of active subagents utilized.
- **Execution Layers (`execution_layers_count`):** Number of funnel stages applied.
- **Local DB Rows (`local_db_records_count`):** Total rows persisted in local `data.db`.
- **Efficiency Score & Notes (`efficiency_score`, `efficiency_notes`):** Context optimization notes and anti-mock compliance records.

---
*Note: Using Sequential Thinking and synchronizing final metrics with `research_master.db` is strictly required.*
