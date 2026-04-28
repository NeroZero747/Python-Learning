"""Fix the module-lessons TOC sidebar across all 12 lessons in
pages/mod_06_sql_foundation/.

For each lesson file:
  1. Replace the entire `<div class="space-y-1"> ... </div>` block inside
     `<div class="toc-module-list ...">` with the canonical 12-lesson list.
  2. On the current lesson's own row, stamp `mod-lesson-active` on the <a>
     and `lesson-dot` on the dot <span>, so the existing #hub-root CSS rule
     gives it pink background, pink border, pink text, and pink dot.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOD_DIR = ROOT / "pages" / "mod_06_sql_foundation"

# Canonical (filename, sidebar-title) pairs in lesson order.
LESSONS: list[tuple[str, str]] = [
    ("lesson01_what_is_sql.html",                    "What is SQL?"),
    ("lesson02_tables_rows_and_columns.html",        "Tables, Rows, and Columns"),
    ("lesson03_the_select_statement.html",           "SELECT &amp; ORDER BY"),
    ("lesson04_filtering_data_with_where.html",      "Filtering Data with WHERE"),
    ("lesson05_aggregations_count_sum_avg.html",     "Aggregations (COUNT, SUM, AVG)"),
    ("lesson06_group_by_having.html",                "GROUP BY and HAVING"),
    ("lesson07_joining_tables.html",                 "Joining Tables (JOIN)"),
    ("lesson08_subqueries_ctes.html",                "Subqueries and CTEs"),
    ("lesson09_window_functions_partition_by.html",  "Window Functions"),
    ("lesson10_advanced_joins.html",                 "Advanced Joins"),
    ("lesson11_case_statements.html",                "CASE Statements &amp; NULL Handling"),
    ("lesson12_query_optimization.html",             "Query Optimization"),
]

INACTIVE_LINK_CLASSES = (
    "flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 "
    "text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors"
)
ACTIVE_LINK_CLASSES = (
    "mod-lesson-active flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 "
    "text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors"
)
INACTIVE_DOT = '<span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>'
ACTIVE_DOT   = '<span class="lesson-dot w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>'


def build_module_list(current_filename: str) -> str:
    """Return the inner HTML of the `<div class="space-y-1">...</div>` container."""
    rows: list[str] = []
    for idx, (fname, title) in enumerate(LESSONS, start=1):
        is_active = (fname == current_filename)
        link_cls = ACTIVE_LINK_CLASSES if is_active else INACTIVE_LINK_CLASSES
        dot      = ACTIVE_DOT          if is_active else INACTIVE_DOT
        rows.append(
            f'<a href="{fname}" class="{link_cls}">\n'
            f'  {dot}\n'
            f'  <span class="truncate">{idx}. {title}</span>\n'
            f'</a>'
        )
    return '<div class="space-y-1">' + "\n".join(rows) + "\n</div>"


# Regex: capture the entire `<div class="space-y-1"> ... </div>` block.
# The block sits inside `<div class="toc-module-list ...">` and is the only
# `space-y-1` div in that area, so we anchor on the unique opening tag and
# match up to the closing `</div>` that immediately precedes the
# `</div>\n          </div>\n        </div>\n      </aside>` container chain.
SPACE_Y1_RE = re.compile(
    r'<div class="space-y-1">.*?</div>\s*</div>\s*</div>\s*</aside>',
    re.DOTALL,
)


def fix_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    new_inner = build_module_list(path.name)
    # Replace just the `space-y-1` block; preserve the outer wrappers exactly.
    replacement_tail = '\n          </div>\n        </div>\n      </aside>'
    new_text, n = SPACE_Y1_RE.subn(new_inner + replacement_tail, text, count=1)
    if n == 0:
        return "no-match"
    if new_text == text:
        return "unchanged"
    path.write_text(new_text, encoding="utf-8")
    return "patched"


def main() -> None:
    print(f"Fixing TOCs in {MOD_DIR}\n")
    for fname, _ in LESSONS:
        p = MOD_DIR / fname
        if not p.exists():
            print(f"  [missing]  {fname}")
            continue
        status = fix_file(p)
        marker = {"patched": "OK ", "unchanged": "-- ", "no-match": "!! "}[status]
        print(f"  [{marker}]  {fname}  ({status})")


if __name__ == "__main__":
    main()
