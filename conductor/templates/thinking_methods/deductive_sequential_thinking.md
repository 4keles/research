# Reasoning Method: Deductive Sequential Thinking (Macro to Micro)

This template guides the agent through structured deductive progression, beginning from the macro domain, filtering non-essential variables, and narrowing focus to the micro target.

## 1. Core Logic
Start at the broadest systemic scope, eliminate irrelevant variables via specified constraints, and converge deterministically on the target problem.
*(e.g., When estimating technical adoption: Analyze global architectural shifts -> Filter factors impacting target language ecosystems -> Isolate concurrency/runtime constraints -> Synthesize comparative benchmark model.)*

## 2. Mandatory Tool: Sequential Thinking
Applying **`sequential_thinking`** (or equivalent step-by-step reasoning) is **mandatory** at each deduction stage. The agent must evaluate hypotheses against concrete evidence before transitioning to narrower layers.

## 3. Step-by-Step Execution Plan

### Step 1: Broad Domain Survey (Macro Level)
* **Action:** Identify the broadest parent domains governing the research topic.
* **Sequential Thinking:** Analyze: "What global and structural forces determine the parameters of this domain?"
* **Data Collection:** Gather primary macro-level sources matching depth requirements and persist extracted records to `data.db`.

### Step 2: Context Filtering (Meso Level)
* **Action:** Filter the candidate factors against the task's explicit boundary constraints.
* **Sequential Thinking:** Analyze: "Which factors directly govern the target problem? Which variables can be safely eliminated?"
* **Data Collection:** Execute secondary targeted queries on the filtered candidate subset.

### Step 3: Deep Technical Targeting (Micro Level)
* **Action:** Focus strictly on the core technical target, component, or metric.
* **Sequential Thinking:** Analyze: "Does the current evidence satisfy all verification requirements? What specific technical gaps remain?"
* **Data Collection:** Execute precise, point-lookup queries to resolve all remaining analytical ambiguities.

### Step 4: Synthesis and Delivery
* **Action:** Synthesize verified evidence into the final deliverable.
* **Sequential Thinking:** Synthesize: "What is the unified technical conclusion, comparison matrix, or architectural blueprint?"
* **Output:** Produce the final synthesis in `report.md`, close the SQLite database connection, and register completion in `research_master.db`.
