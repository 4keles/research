# Research Directory and Data Management Standards

This document defines directory structure and data persistence standards for research tasks. The agent must strictly adhere to this layout during file operations and database initialization.

## 1. Directory Naming Convention
Create an isolated, unique directory within the workspace for each research task.

**Format:** `{Task_ID}-{Date}-{Research_Name}`
* **Task_ID:** Short task identifier (e.g., `TASK01` or `RES001`)
* **Date:** `YYYYMMDD` format (e.g., `20260901`)
* **Research_Name:** Kebab-case concise topic slug (e.g., `distributed-memory-systems`)

**Example:** `RES001-20260901-distributed-memory-systems/`

## 2. Directory Hierarchy and Content Separation

Maintain strict separation between synthesized reports and raw extracted records:

```text
RES001-20260901-distributed-memory-systems/
├── report.md           # [MANDATORY] Final synthesis and executive summary (user-facing)
├── data.db             # [MANDATORY] SQLite database containing raw dumps, URLs, and metrics
└── assets/             # [OPTIONAL] Visual diagrams, charts, and architecture schematics
```

## 3. Core Storage Rules (Markdown vs. Database)

### Markdown (`report.md`)
* **Purpose:** Distilled, human-readable final technical report.
* **Content:** Synthesized findings, architecture trade-offs, decision matrices, and curated source citations.
* **Constraint:** Do not include raw full-page text dumps, massive link logs, or unparsed JSON payloads.

### SQLite Database (`data.db`)
* **Purpose:** Structured, permanent store for all raw text, extracted metadata, and intermediate analysis records.
* **Content:**
  * Examined URLs, HTTP status codes, and timestamps.
  * Raw extracted page text, technical specifications, and repository documentation.
  * Agent sequential thinking telemetry and subagent logs.
  * Verification scores, authorship metadata, and citation data.
* **Rule:** Regardless of research depth (e.g., 100 or 1,000 sources), route all raw data directly into `data.db` to prevent context memory overflow.

---

## 4. Master Registry Synchronization (`research_master.db`)

After populating `report.md` and `data.db`, log the task to the root audit database to mark it complete:

* **Database Path:** `/home/kayra/research/research_master.db`
* **Registry Tool:** `python3 scripts/master_db_manager.py`
* **Registered Parameters:**
  1. `research_id` and `track_code` (e.g., `RES001-20260901-ai-enerji`, `RES001`)
  2. `methodological_approach` (e.g., Deductive Sequential Funnel, Multi-Agent Swarm)
  3. `sources_scanned_count` (Total primary URLs/candidates scanned)
  4. `sources_analyzed_count` (Candidates subjected to deep full-text parsing)
  5. `total_volume_analyzed` (Total word or document volume parsed)
  6. `local_db_records_count` (Row count in local `data.db`)
  7. `efficiency_score` and `efficiency_notes` (Context efficiency and optimization notes)
  8. `summary` and `key_findings` (Executive summary and core takeaways)
