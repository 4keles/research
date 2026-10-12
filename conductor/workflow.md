# Workflow

## Testing Policy
- **TDD Strictness:** Flexible. Recommended for complex procedural logic and multi-agent coordination scripts.

## Commit Strategy
- **Format:** Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, etc.).

## Code Review Policy
- **Scope:** Mandatory for architectural updates and behavioral rules governing agent operations.

## Verification Checkpoints
- **Task Verification:** Verified upon completion of each individual task.
- **Master Research Database Sync:** Every completed research task must be logged into `research_master.db` via `scripts/master_db_manager.py` after local `data.db` and `report.md` generation. Logged metrics include methodology, source counts, data volume, and efficiency scores.
