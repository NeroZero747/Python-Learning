#!/usr/bin/env python3
"""Rewrite #recap section for all 28 track_02 lessons."""

import re, os, sys

ROOT = r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics"

# ── HTML builders ─────────────────────────────────────────────────────────────

def card(num, icon, label, sentence):
    return (
        f'  <!-- Card {num} -->\n'
        f'  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">\n'
        f'    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">\n'
        f'      <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{num}</span>\n'
        f'      <div class="relative flex items-start gap-3">\n'
        f'        <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">\n'
        f'          <span class="iconify text-sm" data-icon="{icon}"></span>\n'
        f'        </span>\n'
        f'        <div>\n'
        f'          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">{label}</p>\n'
        f'          <p class="text-[11px] text-gray-600 leading-snug">{sentence}</p>\n'
        f'        </div>\n'
        f'      </div>\n'
        f'    </div>\n'
        f'  </div>'
    )

BANNER = (
    '  <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">\n'
    '    <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>\n'
    '    <div class="relative flex items-center gap-4">\n'
    '      <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">\n'
    '        <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>\n'
    '      </span>\n'
    '      <div>\n'
    '        <p class="text-sm font-bold text-white">Lesson Complete!</p>\n'
    '        <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 4 key concepts. Ready for the knowledge check?</p>\n'
    '      </div>\n'
    '    </div>\n'
    '  </div>'
)

SECTION_HEADER = (
    '<section id="recap">\n'
    '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
    '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
    '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
    '        <span class="iconify text-white text-base" data-icon="fa6-solid:list-check"></span>\n'
    '      </span>\n'
    '      <div class="min-w-0">\n'
    '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Recap</h2>\n'
    '        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A quick summary of what you learned</p>\n'
    '      </div>\n'
    '    </div>\n'
    '    <div class="bg-white px-8 py-7 space-y-6">\n'
)
SECTION_FOOTER = '    </div>\n  </div>\n</section>'

def build_section(cards_data):
    grid_rows = []
    for i, (icon, label, sentence) in enumerate(cards_data):
        num = f"{i+1:02d}"
        grid_rows.append(card(num, icon, label, sentence))
    grid = (
        '      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n\n'
        + '\n\n'.join(grid_rows) + '\n\n'
        '      </div>\n'
    )
    return SECTION_HEADER + '\n' + grid + '\n' + BANNER + '\n\n' + SECTION_FOOTER


# ── Lesson data ───────────────────────────────────────────────────────────────
# Each entry: list of 4 tuples (icon, label, sentence)
# Labels and icons extracted from #objective sections exactly.

MOD01 = "mod_01_data_analysis_with_pandas"
MOD02 = "mod_02_working_with_data_sources"
MOD03 = "mod_03_python_for_analysts"
MOD04 = "mod_04_handling_large_data"

LESSONS = {

    f"{MOD01}/lesson01_introduction_to_pandas.html": [
        ("fa6-solid:book-open",    "What pandas is",
         "Pandas is a Python library that loads data files into structured tables."),
        ("fa6-solid:chart-bar",    "Why analysts use it",
         "You can filter, calculate, and summarise any dataset without clicking menus."),
        ("fa6-solid:table",        "DataFrames, rows and columns",
         "Every data file pandas opens becomes a DataFrame of rows and columns."),
        ("fa6-solid:puzzle-piece", "Where pandas fits",
         "Pandas sits between your raw data file and any chart or report you build."),
    ],

    f"{MOD01}/lesson02_dataframes_explained.html": [
        ("fa6-solid:table-cells",       "What a DataFrame is",
         "A DataFrame is an in-memory table of rows and columns that pandas manages."),
        ("fa6-solid:grip-lines",        "Index, rows and columns",
         "Every row has an index address; every column holds one field of data."),
        ("fa6-solid:plus",              "Build a DataFrame",
         "You can construct a DataFrame from a dictionary using <code class=\"font-mono\">pd.DataFrame()</code>."),
        ("fa6-solid:magnifying-glass",  "Check shape and types",
         "<code class=\"font-mono\">df.shape</code> and <code class=\"font-mono\">df.dtypes</code> confirm row count and column types."),
    ],

    f"{MOD01}/lesson03_reading_data_csv_excel.html": [
        ("fa6-solid:file-arrow-down",       "Load a CSV file",
         "<code class=\"font-mono\">pd.read_csv()</code> opens any CSV into a DataFrame in one line."),
        ("fa6-solid:file-lines",            "Read Excel files",
         "<code class=\"font-mono\">pd.read_excel()</code> loads any sheet from an xlsx file by name."),
        ("fa6-solid:eye",                   "Inspect data after loading",
         "<code class=\"font-mono\">df.head()</code> shows the first five rows immediately after loading."),
        ("fa6-solid:triangle-exclamation",  "Fix common load errors",
         "Wrong separators and encodings are fixed with the <code class=\"font-mono\">sep=</code> and <code class=\"font-mono\">encoding=</code> parameters."),
    ],

    f"{MOD01}/lesson04_selecting_columns.html": [
        ("fa6-solid:hand-pointer",  "Select a single column",
         "You can pull one column by typing its name inside square brackets."),
        ("fa6-solid:layer-group",   "Select multiple columns",
         "Passing a list of names returns a smaller DataFrame with only those columns."),
        ("fa6-solid:pen",           "Rename columns cleanly",
         "<code class=\"font-mono\">rename()</code> replaces cryptic column names with clear, consistent labels."),
        ("fa6-solid:list",          "List all column names",
         "<code class=\"font-mono\">df.columns</code> returns every column name so you can check them at a glance."),
    ],

    f"{MOD01}/lesson05_filtering_rows.html": [
        ("fa6-solid:filter",        "Filter by a condition",
         "A Boolean condition inside brackets keeps only the rows that match your rule."),
        ("fa6-solid:code-branch",   "Combine filter conditions",
         "<code class=\"font-mono\">&amp;</code> and <code class=\"font-mono\">|</code> let you apply two rules in a single filter step."),
        ("fa6-solid:list-check",    "Filter with a value list",
         "<code class=\"font-mono\">isin()</code> keeps rows whose column value appears in a list you provide."),
        ("fa6-solid:circle-xmark",  "Remove missing rows",
         "<code class=\"font-mono\">dropna()</code> removes every row that contains at least one missing value."),
    ],

    f"{MOD01}/lesson06_creating_calculated_columns.html": [
        ("fa6-solid:calculator",    "Add a calculated column",
         "Assigning an expression to a new column name adds it to every row at once."),
        ("fa6-solid:percent",       "Apply arithmetic operations",
         "Standard operators like <code class=\"font-mono\">+</code>, <code class=\"font-mono\">*</code>, and <code class=\"font-mono\">/</code> run across every row simultaneously."),
        ("fa6-solid:sliders",       "Set values conditionally",
         "<code class=\"font-mono\">np.where()</code> assigns different values to each row based on a condition."),
        ("fa6-solid:trash",         "Delete unwanted columns",
         "<code class=\"font-mono\">drop()</code> removes any column you no longer need from the DataFrame."),
    ],

    f"{MOD01}/lesson07_aggregations_group_by.html": [
        ("fa6-solid:object-group",  "Group data by category",
         "<code class=\"font-mono\">groupby()</code> splits rows into separate groups on any column you choose."),
        ("fa6-solid:chart-column",  "Compute group totals",
         "Functions like <code class=\"font-mono\">sum()</code>, <code class=\"font-mono\">mean()</code>, and <code class=\"font-mono\">count()</code> produce one result per group."),
        ("fa6-solid:sliders",       "Apply multiple aggregations",
         "<code class=\"font-mono\">agg()</code> calculates several different metrics across all group columns at once."),
        ("fa6-solid:rotate",        "Reset the index after grouping",
         "<code class=\"font-mono\">reset_index()</code> turns grouped labels back into plain columns for export."),
    ],

    f"{MOD01}/lesson08_joining_data_merge.html": [
        ("fa6-solid:arrows-left-right", "Merge two DataFrames",
         "<code class=\"font-mono\">merge()</code> joins two tables on any shared key column you specify."),
        ("fa6-solid:scale-balanced",    "Choose the right join type",
         "The <code class=\"font-mono\">how=</code> parameter controls whether unmatched rows are kept or dropped."),
        ("fa6-solid:key",               "Join on multiple keys",
         "Passing a list to <code class=\"font-mono\">on=</code> matches rows across two or more key columns."),
        ("fa6-solid:magnifying-glass",  "Spot mismatched keys",
         "Comparing row counts before and after merge reveals rows that had no matching key."),
    ],

    f"{MOD01}/lesson09_handling_missing_data.html": [
        ("fa6-solid:circle-question",   "Detect missing values",
         "<code class=\"font-mono\">isnull().sum()</code> counts exactly how many gaps exist in each column."),
        ("fa6-solid:minus",             "Drop rows or columns",
         "<code class=\"font-mono\">dropna()</code> removes rows or columns based on how many nulls they contain."),
        ("fa6-solid:fill",              "Fill missing values",
         "<code class=\"font-mono\">fillna()</code> replaces every gap with a constant, mean, or forward-filled value."),
        ("fa6-solid:brain",             "Pick the right strategy",
         "Your fill strategy must match the data — use mean for numbers, mode for categories."),
    ],

    f"{MOD01}/lesson10_exporting_data.html": [
        ("fa6-solid:download",      "Save to CSV",
         "<code class=\"font-mono\">to_csv()</code> writes the DataFrame to a plain text file any tool can open."),
        ("fa6-solid:file-lines",    "Write to Excel",
         "<code class=\"font-mono\">to_excel()</code> creates an xlsx file from any DataFrame with one call."),
        ("fa6-solid:sliders",       "Control columns and index",
         "The <code class=\"font-mono\">index=False</code> and <code class=\"font-mono\">columns=</code> parameters control what appears in the export."),
        ("fa6-solid:plus",          "Append without overwriting",
         "<code class=\"font-mono\">ExcelWriter</code> lets you write multiple DataFrames into separate sheets at once."),
    ],

    # ── Module 02 ─────────────────────────────────────────────────────────────

    f"{MOD02}/lesson01_reading_csv_files.html": [
        ("fa6-solid:gear",      "Read custom delimiters",
         "The <code class=\"font-mono\">sep=</code> parameter handles any delimiter — tab, pipe, or semicolon."),
        ("fa6-solid:filter",    "Load selected columns only",
         "<code class=\"font-mono\">usecols=</code> tells pandas to read only the columns your analysis needs."),
        ("fa6-solid:language",  "Fix encoding issues",
         "The <code class=\"font-mono\">encoding=</code> parameter prevents garbled characters from non-ASCII files."),
        ("fa6-solid:bolt",      "Speed up large file loads",
         "Combining <code class=\"font-mono\">usecols=</code> and <code class=\"font-mono\">dtype=</code> cuts load time significantly on wide files."),
    ],

    f"{MOD02}/lesson02_working_with_json_files.html": [
        ("fa6-solid:code",              "Read a JSON file",
         "<code class=\"font-mono\">pd.read_json()</code> loads a flat JSON file directly into a DataFrame."),
        ("fa6-solid:diagram-project",   "Normalise nested JSON",
         "<code class=\"font-mono\">json_normalize()</code> unpacks nested keys into separate flat columns."),
        ("fa6-solid:upload",            "Write DataFrame as JSON",
         "<code class=\"font-mono\">to_json()</code> converts your DataFrame back to a JSON string or file."),
        ("fa6-solid:sitemap",           "Handle different JSON shapes",
         "Flat arrays and nested objects each need a different parsing approach to load correctly."),
    ],

    f"{MOD02}/lesson03_connecting_to_databases.html": [
        ("fa6-solid:plug",          "Build a connection string",
         "A connection string contains the database type, host, port, and login credentials."),
        ("fa6-solid:link",          "Connect with SQLAlchemy",
         "<code class=\"font-mono\">create_engine()</code> builds the connection object pandas uses to talk to any database."),
        ("fa6-solid:table",         "Load a table into pandas",
         "<code class=\"font-mono\">read_sql_table()</code> fetches an entire database table as a DataFrame."),
        ("fa6-solid:circle-check",  "Close connections safely",
         "Using a <code class=\"font-mono\">with</code> block ensures the connection closes even if your script crashes."),
    ],

    f"{MOD02}/lesson04_running_sql_in_python.html": [
        ("fa6-solid:database",      "Run a SQL query",
         "<code class=\"font-mono\">read_sql()</code> sends any SELECT statement and returns the result as a DataFrame."),
        ("fa6-solid:shield",        "Pass safe parameters",
         "Passing filter values through <code class=\"font-mono\">params=</code> prevents SQL injection vulnerabilities."),
        ("fa6-solid:table-cells",   "Load results as DataFrames",
         "Every query result lands in a DataFrame, ready for pandas filtering and aggregation."),
        ("fa6-solid:sitemap",       "Query multiple tables",
         "JOIN logic written in SQL runs in the database, which is faster than merging in pandas."),
    ],

    f"{MOD02}/lesson05_writing_data_back_to_a_database.html": [
        ("fa6-solid:upload",    "Write a DataFrame to a table",
         "<code class=\"font-mono\">to_sql()</code> pushes every row of a DataFrame into a database table."),
        ("fa6-solid:sliders",   "Choose the write mode",
         "<code class=\"font-mono\">if_exists='replace'</code> overwrites; <code class=\"font-mono\">if_exists='append'</code> adds rows to an existing table."),
        ("fa6-solid:table",     "Create tables automatically",
         "When the target table does not exist, <code class=\"font-mono\">to_sql()</code> creates it from the DataFrame schema."),
        ("fa6-solid:wrench",    "Fix type mismatches",
         "The <code class=\"font-mono\">dtype=</code> parameter ensures each column matches the database column type exactly."),
    ],

    f"{MOD02}/lesson06_managing_credentials_env.html": [
        ("fa6-solid:lock",          "Never hard-code passwords",
         "A password in your script is visible to anyone who opens or receives the file."),
        ("fa6-solid:file-lines",    "Use .env files",
         "A <code class=\"font-mono\">.env</code> file stores credentials as key-value pairs outside your code."),
        ("fa6-solid:gear",          "Load env vars with dotenv",
         "<code class=\"font-mono\">load_dotenv()</code> reads the <code class=\"font-mono\">.env</code> file and makes every variable available to your script."),
        ("fa6-solid:shield",        "Keep secrets out of Git",
         "Adding <code class=\"font-mono\">.env</code> to <code class=\"font-mono\">.gitignore</code> prevents credentials from ever reaching a repository."),
    ],

    # ── Module 03 ─────────────────────────────────────────────────────────────

    f"{MOD03}/lesson01_why_analysts_use_python.html": [
        ("fa6-solid:chart-bar",         "What Python adds to analysts",
         "Python automates repetitive data tasks that would take hours in Excel manually."),
        ("fa6-solid:cubes",             "Key analytics libraries",
         "Pandas, NumPy, and Matplotlib together cover loading, calculating, and charting data."),
        ("fa6-solid:diagram-project",   "Python in a workflow",
         "Python connects to databases, processes files, and delivers reports without manual steps."),
        ("fa6-solid:scale-balanced",    "When to choose Python",
         "Choose Python when data is too large for Excel, or the task must repeat automatically."),
    ],

    f"{MOD03}/lesson02_replacing_excel_workflows_with_python.html": [
        ("fa6-solid:arrows-left-right", "Replicate VLOOKUP with merge",
         "<code class=\"font-mono\">merge()</code> performs the same lookup as VLOOKUP without formula columns or row limits."),
        ("fa6-solid:table-cells-large", "Replace pivot tables",
         "<code class=\"font-mono\">groupby()</code> produces identical pivot-style totals in one line on any file size."),
        ("fa6-solid:file-lines",        "Generate multi-sheet reports",
         "<code class=\"font-mono\">ExcelWriter</code> writes multiple DataFrames to named sheets in a single xlsx file."),
        ("fa6-solid:rotate",            "Automate repetitive steps",
         "A folder loop processes every file automatically — no opening or saving by hand."),
    ],

    f"{MOD03}/lesson03_using_python_with_sql_queries.html": [
        ("fa6-solid:database",      "Run parameterised SQL",
         "Parameterised queries pass filter values safely without rewriting the SQL string."),
        ("fa6-solid:layer-group",   "Combine SQL with pandas",
         "SQL handles filtering at source; pandas reshapes and enriches the results afterwards."),
        ("fa6-solid:folder",        "Organise query strings",
         "Storing SQL in named variables or <code class=\"font-mono\">.sql</code> files keeps Python code readable and clean."),
        ("fa6-solid:stopwatch",     "Profile slow queries",
         "Measuring each SQL call reveals whether the bottleneck is in the database or the Python code."),
    ],

    f"{MOD03}/lesson04_automating_repetitive_data_tasks.html": [
        ("fa6-solid:magnifying-glass",  "Identify automatable tasks",
         "Any task you repeat weekly with the same steps is a good candidate for automation."),
        ("fa6-solid:rotate",            "Loop over multiple files",
         "A <code class=\"font-mono\">for</code> loop over a folder processes every file without opening each one manually."),
        ("fa6-solid:clock",             "Schedule a script to run",
         "Task Scheduler on Windows and cron on Mac/Linux run your script at a set time."),
        ("fa6-solid:list",              "Log automated results",
         "Writing a timestamped log entry after each run proves the automation completed successfully."),
    ],

    f"{MOD03}/lesson05_building_a_simple_reporting_script.html": [
        ("fa6-solid:sitemap",   "Structure a report script",
         "Splitting load, transform, and export into labelled sections keeps your script readable."),
        ("fa6-solid:pen",       "Format numbers and dates",
         "You can apply consistent date formats and number rounding before writing to Excel."),
        ("fa6-solid:file-lines","Export with multiple sheets",
         "<code class=\"font-mono\">ExcelWriter</code> places each summary DataFrame onto its own named worksheet."),
        ("fa6-solid:chart-bar", "Add summary statistics",
         "A totals row or column computed with <code class=\"font-mono\">sum()</code> gives readers the headline figure instantly."),
    ],

    f"{MOD03}/lesson06_automating_reports_end_to_end.html": [
        ("fa6-solid:link",      "Connect all pipeline steps",
         "Each function hands its output to the next so the whole pipeline runs in one call."),
        ("fa6-solid:shield",    "Handle errors gracefully",
         "<code class=\"font-mono\">try/except</code> catches failures and writes the error to a log without crashing the script."),
        ("fa6-solid:envelope",  "Send reports by email",
         "Python's <code class=\"font-mono\">smtplib</code> can attach a finished Excel file and send it to any inbox."),
        ("fa6-solid:clock",     "Schedule and log runs",
         "Combining a scheduler with a log file gives you a full audit trail of every automated run."),
    ],

    # ── Module 04 ─────────────────────────────────────────────────────────────

    f"{MOD04}/lesson02_memory_optimization.html": [
        ("fa6-solid:memory",            "Why DataFrames use so much RAM",
         "Pandas defaults to 64-bit types for every column, even when 8-bit would hold all values."),
        ("fa6-solid:magnifying-glass",  "Inspect memory column by column",
         "<code class=\"font-mono\">memory_usage(deep=True)</code> shows exactly how many bytes each column uses."),
        ("fa6-solid:compress",          "Downcast numeric columns",
         "<code class=\"font-mono\">pd.to_numeric(df[col], downcast='integer')</code> shrinks a column to the smallest fitting type."),
        ("fa6-solid:tags",              "Use categorical columns",
         "Converting a repeated-string column to <code class=\"font-mono\">category</code> type can reduce its RAM use by 80%."),
    ],

    f"{MOD04}/lesson03_chunk_processing.html": [
        ("fa6-solid:triangle-exclamation",  "Why large files crash Python",
         "Loading a file larger than available RAM causes a <code class=\"font-mono\">MemoryError</code> and halts the script."),
        ("fa6-solid:layer-group",           "Read CSV files in chunks",
         "<code class=\"font-mono\">chunksize=</code> makes <code class=\"font-mono\">read_csv()</code> return an iterator that delivers rows in batches."),
        ("fa6-solid:rotate",                "Process each chunk in turn",
         "A <code class=\"font-mono\">for</code> loop over the iterator handles one batch at a time, then frees its memory."),
        ("fa6-solid:object-group",          "Combine chunk results",
         "Collecting partial results from each chunk and concatenating at the end assembles the final output."),
    ],

    f"{MOD04}/lesson04_processing_millions_of_rows.html": [
        ("fa6-solid:stopwatch",     "Spot slow operations",
         "<code class=\"font-mono\">time.time()</code> before and after each step reveals which line is the bottleneck."),
        ("fa6-solid:bolt",          "Use vectorised calculations",
         "Vectorised pandas expressions run in compiled C and are up to 100 times faster than for-loops."),
        ("fa6-solid:gear",          "Apply complex column logic",
         "<code class=\"font-mono\">apply()</code> runs a custom Python function row by row when no vectorised alternative exists."),
        ("fa6-solid:gauge-high",    "Benchmark your code",
         "Testing on a realistic data size confirms whether a change actually improves production performance."),
    ],

    f"{MOD04}/lesson05_columnar_storage.html": [
        ("fa6-solid:bars",          "What columnar storage is",
         "Columnar storage keeps all values of one column together on disk rather than row by row."),
        ("fa6-solid:scale-balanced","Row vs. columnar comparison",
         "Row formats scan every field; columnar formats read only the columns your query touches."),
        ("fa6-solid:compress",      "How columnar reads less data",
         "Columnar files skip entire column groups on disk, so analytics queries read far fewer bytes."),
        ("fa6-solid:cube",          "Columnar formats in Python",
         "Parquet and ORC are the two columnar formats that pandas reads and writes natively."),
    ],

    f"{MOD04}/lesson06_parquet_files.html": [
        ("fa6-solid:file-lines",    "What Parquet files are",
         "Parquet is a binary, column-oriented format built for fast analytics reads."),
        ("fa6-solid:download",      "Write a DataFrame to Parquet",
         "<code class=\"font-mono\">to_parquet()</code> saves any DataFrame in compressed binary format in one call."),
        ("fa6-solid:filter",        "Read and filter efficiently",
         "<code class=\"font-mono\">read_parquet(columns=[])</code> loads only the columns you name, skipping the rest."),
        ("fa6-solid:scale-balanced","Parquet versus CSV size",
         "A snappy-compressed Parquet file is typically half the size of the equivalent CSV."),
    ],

    f"{MOD04}/lesson13_performance_profiling.html": [
        ("fa6-solid:stopwatch",         "Measure operation time",
         "<code class=\"font-mono\">time.time()</code> timestamps let you measure the wall-clock duration of each step."),
        ("fa6-solid:magnifying-glass",  "Find the slowest steps",
         "<code class=\"font-mono\">cProfile</code> ranks every function call by total time, revealing the true bottleneck."),
        ("fa6-solid:code",              "Use cProfile and line_profiler",
         "<code class=\"font-mono\">line_profiler</code> zooms into a single function and times each line individually."),
        ("fa6-solid:list-check",        "Document and prioritise fixes",
         "Recording before-and-after timings confirms each optimisation actually improved performance."),
    ],
}

# ── Regex ─────────────────────────────────────────────────────────────────────

PATTERN = re.compile(r'<section id="recap">.*?</section>', re.DOTALL)

# ── Apply ─────────────────────────────────────────────────────────────────────

ok = fail = 0

for rel_path, cards_data in LESSONS.items():
    abs_path = os.path.join(ROOT, rel_path.replace("/", os.sep))
    if not os.path.exists(abs_path):
        print(f"  ❌ FILE NOT FOUND: {rel_path}")
        fail += 1
        continue

    html = open(abs_path, encoding="utf-8").read()
    new_section = build_section(cards_data)
    new_html, count = PATTERN.subn(new_section, html, count=1)

    if count == 0:
        print(f"  ⚠️  PATTERN NOT FOUND: {rel_path}")
        fail += 1
        continue

    open(abs_path, "w", encoding="utf-8").write(new_html)
    print(f"  ✅ {rel_path}")
    ok += 1

print(f"\n{ok}/{ok+fail} files updated.")
if fail:
    sys.exit(1)
