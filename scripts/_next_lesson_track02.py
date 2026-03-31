#!/usr/bin/env python3
"""Rewrite #next-lesson section + bottom nav for all 28 track_02 lessons."""

import re, os, sys

ROOT = r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics"
HUB  = "../../../hub_home_page.html"

# ── HTML builders ─────────────────────────────────────────────────────────────

def card(icon, text):
    return f'''\
    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:{icon}"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">{text}</p>
      </div>
    </div>'''


def next_lesson_section(next_mod, next_num, next_title, next_file, c1, c2, c3):
    """Build the full #next-lesson section HTML."""
    return f'''\
<section id="next-lesson" class="scroll-mt-24">
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
    <div class="bg-white px-8 py-7 space-y-6">

      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">{next_num}</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module {next_mod} &middot; Lesson {next_num}</p>
          <h3 class="text-base font-bold text-gray-800">{next_title}</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
{card(*c1)}

{card(*c2)}

{card(*c3)}
        </div>
      </div>

    </div>
  </div>
</section>'''


def bottom_nav(prev_file, prev_title, next_file, next_title):
    """Build the bottom nav section. Pass next_file=None to omit next link."""
    if prev_file is None:
        prev_slot = '    <div class="flex-1"></div>'
    else:
        prev_slot = f'''\
    <a href="{prev_file}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{prev_title}</p>
      </div>
    </a>'''

    hub_slot = f'''\
    <a href="{HUB}" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>'''

    if next_file is None:
        next_slot = ''
    else:
        next_slot = f'''\
    <a href="{next_file}" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{next_title}</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>'''

    parts = [prev_slot, hub_slot]
    if next_slot:
        parts.append(next_slot)

    return '<section>\n  <div class="flex flex-col sm:flex-row gap-3">\n\n' + \
           '\n\n'.join(parts) + \
           '\n\n  </div>\n</section>'


# ── Per-lesson data ───────────────────────────────────────────────────────────
# Keys  : relative file path from ROOT
# Fields:
#   next_mod   : module number of the NEXT lesson (for badge label)
#   next_num   : lesson number displayed in badge (matches filename/label)
#   next_title : title of the next lesson (use &amp; for &)
#   next_file  : href to next lesson (relative to current file), or None
#   c1/c2/c3   : (icon_suffix, card_text) tuples for 3 preview cards
#   prev_file  : href to previous lesson, or None (first lesson)
#   prev_title : display title of previous lesson

MOD01 = "mod_01_data_analysis_with_pandas"
MOD02 = "mod_02_working_with_data_sources"
MOD03 = "mod_03_python_for_analysts"
MOD04 = "mod_04_handling_large_data"

LESSONS = {

    # ── Module 01 ──────────────────────────────────────────────────────────────

    f"{MOD01}/lesson01_introduction_to_pandas.html": dict(
        next_mod=1, next_num=2,
        next_title="DataFrames Explained",
        next_file="lesson02_dataframes_explained.html",
        c1=("table-cells",    "What a DataFrame Is and How It Is Structured"),
        c2=("grip-lines",     "Rows, Columns, and the Index"),
        c3=("plus",           "Creating a DataFrame from a Dictionary"),
        prev_file=None, prev_title=None,
    ),

    f"{MOD01}/lesson02_dataframes_explained.html": dict(
        next_mod=1, next_num=3,
        next_title="Reading Data (CSV / Excel)",
        next_file="lesson03_reading_data_csv_excel.html",
        c1=("file-arrow-down", "Loading a CSV File with read_csv"),
        c2=("file-lines",      "Reading Excel Sheets with read_excel"),
        c3=("eye",             "Inspecting Data After Loading"),
        prev_file="lesson01_introduction_to_pandas.html",
        prev_title="Introduction to Pandas",
    ),

    f"{MOD01}/lesson03_reading_data_csv_excel.html": dict(
        next_mod=1, next_num=4,
        next_title="Selecting Columns",
        next_file="lesson04_selecting_columns.html",
        c1=("hand-pointer", "Selecting a Single Column by Name"),
        c2=("layer-group",  "Selecting Multiple Columns at Once"),
        c3=("pen",          "Renaming Columns to Cleaner Labels"),
        prev_file="lesson02_dataframes_explained.html",
        prev_title="DataFrames Explained",
    ),

    f"{MOD01}/lesson04_selecting_columns.html": dict(
        next_mod=1, next_num=5,
        next_title="Filtering Rows",
        next_file="lesson05_filtering_rows.html",
        c1=("filter",       "Filtering Rows by a Condition"),
        c2=("code-branch",  "Combining Multiple Filter Conditions"),
        c3=("circle-xmark", "Removing Rows with Missing Values"),
        prev_file="lesson03_reading_data_csv_excel.html",
        prev_title="Reading Data (CSV / Excel)",
    ),

    f"{MOD01}/lesson05_filtering_rows.html": dict(
        next_mod=1, next_num=6,
        next_title="Creating Calculated Columns",
        next_file="lesson06_creating_calculated_columns.html",
        c1=("calculator", "Adding a New Calculated Column"),
        c2=("percent",    "Applying Arithmetic Across Every Row"),
        c3=("sliders",    "Setting Column Values Conditionally"),
        prev_file="lesson04_selecting_columns.html",
        prev_title="Selecting Columns",
    ),

    f"{MOD01}/lesson06_creating_calculated_columns.html": dict(
        next_mod=1, next_num=7,
        next_title="Aggregations (GROUP BY)",
        next_file="lesson07_aggregations_group_by.html",
        c1=("object-group",  "Grouping Data by Category"),
        c2=("chart-column",  "Computing Totals and Averages per Group"),
        c3=("layer-group",   "Applying Multiple Aggregations at Once"),
        prev_file="lesson05_filtering_rows.html",
        prev_title="Filtering Rows",
    ),

    f"{MOD01}/lesson07_aggregations_group_by.html": dict(
        next_mod=1, next_num=8,
        next_title="Joining Data (Merge)",
        next_file="lesson08_joining_data_merge.html",
        c1=("arrows-left-right", "Merging Two DataFrames on a Shared Key"),
        c2=("scale-balanced",    "Choosing the Right Join Type"),
        c3=("magnifying-glass",  "Verifying Merge Results with Row Counts"),
        prev_file="lesson06_creating_calculated_columns.html",
        prev_title="Creating Calculated Columns",
    ),

    f"{MOD01}/lesson08_joining_data_merge.html": dict(
        next_mod=1, next_num=9,
        next_title="Handling Missing Data",
        next_file="lesson09_handling_missing_data.html",
        c1=("circle-question", "Detecting Missing Values in a DataFrame"),
        c2=("minus",           "Dropping Rows and Columns with Nulls"),
        c3=("fill",            "Filling Missing Values with Sensible Defaults"),
        prev_file="lesson07_aggregations_group_by.html",
        prev_title="Aggregations (GROUP BY)",
    ),

    f"{MOD01}/lesson09_handling_missing_data.html": dict(
        next_mod=1, next_num=10,
        next_title="Exporting Data",
        next_file="lesson10_exporting_data.html",
        c1=("download",    "Saving a DataFrame as a CSV File"),
        c2=("file-lines",  "Writing Results to an Excel File"),
        c3=("sliders",     "Controlling Columns and Index in Output"),
        prev_file="lesson08_joining_data_merge.html",
        prev_title="Joining Data (Merge)",
    ),

    f"{MOD01}/lesson10_exporting_data.html": dict(
        next_mod=2, next_num=1,
        next_title="Reading CSV Files",
        next_file=f"../{MOD02}/lesson01_reading_csv_files.html",
        c1=("gear",    "Handling Custom Delimiters and Encodings"),
        c2=("filter",  "Loading Only the Columns You Need"),
        c3=("bolt",    "Speeding Up Reads on Large CSV Files"),
        prev_file="lesson09_handling_missing_data.html",
        prev_title="Handling Missing Data",
    ),

    # ── Module 02 ──────────────────────────────────────────────────────────────

    f"{MOD02}/lesson01_reading_csv_files.html": dict(
        next_mod=2, next_num=2,
        next_title="Working with JSON Files",
        next_file="lesson02_working_with_json_files.html",
        c1=("code",            "Reading a Flat JSON File into pandas"),
        c2=("diagram-project", "Normalising Nested JSON Structures"),
        c3=("upload",          "Writing a DataFrame Back to JSON"),
        prev_file=f"../{MOD01}/lesson10_exporting_data.html",
        prev_title="Exporting Data",
    ),

    f"{MOD02}/lesson02_working_with_json_files.html": dict(
        next_mod=2, next_num=3,
        next_title="Connecting to Databases",
        next_file="lesson03_connecting_to_databases.html",
        c1=("plug",  "Building a Database Connection String"),
        c2=("link",  "Connecting with SQLAlchemy"),
        c3=("table", "Loading a Database Table into pandas"),
        prev_file="lesson01_reading_csv_files.html",
        prev_title="Reading CSV Files",
    ),

    f"{MOD02}/lesson03_connecting_to_databases.html": dict(
        next_mod=2, next_num=4,
        next_title="Running SQL in Python",
        next_file="lesson04_running_sql_in_python.html",
        c1=("database",    "Executing a SQL SELECT from Python"),
        c2=("shield",      "Passing Query Parameters Safely"),
        c3=("table-cells", "Loading Query Results as a DataFrame"),
        prev_file="lesson02_working_with_json_files.html",
        prev_title="Working with JSON Files",
    ),

    f"{MOD02}/lesson04_running_sql_in_python.html": dict(
        next_mod=2, next_num=5,
        next_title="Writing Data Back to a Database",
        next_file="lesson05_writing_data_back_to_a_database.html",
        c1=("upload",  "Pushing a DataFrame to a Database Table"),
        c2=("sliders", "Choosing Append, Replace, or Error Mode"),
        c3=("wrench",  "Fixing Type Mismatches Before Writing"),
        prev_file="lesson03_connecting_to_databases.html",
        prev_title="Connecting to Databases",
    ),

    f"{MOD02}/lesson05_writing_data_back_to_a_database.html": dict(
        next_mod=2, next_num=6,
        next_title="Managing Credentials (.env)",
        next_file="lesson06_managing_credentials_env.html",
        c1=("lock",       "Why Hard-Coding Passwords Is Dangerous"),
        c2=("file-lines", "Storing Secrets in a .env File"),
        c3=("shield",     "Keeping Credentials Out of Version Control"),
        prev_file="lesson04_running_sql_in_python.html",
        prev_title="Running SQL in Python",
    ),

    f"{MOD02}/lesson06_managing_credentials_env.html": dict(
        next_mod=3, next_num=1,
        next_title="Why Analysts Use Python",
        next_file=f"../{MOD03}/lesson01_why_analysts_use_python.html",
        c1=("chart-bar",       "What Python Adds to an Analyst's Toolkit"),
        c2=("cubes",           "The Core Analytics Libraries"),
        c3=("diagram-project", "Where Python Fits in a Data Workflow"),
        prev_file="lesson05_writing_data_back_to_a_database.html",
        prev_title="Writing Data Back to a Database",
    ),

    # ── Module 03 ──────────────────────────────────────────────────────────────

    f"{MOD03}/lesson01_why_analysts_use_python.html": dict(
        next_mod=3, next_num=2,
        next_title="Replacing Excel Workflows with Python",
        next_file="lesson02_replacing_excel_workflows_with_python.html",
        c1=("arrows-left-right",  "Replacing VLOOKUP with pandas merge"),
        c2=("table-cells-large",  "Replacing Pivot Tables with groupby"),
        c3=("rotate",             "Automating Repetitive Copy-Paste Steps"),
        prev_file=f"../{MOD02}/lesson06_managing_credentials_env.html",
        prev_title="Managing Credentials (.env)",
    ),

    f"{MOD03}/lesson02_replacing_excel_workflows_with_python.html": dict(
        next_mod=3, next_num=3,
        next_title="Using Python with SQL Queries",
        next_file="lesson03_using_python_with_sql_queries.html",
        c1=("database",    "Running Parameterised SQL Queries from Python"),
        c2=("layer-group", "Combining SQL Results with pandas"),
        c3=("folder",      "Organising Query Strings in a Script"),
        prev_file="lesson01_why_analysts_use_python.html",
        prev_title="Why Analysts Use Python",
    ),

    f"{MOD03}/lesson03_using_python_with_sql_queries.html": dict(
        next_mod=3, next_num=4,
        next_title="Automating Repetitive Data Tasks",
        next_file="lesson04_automating_repetitive_data_tasks.html",
        c1=("magnifying-glass", "Identifying Tasks Worth Automating"),
        c2=("rotate",           "Looping Over Multiple Files at Once"),
        c3=("clock",            "Scheduling a Script to Run Automatically"),
        prev_file="lesson02_replacing_excel_workflows_with_python.html",
        prev_title="Replacing Excel Workflows with Python",
    ),

    f"{MOD03}/lesson04_automating_repetitive_data_tasks.html": dict(
        next_mod=3, next_num=5,
        next_title="Building a Simple Reporting Script",
        next_file="lesson05_building_a_simple_reporting_script.html",
        c1=("sitemap",    "Structuring a Clean Reporting Script"),
        c2=("file-lines", "Writing Results to Multiple Excel Sheets"),
        c3=("chart-bar",  "Adding Summary Statistics to a Report"),
        prev_file="lesson03_using_python_with_sql_queries.html",
        prev_title="Using Python with SQL Queries",
    ),

    f"{MOD03}/lesson05_building_a_simple_reporting_script.html": dict(
        next_mod=3, next_num=6,
        next_title="Automating Reports End-to-End",
        next_file="lesson06_automating_reports_end_to_end.html",
        c1=("link",    "Connecting All Pipeline Steps Together"),
        c2=("shield",  "Handling Errors So Pipelines Don't Crash"),
        c3=("clock",   "Scheduling and Logging Automated Runs"),
        prev_file="lesson04_automating_repetitive_data_tasks.html",
        prev_title="Automating Repetitive Data Tasks",
    ),

    f"{MOD03}/lesson06_automating_reports_end_to_end.html": dict(
        next_mod=4, next_num=2,
        next_title="Memory Optimization",
        next_file=f"../{MOD04}/lesson02_memory_optimization.html",
        c1=("memory",          "Why DataFrames Use More RAM Than Expected"),
        c2=("magnifying-glass","Inspecting Memory Usage Column by Column"),
        c3=("compress",        "Downcasting Types to Cut RAM Usage"),
        prev_file="lesson05_building_a_simple_reporting_script.html",
        prev_title="Building a Simple Reporting Script",
    ),

    # ── Module 04 ──────────────────────────────────────────────────────────────

    f"{MOD04}/lesson02_memory_optimization.html": dict(
        next_mod=4, next_num=3,
        next_title="Chunk Processing",
        next_file="lesson03_chunk_processing.html",
        c1=("triangle-exclamation", "Why Large Files Exhaust Available Memory"),
        c2=("layer-group",           "Reading a CSV File in Chunks"),
        c3=("object-group",          "Combining Results from Each Chunk"),
        prev_file=f"../{MOD03}/lesson06_automating_reports_end_to_end.html",
        prev_title="Automating Reports End-to-End",
    ),

    f"{MOD04}/lesson03_chunk_processing.html": dict(
        next_mod=4, next_num=4,
        next_title="Processing Millions of Rows",
        next_file="lesson04_processing_millions_of_rows.html",
        c1=("stopwatch",   "Spotting the Slow Operations in a Pipeline"),
        c2=("bolt",        "Replacing Loops with Vectorised Operations"),
        c3=("gauge-high",  "Benchmarking Code Before and After Changes"),
        prev_file="lesson02_memory_optimization.html",
        prev_title="Memory Optimization",
    ),

    f"{MOD04}/lesson04_processing_millions_of_rows.html": dict(
        next_mod=4, next_num=5,
        next_title="Columnar Storage",
        next_file="lesson05_columnar_storage.html",
        c1=("database",       "What Columnar Storage Is and How It Works"),
        c2=("scale-balanced", "Row-Based vs. Columnar Format Comparison"),
        c3=("bolt",           "How Columnar Files Read Less Data from Disk"),
        prev_file="lesson03_chunk_processing.html",
        prev_title="Chunk Processing",
    ),

    f"{MOD04}/lesson05_columnar_storage.html": dict(
        next_mod=4, next_num=6,
        next_title="Parquet Files",
        next_file="lesson06_parquet_files.html",
        c1=("file-lines",     "What a Parquet File Is"),
        c2=("download",       "Writing and Reading Parquet with pandas"),
        c3=("scale-balanced", "Parquet vs. CSV: Size and Speed Comparison"),
        prev_file="lesson04_processing_millions_of_rows.html",
        prev_title="Processing Millions of Rows",
    ),

    f"{MOD04}/lesson06_parquet_files.html": dict(
        next_mod=4, next_num=13,
        next_title="Performance Profiling",
        next_file="lesson13_performance_profiling.html",
        c1=("stopwatch",       "Measuring How Long Each Operation Takes"),
        c2=("magnifying-glass","Finding the Slowest Steps with cProfile"),
        c3=("list-check",      "Documenting and Prioritising Performance Fixes"),
        prev_file="lesson05_columnar_storage.html",
        prev_title="Columnar Storage",
    ),

    # Last lesson — no next section, only bottom nav
    f"{MOD04}/lesson13_performance_profiling.html": dict(
        next_mod=None, next_num=None,
        next_title=None,
        next_file=None,
        c1=None, c2=None, c3=None,
        prev_file="lesson06_parquet_files.html",
        prev_title="Parquet Files",
    ),
}

# ── Regex: match old #next-lesson section + old bottom nav div ────────────────
PATTERN = re.compile(
    r'<section id="next-lesson">.*?(?=[ \t]*</main>)',
    re.DOTALL
)

# ── Apply ─────────────────────────────────────────────────────────────────────

ok = fail = 0

for rel_path, d in LESSONS.items():
    abs_path = os.path.join(ROOT, rel_path.replace("/", os.sep))
    if not os.path.exists(abs_path):
        print(f"  ❌ FILE NOT FOUND: {rel_path}")
        fail += 1
        continue

    with open(abs_path, encoding="utf-8") as fh:
        html = fh.read()

    # Build replacement HTML
    if d["next_file"] is None:
        # Last lesson — no #next-lesson section, just the bottom nav
        replacement = bottom_nav(
            d["prev_file"], d["prev_title"],
            None, None,
        )
    else:
        nl_section = next_lesson_section(
            d["next_mod"], d["next_num"], d["next_title"], d["next_file"],
            d["c1"], d["c2"], d["c3"],
        )
        nav = bottom_nav(
            d["prev_file"], d["prev_title"],
            d["next_file"], d["next_title"],
        )
        replacement = nl_section + "\n\n" + nav

    new_html, count = PATTERN.subn(replacement, html, count=1)

    if count == 0:
        print(f"  ⚠️  PATTERN NOT FOUND: {rel_path}")
        fail += 1
        continue

    with open(abs_path, "w", encoding="utf-8") as fh:
        fh.write(new_html)

    print(f"  ✅ {rel_path}")
    ok += 1

print(f"\n{ok}/{ok+fail} files updated.")
if fail:
    sys.exit(1)
