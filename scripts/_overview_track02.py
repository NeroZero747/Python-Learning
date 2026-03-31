#!/usr/bin/env python3
"""Rewrite #overview section body for all 28 track_02 lessons."""

import re, os, sys

ROOT = r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics"

# ── HTML builders ─────────────────────────────────────────────────────────────

def hook_banner(sentence):
    return f"""\
<div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
  <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
  <div class="relative flex items-center gap-4">
    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
      <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
    </span>
    <p class="text-base text-gray-800 leading-relaxed font-medium">{sentence}</p>
  </div>
</div>"""


def card_pink(icon, title, subtitle, desc):
    return f"""\
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
        <span class="iconify text-brand text-base" data-icon="fa6-solid:{icon}"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">{title}</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">{subtitle}</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">{desc}</p>
  </div>"""


def card_violet(icon, title, subtitle, desc):
    return f"""\
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-violet-50 shrink-0">
        <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:{icon}"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">{title}</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">{subtitle}</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">{desc}</p>
  </div>"""


def card_blue(icon, title, subtitle, desc):
    return f"""\
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-blue-50 shrink-0">
        <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:{icon}"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">{title}</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">{subtitle}</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">{desc}</p>
  </div>"""


def card_emerald(icon, title, subtitle, desc):
    return f"""\
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-50 shrink-0">
        <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:{icon}"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">{title}</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">{subtitle}</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">{desc}</p>
  </div>"""


def amber_tip(text):
    return f"""\
<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">{text}</p>
</div>"""


def build_body(hook, intro, c1, c2, c3, c4, tip):
    return "\n".join([
        hook_banner(hook),
        "",
        f'<p class="text-sm text-gray-600 leading-relaxed">{intro}</p>',
        "",
        '<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">',
        "",
        card_pink(*c1),
        "",
        card_violet(*c2),
        "",
        card_blue(*c3),
        "",
        card_emerald(*c4),
        "",
        "</div>",
        "",
        amber_tip(tip),
    ])


def build_section(body_html):
    return (
        '<section id="overview">\n'
        '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
        '        <span class="iconify text-white text-base" data-icon="fa6-solid:binoculars"></span>\n'
        '      </span>\n'
        '      <div class="min-w-0">\n'
        '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Overview</h2>\n'
        '        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A high-level summary of the topic</p>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="bg-white px-8 py-7 space-y-5">\n'
        + body_html + '\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )


# ── Lesson data ───────────────────────────────────────────────────────────────
# Each entry: hook, intro, (c1_pink, c2_violet, c3_blue, c4_emerald), tip
# Cards: (icon, title, subtitle ≤50 chars, desc ≤12 words—analogy-anchored, no definitions)

MOD01 = "mod_01_data_analysis_with_pandas"
MOD02 = "mod_02_working_with_data_sources"
MOD03 = "mod_03_python_for_analysts"
MOD04 = "mod_04_handling_large_data"

LESSONS = {

    # ── Module 01 ──────────────────────────────────────────────────────────────

    f"{MOD01}/lesson01_introduction_to_pandas.html": dict(
        hook="Pandas is the Python library that turns raw data files into structured tables you can filter, calculate, and summarise in code.",
        intro="Think of pandas as a programmable spreadsheet — instead of clicking menus, you type instructions that run instantly on any size of data.",
        c1=("table-cells",       "DataFrame",      "The spreadsheet — rows and columns in memory",       "The table pandas creates when it loads your data."),
        c2=("bars",              "Series",          "A single column — one strip of the spreadsheet",     "One column lifted out of the DataFrame."),
        c3=("cubes",             "Library",         "The extension pack — tools built into Python",        "A bundle of pre-written data tools you can use."),
        c4=("code",              "import pandas",   "The power button — starts the spreadsheet engine",    "One line that makes pandas available to use."),
        tip="If you already use Excel or SQL to analyse data, you already understand what pandas does — it just removes the manual clicking.",
    ),

    f"{MOD01}/lesson02_dataframes_explained.html": dict(
        hook="A DataFrame is a table that pandas holds in memory — rows of records, columns of fields — ready to query and transform with code.",
        intro="Think of a DataFrame like a database table — every row is one record, every column is one field, and Python is the query language you use.",
        c1=("grip-lines",        "Rows",            "Records — each row describes one thing",             "Each row holds all the fields for one entry."),
        c2=("table-list",        "Columns",         "Fields — each holds one type of value",              "Each column runs top to bottom with one kind of data."),
        c3=("bookmark",          "Index",           "The row ID — pandas assigns one per record",         "The address pandas uses to find any row instantly."),
        c4=("arrows-left-right", "Shape",           "The table size — rows and columns at a glance",      "How many records and fields the table holds."),
        tip="A pandas DataFrame stores data exactly like a SQL table — columns have types, rows are records, and you query it with code.",
    ),

    f"{MOD01}/lesson03_reading_data_csv_excel.html": dict(
        hook="Pandas can open a CSV or Excel file in one line of code and give you a structured table that is ready to filter and calculate.",
        intro="Think of pandas as a smart file-opener — you hand it a filename, it reads every row, names the columns, and returns a ready-to-use table.",
        c1=("file-arrow-down",   "read_csv()",      "The CSV door — opens flat files in one call",        "The function that turns a CSV file into a table."),
        c2=("file-lines",        "read_excel()",    "The workbook key — picks any sheet by name",         "The function that opens any sheet from an xlsx file."),
        c3=("eye",               "head()",          "The first look — shows the top five rows",           "The quick preview after the file is opened."),
        c4=("list",              "dtypes",          "The column label — shows what each column holds",    "The type report for every column in the table."),
        tip="You can open files too large for Excel — pandas handles tens of millions of rows without hitting a row limit.",
    ),

    f"{MOD01}/lesson04_selecting_columns.html": dict(
        hook="Selecting columns means telling pandas which fields to keep — like pulling only the drawers you need from a filing cabinet.",
        intro="Think of a DataFrame as a filing cabinet — each column is a labelled drawer, and selecting means pulling only the drawers your analysis needs.",
        c1=("hand-pointer",      "Single column",   "One drawer — grabs one strip of values",             "The one column you pull by typing its name."),
        c2=("layer-group",       "Multiple columns","A handful of drawers — all the ones you named",      "The subset of columns returned as a new table."),
        c3=("pen",               "rename()",        "The relabeller — swaps a drawer's name tag",         "The method that replaces cryptic column names."),
        c4=("list",              "columns attribute","The index card — lists every drawer name",           "The full list of column names in the cabinet."),
        tip="Selecting only the columns you need before any calculation makes your script faster and easier to read.",
    ),

    f"{MOD01}/lesson05_filtering_rows.html": dict(
        hook="Filtering rows keeps only the records that match a rule — the same idea as a WHERE clause in SQL or AutoFilter in Excel.",
        intro="Think of filtering like a postal sorter — you set a rule, and only the matching envelopes pass through; everything else is set aside.",
        c1=("filter",            "Boolean condition","The address check — keeps matching rows only",       "Envelopes that passed the rule travel forward."),
        c2=("list-check",        "isin()",           "The approved list — rows must appear on it",        "Envelopes forwarded only if the address is listed."),
        c3=("code-branch",       "& / | operators",  "The dual rule — two checks applied at once",        "Envelopes sorted by two rules in a single pass."),
        c4=("circle-xmark",      "dropna()",         "The blank-envelope filter — removes null rows",     "Envelopes with no address thrown out of the pile."),
        tip="The same filtering logic you write in SQL WHERE clauses translates directly to pandas — same operators, same behaviour.",
    ),

    f"{MOD01}/lesson06_creating_calculated_columns.html": dict(
        hook="Adding a calculated column means computing a new value from your existing data — exactly like typing a formula in an Excel column.",
        intro="Think of calculated columns like Excel formulas — you write the calculation once, and it fills every row automatically without any dragging.",
        c1=("calculator",        "Column assignment","The formula bar — writes the new column in",         "The new column appears on the right of the sheet."),
        c2=("percent",           "Arithmetic ops",   "The formula symbols — run across every row",         "The same operators you use in any spreadsheet formula."),
        c3=("sliders",           "Conditional values","The IF formula — different result per condition",   "Two possible values assigned based on a row rule."),
        c4=("trash",             "drop()",           "The delete column — removes it for good",            "The unwanted column erased from the spreadsheet."),
        tip="Unlike Excel, a pandas calculated column never breaks when you add rows — the formula recalculates the whole DataFrame at once.",
    ),

    f"{MOD01}/lesson07_aggregations_group_by.html": dict(
        hook="Aggregating data means rolling up many rows into summary numbers — totals, averages, and counts — grouped by a shared category.",
        intro="Think of groupby like an accountant's summary ledger — you split rows by department, then add one subtotal line for each group.",
        c1=("object-group",      "groupby()",        "The tab divider — splits rows into groups",          "Each category gets its own section in the ledger."),
        c2=("chart-column",      "sum / mean / count","The subtotal row — one number per group",           "The aggregated value that represents each section."),
        c3=("sliders",           "agg()",            "The multi-column total — several at once",           "Multiple calculations run on each group together."),
        c4=("rotate",            "reset_index()",    "The ledger flatten — groups become plain rows",      "The grouped result turned back into a normal table."),
        tip="groupby in pandas mirrors SQL GROUP BY exactly — any aggregate you write in SQL you can replicate here in one line.",
    ),

    f"{MOD01}/lesson08_joining_data_merge.html": dict(
        hook="Merging combines two tables into one by matching rows that share the same key value — identical to a SQL JOIN.",
        intro="Think of merge like matching receipts to invoices — both share an invoice number, so you staple the matching pairs together into one document.",
        c1=("arrows-left-right", "merge()",          "The stapler — joins two tables on a shared key",    "Two tables snapped together where their key matches."),
        c2=("scale-balanced",    "Join type (how=)", "The matching rule — what to do with no match",      "Whether unmatched rows are kept or discarded."),
        c3=("key",               "Join key columns", "The invoice number — the column used to match",     "The column that identifies matching rows."),
        c4=("circle-question",   "Unmatched rows",   "The orphan receipt — no match in the other pile",   "A row with no partner in the other table."),
        tip="The four join types — inner, left, right, outer — work identically to SQL; pick the same one you would use in a query.",
    ),

    f"{MOD01}/lesson09_handling_missing_data.html": dict(
        hook="Missing data is a gap in your table where no value was recorded — and pandas gives you tools to find, remove, or fill those gaps.",
        intro="Think of missing data like blank answers on a survey form — you can discard the form, skip the blank, or estimate a reasonable answer.",
        c1=("circle-question",   "isnull()",         "The blank-field scanner — marks every empty cell", "Which survey fields were left unanswered."),
        c2=("minus",             "dropna()",         "The discard pile — removes forms with blanks",      "Forms thrown out because of one empty field."),
        c3=("fill",              "fillna()",         "The best-guess pen — writes into every blank",      "A replacement value written into each empty cell."),
        c4=("brain",             "Imputation strategy","The estimation rule — how to pick the fill value", "The logic used to choose what value to write in."),
        tip="One missing value in a numeric column turns the entire column's sum to NaN — always check for nulls before aggregating.",
    ),

    f"{MOD01}/lesson10_exporting_data.html": dict(
        hook="Exporting sends your cleaned, transformed DataFrame back to a file — a CSV anyone can open or an Excel workbook with multiple sheets.",
        intro="Think of exporting like printing a finished report — your analysis is done, so you choose the format and deliver it to whoever needs it.",
        c1=("download",          "to_csv()",         "The plain-text print — saves every row as CSV",     "The finished report printed as a comma-separated file."),
        c2=("file-lines",        "to_excel()",       "The spreadsheet print — creates an xlsx file",      "The report delivered as a formatted Excel workbook."),
        c3=("table-cells-large", "ExcelWriter",      "The multi-sheet print — several tabs at once",      "Multiple DataFrames printed to named sheets in one file."),
        c4=("sliders",           "index parameter",  "The row-number switch — include or exclude it",     "The setting that controls whether row numbers appear."),
        tip="Set the index parameter to False almost every time — the row number column pandas adds by default is rarely expected.",
    ),

    # ── Module 02 ──────────────────────────────────────────────────────────────

    f"{MOD02}/lesson01_reading_csv_files.html": dict(
        hook="Not all CSV files use the same delimiter, encoding, or column structure — and pandas gives you a parameter for every variation.",
        intro="Think of loading a CSV like translating a foreign-dialect document — the words are familiar but you have to specify the local rules before Python can read it cleanly.",
        c1=("gear",              "sep parameter",    "The dialect rule — which character splits values",   "The separator your translator uses to parse the text."),
        c2=("filter",            "usecols",          "The page selector — loads only named columns",      "Only the columns from the glossary are translated."),
        c3=("language",          "encoding",         "The character set — handles non-ASCII text",         "The alphabet rule for accented or special characters."),
        c4=("tags",              "dtype on load",    "The type label — assigns types before reading",     "Column types set before translation even begins."),
        tip="Specifying dtype and usecols at load time is far faster than converting columns after — especially on files with millions of rows.",
    ),

    f"{MOD02}/lesson02_working_with_json_files.html": dict(
        hook="JSON is the format web APIs speak — and pandas can turn a JSON response into a structured table with a single function call.",
        intro="Think of JSON like a structured form that arrived as a text message — the data is all there, but you have to unfold the nested layers to see the table.",
        c1=("code",              "read_json()",      "The form reader — loads flat JSON directly",         "A flat JSON file opened straight into a DataFrame."),
        c2=("diagram-project",   "json_normalize()","The layer unfolder — flattens nested objects",       "Nested keys unpacked into separate flat columns."),
        c3=("upload",            "to_json()",        "The form serialiser — converts back to JSON",       "The DataFrame converted back to JSON text."),
        c4=("sitemap",           "JSON structure types","The message shapes — arrays vs nested objects",   "Different layouts need different unpacking rules."),
        tip="Most REST APIs return JSON — once you can load and normalise a response, you can pull live data from any web service into pandas.",
    ),

    f"{MOD02}/lesson03_connecting_to_databases.html": dict(
        hook="A database connection lets Python talk directly to a live database — no CSV export needed.",
        intro="Think of a database connection like a phone call — you dial the number (connection string), ask your question (query), get the answer (DataFrame), then hang up.",
        c1=("plug",              "Connection string","The phone number — address and login details",       "The URL that tells Python where the database lives."),
        c2=("link",              "SQLAlchemy engine","The phone handset — manages the connection",        "The Python object that opens and holds the line."),
        c3=("table",             "read_sql_table()", "The question — loads a full table as a DataFrame",  "One table from the database fetched in a single call."),
        c4=("circle-check",      "close()",          "The hang-up — releases the connection cleanly",     "The call ended so the database stops waiting."),
        tip="SQLAlchemy supports PostgreSQL, MySQL, SQL Server, and SQLite — the same connection code works across all of them.",
    ),

    f"{MOD02}/lesson04_running_sql_in_python.html": dict(
        hook="Running SQL from Python lets you filter and join data in the database first — before any results load into pandas.",
        intro="Think of running SQL like placing a restaurant order instead of using the buffet — you tell the kitchen exactly what you want, and they bring it ready to eat.",
        c1=("database",          "read_sql()",       "The order ticket — sends SELECT, returns rows",     "The kitchen brings exactly what your query asked for."),
        c2=("shield",            "Parameterised query","The custom order — filter values passed safely",  "Your rule applied without rewriting the query each time."),
        c3=("folder",            "Organised queries","The menu book — named SQL strings in the script",   "Each query stored by name so the script stays readable."),
        c4=("stopwatch",         "Query profiling",  "The kitchen timer — how long each dish takes",     "How long each SQL round-trip takes to return results."),
        tip="Running a WHERE clause in the database is far faster than loading the whole table and filtering in pandas — push filtering into SQL.",
    ),

    f"{MOD02}/lesson05_writing_data_back_to_a_database.html": dict(
        hook="Pushing a DataFrame to a database table completes the data pipeline — the cleaned result goes back where applications can use it.",
        intro="Think of writing to a database like returning finished goods to a warehouse — you took raw stock, processed it, and now ship the finished product back to the shelf.",
        c1=("upload",            "to_sql()",         "The dispatch truck — pushes rows into a table",     "The finished DataFrame delivered to the warehouse shelf."),
        c2=("sliders",           "if_exists modes",  "The delivery instruction — replace or append",      "The rule for what to do when the table already exists."),
        c3=("table",             "Auto schema",      "The empty shelf — table created if not there yet",  "The table built from scratch if the shelf is empty."),
        c4=("wrench",            "dtype casting",    "The packaging check — columns match the shelf",     "Column types converted to match the database's expectation."),
        tip="Check row counts before and after writing — a silent type mismatch can truncate string data without raising any error.",
    ),

    f"{MOD02}/lesson06_managing_credentials_env.html": dict(
        hook="A .env file stores passwords and API keys outside your code — so you can share a script without accidentally sharing your secrets.",
        intro="Think of a .env file like a lock box beside your door — your key (password) lives there safely, and your script knows to look for it there.",
        c1=("lock",              "Hard-coding risk", "The code on the door — visible to anyone",          "Your password readable by anyone who sees the script."),
        c2=("file-lines",        ".env file",        "The lock box — secrets stored outside the code",    "Passwords kept in a separate file the script reads."),
        c3=("gear",              "python-dotenv",    "The lock box reader — loads .env into Python",      "The library that reads the lock box at script startup."),
        c4=("shield",            ".gitignore",       "The do-not-copy rule — never uploaded to Git",      "The instruction that keeps the lock box out of repos."),
        tip="Even a private repository can become public — any hard-coded credential you commit today could be exposed tomorrow.",
    ),

    # ── Module 03 ──────────────────────────────────────────────────────────────

    f"{MOD03}/lesson01_why_analysts_use_python.html": dict(
        hook="Python automates the repetitive work that Excel forces you to do by hand — and it scales to data volumes that Excel cannot handle.",
        intro="Think of Python like upgrading from a hand calculator to a programmable one — the same calculations run, but you write the formula once and it handles any size of input.",
        c1=("rotate",            "Automation",       "The repeat button — runs the same steps again",     "Your weekly task completed without any manual work."),
        c2=("bolt",              "Scale",            "The bigger input — handles any dataset size",       "The million-row file your calculator processes easily."),
        c3=("list-check",        "Reproducibility",  "The saved formula — runs identically every time",   "The exact same steps applied to every new dataset."),
        c4=("cubes",             "Ecosystem",        "The extension pack — analytics tools built in",     "Charts, SQL queries, and machine learning all in one language."),
        tip="If a task in Excel takes more than ten clicks and you repeat it weekly, a short Python script can replace it with a double-click.",
    ),

    f"{MOD03}/lesson02_replacing_excel_workflows_with_python.html": dict(
        hook="Almost every Excel formula, filter, and pivot table has a direct pandas equivalent — and the pandas version scales to any file size.",
        intro="Think of moving from Excel to pandas like swapping a hand saw for a power saw — you cut the same wood, but the power tool handles any thickness without losing speed.",
        c1=("arrows-left-right", "merge() as VLOOKUP","The lookup swap — no formula dragged down",        "The lookup that matches rows without a formula column."),
        c2=("table-cells-large", "groupby() as pivot","The summary engine — same totals, one line",       "The group total that replaces a full pivot table."),
        c3=("file-lines",        "ExcelWriter",      "The tab builder — each result on its own sheet",    "Multiple summaries written to one Excel file automatically."),
        c4=("rotate",            "Folder loop",      "The autopilot — opens every file in sequence",      "Each file in a folder processed without opening it manually."),
        tip="Any Excel workflow you can describe in plain steps can be translated to Python — the structure maps one-to-one.",
    ),

    f"{MOD03}/lesson03_using_python_with_sql_queries.html": dict(
        hook="Running SQL from inside a Python script lets you filter at the database — then use pandas for the work that SQL cannot do easily.",
        intro="Think of Python as a bilingual translator — it speaks SQL when talking to the database, then switches to pandas when reshaping or enriching the results.",
        c1=("database",          "Parameterised SQL","The template — filter values swapped in safely",    "The query that accepts new values without being rewritten."),
        c2=("layer-group",       "read_sql() result","The bridge — query result carried to pandas",       "The database answer delivered straight into a DataFrame."),
        c3=("folder",            "Organised queries","The phrase book — named queries in the script",     "SQL strings stored by name so the script stays clean."),
        c4=("stopwatch",         "Query profiling",  "The translation timer — measures each call",        "How long each SQL round-trip takes to complete."),
        tip="Write WHERE, GROUP BY, and JOIN in SQL — filters run faster in the database engine than in pandas on the same data.",
    ),

    f"{MOD03}/lesson04_automating_repetitive_data_tasks.html": dict(
        hook="Automation means writing a script once and having Python repeat it — on any schedule, across any number of files, without your involvement.",
        intro="Think of automation like setting a washing machine — you load the clothes (data), set the programme (script), and press start, then the machine handles everything.",
        c1=("magnifying-glass",  "Task selection",   "Loading the machine — choosing what to automate",   "The weekly task worth handing over to the script."),
        c2=("rotate",            "File loop",        "The drum cycle — processes each file in turn",      "Each file in the folder handled one by one."),
        c3=("clock",             "Scheduling",       "The timer dial — starts the machine on time",       "The script set to run at a chosen date and hour."),
        c4=("list",              "Logging",          "The cycle report — records what ran and when",      "A timestamped log written after each completed run."),
        tip="Start with the task you repeat most often — even a ten-minute weekly routine saved by automation frees up eight hours a year.",
    ),

    f"{MOD03}/lesson05_building_a_simple_reporting_script.html": dict(
        hook="A reporting script loads data, transforms it, and writes the result to a file — all in one run, with no manual steps in between.",
        intro="Think of a reporting script like an assembly line — raw data enters at one end, each station cleans or transforms it, and a formatted report exits the other end.",
        c1=("sitemap",           "Script structure", "The line layout — clear sections in sequence",      "Load, transform, and export in a clean order."),
        c2=("pen",               "Number formatting","The quality station — consistent labels applied",   "Dates and numbers made uniform before leaving the line."),
        c3=("file-lines",        "ExcelWriter",      "The packaging machine — wraps results in tabs",     "Each summary tidied into its own named sheet."),
        c4=("chart-bar",         "Summary statistics","The QC readout — totals at the top of the report", "Totals and averages placed where readers look first."),
        tip="A well-structured script adapts to a new dataset in under a minute — name your sections and output columns clearly from the start.",
    ),

    f"{MOD03}/lesson06_automating_reports_end_to_end.html": dict(
        hook="An end-to-end pipeline connects every step — load, clean, transform, export, and deliver — so the whole process runs without any human input.",
        intro="Think of an end-to-end pipeline like a fully automated factory — raw data arrives on the conveyor, each station does its job, and a finished report exits at the end.",
        c1=("link",              "Chained steps",    "The conveyor belt — connects all stations",          "Each stage hands its output to the next automatically."),
        c2=("shield",            "Error handling",   "The safety shutoff — stops the line cleanly",       "A broken station stops the run and writes what failed."),
        c3=("envelope",          "Email delivery",   "The shipping dock — sends the report out",           "The finished report dispatched to the right inbox."),
        c4=("clock",             "Scheduling + logging","The shift clock — records every run",             "The script runs on time and writes proof it completed."),
        tip="Add try-except around every external call — file reads, database queries, and email sends are the steps most likely to fail.",
    ),

    # ── Module 04 ──────────────────────────────────────────────────────────────

    f"{MOD04}/lesson02_memory_optimization.html": dict(
        hook="Memory optimisation means making a DataFrame use less RAM — by choosing smaller data types for each column.",
        intro="Think of memory optimisation like packing a suitcase efficiently — pandas loads everything in the largest size by default, but most values fit just as well in a much smaller one.",
        c1=("memory",            "Default 64-bit types","The oversize packing — everything in XL",        "Every column packed in the largest container by default."),
        c2=("magnifying-glass",  "memory_usage()",   "The luggage scale — weighs each column",            "Each column weighed so you know where to cut first."),
        c3=("compress",          "Downcasting",      "The repack — fits values into a smaller size",      "Integer and float columns switched to a smaller type."),
        c4=("tags",              "Categorical type", "The shared hanger — repeated strings stored once",  "One copy stored for all repeated values in the column."),
        tip="Converting one large string column to categorical on a million-row DataFrame can cut that column's memory use by 80% or more.",
    ),

    f"{MOD04}/lesson03_chunk_processing.html": dict(
        hook="Chunk processing reads a file in pieces — so Python only ever holds one piece in memory at a time, no matter how large the file is.",
        intro="Think of chunk processing like reading a very long book one chapter at a time — you only hold one chapter, process what you learned, then move to the next.",
        c1=("triangle-exclamation","Memory limit",   "The too-heavy book — too big to hold in RAM",       "The whole file too large to load in one go."),
        c2=("layer-group",       "chunksize parameter","The chapter length — rows handed over at a time", "How many rows pandas delivers in each reading session."),
        c3=("rotate",            "Chunk loop",       "The reading session — one chapter processed",       "Each chunk handled, then set aside for the next."),
        c4=("object-group",      "Collecting results","The reading notes — summaries gathered per chunk",  "Partial results from each chunk assembled at the end."),
        tip="A chunk loop takes slightly longer than loading the whole file — use it only when the file is too large to fit in RAM.",
    ),

    f"{MOD04}/lesson04_processing_millions_of_rows.html": dict(
        hook="Operations that feel instant on small data can take minutes on millions of rows — the key is avoiding Python for-loops.",
        intro="Think of vectorised operations like a printing press — instead of addressing one envelope at a time (a for-loop), you stamp every address in a single pass.",
        c1=("hand-pointer",      "For-loop slowness","The hand-addressing — one envelope at a time",      "Each row processed individually in slow Python code."),
        c2=("bolt",              "Vectorised ops",   "The printing press — all rows stamped at once",     "The whole column processed by compiled C code."),
        c3=("gear",              "apply()",          "The semi-manual press — custom function per row",   "A Python function run row-by-row when no vector exists."),
        c4=("stopwatch",         "Benchmarking",     "The stop-watch test — times every step taken",     "How long each operation actually takes to complete."),
        tip="Replacing a for-loop with a vectorised pandas operation can make the same calculation 100 times faster on a large dataset.",
    ),

    f"{MOD04}/lesson05_columnar_storage.html": dict(
        hook="Columnar storage keeps all values of one column together on disk — so a query reads only the columns it needs, not every field in every row.",
        intro="Think of columnar storage like a library sorted by genre on dedicated shelves — to find all science fiction, you walk to one shelf rather than checking every aisle.",
        c1=("bars",              "Row-based layout", "The aisle-by-aisle walk — every row together",      "All fields scanned even when you only need one column."),
        c2=("database",          "Columnar layout",  "The genre shelf — all values of one column",        "Only the requested shelf is read; the rest are skipped."),
        c3=("compress",          "Column compression","The shelf organiser — identical values grouped",    "Similar values stored together compress far more tightly."),
        c4=("file-lines",        "Parquet and ORC",  "The catalogued shelves — readable by Python",       "Columnar formats pandas reads natively for fast queries."),
        tip="An analytics query on a Parquet file reads only the columns in your code — the rest of the file is never touched on disk.",
    ),

    f"{MOD04}/lesson06_parquet_files.html": dict(
        hook="Parquet is a binary file format built for analytics — smaller than CSV, faster to read, and it preserves the data type of every column.",
        intro="Think of Parquet like replacing a handwritten card catalogue with a barcode scanner — the same data, but scanned in a fraction of the time and never misread.",
        c1=("file-lines",        "Parquet format",   "The barcode system — binary, dense, fast",           "The file format designed for efficient column reads."),
        c2=("download",          "to_parquet()",     "The barcode print — encodes as a compact file",     "The DataFrame saved in the compressed binary format."),
        c3=("filter",            "read_parquet()",   "The barcode read — loads only named columns",       "Only the requested columns pulled from the file."),
        c4=("scale-balanced",    "Parquet vs CSV",   "The old card vs the scanner — smaller, faster",     "The same dataset, smaller file, and faster to open."),
        tip="Switch intermediate working files from CSV to Parquet — they load ten times faster and take up half the disk space.",
    ),

    f"{MOD04}/lesson13_performance_profiling.html": dict(
        hook="Profiling measures where your script spends its time — so you fix the actual slow step instead of guessing and optimising the wrong one.",
        intro="Think of profiling like a factory time-and-motion study — you observe every workstation before deciding where to invest improvements, so you fix the real bottleneck.",
        c1=("stopwatch",         "Timing with time", "The stopwatch — measures each step in seconds",     "How long each part of the script takes to run."),
        c2=("gauge-high",        "cProfile",         "The full audit — every function call ranked",       "All function calls measured and sorted by total time."),
        c3=("magnifying-glass",  "line_profiler",    "The microscope — shows which lines are slow",       "Individual lines inside each function timed precisely."),
        c4=("list-check",        "Documenting fixes","The improvement log — before and after recorded",   "Timings compared before and after each change."),
        tip="Profile before you optimise — the slowest-looking line of code is almost never the actual bottleneck in a real pipeline.",
    ),
}

# ── Regex: match the full #overview section ────────────────────────────────────

PATTERN = re.compile(r'<section id="overview">.*?</section>', re.DOTALL)

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

    body = build_body(d["hook"], d["intro"], d["c1"], d["c2"], d["c3"], d["c4"], d["tip"])
    new_section = build_section(body)
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
