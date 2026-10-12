# Dynamic Task Scoping Directives - Interview Protocol

This protocol standardizes the requirements collection interview that the agent must conduct with the user before initiating any research engagement.

## Agent Directives

When a new research task is requested, execute an interactive requirements gathering interview before performing any web or file actions.

### Rule 1: Question Strategy
* Present **one question at a time** in sequence.
* Tailor questions specifically to the technical domain of the requested topic.
* Ask a **minimum of 3 questions**.
* Provide 2 to 3 structured options along with a custom text input option.

### Rule 2: Mandatory Scoping Themes
Incorporate these required themes across the interview:
1. **Depth and Target Scale:** Define boundaries (e.g., "Global or European market?", "How many verified sources are required, e.g., 50 or 100?").
2. **Deterministic Constraints:** Define filtering rules (e.g., "Only open-source licenses?", "Data published after 2024?", "Exclude proprietary enterprise platforms?").
3. **Synthesis Format and Level of Detail:** Define output expectations (e.g., "Implementation guide with code snippets or high-level architecture comparison?").

### Rule 3: Dynamic Plan Construction
Upon completing the interview, synthesize the user's responses into the **"Execution Steps"** section of `research_task_template.md`.

**Example Derived Steps:**
* Step 1: Query primary sources matching topic X and constraint Y up to the target count.
* Step 2: Audit extracted sources against criteria Z and populate `data.db`.
* Step 3: Produce executive summary report `report.md` and sync metrics to `research_master.db`.

### Rule 4: Final Confirmation Gate
Present the synthesized task template to the user and request explicit confirmation before initializing the workspace directory and starting execution.
