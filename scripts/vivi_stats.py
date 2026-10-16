#!/usr/bin/env python3
"""Aggregate statistics from a Vivi mailspace database.

Reads the database read-only (immutable) and prints counts only: no
message bodies, subjects, or addresses leave the database. Optional
repository paths add commit counts over the same window.

Usage:
    python3 vivi_stats.py ~/work/faberlang/.vivi/mail.sqlite \
        [--repos ~/work/faberlang/radix ~/work/faberlang/faber ...]
"""

import argparse
import collections
import json
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

# Auditor report subjects read "auditor report: <verdict> ...".
VERDICT_GROUPS = {
    "clean": {"clean_pass", "clean", "pass", "clean_range", "conditional_pass"},
    "admitted": {"admitted", "go-with-notes", "admitted-with-residuals"},
    "residual": {"residual"},
    "revise": {"revise"},
    "blocked": {"block_ship", "block", "block_range"},
}


def connect(path):
    uri = f"file:{Path(path).expanduser()}?mode=ro&immutable=1"
    return sqlite3.connect(uri, uri=True)


def sender_role(addr):
    local = re.sub(r'[<>"]', "", addr.lower()).split("@")[0].strip()
    return re.sub(r"[-_]?\d+$", "", local)


def verdict_of(subject):
    tail = subject.split(":", 1)[1].strip() if ":" in subject else ""
    word = tail.split()[0].strip(" —-(").lower() if tail else ""
    for group, words in VERDICT_GROUPS.items():
        if word in words:
            return group
    return "other"


def mailspace_stats(db):
    q = lambda sql: db.execute(sql).fetchall()
    total, first, last = q("SELECT count(*), min(date), max(date) FROM message_metadata")[0]
    roles = collections.Counter(sender_role(a) for (a,) in q("SELECT from_addr FROM message_metadata"))
    reports = [s for (s,) in q(
        "SELECT subject FROM message_metadata "
        "WHERE lower(subject) LIKE 'auditor report:%' OR lower(subject) LIKE 'auditor-_ report:%'"
    )]
    verdicts = collections.Counter(verdict_of(s) for s in reports)
    nodes = q("SELECT state, count(*) FROM work_graph_nodes GROUP BY state")
    attempts = q("SELECT coalesce(role, '?'), count(*) FROM work_graph_attempts GROUP BY 1")
    per_node = q(
        "SELECT n, count(*) FROM (SELECT count(*) n FROM work_graph_attempts GROUP BY node_handle) GROUP BY n"
    )
    return {
        "window": {"first": first, "last": last},
        "messages": total,
        "events": q("SELECT count(*) FROM mailspace_events")[0][0],
        "messages_by_month": dict(q("SELECT substr(date,1,7), count(*) FROM message_metadata GROUP BY 1")),
        "messages_by_sender_role": dict(roles.most_common()),
        "auditor_reports": {"total": len(reports), "by_verdict": dict(verdicts.most_common())},
        "work_items_by_state": dict(nodes),
        "work_assignments_by_role": dict(sorted(attempts, key=lambda r: -r[1])),
        "assignments_per_item": {str(n): c for n, c in per_node},
    }


def commit_counts(repos, since):
    out = {}
    for repo in repos:
        path = Path(repo).expanduser()
        result = subprocess.run(
            ["git", "-C", str(path), "rev-list", "--count", f"--since={since}", "HEAD"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            out[path.name] = int(result.stdout.strip())
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("database")
    parser.add_argument("--repos", nargs="*", default=[])
    args = parser.parse_args()

    stats = mailspace_stats(connect(args.database))
    if args.repos:
        stats["commits_since_window_start"] = commit_counts(args.repos, stats["window"]["first"][:10])
    json.dump(stats, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
