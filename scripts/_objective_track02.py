#!/usr/bin/env python3
"""Apply rewritten #objective sections to all 28 track_02 lessons."""

import re, os, sys

ROOT = r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics"

# ── Templates ────────────────────────────────────────────────────────────────

SECTION_OPEN = '''\
        <section id="objective">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:bullseye"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Objective</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The goal and expected outcome of this lesson</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">'''

SECTION_CLOSE = '''\
      </div>
      <div class="mt-5">
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">TIP_PLACEHOLDER</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

CARD_TMPL = '''\
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:ICON_PLACEHOLDER"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">TITLE_PLACEHOLDER</p>
            <p class="text-xs text-gray-500 mt-0.5">DESC_PLACEHOLDER</p>
          </div>
        </div>'''


def build_card(title, icon, desc):
    return (CARD_TMPL
            .replace("ICON_PLACEHOLDER", icon)
            .replace("TITLE_PLACEHOLDER", title)
            .replace("DESC_PLACEHOLDER", desc))


def build_section(cards, tip):
    cards_html = "\n\n".join(build_card(*c) for c in cards)
    close = SECTION_CLOSE.replace("TIP_PLACEHOLDER", tip)
    return SECTION_OPEN + "\n" + cards_html + "\n" + close


# ── Per-lesson data ───────────────────────────────────────────────────────────
#  Each entry: (title ≤5 words, icon, description 12–18 words)

LESSONS = {
    # ── Module 01 — Data Analysis with Pandas ────────────────────────────────
    "mod_01_data_analysis_with_pandas/lesson01_introduction_to_pandas.html": {
        "cards": [
            ("What pandas is",
             "book-open",
             "Pandas is a Python library that turns raw data files into fast, structured tables you can query and analyse."),
            ("Why analysts use it",
             "chart-bar",
             "Pandas processes datasets that would slow Excel to a halt, running complex operations in seconds."),
            ("DataFrames, rows and columns",
             "table",
             "A DataFrame organises data into labelled rows and columns, making selection, filtering, and calculation easy."),
            ("Where pandas fits",
             "puzzle-piece",
             "Pandas works alongside NumPy, Matplotlib, and scikit-learn in the core Python data science stack."),
        ],
        "tip": "This lesson introduces the tool you will rely on throughout every data analysis task in this track.",
    },
    "mod_01_data_analysis_with_pandas/lesson02_dataframes_explained.html": {
        "cards": [
            ("What a DataFrame is",
             "table-cells",
             "A DataFrame is a two-dimensional table of typed rows and columns you can query with Python code."),
            ("Index, rows and columns",
             "grip-lines",
             "Every DataFrame has an index that identifies rows and named columns that hold the values for each field."),
            ("Build a DataFrame",
             "plus",
             "You can create a DataFrame from a dictionary, a list, or any external file you load into pandas."),
            ("Check shape and types",
             "magnifying-glass",
             "The shape attribute shows how many rows and columns exist while dtypes reveals the data type of each column."),
        ],
        "tip": "This lesson teaches the fundamental pandas data structure you will work with in every exercise throughout this track.",
    },
    "mod_01_data_analysis_with_pandas/lesson03_reading_data_csv_excel.html": {
        "cards": [
            ("Load a CSV file",
             "file-arrow-down",
             "The read_csv function in pandas loads any comma-separated file from disk into a structured DataFrame in one line."),
            ("Read Excel files",
             "file-lines",
             "The read_excel function opens an xlsx file and lets you select any sheet by name or number."),
            ("Inspect data after loading",
             "eye",
             "Calling head on a freshly loaded DataFrame shows the first five rows so you can verify the import."),
            ("Fix common load errors",
             "triangle-exclamation",
             "Wrong separator characters, mismatched encodings, and blank header rows are the most common problems you will encounter."),
        ],
        "tip": "This lesson gives you the skills to load real-world data files into Python reliably and without errors.",
    },
    "mod_01_data_analysis_with_pandas/lesson04_selecting_columns.html": {
        "cards": [
            ("Select a single column",
             "hand-pointer",
             "Bracket notation pulls a single column from any DataFrame so you can inspect or transform just that field."),
            ("Select multiple columns",
             "layer-group",
             "Passing a list of column names inside brackets returns a new DataFrame containing only the columns you chose."),
            ("Rename columns cleanly",
             "pen",
             "The rename method replaces cryptic column names with clear, user-facing labels that match your reporting requirements."),
            ("List all column names",
             "list",
             "The columns attribute returns every column name in a DataFrame so you can confirm what fields are available."),
        ],
        "tip": "This lesson shows you how to isolate the columns that matter before you start any analysis on a dataset.",
    },
    "mod_01_data_analysis_with_pandas/lesson05_filtering_rows.html": {
        "cards": [
            ("Filter by a condition",
             "filter",
             "A Boolean condition inside brackets returns only the rows where that condition is true, removing all others."),
            ("Combine filter conditions",
             "code-branch",
             "The and and or operators combine multiple conditions so you can filter by region, date, and product simultaneously."),
            ("Filter with a value list",
             "list-check",
             "The isin method checks whether a column value appears in a given list, returning only the matching rows."),
            ("Remove missing rows",
             "circle-xmark",
             "Calling dropna removes rows that contain null values, ensuring calculations run only on complete, valid records."),
        ],
        "tip": "This lesson gives you precise control over which rows enter your analysis so your results are always accurate.",
    },
    "mod_01_data_analysis_with_pandas/lesson06_creating_calculated_columns.html": {
        "cards": [
            ("Add a calculated column",
             "calculator",
             "Assigning a formula to a new column name computes the value for every row in the DataFrame automatically."),
            ("Apply arithmetic operations",
             "percent",
             "Standard operators like addition, subtraction, and division work directly on DataFrame columns, running across all rows at once."),
            ("Set values conditionally",
             "sliders",
             "Conditional logic lets you assign different column values depending on whether each row meets a specified rule."),
            ("Delete unwanted columns",
             "trash",
             "The drop method removes any column by name, keeping only the fields your downstream report actually needs."),
        ],
        "tip": "This lesson teaches you to derive new metrics from raw data without changing or duplicating the original source file.",
    },
    "mod_01_data_analysis_with_pandas/lesson07_aggregations_group_by.html": {
        "cards": [
            ("Group data by category",
             "object-group",
             "The groupby method splits a DataFrame into groups based on column values, exactly like a SQL GROUP BY clause."),
            ("Compute group totals",
             "chart-column",
             "Functions like sum, mean, and count produce a single aggregated value for every group in the data."),
            ("Apply multiple aggregations",
             "sliders",
             "Passing a dictionary to agg computes totals, averages, and counts for each group column in a single call."),
            ("Reset the index after grouping",
             "rotate",
             "Calling reset_index after a groupby flattens the result back into a plain DataFrame with numbered rows."),
        ],
        "tip": "This lesson replicates the GROUP BY behaviour you already know from SQL, entirely inside a Python script.",
    },
    "mod_01_data_analysis_with_pandas/lesson08_joining_data_merge.html": {
        "cards": [
            ("Merge two DataFrames",
             "arrows-left-right",
             "The merge function joins two DataFrames on a matching column, combining related records into a single table."),
            ("Choose the right join type",
             "scale-balanced",
             "Join type determines whether rows with no match in the other table are kept or discarded from results."),
            ("Join on multiple keys",
             "key",
             "Passing a list to the on parameter merges across several columns at once, handling composite keys correctly."),
            ("Spot mismatched keys",
             "magnifying-glass",
             "Checking row counts and null values after a merge reveals whether keys matched correctly between the two tables."),
        ],
        "tip": "This lesson teaches the pandas equivalent of a SQL JOIN, essential when your data lives across multiple tables.",
    },
    "mod_01_data_analysis_with_pandas/lesson09_handling_missing_data.html": {
        "cards": [
            ("Detect missing values",
             "circle-question",
             "The isnull function marks every missing cell so you can count how many gaps exist in each column."),
            ("Drop rows or columns",
             "minus",
             "The dropna method removes any row or column that contains at least one null value from the DataFrame."),
            ("Fill missing values",
             "fill",
             "The fillna method replaces null cells with a constant value, a column average, or an adjacent row value."),
            ("Pick the right strategy",
             "brain",
             "Numeric columns usually benefit from mean imputation while categorical columns are better filled with the most common value."),
        ],
        "tip": "This lesson prevents silent calculation errors that occur when missing data slips through into aggregations and summaries.",
    },
    "mod_01_data_analysis_with_pandas/lesson10_exporting_data.html": {
        "cards": [
            ("Save to CSV",
             "download",
             "The to_csv method writes a DataFrame to disk as a comma-separated file that any spreadsheet tool can open."),
            ("Write to Excel",
             "file-lines",
             "The to_excel method creates an xlsx file from a DataFrame, with options for formatting headers and column widths."),
            ("Control columns and index",
             "sliders",
             "Keyword arguments let you include or exclude the index and choose exactly which columns appear in the output file."),
            ("Append without overwriting",
             "plus",
             "Opening an existing file with ExcelWriter in append mode adds a new sheet without deleting data already there."),
        ],
        "tip": "This lesson completes the data pipeline — turning a processed, clean DataFrame back into a shareable, deliverable file.",
    },

    # ── Module 02 — Working with Data Sources ────────────────────────────────
    "mod_02_working_with_data_sources/lesson01_reading_csv_files.html": {
        "cards": [
            ("Read custom delimiters",
             "gear",
             "The sep parameter handles files that use tabs, semicolons, or pipes instead of commas between values."),
            ("Load selected columns only",
             "filter",
             "The usecols parameter reads only the columns you name, keeping memory usage low on very wide datasets."),
            ("Fix encoding issues",
             "language",
             "Setting the right encoding option prevents garbled text when loading data files created in another language or region."),
            ("Speed up large file loads",
             "bolt",
             "Specifying dtypes upfront and skipping unused columns cuts the time pandas needs to parse a multi-million-row CSV."),
        ],
        "tip": "This lesson moves beyond simple read_csv calls to handle the complex, inconsistent CSV files that real projects produce.",
    },
    "mod_02_working_with_data_sources/lesson02_working_with_json_files.html": {
        "cards": [
            ("Read a JSON file",
             "code",
             "The read_json function loads a flat JSON file into a pandas DataFrame with a single line of code."),
            ("Normalise nested JSON",
             "diagram-project",
             "The json_normalize function flattens nested JSON objects into separate columns, making them easy to query as a DataFrame."),
            ("Write DataFrame as JSON",
             "upload",
             "The to_json method serialises a DataFrame back to a JSON string or file, with options for the output structure."),
            ("Handle different JSON shapes",
             "sitemap",
             "API responses come as single objects, arrays, or nested structures — pandas provides options to handle each format cleanly."),
        ],
        "tip": "This lesson prepares you to consume API responses, which almost always return data in JSON format.",
    },
    "mod_02_working_with_data_sources/lesson03_connecting_to_databases.html": {
        "cards": [
            ("Build a connection string",
             "plug",
             "A connection string includes the database type, host, port, user, and password needed to open a live connection."),
            ("Connect with SQLAlchemy",
             "link",
             "SQLAlchemy provides a Python object that manages your database connection so pandas can query it directly."),
            ("Load a table into pandas",
             "table",
             "The read_sql_table function retrieves an entire database table and returns it as a fully typed DataFrame."),
            ("Close connections safely",
             "circle-check",
             "Always closing a database connection after querying prevents resource leaks that can crash long-running scripts."),
        ],
        "tip": "This lesson replaces the manual step of exporting data from a database to CSV before loading it in Python.",
    },
    "mod_02_working_with_data_sources/lesson04_running_sql_in_python.html": {
        "cards": [
            ("Run a SQL query",
             "database",
             "The read_sql function executes any SELECT statement against a connected database and loads the result into a DataFrame."),
            ("Pass safe parameters",
             "shield",
             "Parameterised queries pass filter values separately from the SQL text, preventing injection in your scripts."),
            ("Load results as DataFrames",
             "table-cells",
             "Wrapping a query in read_sql delivers the result set directly into a pandas DataFrame, ready for analysis."),
            ("Query multiple tables",
             "sitemap",
             "A single Python script can run separate queries against different tables and combine the results with a merge."),
        ],
        "tip": "This lesson lets you use your existing SQL skills from inside Python, combining query power with pandas analytics.",
    },
    "mod_02_working_with_data_sources/lesson05_writing_data_back_to_a_database.html": {
        "cards": [
            ("Write a DataFrame to a table",
             "upload",
             "The to_sql method pushes a complete DataFrame into a database table, creating the table if it does not exist."),
            ("Choose the write mode",
             "sliders",
             "The if_exists parameter lets you replace an existing table, append new rows to it, or raise an error instead."),
            ("Create tables automatically",
             "table",
             "Pandas infers column names and data types from the DataFrame and creates a matching database schema automatically."),
            ("Fix type mismatches",
             "wrench",
             "Explicitly casting DataFrame columns to the right types before writing prevents errors from mismatched numeric and text fields."),
        ],
        "tip": "This lesson closes the read-transform-write cycle that powers most automated data pipelines in organisations.",
    },
    "mod_02_working_with_data_sources/lesson06_managing_credentials_env.html": {
        "cards": [
            ("Never hard-code passwords",
             "lock",
             "Hard-coding credentials in a Python script exposes them to anyone who reads, copies, or commits your code."),
            ("Use .env files",
             "file-lines",
             "A .env file stores secret values outside your codebase in plain key-value pairs that only your machine reads."),
            ("Load env vars with dotenv",
             "gear",
             "The python-dotenv library reads a .env file at startup and makes each value available as an environment variable."),
            ("Keep secrets out of Git",
             "shield",
             "Adding .env to .gitignore prevents secret credentials from appearing in version control history where others could find them."),
        ],
        "tip": "This lesson protects your team and organisation from the most common cause of accidental credential exposure.",
    },

    # ── Module 03 — Python for Analysts ──────────────────────────────────────
    "mod_03_python_for_analysts/lesson01_why_analysts_use_python.html": {
        "cards": [
            ("What Python adds to analysts",
             "chart-bar",
             "Python automates repetitive tasks, handles millions of rows, and runs the same analysis every time without manual steps."),
            ("Key analytics libraries",
             "cubes",
             "Pandas, NumPy, and Matplotlib form the core analytics toolkit that replaces disconnected spreadsheet formulas with reusable code."),
            ("Python in a workflow",
             "diagram-project",
             "Python sits between raw data sources and final reports, transforming, cleaning, and summarising data along the way."),
            ("When to choose Python",
             "scale-balanced",
             "Python excels when tasks repeat regularly, datasets are large, or every step of an analysis must be auditable."),
        ],
        "tip": "This lesson explains exactly where Python fits in an analyst's toolkit before you start using it in real work.",
    },
    "mod_03_python_for_analysts/lesson02_replacing_excel_workflows_with_python.html": {
        "cards": [
            ("Replicate VLOOKUP with merge",
             "arrows-left-right",
             "Pandas merge performs the same lookup that VLOOKUP does in Excel but handles millions of rows without slowing down."),
            ("Replace pivot tables",
             "table-cells-large",
             "The groupby and agg functions reproduce any pivot table calculation in a reusable, repeatable Python script."),
            ("Generate multi-sheet reports",
             "file-lines",
             "Python can write multiple summary tables to separate Excel sheets in a single script run, replacing a manual process."),
            ("Automate repetitive steps",
             "rotate",
             "A short script replaces copying, pasting, and reformatting across files that previously consumed hours each week."),
        ],
        "tip": "This lesson shows you how to automate the Excel tasks that consume the most time in a typical analyst's week.",
    },
    "mod_03_python_for_analysts/lesson03_using_python_with_sql_queries.html": {
        "cards": [
            ("Run parameterised SQL",
             "database",
             "Parameterised queries let you filter results by date, region, or any value without rewriting the SQL each time."),
            ("Combine SQL with pandas",
             "layer-group",
             "Running a SQL query returns raw results that pandas can then clean, reshape, and enrich with extra calculations."),
            ("Organise query strings",
             "folder",
             "Storing SQL queries as named variables or in separate files keeps your analysis script clean and easy to update."),
            ("Profile slow queries",
             "stopwatch",
             "Timing how long each query takes lets you spot the bottleneck before it affects an automated report's runtime."),
        ],
        "tip": "This lesson lets you combine the SQL skills you already have with Python's data manipulation and automation power.",
    },
    "mod_03_python_for_analysts/lesson04_automating_repetitive_data_tasks.html": {
        "cards": [
            ("Identify automatable tasks",
             "magnifying-glass",
             "Repetitive tasks like downloading, filtering, and exporting the same data every week are ideal candidates for automation."),
            ("Loop over multiple files",
             "rotate",
             "A Python loop processes every file in a folder one by one, applying the same transformation to each."),
            ("Schedule a script to run",
             "clock",
             "Tools like Task Scheduler on Windows or cron on Linux run a Python script automatically at a chosen time."),
            ("Log automated results",
             "list",
             "Writing a timestamped log file after each run gives you an audit trail to verify that automation ran correctly."),
        ],
        "tip": "This lesson turns a daily manual task into a Python script that runs itself without any input from you.",
    },
    "mod_03_python_for_analysts/lesson05_building_a_simple_reporting_script.html": {
        "cards": [
            ("Structure a report script",
             "sitemap",
             "A well-structured reporting script has clear sections for loading data, transforming it, and writing the final output."),
            ("Format numbers and dates",
             "pen",
             "Using format strings and date parsing functions produces clean, consistent values that match business reporting standards."),
            ("Export with multiple sheets",
             "file-lines",
             "The ExcelWriter class writes several DataFrames to separate sheets in one xlsx file, keeping related tables together."),
            ("Add summary statistics",
             "chart-bar",
             "Calculating totals, column averages, and percentage breakdowns at the top of a report gives readers immediate context."),
        ],
        "tip": "This lesson produces a working report script you can adapt immediately for your own team's data needs.",
    },
    "mod_03_python_for_analysts/lesson06_automating_reports_end_to_end.html": {
        "cards": [
            ("Connect all pipeline steps",
             "link",
             "A complete reporting pipeline chains data loading, cleaning, transformation, and file export into a single script execution."),
            ("Handle errors gracefully",
             "shield",
             "Adding try-except blocks prevents a missing file or broken connection from killing the entire pipeline mid-run."),
            ("Send reports by email",
             "envelope",
             "Python's smtplib library can attach a finished report to an email and deliver it automatically after each pipeline run."),
            ("Schedule and log runs",
             "clock",
             "Scheduling a script with a timer and writing a log file creates a fully hands-off automated reporting workflow."),
        ],
        "tip": "This lesson turns a manual reporting process into a fully automated pipeline that runs and delivers itself.",
    },

    # ── Module 04 — Handling Large Data ──────────────────────────────────────
    "mod_04_handling_large_data/lesson02_memory_optimization.html": {
        "cards": [
            ("Why DataFrames use so much RAM",
             "memory",
             "Pandas defaults to 64-bit types for every numeric column, consuming far more memory than the actual values require."),
            ("Inspect memory column by column",
             "magnifying-glass",
             "The memory_usage method shows how many bytes each column consumes so you can target the largest ones first."),
            ("Downcast numeric columns",
             "compress",
             "Converting a float64 column to float32 or an int64 to int16 can cut that column's memory use in half."),
            ("Use categorical columns",
             "tags",
             "Switching string columns to the categorical type stores repeated values once instead of once per row, slashing memory."),
        ],
        "tip": "This lesson teaches you to cut RAM usage so your script can handle datasets that would otherwise crash Python.",
    },
    "mod_04_handling_large_data/lesson03_chunk_processing.html": {
        "cards": [
            ("Why large files crash Python",
             "triangle-exclamation",
             "A file larger than your available RAM causes Python to run out of memory and crash before loading completes."),
            ("Read CSV files in chunks",
             "layer-group",
             "Setting the chunksize parameter in read_csv returns a chunk iterator instead of loading the entire file at once."),
            ("Process each chunk in turn",
             "rotate",
             "Looping over each chunk and applying a transformation processes the full dataset without holding it all in memory."),
            ("Combine chunk results",
             "object-group",
             "Collecting partial results from each chunk and concatenating them at the end produces one clean summary output."),
        ],
        "tip": "This lesson lets you analyse files larger than your available RAM by reading and processing them piece by piece.",
    },
    "mod_04_handling_large_data/lesson04_processing_millions_of_rows.html": {
        "cards": [
            ("Spot slow operations",
             "stopwatch",
             "Python for-loops and row-by-row apply calls become painfully slow on datasets with millions of rows."),
            ("Use vectorised calculations",
             "bolt",
             "Pandas and NumPy operations run across entire columns at once using compiled C code, avoiding slow Python iteration."),
            ("Apply complex column logic",
             "gear",
             "The apply function runs a custom Python function on each column when no built-in vectorised method covers the case."),
            ("Benchmark your code",
             "gauge-high",
             "Timing individual operations with timeit or the time module shows which step is slowing down the full pipeline."),
        ],
        "tip": "This lesson shows you why fast-looking code stalls when row counts jump from thousands to millions.",
    },
    "mod_04_handling_large_data/lesson05_columnar_storage.html": {
        "cards": [
            ("What columnar storage is",
             "bars",
             "Columnar formats store a column's values together on disk instead of writing complete rows from start to finish."),
            ("Row vs. columnar comparison",
             "scale-balanced",
             "Row-based files must scan all columns even for single-column queries, while columnar files read only what is needed."),
            ("How columnar reads less data",
             "compress",
             "An analytics query on a columnar file skips unneeded columns entirely, dramatically cutting the data read from disk."),
            ("Columnar formats in Python",
             "cube",
             "Parquet and ORC are two columnar file formats that Python reads natively through pandas for fast analytical queries."),
        ],
        "tip": "This lesson explains the storage model that powers modern analytics databases and gives Parquet files their speed advantage.",
    },
    "mod_04_handling_large_data/lesson06_parquet_files.html": {
        "cards": [
            ("What Parquet files are",
             "file-lines",
             "Parquet is a columnar binary file format designed for analytics workloads, storing data more efficiently than CSV."),
            ("Write a DataFrame to Parquet",
             "download",
             "The to_parquet method saves a DataFrame to disk in Parquet format, embedding the column types automatically."),
            ("Read and filter efficiently",
             "filter",
             "Reading a Parquet file with selected columns skips the rest entirely on disk, loading only the data you requested."),
            ("Parquet versus CSV size",
             "scale-balanced",
             "Parquet compresses column data far more efficiently than CSV, making the same dataset significantly smaller on disk."),
        ],
        "tip": "This lesson shows you how switching from CSV to Parquet delivers faster reads, smaller files, and reliable schema preservation.",
    },
    "mod_04_handling_large_data/lesson13_performance_profiling.html": {
        "cards": [
            ("Measure operation time",
             "stopwatch",
             "Timing how long each pandas operation runs helps you identify which step in a pipeline is slowing everything down."),
            ("Find the slowest steps",
             "magnifying-glass",
             "Profiling reports how much time each step consumes, pinpointing the exact bottleneck in your data pipeline."),
            ("Use cProfile and line_profiler",
             "code",
             "The cProfile module measures total call time while line_profiler reveals which individual lines inside a function are slow."),
            ("Document and prioritise fixes",
             "list-check",
             "Recording baseline timings before and after each change provides evidence that your optimisation actually improved performance."),
        ],
        "tip": "This lesson teaches you to diagnose performance problems before they affect a production pipeline or frustrate end users.",
    },
}

# ── Regex pattern ─────────────────────────────────────────────────────────────

PATTERN = re.compile(
    r'[ \t]*<section id="objective">.*?</section>',
    re.DOTALL
)

# ── Apply ─────────────────────────────────────────────────────────────────────

ok = 0
fail = 0

for rel_path, data in LESSONS.items():
    abs_path = os.path.join(ROOT, rel_path.replace("/", os.sep))
    if not os.path.exists(abs_path):
        print(f"  ❌ FILE NOT FOUND: {rel_path}")
        fail += 1
        continue

    with open(abs_path, encoding="utf-8") as fh:
        html = fh.read()

    new_section = build_section(data["cards"], data["tip"])
    new_html, count = PATTERN.subn(new_section, html, count=1)

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
