#!/usr/bin/env python3
"""Rewrite #comparison section for all 28 track_02 lessons."""

import re, os, sys

ROOT = r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics"
PATTERN = re.compile(r'<section id="comparison">.*?</section>', re.DOTALL)

MOD01 = "mod_01_data_analysis_with_pandas"
MOD02 = "mod_02_working_with_data_sources"
MOD03 = "mod_03_python_for_analysts"
MOD04 = "mod_04_handling_large_data"


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
# rows: list of (label, icon, py_term, py_desc, sql_term, sql_desc, xl_term, xl_desc)
# descriptions may contain safe inline HTML (e.g. <code class="font-mono">...</code>)
# code strings are raw — he() handles encoding at render time

LESSONS = {

    # ── MOD 01 ────────────────────────────────────────────────────────────────

    f"{MOD01}/lesson01_introduction_to_pandas.html": (
        "If you already query tables in SQL or organise data in Excel, pandas does the same things in Python — you load data, filter rows, calculate totals, and export results, all inside a single script.",
        [
            ("a table of data", "fa6-solid:table",
             "DataFrame", "The in-memory table of rows and columns that pandas loads your data into.",
             "table", "A named collection of rows and columns stored inside a database.",
             "worksheet", "The rows-and-columns grid you work with inside an Excel workbook."),
            ("one column", "fa6-solid:grip-vertical",
             "Series", "A single column extracted from a DataFrame, with an index label beside every value.",
             "column", "A named field in a SELECT list that returns one value per row.",
             "column range", "A lettered column — such as A or B — that holds one field of data per row."),
            ("loading a file", "fa6-solid:file-arrow-down",
             "pd.read_csv()", "Reads a CSV file from your drive into a DataFrame in one line of code.",
             "LOAD / IMPORT", "A database command that reads an external file into a table.",
             "Data → Get Data", "The Excel ribbon option for importing a CSV file into a worksheet."),
            ("a quick preview", "fa6-solid:eye",
             "df.head()", "Returns the first five rows of the DataFrame so you can verify it loaded correctly.",
             "SELECT … LIMIT 5", "Returns the first five rows from a table or query result set.",
             "visible top rows", "The rows shown at the top of the worksheet when you first open the file."),
        ],
        "Same sales file, three tools",
        "df = pd.read_csv('sales.csv')\nprint(df.head())",
        "SELECT *\nFROM sales\nLIMIT 5;",
        "Data -> Get Data -> From Text/CSV\n-> select sales.csv -> Load",
        "All three load and display the first rows of the same sales file — the same result, just written in a different tool.",
        "Pandas is another way to express ideas you already know from SQL and Excel. Your knowledge of tables, columns, and rows transfers directly."
    ),

    f"{MOD01}/lesson02_dataframes_explained.html": (
        "If you already work with database tables or Excel grids, a DataFrame is exactly that — a rectangular table of rows and columns that pandas holds in Python memory and lets you work with using code.",
        [
            ("the full table", "fa6-solid:table",
             "DataFrame", "The complete in-memory table that holds all rows and columns of your loaded data.",
             "result set", "All rows returned by a SELECT query from a database table.",
             "sheet range", "The rectangular block of data spanning rows and columns in a worksheet."),
            ("column types", "fa6-solid:tag",
             "df.dtypes", "Lists the data type of each column — int64, float64, object, bool, or datetime.",
             "column type", "The type declared for a database column — INT, VARCHAR, DATE, or DECIMAL.",
             "cell format", "The format applied to a column in Excel — Number, Text, Date, or General."),
            ("dimensions", "fa6-solid:ruler-combined",
             "df.shape", "Returns a (rows, columns) tuple showing the exact size of the DataFrame.",
             "COUNT(*)", "An aggregate that counts the total number of rows in a table or query result.",
             "ROWS()", "An Excel function that counts the rows in a selected range of cells."),
            ("column names", "fa6-solid:list",
             "df.columns", "Returns the name of every column in the DataFrame as an index object.",
             "INFORMATION_SCHEMA", "The system view that lists every column name and type for a given table.",
             "header row", "The text labels in row 1 of your spreadsheet that name each column."),
        ],
        "Same employee table, three tools",
        "df = pd.read_csv('employees.csv')\nprint(df.shape)\nprint(df.dtypes)",
        "SELECT COUNT(*) AS total_rows\nFROM employees;",
        "=ROWS(A2:A201)    -- row count\n=COLUMNS(A1:E1)  -- column count",
        "All three inspect the dimensions and types of the same employee table — the same result, just written in a different tool.",
        "A DataFrame is a table with a Python name. Every property — shape, dtypes, columns — has a direct SQL or Excel equivalent you already understand."
    ),

    f"{MOD01}/lesson03_reading_data_csv_excel.html": (
        "If you already import CSV files via the Excel Data ribbon or load tables with a SQL LOAD command, <code class=\"font-mono\">pd.read_csv()</code> and <code class=\"font-mono\">pd.read_excel()</code> do the same thing — they pull external files into a pandas table you can work with in Python.",
        [
            ("read a csv file", "fa6-solid:file-arrow-down",
             "pd.read_csv()", "Opens a CSV file from disk and returns a full DataFrame in one line.",
             "LOAD DATA INFILE", "A MySQL command that reads a CSV file into a database table.",
             "Data → Get Data", "The Excel ribbon command that imports a CSV into a worksheet."),
            ("read an excel file", "fa6-solid:file-lines",
             "pd.read_excel()", "Opens any sheet from an xlsx file, using the sheet name or index number.",
             "n/a", "SQL databases don't read Excel directly — files must first be exported to CSV.",
             "double-click open", "Opening an xlsx file in Excel is the manual equivalent of pd.read_excel()."),
            ("pick a sheet", "fa6-solid:layer-group",
             "sheet_name=", "The parameter that tells <code class=\"font-mono\">pd.read_excel()</code> which worksheet to load.",
             "n/a", "SQL has no built-in concept of worksheets — a CSV or table has no sheet tabs.",
             "sheet tab", "The named tab at the bottom of an Excel workbook that selects a worksheet."),
            ("preview rows", "fa6-solid:eye",
             "df.head()", "Returns the first five rows so you can confirm the file loaded correctly.",
             "SELECT … LIMIT 5", "Returns the first five rows of a table to verify the data loaded correctly.",
             "Ctrl+Home", "Pressing Ctrl+Home in Excel takes you to cell A1 to see the first rows."),
        ],
        "Same CSV file, three tools",
        "df = pd.read_csv('orders.csv')\nprint(df.head())",
        "LOAD DATA INFILE 'orders.csv'\nINTO TABLE orders;",
        "Data -> Get Data -> From Text/CSV\n-> orders.csv -> Load",
        "All three import the same CSV file into a tabular structure ready for analysis — the same result, just written in a different tool.",
        "Whether you use pd.read_csv(), a SQL LOAD command, or the Excel data ribbon, you are doing the same thing — turning a flat file into a queryable table."
    ),

    f"{MOD01}/lesson04_selecting_columns.html": (
        "If you already pick specific columns in a SQL SELECT or hide unwanted columns in Excel, selecting columns in pandas works the same way — you name the columns you want and get back only those fields.",
        [
            ("one column", "fa6-solid:grip-vertical",
             "df[\"col\"]", "Selects one column by name and returns it as a Series.",
             "SELECT col", "Names a single column in a SELECT clause to return only that field.",
             "single column", "Clicking a column letter in Excel to select all values in that column."),
            ("multiple columns", "fa6-solid:table-columns",
             "df[[\"a\",\"b\"]]", "Passes a list of names inside double brackets to select multiple columns.",
             "SELECT a, b", "Lists two or more column names in a SELECT clause.",
             "Ctrl+click columns", "Holding Ctrl and clicking column letters in Excel to select multiple columns."),
            ("rename a column", "fa6-solid:pen",
             "rename()", "Replaces existing column names with new labels using a dictionary mapping.",
             "AS alias", "Renames a column in query output using an alias after the AS keyword.",
             "header cell edit", "Double-clicking a header cell in row 1 to rename the column."),
            ("list all columns", "fa6-solid:list",
             "df.columns", "Returns the names of every column in the DataFrame.",
             "INFORMATION_SCHEMA", "The system view that lists every column name in a given database table.",
             "row 1 headers", "The text labels in row 1 of your spreadsheet that name every column."),
        ],
        "Same column selection, three tools",
        "df[[\"product\", \"revenue\"]].head()",
        "SELECT product, revenue\nFROM sales\nLIMIT 5;",
        "=Table1[product]   -- structured ref\n=Table1[revenue]",
        "All three select only the product and revenue columns from the same sales data — the same result, just written in a different tool.",
        "Selecting columns in pandas is just like writing a SELECT list in SQL or clicking columns in Excel — you name what you want and ignore the rest."
    ),

    f"{MOD01}/lesson05_filtering_rows.html": (
        "If you already filter rows with a SQL WHERE clause or use AutoFilter in Excel, pandas boolean filtering does the same thing — you define a condition and keep only the rows that match.",
        [
            ("one condition", "fa6-solid:filter",
             "boolean mask", "A True/False Series that selects only the rows where the condition is met.",
             "WHERE clause", "The SQL filter applied to a query to keep only rows that meet a condition.",
             "AutoFilter", "The dropdown filter on a column header that shows only matching rows."),
            ("combine conditions", "fa6-solid:code-branch",
             "& and |", "The <code class=\"font-mono\">&</code> operator requires both conditions; <code class=\"font-mono\">|</code> requires either one to be true.",
             "AND / OR", "AND requires both conditions to be true; OR requires either condition to be true.",
             "AND() / OR()", "Excel functions that combine multiple conditions inside a formula."),
            ("match a list", "fa6-solid:list-check",
             "isin()", "Keeps rows where the column value appears in a list you supply.",
             "IN (...)", "Returns rows where a column value matches any value in the given list.",
             "AutoFilter multi-select", "The checkbox list in Excel AutoFilter that lets you select specific values to display."),
            ("remove nulls", "fa6-solid:ban",
             "dropna()", "Removes every row that has at least one missing (NaN) value.",
             "WHERE col IS NOT NULL", "Filters out rows where a column contains a NULL database value.",
             "Filter → uncheck Blanks", "Unchecking Blanks in Excel AutoFilter hides rows with empty cells."),
        ],
        "Same filter, three tools",
        "filtered = df[df[\"region\"] == \"North\"]\nprint(filtered.head())",
        "SELECT *\nFROM sales\nWHERE region = 'North';",
        "=FILTER(A2:D100, C2:C100=\"North\")",
        "All three keep only the rows where region equals North from the same sales table — the same result, just written in a different tool.",
        "A pandas boolean filter is the same concept as a SQL WHERE clause or an Excel FILTER formula — define a condition, and only matching rows come through."
    ),

    f"{MOD01}/lesson06_creating_calculated_columns.html": (
        "If you already write calculated columns in SQL SELECT expressions or add formula columns in Excel, pandas lets you do the same — you assign a calculation to a new column name and it applies to every row at once.",
        [
            ("add a column", "fa6-solid:plus",
             "df[\"new\"] = expr", "Assigns any expression to a new column name, adding it to every row in the DataFrame.",
             "AS alias", "A SELECT expression with an alias that creates a derived field in the result set.",
             "formula column", "A new column in Excel whose cells each contain the same formula."),
            ("arithmetic", "fa6-solid:calculator",
             "+  -  *  /", "Standard operators applied to an entire column at once without writing a loop.",
             "arithmetic operators", "The +, -, *, / symbols used inside SQL column expressions.",
             "arithmetic operators", "The same +, -, *, / symbols written inside an Excel cell formula."),
            ("conditional value", "fa6-solid:toggle-on",
             "np.where()", "Assigns a different value to each row depending on whether a condition is true or false.",
             "CASE WHEN", "Returns different values for different conditions, row by row.",
             "=IF()", "The Excel function that returns one value when true and another when false."),
            ("remove a column", "fa6-solid:trash",
             "drop()", "Deletes one or more columns from the DataFrame.",
             "omit from SELECT", "Leaving a column out of the SELECT list excludes it from the result set.",
             "hide / delete column", "Hiding or right-click deleting a column removes it from the Excel sheet."),
        ],
        "Same discount calculation, three tools",
        "df[\"discount\"] = df[\"price\"] * 0.10\ndf[\"final_price\"] = df[\"price\"] - df[\"discount\"]",
        "SELECT price,\n  price * 0.10 AS discount,\n  price * 0.90 AS final_price\nFROM products;",
        "=B2*0.10         (discount in C2)\n=B2-C2           (final price in D2)",
        "All three calculate a 10% discount and the resulting final price from the same product data — the same result, just written in a different tool.",
        "Adding a calculated column in pandas uses the same arithmetic you already write in SQL SELECT expressions or Excel formula columns — just assign the result to a new column name."
    ),

    f"{MOD01}/lesson07_aggregations_group_by.html": (
        "If you already use GROUP BY in SQL or pivot tables in Excel to summarise data by category, pandas <code class=\"font-mono\">groupby()</code> does the same thing — it groups rows by a column and computes a summary for each group.",
        [
            ("group rows", "fa6-solid:object-group",
             "groupby()", "Splits the DataFrame into groups based on the unique values of a column.",
             "GROUP BY", "The SQL clause that groups rows by a column before applying aggregate functions.",
             "PivotTable row field", "The field you drag into the Rows area of a pivot table to group by that column."),
            ("total per group", "fa6-solid:calculator",
             ".sum()", "Adds up all values in a numeric column for each group.",
             "SUM()", "An aggregate function that totals a numeric column for each GROUP BY group.",
             "SUM in Values area", "The SUM aggregation you set on a value field in an Excel pivot table."),
            ("count per group", "fa6-solid:hashtag",
             ".count()", "Counts the number of non-null rows in each group.",
             "COUNT(*)", "Counts the total number of rows in each GROUP BY group.",
             "COUNT in Values area", "The COUNT aggregation set on a value field in an Excel pivot table."),
            ("multiple stats", "fa6-solid:sliders",
             ".agg()", "Calculates several different aggregations across all groups in a single call.",
             "multiple aggregates", "Listing SUM, COUNT, AVG alongside GROUP BY to compute several stats at once.",
             "multiple value fields", "Dragging several columns into the Values area of a pivot table."),
        ],
        "Same sales aggregation, three tools",
        "df.groupby(\"region\")[\"revenue\"].sum()",
        "SELECT region,\n  SUM(revenue) AS total\nFROM sales\nGROUP BY region;",
        "PivotTable: rows = Region\nvalues = SUM of Revenue",
        "All three calculate total revenue by region from the same sales data — the same result, just written in a different tool.",
        "groupby() in pandas is GROUP BY in SQL and the Rows area in a pivot table. All three split data into groups and summarise each one — the concept is identical."
    ),

    f"{MOD01}/lesson08_joining_data_merge.html": (
        "If you already join tables in SQL with JOIN or use VLOOKUP in Excel to combine two datasets, pandas <code class=\"font-mono\">merge()</code> does the same thing — it matches rows from two DataFrames on a shared key column.",
        [
            ("combine two tables", "fa6-solid:arrows-left-right",
             "merge()", "Joins two DataFrames on a matching key column and returns one combined table.",
             "JOIN", "The SQL clause that combines rows from two tables based on a matching key column.",
             "VLOOKUP / XLOOKUP", "The Excel function that looks up a key in one table and returns a column from another."),
            ("keep only matches", "fa6-solid:circle-dot",
             "how=\"inner\"", "Keeps only rows that have a matching key in both DataFrames.",
             "INNER JOIN", "Returns only rows that have a matching key in both tables.",
             "VLOOKUP exact match", "VLOOKUP returns a value only when the lookup key has an exact match."),
            ("keep all left rows", "fa6-solid:arrow-left",
             "how=\"left\"", "Keeps all rows from the left DataFrame even if there is no match on the right.",
             "LEFT JOIN", "Keeps all rows from the left table and fills NULL for unmatched right rows.",
             "IFERROR(VLOOKUP…)", "Wrapping VLOOKUP in IFERROR handles rows that have no match in the lookup table."),
            ("join key column", "fa6-solid:key",
             "on=", "The column name (or list of names) used to match rows between the two DataFrames.",
             "ON clause", "The condition defining which columns to match when joining two tables.",
             "lookup column", "The column in one table whose values are used to find matching rows in the other."),
        ],
        "Same customer join, three tools",
        "result = pd.merge(orders, customers,\n    on=\"customer_id\", how=\"left\")",
        "SELECT *\nFROM orders\nLEFT JOIN customers\n  ON orders.customer_id = customers.id;",
        "=VLOOKUP(A2, Customers!A:C, 2, FALSE)",
        "All three join the orders table with the customers table on a shared ID column — the same result, just written in a different tool.",
        "merge() is SQL JOIN and Excel VLOOKUP expressed in Python. The concept — match rows from two tables on a shared key — is exactly the same in all three tools."
    ),

    f"{MOD01}/lesson09_handling_missing_data.html": (
        "If you already handle NULL values in SQL or work with empty cells in Excel, pandas uses NaN to represent missing data — and the same three approaches apply: detect it, drop it, or fill it.",
        [
            ("detect gaps", "fa6-solid:circle-question",
             "isnull()", "Returns a True/False mask showing which cells in the DataFrame contain NaN.",
             "IS NULL", "A SQL condition that tests whether a column value is NULL.",
             "ISBLANK()", "An Excel function that returns TRUE when a cell is empty."),
            ("count gaps", "fa6-solid:hashtag",
             "isnull().sum()", "Counts the total number of missing values in each column.",
             "COUNT(*) - COUNT(col)", "The difference between total rows and non-null count gives the null tally.",
             "COUNTBLANK()", "An Excel function that counts the number of empty cells in a range."),
            ("remove rows", "fa6-solid:minus",
             "dropna()", "Deletes every row that contains at least one missing value.",
             "WHERE col IS NOT NULL", "A filter that removes rows where a column value is NULL.",
             "Filter → uncheck Blanks", "Filtering out blank rows in Excel AutoFilter, then deleting them."),
            ("fill gaps", "fa6-solid:fill",
             "fillna()", "Replaces missing values with a constant, a mean, or a forward-filled prior value.",
             "UPDATE … SET col = val", "An UPDATE statement that replaces NULL values with a specific value.",
             "=IF(ISBLANK(…), val)", "An IF formula that substitutes a default value when a cell is empty."),
        ],
        "Same missing-value check, three tools",
        "df.isnull().sum()",
        "SELECT COUNT(*) - COUNT(salary)\n  AS missing_salary\nFROM employees;",
        "=COUNTBLANK(B2:B201)",
        "All three count the number of missing salary values in the same employee table — the same result, just written in a different tool.",
        "NaN in pandas is NULL in SQL and an empty cell in Excel. The same three strategies — detect, drop, fill — apply in all three tools."
    ),

    f"{MOD01}/lesson10_exporting_data.html": (
        "If you already use SQL SELECT … INTO OUTFILE or save a workbook from Excel, pandas <code class=\"font-mono\">to_csv()</code> and <code class=\"font-mono\">to_excel()</code> do the same thing — they write a DataFrame to a file on your drive.",
        [
            ("save to CSV", "fa6-solid:file-arrow-up",
             "to_csv()", "Writes the DataFrame to a plain-text CSV file that any tool can open.",
             "SELECT … INTO OUTFILE", "Exports query results from a MySQL database into a CSV file on disk.",
             "File → Save As → .csv", "Saves the current worksheet as a plain-text CSV file from the Save As dialog."),
            ("save to Excel", "fa6-solid:file-lines",
             "to_excel()", "Saves the DataFrame as an xlsx file with column headers and typed values.",
             "n/a — use export GUI", "Most databases export to Excel via a GUI tool or management studio.",
             "File → Save As → .xlsx", "Saves the workbook as an Excel file from the Save As dialog."),
            ("drop the index", "fa6-solid:hashtag",
             "index=False", "Omits the numeric row index so it doesn't appear as an extra column in the file.",
             "no equivalent", "SQL result sets have no row index, so this issue doesn't arise in SQL.",
             "no row numbers", "Row numbers are part of Excel's grid, not part of the data when saved."),
            ("multiple sheets", "fa6-solid:layer-group",
             "ExcelWriter", "Writes multiple DataFrames to separately named sheets inside one xlsx file.",
             "n/a", "SQL writes to tables, not sheets — multiple results stay in separate tables.",
             "multiple sheet tabs", "Creating separate worksheet tabs and pasting each summary onto them manually."),
        ],
        "Same CSV export, three tools",
        "df.to_csv('results.csv', index=False)",
        "SELECT *\n  INTO OUTFILE '/tmp/results.csv'\nFROM sales;",
        "File -> Save As -> results.csv -> Save",
        "All three export the same dataset to a CSV file on disk — the same result, just written in a different tool.",
        "to_csv() in pandas is the same as Save As in Excel or SELECT INTO OUTFILE in MySQL. You have always been exporting data — pandas just automates it in a script."
    ),

    # ── MOD 02 ────────────────────────────────────────────────────────────────

    f"{MOD02}/lesson01_reading_csv_files.html": (
        "If you already import CSV data into SQL or use Excel's Data ribbon, <code class=\"font-mono\">pd.read_csv()</code> gives you fine-grained control over every part of the import — the separator, the columns you load, the encoding, and the row count.",
        [
            ("custom delimiter", "fa6-solid:grip-lines",
             "sep=", "Tells pandas which character separates values — tab, pipe, semicolon, or any string.",
             "FIELDS TERMINATED BY", "The MySQL LOAD DATA clause that specifies the value separator character.",
             "Delimiter dropdown", "The delimiter dropdown in the Excel Data import wizard."),
            ("select columns", "fa6-solid:filter",
             "usecols=", "Loads only the columns you name, skipping all others to save memory.",
             "SELECT col1, col2", "A SELECT list that names only the columns you need from the table.",
             "Column selection step", "The checkbox list in the Excel import wizard that lets you deselect unwanted columns."),
            ("file encoding", "fa6-solid:language",
             "encoding=", "Tells pandas the character encoding of the file — utf-8, latin-1, or cp1252.",
             "CHARACTER SET", "The MySQL clause that declares the character encoding of an imported file.",
             "File Origin dropdown", "The file origin setting in the Excel Text Import wizard that sets the encoding."),
            ("row limit", "fa6-solid:hashtag",
             "nrows=", "Reads only the first N rows, useful for testing on a large file quickly.",
             "LIMIT n", "Returns only the first N rows from a SQL query result.",
             "load a sample", "Manually deleting rows below the first N in Excel to work with a sample dataset."),
        ],
        "Same pipe-delimited file, three tools",
        "df = pd.read_csv('data.txt',\n    sep='|',\n    usecols=['id', 'amount'],\n    encoding='utf-8')",
        "LOAD DATA INFILE 'data.txt'\n  FIELDS TERMINATED BY '|'\n  INTO TABLE data;",
        "Data -> Get Data -> From Text/CSV\n-> Delimiter: | -> select columns -> Load",
        "All three import the same pipe-delimited file, loading only the needed columns — the same result, just written in a different tool.",
        "Every option in pd.read_csv() maps to an equivalent step in the SQL LOAD DATA statement or the Excel import wizard — the only difference is that pandas does it in code."
    ),

    f"{MOD02}/lesson02_working_with_json_files.html": (
        "If you already query structured data from a database or work with imported records in Excel, JSON is the format you'll encounter most often from APIs and web services — pandas reads it with <code class=\"font-mono\">pd.read_json()</code> or <code class=\"font-mono\">json_normalize()</code>.",
        [
            ("read flat json", "fa6-solid:code",
             "pd.read_json()", "Loads a JSON file where each record is a top-level object into a DataFrame.",
             "JSON_TABLE()", "A MySQL function that converts a flat JSON array to a tabular result set.",
             "Power Query JSON", "Excel Power Query can import a JSON file and expand it into flat columns."),
            ("nested json", "fa6-solid:diagram-project",
             "json_normalize()", "Unpacks a nested JSON field into separate flat columns using dotted key paths.",
             "JSON_EXTRACT()", "A SQL function that extracts a value from a nested path inside a JSON column.",
             "Expand nested columns", "The Power Query expand step that unfolds nested JSON objects into flat columns."),
            ("write to json", "fa6-solid:upload",
             "to_json()", "Serialises a DataFrame back to a JSON string or file.",
             "FOR JSON", "A SQL Server clause that converts query results to a JSON string.",
             "n/a", "Saving data as JSON from Excel requires a custom Power Query or VBA export step."),
            ("json orientation", "fa6-solid:sitemap",
             "orient=", "Controls the output structure — records, index, columns, split, or table.",
             "n/a", "SQL databases don't have JSON orientation modes — data maps to rows directly.",
             "records by default", 'Each row becomes one object in the JSON array when using <code class="font-mono">orient="records"</code>.'),
        ],
        "Same transaction data, three tools",
        "df = pd.read_json('transactions.json')\nprint(df.head())",
        "SELECT *\nFROM transactions\nLIMIT 5;",
        "Data -> Get Data -> From JSON\n-> transactions.json -> Expand -> Load",
        "All three load and display the same transaction data from a structured source — the same result, just written in a different tool.",
        "JSON is just another data format. Whether you use pd.read_json(), a SQL JSON function, or Excel Power Query, you are always turning structured text into a table of rows and columns."
    ),

    f"{MOD02}/lesson03_connecting_to_databases.html": (
        "If you already connect to a database using a SQL client or an Excel ODBC connector, SQLAlchemy and <code class=\"font-mono\">pd.read_sql()</code> do the same thing in Python — they open a connection, run a query, and return the data as a table.",
        [
            ("connection string", "fa6-solid:plug",
             "connection string", "A text string that encodes the database type, host, port, name, and credentials.",
             "DSN / client string", "The connection string set in a SQL client like DBeaver to identify the database.",
             "ODBC connection", "The connection string entered in Excel Data → Get Data → From ODBC."),
            ("open connection", "fa6-solid:link",
             "create_engine()", "Creates a SQLAlchemy engine object that manages the database connection pool.",
             "client connect", "The connect action in a SQL GUI client like SSMS or DBeaver.",
             "From ODBC", "The Excel Data ribbon option that opens an ODBC connection to a database."),
            ("read a table", "fa6-solid:table",
             "read_sql_table()", "Loads an entire database table into a DataFrame in one call.",
             "SELECT * FROM table", "The simplest query that returns every row and column from a database table.",
             "Data → From Table", "Selecting a database table in the Excel data connection wizard."),
            ("close connection", "fa6-solid:power-off",
             "with engine.connect()", "A context manager that automatically closes the connection when the block ends.",
             "DISCONNECT", "The command that closes an open database session in a SQL client.",
             "Close & Load", "The Excel button that closes Power Query and loads data into the worksheet."),
        ],
        "Same database table, three tools",
        "engine = create_engine(conn_str)\ndf = pd.read_sql_table('sales', engine)",
        "SELECT *\nFROM sales;",
        "Data -> Get Data -> From ODBC\n-> select sales table -> Load",
        "All three load the same database table into a row-and-column format ready for analysis — the same result, just written in a different tool.",
        "SQLAlchemy is just a connection manager — it gives pandas the same access to a database that a SQL client or an Excel ODBC connector gives you."
    ),

    f"{MOD02}/lesson04_running_sql_in_python.html": (
        "If you already run SELECT queries in a SQL client or use database connections in Excel to pull data, <code class=\"font-mono\">pd.read_sql()</code> does the same thing in Python — you write your query, pass it to the function, and get back a DataFrame.",
        [
            ("run a query", "fa6-solid:database",
             "pd.read_sql()", "Sends a SQL SELECT string to the database and returns the results as a DataFrame.",
             "SQL client query", "A query typed into DBeaver, SSMS, or any SQL client that returns results in a grid.",
             "Power Query SQL", 'The SQL statement option under Excel Data → Get Data → From Database.'),
            ("safe parameters", "fa6-solid:shield",
             "params=", "Passes filter values as a tuple or dict so they are safely escaped before being sent.",
             "parameterised query", "A prepared statement that uses placeholders instead of string-concatenated values.",
             "Power Query parameter", "A Power Query parameter that substitutes a safe value into the query string."),
            ("results as table", "fa6-solid:table",
             "result DataFrame", "Every row the database returns lands in a pandas DataFrame for immediate use.",
             "results grid", "The rows shown in the SQL client results pane after a query runs.",
             "Load to sheet", "The Excel option that puts query results into a worksheet range."),
            ("multi-table query", "fa6-solid:sitemap",
             "SQL JOIN inside string", "Joins written inside the SQL string run in the database, not in pandas memory.",
             "JOIN", "The SQL clause that combines rows from two tables based on a shared key column.",
             "multiple connections", "Using separate Excel data connections to pull from two tables without joining them."),
        ],
        "Same parameterised query, three tools",
        "df = pd.read_sql(\n    'SELECT * FROM orders WHERE year = %s',\n    engine, params=(2024,))",
        "SELECT *\nFROM orders\nWHERE year = 2024;",
        "Data -> From Database\n-> SQL: SELECT * FROM orders\n->   WHERE year = 2024 -> Load",
        "All three run the same filtered query against the orders table and return only 2024 rows — the same result, just written in a different tool.",
        "The SQL inside pd.read_sql() is identical to what you'd type in a SQL client or paste into an Excel data connection — pd.read_sql() is just the Python driver."
    ),

    f"{MOD02}/lesson05_writing_data_back_to_a_database.html": (
        "If you already use SQL INSERT statements or an Excel export-to-database tool to write data back to a table, pandas <code class=\"font-mono\">to_sql()</code> does the same thing — it pushes every row of a DataFrame into a database table.",
        [
            ("write rows", "fa6-solid:upload",
             "to_sql()", "Inserts every row of the DataFrame into a database table with one call.",
             "INSERT INTO", "The SQL statement that adds new rows to an existing database table.",
             "Export to database", "The Access export feature or ODBC write step that writes rows to a database table."),
            ("replace table", "fa6-solid:rotate",
             "if_exists=\"replace\"", "Drops the existing table and creates a fresh one with the DataFrame contents.",
             "TRUNCATE then INSERT", "Empties the table first, then inserts all rows from the new dataset.",
             "delete rows then paste", "Clearing all data from a sheet then pasting in the new dataset."),
            ("append rows", "fa6-solid:plus",
             "if_exists=\"append\"", "Adds the DataFrame rows to the end of the existing table without deleting anything.",
             "INSERT INTO (append)", "An INSERT statement that adds rows to a table without modifying existing rows.",
             "paste below last row", "Pasting new rows directly below the existing data in an Excel table."),
            ("auto-create table", "fa6-solid:table",
             "auto-created", "If the target table does not exist, to_sql() creates it from the DataFrame schema.",
             "CREATE TABLE", "The SQL statement that defines a new table structure before inserting rows.",
             "n/a", "Excel doesn't auto-create database tables — you must define the schema first."),
        ],
        "Same data write, three tools",
        "df.to_sql('results', engine,\n    if_exists='replace',\n    index=False)",
        "TRUNCATE TABLE results;\nINSERT INTO results\nSELECT * FROM staging;",
        "n/a -- Excel writes to its own format;\nexport to database requires a plugin.",
        "All three write a dataset into a target table, replacing any existing rows — the same result, just written in a different tool.",
        "to_sql() is the Python equivalent of clicking INSERT in a SQL client or pasting data into a table. The if_exists parameter is the Python way of deciding whether to overwrite or extend."
    ),

    f"{MOD02}/lesson06_managing_credentials_env.html": (
        "If you already hide database passwords in a SQL client's saved connection or an Excel ODBC profile, a .env file does the same thing — it stores sensitive values outside your code so they never appear in a shared script.",
        [
            ("store credentials", "fa6-solid:lock",
             ".env file", "A plain-text file of KEY=VALUE pairs stored outside your project code folder.",
             "saved connection", "A password stored in a SQL client's connection manager, not in a query file.",
             "stored ODBC password", "A password saved inside the Excel Data → From ODBC connection settings."),
            ("load credentials", "fa6-solid:gear",
             "load_dotenv()", "Reads the .env file and makes every variable available via <code class=\"font-mono\">os.getenv()</code>.",
             "connection profile", "The saved profile a SQL client loads automatically when you open the client.",
             "stored ODBC DSN", "The ODBC data source that holds the connection string and credentials for Excel."),
            ("read a variable", "fa6-solid:key",
             "os.getenv()", "Returns the value of an environment variable by name, or None if it is not set.",
             "n/a", "SQL client tools read credentials from their own connection store, not env variables.",
             "n/a", "Excel reads ODBC credentials automatically with no getenv() equivalent."),
            ("keep out of git", "fa6-solid:shield",
             ".gitignore", "Adding .env to .gitignore prevents the credentials file from ever reaching a repository.",
             "n/a", "SQL connection files are stored locally — never commit passwords to any shared file.",
             "n/a", "Excel ODBC connections are local and never committed to a code repository."),
        ],
        "Same connection string, three tools",
        "load_dotenv()\nconn = os.getenv('DB_CONN')\nengine = create_engine(conn)",
        "-- Stored in DBeaver connection profile:\n-- host=db.corp.com user=analyst",
        "Data -> ODBC connection -> saved DSN\n(password stored outside workbook)",
        "All three read the database connection credentials from a secure location outside the code — the same approach, just in a different tool.",
        "A .env file is the Python equivalent of a saved SQL client connection or an Excel ODBC profile — the password lives outside your code so it never ends up in a shared file."
    ),

    # ── MOD 03 ────────────────────────────────────────────────────────────────

    f"{MOD03}/lesson01_why_analysts_use_python.html": (
        "If you already automate data tasks with SQL stored procedures or Excel macros, Python does the same things — and more. It connects to databases, processes files, calculates results, and delivers reports without you clicking anything.",
        [
            ("automate a task", "fa6-solid:rotate",
             "Python script", "A .py file that runs every data step from top to bottom without human input.",
             "stored procedure", "A named block of SQL that the database runs on demand or on a schedule.",
             "Excel macro (VBA)", "A recorded or written VBA procedure that runs inside an Excel workbook."),
            ("connect to data", "fa6-solid:plug",
             "pandas + SQLAlchemy", "Python libraries that read CSVs, Excel files, and databases in the same script.",
             "database session", "The SQL session that grants access to tables and views in a database.",
             "Data → Get Data", "The Excel ribbon option that connects to databases, files, and web sources."),
            ("schedule it", "fa6-solid:clock",
             "Task Scheduler / cron", "An OS scheduler that runs a Python script at a set time with no user action.",
             "SQL Agent job", "A SQL Agent job that runs a stored procedure on a defined schedule.",
             "macro on open", "A macro set to run on workbook open — but it requires someone to open the file."),
            ("scale to any size", "fa6-solid:bolt",
             "unlimited rows", "Pandas and Python handle millions of rows with no hard row limit.",
             "unlimited rows", "SQL databases hold billions of rows by design with no practical row limit.",
             "1,048,576 row limit", "Excel is capped at just over one million rows per worksheet."),
        ],
        "Same daily report, three tools",
        "df = pd.read_csv('sales.csv')\nsummary = df.groupby('region')['revenue'].sum()\nsummary.to_excel('report.xlsx')",
        "SELECT region, SUM(revenue) AS total\nFROM sales\nGROUP BY region;",
        "PivotTable: rows = Region\nvalues = SUM of Revenue\n(manually refresh daily)",
        "All three produce a revenue-by-region summary from the same sales data — the same result, just written in a different tool.",
        "Python does not replace SQL or Excel — it combines both. Any analysis you can do in a SQL query or Excel pivot table can be scripted in Python and run automatically."
    ),

    f"{MOD03}/lesson02_replacing_excel_workflows_with_python.html": (
        "If you already use VLOOKUP, pivot tables, and multi-sheet workbooks in Excel, pandas does the same things in code — <code class=\"font-mono\">merge()</code> replaces VLOOKUP, <code class=\"font-mono\">groupby()</code> replaces pivot tables, and <code class=\"font-mono\">ExcelWriter</code> handles multi-sheet reports.",
        [
            ("lookup values", "fa6-solid:magnifying-glass",
             "merge()", "Matches rows from two DataFrames on a key column — the code equivalent of VLOOKUP.",
             "JOIN", "The SQL clause that combines rows from two tables based on a shared key value.",
             "VLOOKUP / XLOOKUP", "The Excel function that looks up a key and returns a field from a second table."),
            ("pivot summary", "fa6-solid:table-cells-large",
             "groupby().agg()", "Groups rows by a column and computes totals, counts, or averages — like a pivot table.",
             "GROUP BY", "The SQL clause that groups rows and applies aggregate functions to each group.",
             "PivotTable", "The Excel feature that groups data by a field and computes summaries in a grid."),
            ("multi-sheet report", "fa6-solid:layer-group",
             "ExcelWriter", "Writes multiple DataFrames to separately named sheets in a single xlsx file.",
             "n/a", "SQL writes to tables, not workbook sheets — multi-sheet output needs a reporting tool.",
             "multiple sheet tabs", "Manually creating tabs and pasting a summary onto each sheet by hand."),
            ("loop over files", "fa6-solid:rotate",
             "for loop", "Loops over a list of files and applies the same operations to each one automatically.",
             "batch stored proc", "A SQL Agent job that calls a stored procedure once per file in a loop.",
             "manual open & paste", "Opening each file manually in Excel and repeating the same steps every time."),
        ],
        "Same VLOOKUP join, three tools",
        "result = pd.merge(orders, prices,\n    on='product_id', how='left')",
        "SELECT o.*, p.price\nFROM orders o\nLEFT JOIN prices p\n  ON o.product_id = p.id;",
        "=VLOOKUP(A2, Prices!A:B, 2, FALSE)",
        "All three join the orders table with the prices table on a product ID to add the unit price — the same result, just written in a different tool.",
        "Every Excel workflow you already build — lookup, pivot, multi-sheet export — has a direct pandas equivalent that runs in a script without opening Excel at all."
    ),

    f"{MOD03}/lesson03_using_python_with_sql_queries.html": (
        "If you already write queries in a SQL client or paste SQL into an Excel data connection, <code class=\"font-mono\">pd.read_sql()</code> runs the exact same query in Python and returns the result as a DataFrame you can keep working with.",
        [
            ("run a query", "fa6-solid:database",
             "pd.read_sql()", "Sends a SQL string to the database and returns the results as a DataFrame.",
             "SQL client query", "A query typed or pasted into DBeaver, SSMS, or any SQL client tool.",
             "Data → From Database", "The Excel equivalent that runs a SQL statement and loads results into a sheet."),
            ("safe parameters", "fa6-solid:shield",
             "params=", "Passes filter values separately so they are escaped before insertion into the query.",
             "parameterised query", "A prepared statement that uses %s or ? placeholders instead of string values.",
             "Power Query parameter", "A Power Query parameter that substitutes a safe value into the query string."),
            ("organise queries", "fa6-solid:folder",
             "query variables", "Storing SQL strings in labelled Python variables keeps script code clean and readable.",
             "named views", "Saving a query as a view gives it a name so it can be reused without repetition.",
             "named Power Query", "A named Power Query in Excel that can be reused across multiple worksheets."),
            ("post-process results", "fa6-solid:sliders",
             "pandas methods", "The DataFrame from read_sql can immediately be filtered, pivoted, or exported.",
             "CTE / subquery", "A CTE lets you query the output of another query in the same SQL statement.",
             "Power Query steps", "Transform steps applied to data in Power Query after it loads from the database."),
        ],
        "Same filtered query, three tools",
        "df = pd.read_sql(\n    'SELECT * FROM sales WHERE year = %s',\n    engine, params=(2024,))",
        "SELECT *\nFROM sales\nWHERE year = 2024;",
        "Data -> From Database\n-> SQL: SELECT * FROM sales\n->   WHERE year = 2024 -> Load",
        "All three filter sales rows to show only 2024 data from the same database table — the same result, just written in a different tool.",
        "The SQL inside pd.read_sql() is identical to what you'd type in a client tool or paste into an Excel connection — Python is just the driver."
    ),

    f"{MOD03}/lesson04_automating_repetitive_data_tasks.html": (
        "If you already run the same SQL query every Monday or open the same Excel file to refresh a report, Python automation replaces that manual step — a script does the work on a schedule and delivers the same output without you touching it.",
        [
            ("find the task", "fa6-solid:magnifying-glass",
             "repeating script", "Any task you run manually more than once a week with the same steps is a candidate for automation.",
             "scheduled job", "A repeating job in SQL Agent that runs a stored procedure at a set time.",
             "macro or refresh", "An Excel macro or refresh schedule that runs the same steps on a fixed timetable."),
            ("loop over files", "fa6-solid:rotate",
             "for file in files", "A Python loop that opens, processes, and saves every file in a folder automatically.",
             "cursor loop", "A SQL cursor that iterates over a result set and applies the same logic to each row.",
             "manual open loop", "Opening each file in Excel and repeating the same steps — no automation involved."),
            ("schedule it", "fa6-solid:clock",
             "Task Scheduler / cron", "The OS scheduler that runs a Python script at a set time without any user action.",
             "SQL Agent schedule", "A SQL Agent job that runs a stored procedure on a defined schedule.",
             "Workbook open macro", "An Excel macro on Workbook_Open — but it still requires someone to open the file."),
            ("log results", "fa6-solid:list",
             "log file", "A text file the script appends to after every run, recording the time and outcome.",
             "SQL Agent history", "The SQL Server job history log that records when a job ran and whether it succeeded.",
             "manual log sheet", "An Excel sheet where you manually note the date and outcome of each run."),
        ],
        "Same folder loop, three tools",
        "from pathlib import Path\nfor f in Path('reports/').glob('*.csv'):\n    pd.read_csv(f).to_excel(f.with_suffix('.xlsx'))",
        "-- SQL Agent calls a stored proc\n-- once per file in the folder",
        "Manually open each .csv\nand Save As .xlsx\none file at a time",
        "All three process a folder of CSV files and convert them to Excel format — the same result, just written in a different tool.",
        "Any task you do the same way every time is a candidate for automation. A Python loop replaces the manual steps you currently perform in a SQL client or Excel."
    ),

    f"{MOD03}/lesson05_building_a_simple_reporting_script.html": (
        "If you already build reports by running SQL queries and pasting results into Excel, a Python reporting script does the same thing — it queries data, calculates summaries, and writes a formatted xlsx file, automatically.",
        [
            ("structure the script", "fa6-solid:sitemap",
             "load → transform → export", "Splitting the script into labelled sections keeps each step visible and easy to maintain.",
             "proc with sections", "Breaking a stored procedure into named comment sections for readability.",
             "raw / calc / report sheets", "Using separate worksheet tabs in Excel to hold raw data, calculations, and the final report."),
            ("format numbers", "fa6-solid:pen",
             ".round()", "Rounds numeric columns to a set number of decimal places before exporting.",
             "ROUND()", "The SQL function that rounds a numeric value to a specified number of decimals.",
             "=ROUND()", "The Excel function that rounds a cell value to a set number of decimal places."),
            ("export multi-sheet", "fa6-solid:layer-group",
             "ExcelWriter", "Writes each summary DataFrame to a separately named sheet inside one xlsx file.",
             "n/a", "SQL writes to tables — generating a multi-sheet Excel file needs external tools.",
             "multiple sheet tabs", "Creating separate worksheet tabs and pasting each summary manually."),
            ("summary statistics", "fa6-solid:chart-bar",
             ".describe()", "Returns count, mean, min, max, and percentiles for every numeric column.",
             "aggregate SELECT", "A SELECT with SUM, AVG, MIN, MAX that summarises numeric columns.",
             "=AVERAGE(), =MAX()", "Excel functions that compute individual summary statistics in formula cells."),
        ],
        "Same monthly summary, three tools",
        "summary = df.groupby('month')['revenue'].sum()\nsummary.to_excel('report.xlsx', index=False)",
        "SELECT month,\n  SUM(revenue) AS total\nFROM sales\nGROUP BY month;",
        "PivotTable: rows = Month\nvalues = SUM of Revenue\n-> paste into report sheet",
        "All three produce a monthly revenue summary from the same sales data — the same result, just written in a different tool.",
        "A reporting script is just a SQL query plus an Excel export step, written in Python and run without touching a keyboard. Every step you do manually in a SQL client and Excel can be automated."
    ),

    f"{MOD03}/lesson06_automating_reports_end_to_end.html": (
        "If you already run a SQL query, paste the results into Excel, and email the file every week, Python end-to-end automation does all three steps in one script — query, format, and deliver — without any manual action.",
        [
            ("connect the steps", "fa6-solid:link",
             "pipeline functions", "Splitting a script into functions where each one passes its output to the next.",
             "multi-step proc", "A stored procedure that calls sub-procedures in sequence to complete a workflow.",
             "macro sequence", "A VBA macro that calls other sub-procedures in order to run a multi-step process."),
            ("handle errors", "fa6-solid:shield",
             "try / except", "Catches any failure and writes the error to a log without stopping the whole script.",
             "TRY / CATCH", "A SQL Server error-handling block that catches exceptions in a stored procedure.",
             "On Error GoTo", "The VBA error handler that redirects execution to an error-handling section on failure."),
            ("send by email", "fa6-solid:envelope",
             "smtplib", "Python's built-in email library that attaches a file and delivers it via an SMTP server.",
             "Database Mail", "SQL Server's built-in feature that sends emails with attachments from a stored procedure.",
             "Outlook VBA", "A VBA script that uses the Outlook object model to attach and send the Excel file."),
            ("schedule and log", "fa6-solid:clock",
             "cron / Task Scheduler", "The OS scheduler that runs the whole pipeline on a timer and records the outcome.",
             "SQL Agent schedule", "A SQL Agent job schedule that triggers the stored procedure at a set time.",
             "Workbook open event", "A VBA Workbook_Open event that starts the macro — but only when someone opens the file."),
        ],
        "Same weekly report pipeline, three tools",
        "df = load_data()\nreport = build_report(df)\nsend_email(report, 'team@corp.com')",
        "EXEC sp_RunReport;\nEXEC sp_SendReportEmail;",
        "Manually run macro -> refresh pivot\n-> save xlsx -> email via Outlook",
        "All three generate and deliver the same weekly report — the same workflow, just written in a different tool.",
        "An end-to-end Python pipeline does everything you already do manually — query, format, and send — in a single script that runs on a schedule with no human input required."
    ),

    # ── MOD 04 ────────────────────────────────────────────────────────────────

    f"{MOD04}/lesson02_memory_optimization.html": (
        "If you already optimise SQL queries to scan fewer columns or format Excel columns as integers to reduce file size, pandas memory optimisation works the same way — it reduces the bytes each column uses so your script can handle larger datasets.",
        [
            ("check memory use", "fa6-solid:memory",
             "memory_usage()", "Reports the number of bytes each column occupies in the DataFrame.",
             "sp_spaceused", "A SQL Server command that shows how much disk space a table occupies.",
             "workbook file size", "The file size shown in Windows Explorer or the Excel title bar."),
            ("downcast numbers", "fa6-solid:compress",
             "pd.to_numeric(downcast=)", "Converts a column to the smallest integer or float type that still holds all values.",
             "SMALLINT / TINYINT", "Using a smaller integer type in SQL instead of INT when values are small.",
             "format as integer", "Setting a column format in Excel to Integer to reduce stored decimal precision."),
            ("categorical columns", "fa6-solid:tags",
             "astype(\"category\")", "Converts a repeated-string column to a type that stores each unique string only once.",
             "ENUM / lookup table", "An ENUM or indexed lookup table in SQL where each unique string is stored once.",
             "dropdown list column", "An Excel column with a data-validation dropdown list that uses a short code per value."),
            ("measure improvement", "fa6-solid:ruler",
             "before / after compare", "Call <code class=\"font-mono\">memory_usage()</code> before and after optimisation to measure the saving.",
             "sp_spaceused before/after", "Running sp_spaceused before and after a schema change to measure the byte savings.",
             "file size before/after", "Saving the workbook before and after changing column formats to compare sizes."),
        ],
        "Same employee table, less memory",
        "df['dept_id'] = pd.to_numeric(\n    df['dept_id'], downcast='integer')\ndf['region'] = df['region'].astype('category')",
        "ALTER TABLE employees\n  MODIFY dept_id SMALLINT,\n  MODIFY region ENUM('North','South');",
        "Format column as Integer\nUse a dropdown list for region\n(reduces stored data volume)",
        "All three reduce the memory used by the employee table by choosing smaller types for each column — the same goal, just expressed in a different tool.",
        "Every byte you save in a pandas column is a byte the database already avoids by using the right data type. The principle is identical — smaller types mean faster, leaner data."
    ),

    f"{MOD04}/lesson03_chunk_processing.html": (
        "If you already process SQL data in batches using LIMIT and OFFSET, or split a large Excel workbook into smaller sheets, pandas chunk processing uses the same idea — it reads the file in fixed-size batches so you never load more than you need at once.",
        [
            ("why chunks", "fa6-solid:triangle-exclamation",
             "MemoryError", "Python crashes with MemoryError when a file is larger than available RAM.",
             "cursor fetch batches", "A SQL cursor using FETCH NEXT N ROWS processes results in controlled batches.",
             "split workbook", "Splitting a large Excel file into smaller workbooks to avoid performance problems."),
            ("read in chunks", "fa6-solid:layer-group",
             "chunksize=", "The pd.read_csv() parameter that makes the function return an iterator over batches.",
             "LIMIT / OFFSET", "SQL clauses that return a fixed number of rows starting at a given offset position.",
             "manual split", "Copying fixed row ranges from a large sheet into separate smaller sheets."),
            ("process each chunk", "fa6-solid:rotate",
             "for chunk in reader", "A for loop that applies the same computation to each batch of rows in sequence.",
             "cursor loop", "A SQL cursor loop that performs the same operation on each batch of fetched rows.",
             "loop over sheets", "A VBA loop that iterates over each worksheet and applies the same processing steps."),
            ("combine results", "fa6-solid:object-group",
             "pd.concat()", "Merges a list of partial results into one complete output after all chunks are processed.",
             "UNION ALL", "A SQL operator that stacks rows from multiple result sets into a single result.",
             "copy / paste rows", "Manually copying each sheet result and pasting them below each other."),
        ],
        "Same large file, three tools",
        "results = []\nfor chunk in pd.read_csv('big.csv',\n        chunksize=100_000):\n    results.append(chunk['amount'].sum())",
        "SELECT SUM(amount)\nFROM big_table;",
        "File too large for Excel.\nSplit into smaller files\nbefore processing.",
        "All three calculate the total amount from a large dataset — the same goal, though Excel cannot open the file directly.",
        "Chunk processing in pandas is the same philosophy as LIMIT/OFFSET in SQL — process a manageable slice at a time so the system never runs out of memory."
    ),

    f"{MOD04}/lesson04_processing_millions_of_rows.html": (
        "If you already write optimised SQL that avoids full table scans, or use Excel array formulas to speed up calculations, pandas vectorisation uses the same idea — it calculates across every row at once using compiled C code instead of a Python loop.",
        [
            ("slow approach", "fa6-solid:hourglass",
             "for loop row-by-row", "Iterating row by row in Python is slow because each step goes through the interpreter.",
             "cursor row-by-row", "A SQL cursor that processes one row at a time is much slower than a set-based query.",
             "nested IF formulas", "Complex nested Excel formulas that recalculate every individual cell."),
            ("fast approach", "fa6-solid:bolt",
             "vectorised operation", "A pandas expression applied to an entire column at once using compiled NumPy code.",
             "set-based query", "A SQL query that computes results for all rows in a single, optimised operation.",
             "array formula", "An Excel formula wrapped in Ctrl+Shift+Enter that processes a whole range at once."),
            ("custom logic", "fa6-solid:gear",
             ".apply()", "Applies a Python function row by row when no vectorised alternative is available.",
             "scalar function", "A user-defined SQL function applied to each row during query execution.",
             "helper column", "A temporary Excel column that breaks a complex formula into simpler per-row steps."),
            ("benchmark it", "fa6-solid:stopwatch",
             "time.time()", "Records wall-clock seconds before and after a block to measure its elapsed time.",
             "SET STATISTICS TIME ON", "A SQL Server option that reports elapsed and CPU time for each query.",
             "Evaluate Formula", "The Excel tool that steps through formula logic but cannot measure execution time."),
        ],
        "Same discount on millions of rows, three tools",
        "df['discounted'] = df['price'] * 0.9\n# ~30ms for 5 million rows",
        "SELECT price * 0.9 AS discounted\nFROM products;",
        "=B2*0.9  (drag down 5M rows)\n-- not practical at this scale",
        "All three calculate a 10% discount across every row in a large product table — the same result, just written in a different tool.",
        "Pandas vectorisation is the same principle as a set-based SQL query — compute the result for every row at once rather than one row at a time."
    ),

    f"{MOD04}/lesson05_columnar_storage.html": (
        "If you already know that SQL indexes speed up queries by avoiding full table scans, columnar storage uses the same idea at the file level — data for each column is stored together, so a query that touches two columns reads only those two column blocks.",
        [
            ("row vs columnar files", "fa6-solid:grip-lines",
             "row-oriented CSV", "A CSV stores every column of row 1, then every column of row 2 — you read all columns even if you need one.",
             "row-oriented table", "A traditional database table stores all columns for each row together on a data page.",
             "row-based sheet", "An Excel worksheet stores all column values per row — reading one column still loads the whole row."),
            ("skip unneeded columns", "fa6-solid:bolt",
             "columnar read", "A columnar file physically skips column blocks you did not request, saving read time.",
             "index scan", "A SQL index lets the engine skip rows and pages that don't match the query condition.",
             "n/a", "Hiding a column in Excel only hides it visually — the data is still loaded into memory."),
            ("columnar formats", "fa6-solid:cube",
             "Parquet / ORC", "The two most common columnar formats that pandas can read and write natively.",
             "n/a", "SQL databases use their own engine storage format — they don't produce Parquet files.",
             "n/a", "Excel does not support Parquet or ORC — they require Python, Power BI, or a BI tool."),
            ("compression benefit", "fa6-solid:compress",
             "built-in compression", "Parquet compresses each column independently, making files far smaller than CSV.",
             "tablespace compression", "Databases can compress data blocks, but this is a database-admin configuration.",
             "xlsx compression", "Excel's xlsx is a zipped XML file, but it is not optimised per column like Parquet."),
        ],
        "Same sales data, three storage formats",
        "df.to_parquet('sales.parquet')\ndf2 = pd.read_parquet('sales.parquet',\n    columns=['region', 'revenue'])",
        "SELECT region, revenue\nFROM sales;",
        "n/a -- Parquet is not supported\nin Excel natively",
        "All three access only the region and revenue columns from the same sales data — but columnar Parquet reads far less disk data than CSV.",
        "Columnar storage is the file-level version of a SQL column index — both exist to avoid reading data you don't need. If you understand why indexes speed up SQL, you understand why Parquet is faster than CSV."
    ),

    f"{MOD04}/lesson06_parquet_files.html": (
        "If you already know that saving a SQL table to CSV loses type information and produces large plain-text files, Parquet solves both problems — it preserves column types and compresses the data, so files are smaller and load faster.",
        [
            ("write to parquet", "fa6-solid:download",
             "to_parquet()", "Saves a DataFrame to a compressed binary Parquet file that preserves all column types.",
             "n/a — needs Python/Spark", "Most databases don't write Parquet directly — you need a Python or Spark export step.",
             "n/a", "Excel cannot save a file as Parquet format."),
            ("read parquet", "fa6-solid:file-lines",
             "pd.read_parquet()", "Loads a Parquet file into a DataFrame, restoring all column types from its metadata.",
             "n/a", "SQL databases don't read Parquet natively — you query the database table instead.",
             "n/a", "Excel cannot open Parquet files — they require Python, Power BI, or a BI tool."),
            ("column selection", "fa6-solid:filter",
             "columns=", "Loads only the columns you name, physically skipping all others in the file.",
             "SELECT col1, col2", "Returns only the named columns, but still scans the full row on disk.",
             "hide / select columns", "Selecting specific columns in Excel still loads the entire file into memory first."),
            ("parquet vs csv", "fa6-solid:scale-balanced",
             "smaller and typed", "Parquet files are typically 50–80% smaller than CSV and restore types without re-parsing.",
             "database table", "A database table already stores typed data efficiently — Parquet is its file-level equivalent.",
             "xlsx format", "Excel's xlsx format is smaller than CSV but not as optimised for analytics as Parquet."),
        ],
        "Same sales data — CSV vs Parquet",
        "df.to_parquet('sales.parquet')\ndf2 = pd.read_parquet('sales.parquet')",
        "SELECT *\nFROM sales; -- data typed in DB",
        "File -> Save As -> .xlsx\n(no Parquet option available)",
        "All three persist and reload the same sales data — Parquet preserves types and is far smaller than the CSV equivalent.",
        "Parquet is the file version of a typed database table. If you already store data in a database to preserve types and save space, Parquet gives you the same benefits when you work with files."
    ),

    f"{MOD04}/lesson13_performance_profiling.html": (
        "If you already use SQL execution plans or Excel formula auditing to find what is slow, Python profiling tools do the same thing — they measure exactly where your script spends its time so you fix the right line.",
        [
            ("measure elapsed time", "fa6-solid:stopwatch",
             "time.time()", "Records wall-clock seconds before and after a block to measure its elapsed duration.",
             "SET STATISTICS TIME ON", "A SQL Server setting that reports elapsed and CPU time for each statement.",
             "manual timer", "Starting a stopwatch manually before a calculation in Excel is not practical at scale."),
            ("profile all functions", "fa6-solid:magnifying-glass",
             "cProfile", "Runs the entire script and ranks every function call by total execution time.",
             "execution plan", "A SQL execution plan that ranks each operation by its share of total query cost.",
             "Evaluate Formula", "The Excel tool that steps through a formula but cannot measure actual run time."),
            ("line-level timing", "fa6-solid:list-check",
             "line_profiler", "Times each individual line inside a chosen function to find the exact slow statement.",
             "query hints / trace", "A SQL Server trace that exposes per-operation timing deep inside a query.",
             "n/a", "Excel has no line-level timing tool for formula evaluation."),
            ("fix and verify", "fa6-solid:bolt",
             "benchmark before/after", "Run the same timing measurement after each fix to confirm the performance improved.",
             "before/after plan compare", "Comparing execution plans before and after adding an index or rewriting a query.",
             "before/after calc time", "Measuring workbook calculation time before and after simplifying a formula."),
        ],
        "Same slow script, three profiling approaches",
        "import cProfile\ncProfile.run('process_data(df)')\n# shows per-function time ranking",
        "SET STATISTICS TIME ON;\nSELECT * FROM sales\nWHERE year = 2024;",
        "Formulas -> Evaluate Formula\n(steps through logic but not timed)",
        "All three help you understand where computation time is spent in the same data operation — the same goal, just measured in a different tool.",
        "Profiling in Python is the same discipline as reading a SQL execution plan — identify the expensive step, fix it, then measure again to confirm the gain. Always profile before you optimise."
    ),
}


# ── Apply ─────────────────────────────────────────────────────────────────────

ok = fail = 0

for rel_path, (intro, rows, divider, py_code, sql_code, xl_code, caption, tip) in LESSONS.items():
    abs_path = os.path.join(ROOT, rel_path.replace("/", os.sep))
    if not os.path.exists(abs_path):
        print(f"  ❌ FILE NOT FOUND: {rel_path}")
        fail += 1
        continue

    html = open(abs_path, encoding="utf-8").read()
    new_section = build_section(intro, rows, divider, py_code, sql_code, xl_code, caption, tip)
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
