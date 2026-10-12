#!/usr/bin/env python3
"""
Master Research Database Manager & Registry
Collects and manages metadata, methodology, and telemetry metrics 
across research tasks in the central `research_master.db` SQLite database.
"""

import os
import sys
import sqlite3
import argparse
from datetime import datetime

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_DB_PATH = os.path.join(WORKSPACE_DIR, "research_master.db")

SCHEMA_SQL = """
PRAGMA journal_mode = WAL;
PRAGMA busy_timeout = 30000;

CREATE TABLE IF NOT EXISTS researches (
    research_id TEXT PRIMARY KEY,
    track_code TEXT NOT NULL,
    title TEXT NOT NULL,
    created_date TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'COMPLETED',
    category TEXT NOT NULL,
    methodological_approach TEXT NOT NULL,
    agent_architecture TEXT NOT NULL,
    summary TEXT NOT NULL,
    key_findings TEXT,
    folder_path TEXT NOT NULL,
    report_file TEXT NOT NULL,
    local_db_file TEXT,
    html_dashboard TEXT,
    tags TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS research_metrics (
    research_id TEXT PRIMARY KEY,
    sources_scanned_count INTEGER DEFAULT 0,
    sources_analyzed_count INTEGER DEFAULT 0,
    total_volume_analyzed TEXT,
    agent_count INTEGER DEFAULT 1,
    execution_layers_count INTEGER DEFAULT 1,
    local_db_records_count INTEGER DEFAULT 0,
    efficiency_score REAL DEFAULT 100.0,
    efficiency_notes TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(research_id) REFERENCES researches(research_id) ON DELETE CASCADE
);

CREATE VIEW IF NOT EXISTS v_research_catalog AS
SELECT 
    r.research_id,
    r.track_code,
    r.title,
    r.created_date,
    r.status,
    r.category,
    r.methodological_approach,
    r.agent_architecture,
    m.sources_scanned_count,
    m.sources_analyzed_count,
    m.total_volume_analyzed,
    m.agent_count,
    m.local_db_records_count,
    m.efficiency_score,
    m.efficiency_notes,
    r.folder_path,
    r.report_file,
    r.html_dashboard,
    r.tags
FROM researches r
LEFT JOIN research_metrics m ON r.research_id = m.research_id;
"""

def get_connection():
    conn = sqlite3.connect(MASTER_DB_PATH)
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA busy_timeout = 30000;")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_master_db():
    conn = get_connection()
    conn.executescript(SCHEMA_SQL)
    conn.commit()
    conn.close()

def upsert_research(research_data, metrics_data):
    init_master_db()
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        INSERT INTO researches (
            research_id, track_code, title, created_date, status, category,
            methodological_approach, agent_architecture, summary, key_findings,
            folder_path, report_file, local_db_file, html_dashboard, tags, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(research_id) DO UPDATE SET
            track_code=excluded.track_code,
            title=excluded.title,
            created_date=excluded.created_date,
            status=excluded.status,
            category=excluded.category,
            methodological_approach=excluded.methodological_approach,
            agent_architecture=excluded.agent_architecture,
            summary=excluded.summary,
            key_findings=excluded.key_findings,
            folder_path=excluded.folder_path,
            report_file=excluded.report_file,
            local_db_file=excluded.local_db_file,
            html_dashboard=excluded.html_dashboard,
            tags=excluded.tags,
            updated_at=CURRENT_TIMESTAMP;
    """, (
        research_data["research_id"],
        research_data["track_code"],
        research_data["title"],
        research_data["created_date"],
        research_data.get("status", "COMPLETED"),
        research_data["category"],
        research_data["methodological_approach"],
        research_data["agent_architecture"],
        research_data["summary"],
        research_data.get("key_findings", ""),
        research_data["folder_path"],
        research_data["report_file"],
        research_data.get("local_db_file"),
        research_data.get("html_dashboard"),
        research_data.get("tags", "")
    ))

    cur.execute("""
        INSERT INTO research_metrics (
            research_id, sources_scanned_count, sources_analyzed_count,
            total_volume_analyzed, agent_count, execution_layers_count,
            local_db_records_count, efficiency_score, efficiency_notes, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(research_id) DO UPDATE SET
            sources_scanned_count=excluded.sources_scanned_count,
            sources_analyzed_count=excluded.sources_analyzed_count,
            total_volume_analyzed=excluded.total_volume_analyzed,
            agent_count=excluded.agent_count,
            execution_layers_count=excluded.execution_layers_count,
            local_db_records_count=excluded.local_db_records_count,
            efficiency_score=excluded.efficiency_score,
            efficiency_notes=excluded.efficiency_notes,
            updated_at=CURRENT_TIMESTAMP;
    """, (
        research_data["research_id"],
        metrics_data.get("sources_scanned_count", 0),
        metrics_data.get("sources_analyzed_count", 0),
        metrics_data.get("total_volume_analyzed", ""),
        metrics_data.get("agent_count", 1),
        metrics_data.get("execution_layers_count", 1),
        metrics_data.get("local_db_records_count", 0),
        metrics_data.get("efficiency_score", 100.0),
        metrics_data.get("efficiency_notes", "")
    ))

    conn.commit()
    conn.close()

def list_researches():
    init_master_db()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT track_code, title, category, methodological_approach, 
               sources_scanned_count, sources_analyzed_count, local_db_records_count, efficiency_score
        FROM v_research_catalog
        ORDER BY track_code ASC
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def get_research_detail(research_id_or_code):
    init_master_db()
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM v_research_catalog 
        WHERE research_id = ? OR track_code = ?
    """, (research_id_or_code, research_id_or_code))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None

def print_table():
    rows = list_researches()
    if not rows:
        print("No research tasks registered in central master database.")
        return
    
    print("\n" + "="*120)
    print(f"{'CODE':<8} | {'TITLE':<38} | {'CATEGORY':<24} | {'SCANNED':<8} | {'ANALYZED':<8} | {'DB ROWS':<8} | {'SCORE':<5}")
    print("="*120)
    for r in rows:
        title = (r[1][:35] + '...') if len(r[1]) > 35 else r[1]
        cat = (r[2][:21] + '...') if len(r[2]) > 21 else r[2]
        print(f"{r[0]:<8} | {title:<38} | {cat:<24} | {r[4]:<8} | {r[5]:<8} | {r[6]:<8} | {r[7]:<5.1f}")
    print("="*120 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Central Research Master Database Manager")
    parser.add_argument("--list", action="store_true", help="List all registered research tasks")
    parser.add_argument("--info", type=str, help="Show details for a specific research ID or code (e.g., RES001)")
    args = parser.parse_args()

    init_master_db()
    if args.info:
        detail = get_research_detail(args.info)
        if detail:
            print("\n" + "="*80)
            print(f"Research Detail: {detail['track_code']} - {detail['title']}")
            print("="*80)
            for k, v in detail.items():
                print(f"{k:<25}: {v}")
            print("="*80 + "\n")
        else:
            print(f"Record not found: {args.info}")
    else:
        print_table()
