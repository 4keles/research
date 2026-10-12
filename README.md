# Conductor Research Framework

## Overview
This repository contains an autonomous research framework for AI agents. The framework uses the Conductor protocol and sequential thinking to collect and analyze technical data.

## Deterministic Parameters

The framework uses five deterministic parameters to control agent operations:

1. `min_sources_scanned`: Minimum count of primary web sources that the agent must scan.
2. `min_sources_analyzed`: Minimum count of full-text documents that the agent must parse.
3. `thinking_mode`: Fixed deduction sequence (`macro -> meso -> micro`).
4. `anti_mock`: Strict validation flag that prohibits synthetic and simulated records.
5. `local_db_mode`: Direct storage parameter that routes raw text to SQLite.

## Cause and Effect Relationships

The table below shows the cause and effect relationships of each operational parameter:

| Cause (Parameter / Condition) | System Action | Direct Effect |
| :--- | :--- | :--- |
| Set `min_sources_scanned = 100` | The agent executes iterative search queries. | The agent does not stop before it verifies 100 live sources. |
| Set `anti_mock = true` | The system validates every URL and HTTP response. | The database contains only verified real data. Fake data is rejected. |
| Set `local_db_mode = enabled` | The agent writes raw web data directly to SQLite (`data.db`). | Context window bloat does not occur. Token consumption stays constant. |
| Set `thinking_mode = deductive` | The agent processes broad domain data before it inspects narrow technical targets. | Early bias is removed. The agent finds the root cause before edge cases. |
| Run `multi_agent_optimizer.py` | The system partitions analysis tasks across specialized subagents. | Execution time decreases and task collisions do not occur. |
| Run `master_db_manager.py` | The system logs metrics to `research_master.db`. | The project maintains an audit record of research volume and efficiency. |

## Repository Architecture

- `.agents/`: Agent personas, specialized skills, and operational rules.
- `conductor/`: Process workflows, track registries, and specifications.
- `scripts/`: Central registry managers and multi-agent optimization utilities.
- `GEMINI.md`: Root routing instructions and behavioral directives.

## Execution Workflow

1. Define the research scope with explicit boundary constraints.
2. Set the deterministic source limits and the sequential thinking mode.
3. Run the research agent to collect live sources into the local SQLite database.
4. Execute `master_db_manager.py` to record completion metrics in the central database.
