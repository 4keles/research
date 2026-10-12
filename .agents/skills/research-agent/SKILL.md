---
name: research-agent
description: Conductor-standard autonomous deep research skill executing multi-agent optimization and deductive sequential thinking.
---

# Research Agent & Multi-Agent Orchestration

As the **Principal Research and Performance Engineer**, you orchestrate autonomous technical research workflows. When a research task is requested (e.g., "Research X", "Analyze 1,000 repositories"), apply these procedures and **Multi-Agent Optimization** principles:

---

## 1. Scoping and Task Specification (Requirements Analysis)
* Read the scoping directives in `conductor/templates/dynamic_task_prompt.md`.
* Query the user with interactive modal dialogs according to the scoping rules.
* Populate the task template using `conductor/templates/research_task_template.md` and obtain final user confirmation.

---

## 2. Directory and Database Isolation
* Once confirmed, generate a unique directory (`[ID]-[Date]-[Research_Name]`) according to `conductor/templates/directory_structure_standard.md`.
* **Database Setup:** Initialize the local SQLite database (`data.db`) and configure **WAL mode** and a busy timeout to permit concurrent agent operations:
  ```python
  conn.execute("PRAGMA journal_mode=WAL;")
  conn.execute("PRAGMA busy_timeout=30000;")
  ```

---

## 3. Multi-Agent Optimization Principles

Apply `agent-orchestration-multi-agent-optimize` standards to all research operations:

### A. Zero Simulation and Real Data Invariant (Anti-Mock Invariant)
* **Never Generate Synthetic or Mock Data:** Never populate database tables with algorithmically fabricated, mock, or simulated records.
* **Live API and Web Scraping:** Every source must be extracted through live APIs (GitHub API, Arxiv, web scraping). Extract authentic URLs, verified metrics, and real raw content (such as `README.md` or technical specifications).
* **Strict Evaluation Invariant:** Simulating content analysis with local heuristics to save tokens or time is prohibited. You must parse each source.

### B. Parallel Execution and Context Window Optimization
* **Parallel Subagents (`invoke_subagent`):** Partition the task among independent subagents (`TypeName: "self"`) and execute them concurrently in the background.
* **Context Window Protection:** Prevent context bloat by routing voluminous raw text directly to SQLite tables (`readme_raw`, `raw_html`). Deliver only synthesized scores and summaries to higher layers.
* **Telemetry and Observability:** Log scanned source counts, execution timestamps, and decision rationales to the `agent_logs` table.

---

## 4. Multi-Layer Funnel Pipeline

Structure every research engagement as a four-layer deductive funnel:

### Layer 1: Macro Exploration & Workload Partitioning (Explorer Swarm - Phase 1)
1. **Workload Partitioning:** Divide the research domain into orthogonal thematic specializations (e.g., 5 sub-domains x 200 sources = 1,000 total sources).
2. **Parallel Explorer Agents:** Assign an independent Explorer Agent (`invoke_subagent`) to each specialization.
3. **Live Extraction & Content Processing:** Each agent retrieves verified live sources, downloads raw documentation, parses architecture details, and persists extracted data to SQLite.
4. **Domain Reports:** Each agent filters its domain (e.g., top 40 candidates), generates `agentX_[domain]_report.md`, and transmits the summary to the lead agent.

### Layer 2: Meso Audit & Cross-Evaluation (Auditor Swarm - Phase 2)
1. **Independent Auditor Agents:** The candidate pool from Layer 1 (e.g., 200 sources) is audited by specialized review agents evaluating distinct criteria:
   * *Auditor 1: Local Execution & Privacy (Local-First)*
   * *Auditor 2: Knowledge Graph & Link Integration*
   * *Auditor 3: Model Context Protocol (MCP) & Cross-Agent Interoperability*
   * *Auditor 4: Setup Complexity & Dependency Overhead*
   * *Auditor 5: Open-Source Licensing & Operational Cost*
2. **Weighted Scoring:** Each auditor scores candidates independently to reduce the pool to a curated finalist list (e.g., 50 sources).

### Layer 3: Micro Synthesis & Lead Architecture Selection (Lead Synthesis - Phase 3)
1. **Principal Architectural Audit:** Execute deep code inspections, benchmark comparisons, and feasibility analyses on the finalist pool.
2. **Top Finalists:** Select the top benchmark champions (e.g., TOP 10 Champions).
3. **Implementation Specification:** Produce deployment blueprints, architectural diagrams, integration recipes, and agent coordination maps for the selected systems.

### Layer 4: Output Synthesis and Delivery (Delivery Layer)
1. **Local SQLite Database (`data.db`):** Complete repository of raw records, source texts, auditor evaluations, and operational audit logs.
2. **Technical Synthesis Report (`report.md`):** Executive summary, architecture breakdown, and decision matrix structured to Conductor standards.
3. **Interactive Visual Dashboard (`report.html` / `index.html`):**
   * Real-time search and category filtering.
   * Funnel stage selectors (All Candidates, Phase 1, Phase 2, Top Champions).
   * Pagination engine with sorting by score.
   * Agent execution logs and architectural flow diagrams.
4. **Master Registry Registration (`research_master.db`):**
   * Execute `python3 scripts/master_db_manager.py` upon task completion.
   * Register research ID, title, and methodological approach.
   * Record source volume metrics (`sources_scanned_count`, `sources_analyzed_count`, `total_volume_analyzed`).
   * Record subagent telemetry (`agent_count`, execution layers, local database record counts, and efficiency audit scores).
