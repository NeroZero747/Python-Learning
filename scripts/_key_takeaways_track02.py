#!/usr/bin/env python3
"""Rewrite #key-ideas section body for all 28 track_02 lessons."""

import re, os, sys

ROOT = r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics"

# ── Fixed section shell (header preserved exactly per spec) ───────────────────
SECTION_OPEN = (
    '<section id="key-ideas">\n'
    '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
    '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
    '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
    '        <span class="iconify text-white text-base" data-icon="fa6-solid:lightbulb"></span>\n'
    '      </span>\n'
    '      <div class="min-w-0">\n'
    '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Takeaways</h2>\n'
    '        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The most important ideas to remember</p>\n'
    '      </div>\n'
    '    </div>\n'
)
SECTION_CLOSE = '  </div>\n</section>'

# ── Card builders ─────────────────────────────────────────────────────────────

def card_pink(icon, title, desc, p1, p2, p3):
    return (
        '<div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">\n'
        '  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>\n'
        '  <div class="px-6 py-5">\n'
        '    <div class="flex items-center gap-3 mb-3">\n'
        f'      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">\n'
        f'        <span class="iconify text-white text-sm" data-icon="fa6-solid:{icon}"></span>\n'
        '      </span>\n'
        f'      <h3 class="text-sm font-bold text-gray-900">{title}</h3>\n'
        '    </div>\n'
        f'    <p class="text-xs text-gray-600 leading-relaxed mb-4">{desc}</p>\n'
        '    <div class="flex flex-wrap gap-2">\n'
        f'      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">{p1}</span>\n'
        f'      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">{p2}</span>\n'
        f'      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">{p3}</span>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>'
    )

def card_violet(icon, title, desc, p1, p2, p3):
    return (
        '<div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">\n'
        '  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>\n'
        '  <div class="px-6 py-5">\n'
        '    <div class="flex items-center gap-3 mb-3">\n'
        f'      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">\n'
        f'        <span class="iconify text-white text-sm" data-icon="fa6-solid:{icon}"></span>\n'
        '      </span>\n'
        f'      <h3 class="text-sm font-bold text-gray-900">{title}</h3>\n'
        '    </div>\n'
        f'    <p class="text-xs text-gray-600 leading-relaxed mb-4">{desc}</p>\n'
        '    <div class="flex flex-wrap gap-2">\n'
        f'      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">{p1}</span>\n'
        f'      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">{p2}</span>\n'
        f'      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">{p3}</span>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>'
    )

def card_blue(icon, title, desc, p1, p2, p3):
    return (
        '<div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">\n'
        '  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>\n'
        '  <div class="px-6 py-5">\n'
        '    <div class="flex items-center gap-3 mb-3">\n'
        f'      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">\n'
        f'        <span class="iconify text-white text-sm" data-icon="fa6-solid:{icon}"></span>\n'
        '      </span>\n'
        f'      <h3 class="text-sm font-bold text-gray-900">{title}</h3>\n'
        '    </div>\n'
        f'    <p class="text-xs text-gray-600 leading-relaxed mb-4">{desc}</p>\n'
        '    <div class="flex flex-wrap gap-2">\n'
        f'      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">{p1}</span>\n'
        f'      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">{p2}</span>\n'
        f'      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">{p3}</span>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>'
    )

def build_section(c1, c2, c3):
    body = (
        '    <div class="bg-white px-8 py-7 space-y-4">\n\n'
        + c1 + '\n\n'
        + c2 + '\n\n'
        + c3 + '\n\n'
        '    </div>\n'
    )
    return SECTION_OPEN + body + SECTION_CLOSE


# ── Lesson data ───────────────────────────────────────────────────────────────
# Each tuple: (icon, title ≤5w, desc 20–30w, pill1, pill2, pill3)

MOD01 = "mod_01_data_analysis_with_pandas"
MOD02 = "mod_02_working_with_data_sources"
MOD03 = "mod_03_python_for_analysts"
MOD04 = "mod_04_handling_large_data"

LESSONS = {

    # ── Module 01 ─────────────────────────────────────────────────────────────

    f"{MOD01}/lesson01_introduction_to_pandas.html": (
        ("robot",         "Pandas Removes Manual Work",
         "Pandas automates the repetitive data-prep steps you would normally do in Excel — filtering, calculating, and reshaping — applied to every row in one instruction.",
         "No clicks", "Runs instantly", "Any file size"),
        ("bolt",          "One Script, Full Workflow",
         "A single Python script can load a file, clean it, calculate new columns, summarise by group, and export the result without switching between any applications.",
         "Load", "Transform", "Export"),
        ("table-list",    "Every Dataset Has the Same Shape",
         "Whether your data has 100 rows or 10 million, pandas uses the same DataFrame object and the same operations, so you only learn one pattern for all sizes.",
         "Scalable", "Consistent", "DataFrame"),
    ),

    f"{MOD01}/lesson02_dataframes_explained.html": (
        ("triangle-exclamation", "Column Types Prevent Silent Errors",
         "Every column in a DataFrame has a fixed type — integer, float, or text — and pandas will raise an error if you try to perform maths on a text column, catching mistakes early.",
         "dtype", "Type safety", "Early errors"),
        ("bookmark",      "Index Is Not a Column",
         "The index is pandas' internal row address and does not appear as a data column in your exports; resetting it with reset_index() turns it into a regular column when you need it.",
         "Index", "reset_index()", "Row address"),
        ("ruler-combined","Shape Confirms the File Loaded",
         "Checking df.shape immediately after loading confirms the number of rows matches your expectation; a wrong row count means the file was truncated or the separator was incorrect.",
         "df.shape", "Row count", "Validation"),
    ),

    f"{MOD01}/lesson03_reading_data_csv_excel.html": (
        ("gear",          "Parameters Prevent Corrupted Loads",
         "Without specifying the separator and encoding, pandas guesses — and a wrong guess silently turns every accented character and currency symbol into a question mark.",
         "sep=", "encoding=", "Silent errors"),
        ("magnifying-glass", "head() Is Your First Quality Check",
         "Running df.head() immediately after loading catches wrong separators, missing column names, and garbled text before any calculation produces a wrong result.",
         "df.head()", "First 5 rows", "Spot errors"),
        ("triangle-exclamation", "Object dtype Means Numbers Loaded as Text",
         "When a numeric column shows dtype: object, pandas cannot sum or average it; you must convert it with pd.to_numeric() before any calculation will produce a correct answer.",
         "dtype: object", "pd.to_numeric()", "Type fix"),
    ),

    f"{MOD01}/lesson04_selecting_columns.html": (
        ("sort",          "Column Order Controls Export Layout",
         "Selecting columns in a specific list order lets you control the left-to-right layout of every CSV or Excel file you export, without reformatting columns by hand afterwards.",
         "Column order", "Export layout", "No manual work"),
        ("arrows-rotate", "Rename Before Joining Tables",
         "Renaming columns to a shared naming convention before a merge prevents join failures caused by capitalisation differences — 'CustomerID' and 'customer_id' are treated as different keys.",
         "rename()", "Key matching", "Merge safety"),
        ("gauge-high",    "Fewer Columns, Faster Calculation",
         "Selecting only the columns you need before filtering or grouping can cut memory use by half or more on wide files, making every subsequent operation noticeably faster.",
         "Memory", "Performance", "usecols"),
    ),

    f"{MOD01}/lesson05_filtering_rows.html": (
        ("copy",          "Filters Return a New DataFrame",
         "A filtered DataFrame is a separate copy — modifying it never changes the original, so you can safely test different filter conditions without losing your source data.",
         "Copy", "Original safe", "No overwrite"),
        ("list-check",    "isin() Replaces Long OR Chains",
         "A single isin() call replaces five or more chained OR conditions and is less likely to break when the list of allowed values changes, because you only update the list in one place.",
         "isin()", "Cleaner code", "Maintainable"),
        ("magnifying-glass", "Check for Nulls Before Filtering",
         "Filtering on a column that contains NaN values can silently drop valid rows; running isnull().sum() first tells you how many nulls exist before you commit to the filter.",
         "isnull()", "Null check", "Data loss"),
    ),

    f"{MOD01}/lesson06_creating_calculated_columns.html": (
        ("bolt",          "All Rows Update Simultaneously",
         "A pandas calculated column is applied to the whole DataFrame by compiled C code in one pass — typically 50 to 100 times faster than a Python for-loop that processes one row at a time.",
         "Vectorised", "C engine", "No for-loop"),
        ("code-branch",   "np.where() Replaces Row-by-Row if/else",
         "Writing np.where(condition, value_if_true, value_if_false) in one line replaces a for-loop with an if/else inside it, which is 100 times faster on large DataFrames.",
         "np.where()", "Conditional", "Performance"),
        ("tag",           "Name Columns Descriptively",
         "Using a name like revenue_per_unit instead of col_1 means every filter, group-by, and export that references that column is self-documenting and readable by anyone who opens the script.",
         "Naming", "Readability", "Self-documenting"),
    ),

    f"{MOD01}/lesson07_aggregations_group_by.html": (
        ("database",      "Group Once, Aggregate Many Times",
         "Assigning the result of groupby() to a variable lets you apply multiple different aggregation functions — sum, mean, count — without re-scanning the full DataFrame each time.",
         "Reuse groups", "Multiple aggs", "Efficiency"),
        ("tag",           "Named agg() Prevents Column Clashes",
         "Passing a dictionary to agg() with explicit output column names — such as {'sales': 'total_sales'} — prevents duplicate column names that break downstream joins and exports.",
         "agg()", "Named output", "No clashes"),
        ("arrow-down-wide-short", "Sort Totals Before Exporting",
         "Chaining sort_values() after a groupby result produces a report where the largest or most recent group appears first, so recipients do not need to sort the data themselves in Excel.",
         "sort_values()", "Report order", "Export-ready"),
    ),

    f"{MOD01}/lesson08_joining_data_merge.html": (
        ("eye",           "Inner Join Silently Drops Rows",
         "The default merge is an inner join, which discards every row whose key value has no match in the other table; always compare row counts before and after to catch unexpected data loss.",
         "Inner join", "Row count", "Silent drops"),
        ("circle-exclamation", "Duplicate Keys Multiply Row Count",
         "If the key column contains duplicate values in both tables, merge() produces a Cartesian product that multiplies rows — a table with 100 rows can become 10,000 unexpectedly.",
         "Duplicates", "Cartesian", "Key check"),
        ("pen",           "Name Suffixes to Avoid Confusion",
         "When both tables share a column name like value, merge() appends _x and _y by default; setting the suffixes parameter to descriptive names makes the result immediately readable.",
         "suffixes=", "Column names", "_x _y"),
    ),

    f"{MOD01}/lesson09_handling_missing_data.html": (
        ("grip-horizontal","dropna() Removes Whole Rows by Default",
         "Without any arguments, dropna() removes every row that contains at least one null value anywhere — even a single missing field in an unrelated column deletes the entire record.",
         "dropna()", "axis=", "Row removal"),
        ("forward",       "Forward-Fill Works for Time Series",
         "ffill() copies the last known value into the gap below it, which is the correct imputation strategy for sensor readings, prices, or any metric where yesterday's value is the best estimate for today.",
         "ffill()", "Time series", "Imputation"),
        ("file-pen",      "Document Every Fill Decision",
         "Recording why you chose mean, zero, or forward-fill in a script comment or log entry creates an audit trail that lets the next analyst understand your data transformation without guesswork.",
         "Audit trail", "Documentation", "Reproducible"),
    ),

    f"{MOD01}/lesson10_exporting_data.html": (
        ("font",          "Encoding Protects Special Characters",
         "Setting encoding='utf-8-sig' when writing a CSV ensures Excel displays accented characters and currency symbols correctly — without it, non-ASCII text appears as garbled symbols.",
         "utf-8-sig", "encoding=", "Special chars"),
        ("sliders",       "ExcelWriter Enables Formatting",
         "Wrapping to_excel() in an ExcelWriter context manager gives access to the openpyxl engine, which lets you set column widths, freeze rows, and apply number formats programmatically.",
         "ExcelWriter", "openpyxl", "Formatting"),
        ("calendar",      "Stamp Exports with Today's Date",
         "Appending the current date to an export filename — report_2026-03-30.xlsx — prevents recipients from accidentally overwriting a previous version and creates an automatic archive trail.",
         "Date stamp", "Versioning", "Archive"),
    ),

    # ── Module 02 ─────────────────────────────────────────────────────────────

    f"{MOD02}/lesson01_reading_csv_files.html": (
        ("forward-step",  "skiprows Handles Non-Standard Headers",
         "Some CSV exports from legacy systems include a title row or blank rows above the real header; passing skiprows=N tells pandas to ignore exactly those lines before it reads column names.",
         "skiprows=", "Legacy files", "Header offset"),
        ("scissors",      "nrows Tests Large Files Cheaply",
         "Passing nrows=1000 to read_csv() loads only the first thousand rows so you can inspect column names, types, and encoding problems before committing to a full multi-gigabyte read.",
         "nrows=", "Quick preview", "Large files"),
        ("calendar",      "parse_dates Converts on Load",
         "Passing parse_dates=['date_col'] inside read_csv() converts date strings to datetime objects automatically, so you can filter by date range immediately without a separate conversion step.",
         "parse_dates=", "datetime", "No conversion"),
    ),

    f"{MOD02}/lesson02_working_with_json_files.html": (
        ("layer-group",   "Nested JSON Must Be Flattened First",
         "A JSON response where each record contains a sub-object — such as address.city — cannot be aggregated until json_normalize() unpacks every nested key into a separate flat column.",
         "json_normalize()", "Nested", "Flat columns"),
        ("crosshairs",    "record_path Selects the Right Array",
         "Most API responses wrap the data records inside a parent key like results or data; passing record_path tells json_normalize() which list to use as the rows of the DataFrame.",
         "record_path=", "API response", "Parent key"),
        ("terminal",      "Inspect the Schema Before Parsing",
         "Printing the keys of the first record from an API response shows you the exact field names and nesting depth before you write any parsing code, preventing mismatched column errors.",
         "Schema first", "keys()", "Field names"),
    ),

    f"{MOD02}/lesson03_connecting_to_databases.html": (
        ("shield-halved", "Use Context Managers to Close Connections",
         "Wrapping the engine in a with block guarantees the connection is closed even if your script crashes mid-run, preventing the database from holding open connection slots indefinitely.",
         "with block", "Auto-close", "Connection pool"),
        ("eye-slash",     "Never Hard-Code Credentials in Scripts",
         "A connection string with a username and password embedded should never be committed to version control; store credentials in a .env file that Git ignores and load them at runtime.",
         ".env file", "No hard-code", "Git safe"),
        ("user-lock",     "Connect with a Read-Only Role",
         "Using a database account that has only SELECT permissions during development prevents accidental writes to production data and is a standard requirement in most enterprise data teams.",
         "Read-only", "SELECT only", "Least privilege"),
    ),

    f"{MOD02}/lesson04_running_sql_in_python.html": (
        ("shield",        "Never Build SQL with f-Strings",
         "Inserting a filter value directly into an f-string SQL query creates a SQL injection vulnerability; always pass filter values through the params argument with a placeholder instead.",
         "SQL injection", "params=", "Parameterised"),
        ("file-code",     "Store Long Queries in .sql Files",
         "Saving a large SELECT statement as a separate .sql file and reading it with open() keeps your Python script clean and lets SQL tools like DBeaver execute the query independently.",
         ".sql files", "Separation", "DBeaver"),
        ("magnifying-glass-minus", "LIMIT Rows During Development",
         "Adding LIMIT 500 to your development query loads just enough rows to test your pandas transformation code without waiting for a full production data pull on every run.",
         "LIMIT", "Dev speed", "Test rows"),
    ),

    f"{MOD02}/lesson05_writing_data_back_to_a_database.html": (
        ("eraser",        "replace Drops the Table First",
         "Using if_exists='replace' drops and recreates the entire table, removing any indexes, grants, or foreign-key constraints on the old table; use 'append' to add rows without touching the schema.",
         "if_exists=", "Schema loss", "Append vs replace"),
        ("layer-group",   "chunksize Prevents Memory Errors",
         "Writing one million rows in a single call builds the entire INSERT statement in memory first; passing chunksize=1000 streams rows in safe batches that fit comfortably in RAM.",
         "chunksize=", "Batch write", "Memory safe"),
        ("check-double",  "Verify Row Counts After Writing",
         "Querying SELECT COUNT(*) from the target table after to_sql() confirms every row arrived; a silent string-truncation error can reduce the count without raising any Python exception.",
         "COUNT(*)", "Verify rows", "Silent errors"),
    ),

    f"{MOD02}/lesson06_managing_credentials_env.html": (
        ("circle-play",   "Load .env Once at Script Startup",
         "Calling load_dotenv() at the very top of your script, before any other import reads environment variables, ensures all credentials are available to every function throughout the run.",
         "load_dotenv()", "Startup", "Top of file"),
        ("life-ring",     "Use os.environ.get() with a Fallback",
         "Calling os.environ.get('DB_HOST', 'localhost') returns a safe default value instead of crashing with a KeyError when a variable is missing from a local developer's machine.",
         "get() fallback", "KeyError", "Local dev"),
        ("rotate",        "Rotate Credentials After Any Exposure",
         "If a password appears in any commit — even a private repository — change it immediately, because automated crawlers index public GitHub history within minutes of a repository becoming visible.",
         "Rotate now", "Credential leak", "Git history"),
    ),

    # ── Module 03 ─────────────────────────────────────────────────────────────

    f"{MOD03}/lesson01_why_analysts_use_python.html": (
        ("arrows-left-right", "Python Replaces Repetitive Clicks",
         "A task that requires twenty manual filter and copy steps in Excel can be written as five lines of Python that run in under a second and produce identical output every time.",
         "20 clicks → 5 lines", "Instant", "Consistent"),
        ("vial",          "Scripts Are Testable — Clicks Are Not",
         "A Python script can be run on a small sample dataset and its output verified before it touches production data; an Excel macro cannot be unit-tested in the same way.",
         "Testable", "Sample data", "Verification"),
        ("plug",          "Python Connects Where Excel Cannot",
         "Python connects directly to live databases, REST APIs, and cloud storage buckets, pulling data into the analysis without any manual downloading, opening, or copy-pasting of files.",
         "Databases", "REST APIs", "Cloud storage"),
    ),

    f"{MOD03}/lesson02_replacing_excel_workflows_with_python.html": (
        ("link-slash",    "pandas merge Never Breaks on New Rows",
         "A pandas merge recalculates automatically every time the script runs, so adding new rows to the source file never causes the #N/A errors that appear when a VLOOKUP formula runs out of range.",
         "No #N/A", "Auto-refresh", "New rows safe"),
        ("layer-group",   "groupby Handles Multiple Keys at Once",
         "A pandas groupby can group on two or more columns simultaneously in a single call, replacing a pivot-table configuration that requires manual row-field and column-field adjustments each month.",
         "Multi-key", "One call", "No clicking"),
        ("folder-open",   "Folder Loops Catch the File You Forget",
         "A script that opens every CSV in a folder automatically processes any new monthly file placed in that folder, including the one you might miss when opening files manually one by one.",
         "All files", "Auto-detect", "No missed files"),
    ),

    f"{MOD03}/lesson03_using_python_with_sql_queries.html": (
        ("wand-magic-sparkles", "Python Does What SQL Cannot",
         "SQL alone cannot call external APIs, apply a statistical model, or format a multi-sheet Excel report; Python handles all of those steps after the SQL result lands in a DataFrame.",
         "APIs", "ML models", "Excel output"),
        ("code",          "Keep SQL and Python Separate",
         "Storing SQL statements in dedicated .sql files or a named dictionary keeps each language in its own layer, making it easier to tune a slow query without touching the pandas transformation code.",
         ".sql files", "Clean layers", "Independent tuning"),
        ("database",      "Profile at the SQL Boundary First",
         "The biggest performance gain in a SQL-plus-pandas pipeline almost always comes from adding a database index or rewriting the WHERE clause, not from optimising the pandas code that follows.",
         "DB index", "WHERE clause", "Real bottleneck"),
    ),

    f"{MOD03}/lesson04_automating_repetitive_data_tasks.html": (
        ("repeat",        "Write Idempotent Scripts",
         "A well-designed automation script produces the same output whether it runs once or ten times; always overwrite output files rather than appending rows, to avoid duplicating data over time.",
         "Idempotent", "Overwrite", "No duplicates"),
        ("bell",          "Alert on Failure, Not Success",
         "Logging a message only when the script fails means you do not need to check a log every day — silence means everything ran correctly, and a notification means action is required.",
         "Failure alerts", "Silent success", "Notifications"),
        ("code-branch",   "Version-Control Automation Scripts",
         "Storing your automation scripts in Git means you can roll back to last week's working version in thirty seconds if a code change breaks a scheduled run before the next run is due.",
         "Git", "Roll back", "30 seconds"),
    ),

    f"{MOD03}/lesson05_building_a_simple_reporting_script.html": (
        ("calendar-days", "Parametrise the Report Date at the Top",
         "Declaring the report date as a single variable on line one means you change one value to re-run the report for any period, rather than searching for date strings scattered throughout the code.",
         "One variable", "Date param", "Reusable"),
        ("shield-check",  "Validate Input Data Before Transforming",
         "Checking that expected columns exist and contain non-null values at the start of the script catches a broken data feed immediately rather than producing a silently wrong output file.",
         "Column check", "Null guard", "Fail fast"),
        ("table-cells",   "Format Numbers in the Export, Not the Script",
         "Applying number formatting through openpyxl at the export stage keeps the DataFrame values as plain floats, making the underlying data easy to reuse in further calculations.",
         "openpyxl", "num_format", "Float-safe"),
    ),

    f"{MOD03}/lesson06_automating_reports_end_to_end.html": (
        ("puzzle-piece",  "Split Each Stage into Its Own Function",
         "Wrapping load, transform, and export in separate functions lets you test each stage independently and restart from a checkpoint when one stage fails without rerunning everything from scratch.",
         "Functions", "Checkpoint", "Independent test"),
        ("file-lines",    "Log the Full Exception, Not Just the Message",
         "Logging str(e) or traceback.format_exc() inside your except block records the exact line number and error type, so the log file tells you precisely where the pipeline broke.",
         "traceback", "str(e)", "Exact line"),
        ("paper-plane",   "Test Email Delivery in a Sandbox First",
         "Sending a test report to your own address before the first scheduled run confirms that attachments, subject lines, and body text all appear correctly in the recipient's email client.",
         "Test email", "Sandbox", "Attachment check"),
    ),

    # ── Module 04 ─────────────────────────────────────────────────────────────

    f"{MOD04}/lesson02_memory_optimization.html": (
        ("stethoscope",   "Check dtypes Immediately After Loading",
         "Running df.dtypes on a freshly loaded DataFrame reveals which columns pandas guessed as float64 when int8 would hold the same values using only one-eighth of the memory.",
         "df.dtypes", "float64", "int8"),
        ("arrow-down-wide-short", "Downcast Integers Before Strings",
         "Converting integer columns to the smallest fitting numeric type reduces memory first, making the memory_usage() report easier to read before you tackle the larger string columns.",
         "int8 / int16", "Order matters", "Step by step"),
        ("circle-exclamation", "Categorical Breaks on New String Values",
         "A categorical column cannot be assigned a new string value that was not present when the column was categorised; convert it back to object dtype first before inserting any unseen category.",
         "New category", "TypeError", "Convert back"),
    ),

    f"{MOD04}/lesson03_chunk_processing.html": (
        ("compress",      "Pre-Aggregate Inside the Loop",
         "Summing or counting inside each chunk and collecting only the small summary rows uses almost no extra memory, compared to gathering every chunk's full rows and concatenating at the end.",
         "Aggregate first", "Low memory", "Summary only"),
        ("list",          "Pass dtype= Consistently Across Chunks",
         "Without a dtype dictionary, pandas infers column types from each chunk separately and may assign int64 to one chunk and float64 to another, causing type conflicts when you concatenate.",
         "dtype= dict", "Consistent types", "No conflicts"),
        ("gauge-high",    "Print Progress Every N Chunks",
         "Printing a short message every ten chunks gives you a live indicator that the script is still running on a large file and lets you estimate the total runtime without adding a progress-bar library.",
         "Progress log", "Estimate time", "No library"),
    ),

    f"{MOD04}/lesson04_processing_millions_of_rows.html": (
        ("font",          "String Methods Are Vectorised Too",
         "The pandas str accessor — df['col'].str.upper() — applies string operations across the entire column in compiled code, replacing a for-loop that called str.upper() on each cell individually.",
         "str accessor", "str.upper()", "No for-loop"),
        ("triangle-exclamation", "apply() Is a Last Resort",
         "apply() runs a Python function row by row at full interpreter overhead; it is useful for complex logic that cannot be vectorised, but is typically 10 to 100 times slower than an equivalent expression.",
         "apply()", "Last resort", "10–100× slower"),
        ("ruler",         "Benchmark with Realistic Data Sizes",
         "A one-thousand-row test file may not expose the performance gap between apply() and a vectorised operation; always profile on a representative sample of the actual production dataset.",
         "Realistic data", "Production size", "Valid benchmark"),
    ),

    f"{MOD04}/lesson05_columnar_storage.html": (
        ("forward-fast",  "Predicate Pushdown Skips Row Groups",
         "A well-optimised Parquet reader skips entire row groups that cannot contain matching values before Python even starts — reducing the bytes read from disk far beyond what pandas alone can achieve.",
         "Predicate pushdown", "Row groups", "Disk skip"),
        ("server",        "ORC Is Native to Hive and Spark",
         "ORC and Parquet are both columnar formats, but ORC is the native format for Apache Hive; if your pipeline ends in Spark or a Hive metastore, ORC queries may run faster than Parquet.",
         "ORC", "Apache Hive", "Spark native"),
        ("pen-to-square", "Columnar Files Are Not Row-Updateable",
         "You cannot update a single cell in a Parquet or ORC file the way you can in a database row; columnar files are write-once and must be fully rewritten to reflect any change to existing data.",
         "Write-once", "No row update", "Full rewrite"),
    ),

    f"{MOD04}/lesson06_parquet_files.html": (
        ("clock-rotate-left", "Parquet Preserves Column Types",
         "Saving a DataFrame with a datetime column to Parquet and reloading it returns a datetime object automatically; the same round-trip via CSV loses the type and forces a manual re-parse every load.",
         "Type preservation", "datetime", "No re-parse"),
        ("box-archive",   "Snappy Is the Safe Default Codec",
         "Parquet supports several compression codecs; snappy offers the best balance of read speed and file size and is supported natively by pandas, Spark, BigQuery, and Athena without any extra configuration.",
         "snappy", "Codec", "Universal support"),
        ("folder-tree",   "Partition by Date for Incremental Loads",
         "Writing Parquet files partitioned by year, month, and day lets read_parquet() skip entire date folders when you filter by a date range, making daily pipeline refreshes dramatically faster.",
         "Partitioning", "Date folders", "Incremental"),
    ),

    f"{MOD04}/lesson13_performance_profiling.html": (
        ("magnifying-glass-chart", "cProfile Finds the Function, Not the Line",
         "cProfile shows which function consumed the most total time, but you still need line_profiler to zoom into that function and find the exact line causing the slowdown inside it.",
         "cProfile", "line_profiler", "Two tools"),
        ("fire",          "Warm Up Before Starting the Timer",
         "The first call to a function is often slower because Python caches imports and compiles internally; always run the code once before starting the timer to get a stable, representative baseline.",
         "Warm-up run", "Cache effect", "Stable baseline"),
        ("split",         "Compare Wall Time and CPU Time Separately",
         "Wall-clock time includes waiting for disk reads and network queries, while CPU time measures only computation; slow wall time with fast CPU time means the bottleneck is I/O, not your code.",
         "Wall time", "CPU time", "I/O bottleneck"),
    ),
}

# ── Regex ─────────────────────────────────────────────────────────────────────

PATTERN = re.compile(r'<section id="key-ideas">.*?</section>', re.DOTALL)

# ── Apply ─────────────────────────────────────────────────────────────────────

ok = fail = 0

for rel_path, (t1, t2, t3) in LESSONS.items():
    abs_path = os.path.join(ROOT, rel_path.replace("/", os.sep))
    if not os.path.exists(abs_path):
        print(f"  ❌ FILE NOT FOUND: {rel_path}")
        fail += 1
        continue

    html = open(abs_path, encoding="utf-8").read()

    c1 = card_pink(*t1)
    c2 = card_violet(*t2)
    c3 = card_blue(*t3)
    new_section = build_section(c1, c2, c3)

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
