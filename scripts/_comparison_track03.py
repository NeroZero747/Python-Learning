#!/usr/bin/env python3
"""Rewrite #comparison section for all 56 track_03 lessons."""

import re, pathlib

ROOT = pathlib.Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_03_data_engineering")
PATTERN = re.compile(r'<section id="comparison">.*?</section>', re.DOTALL)

MOD01 = "mod_01_data_engineering_foundations"
MOD02 = "mod_02_nosql_and_modern_data_storage"
MOD03 = "mod_03_api_data_integration"
MOD04 = "mod_04_data_pipelines_and_orchestration"
MOD05 = "mod_05_large_scale_data_processing"
MOD06 = "mod_06_automation_and_ci_cd"


# ── HTML helpers ──────────────────────────────────────────────────────────────

def he(s):
    """HTML-encode characters that must be escaped inside <code> blocks."""
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace("'", "&#39;"))


TOOL_HEADERS = (
    '<div class="grid grid-cols-3 gap-3">\n'
    '  <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-indigo-600 text-white">\n'
    '    <span class="iconify text-lg" data-icon="fa6-brands:python"></span> Python\n'
    '  </div>\n'
    '  <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-orange-600 text-white">\n'
    '    <span class="iconify text-lg" data-icon="fa6-solid:database"></span> SQL\n'
    '  </div>\n'
    '  <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-emerald-600 text-white">\n'
    '    <span class="iconify text-lg" data-icon="fa6-solid:table"></span> Excel\n'
    '  </div>\n'
    '</div>'
)


def row_html(label, icon, py_term, py_desc, sql_term, sql_desc, xl_term, xl_desc):
    return (
        '<div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">\n'
        f'  <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">\n'
        f'    <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">\n'
        f'      <span class="iconify text-indigo-400 text-[11px]" data-icon="{icon}"></span>\n'
        f'    </span>\n'
        f'    <span class="text-xs font-bold uppercase tracking-widest text-gray-400">{label}</span>\n'
        f'  </div>\n'
        f'  <div class="grid grid-cols-3 divide-x divide-gray-100">\n'
        f'    <div class="px-4 py-4 flex flex-col gap-2">\n'
        f'      <span class="text-xs text-gray-400">Python</span>\n'
        f'      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">{py_term}</code>\n'
        f'      <p class="text-xs text-gray-500 leading-relaxed">{py_desc}</p>\n'
        f'    </div>\n'
        f'    <div class="px-4 py-4 flex flex-col gap-2">\n'
        f'      <span class="text-xs text-gray-400">SQL</span>\n'
        f'      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">{sql_term}</code>\n'
        f'      <p class="text-xs text-gray-500 leading-relaxed">{sql_desc}</p>\n'
        f'    </div>\n'
        f'    <div class="px-4 py-4 flex flex-col gap-2">\n'
        f'      <span class="text-xs text-gray-400">Excel</span>\n'
        f'      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">{xl_term}</code>\n'
        f'      <p class="text-xs text-gray-500 leading-relaxed">{xl_desc}</p>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'</div>'
    )


def code_grid(divider_label, py_code, sql_code, xl_code, caption):
    return (
        '<div>\n'
        '  <div class="flex items-center gap-3 mb-4">\n'
        '    <span class="flex-1 h-px bg-gray-100"></span>\n'
        '    <div class="flex items-center gap-2 shrink-0">\n'
        '      <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">\n'
        '        <span class="iconify text-brand text-sm" data-icon="fa6-solid:code-compare"></span>\n'
        '      </span>\n'
        f'      <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D]">{divider_label}</p>\n'
        '    </div>\n'
        '    <span class="flex-1 h-px bg-gray-100"></span>\n'
        '  </div>\n'
        '  <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 items-stretch">\n'
        '    <div class="flex flex-col">\n'
        '      <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Python code</p>\n'
        '      <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">\n'
        '        <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">\n'
        '          <div class="flex items-center gap-2">\n'
        '            <span class="iconify" data-icon="logos:python" data-width="16" data-height="16"></span>\n'
        '            <span class="text-xs font-semibold text-gray-400">Python</span>\n'
        '          </div>\n'
        '          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
        '        </div>\n'
        f'        <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-python">{he(py_code)}</code></pre>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="flex flex-col">\n'
        '      <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">SQL query</p>\n'
        '      <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">\n'
        '        <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">\n'
        '          <div class="flex items-center gap-2">\n'
        '            <span class="iconify text-orange-400" data-icon="fa6-solid:database"></span>\n'
        '            <span class="text-xs font-semibold text-gray-400">SQL</span>\n'
        '          </div>\n'
        '          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
        '        </div>\n'
        f'        <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-sql">{he(sql_code)}</code></pre>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="flex flex-col">\n'
        '      <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Excel formula</p>\n'
        '      <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">\n'
        '        <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">\n'
        '          <div class="flex items-center gap-2">\n'
        '            <span class="iconify text-green-400" data-icon="fa6-solid:table"></span>\n'
        '            <span class="text-xs font-semibold text-gray-400">Excel</span>\n'
        '          </div>\n'
        '          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
        '        </div>\n'
        f'        <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-text">{he(xl_code)}</code></pre>\n'
        '      </div>\n'
        '    </div>\n'
        '  </div>\n'
        f'  <p class="text-xs text-gray-400 mt-2">{caption}</p>\n'
        '</div>'
    )


def tip_html(tip_text):
    return (
        '<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        '  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        f'  <p class="text-sm text-gray-600">{tip_text}</p>\n'
        '</div>'
    )


def build_section(intro, rows, divider_label, py_code, sql_code, xl_code, caption, tip):
    row_blocks = "\n".join(row_html(*r) for r in rows)
    return (
        '<section id="comparison">\n'
        '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
        '        <span class="iconify text-white text-base" data-icon="fa6-solid:table-columns"></span>\n'
        '      </span>\n'
        '      <div class="min-w-0">\n'
        '        <h2 class="text-xl font-bold text-gray-900 leading-tight">SQL / Excel Comparison</h2>\n'
        '        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How this topic compares across Python, SQL, and Excel</p>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="bg-white px-8 py-7 space-y-5">\n'
        f'      <p class="text-sm text-gray-600 leading-relaxed">{intro}</p>\n'
        f'      {TOOL_HEADERS}\n'
        f'      {row_blocks}\n'
        f'      {code_grid(divider_label, py_code, sql_code, xl_code, caption)}\n'
        f'      {tip_html(tip)}\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )


# ── Lesson data ───────────────────────────────────────────────────────────────
# Each value: (intro, rows, divider_label, py_code, sql_code, xl_code, caption, tip)

LESSONS = {

    # ── MOD 01 — Data Engineering Foundations ─────────────────────────────────

    f"{MOD01}/lesson01_what_is_data_engineering.html": (
        "If you already write SQL queries or build reports in Excel, you already move data from one place to another. Data engineering formalises that workflow into repeatable, automated pipelines.",
        [
            ("move data between systems", "fa6-solid:right-left",
             "ETL script", "A Python script that extracts data from a source, transforms it, and loads it into a target.",
             "INSERT INTO … SELECT", "A SQL statement that copies rows from one table into another.",
             "copy-paste between sheets", "Manually copying rows from one workbook tab into another."),
            ("schedule a job", "fa6-solid:clock",
             "cron / scheduler", "A system timer that runs your Python script automatically at set intervals.",
             "SQL Agent job", "A database scheduler that executes a stored procedure on a timetable.",
             "refresh on open", "An Excel option that re-queries its data source each time you open the file."),
            ("validate data quality", "fa6-solid:shield-halved",
             "assert / raise", "Python checks that raise an error when data does not meet your rules.",
             "CHECK constraint", "A column rule in SQL that rejects rows failing a condition.",
             "Data Validation", "An Excel feature that restricts what a user can type into a cell."),
        ],
        "Same row count check, three tools",
        "row_count = len(df)\nassert row_count > 0, 'Empty!'",
        "SELECT COUNT(*) AS cnt\nFROM orders\nHAVING COUNT(*) > 0;",
        "=IF(COUNTA(A:A)>1,\"OK\",\"Empty!\")",
        "All three confirm the dataset is not empty before continuing \u2014 the same result, just written in a different tool.",
        "Data engineering automates what you already do by hand in SQL and Excel. The concepts are identical \u2014 only the tooling changes."
    ),

    f"{MOD01}/lesson02_etl_vs_elt.html": (
        "If you already transform data in SQL views or clean columns in Excel before analysis, you already practise ETL or ELT. Python lets you choose where the transformation happens.",
        [
            ("extract", "fa6-solid:file-arrow-down",
             "pd.read_csv()", "Python reads a file or API and pulls the raw data into memory.",
             "SELECT * FROM source", "SQL pulls every row from the source table.",
             "Data \u2192 Get Data", "Excel imports raw data from an external file or connection."),
            ("transform before loading", "fa6-solid:wand-magic-sparkles",
             "df.rename() / df.dropna()", "Python cleans and reshapes data in memory before writing it out.",
             "CASE WHEN / COALESCE", "SQL transforms values inside a query before inserting into a target.",
             "find-and-replace / formulas", "Excel cleans values in a helper column before copying results."),
            ("transform after loading", "fa6-solid:database",
             "SQL in warehouse", "Python loads raw data first, then a SQL script transforms it inside the database.",
             "CREATE VIEW AS SELECT", "SQL builds a view that transforms raw data already sitting in the warehouse.",
             "Power Query refresh", "Excel loads raw data, then a Power Query step reshapes it in place."),
        ],
        "Same cleanup, three tools",
        "df['status'] = df['status'].str.upper()\ndf.to_csv('clean.csv', index=False)",
        "UPDATE orders\nSET status = UPPER(status);",
        "=UPPER(A2)\n-- then paste values",
        "All three standardise the status column to uppercase \u2014 the same result, just written in a different tool.",
        "ETL and ELT describe when you transform. SQL users do it in views, Excel users in Power Query, Python users in scripts. The logic is the same."
    ),

    f"{MOD01}/lesson03_handling_large_datasets.html": (
        "If you already filter large tables in SQL or struggle with slow Excel files, you already know that big data needs special handling. Python gives you chunking and streaming to process files that do not fit in memory.",
        [
            ("process in batches", "fa6-solid:layer-group",
             "chunksize=", "A pandas parameter that reads a large file in small batches instead of all at once.",
             "LIMIT … OFFSET", "SQL fetches a page of rows at a time from a large table.",
             "filter then copy", "Excel filters a large sheet and copies a subset to process separately."),
            ("reduce memory", "fa6-solid:minimize",
             "dtype / category", "Python uses smaller data types or category codes to shrink memory usage.",
             "index / partition", "SQL organises large tables so queries scan only the rows they need.",
             "remove unused columns", "Excel deletes columns you do not need so the file loads faster."),
            ("stream results", "fa6-solid:forward",
             "generator / iterator", "Python yields one chunk at a time instead of holding everything in memory.",
             "cursor.fetchmany()", "SQL fetches a block of rows through a cursor instead of the full result set.",
             "Power Query pagination", "Excel\u2019s Power Query loads data in pages when the source supports it."),
        ],
        "Same large-file read, three tools",
        "for chunk in pd.read_csv('big.csv',\n                         chunksize=10000):\n    process(chunk)",
        "SELECT *\nFROM big_table\nLIMIT 10000 OFFSET 0;",
        "Data -> Get Data -> From CSV\n-> Load first 10,000 rows",
        "All three read the first 10,000 rows from a large dataset \u2014 the same result, just written in a different tool.",
        "SQL pages through rows, Excel filters them, Python chunks them. Different verbs, same idea: process big data in pieces."
    ),

    f"{MOD01}/lesson05_parquet_efficient_storage.html": (
        "If you already save query results to CSV in SQL or export spreadsheets in Excel, you understand file formats. Parquet is a faster, smaller alternative that Python reads and writes natively.",
        [
            ("store data in a file", "fa6-solid:file-lines",
             "df.to_parquet()", "Python writes a DataFrame to a compressed columnar file in one line.",
             "COPY TO … FORMAT PARQUET", "SQL exports query results to a Parquet file on the server.",
             "Save As CSV", "Excel saves the current worksheet as a comma-separated values file."),
            ("read only some columns", "fa6-solid:table-columns",
             "columns=[...]", "Python reads only the columns you name, skipping the rest of the file.",
             "SELECT col1, col2", "SQL returns just the columns listed in the SELECT clause.",
             "hide / delete columns", "Excel hides or removes columns you do not need before analysis."),
            ("compress data", "fa6-solid:compress",
             "compression='snappy'", "Python applies Snappy compression when writing a Parquet file.",
             "GZIP / ZSTD options", "SQL databases compress stored data using algorithms like GZIP or ZSTD.",
             "ZIP the file", "Excel users zip a large CSV to reduce its file size for sharing."),
        ],
        "Same data export, three tools",
        "df.to_parquet('sales.parquet',\n              compression='snappy')",
        "COPY (SELECT * FROM sales)\nTO 'sales.parquet'\n(FORMAT PARQUET);",
        "File -> Save As -> sales.csv\n-> then ZIP to compress",
        "All three export the sales table to a file \u2014 the same result, just written in a different tool.",
        "Parquet replaces CSV for analytics workloads. Your SQL and Excel file-export skills transfer directly \u2014 only the format name changes."
    ),

    f"{MOD01}/lesson06_intro_to_polars_optional.html": (
        "If you already filter rows and group data in SQL or use formulas in Excel, Polars does the same things with a syntax that feels familiar. It runs faster than pandas on large tables.",
        [
            ("filter rows", "fa6-solid:filter",
             "pl.filter()", "Polars keeps only the rows that match a condition you define.",
             "WHERE clause", "SQL keeps only the rows that satisfy the WHERE condition.",
             "AutoFilter", "Excel hides rows that do not match the criteria you select in the filter dropdown."),
            ("group and aggregate", "fa6-solid:object-group",
             "pl.group_by().agg()", "Polars groups rows by a column and calculates a summary per group.",
             "GROUP BY … SUM()", "SQL groups rows and applies an aggregate function to each group.",
             "PivotTable SUM", "Excel groups rows in a PivotTable and sums the values per group."),
            ("select columns", "fa6-solid:grip-vertical",
             "pl.select()", "Polars returns only the columns you list in the select call.",
             "SELECT col1, col2", "SQL returns only the columns named in the SELECT clause.",
             "select column range", "Excel highlights and copies only the columns you need."),
            ("sort rows", "fa6-solid:arrow-down-a-z",
             "pl.sort()", "Polars reorders rows by one or more columns, ascending or descending.",
             "ORDER BY", "SQL sorts the result set by the column you specify.",
             "Sort A\u2192Z", "Excel sorts the selected range alphabetically or numerically."),
        ],
        "Same sales total by region, three tools",
        "import polars as pl\nresult = (\n  df.group_by('region')\n    .agg(pl.col('amount').sum())\n)",
        "SELECT region,\n       SUM(amount) AS total\nFROM sales\nGROUP BY region;",
        "PivotTable: Rows=Region,\nValues=SUM of Amount",
        "All three group sales by region and sum the amounts \u2014 the same result, just written in a different tool.",
        "Polars uses the same filter-group-sort pattern as SQL and Excel. If you can write a GROUP BY, you can write a Polars query."
    ),

    f"{MOD01}/lesson07_pipeline_design_concepts.html": (
        "If you already chain SQL views together or link Excel formulas across sheets, you already design simple pipelines. Python formalises those chains into stages you can test and rerun independently.",
        [
            ("chain steps together", "fa6-solid:link",
             "function calls", "Python calls one function after another, passing results down the chain.",
             "nested views", "SQL creates a view that reads from another view, forming a chain of transformations.",
             "linked formulas", "Excel formulas reference cells that contain other formulas, creating a calculation chain."),
            ("handle a failure", "fa6-solid:triangle-exclamation",
             "try / except", "Python catches errors in one stage so the rest of the pipeline can still report or recover.",
             "TRY_CAST / ISNULL", "SQL uses safe-cast functions to handle invalid data without stopping the query.",
             "IFERROR()", "Excel wraps a formula in IFERROR so a failed calculation shows a fallback value."),
            ("log progress", "fa6-solid:scroll",
             "logging module", "Python writes timestamped messages to a log file at each pipeline stage.",
             "audit table", "SQL inserts a row into an audit table each time a job runs successfully.",
             "change log sheet", "Excel users record run dates and outcomes on a dedicated log worksheet."),
        ],
        "Same three-stage pipeline, three tools",
        "raw = extract('source.csv')\nclean = transform(raw)\nload(clean, 'warehouse.db')",
        "-- view chain\nCREATE VIEW v_clean AS\n  SELECT … FROM raw_table;\nINSERT INTO warehouse\n  SELECT * FROM v_clean;",
        "Sheet1: raw import\nSheet2: =CLEAN(Sheet1!A2)\nSheet3: paste-values final",
        "All three move data through extract, transform, and load stages \u2014 the same result, just written in a different tool.",
        "Pipelines are just chained steps. SQL chains views, Excel chains sheets, Python chains functions. The pattern is the same everywhere."
    ),

    # ── MOD 02 — NoSQL and Modern Data Storage ───────────────────────────────

    f"{MOD02}/lesson01_what_is_nosql.html": (
        "If you already store data in SQL tables or Excel worksheets, you work with structured rows and columns. NoSQL databases store data differently \u2014 as documents, key-value pairs, or graphs \u2014 to handle use cases where rigid tables do not fit.",
        [
            ("store a record", "fa6-solid:box-archive",
             "dict / JSON document", "Python stores a record as a dictionary or JSON object with flexible fields.",
             "INSERT INTO … VALUES", "SQL inserts a row with fixed columns into a relational table.",
             "one row per record", "Excel stores each record as a row with predefined column headers."),
            ("flexible structure", "fa6-solid:shapes",
             "nested dicts", "Python allows each record to have different keys and nested sub-objects.",
             "ALTER TABLE ADD COLUMN", "SQL requires a schema change before a table can hold a new field.",
             "add a new column", "Excel adds a new column header, but existing rows show blanks until filled."),
            ("query data", "fa6-solid:magnifying-glass",
             "collection.find()", "Python queries a NoSQL collection using filter dictionaries.",
             "SELECT … WHERE", "SQL filters rows using a WHERE clause on fixed columns.",
             "VLOOKUP / FILTER", "Excel looks up values using VLOOKUP or the FILTER function."),
        ],
        "Same user record, three tools",
        "user = {\n  'name': 'Alice',\n  'role': 'analyst',\n  'skills': ['SQL', 'Python']\n}",
        "INSERT INTO users\n  (name, role)\nVALUES\n  ('Alice', 'analyst');",
        "A1: Alice  B1: analyst\nC1: SQL, Python",
        "All three store the same user record \u2014 the same result, just written in a different tool.",
        "NoSQL stores flexible records, SQL stores fixed rows, Excel stores flat cells. The same data, different shapes."
    ),

    f"{MOD02}/lesson02_types_of_nosql_databases.html": (
        "If you already choose between SQL tables for different jobs, or separate Excel workbooks by purpose, you understand that different data shapes need different tools. NoSQL gives you four main database types for four different patterns.",
        [
            ("store a document", "fa6-solid:file-lines",
             "MongoDB / dict", "Python sends a JSON-like document to a document database for storage.",
             "row in a table", "SQL stores the same data as a row with fixed columns.",
             "one sheet row", "Excel stores the record as a row in a worksheet."),
            ("cache a value by key", "fa6-solid:key",
             "Redis / dict lookup", "Python stores and retrieves a value using a simple key string.",
             "SELECT … WHERE id =", "SQL looks up a single row by its primary key.",
             "VLOOKUP by ID", "Excel finds a value by matching an ID in the first column."),
            ("store wide columns", "fa6-solid:grip-lines-vertical",
             "Cassandra / wide rows", "Python writes rows where each can have a different set of columns.",
             "sparse table", "SQL uses a table with many nullable columns to simulate variable fields.",
             "merged cells / sparse rows", "Excel leaves cells blank where a column does not apply to that row."),
            ("store relationships", "fa6-solid:diagram-project",
             "Neo4j / nodes + edges", "Python creates nodes and edges in a graph database to model connections.",
             "JOIN across tables", "SQL joins multiple tables on foreign keys to follow relationships.",
             "VLOOKUP across sheets", "Excel uses VLOOKUP or INDEX-MATCH across worksheets to link related data."),
        ],
        "Same key-value lookup, three tools",
        "import redis\nr = redis.Redis()\nr.set('user:1', 'Alice')\nprint(r.get('user:1'))",
        "SELECT name\nFROM users\nWHERE id = 1;",
        "=VLOOKUP(1, A:B, 2, FALSE)",
        "All three retrieve a user name by their ID \u2014 the same result, just written in a different tool.",
        "Document, key-value, columnar, and graph are just storage shapes. SQL and Excel do similar things with tables and lookups \u2014 NoSQL optimises for specific access patterns."
    ),

    f"{MOD02}/lesson03_document_databases_mongodb.html": (
        "If you already insert rows into SQL tables or add records in Excel, MongoDB works the same way \u2014 except each record is a flexible JSON document instead of a fixed row.",
        [
            ("insert a record", "fa6-solid:plus",
             "insert_one()", "Python inserts a single JSON document into a MongoDB collection.",
             "INSERT INTO", "SQL inserts a row with fixed columns into a table.",
             "type a new row", "Excel adds a new row by typing values into the next empty cells."),
            ("find records", "fa6-solid:magnifying-glass",
             "find({filter})", "Python queries a collection by passing a dictionary of conditions.",
             "SELECT … WHERE", "SQL filters rows using a WHERE clause with column conditions.",
             "FILTER() / AutoFilter", "Excel filters visible rows using the FILTER function or dropdown arrows."),
            ("update a record", "fa6-solid:pen-to-square",
             "update_one()", "Python modifies one document that matches a filter condition.",
             "UPDATE … SET … WHERE", "SQL changes column values in rows that match a WHERE clause.",
             "edit a cell", "Excel overwrites a cell value to update a record."),
            ("nest related data", "fa6-solid:sitemap",
             "embedded document", "Python nests a sub-dictionary inside a parent document.",
             "foreign key + JOIN", "SQL stores related data in a separate table and joins on a key.",
             "separate sheet + VLOOKUP", "Excel puts related data on another sheet and links it with VLOOKUP."),
        ],
        "Same order insert, three tools",
        "db.orders.insert_one({\n  'customer': 'Alice',\n  'total': 85.50\n})",
        "INSERT INTO orders\n  (customer, total)\nVALUES\n  ('Alice', 85.50);",
        "A2: Alice  B2: 85.50\n(type into next row)",
        "All three add the same order record \u2014 the same result, just written in a different tool.",
        "MongoDB documents replace SQL rows and Excel rows. The insert-find-update pattern is the same across all three."
    ),

    f"{MOD02}/lesson04_key_value_databases_redis.html": (
        "If you already look up values by a primary key in SQL or use VLOOKUP in Excel, Redis does the same thing \u2014 it stores a value under a key and retrieves it instantly.",
        [
            ("store a value", "fa6-solid:box-archive",
             "r.set(key, value)", "Python stores a string value under a named key in Redis.",
             "INSERT INTO … VALUES", "SQL inserts a value into a row identified by a primary key.",
             "type into a cell", "Excel types a value into a cell addressed by its row and column."),
            ("retrieve a value", "fa6-solid:magnifying-glass",
             "r.get(key)", "Python fetches the value stored under a specific key.",
             "SELECT … WHERE id =", "SQL retrieves a row by matching its primary key in the WHERE clause.",
             "VLOOKUP(key, …)", "Excel looks up a value by finding the key in the first column."),
            ("set an expiry", "fa6-solid:hourglass-half",
             "r.setex(key, ttl, val)", "Python stores a value that automatically deletes itself after a set number of seconds.",
             "event / scheduled job", "SQL uses a scheduled job to delete old rows after a time period.",
             "conditional formatting", "Excel highlights or hides rows past a date, but does not auto-delete them."),
        ],
        "Same session token lookup, three tools",
        "import redis\nr = redis.Redis()\nr.setex('sess:42', 3600, 'token_abc')\nprint(r.get('sess:42'))",
        "SELECT token\nFROM sessions\nWHERE id = 42\n  AND expires > NOW();",
        "=VLOOKUP(42, Sessions!A:B,\n         2, FALSE)",
        "All three retrieve a session token by its ID \u2014 the same result, just written in a different tool.",
        "Redis is a key-value lookup, just like a SQL primary-key query or an Excel VLOOKUP. The speed difference is the reason you pick one over the other."
    ),

    f"{MOD02}/lesson05_column_family_databases_cassandra.html": (
        "If you already query wide tables in SQL or manage spreadsheets with many optional columns, Cassandra solves the same problem \u2014 it stores wide rows where each row can have different columns.",
        [
            ("define a schema", "fa6-solid:table-cells-large",
             "CREATE TABLE (CQL)", "Python sends a CQL statement that defines a table with a partition key and clustering columns.",
             "CREATE TABLE (SQL)", "SQL defines a table with fixed columns, a primary key, and data types.",
             "set up column headers", "Excel types column headers in the first row before entering data."),
            ("write a row", "fa6-solid:pen",
             "session.execute(INSERT)", "Python inserts a row into a Cassandra table using a CQL INSERT statement.",
             "INSERT INTO … VALUES", "SQL inserts a row into a relational table.",
             "type a new row", "Excel types values into the next empty row."),
            ("query by partition", "fa6-solid:magnifying-glass",
             "WHERE partition_key =", "Python queries Cassandra by the partition key to read all rows in that partition.",
             "WHERE indexed_col =", "SQL filters rows using an indexed column in the WHERE clause.",
             "AutoFilter on key col", "Excel filters the sheet to show only rows matching a value in the key column."),
        ],
        "Same sensor reading query, three tools",
        "rows = session.execute(\n  'SELECT * FROM readings '\n  'WHERE sensor_id = %s',\n  ['sensor_42']\n)",
        "SELECT *\nFROM readings\nWHERE sensor_id\n  = 'sensor_42';",
        "AutoFilter: Column A\n= \"sensor_42\"",
        "All three retrieve readings for one sensor \u2014 the same result, just written in a different tool.",
        "Cassandra\u2019s CQL looks like SQL on purpose. If you can write a WHERE clause, you can query Cassandra."
    ),

    f"{MOD02}/lesson06_graph_databases_neo4j.html": (
        "If you already join tables in SQL or use VLOOKUP across sheets in Excel to connect related records, a graph database models those relationships directly as edges between nodes.",
        [
            ("store an entity", "fa6-solid:circle",
             "CREATE (n:Label)", "Python creates a node in Neo4j with a label and properties.",
             "INSERT INTO table", "SQL inserts a row into an entity table.",
             "add a row", "Excel adds a record as a new row in a worksheet."),
            ("link two entities", "fa6-solid:link",
             "CREATE (a)-[:REL]->(b)", "Python creates a named relationship edge between two nodes.",
             "foreign key / JOIN", "SQL links rows across tables using foreign keys and JOIN clauses.",
             "VLOOKUP across sheets", "Excel references a related record on another sheet using VLOOKUP."),
            ("traverse connections", "fa6-solid:route",
             "MATCH path", "Python traverses multi-hop paths between nodes using Cypher\u2019s MATCH clause.",
             "recursive CTE", "SQL follows relationships across tables using a recursive common table expression.",
             "manual cross-reference", "Excel users manually follow lookup chains across multiple sheets."),
        ],
        "Same friend-of-a-friend query, three tools",
        "result = session.run(\n  'MATCH (a)-[:KNOWS]->(b)'\n  '-[:KNOWS]->(c) '\n  'WHERE a.name = \"Alice\" '\n  'RETURN c.name'\n)",
        "WITH RECURSIVE friends AS (\n  SELECT friend_id FROM knows\n  WHERE user_id = 1\n  UNION ALL\n  SELECT k.friend_id\n  FROM knows k\n  JOIN friends f\n    ON k.user_id = f.friend_id\n) SELECT * FROM friends;",
        "=VLOOKUP(\n  VLOOKUP(\"Alice\",\n    Friends!A:B,2,FALSE),\n  Friends!A:B,2,FALSE)",
        "All three find friends-of-friends starting from Alice \u2014 the same result, just written in a different tool.",
        "Graphs make relationship queries natural. SQL uses JOINs, Excel uses nested lookups, Neo4j uses arrows. Same idea, different syntax."
    ),

    f"{MOD02}/lesson07_sql_vs_nosql_choosing_the_right_database.html": (
        "If you already pick between SQL Server and Excel depending on the job, you understand choosing the right tool. Deciding between SQL and NoSQL follows the same logic \u2014 match the database to the data shape.",
        [
            ("structured data", "fa6-solid:table",
             "SQL / pandas DataFrame", "Python uses relational databases or DataFrames when every record has the same columns.",
             "relational table", "SQL stores structured data in tables with fixed schemas.",
             "well-defined worksheet", "Excel handles structured data when every row has the same column headers."),
            ("flexible data", "fa6-solid:shapes",
             "MongoDB / dict", "Python uses a document database when records have different fields.",
             "JSON column / EAV", "SQL stores semi-structured data in a JSON column or entity-attribute-value table.",
             "free-form notes column", "Excel puts variable data in a single text column, losing structure."),
            ("high-speed lookups", "fa6-solid:bolt",
             "Redis / dict cache", "Python uses a key-value store for sub-millisecond lookups.",
             "indexed SELECT", "SQL creates an index for fast lookups, but still slower than an in-memory cache.",
             "VLOOKUP on sorted range", "Excel VLOOKUP on a sorted range is fast, but limited to local file size."),
            ("relationship-heavy queries", "fa6-solid:diagram-project",
             "Neo4j / networkx", "Python uses a graph database or library when queries follow chains of relationships.",
             "multiple JOINs", "SQL joins several tables, but performance degrades as the chain grows.",
             "nested VLOOKUP", "Excel nests VLOOKUP calls, but the formula becomes unreadable quickly."),
        ],
        "Same data, different storage choice",
        "# Structured \u2192 SQL\ndf.to_sql('orders', engine)\n# Flexible \u2192 MongoDB\ndb.logs.insert_one(log_doc)",
        "-- Structured\nINSERT INTO orders …\n-- Flexible\n-- use a JSON column\nINSERT INTO logs(data)\nVALUES ('{\"event\":\"click\"}');",
        "Structured: Orders worksheet\nFlexible: paste JSON\n  into a single cell",
        "All three store the same data, but pick the storage shape that fits \u2014 the same result, different trade-offs.",
        "There is no single best database. SQL is best for structured data, NoSQL for flexible or high-speed patterns. Your SQL skills help you evaluate both."
    ),

    # ── MOD 03 — API Data Integration ─────────────────────────────────────────

    f"{MOD03}/lesson01_what_is_an_api.html": (
        "If you already call SQL stored procedures or use Excel\u2019s Get Data feature, you already request data from another system. An API works the same way \u2014 you send a request and receive data back.",
        [
            ("request data", "fa6-solid:paper-plane",
             "requests.get(url)", "Python sends an HTTP request to a URL and receives data back.",
             "EXEC get_report", "SQL calls a stored procedure that returns a result set.",
             "Data \u2192 Get Data", "Excel\u2019s Get Data wizard fetches data from an external source."),
            ("receive structured data", "fa6-solid:code",
             "response.json()", "Python parses the API\u2019s JSON response into a dictionary.",
             "result set", "SQL returns rows and columns from a stored procedure or query.",
             "imported table", "Excel loads the external data into a worksheet as rows and columns."),
            ("pass parameters", "fa6-solid:sliders",
             "params={'key': 'val'}", "Python sends query parameters that filter or customise the API response.",
             "EXEC proc @param=val", "SQL passes parameter values to a stored procedure.",
             "connection parameters", "Excel sets filter parameters inside the Get Data connection dialog."),
        ],
        "Same weather data request, three tools",
        "import requests\nresp = requests.get(\n  'https://api.weather.io/today',\n  params={'city': 'London'}\n)",
        "EXEC get_weather\n  @city = 'London';",
        "Data -> From Web ->\nhttps://api.weather.io/\n  today?city=London",
        "All three fetch today\u2019s weather for London from an external source \u2014 the same result, just written in a different tool.",
        "An API is just a remote function call. SQL calls stored procedures, Excel calls data connections, Python calls URLs. Same pattern."
    ),

    f"{MOD03}/lesson02_understanding_http_requests.html": (
        "If you already use SELECT to read data and INSERT to write data in SQL, HTTP methods map to the same actions. GET reads, POST writes, PUT updates, DELETE removes.",
        [
            ("read data", "fa6-solid:book-open",
             "GET request", "Python sends a GET request to read data from a server without changing anything.",
             "SELECT", "SQL reads rows from a table without modifying them.",
             "open a file", "Excel opens a workbook to read its contents."),
            ("create data", "fa6-solid:plus",
             "POST request", "Python sends a POST request with a body to create a new record on the server.",
             "INSERT INTO", "SQL adds a new row to a table.",
             "add a row", "Excel types a new record into the next empty row."),
            ("update data", "fa6-solid:pen-to-square",
             "PUT / PATCH request", "Python sends a PUT or PATCH request to update an existing record on the server.",
             "UPDATE … SET", "SQL modifies existing column values in rows that match a condition.",
             "edit a cell", "Excel overwrites a cell to change an existing value."),
            ("delete data", "fa6-solid:trash-can",
             "DELETE request", "Python sends a DELETE request to remove a record from the server.",
             "DELETE FROM … WHERE", "SQL removes rows that match a condition.",
             "delete a row", "Excel right-clicks a row and deletes it from the worksheet."),
        ],
        "Same record creation, three tools",
        "requests.post(\n  'https://api.example.com/users',\n  json={'name': 'Alice'}\n)",
        "INSERT INTO users (name)\nVALUES ('Alice');",
        "A2: Alice\n(type into next empty row)",
        "All three create a new user record named Alice \u2014 the same result, just written in a different tool.",
        "HTTP verbs map directly to SQL\u2019s CRUD operations: GET=SELECT, POST=INSERT, PUT=UPDATE, DELETE=DELETE. Same actions, different protocol."
    ),

    f"{MOD03}/lesson03_using_the_python_requests_library.html": (
        "If you already call database connections in SQL or use the Data ribbon in Excel, the Python requests library is your equivalent \u2014 it connects to external data sources over HTTP.",
        [
            ("connect to a source", "fa6-solid:plug",
             "requests.get(url)", "Python opens a connection to a URL and sends an HTTP request.",
             "ODBC / connection string", "SQL connects to a remote server using a connection string.",
             "Data \u2192 New Connection", "Excel creates a new data connection to an external source."),
            ("check the response", "fa6-solid:circle-check",
             "response.status_code", "Python checks the HTTP status code to see whether the request succeeded.",
             "@@ERROR / TRY", "SQL checks for errors after executing a remote query.",
             "connection test", "Excel shows a preview panel confirming the connection loaded data."),
            ("extract the data", "fa6-solid:download",
             "response.json()", "Python converts the HTTP response body into a Python dictionary.",
             "SELECT * FROM linked_server", "SQL reads data from a linked remote server as if it were a local table.",
             "load into worksheet", "Excel loads the connected data into a worksheet as rows and columns."),
        ],
        "Same API fetch, three tools",
        "import requests\nresp = requests.get(\n  'https://api.example.com/orders'\n)\ndata = resp.json()",
        "SELECT *\nFROM OPENQUERY(\n  linked_server,\n  'SELECT * FROM orders'\n);",
        "Data -> From Web ->\nhttps://api.example.com/orders\n-> Load",
        "All three retrieve order data from an external source \u2014 the same result, just written in a different tool.",
        "The requests library is Python\u2019s data connection. It works like SQL\u2019s linked servers or Excel\u2019s web queries \u2014 same concept, different syntax."
    ),

    f"{MOD03}/lesson04_working_with_json_data.html": (
        "If you already work with rows and columns in SQL, or cells in Excel, JSON is just another way to structure the same data. Python reads JSON natively as dictionaries and lists.",
        [
            ("a single record", "fa6-solid:file-lines",
             "dict (JSON object)", "Python reads a JSON object as a dictionary with key-value pairs.",
             "one row", "SQL stores the same record as one row with named columns.",
             "one row in a sheet", "Excel stores each field in a separate cell along a single row."),
            ("a collection of records", "fa6-solid:list",
             "list of dicts", "Python reads a JSON array as a list of dictionaries.",
             "result set", "SQL returns multiple rows as a result set.",
             "table range", "Excel displays multiple records as a range of rows."),
            ("access a nested value", "fa6-solid:sitemap",
             "data['key']['sub']", "Python drills into nested dictionaries using chained key lookups.",
             "JSON_VALUE() / ->>", "SQL extracts a nested value from a JSON column using a path expression.",
             "no direct equivalent", "Excel has no built-in nesting \u2014 you flatten nested data into extra columns."),
        ],
        "Same order record, three tools",
        "import json\norder = json.loads(resp.text)\nprint(order['customer'])",
        "SELECT JSON_VALUE(\n  data, '$.customer'\n) AS customer\nFROM orders;",
        "=A2\n(customer in column A,\nflattened from JSON)",
        "All three extract the customer name from the same order record \u2014 the same result, just written in a different tool.",
        "JSON is just rows-and-columns in a different shape. SQL has JSON functions, Excel flattens it, Python reads it natively."
    ),

    f"{MOD03}/lesson05_parsing_api_responses.html": (
        "If you already extract columns from SQL result sets or pick values from Excel cells, parsing an API response is the same skill \u2014 you navigate structured data and pull out the fields you need.",
        [
            ("extract a field", "fa6-solid:crosshairs",
             "data['key']", "Python accesses a field by its key name in the response dictionary.",
             "SELECT column_name", "SQL selects a specific column from the result set.",
             "=A2", "Excel references a specific cell to get one value."),
            ("loop through a list", "fa6-solid:rotate-right",
             "for item in data['results']", "Python iterates over a list of records inside the response.",
             "cursor / row-by-row", "SQL processes rows one at a time using a cursor.",
             "fill-down formula", "Excel drags a formula down to apply it to every row in a range."),
            ("handle missing fields", "fa6-solid:question",
             "data.get('key', default)", "Python returns a default value when a key is missing from the dictionary.",
             "COALESCE(col, default)", "SQL returns a fallback value when a column is NULL.",
             "IFERROR(val, default)", "Excel returns a fallback when a formula produces an error."),
        ],
        "Same field extraction, three tools",
        "for item in data['results']:\n    name = item.get('name', 'N/A')\n    print(name)",
        "SELECT\n  COALESCE(name, 'N/A')\nFROM api_results;",
        "=IFERROR(A2, \"N/A\")\n-- drag down for each row",
        "All three extract and display names with a fallback for missing values \u2014 the same result, just written in a different tool.",
        "Parsing is just selecting columns from a result set. SQL uses SELECT, Excel uses cell references, Python uses dictionary keys."
    ),

    f"{MOD03}/lesson06_authentication_with_api_keys.html": (
        "If you already use passwords to connect to a SQL database or protect Excel files, API keys serve the same purpose \u2014 they prove your identity so the server lets you in.",
        [
            ("provide credentials", "fa6-solid:key",
             "headers={'Authorization': key}", "Python sends an API key in the request header to authenticate.",
             "connection credentials", "SQL uses a username and password in the connection string.",
             "password-protected file", "Excel asks for a password before opening a protected workbook."),
            ("keep secrets safe", "fa6-solid:lock",
             "os.environ['API_KEY']", "Python reads the key from an environment variable, not from the code.",
             "credential store", "SQL stores connection passwords in a secure credential manager.",
             "separate config file", "Excel users store connection passwords outside the workbook."),
            ("rotate credentials", "fa6-solid:rotate",
             "update env var", "Python rotates an API key by updating the environment variable.",
             "ALTER LOGIN … PASSWORD", "SQL changes a login password with an ALTER statement.",
             "change file password", "Excel changes the workbook password through File \u2192 Protect."),
        ],
        "Same authenticated request, three tools",
        "import os, requests\nkey = os.environ['API_KEY']\nresp = requests.get(url,\n  headers={'X-API-Key': key})",
        "-- connect with credentials\nSELECT *\nFROM linked_server.db.orders;",
        "Data -> From Web -> URL\n-> enter API key in\n   Advanced settings",
        "All three send credentials to access protected data \u2014 the same result, just written in a different tool.",
        "API keys are just passwords for web services. SQL uses connection passwords, Excel uses file passwords, Python uses header tokens."
    ),

    f"{MOD03}/lesson07_oauth_authentication.html": (
        "If you already use single sign-on to access a SQL database, or sign into Microsoft 365 to open a shared Excel file, you have used OAuth-style authentication. Python follows the same flow \u2014 redirect, authorise, receive a token.",
        [
            ("get an access token", "fa6-solid:ticket",
             "OAuth token exchange", "Python sends client credentials and receives a time-limited access token.",
             "Kerberos / AD token", "SQL Server uses Active Directory to issue a token that grants database access.",
             "Microsoft 365 sign-in", "Excel prompts you to sign in to Microsoft 365 before accessing shared data."),
            ("send the token", "fa6-solid:paper-plane",
             "headers={'Authorization': f'Bearer {token}'}", "Python attaches the token to every API request in an Authorization header.",
             "trusted connection", "SQL uses the authenticated token transparently for every query.",
             "automatic refresh", "Excel stays signed in and refreshes data without re-entering credentials."),
            ("refresh an expired token", "fa6-solid:rotate",
             "refresh_token grant", "Python exchanges a refresh token for a new access token when the old one expires.",
             "re-authenticate", "SQL re-authenticates automatically when the Kerberos ticket expires.",
             "sign in again", "Excel prompts you to sign in again when your session expires."),
        ],
        "Same token-based data fetch, three tools",
        "token = get_oauth_token()\nresp = requests.get(url,\n  headers={\n    'Authorization': f'Bearer {token}'\n  })",
        "-- trusted connection\nSELECT *\nFROM protected_table;",
        "Sign in to M365 ->\nData -> Refresh All",
        "All three use a token to access protected data \u2014 the same result, just written in a different tool.",
        "OAuth is single sign-on for APIs. SQL uses trusted connections, Excel uses Microsoft 365 login, Python uses Bearer tokens. Same pattern."
    ),

    f"{MOD03}/lesson08_handling_pagination_in_apis.html": (
        "If you already page through SQL results with LIMIT and OFFSET, or scroll through rows in Excel, API pagination is the same concept \u2014 you fetch one page at a time and move to the next.",
        [
            ("fetch one page", "fa6-solid:file",
             "params={'page': 1}", "Python requests the first page of results by passing a page number.",
             "LIMIT … OFFSET 0", "SQL returns the first page of rows using LIMIT and OFFSET.",
             "visible rows on screen", "Excel shows one screenful of rows at a time."),
            ("move to the next page", "fa6-solid:forward-step",
             "page += 1", "Python increments the page number to request the next batch.",
             "OFFSET += page_size", "SQL increases the OFFSET to skip rows already fetched.",
             "scroll down / Page Down", "Excel scrolls or presses Page Down to see the next set of rows."),
            ("collect all pages", "fa6-solid:layer-group",
             "while loop + extend", "Python loops through pages, appending each batch into one list.",
             "UNION ALL pages", "SQL unions multiple paged queries to combine all results.",
             "Power Query append", "Excel uses Power Query to append data from multiple pages into one table."),
        ],
        "Same paginated data collection, three tools",
        "all_items = []\npage = 1\nwhile True:\n    data = fetch(page=page)\n    if not data: break\n    all_items.extend(data)\n    page += 1",
        "-- page 1\nSELECT * FROM items\nLIMIT 100 OFFSET 0;\n-- page 2\nSELECT * FROM items\nLIMIT 100 OFFSET 100;",
        "Power Query:\n  Source -> Web API\n  -> append pages 1..N\n  -> Load to sheet",
        "All three collect all items across multiple pages \u2014 the same result, just written in a different tool.",
        "Pagination is just LIMIT/OFFSET for APIs. SQL pages through rows, Excel scrolls, Python loops. Same concept."
    ),

    f"{MOD03}/lesson09_handling_api_rate_limits.html": (
        "If you already throttle SQL queries to avoid overloading a database, or wait for Excel to finish refreshing before clicking again, rate limiting is the same principle \u2014 you slow down to avoid being blocked.",
        [
            ("detect a limit", "fa6-solid:hand",
             "status_code == 429", "Python checks for HTTP 429 (Too Many Requests) to know it has been rate-limited.",
             "query timeout", "SQL throws a timeout error when the server is overloaded.",
             "refresh stalls", "Excel stops responding or shows a timeout when the data source is busy."),
            ("wait and retry", "fa6-solid:clock",
             "time.sleep(seconds)", "Python pauses for a set number of seconds before retrying the request.",
             "WAITFOR DELAY", "SQL pauses execution for a specified interval before retrying.",
             "wait and retry manually", "Excel users wait a moment, then click Refresh again."),
            ("back off gradually", "fa6-solid:arrow-trend-up",
             "exponential backoff", "Python doubles the wait time after each failed retry to reduce pressure on the server.",
             "retry with increasing delay", "SQL jobs can be configured to retry with longer intervals between attempts.",
             "retry with longer waits", "Excel users wait progressively longer before retrying a failed refresh."),
        ],
        "Same retry-after-limit pattern, three tools",
        "import time\nresp = requests.get(url)\nif resp.status_code == 429:\n    time.sleep(60)\n    resp = requests.get(url)",
        "-- if timeout, wait\nWAITFOR DELAY '00:01:00';\nSELECT * FROM source;",
        "If refresh fails:\n  wait 60 seconds\n  -> Refresh All again",
        "All three wait and retry after hitting a limit \u2014 the same result, just written in a different tool.",
        "Rate limits protect servers from overload. SQL has timeouts, Excel has refresh limits, APIs have 429 responses. Same safeguard, different signal."
    ),

    f"{MOD03}/lesson10_loading_api_data_into_pandas.html": (
        "If you already load SQL query results into a table, or import data into an Excel worksheet, loading API data into pandas is the same step \u2014 you take raw data and put it into a tabular format.",
        [
            ("convert to a table", "fa6-solid:table",
             "pd.DataFrame(data)", "Python converts a list of dictionaries from the API into a pandas DataFrame.",
             "SELECT INTO temp_table", "SQL loads query results into a temporary table for further analysis.",
             "Data \u2192 Load to sheet", "Excel loads external data into a worksheet as a table."),
            ("select columns", "fa6-solid:grip-vertical",
             "df[['col1', 'col2']]", "Python selects only the columns you need from the DataFrame.",
             "SELECT col1, col2", "SQL returns only the columns listed in the SELECT clause.",
             "hide unused columns", "Excel hides columns that are not needed for the current analysis."),
            ("filter rows", "fa6-solid:filter",
             "df[df['col'] > val]", "Python keeps only the rows where a column meets a condition.",
             "WHERE col > val", "SQL filters rows using a WHERE clause.",
             "AutoFilter", "Excel filters visible rows using the dropdown arrows on column headers."),
        ],
        "Same API-to-table load, three tools",
        "import pandas as pd, requests\ndata = requests.get(url).json()\ndf = pd.DataFrame(data['results'])\nprint(df.head())",
        "SELECT *\nINTO #api_data\nFROM OPENQUERY(\n  linked, 'SELECT ...');\nSELECT TOP 5 *\nFROM #api_data;",
        "Data -> From Web -> URL\n-> Load to worksheet\n-> view first 5 rows",
        "All three load external data into a table and preview the first rows \u2014 the same result, just written in a different tool.",
        "Loading API data into pandas is the same as importing into SQL or Excel. You fetch, you tabulate, you analyse."
    ),

    f"{MOD03}/lesson11_saving_api_data_to_databases.html": (
        "If you already insert SQL query results into a target table, or copy Excel data into a database, saving API data to a database is the same final step \u2014 you write processed records into permanent storage.",
        [
            ("write to a database", "fa6-solid:database",
             "df.to_sql()", "Python writes a DataFrame directly into a database table in one line.",
             "INSERT INTO … SELECT", "SQL copies rows from a source query into a target table.",
             "copy-paste into Access", "Excel users copy worksheet rows and paste them into a database table."),
            ("handle duplicates", "fa6-solid:clone",
             "if_exists='replace'", "Python replaces the existing table if it already contains data.",
             "MERGE / ON CONFLICT", "SQL uses a MERGE or upsert statement to handle duplicate keys.",
             "remove duplicates", "Excel removes duplicate rows before copying data to the database."),
            ("append incrementally", "fa6-solid:plus",
             "if_exists='append'", "Python adds new rows to the existing table without deleting old data.",
             "INSERT INTO … SELECT (no truncate)", "SQL inserts new rows into a table that already has data.",
             "paste below existing rows", "Excel pastes new records below the last row of existing data."),
        ],
        "Same API data saved to database, three tools",
        "from sqlalchemy import create_engine\nengine = create_engine(conn_str)\ndf.to_sql('api_orders',\n          engine,\n          if_exists='append')",
        "INSERT INTO api_orders\n  (customer, total)\nSELECT customer, total\nFROM staging_table;",
        "Copy worksheet rows ->\nPaste into Access table\n(append to existing)",
        "All three append API-sourced order records into a database table \u2014 the same result, just written in a different tool.",
        "Saving to a database is the last step of any data pipeline. SQL uses INSERT, Excel uses paste, Python uses to_sql(). Same destination."
    ),

    f"{MOD03}/lesson12_building_an_api_data_pipeline.html": (
        "If you already chain SQL queries in a stored procedure, or link Excel formulas across sheets, building an API pipeline is the same idea \u2014 you connect fetch, clean, and store steps into an automated sequence.",
        [
            ("extract from API", "fa6-solid:download",
             "requests.get()", "Python fetches raw data from an API endpoint as the first pipeline step.",
             "OPENQUERY / linked server", "SQL pulls data from an external source using a linked server query.",
             "Data \u2192 From Web", "Excel imports data from a URL into a worksheet."),
            ("transform the data", "fa6-solid:wand-magic-sparkles",
             "df.rename() / df.dropna()", "Python cleans and reshapes the raw API data in a DataFrame.",
             "CASE WHEN / COALESCE", "SQL transforms values inside the INSERT query.",
             "helper columns + formulas", "Excel creates helper columns with formulas to clean the imported data."),
            ("load into storage", "fa6-solid:database",
             "df.to_sql() / to_parquet()", "Python writes the cleaned data to a database or file.",
             "INSERT INTO target", "SQL inserts the transformed rows into the final target table.",
             "copy to final sheet", "Excel copies the cleaned data into a final output worksheet."),
            ("schedule the pipeline", "fa6-solid:clock",
             "cron / scheduler", "Python uses a system scheduler to run the pipeline automatically at intervals.",
             "SQL Agent job", "SQL uses a database scheduler to execute the stored procedure on a timetable.",
             "Power Query refresh timer", "Excel sets an automatic refresh interval in Power Query."),
        ],
        "Same three-stage API pipeline, three tools",
        "raw = requests.get(url).json()\ndf = pd.DataFrame(raw['data'])\ndf = df.dropna(subset=['email'])\ndf.to_sql('contacts', engine,\n          if_exists='append')",
        "INSERT INTO contacts\nSELECT email, name\nFROM OPENQUERY(api_link,\n  'SELECT ...')\nWHERE email IS NOT NULL;",
        "1. Data -> From Web -> URL\n2. Clean with formulas\n3. Copy to final sheet",
        "All three fetch, clean, and store contact data from an API \u2014 the same result, just written in a different tool.",
        "An API pipeline is just ETL with a URL as the source. SQL uses stored procedures, Excel uses Power Query, Python uses scripts. Same three stages."
    ),

    f"{MOD03}/lesson13_real_world_api_integration_project.html": (
        "If you already build end-to-end reports in SQL or multisheet workbooks in Excel, a real-world API project is the same workflow \u2014 you connect to a source, process data, and deliver a usable output.",
        [
            ("plan the pipeline", "fa6-solid:clipboard-list",
             "requirements + design", "Python projects start by listing endpoints, fields, and output tables.",
             "query design document", "SQL projects start with a list of source tables, joins, and target schema.",
             "workbook outline", "Excel projects start by sketching which sheets hold raw data, calcs, and output."),
            ("handle errors", "fa6-solid:triangle-exclamation",
             "try / except + logging", "Python wraps API calls in error handlers and logs failures.",
             "TRY … CATCH", "SQL uses TRY-CATCH blocks to log errors without stopping the procedure.",
             "IFERROR + log sheet", "Excel wraps formulas in IFERROR and records issues on a log sheet."),
            ("deliver output", "fa6-solid:file-export",
             "to_sql() / to_csv()", "Python writes the final dataset to a database or export file.",
             "CREATE VIEW / export", "SQL exposes the final result as a view or exports it to a file.",
             "formatted report sheet", "Excel presents the final data on a polished report worksheet."),
        ],
        "Same end-to-end data delivery, three tools",
        "try:\n    data = fetch_all_pages(url)\n    df = clean(data)\n    df.to_sql('report', engine)\nexcept Exception as e:\n    log.error(e)",
        "BEGIN TRY\n  INSERT INTO report\n  SELECT … FROM source;\nEND TRY\nBEGIN CATCH\n  INSERT INTO error_log …\nEND CATCH;",
        "1. Import data (From Web)\n2. Clean (helper formulas)\n3. Output (Report sheet)\n4. Log errors (Log sheet)",
        "All three deliver a clean report from raw external data \u2014 the same result, just written in a different tool.",
        "A real project combines every skill into one pipeline. SQL, Excel, and Python all follow the same plan-fetch-clean-deliver pattern."
    ),

    f"{MOD03}/lesson14_api_best_practices.html": (
        "If you already follow coding standards in SQL or keep tidy Excel workbooks, API best practices are the same discipline \u2014 organise your code, handle errors, and keep secrets safe.",
        [
            ("keep secrets safe", "fa6-solid:lock",
             "environment variables", "Python stores API keys in environment variables, never in source code.",
             "credential manager", "SQL stores connection passwords in a secure credential vault.",
             "separate config file", "Excel users store connection details outside the workbook file."),
            ("handle errors gracefully", "fa6-solid:shield-halved",
             "try / except + retry", "Python catches network errors and retries before giving up.",
             "TRY … CATCH", "SQL wraps queries in TRY-CATCH to handle failures without crashing.",
             "IFERROR()", "Excel wraps formulas in IFERROR to show a fallback instead of an error."),
            ("log everything", "fa6-solid:scroll",
             "logging module", "Python writes timestamped messages to a log file for every request.",
             "audit table", "SQL inserts a row into an audit table after each job runs.",
             "log worksheet", "Excel records run dates and outcomes on a dedicated log sheet."),
            ("use timeouts", "fa6-solid:stopwatch",
             "timeout=10", "Python sets a timeout so requests do not hang indefinitely.",
             "query timeout setting", "SQL sets a query timeout to cancel long-running operations.",
             "refresh timeout", "Excel\u2019s data connection has a timeout setting for slow sources."),
        ],
        "Same safe API call, three tools",
        "import os, requests\nkey = os.environ['API_KEY']\ntry:\n    resp = requests.get(url,\n      headers={'X-Key': key},\n      timeout=10)\nexcept Exception as e:\n    log.error(e)",
        "BEGIN TRY\n  SELECT *\n  FROM OPENQUERY(lnk,\n    'SELECT …')\n  OPTION (QUERYTIMEOUT 10);\nEND TRY\nBEGIN CATCH\n  INSERT INTO log …\nEND CATCH;",
        "Data -> From Web -> URL\nAdvanced: API key header\nTimeout: 10 seconds\nIFERROR fallback",
        "All three make a safe, authenticated request with error handling and a timeout \u2014 the same result, just written in a different tool.",
        "Best practices are universal. Secure your credentials, handle errors, log outcomes, set timeouts. SQL, Excel, and Python all follow the same rules."
    ),

    # ── MOD 04 — Data Pipelines and Orchestration ─────────────────────────────

    f"{MOD04}/lesson01_what_is_a_data_pipeline.html": (
        "If you already chain SQL queries together or link Excel formulas across sheets, you already build simple data pipelines. Python formalises that chain into stages you can automate and monitor.",
        [
            ("move data from A to B", "fa6-solid:right-left",
             "extract \u2192 load", "Python reads data from a source and writes it to a target in a script.",
             "INSERT INTO … SELECT", "SQL copies rows from one table into another in a single statement.",
             "copy-paste between sheets", "Excel copies data from one worksheet and pastes it into another."),
            ("transform along the way", "fa6-solid:wand-magic-sparkles",
             "df.apply() / map()", "Python modifies values during the pipeline before loading them.",
             "CASE WHEN in INSERT", "SQL transforms values inside the INSERT statement.",
             "formula columns", "Excel adds helper columns with formulas that clean data before final output."),
            ("run automatically", "fa6-solid:clock",
             "cron / scheduler", "Python uses a system scheduler to run the pipeline on a timetable.",
             "SQL Agent job", "SQL uses a database agent to execute procedures on a schedule.",
             "Power Query auto-refresh", "Excel schedules automatic data refreshes at set intervals."),
        ],
        "Same daily data load, three tools",
        "raw = pd.read_csv('daily_sales.csv')\nclean = raw.dropna(subset=['amount'])\nclean.to_sql('sales', engine,\n             if_exists='append')",
        "INSERT INTO sales\nSELECT *\nFROM daily_import\nWHERE amount IS NOT NULL;",
        "1. Import daily CSV\n2. Filter blanks\n3. Paste into final sheet",
        "All three load, clean, and store daily sales data \u2014 the same result, just written in a different tool.",
        "A data pipeline is just an automated chain of steps. SQL chains queries, Excel chains formulas, Python chains functions. Same pattern."
    ),

    f"{MOD04}/lesson02_etl_vs_elt.html": (
        "If you already clean data before inserting it in SQL, or transform values in Excel before pasting them elsewhere, you already do ETL. ELT flips the order \u2014 load first, transform later.",
        [
            ("transform then load (ETL)", "fa6-solid:arrow-right",
             "clean in Python, then to_sql()", "Python cleans the data in memory before writing it to the database.",
             "transform in staging query", "SQL cleans data in a staging query before inserting into the final table.",
             "fix in helper columns first", "Excel creates helper columns to clean data, then copies clean values."),
            ("load then transform (ELT)", "fa6-solid:arrow-down",
             "to_sql() raw, then SQL view", "Python loads raw data first, then a SQL view transforms it in the database.",
             "INSERT raw, CREATE VIEW", "SQL loads raw rows into a staging table, then a view reshapes them.",
             "import raw, clean later", "Excel imports raw data, then uses Power Query to reshape it in place."),
            ("choose the right approach", "fa6-solid:scale-balanced",
             "if/else logic", "Python picks ETL when data is small or ELT when the database is more powerful.",
             "query plan analysis", "SQL DBAs choose based on where compute resources are cheapest.",
             "Power Query vs formulas", "Excel users decide whether to clean data in Power Query or in the sheet."),
        ],
        "Same data cleanup, two orderings",
        "# ETL: clean first\ndf['status'] = df['status'].str.upper()\ndf.to_sql('orders', engine)\n\n# ELT: load raw, clean in DB\ndf.to_sql('raw_orders', engine)\n# then: CREATE VIEW clean AS ...",
        "-- ETL\nINSERT INTO orders\nSELECT UPPER(status) …\n  FROM staging;\n-- ELT\nINSERT INTO raw_orders\n  SELECT * FROM staging;\nCREATE VIEW clean AS\n  SELECT UPPER(status) …\n  FROM raw_orders;",
        "ETL: =UPPER(A2) in helper\n  -> paste values\nELT: import raw\n  -> Power Query transform",
        "All three clean the same data \u2014 the difference is whether you clean before or after loading.",
        "ETL and ELT are just two orderings of the same steps. SQL and Excel users make the same choice \u2014 the logic is identical."
    ),

    f"{MOD04}/lesson03_pipeline_design_patterns.html": (
        "If you already modularise SQL into views and stored procedures, or split Excel work across sheets, pipeline design patterns are the same idea \u2014 organise your steps so they are reusable, testable, and easy to debug.",
        [
            ("modular stages", "fa6-solid:puzzle-piece",
             "separate functions", "Python puts each pipeline stage into its own function so you can test it independently.",
             "views + stored procedures", "SQL separates logic into views and procedures you can call by name.",
             "separate sheets", "Excel puts each stage on a different worksheet with clear input/output ranges."),
            ("configuration over code", "fa6-solid:gear",
             "config dict / YAML", "Python reads source paths, table names, and options from a config file.",
             "parameters / variables", "SQL uses variables or parameters to avoid hard-coding values.",
             "named ranges", "Excel uses named ranges so formulas reference labels instead of cell addresses."),
            ("idempotent runs", "fa6-solid:rotate",
             "REPLACE / upsert", "Python writes results so re-running the pipeline produces the same outcome.",
             "MERGE … ON CONFLICT", "SQL uses MERGE or ON CONFLICT to safely rerun an INSERT.",
             "clear + reload", "Excel clears the output range before reloading to avoid duplicate rows."),
        ],
        "Same modular pipeline, three tools",
        "def extract():\n    return pd.read_csv('src.csv')\ndef transform(df):\n    return df.dropna()\ndef load(df):\n    df.to_sql('tgt', engine,\n              if_exists='replace')",
        "CREATE VIEW v_clean AS\n  SELECT * FROM raw\n  WHERE col IS NOT NULL;\n\nCREATE PROC load_clean AS\n  INSERT INTO target\n  SELECT * FROM v_clean;",
        "Sheet1: raw import\nSheet2: =IF(A2<>\"\",A2,\"\")\nSheet3: paste-values final\n(clear Sheet3 before reload)",
        "All three split the pipeline into reusable, testable stages \u2014 the same result, just written in a different tool.",
        "Design patterns keep pipelines maintainable. SQL uses views, Excel uses sheets, Python uses functions. Same principle."
    ),

    f"{MOD04}/lesson04_working_with_large_data_files.html": (
        "If you already page through SQL results or filter large Excel files before processing, working with large data files in Python is the same challenge \u2014 process more data than fits in memory by reading in pieces.",
        [
            ("read in chunks", "fa6-solid:layer-group",
             "chunksize=N", "Python\u2019s pandas reads a large file in N-row batches instead of loading it all.",
             "LIMIT … OFFSET", "SQL fetches rows in pages using LIMIT and OFFSET.",
             "Power Query incremental", "Excel\u2019s Power Query can load data in incremental batches."),
            ("use efficient formats", "fa6-solid:file-zipper",
             "Parquet / Feather", "Python reads columnar formats that compress data and skip unneeded columns.",
             "partitioned tables", "SQL partitions large tables so queries scan only relevant segments.",
             "binary .xlsx vs CSV", "Excel\u2019s binary format loads faster than CSV for large files."),
            ("stream results", "fa6-solid:forward",
             "generator / yield", "Python yields one chunk at a time to keep memory flat.",
             "cursor + fetchmany()", "SQL fetches a batch of rows through a server-side cursor.",
             "scroll through rows", "Excel scrolls through rows on screen, loading only what is visible."),
        ],
        "Same chunked file read, three tools",
        "for chunk in pd.read_csv(\n    'big.csv', chunksize=50000):\n    process(chunk)",
        "DECLARE cur CURSOR FOR\n  SELECT * FROM big_table;\nFETCH NEXT 50000 ROWS\n  FROM cur;",
        "Power Query:\n  Source -> CSV\n  -> Keep first 50,000 rows\n  -> Load",
        "All three read a large dataset in manageable batches \u2014 the same result, just written in a different tool.",
        "Big-data handling is universal. SQL uses cursors, Excel uses Power Query, Python uses chunking. Same strategy \u2014 process in pieces."
    ),

    f"{MOD04}/lesson05_data_validation_in_pipelines.html": (
        "If you already use CHECK constraints in SQL or Data Validation in Excel, pipeline validation is the same idea \u2014 you define rules that reject bad data before it reaches the final table.",
        [
            ("check for nulls", "fa6-solid:circle-exclamation",
             "df['col'].notna()", "Python checks that a column has no missing values.",
             "col IS NOT NULL", "SQL rejects rows where a required column is NULL.",
             "Data Validation \u2192 Not Blank", "Excel\u2019s Data Validation rule prevents empty cells."),
            ("check value ranges", "fa6-solid:ruler-combined",
             "assert df['age'].between(0,120).all()", "Python asserts that every value falls within an expected range.",
             "CHECK (age BETWEEN 0 AND 120)", "SQL\u2019s CHECK constraint rejects rows outside the allowed range.",
             "Data Validation \u2192 Between", "Excel restricts cell input to a number between two bounds."),
            ("check uniqueness", "fa6-solid:fingerprint",
             "assert not df['id'].duplicated().any()", "Python asserts that a column has no duplicate values.",
             "UNIQUE constraint", "SQL\u2019s UNIQUE constraint prevents duplicate values in a column.",
             "Remove Duplicates", "Excel\u2019s Remove Duplicates feature deletes rows with repeated values."),
            ("check data types", "fa6-solid:font",
             "df['col'].dtype", "Python checks that a column\u2019s data type matches the expected type.",
             "column data type", "SQL defines the column type at table creation and rejects mismatches.",
             "Format Cells", "Excel\u2019s Format Cells sets a column to Number, Date, or Text."),
        ],
        "Same null-check validation, three tools",
        "assert df['email'].notna().all(), \\\n    'Missing emails found!'",
        "ALTER TABLE users\n  ADD CONSTRAINT chk_email\n  CHECK (email IS NOT NULL);",
        "Data -> Validation ->\nAllow: Any value\nCheck: Reject blank cells",
        "All three reject records with missing email addresses \u2014 the same result, just written in a different tool.",
        "Validation rules are the same everywhere. SQL uses constraints, Excel uses Data Validation, Python uses assertions. Same goal \u2014 clean data."
    ),

    f"{MOD04}/lesson09_scheduling_pipelines.html": (
        "If you already schedule SQL Agent jobs or set Excel to auto-refresh, scheduling a Python pipeline is the same action \u2014 you tell the system when and how often to run your code.",
        [
            ("define a schedule", "fa6-solid:calendar-days",
             "cron expression", "Python uses a cron expression like <code class=\"font-mono\">0 6 * * *</code> to run a job at 6 a.m. daily.",
             "SQL Agent schedule", "SQL uses a job schedule dialog to pick the time and frequency.",
             "refresh interval", "Excel sets an auto-refresh interval in minutes on the data connection."),
            ("trigger on an event", "fa6-solid:bell",
             "file watcher / webhook", "Python triggers a pipeline when a new file appears or a webhook fires.",
             "trigger / event", "SQL uses a database trigger to start a procedure when data changes.",
             "on-open refresh", "Excel refreshes data automatically when the workbook is opened."),
            ("monitor a run", "fa6-solid:chart-line",
             "logging + alerts", "Python logs each run and sends an alert if the pipeline fails.",
             "job history", "SQL Agent records success or failure in its job history.",
             "refresh status bar", "Excel shows a status bar message while data is refreshing."),
        ],
        "Same daily 6 a.m. schedule, three tools",
        "# crontab entry\n# 0 6 * * * python /etl/run.py\nimport schedule\nschedule.every().day.at('06:00').do(run)",
        "-- SQL Agent Job\n-- Schedule: Daily at 06:00\nEXEC msdb.dbo.sp_add_jobschedule\n  @job_name = 'etl_job',\n  @freq_type = 4,\n  @active_start_time = 060000;",
        "Data -> Connection Properties\n-> Refresh every 1440 min\n(= once per day)",
        "All three schedule a data job to run once per day at 6 a.m. \u2014 the same result, just written in a different tool.",
        "Scheduling is the same concept everywhere. SQL uses Agent jobs, Excel uses refresh timers, Python uses cron. Same clock, different interface."
    ),

    f"{MOD04}/lesson10_building_a_simple_python_pipeline.html": (
        "If you already write stored procedures in SQL or build multisheet workbooks in Excel, a simple Python pipeline is the same thing \u2014 a sequence of steps that extract, transform, and load data.",
        [
            ("define extract step", "fa6-solid:file-arrow-down",
             "def extract():", "Python reads raw data from a file or API inside a dedicated function.",
             "SELECT * FROM source", "SQL reads all rows from the source table as the first step.",
             "import data sheet", "Excel imports raw data into a dedicated input worksheet."),
            ("define transform step", "fa6-solid:wand-magic-sparkles",
             "def transform(df):", "Python cleans and reshapes data inside a transform function.",
             "CREATE VIEW v_clean", "SQL creates a view that applies transformations to the raw data.",
             "helper formula columns", "Excel adds formula columns that clean values on a separate sheet."),
            ("define load step", "fa6-solid:database",
             "def load(df):", "Python writes the final DataFrame to a database or file.",
             "INSERT INTO target", "SQL inserts the transformed rows into the final target table.",
             "paste values to output", "Excel copies clean values and pastes them into the output sheet."),
            ("run the pipeline", "fa6-solid:play",
             "if __name__ == '__main__':", "Python\u2019s main block calls extract, transform, and load in order.",
             "EXEC run_etl", "SQL calls the stored procedure that runs all steps in sequence.",
             "click Refresh All", "Excel refreshes all data connections to re-run the pipeline."),
        ],
        "Same three-function pipeline, three tools",
        "def extract():\n    return pd.read_csv('raw.csv')\ndef transform(df):\n    return df.dropna()\ndef load(df):\n    df.to_sql('clean', engine)\n\nload(transform(extract()))",
        "-- stored procedure\nCREATE PROC run_etl AS\nBEGIN\n  INSERT INTO clean\n  SELECT * FROM raw\n  WHERE col IS NOT NULL;\nEND;\nEXEC run_etl;",
        "1. Import -> Raw sheet\n2. Clean -> Helper sheet\n3. Output -> Final sheet\n4. Refresh All to rerun",
        "All three execute an extract-transform-load pipeline \u2014 the same result, just written in a different tool.",
        "A Python pipeline is just a stored procedure written as functions. SQL chains queries, Excel chains sheets, Python chains function calls."
    ),

    f"{MOD04}/lesson11_pipeline_project_automating_data_ingestion.html": (
        "If you already schedule SQL imports or set Excel to auto-refresh from external sources, automating data ingestion in Python is the same goal \u2014 new data arrives without you clicking a button.",
        [
            ("fetch new data only", "fa6-solid:forward-step",
             "watermark / last_id", "Python tracks the last-processed ID and fetches only newer records.",
             "WHERE id > @last_id", "SQL filters on an incrementing ID to select only new rows.",
             "filter by date column", "Excel filters the import source to show only rows after the last date."),
            ("store raw data", "fa6-solid:box-archive",
             "to_sql('raw_table')", "Python loads fetched records into a raw staging table in the database.",
             "INSERT INTO staging", "SQL inserts new rows into a staging table before final processing.",
             "paste into raw sheet", "Excel pastes imported data into a raw data worksheet."),
            ("handle failures", "fa6-solid:triangle-exclamation",
             "try / except + log", "Python catches errors during ingestion and logs them without stopping.",
             "TRY … CATCH", "SQL uses TRY-CATCH to log failures and continue.",
             "IFERROR on import", "Excel wraps import formulas in IFERROR to handle missing data."),
        ],
        "Same incremental data fetch, three tools",
        "last_id = get_watermark()\nnew_rows = fetch(since=last_id)\ndf = pd.DataFrame(new_rows)\ndf.to_sql('raw', engine,\n          if_exists='append')\nupdate_watermark(df['id'].max())",
        "DECLARE @last INT =\n  (SELECT MAX(id)\n   FROM watermarks);\nINSERT INTO raw\nSELECT * FROM source\nWHERE id > @last;\nUPDATE watermarks\n  SET last_id = @@IDENTITY;",
        "1. Filter source: Date >\n   last import date\n2. Load new rows\n3. Update date stamp cell",
        "All three fetch and store only new records since the last run \u2014 the same result, just written in a different tool.",
        "Incremental ingestion uses the same watermark pattern everywhere. SQL tracks MAX(id), Excel tracks a date cell, Python tracks a stored value."
    ),

    f"{MOD04}/lesson12_pipeline_project_data_quality_checks.html": (
        "If you already use CHECK constraints in SQL or conditional formatting in Excel to flag bad data, pipeline quality checks do the same thing \u2014 they verify records before they reach the final table.",
        [
            ("check completeness", "fa6-solid:list-check",
             "df.notna().all()", "Python checks that no required columns have missing values.",
             "NOT NULL constraint", "SQL rejects rows where a required column is NULL.",
             "Conditional Formatting \u2192 Blanks", "Excel highlights blank cells so you can spot missing data."),
            ("check ranges", "fa6-solid:ruler-combined",
             "df['val'].between(lo, hi)", "Python checks that values fall within an expected range.",
             "CHECK (val BETWEEN …)", "SQL\u2019s CHECK constraint rejects out-of-range values.",
             "Data Validation \u2192 Between", "Excel restricts input to values between two bounds."),
            ("flag and quarantine", "fa6-solid:flag",
             "bad = df[~mask]; good = df[mask]", "Python splits the DataFrame into good and bad rows.",
             "INSERT INTO quarantine", "SQL moves rejected rows into a quarantine table for review.",
             "move to error sheet", "Excel moves flagged rows to a separate error worksheet."),
        ],
        "Same completeness check, three tools",
        "mask = df['email'].notna()\ngood = df[mask]\nbad = df[~mask]\nbad.to_csv('quarantine.csv')\ngood.to_sql('clean', engine)",
        "INSERT INTO quarantine\nSELECT * FROM staging\nWHERE email IS NULL;\n\nINSERT INTO clean\nSELECT * FROM staging\nWHERE email IS NOT NULL;",
        "1. Filter: Email = Blanks\n2. Cut rows -> Error sheet\n3. Remaining -> Output sheet",
        "All three separate good records from bad ones based on missing emails \u2014 the same result, just written in a different tool.",
        "Quality checks are universal. SQL uses constraints, Excel uses validation rules, Python uses boolean masks. Same gate, different syntax."
    ),

    f"{MOD04}/lesson13_pipeline_project_database_loading.html": (
        "If you already INSERT rows in SQL or paste data into an Access table from Excel, database loading in Python is the last pipeline step \u2014 you write clean records into permanent storage.",
        [
            ("bulk insert", "fa6-solid:boxes-packing",
             "df.to_sql(method='multi')", "Python inserts thousands of rows in a single batch for speed.",
             "BULK INSERT", "SQL\u2019s BULK INSERT loads many rows from a file in one operation.",
             "paste large range", "Excel pastes a large range of rows into a database table at once."),
            ("upsert / merge", "fa6-solid:arrows-rotate",
             "INSERT … ON CONFLICT UPDATE", "Python executes an upsert statement to update existing rows and insert new ones.",
             "MERGE … WHEN MATCHED", "SQL\u2019s MERGE updates or inserts depending on whether the key exists.",
             "find duplicates + overwrite", "Excel finds duplicate rows and overwrites them with updated values."),
            ("verify the load", "fa6-solid:magnifying-glass-chart",
             "assert len(df) == count", "Python compares the DataFrame row count to the database row count after loading.",
             "SELECT COUNT(*)", "SQL counts rows in the target table to verify the load succeeded.",
             "count rows in output", "Excel uses COUNTA to count rows in the output sheet after pasting."),
        ],
        "Same bulk load with verification, three tools",
        "df.to_sql('orders', engine,\n          if_exists='append',\n          method='multi')\ndb_count = pd.read_sql(\n  'SELECT COUNT(*) FROM orders',\n  engine).iloc[0,0]\nassert db_count >= len(df)",
        "BULK INSERT orders\nFROM 'orders.csv';\nSELECT COUNT(*) FROM orders;",
        "1. Paste rows into table\n2. =COUNTA(A:A)-1\n   to verify row count",
        "All three load records in bulk and verify the count afterwards \u2014 the same result, just written in a different tool.",
        "Database loading is the final pipeline step. SQL uses BULK INSERT, Excel uses paste, Python uses to_sql(). Same destination \u2014 a populated table."
    ),

    f"{MOD04}/lesson14_production_pipeline_architecture.html": (
        "If you already set up SQL replication or maintain shared Excel templates, production architecture is the same challenge \u2014 you make your pipeline reliable, monitored, and recoverable in a live environment.",
        [
            ("separate environments", "fa6-solid:layer-group",
             "dev / staging / prod configs", "Python uses different config files for development, staging, and production databases.",
             "dev / staging / prod databases", "SQL maintains separate database instances for each environment.",
             "draft / final workbooks", "Excel users keep a draft workbook for testing and a final one for production."),
            ("monitor pipeline health", "fa6-solid:chart-line",
             "logging + dashboards", "Python logs metrics and displays them on a monitoring dashboard.",
             "SQL Agent alerts", "SQL Agent sends email alerts when a job fails.",
             "conditional formatting flags", "Excel uses conditional formatting to highlight errors in the output."),
            ("recover from failures", "fa6-solid:rotate-left",
             "retry + rollback", "Python retries failed steps and rolls back partial writes on error.",
             "TRANSACTION + ROLLBACK", "SQL wraps loads in a transaction and rolls back if any step fails.",
             "Undo / restore backup", "Excel users undo changes or restore a backup copy of the file."),
        ],
        "Same transactional load with rollback, three tools",
        "try:\n    with engine.begin() as conn:\n        df.to_sql('orders', conn,\n                  if_exists='append')\nexcept Exception:\n    log.error('Rolled back')",
        "BEGIN TRANSACTION;\nINSERT INTO orders\n  SELECT * FROM staging;\nIF @@ERROR <> 0\n  ROLLBACK;\nELSE\n  COMMIT;",
        "1. Save backup copy\n2. Paste new data\n3. If error -> revert\n   to backup file",
        "All three wrap a data load in a safe transaction that rolls back on failure \u2014 the same result, just written in a different tool.",
        "Production architecture adds safety nets. SQL uses transactions, Excel uses backups, Python uses try/except + rollback. Same principle \u2014 protect the data."
    ),

    # ── MOD 05 — Large Scale Data Processing ──────────────────────────────────

    f"{MOD05}/lesson02_memory_optimization.html": (
        "If you already choose INT vs VARCHAR in SQL, or format cells as Number vs Text in Excel, memory optimisation is the same idea \u2014 use smaller data types to reduce the space your data consumes.",
        [
            ("choose a smaller type", "fa6-solid:minimize",
             "astype('int32')", "Python downcasts a column to a smaller integer type to cut memory in half.",
             "INT vs BIGINT", "SQL picks INT (4 bytes) instead of BIGINT (8 bytes) when values are small.",
             "Number vs Text format", "Excel formats a column as Number instead of General to help it load faster."),
            ("use categories", "fa6-solid:tags",
             "astype('category')", "Python replaces repeated strings with integer codes that take far less memory.",
             "foreign key lookup", "SQL stores a small integer FK instead of repeating the full string in every row.",
             "Data Validation list", "Excel uses a dropdown list so cells store a reference instead of free text."),
            ("drop unused columns", "fa6-solid:scissors",
             "df.drop(columns=[...])", "Python drops columns that are not needed to free memory.",
             "SELECT only needed cols", "SQL queries only the columns required instead of SELECT *.",
             "delete unused columns", "Excel deletes columns that are not needed for the analysis."),
        ],
        "Same column downcast, three tools",
        "df['quantity'] = df['quantity'].astype('int16')\nprint(df.memory_usage(deep=True))",
        "ALTER TABLE orders\n  ALTER COLUMN quantity\n  SMALLINT;  -- was INT",
        "Select column -> Format\n  -> Number (0 decimals)\n  instead of General",
        "All three reduce storage by using a smaller data type for the quantity column \u2014 the same result, just written in a different tool.",
        "Memory optimisation is about choosing the right size. SQL picks column types, Excel picks cell formats, Python picks dtypes. Same trade-off."
    ),

    f"{MOD05}/lesson03_chunk_processing.html": (
        "If you already page through SQL results or process Excel data in filtered batches, chunk processing in Python is the same approach \u2014 handle a large dataset one piece at a time.",
        [
            ("set the chunk size", "fa6-solid:ruler-horizontal",
             "chunksize=10000", "Python tells pandas how many rows to read in each batch.",
             "LIMIT 10000", "SQL limits the result set to 10,000 rows per page.",
             "filter first 10,000 rows", "Excel filters or selects the first 10,000 rows for processing."),
            ("process each chunk", "fa6-solid:gears",
             "for chunk in reader:", "Python loops through chunks, applying the same logic to each one.",
             "WHILE loop + OFFSET", "SQL uses a loop to fetch and process one page at a time.",
             "process by sheet", "Excel splits data across sheets and processes each one separately."),
            ("combine results", "fa6-solid:object-group",
             "results.append(chunk_result)", "Python collects each chunk\u2019s output into a final list or DataFrame.",
             "UNION ALL", "SQL combines the results of multiple paged queries into one result set.",
             "consolidate sheets", "Excel copies results from each sheet into a summary sheet."),
        ],
        "Same chunked aggregation, three tools",
        "total = 0\nfor chunk in pd.read_csv(\n    'big.csv', chunksize=10000):\n    total += chunk['amount'].sum()\nprint(total)",
        "-- sum page by page\nSELECT SUM(amount)\nFROM big_table;  -- DB handles\n                 -- internally",
        "=SUM(Sheet1!B:B)\n+ SUM(Sheet2!B:B)\n+ SUM(Sheet3!B:B)",
        "All three calculate the total amount from a large dataset \u2014 the same result, just written in a different tool.",
        "Chunking is just pagination for processing. SQL pages with OFFSET, Excel splits into sheets, Python splits into chunks. Same pattern."
    ),

    f"{MOD05}/lesson04_processing_millions_of_rows.html": (
        "If you already use SUM() in SQL or array formulas in Excel to operate on entire columns at once, vectorised processing in Python is the same idea \u2014 apply one operation to millions of values in a single step.",
        [
            ("operate on a whole column", "fa6-solid:bolt",
             "df['col'] * 1.1", "Python multiplies every value in a column at once without a loop.",
             "UPDATE … SET col = col * 1.1", "SQL updates every row in a column with one statement.",
             "=A2*1.1 dragged down", "Excel applies a formula to every row by dragging it down the column."),
            ("avoid row-by-row loops", "fa6-solid:ban",
             "vectorised operations", "Python uses NumPy/pandas array operations instead of for-loops.",
             "set-based operations", "SQL operates on the full result set, not one row at a time.",
             "array formulas", "Excel\u2019s array formulas process entire ranges in a single expression."),
            ("index for fast lookup", "fa6-solid:magnifying-glass",
             "df.set_index('id')", "Python sets an index column so lookups skip scanning every row.",
             "CREATE INDEX", "SQL creates an index so the database finds rows without a full table scan.",
             "sort + VLOOKUP", "Excel sorts data and uses VLOOKUP for faster approximate matching."),
        ],
        "Same column-wide price increase, three tools",
        "df['price'] = df['price'] * 1.1",
        "UPDATE products\nSET price = price * 1.1;",
        "=A2*1.1\n(fill down entire column)",
        "All three increase every price by 10% in a single operation \u2014 the same result, just written in a different tool.",
        "Vectorised operations are the Python equivalent of SQL\u2019s set-based queries. Avoid loops \u2014 let the engine process the whole column at once."
    ),

    f"{MOD05}/lesson05_columnar_storage.html": (
        "If you already SELECT specific columns in SQL rather than SELECT *, or hide unused columns in Excel, columnar storage applies the same principle at the file level \u2014 read only the columns you need.",
        [
            ("read selected columns", "fa6-solid:table-columns",
             "columns=['a','b']", "Python reads only named columns from a columnar file, skipping the rest.",
             "SELECT a, b", "SQL returns only the columns listed in the SELECT clause.",
             "hide unused columns", "Excel hides columns that are not needed for the current analysis."),
            ("compress similar values", "fa6-solid:compress",
             "Parquet compression", "Python benefits from columnar compression because similar values group together.",
             "columnstore index", "SQL\u2019s columnstore index compresses data by storing columns together.",
             "ZIP the file", "Excel users zip a CSV to compress it, but without per-column benefits."),
            ("skip irrelevant data", "fa6-solid:forward-fast",
             "predicate pushdown", "Python\u2019s reader skips entire column groups that are not in the query.",
             "index seek", "SQL\u2019s index lets the engine skip rows and pages that do not match the filter.",
             "AutoFilter + copy", "Excel filters rows visually and copies only the visible subset."),
        ],
        "Same two-column read, three tools",
        "df = pd.read_parquet(\n  'sales.parquet',\n  columns=['region', 'total']\n)",
        "SELECT region, total\nFROM sales;",
        "Hide all columns except\nRegion (C) and Total (F)",
        "All three retrieve only the region and total columns from the sales data \u2014 the same result, just written in a different tool.",
        "Columnar storage is SELECT-specific-columns at the file level. SQL picks columns in queries, Excel hides them, Parquet physically skips them."
    ),

    f"{MOD05}/lesson06_parquet_files.html": (
        "If you already export SQL query results to files, or save Excel workbooks in different formats, Parquet is just another file format \u2014 optimised for fast reads and small size.",
        [
            ("write to a file", "fa6-solid:file-arrow-down",
             "df.to_parquet()", "Python writes a DataFrame to a Parquet file in one line.",
             "COPY TO … PARQUET", "SQL exports query results to a Parquet file on disk.",
             "Save As CSV", "Excel saves the worksheet as a CSV file for sharing."),
            ("read selected columns", "fa6-solid:grip-vertical",
             "columns=[...]", "Python loads only the columns you list, skipping the rest of the file.",
             "SELECT col1, col2", "SQL returns only the columns named in the SELECT clause.",
             "delete unused columns", "Excel deletes columns not needed before processing."),
            ("read metadata without loading", "fa6-solid:circle-info",
             "pq.read_metadata()", "Python reads the file footer to see row counts and column stats without loading data.",
             "sp_spaceused / stats", "SQL queries table statistics without reading every row.",
             "file properties", "Excel shows file size and row count in the statusbar and properties dialog."),
        ],
        "Same data export, three tools",
        "df.to_parquet('orders.parquet',\n              compression='snappy')",
        "COPY (SELECT * FROM orders)\nTO 'orders.parquet'\n(FORMAT PARQUET);",
        "File -> Save As ->\norders.csv",
        "All three export the orders table to a file for storage or sharing \u2014 the same result, just written in a different tool.",
        "Parquet replaces CSV for analytics. SQL and Excel export to files too \u2014 Parquet just compresses better and reads faster."
    ),

    f"{MOD05}/lesson07_pyarrow_basics.html": (
        "If you already use SQL\u2019s typed columns or Excel\u2019s cell formats, PyArrow\u2019s strict schemas do the same thing \u2014 they enforce data types so every column has a known format.",
        [
            ("define column types", "fa6-solid:clipboard-list",
             "pa.schema([...])", "Python defines a schema listing each column name and its exact data type.",
             "CREATE TABLE (col INT, …)", "SQL defines column types when creating a table.",
             "Format Cells", "Excel sets column formats to Number, Date, or Text."),
            ("convert between formats", "fa6-solid:arrows-turn-to-dots",
             "table.to_pandas()", "Python converts a PyArrow table to a pandas DataFrame and back.",
             "CAST(col AS type)", "SQL converts a column from one type to another with CAST.",
             "paste as values", "Excel converts formulas to static values by pasting as values."),
            ("read/write Parquet", "fa6-solid:hard-drive",
             "pq.write_table()", "Python writes a PyArrow table to a Parquet file at compiled speed.",
             "COPY TO PARQUET", "SQL exports data to Parquet format using a COPY command.",
             "Save As CSV", "Excel saves data to a file, though not in Parquet format natively."),
        ],
        "Same typed table creation, three tools",
        "import pyarrow as pa\nschema = pa.schema([\n  ('name', pa.string()),\n  ('age', pa.int32())\n])\ntable = pa.table(\n  {'name': ['Alice'], 'age': [30]},\n  schema=schema)",
        "CREATE TABLE users (\n  name VARCHAR(100),\n  age INT\n);\nINSERT INTO users\nVALUES ('Alice', 30);",
        "A1: Name (Text)\nB1: Age (Number)\nA2: Alice  B2: 30",
        "All three create a typed table with a name and age column \u2014 the same result, just written in a different tool.",
        "PyArrow schemas are like SQL\u2019s CREATE TABLE or Excel\u2019s Format Cells. They enforce column types so your data stays consistent."
    ),

    f"{MOD05}/lesson08_introduction_to_polars.html": (
        "If you already filter and group data in SQL, or build PivotTables in Excel, Polars does the same operations \u2014 with a syntax familiar to pandas users but an engine that runs much faster.",
        [
            ("filter rows", "fa6-solid:filter",
             "df.filter(pl.col('x') > 10)", "Polars keeps only rows where a condition is true.",
             "WHERE x > 10", "SQL filters rows using a WHERE clause.",
             "AutoFilter > 10", "Excel\u2019s AutoFilter hides rows that do not match the condition."),
            ("group and aggregate", "fa6-solid:object-group",
             "df.group_by('g').agg(…)", "Polars groups rows and calculates summaries per group.",
             "GROUP BY g", "SQL groups rows and applies aggregate functions.",
             "PivotTable", "Excel\u2019s PivotTable groups and summarises data interactively."),
            ("lazy evaluation", "fa6-solid:lightbulb",
             "df.lazy().collect()", "Polars builds a query plan first and optimises it before executing.",
             "query plan / EXPLAIN", "SQL builds an execution plan and optimises it before running.",
             "Power Query steps", "Excel\u2019s Power Query records steps and applies them on refresh."),
            ("parallel execution", "fa6-solid:microchip",
             "automatic multi-threading", "Polars uses all CPU cores automatically without extra code.",
             "parallel query", "SQL can execute parts of a query on multiple cores.",
             "manual workaround", "Excel has limited parallel processing; large files slow down."),
        ],
        "Same group-by total, three tools",
        "import polars as pl\nresult = (\n  df.group_by('region')\n    .agg(pl.col('sales').sum())\n)",
        "SELECT region,\n       SUM(sales) AS total\nFROM orders\nGROUP BY region;",
        "PivotTable:\n  Rows = Region\n  Values = SUM of Sales",
        "All three calculate total sales per region \u2014 the same result, just written in a different tool.",
        "Polars is the fast lane for DataFrame work. If you know SQL\u2019s GROUP BY or Excel\u2019s PivotTables, Polars syntax will feel natural."
    ),

    f"{MOD05}/lesson09_faster_dataframes_with_polars.html": (
        "If you already optimise SQL queries with indexes and execution plans, or speed up Excel with array formulas, Polars expressions and lazy mode are the same optimisation strategy \u2014 plan first, execute fast.",
        [
            ("write an expression", "fa6-solid:receipt",
             "pl.col('x') * 1.1", "Polars describes what to compute without running it yet.",
             "SELECT x * 1.1", "SQL describes a calculation in the SELECT list.",
             "=A2*1.1", "Excel writes a formula that calculates a new value."),
            ("optimise before running", "fa6-solid:brain",
             "lazy().collect()", "Polars optimises the full query plan before executing any step.",
             "EXPLAIN / query optimiser", "SQL\u2019s optimiser rearranges the execution plan for speed.",
             "Power Query fold", "Excel\u2019s Power Query pushes operations to the data source when possible."),
            ("filter early", "fa6-solid:forward-fast",
             "predicate pushdown", "Polars moves filters as early as possible to reduce the data scanned.",
             "WHERE before JOIN", "SQL\u2019s optimiser pushes WHERE filters before expensive JOINs.",
             "filter before PivotTable", "Excel users filter their source range before creating a PivotTable."),
        ],
        "Same optimised group query, three tools",
        "result = (\n  df.lazy()\n    .filter(pl.col('active'))\n    .group_by('dept')\n    .agg(pl.col('salary').mean())\n    .collect()\n)",
        "SELECT dept,\n       AVG(salary) AS avg_sal\nFROM employees\nWHERE active = 1\nGROUP BY dept;",
        "1. Filter Active = TRUE\n2. PivotTable:\n   Rows = Dept\n   Values = AVG of Salary",
        "All three calculate average salary per department for active employees \u2014 the same result, just written in a different tool.",
        "Lazy evaluation is Polars\u2019 query optimiser. SQL has one too, and Excel\u2019s Power Query folds operations. Same idea \u2014 plan before you execute."
    ),

    f"{MOD05}/lesson10_duckdb_for_analytics.html": (
        "If you already write SQL queries against a database, DuckDB lets you write the exact same SQL \u2014 directly on files and DataFrames, with no server to set up.",
        [
            ("query a file directly", "fa6-solid:file-code",
             "duckdb.sql(\"SELECT …\")", "Python runs a SQL query directly on a CSV or Parquet file.",
             "SELECT … FROM table", "SQL queries data that has already been loaded into a database.",
             "open a CSV", "Excel opens a CSV file and displays it as a worksheet."),
            ("aggregate data", "fa6-solid:calculator",
             "GROUP BY in DuckDB SQL", "Python uses familiar SQL syntax inside DuckDB to group and sum.",
             "GROUP BY … SUM()", "SQL groups rows and calculates aggregates in the database.",
             "PivotTable SUM", "Excel groups data in a PivotTable and sums the values."),
            ("join datasets", "fa6-solid:link",
             "JOIN in DuckDB SQL", "Python joins two files or DataFrames using standard SQL JOIN syntax.",
             "JOIN … ON", "SQL joins tables on matching keys.",
             "VLOOKUP / XLOOKUP", "Excel links data from two sheets using VLOOKUP or XLOOKUP."),
        ],
        "Same group-by query on a file, three tools",
        "import duckdb\nresult = duckdb.sql(\"\"\"\n  SELECT region, SUM(amount)\n  FROM 'sales.parquet'\n  GROUP BY region\n\"\"\")",
        "SELECT region,\n       SUM(amount)\nFROM sales\nGROUP BY region;",
        "PivotTable:\n  Rows = Region\n  Values = SUM of Amount",
        "All three calculate total sales per region \u2014 the same result, just written in a different tool.",
        "DuckDB is SQL that runs on files. If you know SQL, you already know DuckDB \u2014 just point it at a Parquet file instead of a database table."
    ),

    f"{MOD05}/lesson11_parallel_processing.html": (
        "If you already use SQL\u2019s parallel query execution, or split Excel work across multiple workbooks, parallel processing in Python is the same strategy \u2014 divide work across multiple workers to finish faster.",
        [
            ("split work across workers", "fa6-solid:people-group",
             "Pool.map(func, chunks)", "Python distributes chunks of data to multiple worker processes.",
             "parallel query plan", "SQL\u2019s engine splits a query across multiple threads automatically.",
             "split across workbooks", "Excel users split data into multiple workbooks and process them separately."),
            ("choose processes vs threads", "fa6-solid:code-branch",
             "multiprocessing vs threading", "Python uses processes for CPU work and threads for I/O work.",
             "MAXDOP setting", "SQL controls how many CPU cores a query can use with the MAXDOP setting.",
             "no built-in option", "Excel does not offer a built-in parallel processing option."),
            ("collect results", "fa6-solid:object-group",
             "pool.map() returns list", "Python collects results from all workers into a single list.",
             "query returns full set", "SQL combines parallel thread results into a single result set.",
             "consolidate workbooks", "Excel copies results from multiple workbooks into one summary sheet."),
        ],
        "Same parallel sum across chunks, three tools",
        "from multiprocessing import Pool\ndef total(chunk):\n    return chunk['amount'].sum()\nwith Pool(4) as p:\n    results = p.map(total, chunks)\nprint(sum(results))",
        "-- SQL auto-parallelises\nSELECT SUM(amount)\nFROM big_table\nOPTION (MAXDOP 4);",
        "Split data into 4 files,\nSUM each, add totals\non summary sheet",
        "All three sum a large column using multiple workers \u2014 the same result, just written in a different tool.",
        "Parallel processing splits work to finish faster. SQL parallelises queries, Excel users split files, Python uses worker pools. Same strategy."
    ),

    f"{MOD05}/lesson12_dask_basics.html": (
        "If you already work with SQL views that only compute on demand, or use Excel Power Query\u2019s lazy loading, Dask applies the same principle \u2014 it records your operations and runs them only when you ask.",
        [
            ("lazy computation", "fa6-solid:lightbulb",
             "ddf = dask.dataframe.read_csv()", "Dask records the read but does not load data until you call <code class=\"font-mono\">.compute()</code>.",
             "CREATE VIEW", "SQL\u2019s view defines a query but does not run it until you SELECT from the view.",
             "Power Query steps", "Excel\u2019s Power Query records transformation steps and runs them on refresh."),
            ("partition data", "fa6-solid:puzzle-piece",
             "npartitions=4", "Dask splits a DataFrame into partitions that it processes in parallel.",
             "table partitioning", "SQL splits a large table into partitions for faster scans.",
             "split across sheets", "Excel users spread data across multiple worksheets for manageability."),
            ("trigger execution", "fa6-solid:play",
             ".compute()", "Dask runs all queued operations and returns the final result.",
             "SELECT FROM view", "SQL executes the view\u2019s query when you select from it.",
             "Refresh All", "Excel runs all Power Query steps when you click Refresh."),
        ],
        "Same lazy group-by, three tools",
        "import dask.dataframe as dd\nddf = dd.read_csv('big.csv')\nresult = (\n  ddf.groupby('region')\n     ['amount'].sum()\n     .compute()\n)",
        "CREATE VIEW v_totals AS\n  SELECT region,\n    SUM(amount) AS total\n  FROM big_table\n  GROUP BY region;\n\nSELECT * FROM v_totals;",
        "Power Query:\n  Source -> CSV\n  -> Group By Region\n  -> Sum Amount\n  -> Refresh to execute",
        "All three calculate total amount per region using deferred execution \u2014 the same result, just written in a different tool.",
        "Dask is lazy like SQL views and Power Query. It plans first, runs later. If you understand deferred execution, you understand Dask."
    ),

    f"{MOD05}/lesson13_performance_profiling.html": (
        "If you already check SQL query execution plans or watch Excel\u2019s calculation progress bar, performance profiling in Python is the same discipline \u2014 measure first, then optimise.",
        [
            ("measure execution time", "fa6-solid:stopwatch",
             "%timeit / time.time()", "Python times a block of code to see how many seconds it takes.",
             "SET STATISTICS TIME ON", "SQL reports how long a query took to execute.",
             "statusbar timer", "Excel shows a progress bar and clock while recalculating large sheets."),
            ("find the bottleneck", "fa6-solid:magnifying-glass",
             "cProfile / line_profiler", "Python profiles every function call to find the slowest one.",
             "EXPLAIN ANALYZE", "SQL\u2019s EXPLAIN shows which step in the query plan costs the most time.",
             "manual testing", "Excel users time individual formula ranges by commenting them out."),
            ("measure memory", "fa6-solid:microchip",
             "memory_profiler", "Python\u2019s memory_profiler tracks how much RAM each line allocates.",
             "sys.dm_exec_memory_grants", "SQL\u2019s DMVs show how much memory a query consumes.",
             "Task Manager", "Excel users check Task Manager to see how much RAM the workbook uses."),
        ],
        "Same query timing, three tools",
        "import time\nstart = time.time()\ndf = pd.read_csv('big.csv')\nelapsed = time.time() - start\nprint(f'{elapsed:.2f}s')",
        "SET STATISTICS TIME ON;\nSELECT *\nFROM big_table;\n-- CPU time: 1250 ms",
        "Open big.xlsx\n-> watch status bar\n-> note load time",
        "All three measure how long it takes to load a large dataset \u2014 the same result, just written in a different tool.",
        "Profiling answers the question \u201cwhere is my code slow?\u201d SQL uses execution plans, Excel uses the progress bar, Python uses profilers. Measure before optimising."
    ),

    f"{MOD05}/lesson14_real_large_data_project.html": (
        "If you already build end-to-end SQL ETL jobs or create multisheet Excel reporting workbooks, a real large-data project in Python combines every technique you have learned into one pipeline.",
        [
            ("plan the pipeline", "fa6-solid:clipboard-list",
             "design doc / notebook", "Python projects start with a plan listing data sources, transformations, and outputs.",
             "query design document", "SQL projects start with a list of tables, joins, and target schema.",
             "workbook layout sketch", "Excel projects start by sketching which sheets hold raw data and output."),
            ("ingest large files", "fa6-solid:truck-ramp-box",
             "read_parquet / chunked CSV", "Python ingests large files using Parquet or chunked CSV reads.",
             "BULK INSERT / COPY", "SQL loads large files using bulk import commands.",
             "Data \u2192 Get Data", "Excel imports large files using the Get Data wizard."),
            ("transform and aggregate", "fa6-solid:gears",
             "pandas / Polars / DuckDB", "Python transforms data using the best library for the scale.",
             "views + stored procedures", "SQL chains views and procedures to transform and aggregate.",
             "PivotTables + formulas", "Excel uses PivotTables and formulas to summarise data."),
            ("deliver results", "fa6-solid:truck-fast",
             "to_sql() / to_parquet()", "Python writes the final output to a database or export file.",
             "CREATE VIEW / export", "SQL exposes results as a view or exports them to a file.",
             "formatted report sheet", "Excel presents the final data on a polished report worksheet."),
        ],
        "Same end-to-end pipeline, three tools",
        "df = pd.read_parquet('raw.parquet')\ndf = df.dropna(subset=['id'])\ntotals = df.groupby('category')['amount'].sum()\ntotals.to_sql('summary', engine)",
        "INSERT INTO summary\nSELECT category,\n       SUM(amount)\nFROM raw_data\nWHERE id IS NOT NULL\nGROUP BY category;",
        "1. Import Parquet (Get Data)\n2. Filter blanks\n3. PivotTable by Category\n4. Copy to Report sheet",
        "All three build a complete pipeline from raw data to summary output \u2014 the same result, just written in a different tool.",
        "A large-data project combines every skill. SQL, Excel, and Python all follow the same plan-ingest-transform-deliver pattern."
    ),

    f"{MOD05}/lesson15_performance_best_practices.html": (
        "If you already tune SQL queries with indexes or keep Excel workbooks lean by removing unused formulas, performance best practices in Python follow the same principles \u2014 choose the right tool, avoid waste, and measure regularly.",
        [
            ("pick the right tool", "fa6-solid:toolbox",
             "pandas / Polars / DuckDB", "Python picks the library that matches the data size and operation.",
             "table vs view vs temp table", "SQL picks the storage method that best fits the query pattern.",
             "PivotTable vs formulas", "Excel picks PivotTables for summaries and formulas for row-level calcs."),
            ("avoid unnecessary copies", "fa6-solid:clone",
             "inplace / chained ops", "Python avoids creating extra DataFrame copies that waste memory.",
             "UPDATE vs SELECT INTO", "SQL updates in place instead of copying data to a new table.",
             "paste values", "Excel pastes as values to remove formula overhead."),
            ("read only what you need", "fa6-solid:scissors",
             "usecols / columns=", "Python reads only the columns needed from a file.",
             "SELECT col1, col2", "SQL selects only the columns required.",
             "delete unused columns", "Excel deletes columns that are unused in the analysis."),
            ("profile regularly", "fa6-solid:gauge-simple-high",
             "%timeit / memory_profiler", "Python profiles code periodically to catch performance regressions.",
             "EXPLAIN ANALYZE", "SQL reviews execution plans to spot slow queries.",
             "check file size + calc time", "Excel monitors workbook size and recalculation time."),
        ],
        "Same column-selective read, three tools",
        "df = pd.read_parquet(\n  'data.parquet',\n  columns=['id', 'amount']\n)",
        "SELECT id, amount\nFROM data;",
        "Open file -> delete all\ncolumns except ID and Amount",
        "All three load only the ID and amount columns \u2014 the same result, just written in a different tool.",
        "Best practices are universal: use the right tool, read only what you need, and measure your performance. SQL, Excel, and Python all benefit from the same habits."
    ),

    # ── MOD 06 — Automation and CI/CD ─────────────────────────────────────────

    f"{MOD06}/lesson01_devops_concepts_for_data_analytics.html": (
        "If you already back up SQL databases or save versioned Excel files, DevOps applies the same discipline \u2014 version your code, automate your tests, and deploy with confidence.",
        [
            ("version control", "fa6-solid:code-branch",
             "git commit / push", "Python stores every code change in a Git repository with a history trail.",
             "database backups / scripts", "SQL uses scripted backups or migration files to track schema changes.",
             "Save As v2, v3…", "Excel users save versioned copies of workbooks by appending a version number."),
            ("automated testing", "fa6-solid:vial",
             "pytest / assert", "Python runs automated tests that verify code works after every change.",
             "unit test sproc", "SQL tests stored procedures by running them with known inputs.",
             "manual spot-check", "Excel users manually verify formulas by checking sample cells."),
            ("continuous deployment", "fa6-solid:rocket",
             "CI/CD pipeline", "Python uses a CI/CD pipeline to test and deploy code automatically on every push.",
             "scheduled migration", "SQL applies database migrations on a release schedule.",
             "email the file", "Excel users email the updated workbook to stakeholders."),
        ],
        "Same code-test-deploy cycle, three tools",
        "# 1. Code\ngit commit -m 'fix etl'\n# 2. Test\npytest tests/\n# 3. Deploy\ngit push origin main\n# CI/CD runs automatically",
        "-- 1. Code\nALTER PROC etl_clean …\n-- 2. Test\nEXEC test_etl_clean;\n-- 3. Deploy\nEXEC sp_apply_migration;",
        "1. Edit workbook\n2. Spot-check formulas\n3. Save As v4\n4. Email to team",
        "All three follow the same code-test-deploy cycle \u2014 the same result, just written in a different tool.",
        "DevOps is version control + testing + deployment. SQL uses migration scripts, Excel uses manual versions, Python uses Git + CI/CD. Same discipline."
    ),

    f"{MOD06}/lesson02_gitlab_ci_cd_overview.html": (
        "If you already run SQL Agent jobs on a schedule, or manually test Excel workbooks before sharing them, GitLab CI/CD automates that same test-and-deploy workflow \u2014 triggered every time you push code.",
        [
            ("define the workflow", "fa6-solid:file-lines",
             ".gitlab-ci.yml", "Python defines CI/CD stages and jobs in a single YAML file.",
             "SQL Agent job steps", "SQL defines a sequence of steps inside a SQL Agent job.",
             "manual checklist", "Excel users follow a written checklist before distributing a workbook."),
            ("run tests automatically", "fa6-solid:play",
             "test stage", "Python\u2019s CI pipeline runs pytest automatically after every push.",
             "EXEC test_proc", "SQL runs a test procedure as a job step.",
             "open + verify", "Excel users open the file and manually verify formulas."),
            ("deploy on success", "fa6-solid:rocket",
             "deploy stage", "Python\u2019s CI pipeline deploys the code to production after tests pass.",
             "promote to production DB", "SQL promotes a tested script to the production database.",
             "email final version", "Excel users email the verified workbook to stakeholders."),
        ],
        "Same automated test run, three tools",
        "# .gitlab-ci.yml\ntest:\n  stage: test\n  script:\n    - pytest tests/ -v",
        "-- SQL Agent Job Step\nEXEC msdb.dbo.sp_add_jobstep\n  @step_name = 'run_tests',\n  @command = 'EXEC test_etl';",
        "1. Open workbook\n2. Check each formula\n3. If OK -> Save As final\n4. Email to team",
        "All three run a test step before the work is considered complete \u2014 the same result, just written in a different tool.",
        "CI/CD automates your test-and-deploy checklist. SQL uses Agent jobs, Excel uses manual checks, GitLab CI runs it all on every push."
    ),

    f"{MOD06}/lesson03_scheduling_data_jobs.html": (
        "If you already schedule SQL Agent jobs or set Excel to auto-refresh, scheduling Python data jobs is the same action \u2014 a timer runs your code at a fixed interval.",
        [
            ("time-based trigger", "fa6-solid:clock",
             "cron / systemd timer", "Python uses a system scheduler to run a script at set times.",
             "SQL Agent schedule", "SQL\u2019s Agent lets you pick the exact time and frequency for a job.",
             "auto-refresh interval", "Excel auto-refreshes data connections at a set minute interval."),
            ("event-based trigger", "fa6-solid:bell",
             "file watcher / webhook", "Python triggers a job when a new file appears or a webhook fires.",
             "DDL / DML trigger", "SQL fires a trigger automatically when data changes.",
             "on-open macro", "Excel runs a macro automatically when the workbook is opened."),
            ("log each run", "fa6-solid:scroll",
             "logging module", "Python writes a timestamped log entry for every scheduled run.",
             "job history table", "SQL Agent records each run\u2019s outcome in its history table.",
             "log worksheet", "Excel users log each refresh date and status on a dedicated sheet."),
        ],
        "Same daily scheduled job, three tools",
        "# crontab\n# 0 7 * * * python etl.py\nimport logging\nlogging.info('ETL started')\nrun_pipeline()\nlogging.info('ETL complete')",
        "-- SQL Agent Job\n-- Daily at 07:00\nEXEC run_etl;\nINSERT INTO job_log\n  VALUES (GETDATE(), 'OK');",
        "1. Connection Properties\n   -> Refresh every 1440 min\n2. Log date in Log sheet",
        "All three run a data job once per day and record the outcome \u2014 the same result, just written in a different tool.",
        "Scheduling is the same everywhere. SQL uses Agent, Excel uses refresh timers, Python uses cron. Same clock \u2014 different interface."
    ),

    f"{MOD06}/lesson05_deployment_workflow.html": (
        "If you already promote SQL scripts from dev to production, or share a final Excel workbook with stakeholders, a deployment workflow formalises those hand-off steps into a safe, repeatable process.",
        [
            ("development environment", "fa6-solid:laptop-code",
             "local / dev config", "Python runs and tests code locally using a development configuration.",
             "dev database", "SQL runs queries against a development database copy.",
             "draft workbook", "Excel users edit a draft copy of the workbook for development."),
            ("staging / test step", "fa6-solid:flask-vial",
             "staging deploy + tests", "Python deploys to a staging server and runs integration tests.",
             "staging database test", "SQL runs the migration against a staging database before production.",
             "review copy", "Excel users send a review copy to a colleague for checking."),
            ("production release", "fa6-solid:rocket",
             "CI/CD deploy to prod", "Python\u2019s CI pipeline deploys tested code to the production server.",
             "apply migration to prod", "SQL applies the approved migration script to the production database.",
             "distribute final file", "Excel users save the final workbook to a shared drive or email it."),
            ("rollback on failure", "fa6-solid:rotate-left",
             "revert commit / redeploy", "Python reverts to the previous commit and redeploys if production breaks.",
             "ROLLBACK migration", "SQL rolls back the migration to restore the previous database state.",
             "restore backup copy", "Excel users restore the previous version of the workbook from a backup."),
        ],
        "Same staging-to-production promotion, three tools",
        "# CI/CD stages\n# 1. test -> pytest\n# 2. staging -> deploy + smoke test\n# 3. prod -> deploy\ngit push origin main\n# pipeline runs automatically",
        "-- 1. Test on dev DB\nEXEC test_migration;\n-- 2. Apply to staging\nEXEC apply_migration @env='stg';\n-- 3. Apply to production\nEXEC apply_migration @env='prd';",
        "1. Edit draft workbook\n2. Send for review\n3. Save As FINAL\n4. Upload to shared drive",
        "All three promote work through dev, staging, and production stages \u2014 the same result, just written in a different tool.",
        "Deployment is the same everywhere: test in dev, verify in staging, release to production. SQL, Excel, and Python all follow this pattern."
    ),
}

# ── Main ──────────────────────────────────────────────────────────────────────
assert len(LESSONS) == 56, f"Expected 56 lessons, got {len(LESSONS)}"

ok = fail = 0
for rel, data in LESSONS.items():
    path = ROOT / rel
    if not path.exists():
        print(f"\u274c NOT FOUND  {rel}")
        fail += 1
        continue
    text = path.read_text(encoding="utf-8")
    intro, rows, divider, py, sql, xl, caption, tip = data
    new_sec = build_section(intro, rows, divider, py, sql, xl, caption, tip)
    new_text, n = PATTERN.subn(new_sec, text, count=1)
    if n == 0:
        print(f"\u274c NO MATCH   {rel}")
        fail += 1
        continue
    path.write_text(new_text, encoding="utf-8")
    print(f"\u2705 OK         {rel}")
    ok += 1

print(f"\n{ok}/{ok + fail} comparison sections rewritten")
