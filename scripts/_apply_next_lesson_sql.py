"""
Rewrite #next-lesson section and bottom navigation bar for all lessons
under mod_06a_sql_foundation, following the lesson-next-lesson prompt rules.
"""

import re
from pathlib import Path

BASE = Path("c:/Users/nightwolf/Projects/Python-Learning/pages/mod_06a_sql_foundation")
HUB = "../../hub_home_page.html"

# ── Lesson data ────────────────────────────────────────────────────────────────
# Each entry: (file_path, module_num, lesson_num, prev_file, prev_title,
#              next_file, next_num, next_title, card1, card2, card3)
# card = (icon, text)

MOD5 = "mod_05_sql_foundations"
MOD6 = "mod_06_advanced_sql_for_data_analysis"

LESSONS = [
    # ── mod_05: SQL Foundations ─────────────────────────────────────────────
    {
        "path": f"{MOD5}/lesson01_what_is_sql.html",
        "module": 5, "num": 1,
        "prev_file": None, "prev_title": None,
        "next_file": "lesson02_tables_rows_and_columns.html",
        "next_num": 2, "next_title": "Tables, Rows, and Columns",
        "cards": [
            ("fa6-solid:table", "How Database Tables Are Structured"),
            ("fa6-solid:database", "Rows as Records, Columns as Attributes"),
            ("fa6-solid:key", "Primary Keys and Unique Row Identifiers"),
        ],
    },
    {
        "path": f"{MOD5}/lesson02_tables_rows_and_columns.html",
        "module": 5, "num": 2,
        "prev_file": "lesson01_what_is_sql.html", "prev_title": "What is SQL?",
        "next_file": "lesson03_the_select_statement.html",
        "next_num": 3, "next_title": "The SELECT Statement",
        "cards": [
            ("fa6-solid:table-columns", "The SELECT and FROM Clauses"),
            ("fa6-solid:list", "Choosing Specific Columns to Return"),
            ("fa6-solid:asterisk", "Using * to Select All Columns"),
        ],
    },
    {
        "path": f"{MOD5}/lesson03_the_select_statement.html",
        "module": 5, "num": 3,
        "prev_file": "lesson02_tables_rows_and_columns.html", "prev_title": "Tables, Rows, and Columns",
        "next_file": "lesson04_filtering_data_with_where.html",
        "next_num": 4, "next_title": "Filtering Data with WHERE",
        "cards": [
            ("fa6-solid:filter", "The WHERE Clause"),
            ("fa6-solid:equals", "Comparison Operators (=, &lt;, &gt;, !=)"),
            ("fa6-solid:code-branch", "AND, OR, and NOT Conditions"),
        ],
    },
    {
        "path": f"{MOD5}/lesson04_filtering_data_with_where.html",
        "module": 5, "num": 4,
        "prev_file": "lesson03_the_select_statement.html", "prev_title": "The SELECT Statement",
        "next_file": "lesson05_sorting_data_with_order_by.html",
        "next_num": 5, "next_title": "Sorting Data with ORDER BY",
        "cards": [
            ("fa6-solid:sort", "The ORDER BY Clause"),
            ("fa6-solid:arrow-up", "Ascending and Descending Sort Order"),
            ("fa6-solid:layer-group", "Sorting by Multiple Columns"),
        ],
    },
    {
        "path": f"{MOD5}/lesson05_sorting_data_with_order_by.html",
        "module": 5, "num": 5,
        "prev_file": "lesson04_filtering_data_with_where.html", "prev_title": "Filtering Data with WHERE",
        "next_file": "lesson06_aggregations_count_sum_avg.html",
        "next_num": 6, "next_title": "Aggregations: COUNT, SUM, AVG",
        "cards": [
            ("fa6-solid:calculator", "COUNT, SUM, and AVG Functions"),
            ("fa6-solid:arrow-up-wide-short", "MIN and MAX Functions"),
            ("fa6-solid:chart-bar", "Summarizing Data with Aggregations"),
        ],
    },
    {
        "path": f"{MOD5}/lesson06_aggregations_count_sum_avg.html",
        "module": 5, "num": 6,
        "prev_file": "lesson05_sorting_data_with_order_by.html", "prev_title": "Sorting Data with ORDER BY",
        "next_file": "lesson07_group_by.html",
        "next_num": 7, "next_title": "GROUP BY",
        "cards": [
            ("fa6-solid:object-group", "The GROUP BY Clause"),
            ("fa6-solid:table", "Grouping Rows by Column Values"),
            ("fa6-solid:chart-simple", "Combining GROUP BY with Aggregations"),
        ],
    },
    {
        "path": f"{MOD5}/lesson07_group_by.html",
        "module": 5, "num": 7,
        "prev_file": "lesson06_aggregations_count_sum_avg.html", "prev_title": "Aggregations: COUNT, SUM, AVG",
        "next_file": "lesson08_filtering_groups_with_having.html",
        "next_num": 8, "next_title": "Filtering Groups with HAVING",
        "cards": [
            ("fa6-solid:filter", "The HAVING Clause"),
            ("fa6-solid:not-equal", "HAVING vs WHERE — Key Differences"),
            ("fa6-solid:database", "Filtering After Aggregation"),
        ],
    },
    {
        "path": f"{MOD5}/lesson08_filtering_groups_with_having.html",
        "module": 5, "num": 8,
        "prev_file": "lesson07_group_by.html", "prev_title": "GROUP BY",
        "next_file": "lesson09_joining_tables_join.html",
        "next_num": 9, "next_title": "Joining Tables (JOIN)",
        "cards": [
            ("fa6-solid:link", "The JOIN Keyword"),
            ("fa6-solid:circle-dot", "INNER JOIN and LEFT JOIN"),
            ("fa6-solid:key", "Joining Tables Using Keys"),
        ],
    },
    {
        "path": f"{MOD5}/lesson09_joining_tables_join.html",
        "module": 5, "num": 9,
        "prev_file": "lesson08_filtering_groups_with_having.html", "prev_title": "Filtering Groups with HAVING",
        "next_file": f"../{MOD6}/lesson01_subqueries.html",
        "next_num": 1, "next_title": "Subqueries",
        "cards": [
            ("fa6-solid:code", "What a Subquery Is"),
            ("fa6-solid:layer-group", "Subqueries Inside SELECT and WHERE"),
            ("fa6-solid:circle-nodes", "Nested Query Structure"),
        ],
    },
    # ── mod_06: Advanced SQL ────────────────────────────────────────────────
    {
        "path": f"{MOD6}/lesson01_subqueries.html",
        "module": 6, "num": 1,
        "prev_file": f"../{MOD5}/lesson09_joining_tables_join.html",
        "prev_title": "Joining Tables (JOIN)",
        "next_file": "lesson02_common_table_expressions_ctes.html",
        "next_num": 2, "next_title": "Common Table Expressions (CTEs)",
        "cards": [
            ("fa6-solid:file-code", "Common Table Expressions (CTEs)"),
            ("fa6-solid:rotate-left", "WITH Clause Syntax"),
            ("fa6-solid:arrows-split-up-and-left", "CTEs vs Subqueries"),
        ],
    },
    {
        "path": f"{MOD6}/lesson02_common_table_expressions_ctes.html",
        "module": 6, "num": 2,
        "prev_file": "lesson01_subqueries.html", "prev_title": "Subqueries",
        "next_file": "lesson03_window_functions_partition_by.html",
        "next_num": 3, "next_title": "Window Functions (PARTITION BY)",
        "cards": [
            ("fa6-solid:window-restore", "Window Functions &amp; OVER()"),
            ("fa6-solid:table-cells", "The PARTITION BY Clause"),
            ("fa6-solid:chart-area", "Running Calculations Across Rows"),
        ],
    },
    {
        "path": f"{MOD6}/lesson03_window_functions_partition_by.html",
        "module": 6, "num": 3,
        "prev_file": "lesson02_common_table_expressions_ctes.html",
        "prev_title": "Common Table Expressions (CTEs)",
        "next_file": "lesson04_ranking_functions.html",
        "next_num": 4, "next_title": "Ranking Functions",
        "cards": [
            ("fa6-solid:medal", "ROW_NUMBER, RANK, and DENSE_RANK"),
            ("fa6-solid:list-ol", "How Ranking Functions Order Rows"),
            ("fa6-solid:sliders", "Differences Between Ranking Functions"),
        ],
    },
    {
        "path": f"{MOD6}/lesson04_ranking_functions.html",
        "module": 6, "num": 4,
        "prev_file": "lesson03_window_functions_partition_by.html",
        "prev_title": "Window Functions (PARTITION BY)",
        "next_file": "lesson05_running_totals.html",
        "next_num": 5, "next_title": "Running Totals",
        "cards": [
            ("fa6-solid:chart-line", "Running Totals with SUM OVER"),
            ("fa6-solid:arrows-down-to-line", "Cumulative Aggregations"),
            ("fa6-solid:table-list", "Using ORDER BY Inside a Window"),
        ],
    },
    {
        "path": f"{MOD6}/lesson05_running_totals.html",
        "module": 6, "num": 5,
        "prev_file": "lesson04_ranking_functions.html", "prev_title": "Ranking Functions",
        "next_file": "lesson06_advanced_joins.html",
        "next_num": 6, "next_title": "Advanced Joins",
        "cards": [
            ("fa6-solid:arrows-rotate", "Self Joins"),
            ("fa6-solid:table-columns", "FULL OUTER JOIN"),
            ("fa6-solid:diagram-project", "Multi-Table Join Patterns"),
        ],
    },
    {
        "path": f"{MOD6}/lesson06_advanced_joins.html",
        "module": 6, "num": 6,
        "prev_file": "lesson05_running_totals.html", "prev_title": "Running Totals",
        "next_file": "lesson07_case_statements.html",
        "next_num": 7, "next_title": "CASE Statements",
        "cards": [
            ("fa6-solid:code-branch", "The CASE WHEN Statement"),
            ("fa6-solid:list-check", "Multiple WHEN Conditions"),
            ("fa6-solid:tags", "Creating Computed Columns with CASE"),
        ],
    },
    {
        "path": f"{MOD6}/lesson07_case_statements.html",
        "module": 6, "num": 7,
        "prev_file": "lesson06_advanced_joins.html", "prev_title": "Advanced Joins",
        "next_file": "lesson08_null_handling.html",
        "next_num": 8, "next_title": "NULL Handling",
        "cards": [
            ("fa6-solid:ban", "What NULL Means in SQL"),
            ("fa6-solid:circle-question", "IS NULL and IS NOT NULL"),
            ("fa6-solid:fill", "COALESCE and NULLIF Functions"),
        ],
    },
    {
        "path": f"{MOD6}/lesson08_null_handling.html",
        "module": 6, "num": 8,
        "prev_file": "lesson07_case_statements.html", "prev_title": "CASE Statements",
        "next_file": "lesson09_query_optimization.html",
        "next_num": 9, "next_title": "Query Optimization",
        "cards": [
            ("fa6-solid:gauge-high", "Why Query Performance Matters"),
            ("fa6-solid:magnifying-glass-chart", "How Indexes Speed Up Queries"),
            ("fa6-solid:list-check", "Writing Efficient SQL Queries"),
        ],
    },
    {
        "path": f"{MOD6}/lesson09_query_optimization.html",
        "module": 6, "num": 9,
        "prev_file": "lesson08_null_handling.html", "prev_title": "NULL Handling",
        "next_file": "lesson10_sql_for_analytics_workflows.html",
        "next_num": 10, "next_title": "SQL for Analytics Workflows",
        "cards": [
            ("fa6-solid:chart-line", "SQL in Analytics Pipelines"),
            ("fa6-solid:database", "Connecting SQL to Python &amp; BI Tools"),
            ("fa6-solid:layer-group", "End-to-End Analytics Workflow"),
        ],
    },
    {
        "path": f"{MOD6}/lesson10_sql_for_analytics_workflows.html",
        "module": 6, "num": 10,
        "prev_file": "lesson09_query_optimization.html", "prev_title": "Query Optimization",
        "next_file": None, "next_num": None, "next_title": None,
        "cards": None,  # last lesson — no next
    },
]


def build_next_lesson_section(lesson):
    """Build the full #next-lesson section + bottom nav HTML."""
    nf = lesson["next_file"]
    nn = lesson["next_num"]
    nt = lesson["next_title"]
    mod = lesson["module"]
    cards = lesson["cards"]
    pf = lesson["prev_file"]
    pt = lesson["prev_title"]

    # ── #next-lesson section ──────────────────────────────────────────────
    if nf is not None:
        card_html = ""
        for icon, text in cards:
            card_html += f"""
    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="{icon}"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">{text}</p>
      </div>
    </div>"""

        section_body = f"""
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">{nn}</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module {mod} &middot; Lesson {nn}</p>
          <h3 class="text-base font-bold text-gray-800">{nt}</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">{card_html}
        </div>
      </div>"""
    else:
        section_body = """
      <p class="text-sm text-gray-600 leading-relaxed">You have completed all lessons in this module. Well done!</p>"""

    next_section = f"""<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:circle-arrow-right"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Next Lesson</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Preview of what comes next</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">{section_body}
    </div>
  </div>
</section>"""

    # ── Bottom nav ────────────────────────────────────────────────────────
    if pf is None:
        prev_slot = '    <div class="flex-1"></div>'
    else:
        prev_slot = f"""    <a href="{pf}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{pt}</p>
      </div>
    </a>"""

    hub_slot = f"""    <a href="{HUB}" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>"""

    if nf is not None:
        next_slot = f"""    <a href="{nf}" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{nt}</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>"""
    else:
        next_slot = ""

    bottom_nav = f"""<section>
  <div class="flex flex-col sm:flex-row gap-3">

{prev_slot}

{hub_slot}

{next_slot}

  </div>
</section>"""

    return next_section + "\n\n" + bottom_nav


def replace_next_lesson_block(html, new_block):
    """Replace the existing #next-lesson section + bottom nav with new content."""
    # Match from <section id="next-lesson" to the end of the following bare <section> (bottom nav)
    pattern = re.compile(
        r'<section id="next-lesson"[^>]*>.*?</section>\s*\n\s*\n\s*<section>\s*\n\s*<div class="flex flex-col sm:flex-row[^>]*>.*?</section>',
        re.DOTALL,
    )
    new_html, count = pattern.subn(new_block, html)
    if count == 0:
        # Try alternate: old next-lesson section only (no separate bottom nav)
        pattern2 = re.compile(
            r'<section id="next-lesson"[^>]*>.*?</section>',
            re.DOTALL,
        )
        new_html, count = pattern2.subn(new_block, html)
    return new_html, count


results = []

for lesson in LESSONS:
    fpath = BASE / lesson["path"]
    if not fpath.exists():
        results.append(("⚠️ ", fpath.name, "file not found"))
        continue

    html = fpath.read_text(encoding="utf-8")
    new_block = build_next_lesson_section(lesson)
    new_html, count = replace_next_lesson_block(html, new_block)

    if count == 0:
        results.append(("❌", fpath.name, "pattern not matched"))
        continue

    fpath.write_text(new_html, encoding="utf-8")
    results.append(("✅", fpath.name, f"replaced ({count})"))

print(f"{'St':<4} {'File':<55}  Note")
print("-" * 80)
for status, name, note in results:
    print(f"{status}  {name:<55}  {note}")

ok = all(r[0] == "✅" for r in results)
print(f"\n{'✅ All done.' if ok else '❌ Some files had issues — review above.'}")
